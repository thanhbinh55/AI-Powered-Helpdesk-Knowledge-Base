# Biên bản Bàn giao & Đối soát Markdown — Phan Gia Phúc

> **Thành viên phụ trách:** Phan Gia Phúc (Ticket & QA Lead)  
> **Mã task liên quan:** [T1-DOC-03](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-03), [T1-DOC-05](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-05), [T1-DOC-MD](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-md).  
> **Phạm vi nghiệp vụ:** Module C (Ticket Management): `FR-TK-01`..`12`, `US-07`..`17`, `28`, `29`, `UC-05`..`10`; Ma trận 41 FRs ↔ 30 USs.  
> **Tài liệu soạn thảo chung:** [[SE - Nhóm 4] template1 - Google Docs](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0).  
> **Bản thiết kế Figma (Redesign v2):** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev) & kho 151 ảnh PNG tại `docs/design/anh/`.

---

## 1. Lộ trình Triển khai & Cột mốc Bắt buộc
- **Soạn thảo trực tiếp trên Google Docs:** từ 03/11 đến trước **23:59 ngày 07/11/2026**.
- **Đóng băng bản nháp (Draft Freeze):** lúc **23:59 ngày 07/11/2026** trên Google Docs.
- **Review chéo xoay vòng:** hoàn thành trước **23:59 ngày 08/11/2026** (Reviewer: Lãm phản biện, góp ý trực tiếp trên Docs).
- **Task T1-DOC-MD — Chuyển đổi Markdown, xuất SVG & Commit Git:** Hoàn tất sửa đổi sau review, chuyển đổi toàn bộ nội dung sang file `.md`, xuất sơ đồ vector `.svg` nộp vào repo và mở PR trước **23:59 ngày 10/11/2026**.
- **Rà soát kỹ thuật & Khởi động code MVP:** ngày **11/11/2026** (chốt hợp đồng API DTOs `T1-CONTRACT-01` và phối hợp ghép nối Template 1).
- **Final nộp bài Template 1:** Độc lập rà soát, kiểm tra gói nộp trước khi Bình nộp chính thức trước **23:59 ngày 12/11/2026**.

---

## 2. Danh mục File Markdown & Sơ đồ Bàn giao (Task T1-DOC-MD)
- [ ] `reports/template1/03-tong-quan-yeu-cau/03.2.1-yeu-cau-chuc-nang.md` (Bảng ma trận truy vết toàn diện 41 FRs ↔ 30 User Stories).
- [ ] `reports/template1/04-dac-ta-use-cases/04.2-module-C-ticket.md` (Đặc tả 6 Use Cases chuẩn 9 trường: UC-05..10).
- [ ] `reports/template1/assets/diagrams/uc-module-C.svg` & `uc-module-C.drawio` (Sơ đồ Use Case phân hệ Ticket Management).
- [ ] Ánh xạ màn hình Figma Ticket (Frames Node ID `55:1992` đến `62:15156`, ảnh PNG tại `docs/design/anh/`).
- [ ] Bàn giao phạm vi `US-28 / FR-TK-12` (Analytics P1) cho Quý Phúc để viết `04.2-uc-17-analytics.md`.
- [ ] Nhật ký AI Usage cá nhân cập nhật đầy đủ tại [reports/07-ai-usage.md](../../07-ai-usage.md).

---

## 3. Tiêu chí Nghiệm thu Bàn giao (DoD)
1. 100% Use Cases của module C có đủ 9 trường chuẩn, thể hiện rõ atomic claim lock, state machine và phân quyền tin nhắn.
2. Bảng ma trận 41 FRs và 30 User Stories khớp 100% với SRS-master Mục 3.2 và 4.
3. Sơ đồ Use Case vẽ chuẩn UML, xuất định dạng `.svg` sắc nét, không gãy font tiếng Việt.
4. Commit Git có gắn mã Jira `SCRUM-xx`, PR mở trước **23:59 ngày 10/11/2026** và đã được reviewer approve.
