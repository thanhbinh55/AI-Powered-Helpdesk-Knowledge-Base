#!/usr/bin/env python3
"""
scripts/render_ai_usage_template0.py
Render Báo cáo Sử dụng AI (AI Usage Report) sang định dạng HTML tự chứa (self-contained)
áp dụng 100% phong cách Template 0 chính thức:
- Trang bìa chuẩn học thuật với tiêu đề NMCNPM - AI-Powered Helpdesk & Knowledge Base - Group 04,
  banner lớn và logo HCMUS góc dưới bên trái.
- Phân trang dòng chảy liên tục (continuous flow) giống hệt Microsoft Word docx theo khổ A4: 210mm x 297mm.
- Lề trang cấu hình qua biến CSS: --page-margin-top: 25mm; --page-margin-bottom: 20mm; --page-margin-left: 30mm; --page-margin-right: 20mm.
- Header & Footer chuẩn biểu mẫu trên từng trang nội dung, số trang tự tăng dần (.pn).
- Thuật toán phân trang pure vanilla JS: ngắt trang tự động, tách bảng lặp thead, tách danh sách li, tách đoạn văn orphans/widows >= 2 dòng, keep-with-next cho headings.
- Typography Times New Roman 12pt, line-height 1.5, in ấn A4 chuẩn 1:1.
"""

import os
import sys
import re
import html
import base64

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MD_FILE = os.path.join(REPO_ROOT, "reports", "submit", "ai-usage", "ai-usage.md")
OUT_HTML = os.path.join(REPO_ROOT, "reports", "submit", "ai-usage", "ai-usage.html")
LOGO_PNG = os.path.join(REPO_ROOT, "reports", "submit", "ai-usage", "hcmus_logo.png")


def get_logo_base64():
    candidates = [
        LOGO_PNG,
        os.path.join(os.path.dirname(MD_FILE), "hcmus_logo.png"),
        os.path.join(REPO_ROOT, "reports", "assets", "hcmus_logo.png"),
        os.path.join(REPO_ROOT, "reports", "submit", "project-proposal", "hcmus_logo.png"),
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


def render_cover_page():
    return f"""<!-- TRANG 1: TRANG BÌA (COVER PAGE) -->
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
              <td style="padding: 5px 8px;">Ngô Viết Thanh Bình (Nhóm trưởng)</td>
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
"""


PAGE_CSS = """
:root {
  --page-width: 210mm;
  --page-height: 297mm;
  --page-margin-top: 25mm;
  --page-margin-bottom: 20mm;
  --page-margin-left: 30mm;
  --page-margin-right: 20mm;

  --primary-blue: #548dd4;
  --header-blue: #548dd4;
  --sub-blue: #4f81bd;
  --dark-blue: #366091;
  --text-dark: #000000;
  --border-dark: #cbd5e1;
  --table-stripe: #f8fafc;
  --quote-bg: #f8fafc;
}

*, *::before, *::after,
html, body, p, span, div, a, li, ul, ol, blockquote, table, th, td, tr, 
h1, h2, h3, h4, h5, h6, input, button, select, textarea, b, strong, em, i, 
code, pre, small, sub, sup, header, footer, section, article, caption {
  font-family: 'Times New Roman', Times, serif !important;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  font-family: 'Times New Roman', Times, serif !important;
}

body {
  font-family: 'Times New Roman', Times, serif !important;
  color: var(--text-dark);
  background-color: #f1f5f9;
  margin: 0;
  padding: 20px 0 60px 0;
  line-height: 1.5;
  font-size: 12pt;
}

.doc-page, .report-container, .container {
  background-color: #ffffff;
  max-width: 900px;
  margin: 0 auto 35px auto;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border-radius: 4px;
  box-sizing: border-box;
}

.cover-page {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  min-height: 297mm;
  height: 297mm;
  width: var(--page-width);
  padding: 30mm 25mm 25mm 25mm !important;
  box-sizing: border-box !important;
  background-color: #ffffff;
  margin: 12mm auto;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
  position: relative;
  overflow: hidden;
  page-break-after: always;
  break-after: page;
}

.cover-top-section {
  display: flex;
  flex-direction: column;
}

.cover-doc-id {
  text-align: center;
  font-size: 15pt !important;
  font-weight: 700 !important;
  color: #000000 !important;
  line-height: 1.4;
  margin-bottom: 25px;
  letter-spacing: 0.5px;
}

.proposal-banner {
  background: linear-gradient(135deg, #548dd4 0%, #366091 100%);
  color: #ffffff !important;
  padding: 30px 25px;
  text-align: center;
  border-radius: 4px;
  box-shadow: 0 4px 15px rgba(84, 141, 212, 0.25);
  margin-bottom: 25px;
}

.banner-title {
  font-size: 24pt !important;
  font-weight: 700 !important;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 10px;
  color: #ffffff !important;
}

.banner-subtitle {
  font-size: 13.5pt !important;
  font-style: italic;
  opacity: 0.95;
  color: #ffffff !important;
}

.cover-meta-box {
  background-color: #f8fafc;
  border: 1px solid #cbd5e1;
  padding: 16px 20px;
  margin: 15px 0 20px 0;
  border-radius: 4px;
  font-size: 11pt !important;
  line-height: 1.5;
}

.cover-institution-block-bottom {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 16px;
  margin-top: auto;
  margin-bottom: 5px;
}

.cover-logo-wrapper {
  width: 70px;
  height: 70px;
  flex-shrink: 0;
}

.cover-logo-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.cover-inst-text {
  text-align: left;
  line-height: 1.35;
}

.inst-line-dept {
  font-size: 11.5pt !important;
  font-weight: 700 !important;
  color: #366091;
  text-transform: uppercase;
}

.inst-line-faculty {
  font-size: 12.5pt !important;
  font-weight: 700 !important;
  color: #000000;
  text-transform: uppercase;
}

.inst-line-school {
  font-size: 13.5pt !important;
  font-weight: 700 !important;
  color: #548dd4;
  text-transform: uppercase;
}

/* Page Frame for Word-like pagination */
.page {
  width: var(--page-width);
  height: var(--page-height);
  min-height: var(--page-height);
  max-height: var(--page-height);
  background-color: #ffffff;
  margin: 12mm auto;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  page-break-after: always;
  break-after: page;
  padding: var(--page-margin-top) var(--page-margin-right) var(--page-margin-bottom) var(--page-margin-left);
}

.page .template-header-bar {
  flex: none;
  margin-bottom: 4mm;
}

.page .template-footer-bar {
  flex: none;
  margin-top: 4mm;
}

.page-body {
  flex: 1 1 auto;
  min-height: 0;
  width: 100%;
  overflow: hidden;
  box-sizing: border-box;
  position: relative;
}

.page-body > :first-child {
  margin-top: 0 !important;
}

.template-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 2px solid #548dd4;
  margin-bottom: 0;
  padding-bottom: 0;
  width: 100%;
}

.template-footer-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-top: 2px solid #548dd4;
  margin-top: 0;
  padding-top: 0;
  width: 100%;
}

.header-tab {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  line-height: 1.2;
  padding: 4px 20px;
  display: inline-block;
  margin-bottom: -1px;
  letter-spacing: 0.2px;
}

.header-title {
  color: #000000 !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  line-height: 1.2;
  padding-bottom: 4px;
  padding-right: 2px;
  text-align: right;
  letter-spacing: 0.2px;
}

.footer-left {
  color: #000000 !important;
  font-size: 10.5pt !important;
  padding-top: 5px;
  line-height: 1.2;
}

.footer-tab {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  padding: 4px 22px;
  min-width: 45px;
  text-align: center;
  line-height: 1.2;
  margin-top: -2px;
  display: inline-block;
  letter-spacing: 0.2px;
}

p {
  margin: 0 0 9px 0;
  text-align: justify;
  text-justify: inter-word;
  line-height: 1.45;
  font-size: 12pt;
}

h2 {
  color: #000000;
  font-size: 13.5pt;
  font-weight: 700;
  text-transform: uppercase;
  margin-top: 14px;
  margin-bottom: 8px;
  line-height: 1.35;
}

h3 {
  color: #000000;
  font-size: 12.5pt;
  font-weight: 700;
  margin-top: 12px;
  margin-bottom: 6px;
  line-height: 1.35;
}

ul, ol {
  margin: 0 0 9px 0;
  padding-left: 22px;
  line-height: 1.45;
  font-size: 12pt;
}

li {
  margin-bottom: 3px;
  text-align: justify;
}

blockquote {
  margin: 6px 0 9px 0;
  padding: 7px 12px;
  background-color: var(--quote-bg);
  border: 1px solid var(--border-dark);
  border-radius: 4px;
  font-style: normal;
  font-size: 11pt;
  line-height: 1.45;
}

blockquote p {
  margin: 0;
  font-style: normal;
  text-align: justify;
}

hr {
  border: 0;
  border-top: 1px solid #cbd5e1;
  margin: 8px 0 10px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 6px 0 10px 0;
  font-size: 10.5pt;
  line-height: 1.35;
}

th, td {
  border: 1px solid #94a3b8;
  padding: 4px 6px;
  vertical-align: top;
}

th {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-weight: 700;
  text-align: center;
}

tr:nth-child(even) td {
  background-color: var(--table-stripe);
}

.align-center { text-align: center; }
.align-right { text-align: right; }
.align-left { text-align: left; }

code {
  font-family: 'Times New Roman', Times, serif !important;
  background-color: #f1f5f9;
  padding: 1px 4px;
  border-radius: 3px;
  border: 1px solid #cbd5e1;
  font-size: 11pt;
}

a {
  color: #366091;
  text-decoration: underline;
}

.toc-page-num {
  font-weight: 700;
  color: #366091;
}

@page {
  size: A4 portrait;
  margin: 0;
}

@media print {
  html, body {
    background: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .page, .cover-page {
    margin: 0 !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    height: 296.5mm !important;
    overflow: hidden !important;
    break-after: page !important;
    page-break-after: always !important;
  }
  .page:last-of-type {
    break-after: auto !important;
    page-break-after: auto !important;
  }
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  #source, .back-to-top {
    display: none !important;
  }
}

#source {
  position: absolute;
  left: -99999px;
  top: 0;
  width: calc(var(--page-width) - var(--page-margin-left) - var(--page-margin-right));
  visibility: hidden;
  pointer-events: none;
}

.back-to-top {
  position: fixed;
  bottom: 25px;
  right: 25px;
  background-color: #548dd4;
  color: #ffffff !important;
  padding: 10px 18px;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 700;
  font-size: 11pt;
  box-shadow: 0 4px 12px rgba(84, 141, 212, 0.4);
  z-index: 9999;
  transition: all 0.2s ease;
}
.back-to-top:hover {
  background-color: #366091;
  transform: translateY(-2px);
}
"""

PAGINATOR_SCRIPT = """
<script>
(function () {
  var pages = document.getElementById('pages'), src = document.getElementById('source');
  var HEAD = document.getElementById('tpl-header').innerHTML, FOOT = document.getElementById('tpl-footer').innerHTML;
  var pg, bd, n = 0;

  function newPage() {
    n++; pg = document.createElement('section'); pg.className = 'page';
    pg.innerHTML = HEAD + '<div class="page-body"></div>' + FOOT;
    pg.querySelector('.pn').textContent = n;
    pages.appendChild(pg); bd = pg.querySelector('.page-body');
  }
  function fits() { return bd.scrollHeight <= bd.clientHeight; }
  function probe(node) { bd.appendChild(node); var ok = fits(); bd.removeChild(node); return ok; }
  function maxK(cnt, make) {
    var lo = 0, hi = cnt;
    while (lo < hi) { var m = Math.ceil((lo + hi) / 2); if (probe(make(m))) lo = m; else hi = m - 1; }
    return lo;
  }
  function stripIds(e) { e.removeAttribute('id'); e.querySelectorAll('[id]').forEach(function (x) { x.removeAttribute('id'); }); }

  // Tách đoạn văn theo từ/khoảng trắng, giữ tối thiểu 2 dòng mỗi bên (orphans/widows)
  function textSplit(el) {
    var txt = el.textContent, N = txt.length;
    function part(a, b) {
      var c = el.cloneNode(true), pos = 0, ns = [], w = document.createTreeWalker(c, NodeFilter.SHOW_TEXT);
      while (w.nextNode()) ns.push(w.currentNode);
      ns.forEach(function (x) {
        var L = x.nodeValue.length, s = Math.max(a - pos, 0), e = Math.min(b - pos, L);
        x.nodeValue = e > s ? x.nodeValue.slice(s, e) : ''; pos += L;
      });
      c.querySelectorAll('*').forEach(function (x) { if (!x.textContent && !x.querySelector('img,br')) x.remove(); });
      return c;
    }
    bd.appendChild(el); var lh = parseFloat(getComputedStyle(el).lineHeight) || 24; bd.removeChild(el);
    function lines(node) { bd.appendChild(node); var h = node.getBoundingClientRect().height; bd.removeChild(node); return Math.round(h / lh); }
    var lo = 0, hi = N;
    while (lo < hi) { var m = Math.ceil((lo + hi) / 2); if (probe(part(0, m))) lo = m; else hi = m - 1; }
    var b = txt.lastIndexOf(' ', lo);
    for (var t = 0; t < 12 && b > 0; t++) {
      var head = part(0, b), tail = part(b + 1, N);
      if (lines(head) < 2) return null;
      if (lines(tail) >= 2) { stripIds(tail); return [head, tail]; }
      b = txt.lastIndexOf(' ', b - 40);
    }
    return null;
  }

  // Tách khối dài thành [phần đầu vừa trang, phần còn lại]
  function split(el) {
    var t = el.tagName, kids, mk, k, tail;
    if (t === 'P') return textSplit(el);
    if (t === 'UL' || t === 'OL') {
      kids = [].slice.call(el.children);
      mk = function (a, b) { var c = el.cloneNode(false); kids.slice(a, b).forEach(function (x) { c.appendChild(x.cloneNode(true)); }); return c; };
      k = maxK(kids.length, function (m) { return mk(0, m); });
      if (k < 1 || k >= kids.length) return null;
      if (k === 1 && /:\s*$/.test(kids[0].textContent)) return null; // nhãn không đứng một mình cuối trang
      tail = mk(k, kids.length); stripIds(tail);
      if (t === 'OL') tail.setAttribute('start', (parseInt(el.getAttribute('start') || 1, 10)) + k);
      return [mk(0, k), tail];
    }
    if (t === 'TABLE') {
      var th = el.querySelector('thead'), rows = [].slice.call(el.tBodies[0] ? el.tBodies[0].rows : []), hdr = null;
      if (!th && rows[0] && rows[0].querySelector('th') && !rows[0].querySelector('td')) hdr = rows.shift();
      mk = function (a, b) {
        var c = el.cloneNode(false); if (th) c.appendChild(th.cloneNode(true));
        var tb = document.createElement('tbody'); if (hdr) tb.appendChild(hdr.cloneNode(true));
        rows.slice(a, b).forEach(function (r) { tb.appendChild(r.cloneNode(true)); });
        c.appendChild(tb); return c;
      };
      k = maxK(rows.length, function (m) { return mk(0, m); });
      if (k < 1 || k >= rows.length) return null;
      tail = mk(k, rows.length); stripIds(tail); return [mk(0, k), tail];
    }
    if (t === 'BLOCKQUOTE' || t === 'DIV') {
      kids = [].slice.call(el.children);
      mk = function (a, b) { var c = el.cloneNode(false); kids.slice(a, b).forEach(function (x) { c.appendChild(x.cloneNode(true)); }); return c; };
      k = maxK(kids.length, function (m) { return mk(0, m); });
      if (k < 1 || k >= kids.length) return null;
      tail = mk(k, kids.length); stripIds(tail); return [mk(0, k), tail];
    }
    return null;
  }

  function keepNext(e) {
    return /^(H[1-6]|HR)$/.test(e.tagName) || (e.tagName === 'UL' && e.children.length === 1 && /:\s*$/.test(e.textContent));
  }

  // Sang trang mới; heading/hr/nhãn mồ côi cuối trang được đẩy theo sang trang sau
  function breakPage(q) {
    var mv = [];
    while (bd.children.length > 1 && keepNext(bd.lastElementChild)) mv.unshift(bd.removeChild(bd.lastElementChild));
    newPage(); q.unshift.apply(q, mv);
  }

  function place(blocks) {
    var q = blocks.slice();
    while (q.length) {
      var el = q.shift();
      if (el.classList.contains('page-break-before')) {
        el.classList.remove('page-break-before');
        if (bd.children.length) { q.unshift(el); breakPage(q); continue; }
      }
      if (el.tagName === 'HR' && !bd.children.length) continue;
      bd.appendChild(el);
      if (fits()) continue;
      bd.removeChild(el);
      var s = split(el);
      if (s) { bd.appendChild(s[0]); q.unshift(s[1]); breakPage(q); }
      else if (bd.children.length) { q.unshift(el); breakPage(q); }
      else { bd.appendChild(el); breakPage(q); }
    }
  }

  function toc() {
    document.querySelectorAll('.toc-link').forEach(function (a) {
      var id = a.getAttribute('href').slice(1), t = document.getElementById(id), box = t && t.closest('.page'), num = a.querySelector('.toc-page-num');
      if (box && num) num.textContent = box.querySelector('.pn').textContent;
    });
  }
  function run() {
    newPage(); place([].slice.call(src.children)); src.remove(); toc(); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run); else run();
})();
</script>
"""


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
    return text


def build_slugs(raw_title):
    s1 = re.sub(r'[^a-zA-Z0-9\u00C0-\u024F\u1EA0-\u1EF9]+', '-', raw_title.lower()).strip('-')
    s1_collapsed = re.sub(r'-+', '-', s1)
    return [s1_collapsed] if s1_collapsed else ["heading"]


def parse_markdown_to_source_blocks(md_text):
    """
    Parse full markdown content of ai-usage.md into semantic HTML blocks for <div id="source">.
    Ensures 100% fidelity with original markdown and clean HTML structure.
    """
    # Specifically extract clean Phiên #11 markup to prevent line-broken prompt artifacts
    lines = md_text.splitlines()
    html_blocks = []

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
        thead_rows = []
        tbody_rows = []

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
            row_html = ["  <tr>"]
            for c_idx, cell in enumerate(cells):
                align_cls = col_aligns[c_idx] if c_idx < len(col_aligns) else ""
                if tag == "td" and not align_cls:
                    if re.match(r'^#\d+$', cell) or cell in ["Minh chứng"]:
                        align_cls = "align-center"
                cls_attr = f' class="{align_cls}"' if align_cls else ""
                inline = format_inline(cell)
                row_html.append(f"    <{tag}{cls_attr}>{inline}</{tag}>")
            row_html.append("  </tr>")

            if tag == "th":
                thead_rows.append("\n".join(row_html))
            else:
                tbody_rows.append("\n".join(row_html))

        if thead_rows:
            out.append("<thead>\n" + "\n".join(thead_rows) + "\n</thead>")
        if tbody_rows:
            out.append("<tbody>\n" + "\n".join(tbody_rows) + "\n</tbody>")
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

        # Handle Phiên 11 specially if detected to maintain complete blockquote and clean prompt
        if "Phiên ghi nhận #11" in line:
            if in_table:
                html_blocks.append(flush_table())
            if in_ul or in_ol:
                html_blocks.append(flush_lists())

            p11_html = """<h3 id="phiên-ghi-nhận-11-rà-soát-kiểm-tra-nội-dung-của-phần-5"><a id="entry-11"></a>Phiên ghi nhận #11: Rà soát, kiểm tra nội dung của phần 5</h3>
<ul>
  <li><strong>Trích dẫn chuẩn:</strong></li>
</ul>
<blockquote><p><strong>ChatGPT.</strong> <em>GPT-6.1 Sol, OpenAI, chat.openai.com</em>, truy cập <em>19h30 ngày 28/10/2026</em>, prompt: <em>“đây là nội dung phần 5 do bạn tôi viết bạn hãy đọc, và kiểm tra lại thật kỹ xem 1. có chỗ nào bị mâu thuẫn so với file SRS không theo nội dung tham khảo như sau: # 5. Kế hoạch nhân sự &amp; chi phí<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Cấu trúc nhân sự toàn dự án và liệt kê các khoản chi phí dự kiến. Tham khảo Mục 16, 16.1, <strong>Phụ lục H</strong> và <strong>Phụ lục I</strong> trong <code>reports/SRS-master.md</code>.<br>
<br>
<em>(Nội dung do <code>Ngô Viết Thanh Bình</code> biên soạn theo Jira <code>SCRUM-11</code>)</em><br>
<br>
### 5.1. Cấu trúc nhân sự<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Ma trận vai trò, mô tả trách nhiệm và người phụ trách. Tham khảo <strong>Phụ lục H</strong> trong <code>reports/SRS-master.md</code>.<br>
<br>
### 5.2. Kế hoạch chi phí<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Bảng tổng hợp chi phí nhân sự, hạ tầng cloud, API LLM, công cụ và dự phòng rủi ro. Tham khảo <strong>Phụ lục I</strong> trong <code>reports/SRS-master.md</code>.<br>
2. có chỗ nào cách viết bị quá máy móc, theo kiẻu của AI quá không, dùng skill $humanizer:humanizer để gợi ý cho tôi các sửa(chỉ gợi ý chỗ bị lỗi và cách sửa, không tự sửa)”</em></p></blockquote>
<ul>
  <li><strong>Thành viên chịu trách nhiệm:</strong> <code>24120083</code> - Nguyễn Đức Lãm (Phân hệ Knowledge Base)</li>
  <li><strong>Chi tiết các câu prompt nguyên văn do thành viên khai báo:</strong></li>
</ul>
<ol>
  <li><em>"- đây là nội dung phần 5 do bạn tôi viết bạn hãy đọc, và kiểm tra lại thật kỹ xem có chỗ nào bị mâu thuẫn so với file SRS không theo nội dung tham khảo như sau: # 5. Kế hoạch nhân sự &amp; chi phí<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Cấu trúc nhân sự toàn dự án và liệt kê các khoản chi phí dự kiến. Tham khảo Mục 16, 16.1, <strong>Phụ lục H</strong> và <strong>Phụ lục I</strong> trong <code>reports/SRS-master.md</code>.<br>
<br>
<em>(Nội dung do <code>Ngô Viết Thanh Bình</code> biên soạn theo Jira <code>SCRUM-11</code>)</em><br>
<br>
### 5.1. Cấu trúc nhân sự<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Ma trận vai trò, mô tả trách nhiệm và người phụ trách. Tham khảo <strong>Phụ lục H</strong> trong <code>reports/SRS-master.md</code>.<br>
<br>
### 5.2. Kế hoạch chi phí<br>
&gt; <em>Ghi chú nguồn nguyên liệu:</em> Bảng tổng hợp chi phí nhân sự, hạ tầng cloud, API LLM, công cụ và dự phòng rủi ro. Tham khảo <strong>Phụ lục I</strong> trong <code>reports/SRS-master.md</code>.<br>
có chỗ nào cách viết bị quá máy móc, theo kiẻu của AI quá không, dùng skill $humanizer:humanizer để gợi ý cho tôi các sửa(chỉ gợi ý chỗ bị lỗi và cách sửa, không tự sửa)"</em></li>
  <li><em>"nhìn chung, thì phần 5.1 đang mô tả quá chi tiết, mở rộng so với bản SRS đúng không"</em></li>
</ol>
<ul>
  <li><strong>Chi tiết đối soát:</strong>
    <ul>
      <li><em>Nội dung AI tạo:</em> Nhận xét cho phần 5.</li>
      <li><em>Nội dung tự thực hiện &amp; kiểm chứng:</em> Kiểm chứng và đối chiếu với mục 16., 16.1, phụ lục H, phụ lục I trong file SRS-master.md.</li>
      <li><em>Minh chứng:</em> Phiên rà soát phản biện được thực hiện trực tiếp trên bản thảo Google Docs nội bộ của nhóm (không phát sinh commit mã nguồn riêng trên Git).</li>
    </ul>
  </li>
</ul>
<hr>"""
            html_blocks.append(p11_html)
            # Skip until ## 4. CAM KẾT
            while i < len(lines) and not lines[i].strip().startswith("## 4."):
                i += 1
            continue

        # Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            if in_ul or in_ol:
                html_blocks.append(flush_lists())
            in_table = True
            table_buf.append(stripped)
            i += 1
            continue
        elif in_table:
            html_blocks.append(flush_table())

        # Empty lines
        if not stripped:
            if in_ul or in_ol:
                html_blocks.append(flush_lists())
            i += 1
            continue

        # Bullet list
        m_ul = re.match(r'^[-*+]\s+(.*)$', stripped)
        if m_ul:
            if in_ol:
                html_blocks.append(flush_lists())
            if not in_ul:
                html_blocks.append("<ul>")
                in_ul = True
            html_blocks.append(f"  <li>{format_inline(m_ul.group(1))}</li>")
            i += 1
            continue

        # Numbered list
        m_ol = re.match(r'^\d+\.\s+(.*)$', stripped)
        if m_ol:
            if in_ul:
                html_blocks.append(flush_lists())
            if not in_ol:
                html_blocks.append("<ol>")
                in_ol = True
            html_blocks.append(f"  <li>{format_inline(m_ol.group(1))}</li>")
            i += 1
            continue

        if in_ul or in_ol:
            html_blocks.append(flush_lists())

        # Headings
        m_h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m_h:
            level = len(m_h.group(1))
            heading_raw = m_h.group(2).strip()
            # Anchor tag
            m_anchor = re.match(r'^(<a\s+id="[^"]+"></a>)(.*)$', heading_raw)
            if m_anchor:
                anchor_tag = m_anchor.group(1)
                text_part = m_anchor.group(2).strip()
                slugs = build_slugs(text_part)
                primary_slug = slugs[0]
                heading_text = format_inline(text_part)
                html_blocks.append(f'<h{level} id="{primary_slug}">{anchor_tag}{heading_text}</h{level}>')
            else:
                slugs = build_slugs(heading_raw)
                primary_slug = slugs[0]
                heading_text = format_inline(heading_raw)
                if primary_slug == "2-bảng-tổng-hợp-nhật-ký-sử-dụng-ai-summary-log-matrix":
                    html_blocks.append(f'<h{level} id="{primary_slug}" class="page-break-before">{heading_text}</h{level}>')
                else:
                    html_blocks.append(f'<h{level} id="{primary_slug}">{heading_text}</h{level}>')
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            quote_text = format_inline(stripped.lstrip("> ").strip())
            html_blocks.append(f"<blockquote><p>{quote_text}</p></blockquote>")
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^(\*{3,}|-{3,}|_{3,})$', stripped):
            html_blocks.append("<hr>")
            i += 1
            continue

        # Paragraph
        html_blocks.append(f"<p>{format_inline(stripped)}</p>")
        i += 1

    if in_table:
        html_blocks.append(flush_table())
    if in_ul or in_ol:
        html_blocks.append(flush_lists())

    # Filter out empty blocks
    return [b for b in html_blocks if b and b.strip()]


def build_ai_usage_document():
    with open(MD_FILE, "r", encoding="utf-8") as f:
        md_text = f.read()

    cover_html = render_cover_page()

    # Extract content starting from Section 1
    sec1_idx = md_text.find("## 1. NGUYÊN TẮC")
    if sec1_idx != -1:
        content_md = md_text[sec1_idx:]
    else:
        content_md = md_text

    blocks = parse_markdown_to_source_blocks(content_md)
    source_content = "\n".join(blocks)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NMCNPM - AI-Powered Helpdesk &amp; Knowledge Base - Group 04 | AI Usage Report</title>
  <style>
{PAGE_CSS}
  </style>
</head>
<body>

{cover_html}

<div id="pages"></div>

<div id="source">
{source_content}
</div>

<template id="tpl-header">
  <div class="template-header-bar">
    <div class="header-tab">Nhập môn công nghệ phần mềm</div>
    <div class="header-title">Báo cáo sử dụng AI (AI Usage Report)</div>
  </div>
</template>

<template id="tpl-footer">
  <div class="template-footer-bar">
    <div class="footer-left">ĐH Khoa học tự nhiên TP HCM | Bộ môn Công nghệ phần mềm</div>
    <div class="footer-tab">Trang <span class="pn"></span></div>
  </div>
</template>

<!-- Floating Back to Top Button -->
<a href="#trang-bia" class="back-to-top" title="Lên đầu trang">
  <span>▲ Lên đầu trang</span>
</a>

{PAGINATOR_SCRIPT}

</body>
</html>
"""

    with open(OUT_HTML, "w", encoding="utf-8") as f_out:
        f_out.write(full_html)
    print(f"✅ Đã render thành công bản HTML chuẩn Template 0: {OUT_HTML}")


if __name__ == "__main__":
    build_ai_usage_document()
