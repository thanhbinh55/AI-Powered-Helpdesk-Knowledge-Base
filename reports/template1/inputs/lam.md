# Biên bản Bàn giao & Đối soát Markdown — Nguyễn Đức Lãm

> **Thành viên phụ trách:** Nguyễn Đức Lãm (Knowledge Base & Database Lead)  
> **Mã task liên quan:** [T1-DOC-02](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-02), [T1-DOC-06](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-06), [T1-DOC-MD](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-doc-md), [T1-PUB-01](../../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md#t1-pub-01).  
> **Phạm vi nghiệp vụ:** Module B (Knowledge Base): `FR-KB-01`..`10`, `US-18`..`21`, `UC-11`..`13`; Stakeholders; Yêu cầu phi chức năng (NFR); Điều phối thu nhận Markdown và đóng gói Template 1.  
> **Tài liệu soạn thảo chung:** [[SE - Nhóm 4] template1 - Google Docs](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0).  
> **Bản thiết kế Figma (Redesign v2):** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev) & kho 151 ảnh PNG tại `docs/design/anh/`.

---

## 1. Lộ trình Triển khai & Cột mốc Bắt buộc
- **Soạn thảo trực tiếp trên Google Docs:** từ 03/11 đến trước **23:59 ngày 07/11/2026**.
- **Đóng băng bản nháp (Draft Freeze):** lúc **23:59 ngày 07/11/2026** trên Google Docs.
- **Review chéo xoay vòng:** hoàn thành trước **23:59 ngày 08/11/2026** (Reviewer: Bình phản biện, góp ý trực tiếp trên Docs).
- **Task T1-DOC-MD — Chuyển đổi Markdown, xuất SVG & Điều phối thu nhận:** Hoàn tất sửa đổi sau review, chuyển đổi toàn bộ nội dung sang file `.md`, xuất sơ đồ vector `.svg` nộp vào repo, mở PR và tiếp nhận bản nộp của 4 module trước **23:59 ngày 10/11/2026**.
- **Rà soát kỹ thuật & Khởi động code MVP:** ngày **11/11/2026** (ghép nối kỹ thuật Template 1; khởi động Schema baseline `T1-SCHEMA-01` và Conceptual Model `T2-MODEL-01`).
- **Đóng gói phát hành Template 1 (T1-PUB-01):** Render HTML/PDF khổ A4 chuẩn Word, đóng gói hoàn thiện bàn giao cho Bình trước **23:59 ngày 12/11/2026**.

---

## 2. Danh mục File Markdown & Sơ đồ Bàn giao (Task T1-DOC-MD)
- [ ] `reports/template1/03-tong-quan-yeu-cau/03.1-stakeholders.md` (Bảng phân tích Stakeholders).
- [ ] `reports/template1/03-tong-quan-yeu-cau/03.2.2-yeu-cau-phi-chuc-nang.md` (Bảng NFRs đầy đủ thước đo kiểm chứng).
- [ ] `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md` (Đặc tả 3 Use Cases chuẩn 9 trường: UC-11..13).
- [ ] `reports/template1/assets/diagrams/context-diagram.svg` & `context-diagram.drawio` (Sơ đồ Bối cảnh hệ thống).
- [ ] `reports/template1/assets/diagrams/uc-module-B.svg` & `uc-module-B.drawio` (Sơ đồ Use Case phân hệ Knowledge Base).
- [ ] Ánh xạ màn hình Figma Knowledge Base (Frames Node ID `62:9092` đến `62:11768`, ảnh PNG tại `docs/design/anh/`).
- [ ] Kiểm tra tiếp nhận đủ 4 biên bản bàn giao tại `reports/template1/inputs/{binh,gia-phuc,lam,quy-phuc}.md`.
- [ ] Nhật ký AI Usage cá nhân cập nhật đầy đủ tại [reports/07-ai-usage.md](../../07-ai-usage.md).

---

## 3. Tiêu chí Nghiệm thu Bàn giao (DoD)
1. 100% Use Cases của module B có đủ 9 trường chuẩn, thể hiện rõ quy trình Ingestion Worker nền SKIP LOCKED và phân quyền tài liệu.
2. Bảng NFR giữ nguyên mã, mức yêu cầu và cách đo kiểm chứng từ SRS Mục 8.
3. Sơ đồ Bối cảnh và Use Case phân hệ xuất file `.svg` chuẩn, link ảnh trong Markdown không bị hỏng.
4. Thu nhận đủ 100% file `.md` và `.svg` của cả 4 module trên Git trước **23:59 ngày 10/11/2026** để chuẩn bị ghép nối bài nộp.
