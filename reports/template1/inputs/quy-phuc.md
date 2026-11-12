# Biên bản Bàn giao & Đối soát Markdown — Lê Quý Phúc

> **Thành viên phụ trách:** Lê Quý Phúc (AI & UI/UX Lead)  
> **Mã task liên quan:** [T1-DOC-01](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-01), [T1-DOC-07](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-07), [T1-UI-01](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-ui-01), [T1-DOC-MD](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-md).  
> **Phạm vi nghiệp vụ:** Module A (AI Assistance): `FR-AI-01`..`10`, `US-22`..`26`, `30`, `UC-14`, `15`, `18`, `19` (P1); Ticket Analytics P1: `UC-17`; Trang bìa & Đóng góp thành viên; Mô tả bài toán; Tổng hợp Prototype Figma 229 frames.
> **Tài liệu soạn thảo chung:** [[SE - Nhóm 4] template1 - Google Docs](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0).  
> **Bản thiết kế Figma (Redesign v2):** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev) & bộ thiết kế 34 nhóm màn hình, 229 frames, 82 flow points; ảnh final tại `report/assets/ui/`.

---

## 1. Lộ trình Triển khai & Cột mốc Bắt buộc
- **Soạn thảo trực tiếp trên Google Docs:** từ 03/11 đến trước **23:59 ngày 07/11/2026**.
- **Đóng băng bản nháp (Draft Freeze):** lúc **23:59 ngày 07/11/2026** trên Google Docs.
- **Review chéo xoay vòng:** hoàn thành trước **23:59 ngày 08/11/2026** (Reviewer: Gia Phúc phản biện, góp ý trực tiếp trên Docs).
- **Task T1-DOC-MD — Chuyển đổi Markdown, xuất SVG & Commit Git:** Hoàn tất sửa đổi sau review, chuyển đổi toàn bộ nội dung sang file `.md`, xuất sơ đồ vector `.svg` nộp vào repo và mở PR trước **23:59 ngày 10/11/2026**.
- **Rà soát kỹ thuật & Khởi động code MVP:** ngày **11/11/2026** (cấu hình GitHub Actions CI `T1-CI-01` và hỗ trợ ghép nối Template 1).
- **Final nộp bài Template 1:** Kiểm tra liên kết xem công khai của prototype Figma trước **23:59 ngày 12/11/2026**.

---

## 2. Danh mục File Markdown & Sơ đồ Bàn giao (Task T1-DOC-MD)
- [ ] `reports/template1/01-danh-gia-thanh-vien.md` (Trang bìa, danh sách thành viên, tỷ lệ đóng góp có xác nhận).
- [ ] `reports/template1/02-mo-ta-bai-toan.md` (Bối cảnh, phát biểu bài toán, mục tiêu đo được, môi trường vận hành).
- [ ] `reports/template1/04-dac-ta-use-cases/04.2-module-A-ai.md` (Đặc tả 2 Use Cases chuẩn 9 trường: UC-14, UC-15).
- [ ] `reports/template1/04-dac-ta-use-cases/04.2-uc-17-analytics.md` (Đặc tả Use Case phân tích báo cáo: UC-17).
- [ ] `reports/template1/05-prototype-mockup.md` (Ma trận tổng hợp 34 nhóm màn hình / 229 frames Figma).
- [ ] `reports/template1/report/assets/diagrams/uc_module_a_ai_analytics.svg` & `uc-module-A.drawio` (Sơ đồ Use Case phân hệ AI Assistance).
- [ ] Ánh xạ màn hình Figma AI & Analytics (Frames Node ID `55:1874` đến `62:15617`, ảnh PNG tại `docs/design/anh/`).
- [ ] Nhật ký AI Usage giai đoạn Template 1 cập nhật đầy đủ tại [reports/template1/06-ai-usage.md](../06-ai-usage.md) (theo đúng quy chuẩn 2 bước tại Mục 1.2 kế hoạch).

---

## 3. Tiêu chí Nghiệm thu Bàn giao (DoD)
1. 100% Use Cases của module A và Analytics có đủ 9 trường chuẩn, thể hiện rõ citation verification, abstention rule và workflow duyệt gợi ý.
2. Link view Figma hoạt động ổn định với tài khoản bên ngoài nhóm (không yêu cầu đăng nhập chỉnh sửa).
3. Chuyển đổi chính xác từ Google Docs sang các file Markdown được phân công, **giữ nguyên 100% nội dung đã thống nhất (tuyệt đối không tự ý thay đổi nội dung)**.
4. **LƯU Ý VỀ HÌNH ẢNH / MOCKUP:** Những phần nào có hình ảnh/sơ đồ/mockup, thành viên **chỉ cần ghi tiêu đề của ảnh** (ví dụ: `Hình 4.xx ...`, `Hình 5.xx ...`) đúng theo vị trí trên Google Docs; **KHÔNG CẦN chèn link ảnh hay tải file ảnh lên**. Trưởng nhóm (Bình) sẽ tự thêm mã nhúng ảnh thật trong mã Markdown tổng hợp sau.
5. Nếu có sử dụng AI trong quá trình làm bài, cập nhật đầy đủ nhật ký vào [`reports/template1/06-ai-usage.md`](../06-ai-usage.md) theo chuẩn 2 bước.
6. Commit Git có gắn mã Jira `SCRUM-xx`, PR mở trước **23:59 ngày 10/11/2026** và đã được reviewer approve.
