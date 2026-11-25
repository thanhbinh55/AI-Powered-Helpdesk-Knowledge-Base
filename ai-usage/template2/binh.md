# Nhật ký sử dụng AI — Template 2 (Ngô Viết Thanh Bình - `24120269`)

> Ghi nhận các phiên làm việc với AI phục vụ thiết kế phần mềm Template 2 (`docs/template2/members/binh/`).  
> Mỗi phiên ghi đủ 7 trường chuẩn theo quy định Khoa CNTT & `TEAM_GUIDE_PHASE2.md`: Thời gian, Tác giả, Công cụ/Model, Prompt đã khử dữ liệu nhạy cảm, Nội dung AI tạo, Nội dung tự kiểm chứng & hiệu chỉnh, Minh chứng/Commit.

---

### Phiên T2-01 — Soạn thảo Mục 3.1: Cây phân rã hệ thống & Kiến trúc tổng thể 3-Tier / Modular Monolith (20/11/2026)

* **1. Thời gian:** 2026-11-20 14:30 – 17:45
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm)
* **3. Công cụ / Model:** Antigravity IDE (Gemini 3.8 Flash & Claude 3.5 Sonnet)
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Dựa trên tài liệu SRS-master.md (Mục 9), MVP_CONTRACTS.md và 19 Use Cases đã chốt ở Template 1 của dự án Clarune Helpdesk, hãy soạn thảo Mục 3.1 Thiết kế kiến trúc gồm: (3.1.1) Sơ đồ cây phân rã chức năng hệ thống theo chiều dọc ánh xạ 19 Use Cases; (3.1.2–3.1.6) Kiến trúc tổng quan 3 tầng (Presentation React + TypeScript + Vite, Business Logic Spring Boot 3 Modular Monolith Java 21, Data Layer PostgreSQL 16 + pgvector trên Supabase Singapore & Private File Storage); (3.1.7) Bảng công nghệ sử dụng và 6 mẫu thiết kế (Design Patterns) áp dụng."*
* **5. Nội dung AI tạo:**
  - Bản thảo mô tả chi tiết các mục `3.1.1` đến `3.1.6` theo mô hình Client–Server 3 tầng kết hợp Modular Monolith.
  - Khung bảng tổng hợp công nghệ (`3.1.7.A`) cho 8 lớp kỹ thuật (Frontend, UI Styling & HTTP, Backend Core, Security, Persistence & Migration, Document Parsing, AI & RAG Integration, Testing & DevOps).
  - Mô tả 6 điểm đặc biệt và mẫu thiết kế (`3.1.7.B`): State Machine Pattern, Optimistic Locking & Atomic Claim, Lease-Based Background Worker, Strategy & Adapter Pattern, Human-in-the-Loop Workflow, và Phòng chống Prompt Injection & Kiểm chứng Trích dẫn.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - *Phân định rõ số lượng module:* AI ban đầu gộp chung thành "5 Module độc lập"; tác giả đã đối chiếu với `reports/planning/TEMPLATE2_3_ALIGNMENT.md` và hiệu chỉnh thống nhất tại `3.1.1`, `3.1.3` và `3.2` thành **"4 Module nghiệp vụ độc lập (`Identity`, `Ticket`, `Knowledge`, `AI`) cùng 1 gói điều phối giao dịch liên module (`Workflow`)"**.
  - *Đối chiếu cấu hình thực tế của repo:* Kiểm tra trực tiếp với `backend/pom.xml` (Java 21 LTS, Spring Boot 3.3.5, Flyway, PostgreSQL) và `frontend/package.json` (React 18.3.1, TypeScript 5.6.2, Vite 6.0.1, Tailwind CSS 3.4.15); đổi cột *"Phiên bản dự kiến"* thành *"Phiên bản / Tiêu chuẩn áp dụng"* và lược bỏ các số phiên bản cứng của thư viện chưa cài đặt để tránh mâu thuẫn với khung scaffold nền tảng.
  - *Chốt mô hình nhúng theo DEC-06:* Đồng bộ dòng `AI & RAG Integration` trong Bảng công nghệ (`3.1.7.A`) theo đúng quyết định `DEC-06` đã chốt cùng nhóm Knowledge/AI là **`Mô hình ngôn ngữ lớn (LLM: GPT-4o-mini) & Mô hình nhúng Vector (gemini-embedding-2, 768 chiều)`**, khớp với `vector(768)` tại Mục 3.3.3, Flyway V3 (`4.1`), Hình 4.1 ERD và Bảng 4.8 (`4.2`).
* **7. Minh chứng / Commit:**
  - Jira Task: `SCRUM-59` (`T2-ARCH-01`)
  - File bàn giao: [`docs/template2/members/binh/03-thiet-ke-kien-truc.md`](../../docs/template2/members/binh/03-thiet-ke-kien-truc.md)

---

### Phiên T2-02 — Vẽ sơ đồ nguồn Draw.io & Kết xuất SVG/PNG cho Hình 3.1 và Hình 3.2 (22/11/2026)

* **1. Thời gian:** 2026-11-22 19:30 – 22:15
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity IDE (Gemini 3.8 Flash) & Draw.io
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Tạo file nguồn sơ đồ Draw.io (.drawio) và SVG độ phân giải cao (1760x990) cho 2 hình ở Mục 3.1: (1) Hình 3.1 Sơ đồ cây phân rã chức năng hệ thống Clarune theo chiều dọc gồm 4 Module ánh xạ đủ 19 Use Cases (UC-01..UC-19, đánh dấu rõ nét đứt màu xám cho các UC hoãn P1: UC-16, UC-17, UC-19) kết nối xuống Server Spring Boot và Database PostgreSQL; (2) Hình 3.2 Sơ đồ tổng quan kiến trúc 3 tầng kết hợp Modular Monolith thể hiện rõ luồng gọi HTTPS/REST, Public Ports một chiều (DAG), JDBC SSL tới Supabase Cloud pgvector, File I/O tới Private File Storage và SMTP [P1]."*
* **5. Nội dung AI tạo:**
  - Cấu trúc XML `.drawio` và вектор `.svg` cho 2 sơ đồ `system-decomposition-tree` và `system-architecture`.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Kiểm tra đối chiếu từng mã Use Case (`UC-01` đến `UC-19`) trên **Hình 3.1** khớp với danh mục Use Case của `Template 1`, đảm bảo cả 3 chức năng mở rộng (`UC-16` Đặt lại mật khẩu, `UC-17` Báo cáo thống kê Ticket, `UC-19` Đánh giá câu trả lời hữu ích) đều có nhãn `[P1] (Hoãn P1)` và viền nét đứt.
  - Trên **Hình 3.2**, kiểm tra chiều mũi tên giữa các thành phần trong Tầng 2 (`Workflow` $\to$ `AI` / `Ticket`, `AI` $\to$ `Ticket` / `Knowledge`, `Ingestion Worker` $\to$ `Knowledge`) đảm bảo đồ thị phụ thuộc một chiều có hướng (DAG), không có phụ thuộc vòng, và tách biệt rõ tiến trình chạy ngầm `Ingestion Worker (Async Background Task)` bằng khung nét đứt.
* **7. Minh chứng / Commit:**
  - Jira Task: `SCRUM-59` (`T2-ARCH-01`)
  - Tệp sơ đồ: [`docs/template2/members/binh/diagrams/system-decomposition-tree.drawio`](../../docs/template2/members/binh/diagrams/system-decomposition-tree.drawio), [`system-decomposition-tree.svg`](../../docs/template2/members/binh/diagrams/system-decomposition-tree.svg), [`system-decomposition-tree.png`](../../docs/template2/members/binh/diagrams/system-decomposition-tree.png), [`system-architecture.drawio`](../../docs/template2/members/binh/diagrams/system-architecture.drawio), [`system-architecture.svg`](../../docs/template2/members/binh/diagrams/system-architecture.svg), [`system-architecture.png`](../../docs/template2/members/binh/diagrams/system-architecture.png)

---

### Phiên T2-03 — Review chéo trên Google Doc chung, xử lý bình luận đối soát & đồng bộ bản chốt (24/11 – 25/11/2026)

* **1. Thời gian:** 2026-11-24 17:45 – 2026-11-25 17:30
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity IDE (Gemini 3.8 Flash & Gemini 4 Argon Medium) + Google Workspace `gdocs` CLI
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Kiểm tra toàn bộ các bình luận (comments) review chéo mới nhất trên Google Doc Template 2 của nhóm, đối chiếu với Template 1 final (report.md), SRS-master.md, MVP_CONTRACTS.md và các sơ đồ lớp Mục 3.2 để cập nhật lại Hình 3.2, chuẩn hóa bảng đặc tả lớp Mục 3.3 và bảng sự kiện giao diện Mục 5.2 cho khớp hoàn toàn với bản chốt của nhóm."*
* **5. Nội dung AI tạo:**
  - Danh sách trích xuất và phân tích chi tiết các bình luận review trên Google Doc cùng phương án chỉnh sửa đồng bộ cho từng mục.
  - Bản kết xuất mới của `system-architecture.drawio` / `.svg` / `.png` (**Hình 3.2**) và nội dung cập nhật các bảng đặc tả.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - *Xử lý Comment trên Hình 3.2 (`doco.mKNfx-aRg-AccyCxa5Bsfg`):* Sửa nhãn khung chứa module ở Tầng 2 trên Hình 3.2 từ `"5 Business Modules + Worker"` thành **`"4 Module nghiệp vụ + Workflow + Worker — Public Ports một chiều (DAG)"`** để khớp với mục `3.1.3`, kết xuất lại PNG `1760×990` và thay ảnh trực tiếp trên Google Doc.
  - *Xử lý Comment về chữ ký Public Ports & phân công Controller (`doco.G3-v0SXvRsVr7VMfQLVgCA`, `doco.5ad3qC_WokDdF-RApf7fnw`):* Đối chiếu trực tiếp với bộ sơ đồ lớp **Hình 3.3a..3.3e** mới cập nhật của Gia Phúc, chuẩn hóa chữ ký `TicketContextProvider` (`getForSuggestion`, `lockTicket`, `appendSuggestionReply`), `KnowledgeRetriever` (`search`, `areChunksStillPublishable`), `AISuggestionCommandPort` (`lockGenerated`, `markApplied`, `discard`), tách dòng riêng cho `WorkflowController` (`workflow.api`: `postMessage`, `discard`) và ghi rõ thứ tự khóa cố định: **(1) `lockTicket` $\to$ (2) `lockGenerated` $\to$ (3) `appendSuggestionReply` $\to$ (4) `markApplied`**.
  - *Xử lý Comment về `updatePriority` (`doco.0dOhjWAgXFiYrAna6tRxng`):* Đối chiếu `SRS-master.md` (mục 4.2 FR-TK chỉ chốt mặc định `priority = NORMAL` cho P0), đánh dấu rõ `updatePriority` (`PATCH /api/v1/tickets/{id}/priority`) và sự kiện `PRIORITY_CHANGED` thuộc **Backlog/P1** tại Bảng `Ticket`, `TicketEvent`, `TicketController` (§3.3.2) và Bảng 4.3, 4.5 (§4.2).
  - *Xử lý Comment ở Mục 5 Giao diện (`doco.vNlGTtofpDHryxudvJUlbw`, `doco.SAqvA26nLeZcsSpGt_xCVw`, `doco.6Olc5pl2kgf48qUhzZ_dwg`):* Bổ sung `confirmPassword` vào payload JSON của `UC-01` (`I02`) và `UC-03` (`I03/I04`) kiểm tra ở cả UI lẫn Backend; thống nhất truyền `{ ..., version }` và trả `HTTP 409 TICKET_VERSION_CONFLICT` cho mọi thao tác `claim`, `transitions` (`CLOSE`, `REOPEN`, `REQUEST_INFO`, `RESOLVE`) và `assignment`; làm rõ ánh xạ trạng thái `ARCHIVED` trên bảng `K04` (cột Xử lý giữ `Sẵn sàng`, cột Công bố hiển thị badge `ĐÃ LƯU TRỮ`).
* **7. Minh chứng / Commit:**
  - Jira Task: `SCRUM-59` (`T2-ARCH-01`), `SCRUM-62` (`T2-REVIEW-01`), `SCRUM-55` (`QA1-T2-01`)
  - Nhánh Git: `docs/t2-binh`
