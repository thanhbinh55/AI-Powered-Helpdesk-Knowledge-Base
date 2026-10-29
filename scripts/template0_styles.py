"""
scripts/template0_styles.py
Bộ quy chuẩn CSS và Typography thống nhất 100% Times New Roman cho tất cả báo cáo đồ án:
- Toàn bộ phần tử (HTML, body, bảng, tiêu đề, mã nguồn, trích dẫn, header, footer) dùng font Times New Roman.
- Hệ thống phân cấp cỡ chữ chuẩn mực học thuật:
  + Body / Paragraph / List: 12pt (16px), line-height: 1.5, căn đều (justify)
  + H1 (Chương / Mục lớn cấp 1: 1., 2., 3., 4., 5., Phụ lục): 16pt, bold, xanh #0070c0, gạch chân 2px
  + H2 (Mục cấp 2: 3.1., 3.2., 4.1., 5.1.,...): 14pt, bold, xanh #0070c0, gạch chân 1px
  + H3 (Mục cấp 3: 3.1.1., 3.1.2., 3.2.1.,...): 13pt, bold, xanh đậm #366091
  + H4 (Mục cấp 4: a., b., c.,...): 12.5pt, bold, xanh trung hòa #4f81bd
  + H5 (Mục cấp 5: Xử lý ticket,...): 12pt, bold, nghiêng, #26215c
  + H6: 12pt, bold, nghiêng, #475569
  + Bảng biểu (Table): 11pt, dòng kẻ xám sắc nét, th nền xanh #0070c0 chữ trắng, td zebra striping
  + Tiêu đề bảng / hình (.table-caption, .figure-caption): 11.5pt, bold / nghiêng, căn giữa
  + Mã / Badges (code, commit-badge): Times New Roman 11pt, nền xám nhạt/xanh nhạt
  + Header bar & Footer bar: Times New Roman 11pt / 10.5pt, tab xanh #0070c0
"""

UNIFIED_TEMPLATE0_CSS = """
:root {
  --primary-blue: #548dd4;
  --header-blue: #548dd4;
  --sub-blue: #4f81bd;
  --dark-blue: #366091;
  --text-dark: #000000;
  --border-dark: #cbd5e1;
  --table-stripe: #f8fafc;
  --quote-bg: #f8fafc;
}

/* Ép buộc 100% tất cả các phần tử trên trang sử dụng font Times New Roman */
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
  padding: 30px 0 60px 0;
  line-height: 1.5;
  font-size: 12pt;
}

/* Document Page Sheet representing each paginated section */
.doc-page, .report-container, .container {
  background-color: #ffffff;
  max-width: 900px;
  margin: 0 auto 35px auto;
  padding: 40px 55px 35px 55px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border-radius: 4px;
  box-sizing: border-box;
  font-family: 'Times New Roman', Times, serif !important;
}

.doc-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cover-page {
  min-height: 1050px;
}

.toc-page {
  min-height: 950px;
}

.page-content {
  flex-grow: 1;
}

/* Page Break Divider for Screen */
.page-break-divider {
  height: 20px;
  page-break-after: always;
  break-after: page;
}

/* Running Header strictly matching teacher's Template 0 */
.template-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 2px solid #548dd4;
  margin-bottom: 24px;
  padding-bottom: 0;
  width: 100%;
  font-family: 'Times New Roman', Times, serif !important;
}

.template-header-bar .header-tab {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  line-height: 1.2;
  padding: 5px 22px 5px 22px;
  display: inline-block;
  margin-bottom: -1px;
  letter-spacing: 0.2px;
}

.template-header-bar .header-title {
  color: #000000 !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  line-height: 1.2;
  padding-bottom: 4px;
  padding-right: 2px;
  text-align: right;
  letter-spacing: 0.2px;
}

/* Running Footer strictly matching teacher's Template 0 */
.template-footer-bar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-top: 2px solid #548dd4;
  margin-top: 32px;
  padding-top: 0;
  width: 100%;
  font-family: 'Times New Roman', Times, serif !important;
}

.template-footer-bar .footer-left {
  color: #000000 !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 10.5pt !important;
  padding-top: 6px;
  line-height: 1.2;
}

.template-footer-bar .footer-tab {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-weight: 700 !important;
  font-size: 11pt !important;
  padding: 4px 24px 6px 24px;
  min-width: 45px;
  text-align: center;
  line-height: 1.2;
  margin-top: -2px;
  display: inline-block;
  letter-spacing: 0.2px;
}

/* Cover Page Specific Styles (Template 0) */
.cover-page {
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  min-height: 297mm;
  height: 297mm;
  padding: 30mm 25mm 25mm 25mm !important;
  box-sizing: border-box !important;
}

.cover-doc-id {
  text-align: center;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 15pt !important;
  font-weight: 700 !important;
  color: #000000 !important;
  line-height: 1.4;
  margin-bottom: 35px;
  letter-spacing: 0.5px;
}

.proposal-banner {
  background-color: #548dd4;
  padding: 36px 30px;
  margin: 15px 0 25px 0;
  text-align: center;
}

.banner-title {
  color: #ffffff !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 32pt !important;
  font-weight: 700 !important;
  letter-spacing: 1.5px;
  line-height: 1.2;
  text-transform: uppercase;
}

.banner-subtitle {
  color: #ffffff !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 13.5pt !important;
  font-weight: 400 !important;
  margin-top: 10px;
  font-style: italic;
  opacity: 0.95;
}

.cover-meta-box {
  background-color: #f8fafc;
  border: 1px solid #cbd5e1;
  padding: 16px 22px;
  margin: 25px 0;
  border-radius: 4px;
  font-size: 11.5pt !important;
  line-height: 1.6;
  font-family: 'Times New Roman', Times, serif !important;
}

.cover-meta-box strong {
  color: #000000 !important;
}

.cover-institution-block-bottom {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 16px;
  margin-top: auto;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: 0;
}

.cover-logo-wrapper {
  width: 75px;
  height: 75px;
  flex-shrink: 0;
}

.cover-logo-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.cover-inst-text {
  text-align: left;
  line-height: 1.4;
  font-family: 'Times New Roman', Times, serif !important;
}

.inst-line-dept, .inst-line-faculty {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  font-weight: 700 !important;
  color: #000000 !important;
}

.inst-line-school {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12.5pt !important;
  font-weight: 700 !important;
  color: #366091 !important;
}

/* Headings Hierarchy strictly Times New Roman */
h1 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 16pt !important;
  font-weight: 700 !important;
  color: #366091 !important;
  margin-top: 26px !important;
  margin-bottom: 14px !important;
  padding-bottom: 4px !important;
  border-bottom: 2px solid #548dd4 !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

h2 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 14pt !important;
  font-weight: 700 !important;
  color: #366091 !important;
  margin-top: 22px !important;
  margin-bottom: 10px !important;
  padding-bottom: 3px !important;
  border-bottom: 1px solid #cbd5e1 !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

h3 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 13pt !important;
  font-weight: 700 !important;
  color: #366091 !important;
  margin-top: 18px !important;
  margin-bottom: 8px !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

h4 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12.5pt !important;
  font-weight: 700 !important;
  color: #4f81bd !important;
  margin-top: 14px !important;
  margin-bottom: 6px !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

h5 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  font-weight: 700 !important;
  font-style: italic !important;
  color: #26215c !important;
  margin-top: 12px !important;
  margin-bottom: 4px !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

h6 {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  font-weight: 700 !important;
  font-style: italic !important;
  color: #475569 !important;
  margin-top: 10px !important;
  margin-bottom: 4px !important;
  line-height: 1.3 !important;
  page-break-after: avoid;
}

p {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  line-height: 1.5 !important;
  color: #000000 !important;
  margin-top: 6px !important;
  margin-bottom: 10px !important;
  text-align: justify !important;
}

ul, ol {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  line-height: 1.5 !important;
  color: #000000 !important;
  margin-top: 6px !important;
  margin-bottom: 12px !important;
  padding-left: 28px !important;
}

li {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  line-height: 1.5 !important;
  margin-bottom: 4px !important;
  text-align: justify !important;
}

blockquote {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  line-height: 1.55 !important;
  border: 1px solid #cbd5e1 !important;
  background-color: #f8fafc !important;
  padding: 12px 18px !important;
  margin: 14px 0 !important;
  color: #1e293b !important;
  font-style: italic !important;
  border-radius: 4px !important;
}

blockquote p {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 12pt !important;
  font-style: italic !important;
  margin: 0 !important;
}

/* Captions for Tables and Figures */
.table-caption, .figure-caption {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 11.5pt !important;
  font-weight: 700 !important;
  text-align: center !important;
  margin: 8px 0 12px 0 !important;
  color: #000000 !important;
}

.figure-caption {
  font-style: italic !important;
  font-weight: 400 !important;
}

/* Table of Contents */
.toc-container {
  background-color: #fbfcfe;
  border: 1px solid #dbeafe;
  border-radius: 6px;
  padding: 24px 32px;
  margin: 15px 0 25px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-header-title {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 16pt !important;
  font-weight: 700 !important;
  color: #366091 !important;
  margin-top: 0 !important;
  margin-bottom: 18px !important;
  border-bottom: 2px solid #548dd4 !important;
  padding-bottom: 6px !important;
  text-align: center !important;
  text-transform: uppercase !important;
  letter-spacing: 0.5px !important;
}

.toc-list {
  list-style-type: none;
  padding-left: 0;
  margin: 0;
  font-size: 11.5pt !important;
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-item {
  margin-bottom: 5px;
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-link {
  color: #0f172a;
  text-decoration: none;
  display: flex;
  align-items: baseline;
  padding: 2px 4px;
  border-radius: 3px;
  transition: background-color 0.15s ease, color 0.15s ease;
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-link:hover {
  color: #366091;
  background-color: #eff6ff;
  text-decoration: none;
}

.toc-title-text {
  font-weight: 700 !important;
  font-size: 12pt !important;
  color: #0f172a !important;
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-sub-title-text {
  font-weight: 400 !important;
  font-size: 11.5pt !important;
  color: #334155 !important;
  font-family: 'Times New Roman', Times, serif !important;
}

.toc-dots {
  flex-grow: 1;
  border-bottom: 1px dotted #94a3b8;
  margin: 0 8px;
  min-width: 20px;
}

/* Tables strictly formatted to Template 0 */
table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 16px 0 20px 0 !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 11pt !important;
  line-height: 1.35 !important;
  page-break-inside: avoid;
}

th, td {
  border: 1px solid #cbd5e1 !important;
  padding: 8px 10px !important;
  vertical-align: top !important;
  font-family: 'Times New Roman', Times, serif !important;
}

th {
  background-color: #548dd4 !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  text-align: center !important;
  font-size: 11pt !important;
  border: 1px solid #548dd4 !important;
  vertical-align: middle !important;
}

td {
  font-size: 11pt !important;
  line-height: 1.45 !important;
  color: #000000 !important;
}

tr:nth-child(even) td {
  background-color: #f8fafc !important;
}

.align-center {
  text-align: center !important;
}

.align-right {
  text-align: right !important;
}

.align-left {
  text-align: left !important;
}

/* Inline Code, Badges, & Pre Blocks */
code {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 11pt !important;
  font-weight: 600 !important;
  background-color: #f1f5f9 !important;
  padding: 1px 6px !important;
  border-radius: 3px !important;
  border: 1px solid #cbd5e1 !important;
  color: #0f172a !important;
}

.commit-badge, .entry-badge {
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 11pt !important;
  font-weight: 700 !important;
  color: #1e3a8a !important;
  background-color: #e0f2fe !important;
  padding: 2px 7px !important;
  border-radius: 4px !important;
  border: 1px solid #bae6fd !important;
  display: inline-block !important;
}

pre {
  background-color: #0f172a !important;
  color: #f8fafc !important;
  padding: 12px 16px !important;
  border-radius: 6px !important;
  overflow-x: auto !important;
  font-family: 'Times New Roman', Times, serif !important;
  font-size: 11pt !important;
  margin: 14px 0 !important;
}

pre code {
  background-color: transparent !important;
  color: inherit !important;
  border: none !important;
  padding: 0 !important;
  font-family: 'Times New Roman', Times, serif !important;
}

.mermaid, .svg-diagram-wrapper {
  background-color: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 16px;
  margin: 20px auto;
  text-align: center;
  max-width: 100%;
  overflow-x: auto;
}

.svg-diagram-wrapper svg {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

/* Floating Back to Top Button */
.back-to-top {
  position: fixed;
  bottom: 25px;
  right: 25px;
  background-color: var(--primary-blue);
  color: #ffffff !important;
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 10pt !important;
  font-weight: 700 !important;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(0, 112, 192, 0.3);
  display: flex;
  align-items: center;
  gap: 5px;
  transition: transform 0.15s ease, background-color 0.15s ease;
  z-index: 1000;
  font-family: 'Times New Roman', Times, serif !important;
}

.back-to-top:hover {
  background-color: #005a9e;
  transform: translateY(-2px);
  color: #ffffff !important;
}

/* Print Styles for A4 Paper Export */
@media print {
  body {
    background-color: #ffffff;
    padding: 0;
    margin: 0;
  }
  .doc-page {
    box-shadow: none;
    border: none;
    border-radius: 0;
    max-width: 100%;
    padding: 0;
    margin: 0;
    min-height: auto;
    page-break-after: always;
    break-after: page;
  }
  .doc-page:last-of-type {
    page-break-after: avoid;
    break-after: avoid;
  }
  .page-break-divider {
    display: none;
  }
  .back-to-top {
    display: none !important;
  }
  table, pre, .mermaid, blockquote {
    page-break-inside: avoid;
  }
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
  }
}
"""
