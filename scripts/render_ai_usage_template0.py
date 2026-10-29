#!/usr/bin/env python3
"""
scripts/render_ai_usage_template0.py
Render Báo cáo Sử dụng AI (AI Usage Report) sang định dạng HTML tự chứa (self-contained)
áp dụng 100% phong cách Template 0 chính thức:
- Trang bìa chuẩn học thuật với tiêu đề NMCNPM - AI-Powered Helpdesk & Knowledge Base - Group 04,
  banner lớn và logo HCMUS góc dưới bên trái.
- Phân trang độc lập với thẻ .doc-page.
- Header & Footer chuẩn biểu mẫu trên từng trang nội dung.
- Bảng ma trận 11 phiên, trích dẫn chi tiết theo chuẩn quy định Khoa CNTT - HCMUS.
- Typography Times New Roman, line-height 1.5, in ấn A4 chuẩn.
"""

import os
import sys
import re
import html
import base64

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MD_FILE = os.path.join(REPO_ROOT, "reports", "submit", "ai-usage", "ai-usage.md")
OUT_HTML = os.path.join(REPO_ROOT, "reports", "submit", "ai-usage", "ai-usage.html")
LOGO_PNG = os.path.join(REPO_ROOT, "reports", "submit", "Template0-ProjectProposal.docx", "images", "image4.png")


def get_logo_base64():
    if os.path.exists(LOGO_PNG):
        with open(LOGO_PNG, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
    return ""


def get_logo_html():
    b64 = get_logo_base64()
    if b64:
        return f'<img src="{b64}" alt="HCMUS Logo">'
    return '''<svg width="55" height="55" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="display:inline-block; vertical-align:middle;">
      <circle cx="50" cy="50" r="48" fill="#00549a" stroke="#003865" stroke-width="2"/>
      <circle cx="50" cy="50" r="42" fill="#ffffff"/>
      <circle cx="50" cy="50" r="38" fill="#00549a"/>
      <ellipse cx="50" cy="50" rx="28" ry="10" fill="none" stroke="#ffffff" stroke-width="2" transform="rotate(30 50 50)"/>
      <ellipse cx="50" cy="50" rx="28" ry="10" fill="none" stroke="#ffffff" stroke-width="2" transform="rotate(-30 50 50)"/>
      <ellipse cx="50" cy="50" rx="28" ry="10" fill="none" stroke="#ffffff" stroke-width="2" transform="rotate(90 50 50)"/>
      <circle cx="50" cy="50" r="6" fill="#ffd700"/>
      <text x="50" y="82" font-family="'Times New Roman', serif" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">KHTN</text>
    </svg>'''


from template0_styles import UNIFIED_TEMPLATE0_CSS as TEMPLATE_CSS


def format_inline(text):
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
    def replace_link(match):
        label = match.group(1)
        href = match.group(2)
        if href.startswith('#'):
            return f'<a href="{href}">{label}</a>'
        return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{label}</a>'

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)

    # Restore safe inline tags
    text = text.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")
    text = text.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>").replace("&lt;br /&gt;", "<br>")
    text = text.replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>")
    text = text.replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")
    text = re.sub(r'&lt;(p|div|span|a)\b([^&gt;]*)&gt;', lambda m: f'<{m.group(1)}{html.unescape(m.group(2))}>', text)
    text = re.sub(r'&lt;/(p|div|span|a)&gt;', r'</\1>', text)
    return text


def build_slugs(raw_title):
    s1 = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]+', '-', raw_title.lower()).strip('-')
    s1_collapsed = re.sub(r'-+', '-', s1)
    return [s1_collapsed] if s1_collapsed else ["heading"]


def parse_markdown_snippet_to_html(md_text):
    lines = md_text.splitlines()
    html_lines = []

    in_table = False
    table_buf = []
    in_ul = False
    in_ol = False

    def flush_table():
        nonlocal in_table, table_buf
        if not table_buf:
            return ""
        out = ["<table>"]
        col_aligns = []
        for i, row in enumerate(table_buf):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if all(re.match(r'^:?-+:?$', c) for c in cells if c):
                col_aligns = []
                for c in cells:
                    if c.startswith(":") and c.endswith(":"):
                        col_aligns.append("align-center")
                    elif c.endswith(":"):
                        col_aligns.append("align-right")
                    else:
                        col_aligns.append("align-left")
                continue

            tag = "th" if i == 0 else "td"
            out.append("  <tr>")
            for c_idx, cell in enumerate(cells):
                align_cls = col_aligns[c_idx] if c_idx < len(col_aligns) else ""
                if tag == "td" and not align_cls:
                    if re.match(r'^#\d+$', cell) or cell in ["Minh chứng"]:
                        align_cls = "align-center"
                cls_attr = f' class="{align_cls}"' if align_cls else ""
                inline = format_inline(cell)
                out.append(f"    <{tag}{cls_attr}>{inline}</{tag}>")
            out.append("  </tr>")
        out.append("</table>")
        in_table = False
        table_buf = []
        return "\n".join(out)

    def flush_lists():
        nonlocal in_ul, in_ol
        out = []
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        return "\n".join(out)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            in_table = True
            table_buf.append(stripped)
            i += 1
            continue
        elif in_table:
            html_lines.append(flush_table())

        # Empty lines
        if not stripped:
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            i += 1
            continue

        # Bullet list
        m_ul = re.match(r'^[-*+]\s+(.*)$', stripped)
        if m_ul:
            if in_ol:
                html_lines.append(flush_lists())
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            html_lines.append(f"  <li>{format_inline(m_ul.group(1))}</li>")
            i += 1
            continue

        # Numbered list
        m_ol = re.match(r'^\d+\.\s+(.*)$', stripped)
        if m_ol:
            if in_ul:
                html_lines.append(flush_lists())
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            html_lines.append(f"  <li>{format_inline(m_ol.group(1))}</li>")
            i += 1
            continue

        if in_ul or in_ol:
            html_lines.append(flush_lists())

        # Headings
        m_h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m_h:
            level = len(m_h.group(1))
            heading_raw = m_h.group(2).strip()
            # Check for anchor tag inside heading e.g. <a id="entry-01"></a>Phiên...
            m_anchor = re.match(r'^(<a\s+id="[^"]+"></a>)(.*)$', heading_raw)
            if m_anchor:
                anchor_tag = m_anchor.group(1)
                text_part = m_anchor.group(2).strip()
                slugs = build_slugs(text_part)
                primary_slug = slugs[0]
                heading_text = format_inline(text_part)
                html_lines.append(f'<h{level} id="{primary_slug}">{anchor_tag}{heading_text}</h{level}>')
            else:
                slugs = build_slugs(heading_raw)
                primary_slug = slugs[0]
                heading_text = format_inline(heading_raw)
                html_lines.append(f'<h{level} id="{primary_slug}">{heading_text}</h{level}>')
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            quote_text = format_inline(stripped.lstrip("> ").strip())
            html_lines.append(f"<blockquote><p>{quote_text}</p></blockquote>")
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^(\*{3,}|-{3,}|_{3,})$', stripped):
            html_lines.append("<hr style='border:0; border-top:1px solid #cbd5e1; margin:20px 0;'>")
            i += 1
            continue

        # Regular paragraph
        html_lines.append(f"<p>{format_inline(stripped)}</p>")
        i += 1

    if in_table:
        html_lines.append(flush_table())
    if in_ul or in_ol:
        html_lines.append(flush_lists())

    return "\n".join(html_lines)


def render_cover_page(logo_b64):
    return f"""
<!-- TRANG 1: TRANG BÌA (COVER PAGE) -->
<section class="doc-page cover-page" id="trang-bia">
  <div class="cover-top-section">
    <div class="cover-doc-id">NMCNPM - AI-Powered Helpdesk &amp; Knowledge Base - Group 04</div>

    <div class="proposal-banner">
      <div class="banner-title">AI Usage Report</div>
      <div class="banner-subtitle">Báo cáo Sử dụng Trí tuệ Nhân tạo (AI Usage Transparency &amp; Accountability Report)</div>
    </div>

    <div class="cover-meta-box">
      <div><strong>Học phần:</strong> Nhập môn Công nghệ Phần mềm (CS10014) — Học kỳ 1 / Năm học 2026 - 2027</div>
      <div><strong>Đề tài đề xuất:</strong> AI-Powered Helpdesk &amp; Knowledge Base</div>
      <div><strong>Mã nhóm:</strong> Group 04</div>
      <div><strong>Kho lưu trữ (Repository):</strong> <a href="https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base" target="_blank" rel="noopener noreferrer">https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base</a></div>
      <div><strong>Chuẩn quy định:</strong> Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS</div>
      <div><strong>Mục đích &amp; Phạm vi tài liệu:</strong> Ghi nhận minh bạch toàn bộ quá trình sử dụng các công cụ Trí tuệ nhân tạo (LLM, AI Coding Assistant, Prompt-based generators) trong đồ án theo đúng quy chuẩn bắt buộc của Khoa CNTT - HCMUS.</div>
      <div><strong>Ngày cập nhật:</strong> 28/10/2026</div>
      <div style="margin-top: 14px;">
        <table style="width: 100%; margin: 6px 0 0 0; border-collapse: collapse; font-size: 10.5pt;">
          <thead>
            <tr>
              <th style="padding: 5px 6px; text-align: center; width: 45px;">STT</th>
              <th style="padding: 5px 6px; text-align: center; width: 85px;">MSSV</th>
              <th style="padding: 5px 8px; text-align: left;">Họ và Tên</th>
              <th style="padding: 5px 8px; text-align: center; width: 120px;">GitHub</th>
              <th style="padding: 5px 8px; text-align: left;">Module phụ trách</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="text-align: center; padding: 5px 6px;">1</td>
              <td style="text-align: center; padding: 5px 6px;"><code>24120269</code></td>
              <td style="padding: 5px 8px;">Ngô Viết Thanh Bình (Lead)</td>
              <td style="text-align: center; padding: 5px 8px;"><code>thanhbinh55</code></td>
              <td style="padding: 5px 8px;">D - Identity &amp; Access</td>
            </tr>
            <tr>
              <td style="text-align: center; padding: 5px 6px;">2</td>
              <td style="text-align: center; padding: 4px 6px;"><code>24120083</code></td>
              <td style="padding: 5px 8px;">Nguyễn Đức Lãm</td>
              <td style="text-align: center; padding: 5px 8px;"><code>Lamnguyen-code</code></td>
              <td style="padding: 5px 8px;">B - Knowledge Base</td>
            </tr>
            <tr>
              <td style="text-align: center; padding: 5px 6px;">3</td>
              <td style="text-align: center; padding: 5px 6px;"><code>24120503</code></td>
              <td style="padding: 5px 8px;">Phan Gia Phúc</td>
              <td style="text-align: center; padding: 5px 8px;"><code>t4lf4n</code></td>
              <td style="padding: 5px 8px;">C - Ticket Management</td>
            </tr>
            <tr>
              <td style="text-align: center; padding: 5px 6px;">4</td>
              <td style="text-align: center; padding: 5px 6px;"><code>24120121</code></td>
              <td style="padding: 5px 8px;">Lê Quý Phúc</td>
              <td style="text-align: center; padding: 5px 8px;"><code>Shinkiisme</code></td>
              <td style="padding: 5px 8px;">A - AI Assistance</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div class="cover-bottom-section">
    <div class="cover-institution-block-bottom">
      <div class="cover-logo-wrapper">
        {get_logo_html()}
      </div>
      <div class="cover-inst-text">
        <div class="inst-line-dept">Bộ môn Công nghệ phần mềm</div>
        <div class="inst-line-faculty">Khoa Công nghệ thông tin</div>
        <div class="inst-line-school">Đại học Khoa học tự nhiên TP HCM</div>
      </div>
    </div>
  </div>
</section>

<div class="page-break-divider"></div>
"""


def render_section_page(content_html, page_num_str, section_id=None):
    id_attr = f' id="{section_id}"' if section_id else ""
    return f"""
<section class="doc-page"{id_attr}>
  <!-- Header Bar -->
  <div class="template-header-bar">
    <div class="header-tab">Nhập môn công nghệ phần mềm</div>
    <div class="header-title">Báo cáo sử dụng AI (AI Usage Report)</div>
  </div>

  <!-- Content -->
  <div class="page-content">
{content_html}
  </div>

  <!-- Footer Bar -->
  <div class="template-footer-bar">
    <div class="footer-left">ĐH Khoa học tự nhiên TP HCM | Bộ môn Công nghệ phần mềm</div>
    <div class="footer-tab">Trang {page_num_str}</div>
  </div>
</section>

<div class="page-break-divider"></div>
"""


def build_ai_usage_document():
    with open(MD_FILE, "r", encoding="utf-8") as f:
        md_text = f.read()

    logo_b64 = get_logo_base64()
    cover_html = render_cover_page(logo_b64)

    # Chia các phần nội dung của ai-usage:
    # Trang 1: MỤC 1. NGUYÊN TẮC CỐT LÕI & TUYÊN BỐ SỬ DỤNG AI
    # Trang 2: MỤC 2. BẢNG TỔNG HỢP NHẬT KÝ SỬ DỤNG AI (SUMMARY LOG MATRIX)
    # Trang 3: MỤC 3. CHI TIẾT CÁC PHIÊN SỬ DỤNG AI (Phiên #01 đến #06)
    # Trang 4: MỤC 3 TIẾP THEO (Phiên #07 đến #11) + MỤC 4 (Cam kết) + TÀI LIỆU THAM KHẢO

    part1_match = re.search(r'(## 1\. NGUYÊN TẮC CỐT LÕI.*?\n)(?=## 2\. BẢNG TỔNG HỢP)', md_text, re.DOTALL)
    part1_md = part1_match.group(1) if part1_match else ""

    part2_match = re.search(r'(## 2\. BẢNG TỔNG HỢP NHẬT KÝ SỬ DỤNG AI.*?\n)(?=## 3\. CHI TIẾT)', md_text, re.DOTALL)
    part2_md = part2_match.group(1) if part2_match else ""

    part3_match = re.search(r'(## 3\. CHI TIẾT CÁC PHIÊN SỬ DỤNG AI.*?\n)(?=### <a id="entry-07">)', md_text, re.DOTALL)
    part3_md = part3_match.group(1) if part3_match else ""

    part4_match = re.search(r'(### <a id="entry-07">.*)$', md_text, re.DOTALL)
    part4_md = part4_match.group(1) if part4_match else ""

    pages = [
        render_section_page(parse_markdown_snippet_to_html(part1_md), "1", "sec-intro-principles"),
        render_section_page(parse_markdown_snippet_to_html(part2_md), "2", "sec-summary-matrix"),
        render_section_page(parse_markdown_snippet_to_html(part3_md), "3", "sec-entries-p1"),
        render_section_page(parse_markdown_snippet_to_html(part4_md), "4", "sec-entries-p2"),
    ]

    all_sections_html = "\n".join(pages)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NMCNPM - AI-Powered Helpdesk & Knowledge Base - Group 04 | AI Usage Report</title>
  <style>
{TEMPLATE_CSS}
  </style>
</head>
<body>

{cover_html}
{all_sections_html}

<!-- Floating Back to Top Button -->
<a href="#trang-bia" class="back-to-top" title="Lên đầu trang">
  <span>▲ Lên đầu trang</span>
</a>

</body>
</html>
"""

    with open(OUT_HTML, "w", encoding="utf-8") as f_out:
        f_out.write(full_html)
    print(f"✅ Đã render thành công bản HTML chuẩn Template 0: {OUT_HTML}")


if __name__ == "__main__":
    build_ai_usage_document()
