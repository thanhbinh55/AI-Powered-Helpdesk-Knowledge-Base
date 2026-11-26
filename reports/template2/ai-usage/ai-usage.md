# BÁO CÁO SỬ DỤNG AI — TEMPLATE 2

> **Dự án:** AI-Powered Helpdesk & Knowledge Base (Clarune)  
> **Nhóm thực hiện:** Nhóm 04 — Lớp Nhập môn Công nghệ Phần mềm (CS10014), Trường ĐHKHTN, ĐHQG-HCM  
> **Kho lưu trữ:** https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base  
> **Chuẩn quy định:** Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS  
> **Phạm vi tài liệu:** Nhật ký ghi nhận các phiên sử dụng công cụ AI phục vụ trực tiếp cho Báo cáo Thiết kế Phần mềm Template 2 (kế thừa và tiếp nối độc lập sau khi đã nộp hoàn tất Template 0 và Template 1).  

---

## 1. NGUYÊN TẮC MINH BẠCH & KIỂM CHỨNG TRONG TEMPLATE 2

1. **Minh bạch câu lệnh (Prompts):** Toàn bộ các câu prompt đưa vào AI đều được ghi nhận trung thực từ nhật ký của từng thành viên, tóm tắt rõ mục đích và đã khử các thông tin nhạy cảm (secrets/credentials/PII).
2. **Không sao chép máy móc:** Mọi sơ đồ EER, sơ đồ kiến trúc, sơ đồ lớp (Class Diagram), sơ đồ cơ sở dữ liệu vật lý (Physical ERD), đặc tả dữ liệu Flyway V1–V5 và thiết kế giao diện Figma ver3 do AI hỗ trợ đều được thành viên phụ trách đối chiếu chéo với `SRS-master.md`, `MVP_CONTRACTS.md`, mã nguồn kho lưu trữ và tài liệu nhóm trên Google Docs (`[SE - Nhóm 4] Template2-ThietKe-Clarune-04`) trước khi chốt.
3. **Phân định trách nhiệm cá nhân:** Tác giả từng mục chịu trách nhiệm trực tiếp về phần nội dung con người đã kiểm chứng; báo cáo tổng hợp này giữ nguyên trung thực 100% nội dung các phiên AI mà 4 thành viên đã ghi nhận trên nhánh cá nhân.

---

## 2. NHẬT KÝ SỬ DỤNG AI THEO THÀNH VIÊN

### 2.1 Ngô Viết Thanh Bình — 24120269

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-01** | 16h30 – 20h35<br>20/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Tái cấu trúc repo Giai đoạn 2, lập `TEAM_GUIDE_PHASE2.md`, phân công Jira và khởi tạo khung `TEMPLATE2_DRAFT_MASTER.md` | AI hỗ trợ dựng cấu trúc thư mục tách biệt `members/<ten>/`, lập bảng phân công và khung nháp 6 mục Template 2 từ SRS & Template 1; sinh viên đối chiếu biểu mẫu `Template2-ThietKe.docx`, chốt quy tắc `0% Conflict` và mốc hạn cứng | Commit `e1ab591`, `TEAM_GUIDE_PHASE2.md`, `SCRUM-58..61`, `SCRUM-66` |
| **T2-02** | 20h40 – 21h20<br>20/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Chuẩn hóa liên kết Google Doc làm việc chung, hiện đại hóa `README.md` và đồng bộ danh mục task Jira Giai đoạn 2 | AI hỗ trợ cập nhật URL Google Doc chính thức và Figma ver3 (`node-id=111-3978`) xuyên suốt các file hướng dẫn, `task/template2/*.md` và CSV Jira; sinh viên kiểm tra từng link truy cập và quyền chia sẻ trên Google Doc | Commit `3a3e5b2`, `4c0e056`, `task/jira/tasks_phase2_updated.csv`, `SCRUM-55` |
| **T2-03** | 10h15 – 12h10<br>21/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 2.5 Flash & Gemini 3.8 Flash)<br>via Antigravity IDE | Đối soát kiến trúc Tầng Server & Tầng Dữ liệu (Mục 3.1.5–3.1.7) với khung nền tảng Spring Boot 3.3.5 & Supabase Cloud `pgvector` | AI hỗ trợ đối chiếu thiết kế kết nối JDBC SSL, HikariCP, `ErrorEnvelope`, `ActorPrincipal`, `UserRole` và Docker Compose `pgvector` với mã nguồn scaffold; sinh viên loại bỏ thông tin nhạy cảm khỏi `application.yml`, xác minh build Maven Java 21 | Commit `67f18d2`, `f561235`, `0bc6f33`, `a14ef99`, PR `#14` (`SCRUM-26`, `SCRUM-59`) |
| **T2-04** | 18h00 – 20h45<br>22/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash & Claude 3.5 Sonnet)<br>via Antigravity IDE | Soạn thảo chi tiết Mục 3.1 (`3.1.1`–`3.1.7`): Tổng quan kiến trúc 3-Tier / Modular Monolith, Bảng công nghệ & 6 Design Patterns | AI hỗ trợ diễn giải kiến trúc 3 tầng, cơ chế cô lập thực thể/repository, bảng công nghệ 8 lớp và 6 mẫu thiết kế; sinh viên chuẩn hóa nguyên tắc tách rời phụ thuộc một chiều (DAG) giữa `Ticket` và `Workflow` qua Public Ports | Commit `f3cc774`, `9e96e10`, `SCRUM-59` |
| **T2-05** | 21h00 – 23h30<br>22/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash) & Draw.io | Thiết kế tệp nguồn `.drawio`, kết xuất `.svg` và `.png` Retina (`1760×990`) cho **Hình 3.1** (Cây phân rã) và **Hình 3.2** (Kiến trúc 3 tầng) | AI sinh cấu trúc XML `.drawio` và `.svg` cho Hình 3.1 (19 UCs) và Hình 3.2 (3-Tier + Modular Monolith); sinh viên kiểm tra từng mã `UC-01..UC-19`, đóng khung nét đứt `[P1]` cho `UC-16/17/19` & `SMTP [P1]`, kiểm tra chiều mũi tên Public Ports | `docs/template2/members/binh/diagrams/system-decomposition-tree.*`, `system-architecture.*`, `SCRUM-59` |
| **T2-06** | 17h45 – 18h30<br>24/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>+ Google Workspace `gdocs` CLI | Rà soát độc lập toàn bộ Google Doc Template 2 đối chiếu với repo, SRS, Figma ver3 và xử lý 15 điểm chưa nhất quán | AI hỗ trợ quét đối chiếu giữa Google Doc và repo (`pom.xml`, `package.json`, `SRS-master.md`); sinh viên duyệt và cập nhật trực tiếp lên Google Doc: thống nhất "4 Module nghiệp vụ + 1 gói Workflow", làm sạch thuộc tính vật lý ở EER Mục 2.3.1, đồng bộ mã màn hình Mục 5.1.2, sửa chú thích Hình 5.2.4b (`A-DiscardConfirm`) và `D-Detail` | Lịch sử phiên bản Google Doc ngày 24/11/2026 (`SCRUM-62`) |
| **T2-07** | 16h00 – 17h15<br>25/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium)<br>+ Google Workspace `gdocs` CLI | Xử lý 8 bình luận review chéo của Lê Quý Phúc trên Google Doc, cập nhật nhãn Hình 3.2 và đồng bộ với 5 sơ đồ lớp mới (Hình 3.3a..e) của Phan Gia Phúc | AI hỗ trợ tải sơ đồ từ Google Doc, sửa nhãn Hình 3.2 thành `"4 Module nghiệp vụ + Workflow + Worker — Public Ports một chiều (DAG)"`, kết xuất lại PNG bằng Chrome headless và cập nhật bảng đặc tả; sinh viên kiểm tra trực quan từng hình, phản hồi từng comment trên Google Doc | Lịch sử comment & phiên bản Google Doc ngày 25/11/2026 (`SCRUM-59`, `SCRUM-62`) |
| **T2-08** | 00h10 – 00h35<br>26/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium)<br>via Antigravity IDE | Chuyển thể nguyên bản Mục 3.1 từ bản xuất Markdown chốt cuối của Google Doc sang `docs/template2/members/binh/03-thiet-ke-kien-truc.md` & mở PR `#18` | AI trích xuất chính xác 100% văn bản Mục 3.1 từ file `.md` tải về từ Google Doc, gắn đường dẫn sơ đồ Hình 3.1 & 3.2, tổng hợp nhật ký AI 8 phiên; sinh viên kiểm tra `git diff` đảm bảo 0% chạm vào file của thành viên khác, push nhánh `docs/t2-binh` và mở PR `#18` | Commit `134a1fa`, PR [`#18`](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/18) (`SCRUM-59`, `SCRUM-62`, `SCRUM-55`) |

#### Phiên T2-01: Tái cấu trúc repo Giai đoạn 2, lập `TEAM_GUIDE_PHASE2.md` & Khởi tạo khung `TEMPLATE2_DRAFT_MASTER.md` (20/11/2026)

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

#### Phiên T2-02: Chuẩn hóa liên kết Google Doc chung, hiện đại hóa `README.md` & Đồng bộ danh mục Jira (20/11/2026)

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

#### Phiên T2-03: Đối soát thiết kế kiến trúc Mục 3.1 với khung nền tảng Spring Boot 3.3.5 & Supabase Cloud `pgvector` (21/11/2026)

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

#### Phiên T2-04: Soạn thảo chi tiết Mục 3.1 (`3.1.1`–`3.1.7`) & Chuẩn hóa nguyên tắc tách rời phụ thuộc một chiều DAG (22/11/2026)

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

#### Phiên T2-05: Thiết kế sơ đồ nguồn Draw.io & Kết xuất SVG/PNG Retina cho Hình 3.1 và Hình 3.2 (22/11/2026)

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

#### Phiên T2-06: Rà soát độc lập toàn bộ tài liệu Google Doc Template 2 đối chiếu với Repo & SRS (24/11/2026)

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

#### Phiên T2-07: Xử lý 8 bình luận review chéo của Lê Quý Phúc, cập nhật Hình 3.2 & Đồng bộ với bộ sơ đồ lớp mới của Phan Gia Phúc (25/11/2026)

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

#### Phiên T2-08: Chuyển thể Markdown Mục 3.1 từ bản chốt Google Doc, đóng gói minh chứng cá nhân & Mở Pull Request `#18` (26/11/2026)

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

### 2.2 Nguyễn Đức Lãm — 24120083

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-09** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Phác thảo mô hình quan niệm EER (mục 2) | Em xác định phạm vi và yêu cầu thể hiện ISA. Codex hỗ trợ phác thảo sơ đồ Chen và xuất ảnh PNG để em đối chiếu với SRS và đặc tả nghiệp vụ đã được nhóm thống nhất. | `SCRUM-58`, `aeee95e` (nguồn draw.io và PNG) |
| **T2-10** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Phác thảo Physical ERD (mục 4.1) | Em cung cấp quyết định của nhóm về `gemini-embedding-2` với đầu ra 768 chiều. Codex hỗ trợ dựng Hình 4.1 từ đặc tả để em đối chiếu các cột và khóa với mục 4.2. | `SCRUM-60`, `aa7e99c` (nguồn draw.io và PNG) |
| **T2-11** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Soạn bản nháp Flyway V1–V5 để đối chiếu mục 4.2 | Em xác nhận tên V2, cách sinh UUID, mô hình nhúng và số chiều đầu ra, rồi cung cấp quy ước V5 của nhóm. Codex dựa trên các thông tin đó để soạn năm tệp SQL nháp. | `SCRUM-60`, bản nháp tại `backend/src/main/resources/db/migration/` |
| **T2-12** | 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex, LibreOffice để xem bố cục | Đối chiếu bản nháp Template 2 với kho mã nguồn | Codex liệt kê các điểm chưa nhất quán và lỗi trình bày. Em đối chiếu các nhận xét với quyết định của nhóm, trong đó có tên chỉ mục ở Bảng 4.4. | Báo cáo rà soát bản Word, liên quan `SCRUM-58` và `SCRUM-60` |
| **T2-13** | 26/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Chuyển mục 1, 2 và 4 từ bản Word đã chốt sang Markdown | Em chọn bản Word làm nguồn, xác nhận phạm vi chuyển đổi và commit ba tệp bàn giao. Codex hỗ trợ chuyển định dạng và đối chiếu nội dung, bảng và chú thích hình với Word. | `aeee95e` (`SCRUM-58`), `aa7e99c` (`SCRUM-60`) |

#### Phiên T2-09: Phác thảo và đối chiếu sơ đồ EER

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Dựa vào SRS và các tài liệu đặc tả nghiệp vụ Clarune đã được nhóm thống nhất, hãy đề xuất danh sách thực thể và quan hệ cho mục 2. Ghi lực lượng min–max và quy tắc nghiệp vụ tương ứng. Phác thảo sơ đồ Chen với quan hệ kế thừa ISA từ `User` đến `Customer`, `Support Agent` và `System Administrator`. Thể hiện quan hệ nghiệp vụ trên hình và bỏ các FK vật lý như `ticket_id`. Chuẩn bị tệp nguồn draw.io và xuất ảnh PNG. Sau khi xuất ảnh, hãy đối chiếu tên thực thể, các nhánh ISA, quan hệ và lực lượng trên PNG với những tài liệu nhóm đã thống nhất. Ghi rõ điểm chưa khớp và nguồn tương ứng để em kiểm tra.

* **5. Nội dung AI tạo** Bản phác thảo EER cho Hình 2.1, gồm tệp nguồn draw.io và ảnh PNG.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em dùng SRS và các tài liệu đặc tả nghiệp vụ nhóm đã thống nhất để đối chiếu tên thực thể, quan hệ và lực lượng trên ảnh PNG. Em kiểm tra phần ISA thể hiện mỗi `User` thuộc đúng một trong ba kiểu con. Các FK vật lý được trình bày ở mục thiết kế dữ liệu.
* **7. Minh chứng / Commit** `SCRUM-58`. Commit `aeee95eb635de08158cc51535531be55fb402e4f` ghi nhận tệp nguồn và ảnh Hình 2.1. [Draw.io](../../docs/template2/assets/diagrams/conceptual-model.drawio) · [PNG](../../docs/template2/assets/diagrams/conceptual-model.png)

---

#### Phiên T2-10: Phác thảo Physical ERD cho Hình 4.1

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Dùng Data Dictionary ở mục 4.2 để phác thảo Physical ERD cho PostgreSQL. Ghi đủ tên bảng, tên cột, kiểu dữ liệu, khả năng nhận `NULL`, PK, FK và ràng buộc duy nhất. Mô hình nhúng nhóm đã chốt là Google `gemini-embedding-2` với đầu ra 768 chiều, nên cột `knowledge_chunks.embedding` có kiểu `vector(768)`. Thể hiện FK và chỉ mục duy nhất có điều kiện của `source_suggestion_id` được thêm ở V5. Xuất PNG vào `docs/template2/assets/diagrams/physical-erd.png` và liệt kê những chỗ cần đối chiếu với mục 4.2.

* **5. Nội dung AI tạo** Bản draw.io và PNG cho lược đồ 10 bảng P0. Hình ghi kiểu `vector(768)` và đánh dấu liên kết được bổ sung trong V5.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em xác nhận số chiều của vector nhúng trước khi đưa hình vào tài liệu và dùng Data Dictionary để đối chiếu tên cột, kiểu dữ liệu và các khóa trên hình. Em lưu ý `source_suggestion_id` cho phép `NULL`. Mỗi giá trị khác `NULL` chỉ được xuất hiện một lần.
* **7. Minh chứng / Commit** `SCRUM-60`. Commit `aa7e99c5a5b9e5d98c0141d9ea130d7c8299e555` chứa sơ đồ nguồn và ảnh. [Draw.io](../../docs/template2/assets/diagrams/physical-erd.drawio) · [PNG](../../docs/template2/assets/diagrams/physical-erd.png)

---

#### Phiên T2-11: Soạn bản nháp Flyway V1–V5

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Giải thích từng migration V1–V5 và chỉ ra bảng đặc tả tương ứng. Dựa vào đó, soạn bản nháp SQL trong `backend/src/main/resources/db/migration/` để đối chiếu kiểu dữ liệu, giá trị mặc định, khóa và chỉ mục. Dùng tên `V2__init_ticketing.sql` và để ứng dụng sinh UUID. Trong V3, bật pgvector trước khi tạo cột `vector(768)`. V2 khai báo cột `source_suggestion_id` cho phép `NULL`. Sau khi V4 tạo `ai_suggestions`, V5 mới thêm FK và chỉ mục duy nhất có điều kiện theo quy ước của nhóm.

* **5. Nội dung AI tạo** Năm bản nháp `V1__init_identity.sql`, `V2__init_ticketing.sql`, `V3__init_knowledge.sql`, `V4__init_ai.sql` và `V5__add_ticket_message_suggestion_fk.sql`. Bản nháp V5 dùng tên `idx_unique_applied_suggestion` theo ảnh quy ước của nhóm tại thời điểm đó.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em chốt tên V2 và cách sinh UUID trước khi cung cấp yêu cầu cho Codex. Khi rà soát mục 4, em dùng kết quả đối chiếu SQL để kiểm tra lại tên cột, điều kiện của chỉ mục duy nhất và thứ tự thêm FK. Việc chạy Flyway trên PostgreSQL 16 là bước kiểm tra riêng.
* **7. Minh chứng / Commit** `SCRUM-60` và năm bản nháp SQL trong `backend/src/main/resources/db/migration/`. Commit `aa7e99c` là minh chứng cho phần thiết kế mục 4 và Physical ERD.

---

#### Phiên T2-12: Rà soát bản nháp Word

* **1. Thời gian** 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex, LibreOffice để xem bố cục.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Đọc bản nháp Word Template 2 và đối chiếu với SRS, MVP Contracts cùng các tệp hiện có trong kho mã nguồn. Chia nhận xét thành mâu thuẫn nội dung, thông tin chưa rõ hoặc chưa đồng bộ, lỗi định dạng và góp ý cải thiện. Ghi số mục, bảng, hình hoặc trang và nguồn cần xem lại để thành viên phụ trách có căn cứ quyết định cách sửa.

* **5. Nội dung AI tạo** Báo cáo ghi vị trí của từng vấn đề. Trong phần em phụ trách, dòng V1 vẫn nhắc `pgcrypto` dù ứng dụng sinh UUID, tên chỉ mục ở Bảng 4.4 lệch với SQL và tên mô hình nhúng chưa được ghi nhất quán trong phần chữ. Báo cáo cũng đánh dấu những sơ đồ khó đọc khi đặt trên trang dọc.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em đối chiếu các nhận xét về V1 và mô hình nhúng với quyết định của nhóm. Đối với Bảng 4.4, em xác nhận trong trao đổi tên chỉ mục cần dùng là `idx_msg_source_unique_applied_suggession`. Khi chuyển định dạng ở phiên sau, em dùng bản Word đã chốt làm nguồn cho nội dung Markdown.
* **7. Minh chứng / Commit** Bản nháp `[SE - Nhóm 4] Template2-ThietKe-Clarune-04.docx` và báo cáo rà soát ngày 23/11/2026. Hai commit `aeee95e` và `aa7e99c` ghi nhận các tệp em bàn giao.

---

#### Phiên T2-13: Chuyển mục 1, 2 và 4 từ Word sang Markdown

* **1. Thời gian** 26/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Chuyển mục 1, 2 và 4 từ bản Word Template 2 đã chốt sang ba tệp Markdown trong `docs/template2/members/lam/`. Đặt tên theo tiêu đề mục, bỏ dấu và nối các từ bằng gạch ngang. Giữ nguyên thứ tự tiêu đề, câu chữ và nội dung ô bảng. Bỏ ảnh nhúng và giữ chú thích Hình 2.1, Hình 4.1. Đối chiếu nội dung hiển thị trong Markdown với Word và ghi lại kết quả để em xem trước khi commit.

* **5. Nội dung AI tạo** Ba tệp Markdown và kết quả đối chiếu từng đoạn, từng ô của 17 bảng. Hai chú thích hình được giữ ở mục 2.2 và 4.1.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em chọn bản Word đã chốt, xác nhận ba mục cần chuyển và duyệt tên tệp trước khi ghi. Em dựa vào kết quả đối chiếu để xem lại phần bàn giao. Khi chuyển định dạng, em giữ câu chữ theo bản Word, kể cả tên chỉ mục `idx_msg_source_suggestion_unique` ở Bảng 4.4.
* **7. Minh chứng / Commit** Nhánh `docs/t2-lam`. Commit `aeee95e` lúc 09:21:17 (+07:00) chứa mục 1–2 (`SCRUM-58`). Commit `aa7e99c` lúc 09:24:07 (+07:00) chứa mục 4 (`SCRUM-60`). [Mục 1](../../docs/template2/members/lam/danh-gia-dong-gop-cac-thanh-vien.md) · [Mục 2](../../docs/template2/members/lam/mo-hinh-quan-niem.md) · [Mục 4](../../docs/template2/members/lam/thiet-ke-du-lieu.md)

---

### 2.3 Phan Gia Phúc — 24120503

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-14** | 23/11/2026. | Phan Gia Phúc (24120503). | OpenAI Codex (GPT-6). | Đối chiếu SRS và chỉnh sửa thiết kế lớp | **AI tạo:** Bảng đối chiếu theo trang và yêu cầu SRS, năm sơ đồ lớp, nội dung bổ sung thêm cho các bảng đặc tả Identity, Ticket, Knowledge, AI và Workflow. **Kiểm chứng:** Sinh viên yêu cầu lấy SRS làm căn cứ. Codex đối chiếu hợp đồng các port, thứ tự khóa Ticket rồi Suggestion, phạm vi P0/P1 và quyết định DEC-06. Codex đọc lại Google Doc, kiểm tra hình cùng chú thích trên bản xuất PDF và cập nhật mục lục. | [Bản thiết kế dùng trong phiên](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u) và [SRS của dự án](../../reports/SRS-master.md). |
| **T2-15** | 25/11/2026. | Phan Gia Phúc (24120503). | OpenAI Codex (GPT-6). | Rà soát năm hình và sửa nhãn bị che | **AI tạo:** Bổ sung nhánh AISuggestionController → AISuggestionApplicationService, tách hai controller ở Identity, bổ sung đường gửi tin soạn tay trong Ticket và đường tiếp nhận tài liệu trong Knowledge. Làm rõ bội số trên hình dữ liệu AI. **Kiểm chứng:** Sinh viên chỉ ra các controller bị thiếu. Codex chuyển nhãn xuống dưới các ô lớp, xuất lại PDF và kiểm tra dòng chữ ở trang in 18. | [Google Doc được rà soát, mục 3.2–3.3](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u). |
| **T2-16** | 26/11/2026. | Phan Gia Phúc (24120503). | OpenAI Codex (GPT-6). | Trích bản Markdown bàn giao cá nhân | **AI tạo:** File bàn giao lấy nguyên văn hai mục từ bản Markdown được chỉ định, kèm định nghĩa ảnh của các hình trong hai mục. **Kiểm chứng:** Codex kiểm tra ranh giới bằng tiêu đề trong thân bài, so sánh nội dung đã ghi với nguồn, đếm bốn tiểu mục module, năm chú thích hình. | [Phần bàn giao 3.2–3.3 của Gia Phúc](../../task/template2/gia-phuc.md) tại commit `317dfe6` trên nhánh `docs/t2-giaphuc`. |

#### Phiên T2-14: 23/11/2026 — Đối chiếu SRS và chỉnh sửa thiết kế lớp

- **Thời gian** 23/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Đọc SRS, kiểm tra mục 3.2 và 3.3 trong bản thiết kế còn thiếu, dư hoặc sai gì. Có thể bổ sung vào Google Doc và ghi nhật ký.”
- **Nội dung AI tạo** Bảng đối chiếu theo trang và yêu cầu SRS, năm sơ đồ lớp, nội dung bổ sung thêm cho các bảng đặc tả Identity, Ticket, Knowledge, AI và Workflow.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Sinh viên yêu cầu lấy SRS làm căn cứ. Codex đối chiếu hợp đồng các port, thứ tự khóa Ticket rồi Suggestion, phạm vi P0/P1 và quyết định DEC-06. Codex đọc lại Google Doc, kiểm tra hình cùng chú thích trên bản xuất PDF và cập nhật mục lục.
- **Minh chứng/Commit** [Bản thiết kế dùng trong phiên](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u) và [SRS của dự án](../../reports/SRS-master.md).

---

#### Phiên T2-15: 25/11/2026 — Rà soát năm hình và sửa nhãn bị che

- **Thời gian** 25/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Bổ sung vào Hình 3.3a controller gọi AI suggestion service. Tách 2 controller Identity, thêm đường gửi tin soạn tay cho rõ ràng. Rà soát thêm các lỗi hiển thị.”
- **Nội dung AI tạo** Bổ sung nhánh AISuggestionController → AISuggestionApplicationService, tách hai controller ở Identity, bổ sung đường gửi tin soạn tay trong Ticket và đường tiếp nhận tài liệu trong Knowledge. Làm rõ bội số trên hình dữ liệu AI.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Sinh viên chỉ ra các controller bị thiếu. Codex chuyển nhãn xuống dưới các ô lớp, xuất lại PDF và kiểm tra dòng chữ ở trang in 18.
- **Minh chứng/Commit** [Google Doc được rà soát, mục 3.2–3.3](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u).

---

#### Phiên T2-16: 26/11/2026 — Trích bản Markdown bàn giao cá nhân

- **Thời gian** 26/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Trích mục 3.2 và 3.3 từ bản Markdown Template 2 của nhóm vào file task.”
- **Nội dung AI tạo** File bàn giao lấy nguyên văn hai mục từ bản Markdown được chỉ định, kèm định nghĩa ảnh của các hình trong hai mục.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Codex kiểm tra ranh giới bằng tiêu đề trong thân bài, so sánh nội dung đã ghi với nguồn, đếm bốn tiểu mục module, năm chú thích hình.
- **Minh chứng/Commit** [Phần bàn giao 3.2–3.3 của Gia Phúc](../../task/template2/gia-phuc.md) tại commit `317dfe6` trên nhánh `docs/t2-giaphuc`.

---

### 2.4 Lê Quý Phúc — 24120121

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-17** | 21/11/2026 (UTC+7) | Lê Quý Phúc (`24120121`) | OpenAI Codex (GPT-6), Google Workspace MCP | Hoàn thành SCRUM-61 theo SRS và Figma v3, cập nhật Google Doc chung. | **AI tạo:** Sơ đồ luồng, danh mục Node ID, đặc tả Copilot/Admin, bảng sự kiện và bộ ảnh bàn giao. **Kiểm chứng:** Đối chiếu ảnh PNG với bộ xuất Figma v3, hành vi API với SRS/MVP Contracts. Khôi phục tiêu đề 5.1.1 và dùng tài khoản đã xác thực để chèn ảnh. Kiểm tra lại 7 hình trong bản xuất Google Docs và đối chiếu các mục liền kề. Các trạng thái chưa thấy frame v3 được ghi rõ. | [Google Doc chung](https://docs.google.com/document/d/1xI8hj6xi6dqKEPklbn9H8nXUGhvN8OpxdDhpVNPSLc8/edit?tab=t.0), [bản bàn giao](../../docs/template2/members/quy-phuc/05-thiet-ke-giao-dien.md). |
| **T2-18** | 26/11/2026 (UTC+7) | Lê Quý Phúc (`24120121`) | OpenAI Codex (GPT-6) | Đọc README, xác định các mục Template 2 cá nhân và xuất Markdown theo hướng dẫn. | **AI tạo:** Đồng bộ 5.1.1, 5.1.2, 5.2.4 và 5.2.6 với PDF nhóm. Trích Hình 5.1, cập nhật danh mục màn hình và bảng sự kiện. **Kiểm chứng:** Codex đối chiếu phạm vi với checklist SCRUM-61, bảng sự kiện với PDF, bảy hình với ảnh nhúng và đường dẫn tệp trong repo. | [Bản bàn giao](../../docs/template2/members/quy-phuc/05-thiet-ke-giao-dien.md) · [Checklist SCRUM-61](../../task/template2/quy-phuc.md) |

#### Phiên T2-17: Hoàn thành SCRUM-61 theo SRS và Figma v3, cập nhật Google Doc chung.

- **Thời gian:** 21/11/2026 (UTC+7)
- **Tác giả:** Lê Quý Phúc (`24120121`)
- **Công cụ/Model:** OpenAI Codex (GPT-6), Google Workspace MCP
- **Prompt đã khử dữ liệu nhạy cảm:** Hoàn thành SCRUM-61 theo SRS và Figma v3, cập nhật Google Doc chung.
- **Nội dung AI tạo:** Sơ đồ luồng, danh mục Node ID, đặc tả Copilot/Admin, bảng sự kiện và bộ ảnh bàn giao.
- **Nội dung tự kiểm chứng & hiệu chỉnh:** Đối chiếu ảnh PNG với bộ xuất Figma v3, hành vi API với SRS/MVP Contracts. Khôi phục tiêu đề 5.1.1 và dùng tài khoản đã xác thực để chèn ảnh. Kiểm tra lại 7 hình trong bản xuất Google Docs và đối chiếu các mục liền kề. Các trạng thái chưa thấy frame v3 được ghi rõ.
- **Minh chứng/Commit:** [Google Doc chung](https://docs.google.com/document/d/1xI8hj6xi6dqKEPklbn9H8nXUGhvN8OpxdDhpVNPSLc8/edit?tab=t.0), [bản bàn giao](../../docs/template2/members/quy-phuc/05-thiet-ke-giao-dien.md).

---

#### Phiên T2-18: Đọc README, xác định các mục Template 2 cá nhân và xuất Markdown theo hướng dẫn.

- **Thời gian:** 26/11/2026 (UTC+7)
- **Tác giả:** Lê Quý Phúc (`24120121`)
- **Công cụ/Model:** OpenAI Codex (GPT-6)
- **Prompt đã khử dữ liệu nhạy cảm:** Đọc README, xác định các mục Template 2 cá nhân và xuất Markdown theo hướng dẫn.
- **Nội dung AI tạo:** Đồng bộ 5.1.1, 5.1.2, 5.2.4 và 5.2.6 với PDF nhóm. Trích Hình 5.1, cập nhật danh mục màn hình và bảng sự kiện.
- **Nội dung tự kiểm chứng & hiệu chỉnh:** Codex đối chiếu phạm vi với checklist SCRUM-61, bảng sự kiện với PDF, bảy hình với ảnh nhúng và đường dẫn tệp trong repo.
- **Minh chứng/Commit:** [Bản bàn giao](../../docs/template2/members/quy-phuc/05-thiet-ke-giao-dien.md) · [Checklist SCRUM-61](../../task/template2/quy-phuc.md)

---

### 2.5 Ngô Viết Thanh Bình — Đóng gói Template 2

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| **T2-19** | 26/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium) | Hợp nhất 4 nhánh thành viên và đóng gói bộ nộp Template 2 (`ai-usage`, `report`, `git-contributions`, `4.zip`) | AI hỗ trợ merge 4 nhánh thành viên vào `merge-template2`, tổng hợp nguyên văn nhật ký AI của 4 thành viên, ánh xạ 26 hình từ `Report.pdf` & kho ảnh Figma ver3/draw.io vào `report/report.md` (giữ nguyên 100% câu chữ bản chốt), cập nhật lịch sử Git và xuất HTML chuẩn Template 1; sinh viên kiểm chứng SHA-256, đường dẫn ảnh và bố cục HTML | `report/Report.pdf`; `report/report.md`; `ai-usage/ai-usage.md`; `git-contributions/git-contributions.md`; nhánh `merge-template2` (`SCRUM-55`) |

#### Phiên T2-19: Hợp nhất nhánh và đóng gói bộ nộp Template 2

- **1. Thời gian:** 26/11/2026.
- **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm).
- **3. Công cụ / Model:** Antigravity AI (Gemini 4 Argon Medium) via Antigravity IDE.
- **4. Prompt đã khử dữ liệu nhạy cảm:** Tạo nhánh `merge-template2` hợp nhất bài làm của tất cả thành viên; tổng hợp file `ai-usage` (`.md` và `.html`) dựa theo chính xác nội dung các thành viên đã thực hiện theo chuẩn định dạng Template 1; đưa hai bản tải về từ Google Docs (`Report.pdf` và `report.md`) vào phần nộp bài kèm đầy đủ hình ảnh trong `assets/` mà tuyệt đối không sửa nội dung chữ; cập nhật `git-contributions` (`.md` và `.html`) mới nhất từ repo.
- **5. Nội dung AI tạo:** Script đóng gói `scripts/package_template2.py`, bộ báo cáo `ai-usage/ai-usage.md` & `.html`, `report/Report.pdf`, `report/report.md` kèm 26 tệp hình ảnh sắc nét trong `report/assets/{diagrams,ui}/`, `git-contributions/git-contributions.md` & `.html` và tệp nén `4.zip`.
- **6. Nội dung tự kiểm chứng & hiệu chỉnh:** Đối chiếu fingerprint văn bản giữa file Markdown tải từ Google Docs và `report/report.md` đạt khớp 100% từng từ; kiểm tra 5 sơ đồ lớp trích nguyên gốc từ đối tượng ảnh 2000px trong `Report.pdf`, 5 sơ đồ kiến trúc/EER/ERD/Screen Flow và 16 ảnh giao diện Figma ver3; xác minh toàn bộ 18 phiên AI cá nhân và toàn bộ lịch sử commit Git không sai lệch.
- **7. Minh chứng / Commit:** `reports/template2/`, `docs/template2/release/`, nhánh `merge-template2` (`SCRUM-55`).

---

## 3. CAM KẾT ĐẠO ĐỨC HỌC THUẬT

Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:

1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.
2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.
