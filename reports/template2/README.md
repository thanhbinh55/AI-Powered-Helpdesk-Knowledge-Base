# Gói nộp Template 2 — Thiết kế Phần mềm — Clarune (Nhóm 04)

Thư mục này chứa toàn bộ gói nộp chính thức **Template 2** của Nhóm 04 (đồng nhất cấu trúc với [`reports/template1/`](../template1/)):

- **`4.zip`**: Gói nén chuẩn để nộp cổng trường, chứa đúng 3 thư mục cấp cao nhất: `ai-usage/`, `git-contributions/`, `report/`.
- **`report/`**:
  - [`Report.pdf`](report/Report.pdf): Bản báo cáo chính thức 84 trang xuất từ Google Docs (`[SE - Nhóm 4] Template2-ThietKe-Clarune-04`).
  - [`report.md`](report/report.md): Bản Markdown đồng bộ 100% từng câu chữ và bảng biểu với `Report.pdf`, gắn 26 đường dẫn hình ảnh sắc nét trong `report/assets/`.
  - [`assets/diagrams/`](report/assets/diagrams/): 10 sơ đồ kiến trúc, EER, Class Diagram (5 hình `2000px`), Physical ERD và Screen Flow kèm tệp nguồn `.drawio`/`.svg`.
  - [`assets/ui/`](report/assets/ui/): 16 ảnh màn hình giao diện Clarune Redesign v3 (`1440×900`).
- **`ai-usage/`**:
  - [`ai-usage.md`](ai-usage/ai-usage.md) và [`ai-usage.html`](ai-usage/ai-usage.html): Nhật ký sử dụng AI tổng hợp trung thực từ 18 phiên cá nhân của 4 thành viên và 1 phiên đóng gói (`T2-01`..`T2-19`), định dạng chuẩn A4 Times New Roman như Template 1.
- **`git-contributions/`**:
  - [`git-contributions.md`](git-contributions/git-contributions.md) và [`git-contributions.html`](git-contributions/git-contributions.html): Báo cáo lịch sử Commit Git và Pull Requests giai đoạn Template 2 của 4 thành viên.
- **`sources/`**: Lưu trữ toàn bộ tài liệu nguồn của 4 thành viên (`ai-usage-*.md`, `members/`, `diagrams/`, `pdf-assets/`, `git-snapshot.json`, `report-baseline.json`) phục vụ kiểm toán và tái tạo gói nộp qua `python3 scripts/package_template2.py`.
