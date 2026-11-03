#!/usr/bin/env python3
"""
scripts/render_proposal_template0.py
Biên dịch báo cáo Đề xuất Đồ án (Project Proposal) sang định dạng HTML tự chứa (self-contained)
tuân thủ 100% quy chuẩn biểu mẫu, font chữ, bảng biểu và màu sắc từ Template 0 chính thức của Thầy.
Hỗ trợ phân trang chuẩn học thuật:
- Trang bìa (Cover Page) độc lập với dòng tiêu đề NMCNPM - <Project Name> - <Group ID>.
- Trang mục lục (Table of Contents) độc lập.
- Mỗi phần lớn (Mục 1, 2, 3, 4, 5, Tham khảo & Phụ lục) kết thúc bằng lệnh ngắt trang (end page / page-break).
- Header & Footer chuẩn biểu mẫu theo đúng ảnh chụp thực tế từ Thầy.
"""

import os
import sys
import re
import html
import base64

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MD_FILE = os.path.join(REPO_ROOT, "reports", "submit", "project-proposal", "project-proposal.md")
OUT_HTML = os.path.join(REPO_ROOT, "reports", "submit", "project-proposal", "project-proposal.html")
LOGO_PNG = os.path.join(REPO_ROOT, "reports", "submit", "project-proposal", "hcmus_logo.png")


def get_logo_base64():
    candidates = [
        LOGO_PNG,
        os.path.join(os.path.dirname(MD_FILE), "hcmus_logo.png"),
        os.path.join(REPO_ROOT, "reports", "assets", "hcmus_logo.png"),
    ]
    for c in candidates:
        if os.path.exists(c):
            with open(c, "rb") as f:
                return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
    return ""


def get_logo_html():
    b64 = get_logo_base64()
    if b64:
        return f'<img src="{b64}" alt="HCMUS Logo">'
    return ""


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

    # Links [text](url) -> hash links stay on current page, external links open in new tab
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
    text = re.sub(r'&lt;(p|div|span)\b([^&gt;]*)&gt;', lambda m: f'<{m.group(1)}{html.unescape(m.group(2))}>', text)
    text = re.sub(r'&lt;/(p|div|span)&gt;', r'</\1>', text)
    return text


def build_slugs(raw_title):
    # Primary slug
    s1 = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]+', '-', raw_title.lower()).strip('-')
    s1_collapsed = re.sub(r'-+', '-', s1)

    # Slug without dots (e.g., 2.1. -> 21)
    s2 = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]+', '-', raw_title.replace('.', '').lower()).strip('-')
    s2_collapsed = re.sub(r'-+', '-', s2)

    # Collect unique slugs
    slugs = []
    for s in [s1_collapsed, s1, s2_collapsed, s2]:
        if s and s not in slugs:
            slugs.append(s)
    # Also include double-dash alias for '&'
    if '&' in raw_title:
        s_amp = raw_title.lower().replace('&', '--')
        s_amp = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9-]+', '-', s_amp).strip('-')
        if s_amp and s_amp not in slugs:
            slugs.append(s_amp)
    return slugs


def parse_markdown_snippet_to_html(md_text):
    lines = md_text.splitlines()
    html_lines = []

    in_code = False
    code_lang = ""
    code_buf = []

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
            # Check alignment row
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
                    if re.match(r'^\d+$', cell) or re.match(r'^[A-Z0-9-]+$', cell) or cell in ["100%", "READY", "FAILED", "OPEN"]:
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

        # Code block
        if stripped.startswith("```"):
            if in_ul or in_ol:
                html_lines.append(flush_lists())
            if in_code:
                in_code = False
                content = html.escape("\n".join(code_buf))
                if code_lang == "mermaid":
                    html_lines.append(f'<div class="mermaid">\n{content}\n</div>')
                else:
                    html_lines.append(f'<pre><code class="language-{code_lang}">{content}</code></pre>')
                code_buf = []
                code_lang = ""
            else:
                if in_table:
                    html_lines.append(flush_table())
                in_code = True
                code_lang = stripped[3:].strip()
                code_buf = []
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

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

        # Flush open lists
        if in_ul or in_ol:
            html_lines.append(flush_lists())

        # Headings
        m_h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m_h:
            level = len(m_h.group(1))
            heading_raw = m_h.group(2).strip()
            slugs = build_slugs(heading_raw)
            primary_slug = slugs[0] if slugs else "heading"
            alias_spans = "".join([f'<span id="{s}"></span>' for s in slugs[1:]])
            heading_text = format_inline(heading_raw)
            html_lines.append(f'<h{level} id="{primary_slug}">{alias_spans}{heading_text}</h{level}>')
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

        # Ignore markdown-inserted page break divs since .doc-page wrapper already handles section paging
        if stripped.startswith("<div") and ("page-break" in stripped or "break-after" in stripped):
            i += 1
            continue

        # Raw paragraph or custom block (single or multi-line)
        if stripped.startswith("<p") or (stripped.startswith("<div") and not ("page-break" in stripped or "break-after" in stripped)):
            tag_name = "p" if stripped.startswith("<p") else "div"
            closing_tag = f"</{tag_name}>"
            if closing_tag in stripped:
                html_lines.append(stripped)
                i += 1
                continue
            else:
                buf = [stripped]
                i += 1
                while i < len(lines):
                    buf.append(lines[i].strip())
                    if closing_tag in lines[i]:
                        i += 1
                        break
                    i += 1
                html_lines.append(" ".join(buf))
                continue

        # Markdown image ![alt](src)
        m_img = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', stripped)
        if m_img:
            alt = m_img.group(1)
            src = m_img.group(2)
            if "kien-truc-tong-the.svg" in src:
                svg_path = os.path.join(REPO_ROOT, "reports", "submit", "project-proposal", "kien-truc-tong-the.svg")
                if os.path.exists(svg_path):
                    with open(svg_path, "r", encoding="utf-8") as f_svg:
                        svg_code = f_svg.read()
                    svg_code = re.sub(r'<\?xml[^>]*\?>', '', svg_code)
                    html_lines.append(f'<div class="svg-diagram-wrapper">{svg_code}</div>')
                else:
                    html_lines.append(f'<div class="svg-diagram-wrapper"><img src="{src}" alt="{alt}" style="max-width: 100%; height: auto;"></div>')
            else:
                html_lines.append(f'<div style="text-align: center; margin: 20px auto;"><img src="{src}" alt="{alt}" style="max-width: 100%; height: auto;"></div>')
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
    <!-- Dòng tiêu đề chính theo Template 0 -->
    <div class="cover-doc-id">NMCNPM - AI-Powered Helpdesk &amp; Knowledge Base - Group 04</div>

    <!-- Banner xanh Project Proposal đúng chuẩn Template 0 -->
    <div class="proposal-banner">
      <div class="banner-title">Project Proposal</div>
    </div>
  </div>

  <div class="cover-bottom-section">
    <!-- Khối logo + bộ môn, khoa, trường ở góc trái dưới đúng chuẩn Template 0 -->
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


def render_toc_page(toc_md_text=""):
    toc_items = [
        '<li class="toc-item"><a class="toc-link" href="#1-bảng-đánh-giá-thành-viên"><span class="toc-title-text">1. Bảng đánh giá thành viên</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#2-phát-biểu-bài-toán-sơ-lược"><span class="toc-title-text">2. Phát biểu bài toán sơ lược</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#21-bối-cảnh-và-vấn-đề-đặt-ra"><span class="toc-sub-title-text">2.1. Bối cảnh và vấn đề đặt ra</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#22-ý-tưởng-giải-pháp-đề-xuất"><span class="toc-sub-title-text">2.2. Ý tưởng giải pháp đề xuất</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#23-môi-trường-hoạt-động-dự-kiến"><span class="toc-sub-title-text">2.3. Môi trường hoạt động dự kiến</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#24-ràng-buộc-thiết-kế-và-triển-khai"><span class="toc-sub-title-text">2.4. Ràng buộc thiết kế và triển khai</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#25-mục-tiêu-và-tiêu-chí-thành-công"><span class="toc-sub-title-text">2.5. Mục tiêu và tiêu chí thành công</span><span class="toc-dots"></span><span class="toc-page-num">1</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#26-đối-tượng-sử-dụng"><span class="toc-sub-title-text">2.6. Đối tượng sử dụng</span><span class="toc-dots"></span><span class="toc-page-num">2</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#27-phạm-vi-mvp-và-giá-trị-sử-dụng"><span class="toc-sub-title-text">2.7. Phạm vi MVP và giá trị sử dụng</span><span class="toc-dots"></span><span class="toc-page-num">2</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#3-giải-pháp-đề-xuất"><span class="toc-title-text">3. Giải pháp đề xuất</span><span class="toc-dots"></span><span class="toc-page-num">2</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#31-phần-mềm"><span class="toc-sub-title-text">3.1. Phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">2</span></a></li>',
        '<li class="toc-item" style="padding-left: 36px;"><a class="toc-link" href="#311-danh-sách-các-chức-năng-phần-mềm"><span class="toc-sub-title-text">3.1.1. Danh sách các chức năng phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">2</span></a></li>',
        '<li class="toc-item" style="padding-left: 36px;"><a class="toc-link" href="#312-kiến-trúc-tổng-thể-phần-mềm"><span class="toc-sub-title-text">3.1.2. Kiến trúc tổng thể phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">4</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#32-phần-cứng"><span class="toc-sub-title-text">3.2. Phần cứng</span><span class="toc-dots"></span><span class="toc-page-num">5</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#4-kế-hoạch-phát-triển"><span class="toc-title-text">4. Kế hoạch phát triển</span><span class="toc-dots"></span><span class="toc-page-num">6</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#41-phân-tích-yêu-cầu"><span class="toc-sub-title-text">4.1. Phân tích yêu cầu</span><span class="toc-dots"></span><span class="toc-page-num">6</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#42-thiết-kế-phần-mềm"><span class="toc-sub-title-text">4.2. Thiết kế phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">6</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#43-cài-đặt-implement-phần-mềm"><span class="toc-sub-title-text">4.3. Cài đặt (implement) phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">6</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#44-kiểm-thử-phần-mềm"><span class="toc-sub-title-text">4.4. Kiểm thử phần mềm</span><span class="toc-dots"></span><span class="toc-page-num">7</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#45-triển-khai-bảo-trì"><span class="toc-sub-title-text">4.5. Triển khai, bảo trì</span><span class="toc-dots"></span><span class="toc-page-num">7</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#5-kế-hoạch-nhân-sự-chi-phí"><span class="toc-title-text">5. Kế hoạch nhân sự &amp; chi phí</span><span class="toc-dots"></span><span class="toc-page-num">7</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#51-cấu-trúc-nhân-sự"><span class="toc-sub-title-text">5.1. Cấu trúc nhân sự</span><span class="toc-dots"></span><span class="toc-page-num">7</span></a></li>',
        '<li class="toc-item" style="padding-left: 18px;"><a class="toc-link" href="#52-kế-hoạch-chi-phí"><span class="toc-sub-title-text">5.2. Kế hoạch chi phí</span><span class="toc-dots"></span><span class="toc-page-num">8</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#tài-liệu-tham-khảo-references"><span class="toc-title-text">Tài liệu tham khảo (References)</span><span class="toc-dots"></span><span class="toc-page-num">8</span></a></li>',
        '<li class="toc-item"><a class="toc-link" href="#phụ-lục-tuyên-bố-và-ghi-chú-sử-dụng-ai"><span class="toc-title-text">Phụ lục: Tuyên bố và Ghi chú sử dụng AI</span><span class="toc-dots"></span><span class="toc-page-num">9</span></a></li>'
    ]

    toc_body = "\n".join(toc_items)
    return f"""
<!-- TRANG 2: MỤC LỤC (TABLE OF CONTENTS) -->
<section class="doc-page toc-page" id="trang-muc-luc">
  <div class="page-content">
    <div class="toc-container" id="muc-luc">
      <div class="toc-header-title">MỤC LỤC</div>
      <ul class="toc-list">
{toc_body}
      </ul>
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
    <div class="header-title">Project Proposal</div>
  </div>

  <!-- Content -->
  <div class="page-content">
{content_html}
  </div>

  <!-- Footer Bar -->
  <div class="template-footer-bar">
    <div class="footer-left">ĐH Khoa học tự nhiên TP HCM | Bộ môn Công nghệ phần mềm</div>
    <div class="footer-tab">{page_num_str}</div>
  </div>
</section>

<div class="page-break-divider"></div>
"""


def build_template0_document():
    with open(MD_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    logo_b64 = get_logo_base64()
    cover_html = render_cover_page(logo_b64)
    toc_html = render_toc_page()

    # Phân trang chuẩn A4 (Portrait) tương đương Word docx:
    # Page 1 (Trang 1): 1. Bảng đánh giá thành viên + 2. Phát biểu bài toán (2.1 - 2.5)
    p1 = text[text.find("# 1. Bảng đánh giá thành viên"):text.find("### 2.6. Đối tượng sử dụng")]

    # Page 2 (Trang 2): 2.6, 2.7 + 3. Giải pháp đề xuất (3.1.1 Bảng chức năng STT 1-12)
    idx_2_6 = text.find("### 2.6. Đối tượng sử dụng")
    idx_row_12 = text.find("| 12 | `FR-TK-08`")
    end_row_12 = text.find("\n", idx_row_12) + 1
    p2 = text[idx_2_6:end_row_12]

    # Page 3 (Trang 3): 3.1.1 Bảng chức năng tiếp theo (STT 13-30)
    idx_row_13 = text.find("| 13 | `FR-KB-01`")
    idx_3_1_2 = text.find("### 3.1.2. Kiến trúc tổng thể phần mềm")
    table_header = '''### 3.1.1. Danh sách các chức năng phần mềm (tiếp theo)

<p class="table-caption" style="text-align: center; font-weight: 700; margin-bottom: 8px; font-size: 11.5pt;">Bảng 4. Bảng thể hiện các chức năng cơ bản của phần mềm (tiếp theo)</p>

| STT | Mã US / FR | Phân hệ (Module) | Tên chức năng / Yêu cầu người dùng (User Story) | Mức độ ưu tiên |
| :---: | :--- | :--- | :--- | :---: |
'''
    p3 = table_header + text[idx_row_13:idx_3_1_2]

    # Page 4 (Trang 4): 3.1.2 a. Sơ đồ kiến trúc tổng thể (SVG) + b. Các thành phần và trách nhiệm
    idx_luong = text.find("#### c. Luồng vận hành")
    p4 = text[idx_3_1_2:idx_luong]

    # Page 5 (Trang 5): 3.1.2 c. Luồng vận hành + 3.2 Phần cứng (3.2.1 & 3.2.2)
    idx_sec_4 = text.find("# 4. Kế hoạch phát triển")
    p5 = text[idx_luong:idx_sec_4]

    # Page 6 (Trang 6): 4. Kế hoạch phát triển (Tổng quan + 4.1, 4.2, 4.3)
    idx_4_4 = text.find("### 4.4. Kiểm thử phần mềm")
    p6 = text[idx_sec_4:idx_4_4]

    # Page 7 (Trang 7): 4.4, 4.5 + 5. Kế hoạch nhân sự & chi phí (5.1 Cấu trúc nhân sự)
    idx_5_2 = text.find("### 5.2. Kế hoạch chi phí")
    p7 = text[idx_4_4:idx_5_2]

    # Page 8 (Trang 8): 5.2 Kế hoạch chi phí (47.840.000 VNĐ) + Tài liệu tham khảo
    idx_phuluc = text.find("## PHỤ LỤC:")
    p8 = text[idx_5_2:idx_phuluc]

    # Page 9 (Trang 9): Phụ lục AI
    p9 = text[idx_phuluc:]

    raw_pages = [
        (p1, "Trang 1", "sec-1"),
        (p2, "Trang 2", "sec-2"),
        (p3, "Trang 3", "sec-3-p2"),
        (p4, "Trang 4", "sec-3-arch"),
        (p5, "Trang 5", "sec-3-hw"),
        (p6, "Trang 6", "sec-4"),
        (p7, "Trang 7", "sec-5-p1"),
        (p8, "Trang 8", "sec-5-p2"),
        (p9, "Trang 9", "sec-ref"),
    ]

    section_pages = []
    for p_text, page_tab, sec_id in raw_pages:
        content_html = parse_markdown_snippet_to_html(p_text)
        section_pages.append(render_section_page(content_html, page_tab, sec_id))

    all_sections_html = "\n".join(section_pages)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NMCNPM - AI-Powered Helpdesk & Knowledge Base - Group 04 | Project Proposal (Template 0)</title>
  <style>
{TEMPLATE_CSS}
  </style>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'neutral',
      flowchart: {{ curve: 'linear', useMaxWidth: true }}
    }});
  </script>
</head>
<body>

{cover_html}
{toc_html}
{all_sections_html}

<!-- Floating Back to Top Button -->
<a href="#muc-luc" class="back-to-top" title="Lên đầu trang / Mục lục">
  <span>▲ Mục lục</span>
</a>

</body>
</html>
"""

    with open(OUT_HTML, "w", encoding="utf-8") as f_out:
        f_out.write(full_html)
    print(f"✅ Đã render thành công bản HTML chuẩn Template 0 phân trang: {OUT_HTML}")


if __name__ == "__main__":
    build_template0_document()
