#!/usr/bin/env python3
"""
scripts/render_reports.py
Render các file Markdown (.md) trong thư mục reports/ sang HTML tự chứa (self-contained)
và PDF (nếu hệ thống có sẵn engine hỗ trợ như pandoc, weasyprint, wkhtmltopdf, hoặc headless Chrome).
Hỗ trợ đầy đủ tiếng Việt (UTF-8), bảng biểu, khối mã, định dạng thông báo và biểu đồ Mermaid.
"""

import sys
import os
import re
import html
import subprocess
import shutil

REPORTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))
OUTPUT_DIR = os.path.join(REPORTS_DIR, "rendered")

from template0_styles import UNIFIED_TEMPLATE0_CSS as CSS_STYLES

def simple_markdown_to_html(md_text):
    """Bộ chuyển đổi Markdown sang HTML hỗ trợ tiếng Việt, bảng biểu và mermaid."""
    lines = md_text.splitlines()
    html_lines = []
    in_code_block = False
    code_lang = ""
    code_buffer = []
    in_table = False
    table_buffer = []

    def flush_table():
        nonlocal in_table, table_buffer
        if not table_buffer:
            return ""
        out = ["<table>"]
        has_header = False
        for i, row_line in enumerate(table_buffer):
            cells = [c.strip() for c in row_line.strip().strip('|').split('|')]
            # Bỏ qua dòng phân cách dạng | --- | :---: |
            if all(re.match(r'^:?-+:?$', c) for c in cells if c):
                has_header = True
                continue
            tag = "th" if (i == 0 and not has_header) or (i == 0) else "td"
            out.append("  <tr>")
            for cell in cells:
                inline = format_inline(cell)
                out.append(f"    <{tag}>{inline}</{tag}>")
            out.append("  </tr>")
        out.append("</table>")
        in_table = False
        table_buffer = []
        return "\n".join(out)

    def format_inline(text):
        # Escape html
        text = html.escape(text)
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.+?)_', r'<em>\1</em>', text)
        # Inline code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links [text](url)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', text)
        # Restore safe inline tags
        text = text.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")
        text = text.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>").replace("&lt;br /&gt;", "<br>")
        text = text.replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>")
        text = text.replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")
        return text

    in_ul = False
    in_ol = False

    def flush_lists():
        nonlocal in_ul, in_ol
        res = []
        if in_ul:
            res.append("</ul>")
            in_ul = False
        if in_ol:
            res.append("</ol>")
            in_ol = False
        return "\n".join(res)

    for line in lines:
        stripped = line.strip()

        # Code block marker
        if stripped.startswith("```"):
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            if in_code_block:
                in_code_block = False
                code_content = html.escape("\n".join(code_buffer))
                if code_lang == "mermaid":
                    html_lines.append(f'<div class="mermaid">\n{code_content}\n</div>')
                else:
                    html_lines.append(f'<pre><code class="language-{code_lang}">{code_content}</code></pre>')
                code_buffer = []
                code_lang = ""
            else:
                if in_table:
                    html_lines.append(flush_table())
                in_code_block = True
                code_lang = stripped[3:].strip()
                code_buffer = []
            continue

        if in_code_block:
            code_buffer.append(line)
            continue

        # Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            in_table = True
            table_buffer.append(stripped)
            continue
        elif in_table:
            html_lines.append(flush_table())

        # Empty line
        if not stripped:
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            html_lines.append("")
            continue

        # Bullet lists
        m_ul = re.match(r'^[-*+]\s+(.*)$', stripped)
        if m_ul:
            if in_ol:
                html_lines.append(flush_lists())
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            item_text = format_inline(m_ul.group(1))
            html_lines.append(f"  <li>{item_text}</li>")
            continue

        # Numbered lists
        m_ol = re.match(r'^\d+\.\s+(.*)$', stripped)
        if m_ol:
            if in_ul:
                html_lines.append(flush_lists())
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            item_text = format_inline(m_ol.group(1))
            html_lines.append(f"  <li>{item_text}</li>")
            continue

        # Flush any open list before other block elements
        if in_ul or in_ol:
            html_lines.append(flush_lists())

        # Headings
        m_h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m_h:
            level = len(m_h.group(1))
            heading_text = format_inline(m_h.group(2))
            html_lines.append(f"<h{level}>{heading_text}</h{level}>")
            continue

        # Blockquote
        if stripped.startswith(">"):
            quote_text = format_inline(stripped.lstrip("> ").strip())
            html_lines.append(f"<blockquote>{quote_text}</blockquote>")
            continue

        # Horizontal Rule
        if re.match(r'^(\*{3,}|-{3,}|_{3,})$', stripped):
            html_lines.append("<hr>")
            continue

        # Regular paragraph
        html_lines.append(f"<p>{format_inline(stripped)}</p>")

    if in_table:
        html_lines.append(flush_table())
    if in_ul or in_ol:
        html_lines.append(flush_lists())

    return "\n".join(html_lines)


def build_full_html(title, body_html):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <style>
{CSS_STYLES}
  </style>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
  </script>
</head>
<body>
{body_html}
  <div class="rendered-footer">
    Báo cáo môn Nhập môn Công nghệ Phần mềm - Group 04 (HCMUS) | Tự động sinh từ Markdown sang HTML
  </div>
</body>
</html>
"""


def render_file(file_path, out_html=None, out_pdf=None):
    base_name = os.path.basename(file_path)
    file_stem, _ = os.path.splitext(base_name)
    if out_html is None:
        out_html = os.path.join(OUTPUT_DIR, f"{file_stem}.html")
    if out_pdf is None:
        out_pdf = os.path.join(OUTPUT_DIR, f"{file_stem}.pdf")

    os.makedirs(os.path.dirname(out_html), exist_ok=True)

    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Thử kiểm tra xem có pandoc không
    has_pandoc = shutil.which("pandoc") is not None

    if has_pandoc:
        pandoc_cmd = [
            "pandoc",
            file_path,
            "-o", out_html,
            "--standalone",
            "--embed-resources",
            "--metadata", f"title={file_stem}",
        ]
        try:
            subprocess.run(pandoc_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"  ✅ Đã tạo (Pandoc): {out_html}")
        except Exception:
            body = simple_markdown_to_html(md_content)
            full_html = build_full_html(file_stem, body)
            with open(out_html, "w", encoding="utf-8") as f_out:
                f_out.write(full_html)
            print(f"  ✅ Đã tạo (Python Engine): {out_html}")
    else:
        # Sử dụng bộ render Python nội bộ độc lập
        body = simple_markdown_to_html(md_content)
        full_html = build_full_html(file_stem, body)
        with open(out_html, "w", encoding="utf-8") as f_out:
            f_out.write(full_html)
        print(f"  ✅ Đã tạo (Self-contained HTML): {out_html}")

    # Kiểm tra các engine PDF nếu có
    has_wkhtmltopdf = shutil.which("wkhtmltopdf") is not None
    has_weasyprint = shutil.which("weasyprint") is not None

    if has_weasyprint:
        try:
            subprocess.run(["weasyprint", out_html, out_pdf], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"  📄 Đã xuất PDF (WeasyPrint): {out_pdf}")
        except Exception as e:
            print(f"  ⚠️ Lỗi khi xuất PDF bằng WeasyPrint: {e}")
    elif has_wkhtmltopdf:
        try:
            subprocess.run(["wkhtmltopdf", "--enable-local-file-access", out_html, out_pdf], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"  📄 Đã xuất PDF (wkhtmltopdf): {out_pdf}")
        except Exception as e:
            print(f"  ⚠️ Lỗi khi xuất PDF bằng wkhtmltopdf: {e}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target_files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".md")]
    target_files.sort()

    if not target_files:
        print("❌ Không tìm thấy file markdown nào trong thư mục reports/.")
        sys.exit(1)

    print(f"🚀 Bắt đầu quá trình render {len(target_files)} báo cáo từ reports/ sang HTML...")
    print(f"📂 Thư mục nguồn: {REPORTS_DIR}")
    print(f"📂 Thư mục đầu ra: {OUTPUT_DIR}\n")

    for tf in target_files:
        src = os.path.join(REPORTS_DIR, tf)
        render_file(src)

    # Render thư mục submit và các thư mục con
    submit_dir = os.path.join(REPORTS_DIR, "submit")
    if os.path.exists(submit_dir):
        submit_mds = []
        for root, _, files in os.walk(submit_dir):
            for f in files:
                if f.endswith(".md"):
                    submit_mds.append(os.path.join(root, f))
        submit_mds.sort()
        print(f"\n📦 Bắt đầu quá trình render {len(submit_mds)} báo cáo nộp bài trong reports/submit/...")
        for src in submit_mds:
            folder = os.path.dirname(src)
            stem, _ = os.path.splitext(os.path.basename(src))
            if "project-proposal" in src:
                try:
                    import render_proposal_template0
                    render_proposal_template0.build_template0_document()
                    print(f"  🎨 Đã render Project Proposal chuẩn Template 0: {os.path.join(folder, f'{stem}.html')}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi khi render Project Proposal bằng Template 0: {e}")
                    render_file(src, out_html=os.path.join(folder, f"{stem}.html"), out_pdf=os.path.join(folder, f"{stem}.pdf"))
            elif "git-contributions" in src:
                try:
                    import render_git_contributions_template0
                    render_git_contributions_template0.build_git_contributions_document()
                    print(f"  🎨 Đã render Git Contributions chuẩn Template 0: {os.path.join(folder, f'{stem}.html')}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi khi render Git Contributions bằng Template 0: {e}")
                    render_file(src, out_html=os.path.join(folder, f"{stem}.html"), out_pdf=os.path.join(folder, f"{stem}.pdf"))
            elif "ai-usage" in src:
                try:
                    import render_ai_usage_template0
                    render_ai_usage_template0.build_ai_usage_document()
                    print(f"  🎨 Đã render AI Usage chuẩn Template 0: {os.path.join(folder, f'{stem}.html')}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi khi render AI Usage bằng Template 0: {e}")
                    render_file(src, out_html=os.path.join(folder, f"{stem}.html"), out_pdf=os.path.join(folder, f"{stem}.pdf"))
            else:
                render_file(src, out_html=os.path.join(folder, f"{stem}.html"), out_pdf=os.path.join(folder, f"{stem}.pdf"))

    print("\n✨ Quá trình render hoàn tất!")
    print("💡 Mẹo: Bạn có thể mở các file .html trong trình duyệt và chọn 'In' -> 'Lưu dưới dạng PDF' để có bản in PDF chuẩn nộp bài.")


if __name__ == "__main__":
    main()

