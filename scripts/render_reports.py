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

CSS_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

:root {
  --primary-color: #2563eb;
  --text-color: #1e293b;
  --bg-color: #ffffff;
  --border-color: #e2e8f0;
  --code-bg: #f8fafc;
  --table-stripe: #f8fafc;
  --accent-color: #0284c7;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.65;
  color: var(--text-color);
  background-color: var(--bg-color);
  max-width: 960px;
  margin: 0 auto;
  padding: 40px 24px;
}

h1, h2, h3, h4, h5, h6 {
  color: #0f172a;
  font-weight: 700;
  margin-top: 1.8em;
  margin-bottom: 0.6em;
  line-height: 1.25;
}

h1 {
  font-size: 2.2rem;
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 0.4em;
  margin-top: 0.5em;
  color: #1e3a8a;
}

h2 {
  font-size: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.3em;
}

h3 { font-size: 1.25rem; }
h4 { font-size: 1.1rem; }

p, ul, ol {
  margin-top: 0;
  margin-bottom: 1em;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5em 0;
  font-size: 0.95rem;
}

th, td {
  border: 1px solid var(--border-color);
  padding: 10px 14px;
  text-align: left;
}

th {
  background-color: #f1f5f9;
  font-weight: 600;
  color: #334155;
}

tr:nth-child(even) {
  background-color: var(--table-stripe);
}

blockquote {
  border-left: 4px solid var(--primary-color);
  margin: 1.2em 0;
  padding: 10px 18px;
  background-color: #eff6ff;
  color: #1e40af;
  border-radius: 0 6px 6px 0;
}

code {
  font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
  font-size: 0.88em;
  background-color: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--border-color);
}

pre {
  background-color: #0f172a;
  color: #f8fafc;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
  font-size: 0.9rem;
  line-height: 1.5;
}

pre code {
  background-color: transparent;
  color: inherit;
  padding: 0;
  border: none;
}

hr {
  border: 0;
  border-top: 1px solid var(--border-color);
  margin: 2em 0;
}

.mermaid {
  background-color: #f8fafc;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 20px;
  margin: 1.5em 0;
  text-align: center;
}

.rendered-footer {
  margin-top: 40px;
  padding-top: 16px;
  border-top: 1px solid var(--border-color);
  font-size: 0.85rem;
  color: #64748b;
  text-align: center;
}

@media print {
  body {
    max-width: 100%;
    padding: 10mm;
    font-size: 11pt;
  }
  pre, table {
    page-break-inside: avoid;
  }
  .rendered-footer {
    display: none;
  }
}
"""

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
        # First protect already escaped or tags? We escape raw characters
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
        return text

    for line in lines:
        stripped = line.strip()

        # Code block marker
        if stripped.startswith("```"):
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
            in_table = True
            table_buffer.append(stripped)
            continue
        elif in_table:
            html_lines.append(flush_table())

        # Empty line
        if not stripped:
            html_lines.append("")
            continue

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

        # Bullet lists
        if re.match(r'^[-*+]\s+(.*)$', stripped):
            item_text = format_inline(re.sub(r'^[-*+]\s+', '', stripped))
            html_lines.append(f"<ul><li>{item_text}</li></ul>")
            continue

        # Numbered lists
        if re.match(r'^\d+\.\s+(.*)$', stripped):
            item_text = format_inline(re.sub(r'^\d+\.\s+', '', stripped))
            html_lines.append(f"<ol><li>{item_text}</li></ol>")
            continue

        # Regular paragraph
        html_lines.append(f"<p>{format_inline(stripped)}</p>")

    if in_table:
        html_lines.append(flush_table())

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


def render_file(file_path):
    base_name = os.path.basename(file_path)
    file_stem, _ = os.path.splitext(base_name)
    out_html = os.path.join(OUTPUT_DIR, f"{file_stem}.html")
    out_pdf = os.path.join(OUTPUT_DIR, f"{file_stem}.pdf")

    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Thử kiểm tra xem có pandoc không
    has_pandoc = shutil.which("pandoc") is not None

    if has_pandoc:
        print(f"📄 [Pandoc] Đang render: {base_name} -> HTML...")
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
            print(f"  ✅ Đã tạo: {out_html}")
        except Exception as e:
            print(f"  ⚠️ Pandoc gặp lỗi ({e}), chuyển sang bộ render Python dự phòng...")
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
    else:
        # Không có PDF engine cài sẵn, ghi nhận hướng dẫn
        pass


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target_files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".md")]
    target_files.sort()

    if not target_files:
        print("❌ Không tìm thấy file markdown nào trong thư mục reports/.")
        sys.exit(1)

    print(f"🚀 Bắt đầu quá trình render {len(target_files)} báo cáo từ Markdown...")
    print(f"📂 Thư mục nguồn: {REPORTS_DIR}")
    print(f"📂 Thư mục đầu ra: {OUTPUT_DIR}\n")

    for tf in target_files:
        src = os.path.join(REPORTS_DIR, tf)
        render_file(src)

    print("\n✨ Quá trình render hoàn tất!")
    print("💡 Mẹo: Bạn có thể mở các file .html trong trình duyệt và chọn 'In' -> 'Lưu dưới dạng PDF' để có bản in PDF chuẩn nộp bài.")


if __name__ == "__main__":
    main()
