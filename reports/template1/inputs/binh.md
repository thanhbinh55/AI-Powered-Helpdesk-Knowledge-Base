# Biên bản Bàn giao & Đối soát Markdown — Ngô Viết Thanh Bình

> **Thành viên phụ trách:** Ngô Viết Thanh Bình (Trưởng nhóm / DevOps)  
> **Mã task liên quan:** [T1-DOC-04](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-04), [T1-DOC-MD](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-md), [T1-SUBMIT-01](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-submit-01).  
> **Phạm vi nghiệp vụ:** Module D (Identity & Access): `FR-ID-01`..`09`, `US-01`..`06`, `27`, `UC-01`..`04`, `16`; Sơ đồ tổng thể 17 Use Cases.  
> **Tài liệu soạn thảo chung:** [[SE - Nhóm 4] template1 - Google Docs](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0).  
> **Bản thiết kế Figma (Redesign v2):** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev) & kho 151 ảnh PNG tại `docs/design/anh/`.

---

## 1. Lộ trình Triển khai & Cột mốc Bắt buộc
- **Soạn thảo trực tiếp trên Google Docs:** từ 03/11 đến trước **23:59 ngày 07/11/2026**.
- **Đóng băng bản nháp (Draft Freeze):** lúc **23:59 ngày 07/11/2026** trên Google Docs.
- **Review chéo xoay vòng:** hoàn thành trước **23:59 ngày 08/11/2026** (Reviewer: Quý Phúc phản biện, góp ý trực tiếp trên Docs).
- **Task T1-DOC-MD — Chuyển đổi Markdown, xuất SVG & Commit Git:** Hoàn tất sửa đổi sau review, chuyển đổi toàn bộ nội dung sang file `.md`, xuất sơ đồ vector `.svg` nộp vào repo và mở PR trước **23:59 ngày 10/11/2026**.
- **Rà soát kỹ thuật & Khởi động code MVP:** ngày **11/11/2026** (ghép nối kỹ thuật Template 1; bắt đầu Scaffolding `T1-DEV-01` và Template 2 `T2-ARCH-01`).
- **Final nộp bài Template 1:** Trưởng nhóm tổng hợp, render bản HTML/PDF chuẩn A4 và nộp bài chính thức trước **23:59 ngày 12/11/2026**.

---

## 2. Danh mục File Markdown & Sơ đồ Bàn giao (Task T1-DOC-MD)
- [ ] `reports/template1/04-dac-ta-use-cases/04.1-so-do-tong-the.md` (Sơ đồ tổng thể 17 Use Cases toàn hệ thống, ranh giới 4 phân hệ).
- [ ] `reports/template1/04-dac-ta-use-cases/04.2-module-D-identity.md` (Đặc tả 5 Use Cases chuẩn 9 trường: UC-01..04, UC-16).
- [ ] `reports/template1/assets/diagrams/uc-overview.svg` & `uc-overview.drawio` (Sơ đồ Use Case tổng quan).
- [ ] `reports/template1/assets/diagrams/uc-module-D.svg` & `uc-module-D.drawio` (Sơ đồ Use Case phân hệ Identity).
- [ ] Ánh xạ màn hình Figma Identity (Frames Node ID `62:8214` đến `62:14361`, ảnh PNG tại `docs/design/anh/`).
- [x] Nhật ký AI Usage giai đoạn Template 1 cập nhật đầy đủ tại [reports/template1/06-ai-usage.md](../06-ai-usage.md) (theo đúng quy chuẩn 2 bước tại Mục 1.2 kế hoạch).

---

## 3. Tiêu chí Nghiệm thu Bàn giao (DoD)
1. 100% Use Cases của module D có đủ 9 trường chuẩn, văn phong nghiệp vụ ngắn gọn, không sa đà vào chi tiết cài đặt backend.
2. Sơ đồ Use Case tổng thể 19 Use Cases xuất file `.svg` chuẩn UML, nét liền tam giác rỗng generalization và người que.
3. Chuyển đổi chính xác từ Google Docs sang các file Markdown được phân công, **giữ nguyên 100% nội dung đã thống nhất**.
4. **LƯU Ý VỀ HÌNH ẢNH:** Thành viên chỉ cần ghi tiêu đề ảnh (Hình 4.xx, 5.xx...); Trưởng nhóm sẽ tự tổng hợp và chèn mã nhúng ảnh thật vào tài liệu master.
5. Cập nhật nhật ký AI Usage nếu có vào [`reports/template1/06-ai-usage.md`](../06-ai-usage.md).
6. Commit Git có gắn mã Jira `SCRUM-xx`, PR mở và merge vào `main`.

---

## 4. Bàn giao Markdown từ bản xuất ngày 12/11/2026

- **Nguồn:** `[SE - Nhóm 4] Template 1 (1).md` do Thanh Bình cung cấp.
- **Task đã ánh xạ:** `T1-DOC-04` → `SCRUM-30`; `T1-DOC-MD` → `SCRUM-34` (theo `scripts/jira/tasks_created.csv`). `SCRUM-65` là task thông báo phân công, không thay mã task chuyển đổi.
- [x] Chuyển mục 4.1.1 vào `04-dac-ta-use-cases/04.1-so-do-tong-the.md`: tổng thể **19 Use Cases**.
- [x] Chuyển mục 4.1.2 và đủ 5 bảng đặc tả (9 trường/bảng) UC-01, UC-02, UC-03, UC-04, UC-16 vào `04-dac-ta-use-cases/04.2-module-D-identity.md`.
- [x] Bổ sung phần 5.1 Identity từ nguồn ở cuối `05-prototype-mockup.md` để người tổng hợp UI tiếp nhận; giữ nguyên phần thiết kế chung hiện có.
- [x] Giữ nguyên câu chữ nguồn và tiêu đề hình; không nhúng hình theo quy định chuyển đổi Markdown. Các tệp SVG/drawio hiện có được giữ nguyên, chưa đối chiếu hình nguồn trong phiên này.
- [x] Cập nhật phần AI usage của Bình trong `06-ai-usage.md`; giữ nguyên phần của thành viên khác.
- [ ] Quý Phúc review nội dung và xác nhận nghiệm thu.
- [ ] Trưởng nhóm tổng hợp hình ảnh và bản nộp cuối.

**Lưu ý đối soát:** Các dòng nhắc 17 Use Cases/Module D ở biên bản cũ là thông tin lịch sử; bản nguồn hiện tại có 19 Use Cases và dùng tên phân hệ. Việc chuyển đổi không xác nhận các checklist review/merge trước đó đã hoàn thành.
