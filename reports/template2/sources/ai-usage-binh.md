# Nhật ký sử dụng AI — Template 2 (Ngô Viết Thanh Bình - `24120269`)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base (Clarune)  
> **Nhóm thực hiện:** Nhóm 04 — Lớp Nhập môn Công nghệ Phần mềm (CS10014), Trường ĐHKHTN, ĐHQG-HCM  
> **Thành viên:** Ngô Viết Thanh Bình (`24120269` — Trưởng nhóm · Phụ trách Mục 3.1 Kiến trúc hệ thống & Điều phối đối soát Template 2)  
> **Thư mục bàn giao cá nhân:** [`docs/template2/members/binh/`](../../docs/template2/members/binh/)  
> **Chuẩn quy định:** Mỗi phiên ghi đủ 7 trường bắt buộc theo quy định Khoa CNTT & `TEAM_GUIDE_PHASE2.md` (Thời gian, Tác giả, Công cụ/Model, Prompt đã khử dữ liệu nhạy cảm, Nội dung AI tạo, Nội dung tự kiểm chứng & hiệu chỉnh, Minh chứng/Commit).

---

## 1. BẢNG TỔNG HỢP CÁC PHIÊN SỬ DỤNG AI (TEMPLATE 2 — NGÔ VIẾT THANH BÌNH)

| Mã phiên | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Tóm tắt kết quả AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-01** | 16h30 – 20h35<br>20/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Tái cấu trúc repo Giai đoạn 2, lập `TEAM_GUIDE_PHASE2.md`, phân công Jira và khởi tạo khung `TEMPLATE2_DRAFT_MASTER.md` | AI hỗ trợ dựng cấu trúc thư mục tách biệt `members/<ten>/`, lập bảng phân công và khung nháp 6 mục Template 2 từ SRS & Template 1; sinh viên đối chiếu biểu mẫu `Template2-ThietKe.docx`, chốt quy tắc `0% Conflict` và mốc hạn cứng | Commit `e1ab591`, `TEAM_GUIDE_PHASE2.md`, `SCRUM-58..61`, `SCRUM-66` |
| **T2-02** | 20h40 – 21h20<br>20/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Chuẩn hóa liên kết Google Doc làm việc chung, hiện đại hóa `README.md` và đồng bộ danh mục task Jira Giai đoạn 2 | AI hỗ trợ cập nhật URL Google Doc chính thức và Figma ver3 (`node-id=111-3978`) xuyên suốt các file hướng dẫn, `task/template2/*.md` và CSV Jira; sinh viên kiểm tra từng link truy cập và quyền chia sẻ trên Google Doc | Commit `3a3e5b2`, `4c0e056`, `task/jira/tasks_phase2_updated.csv`, `SCRUM-55` |
| **T2-03** | 10h15 – 12h10<br>21/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 2.5 Flash & Gemini 3.8 Flash)<br>via Antigravity IDE | Đối soát kiến trúc Tầng Server & Tầng Dữ liệu (Mục 3.1.5–3.1.7) với khung nền tảng Spring Boot 3.3.5 & Supabase Cloud `pgvector` | AI hỗ trợ đối chiếu thiết kế kết nối JDBC SSL, HikariCP, `ErrorEnvelope`, `ActorPrincipal`, `UserRole` và Docker Compose `pgvector` với mã nguồn scaffold; sinh viên loại bỏ thông tin nhạy cảm khỏi `application.yml`, xác minh build Maven Java 21 | Commit `67f18d2`, `f561235`, `0bc6f33`, `a14ef99`, PR `#14` (`SCRUM-26`, `SCRUM-59`) |
| **T2-04** | 18h00 – 20h45<br>22/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash & Claude 3.5 Sonnet)<br>via Antigravity IDE | Soạn thảo chi tiết Mục 3.1 (`3.1.1`–`3.1.7`): Tổng quan kiến trúc 3-Tier / Modular Monolith, Bảng công nghệ & 6 Design Patterns | AI hỗ trợ diễn giải kiến trúc 3 tầng, cơ chế cô lập thực thể/repository, bảng công nghệ 8 lớp và 6 mẫu thiết kế; sinh viên chuẩn hóa nguyên tắc tách rời phụ thuộc một chiều (DAG) giữa `Ticket` và `Workflow` qua Public Ports | Commit `f3cc774`, `9e96e10`, `SCRUM-59` |
| **T2-05** | 21h00 – 23h30<br>22/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash) & Draw.io | Thiết kế tệp nguồn `.drawio`, kết xuất `.svg` và `.png` Retina (`1760×990`) cho **Hình 3.1** (Cây phân rã) và **Hình 3.2** (Kiến trúc 3 tầng) | AI sinh cấu trúc XML `.drawio` và `.svg` cho Hình 3.1 (19 UCs) và Hình 3.2 (3-Tier + Modular Monolith); sinh viên kiểm tra từng mã `UC-01..UC-19`, đóng khung nét đứt `[P1]` cho `UC-16/17/19` & `SMTP [P1]`, kiểm tra chiều mũi tên Public Ports | `docs/template2/members/binh/diagrams/system-decomposition-tree.*`, `system-architecture.*`, `SCRUM-59` |
| **T2-06** | 17h45 – 18h30<br>24/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>+ Google Workspace `gdocs` CLI | Rà soát độc lập toàn bộ Google Doc Template 2 đối chiếu với repo, SRS, Figma ver3 và xử lý 15 điểm chưa nhất quán | AI hỗ trợ quét đối chiếu giữa Google Doc và repo (`pom.xml`, `package.json`, `SRS-master.md`); sinh viên duyệt và cập nhật trực tiếp lên Google Doc: thống nhất "4 Module nghiệp vụ + 1 gói Workflow", làm sạch thuộc tính vật lý ở EER Mục 2.3.1, đồng bộ mã màn hình Mục 5.1.2, sửa chú thích Hình 5.2.4b (`A-DiscardConfirm`) và `D-Detail` | Lịch sử phiên bản Google Doc ngày 24/11/2026 (`SCRUM-62`) |
| **T2-07** | 16h00 – 17h15<br>25/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium)<br>+ Google Workspace `gdocs` CLI | Xử lý 8 bình luận review chéo của Lê Quý Phúc trên Google Doc, cập nhật nhãn Hình 3.2 và đồng bộ với 5 sơ đồ lớp mới (Hình 3.3a..e) của Phan Gia Phúc | AI hỗ trợ tải sơ đồ từ Google Doc, sửa nhãn Hình 3.2 thành `"4 Module nghiệp vụ + Workflow + Worker — Public Ports một chiều (DAG)"`, kết xuất lại PNG bằng Chrome headless và cập nhật bảng đặc tả; sinh viên kiểm tra trực quan từng hình, phản hồi từng comment trên Google Doc | Lịch sử comment & phiên bản Google Doc ngày 25/11/2026 (`SCRUM-59`, `SCRUM-62`) |
| **T2-08** | 00h10 – 00h35<br>26/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium)<br>via Antigravity IDE | Chuyển thể nguyên bản Mục 3.1 từ bản xuất Markdown chốt cuối của Google Doc sang `docs/template2/members/binh/03-thiet-ke-kien-truc.md` & mở PR `#18` | AI trích xuất chính xác 100% văn bản Mục 3.1 từ file `.md` tải về từ Google Doc, gắn đường dẫn sơ đồ Hình 3.1 & 3.2, tổng hợp nhật ký AI 8 phiên; sinh viên kiểm tra `git diff` đảm bảo 0% chạm vào file của thành viên khác, push nhánh `docs/t2-binh` và mở PR `#18` | Commit `134a1fa`, PR [`#18`](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/18) (`SCRUM-59`, `SCRUM-62`, `SCRUM-55`) |

---

## 2. CHI TIẾT TỪNG PHIÊN SỬ DỤNG AI (ĐẦY ĐỦ 7 TRƯỜNG BẮT BUỘC)

### Phiên T2-01 — Tái cấu trúc repo Giai đoạn 2, lập `TEAM_GUIDE_PHASE2.md` & Khởi tạo khung `TEMPLATE2_DRAFT_MASTER.md` (20/11/2026)

* **1. Thời gian:** 16h30 – 20h35 ngày 20/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm)
* **3. Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Tái cấu trúc kho mã nguồn để chuẩn bị cho Giai đoạn 2 (chạy song song Thiết kế Template 2 và Code MVP P0 lĩnh vực Đồ điện tử). Thiết lập thư mục bàn giao cá nhân `docs/template2/members/<ten>/`, `task/template2/<ten>.md`, `ai-usage/template2/<ten>.md` đảm bảo 0% xung đột Git khi 4 thành viên làm việc độc lập. Soạn thảo hướng dẫn `TEAM_GUIDE_PHASE2.md` và bản khung `TEMPLATE2_DRAFT_MASTER.md` bám sát biểu mẫu `Template2-ThietKe.docx`, bài mẫu K23 (Planora, Katling, SmartSpend), `Template 1`, `SRS-master.md` và `MVP_CONTRACTS.md`."*
* **5. Nội dung AI tạo:**
  - Cấu trúc thư mục `docs/template2/members/{binh,gia-phuc,lam,quy-phuc}/`, `task/template2/`, `ai-usage/template2/`.
  - Tài liệu hướng dẫn điều phối [`TEAM_GUIDE_PHASE2.md`](../../TEAM_GUIDE_PHASE2.md) quy định rõ 2 luồng công việc, 6 cột mốc cứng, quy tắc đặt tên nhánh `docs/t2-<ten>` và quy chuẩn commit gắn mã Jira `SCRUM-xx`.
  - Bản khung `TEMPLATE2_DRAFT_MASTER.md` gồm 6 mục (Đánh giá thành viên, Mô hình quan niệm EER, Thiết kế kiến trúc & Class Diagram, Thiết kế dữ liệu ERD & Data Dictionary V1–V5, Thiết kế giao diện Figma ver3, Ghi chú sử dụng AI).
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra đối chiếu cấu trúc đề mục của `TEMPLATE2_DRAFT_MASTER.md` với file biểu mẫu gốc `Template2-ThietKe.docx` của môn học.
  - Phân chia rõ trách nhiệm từng mục cho 4 thành viên (`SCRUM-58` Lãm Mục 1–2; `SCRUM-59` Bình Mục 3.1; `SCRUM-66` Gia Phúc Mục 3.2–3.3; `SCRUM-60` Lãm Mục 4; `SCRUM-61` Quý Phúc Mục 5; `SCRUM-62` Review chéo; `SCRUM-55` Đóng gói release).
* **7. Minh chứng / Commit:**
  - Commit `e1ab591` (`docs(phase2): restructure repo, add team guide and template2 draft master SCRUM-58 SCRUM-59 SCRUM-60 SCRUM-61 SCRUM-66`).

---

### Phiên T2-02 — Chuẩn hóa liên kết Google Doc chung, hiện đại hóa `README.md` & Đồng bộ danh mục Jira (20/11/2026)

* **1. Thời gian:** 20h40 – 21h20 ngày 20/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm)
* **3. Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Cập nhật đường dẫn Google Doc làm việc chung chính thức của nhóm cho Template 2 (`[SE - Nhóm 4] Template2-ThietKe-Clarune-04`) và liên kết Figma ver3 (`node-id=111-3978`) vào toàn bộ các file hướng dẫn (`README.md`, `TEAM_GUIDE_PHASE2.md`, `docs/template2/README.md`, `task/template2/*.md` và file CSV Jira `task/jira/tasks_phase2_updated.csv`)."*
* **5. Nội dung AI tạo:**
  - Cập nhật đồng bộ URL Google Doc chung và Figma ver3 trên toàn bộ tài liệu điều hướng và 4 file checklist `task/template2/*.md`.
  - Bổ sung bảng liên kết nhanh Giai đoạn 2 trên `README.md` ở thư mục gốc của dự án.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên trực tiếp mở kiểm tra từng liên kết Google Doc và Figma ver3 từ `README.md` và `task/template2/binh.md`, xác nhận quyền truy cập chỉnh sửa/comment hoạt động bình thường cho cả 4 thành viên.
* **7. Minh chứng / Commit:**
  - Commit `3a3e5b2` (`docs(template2): update official shared Google Doc URL across guides and draft SCRUM-55`) và Commit `4c0e056` (`docs(repo): modernize main README for phase 2 navigation and sync Jira CSV URLs SCRUM-55`).

---

### Phiên T2-03 — Đối soát thiết kế kiến trúc Mục 3.1 với khung nền tảng Spring Boot 3.3.5 & Supabase Cloud `pgvector` (21/11/2026)

* **1. Thời gian:** 10h15 – 12h10 ngày 21/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity AI (Gemini 2.5 Flash & Gemini 3.8 Flash) via Antigravity IDE
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Đối chiếu phần thiết kế Tầng Server (3.1.5), Tầng Cơ sở dữ liệu & Lưu trữ (3.1.6) và Bảng công nghệ (3.1.7.A) của Template 2 với cấu hình thực tế vừa dựng trong `backend/` (Spring Boot 3.3.5, Java 21, `application.yml`, `ErrorEnvelope`, `ActorPrincipal`, `UserRole`, `HealthController`) và `infra/docker-compose.yml` (PostgreSQL 16 + extension `vector`). Đảm bảo thông số thiết kế trong Mục 3.1 phản ánh đúng kiến trúc triển khai trên Supabase Cloud (Singapore) kèm Docker Compose dự phòng."*
* **5. Nội dung AI tạo:**
  - Nội dung mô tả chi tiết tại Mục `3.1.5` (4 lớp bên trong mỗi Module: Controller Layer `/api/v1/*`, Application Service Layer quản lý ranh giới transaction ngắn tách khỏi lời gọi AI, Domain Layer, Infrastructure Layer kèm `JwtAuthenticationFilter` kiểm tra `enabled = true`) và Mục `3.1.6` (PostgreSQL 16 & `pgvector` trên Supabase Cloud Singapore + Docker Compose fallback + Private File Storage).
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra lại `backend/src/main/resources/application.yml` (loại bỏ các giá trị mặc định nhạy cảm, chỉ nhận qua biến môi trường `${DB_URL}`, `${DB_USERNAME}`, `${DB_PASSWORD}`, `${JWT_SECRET}` và xác nhận thời hạn Access Token `900s` = 15 phút, Refresh Token `604800s` = 7 ngày khớp với đặc tả Mục 3.1).
* **7. Minh chứng / Commit:**
  - Commit `67f18d2`, `f561235`, `0bc6f33`, `a14ef99`, Pull Request [`#14`](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/14) (`SCRUM-26`, `SCRUM-59`).

---

### Phiên T2-04 — Soạn thảo chi tiết Mục 3.1 (`3.1.1`–`3.1.7`) & Chuẩn hóa nguyên tắc tách rời phụ thuộc một chiều DAG (22/11/2026)

* **1. Thời gian:** 18h00 – 20h45 ngày 22/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash & Claude 3.5 Sonnet) via Antigravity IDE
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hoàn thiện văn bản học thuật cho toàn bộ Mục 3.1 Thiết kế kiến trúc (từ 3.1.1 đến 3.1.7) để đưa vào Google Doc của nhóm. Làm rõ nguyên tắc Modular Monolith: cô lập thực thể và kho dữ liệu theo từng Module, giao tiếp liên Module qua Public Ports và DTO bất biến theo đồ thị có hướng không chu trình (DAG), giải thích rõ vì sao cần gói điều phối Workflow đứng ở tầng trên để xử lý giao dịch nguyên tử giữa Ticket và AI mà không gây phụ thuộc vòng hai chiều."*
* **5. Nội dung AI tạo:**
  - Bản văn bản hoàn chỉnh của các mục `3.1.1`, `3.1.2`, `3.1.3`, `3.1.4`, `3.1.5`, `3.1.6` và `3.1.7` (gồm Bảng công nghệ `A` và 6 Mẫu thiết kế `B`: State Machine Pattern, Optimistic Locking & Atomic Claim, Lease-Based Background Worker, Strategy & Adapter Pattern, Human-in-the-Loop Workflow, Phòng chống Prompt Injection & Kiểm chứng Trích dẫn).
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên rà soát lại luồng phụ thuộc giữa `Ticket`, `AI`, `Knowledge` và `Workflow`: khẳng định rõ Module `Ticket` không phụ thuộc hay import gói `Workflow`; `Workflow` đứng ở tầng điều phối gọi xuống Public Ports của `Ticket` và `AI` theo thứ tự khóa cố định (`Ticket` trước $\to$ `AISuggestion` sau).
* **7. Minh chứng / Commit:**
  - Commit `f3cc774` & `9e96e10` (`docs(template2): sync ticket-workflow decoupling to draft master SCRUM-59`).

---

### Phiên T2-05 — Thiết kế sơ đồ nguồn Draw.io & Kết xuất SVG/PNG Retina cho Hình 3.1 và Hình 3.2 (22/11/2026)

* **1. Thời gian:** 21h00 – 23h30 ngày 22/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash) & Draw.io + Google Chrome Headless Renderer
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Tạo file nguồn sơ đồ `.drawio` và `.svg` chuẩn kích thước `1760×990` cho 2 hình của Mục 3.1: (1) Hình 3.1 Sơ đồ cây phân rã chức năng hệ thống Clarune theo chiều dọc chia thành 4 Module ánh xạ đủ 19 Use Cases (`UC-01..UC-19`, trong đó `UC-16`, `UC-17`, `UC-19` đóng khung nét đứt ghi rõ `Hoãn P1`) nối xuống `SERVER (Spring Boot)` và `DATABASE (PostgreSQL)`; (2) Hình 3.2 Sơ đồ tổng quan kiến trúc 3 tầng kết hợp Modular Monolith thể hiện đầy đủ Tầng 1 Presentation (React 18 + TypeScript SPA, 4 cụm UI, State & Data Adapters, API Client Axios), Tầng 2 Application/Business Logic (Common Security & Filter gồm JWT Auth Filter, CORS Filter, CSRF Filter, Global Exception; khối các Module nghiệp vụ + Workflow + Ingestion Worker giao tiếp qua Public Port) và Tầng 3 Data & External Services (PostgreSQL Supabase Cloud & pgvector, External AI Service, Private File Storage, Mail Service SMTP [P1])."*
* **5. Nội dung AI tạo:**
  - Tệp nguồn XML `system-decomposition-tree.drawio`, `system-decomposition-tree.svg` và `system-architecture.drawio`, `system-architecture.svg`.
  - Kết xuất ảnh PNG độ phân giải cao (`1760 × 990`) qua Google Chrome Headless để chèn vào Google Doc không bị vỡ nét.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra từng mã Use Case từ `UC-01` đến `UC-19` trên **Hình 3.1**, đối chiếu tên tiếng Việt với bảng danh mục Use Case ở `Template 1`.
  - Trên **Hình 3.2**, kiểm tra từng nhãn giao thức trên mũi tên (`HTTPS / REST`, `Public Port`, `Lease & Extract`, `JDBC SSL`, `File I/O`, `SMTP [P1]`) và bảng chú giải ở góc dưới bên trái.
* **7. Minh chứng / Commit:**
  - Bộ 6 tệp sơ đồ tại [`docs/template2/members/binh/diagrams/`](../../docs/template2/members/binh/diagrams/) và [`docs/template2/assets/diagrams/`](../../docs/template2/assets/diagrams/) (`SCRUM-59`).

---

### Phiên T2-06 — Rà soát độc lập toàn bộ tài liệu Google Doc Template 2 đối chiếu với Repo & SRS (24/11/2026)

* **1. Thời gian:** 17h45 – 18h30 ngày 24/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm)
* **3. Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash) + Google Workspace `gdocs` CLI
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Kết nối với Google Doc làm việc của nhóm (`1xI8hj6xi6dqKEPklbn9H8nXUGhvN8OpxdDhpVNPSLc8`), kéo toàn bộ nội dung hiện tại về đối chiếu chéo giữa các mục (Mục 1, 2, 3, 4, 5) với `SRS-master.md`, `MVP_CONTRACTS.md`, `pom.xml`, `package.json` và Figma ver3. Lập danh sách các điểm tự mâu thuẫn (số lượng module giữa 3.1.1/3.1.3/3.2, thuộc tính vật lý lẫn trong bảng thực thể quan niệm EER 2.3.1, mã màn hình thiếu trong bảng 5.1.2, chú thích Hình 5.2.4b, phiên bản thư viện dự kiến trong bảng 3.1.7.A) và sửa trực tiếp trên Google Doc."*
* **5. Nội dung AI tạo:**
  - Báo cáo rà soát 15 điểm chưa nhất quán trên bản nháp Google Doc và tập lệnh `gdocs mutate replace` để cập nhật đồng bộ.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra từng thay đổi trên Google Doc sau khi chạy lệnh:
    1. Thống nhất cách gọi **"4 Module nghiệp vụ độc lập (`Identity`, `Ticket`, `Knowledge`, `AI`) cùng 1 gói điều phối `Workflow` chung"** tại cả `3.1.1`, `3.1.3` và `3.2`.
    2. Lược bỏ các cột kỹ thuật cài đặt (`passwordHash`, `refreshTokenHash`, `tokenHash`, `version`, `storageKey`, `contentHash`, `embedding`, `leaseToken`, `lockedUntil`) khỏi bảng thực thể ngữ nghĩa EER (`2.3.1`), đổi tên `IngestionJob` thành `KnowledgeIngestionJob` và chuẩn hóa nhãn quan hệ tại bảng `2.3.2`.
    3. Bổ sung các mã màn hình `I05`, `A04`, `A-Resolved`, `K02`, `K03`, `K-ReadyDetail` vào Bảng `5.1.2`; sửa chú thích Hình `5.2.4b` từ `A05` thành `A-DiscardConfirm`; sửa tham chiếu màn hình Admin tại `5.2.3.2` từ `D02` thành `D-Detail`.
    4. Đổi tiêu đề cột cuối Bảng công nghệ (`3.1.7.A`) thành *"Phiên bản / Tiêu chuẩn áp dụng"* và chuẩn hóa thông tin thư viện khớp với repo.
* **7. Minh chứng / Commit:**
  - Lịch sử chỉnh sửa trực tiếp trên Google Doc `[SE - Nhóm 4] Template2-ThietKe-Clarune-04` ngày 24/11/2026 (`SCRUM-62`).

---

### Phiên T2-07 — Xử lý 8 bình luận review chéo của Lê Quý Phúc, cập nhật Hình 3.2 & Đồng bộ với bộ sơ đồ lớp mới của Phan Gia Phúc (25/11/2026)

* **1. Thời gian:** 16h00 – 17h15 ngày 25/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **3. Công cụ / Model:** Antigravity AI (Gemini 4 Argon Medium) + Google Workspace `gdocs` CLI + Google Chrome Headless
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Kiểm tra toàn bộ các comment mới nhất trên Google Doc Template 2. Sửa Comment #3 của Quý Phúc trên Hình 3.2 (đổi nhãn `5 Business Modules + Worker` thành `4 Module nghiệp vụ + Workflow + Worker — Public Ports một chiều (DAG)` trong file `.drawio`, `.svg`, render lại `.png` và thay ảnh trực tiếp trên Google Doc). Tiếp tục phân tích và xử lý các Comment #7, #8, #4 (đồng bộ chữ ký Public Ports, `WorkflowController`, đánh dấu Backlog/P1 cho `updatePriority` & `PRIORITY_CHANGED`), Comment #5 (`confirmPassword` ở UC-01 & UC-03), Comment #6 (truyền `version` và trả 409 ở UC-07 & UC-09), Comment #1 (vị trí hiển thị `ARCHIVED` trên bảng `K04`), phản hồi từng comment và kiểm tra khớp với 5 sơ đồ lớp mới (Hình 3.3a..3.3e) Gia Phúc vừa cập nhật."*
* **5. Nội dung AI tạo:**
  - Cập nhật `system-architecture.drawio`, `system-architecture.svg`, kết xuất lại `system-architecture.png` (`1760 × 990`) với nhãn **`4 Module nghiệp vụ + Workflow + Worker — Public Ports một chiều (DAG)`** và thay thế trực tiếp đối tượng ảnh `kix.qnu0ormxhhvr` (**Hình 3.2**) trên Google Doc.
  - Cập nhật các bảng đặc tả lớp ở Mục `3.3.2`, `3.3.3`, `3.3.4`, Bảng `4.3`, `4.5` và các bảng xử lý sự kiện giao diện ở Mục `5.2.1.2`, `5.2.1.4`, `5.2.2.3`, `5.2.3.1`, `5.2.3.2`, `5.2.5.2`, `5.2.6.1`.
  - Đăng phản hồi chi tiết vào toàn bộ các luồng comment trên Google Doc.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên tải toàn bộ 5 sơ đồ lớp mới của Phan Gia Phúc (**Hình 3.3a, 3.3b, 3.3c, 3.3d, 3.3e**) từ Google Doc về kiểm tra trực quan:
    - Phát hiện trên **Hình 3.3c** mới của Gia Phúc có mũi tên **`Tin soạn tay`** từ `WorkflowController (+ postMessage(...))` trỏ sang `TicketApplicationService (+ addMessage(...))` và trên **Hình 3.3d** có phương thức `+ searchPublished(...)`; sinh viên đã điều chỉnh ngay mô tả của `TicketController` (§3.3.2), `KnowledgeApplicationService` (§3.3.3) và `WorkflowController` (§3.3.4) để khớp tuyệt đối 100% với bộ hình mới của Gia Phúc.
    - Kiểm tra lại quyết định `DEC-06` đã được Lãm và Quý Phúc chốt thống nhất trên Hình 4.1 ERD, Bảng Flyway V3, Bảng 4.8 và Bảng 3.1.7.A là **`gemini-embedding-2, 768 chiều` (`vector(768)`)**.
* **7. Minh chứng / Commit:**
  - Các phản hồi comment trên Google Doc: `doco.mKNfx-aRg-AccyCxa5Bsfg`, `doco.G3-v0SXvRsVr7VMfQLVgCA`, `doco.5ad3qC_WokDdF-RApf7fnw`, `doco.0dOhjWAgXFiYrAna6tRxng`, `doco.RynBVzzxhTMwxJJDPPLmwQ`, `doco.vNlGTtofpDHryxudvJUlbw`, `doco.SAqvA26nLeZcsSpGt_xCVw`, `doco.6Olc5pl2kgf48qUhzZ_dwg` (`SCRUM-59`, `SCRUM-62`).

---

### Phiên T2-08 — Chuyển thể Markdown Mục 3.1 từ bản chốt Google Doc, đóng gói minh chứng cá nhân & Mở Pull Request `#18` (26/11/2026)

* **1. Thời gian:** 00h10 – 00h35 ngày 26/11/2026
* **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm)
* **3. Công cụ / Model:** Antigravity AI (Gemini 4 Argon Medium) via Antigravity IDE + GitHub CLI (`gh`)
* **4. Prompt đã khử dữ liệu nhạy cảm:**
  > *"Phần Google Doc nhóm đã chốt và tôi đã tải file dạng `.md` về trong `~/Downloads/[SE - Nhóm 4] Template2-ThietKe-Clarune-04.md`. Hãy tuân thủ đúng quy định của nhóm: chuyển thể nguyên bản phần Markdown Mục 3.1 tương ứng của tôi vào `docs/template2/members/binh/03-thiet-ke-kien-truc.md` (đảm bảo chính xác 100% nội dung trong doc đã chốt), hoàn thiện chi tiết nhật ký AI usage tại `ai-usage/template2/binh.md`, cập nhật `task/template2/binh.md`, không chạm vào file của thành viên khác và tạo Pull Request lên repo."*
* **5. Nội dung AI tạo:**
  - Trích xuất nguyên bản 100% văn bản Mục `3.1` (`3.1.1` đến hết `3.1.7`) từ file `/Users/ngovietthanhbinh/Downloads/[SE - Nhóm 4] Template2-ThietKe-Clarune-04.md` sang [`docs/template2/members/binh/03-thiet-ke-kien-truc.md`](../../docs/template2/members/binh/03-thiet-ke-kien-truc.md) và thay thế thẻ ảnh bằng đường dẫn tương đối tới `diagrams/system-decomposition-tree.png` (**Hình 3.1**) và `diagrams/system-architecture.png` (**Hình 3.2**).
  - Tổng hợp đầy đủ bảng tóm tắt và 8 phiên chi tiết (`T2-01` đến `T2-08`) vào `ai-usage/template2/binh.md`.
  - Khởi tạo nội dung Pull Request theo đúng mẫu `.github/PULL_REQUEST_TEMPLATE.md`.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra `git status` và `git diff --stat` trên nhánh `docs/t2-binh` để xác nhận chỉ có đúng các file thuộc phạm vi cá nhân của Bình (`docs/template2/members/binh/`, `docs/template2/assets/diagrams/`, `ai-usage/template2/binh.md`, `task/template2/binh.md`), tuyệt đối không gây xung đột với nhánh của Gia Phúc, Lãm và Quý Phúc.
* **7. Minh chứng / Commit:**
  - Commit `134a1fa` trên nhánh `docs/t2-binh`, Pull Request [`#18`](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/18) (`SCRUM-59`, `SCRUM-62`, `SCRUM-55`).
