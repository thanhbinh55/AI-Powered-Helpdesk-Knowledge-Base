# HƯỚNG DẪN GIAO VIỆC GIAI ĐOẠN 2: TEMPLATE 2 & CODE MVP (CLARUNE — NHÓM 04)

> **Cập nhật:** 20/11/2026 | **Đọc trong 3 phút để biết: Làm gì · Nộp ở đâu · Khi nào xong**
>
> **Liên kết bắt buộc:**
> - **Google Doc chung Template 2 (`Template2-ThietKe.docx`):** [Mở Google Doc Template 2](https://docs.google.com/document/d/1VrXi7rRO8nY6pnksHw7wJgMWs6SoptZQ/edit)
> - **Figma UI/UX chính thức (ver3):** [Figma SE ver3 (`node-id=111-3978`)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=111-3978&p=f&m=dev)
> - **Kho bài mẫu K23 tham khảo (Planora, Katling, SmartSpend):** [Thư mục Google Drive K23](https://drive.google.com/drive/folders/1Vk7wPTVLxhoxhTLnqAhIQlQxfslToMGU)
> - **Tài liệu gốc nhóm:** [`reports/template1/report/report.md`](reports/template1/report/report.md) · [`reports/SRS-master.md`](reports/SRS-master.md) · [`reports/MVP_CONTRACTS.md`](reports/MVP_CONTRACTS.md)
> - **Chốt Domain dữ liệu MVP:** Lĩnh vực **Đồ điện tử** (Crawl dữ liệu FAQ + Chính sách bảo hành, đổi trả, hướng dẫn kỹ thuật).

---

## 1. TỔNG QUAN 2 LUỒNG & MỐC THỜI GIAN CỨNG

Nhóm chạy song song 2 luồng từ **20/11/2026**: **Luồng 1 (Thiết kế Template 2)** và **Luồng 2 (Code MVP P0 + Kiểm thử Template 3)**.

| Cột mốc | Hạn chót | Luồng 1: Tài liệu Thiết kế (Template 2) | Luồng 2: Code MVP (Đồ điện tử) & Template 3 |
| :---: | :---: | :--- | :--- |
| **Mốc 1** | **23/11** | **Hoàn thành 100% nội dung** các mục được giao trên Google Doc chung & vẽ xong sơ đồ | Xong Spring Boot + Docker `pgvector` (**21/11**); chốt Flyway V1–V5 & OpenAPI Contract (**22/11**) |
| **Mốc 2** | **24/11** | **Review chéo cả ngày** trực tiếp trên Google Doc chung (Gia Phúc chủ trì đối soát nhất quán) | Xong GitHub Actions CI & **Crawl xong bộ FAQ/Policy Đồ điện tử** (**24/11**) |
| **Mốc 3** | **25/11** | **Commit Markdown, sơ đồ & AI Usage cá nhân lên GitHub** | Code lõi các phân hệ theo Figma ver3: Identity (**27/11**), Ticket (**29/11**), KB (**30/11**) |
| **Mốc 4** | **Trước 26/11** | **Leader (Bình) & Lãm tổng hợp chốt bản hoàn chỉnh Template 2** *(Hạn nộp trường: **28/11**)* | Code xong AI RAG + Workflow Apply (**01/12**) |
| **Mốc 5** | **05/12** | — | Xong Unit/Integration Test (**03/12**), QA tổng hợp (**04/12**), **E2E & Code Freeze MVP P0 (05/12)** |
| **Mốc 6** | **12/12** | — | Test Plan $\ge 25$ ca (**06/12**), Regression & Eval 30 câu AI (**07/12**), gói Template 3 & Demo (**10/12**, **Nộp 12/12**) |

---

## 2. QUY TẮC THƯ MỤC, NHÁNH GIT & VỊ TRÍ COMMIT (0% CONFLICT)

Mỗi thành viên chỉ làm việc và commit vào **đúng thư mục riêng của mình**. Cấm sửa trực tiếp file trong thư mục của thành viên khác.

| Thành viên (MSSV) | `docs/` (Template 2 & 3) | `code/` (Backend, Frontend, Crawler) | `task/` (Checklist cá nhân) | `ai-usage/` (Nhật ký AI riêng) |
| :--- | :--- | :--- | :--- | :--- |
| **Ngô Viết Thanh Bình**<br>`24120269` | `docs/template2/members/binh/`<br>`docs/template3/members/binh/` | `backend/.../identity/`<br>`frontend/src/features/identity/` | `task/template2/binh.md`<br>`task/mvp-template3/binh.md` | `ai-usage/template2/binh.md`<br>`ai-usage/mvp-template3/binh.md` |
| **Phan Gia Phúc**<br>`24120503` | `docs/template2/members/gia-phuc/`<br>`docs/template3/members/gia-phuc/` | `backend/.../ticket/`, `.../workflow/`<br>`frontend/src/features/ticket/` | `task/template2/gia-phuc.md`<br>`task/mvp-template3/gia-phuc.md` | `ai-usage/template2/gia-phuc.md`<br>`ai-usage/mvp-template3/gia-phuc.md` |
| **Nguyễn Đức Lãm**<br>`24120083` | `docs/template2/members/lam/`<br>`docs/template3/members/lam/` | `backend/.../knowledge/`, `crawler/`<br>`frontend/src/features/knowledge/` | `task/template2/lam.md`<br>`task/mvp-template3/lam.md` | `ai-usage/template2/lam.md`<br>`ai-usage/mvp-template3/lam.md` |
| **Lê Quý Phúc**<br>`24120121` | `docs/template2/members/quy-phuc/`<br>`docs/template3/members/quy-phuc/` | `backend/.../ai/`<br>`frontend/src/features/ai/` | `task/template2/quy-phuc.md`<br>`task/mvp-template3/quy-phuc.md` | `ai-usage/template2/quy-phuc.md`<br>`ai-usage/mvp-template3/quy-phuc.md` |

* **Tên nhánh:** `docs/t2-<ten>` (tài liệu T2), `docs/t3-<ten>` (tài liệu T3), `feat/<phan-he>-<tinh-nang>` (code), `test/<phan-he>-<tinh-nang>` (test).
* **Commit Message (bắt buộc gắn mã Jira thật):** `<type>(<scope>): <mô tả ngắn> SCRUM-<số>` *(VD: `docs(template2): hoan thien muc 3.2 class diagram SCRUM-66`)*.
* **Quy chuẩn Sơ đồ & AI Usage:** Xuất song song `.drawio` + `.svg`/`.png` nét rõ vào `docs/template2/assets/diagrams/`; ghi nhận phiên dùng AI vào file `ai-usage/.../<ten>.md` (đủ 7 trường theo quy định Khoa CNTT).

---

## 3. BẢNG PHÂN CÔNG & CHECKLIST THỰC HIỆN TỪNG THÀNH VIÊN

### 3.1. Ngô Viết Thanh Bình (`24120269` — Trưởng nhóm · Identity & Hạ tầng)

| Luồng | Mã Jira | Đầu việc | Hạn chót | Tiêu chí hoàn thành (DoD) & Nguồn tham khảo |
| :---: | :---: | :--- | :---: | :--- |
| **Luồng 1**<br>(T2) | **`SCRUM-59`** | Mục 3.1 Cây phân rã hệ thống & Sơ đồ kiến trúc 3-Tier/C4 | **23/11** | - Vẽ cây phân rã dọc 4 phân hệ & sơ đồ kiến trúc (React, Spring Boot Modular Monolith, PostgreSQL `pgvector`, External LLM/Embedding).<br>- Mô tả tầng Client/Server/DB, công nghệ sử dụng & ranh giới port.<br>- *Tham khảo:* Mục 3.1 mẫu K23 (Planora/Katling) và `reports/SRS-master.md` (Mục 9). |
| **Luồng 1**<br>(T2) | **`SCRUM-55`** | Phối hợp Lãm tổng hợp & chốt gói Template 2 | **25/11** | - Gộp bài 4 thành viên từ `docs/template2/members/`, kiểm tra bố cục A4/mục lục trước **26/11**; chuẩn bị nộp trường hạn **28/11**. |
| **Luồng 2**<br>(MVP) | **`SCRUM-26`** | Khởi tạo Spring Boot 3, Docker `pgvector`, Error Envelope & Principal | **21/11** | - Dựng xong `backend/` (Java 21, Maven), `docker-compose.yml` PostgreSQL 16 + `pgvector`.<br>- Chuẩn hóa `ErrorEnvelope` và `ActorPrincipal` theo `reports/MVP_CONTRACTS.md` (Mục 1–3). |
| **Luồng 2**<br>(MVP) | **`SCRUM-35`** | Code Identity API (JWT, Refresh Rotation, RBAC) & UI ver3 | **27/11** | - Hoàn thành `UC-01..04` (Register mặc định Customer, BCrypt, Refresh Rotation, Profile, Admin Agents).<br>- Ghép UI Identity theo **Figma ver3 (`node 111:3978`)** + Axios 401 Interceptor. |
| **Luồng 2**<br>(MVP) | **`SCRUM-45`** | Test Identity Security & Session (`TC-ID-01..06`) | **03/12** | - Pass kiểm thử tự động: đăng ký ép role bị chặn, token hết hạn/rotated bị thu hồi, disabled agent trả HTTP 403. |
| **Luồng 2**<br>(T3) | **`SCRUM-64`** | Phối hợp chốt Báo cáo Template 3 & Demo App | **10/12** | - Đảm bảo Demo chạy mượt trên Docker, nộp gói Template 3 đúng hạn **12/12**. |

### 3.2. Phan Gia Phúc (`24120503` — Phân hệ Ticket · Workflow · QA Lead)

| Luồng | Mã Jira | Đầu việc | Hạn chót | Tiêu chí hoàn thành (DoD) & Nguồn tham khảo |
| :---: | :---: | :--- | :---: | :--- |
| **Luồng 1**<br>(T2) | **`SCRUM-66`** | Mục 3.2 Sơ đồ lớp (Class Diagram) & Mục 3.3 Đặc tả lớp 4 phân hệ | **23/11** | - Vẽ Class Diagram tổng thể (Entity/Domain/Service cốt lõi) cho cả 4 phân hệ.<br>- Lập bảng đặc tả lớp (Thuộc tính, Phương thức, Modifier, Ràng buộc, Mô tả).<br>- *Tham khảo:* Mục 3.2–3.3 mẫu K23 (Planora/Katling) & `Template1` (19 UCs). |
| **Luồng 1**<br>(T2) | **`SCRUM-62`** | Chủ trì Review chéo & Đối soát nhất quán trên Google Doc | **24/11** | - Kiểm tra chéo 100% tính khớp giữa EER $\leftrightarrow$ Class $\leftrightarrow$ ERD $\leftrightarrow$ UI ver3 $\leftrightarrow$ SRS.<br>- Chốt danh sách chỉnh sửa ngay trên Google Doc để thành viên sửa trước 25/11. |
| **Luồng 2**<br>(MVP) | **`SCRUM-42`** | Chốt OpenAPI Spec, DTO Ports & Error Codes giữa 4 module | **22/11** | - Chốt DTO, Enum trạng thái ticket (`OPEN`, `IN_PROGRESS`, `WAITING_CUSTOMER`, `RESOLVED`, `CLOSED`), Public Ports & mã lỗi `400/401/403/404/409` theo `MVP_CONTRACTS.md`. |
| **Luồng 2**<br>(MVP) | **`SCRUM-36`** | Code Ticket (State Machine, Claim Lock 409, Chat) & UI ver3 | **29/11** | - Cài đặt `UC-05..10`: Atomic Claim Lock (tránh 2 Agent nhận trùng), Internal Note ẩn với Customer, Audit Trail.<br>- Ghép UI Customer Portal & Agent Workspace theo **Figma ver3**. |
| **Luồng 2**<br>(MVP) | **`SCRUM-56`** | Workflow nguyên tử Apply/Discard AI Suggestion | **01/12** | - Khóa ticket + suggestion cùng transaction (`UC-15`): tạo tin nhắn `PUBLIC` và đổi trạng thái `APPLIED`/`DISCARDED` an toàn. |
| **Luồng 2**<br>(MVP) | **`SCRUM-46`**<br>**`SCRUM-39`** | Test Ticket Concurrency (`TC-CON-01/02`) & Tổng hợp QA 4 module | **03/12**<br>**04/12** | - Chạy test tranh chấp đồng thời trên PostgreSQL thật (đúng 1 winner, 1 nhận HTTP 409).<br>- Tổng hợp kết quả pass/fail 4 module ngày 04/12. |
| **Luồng 2**<br>(MVP) | **`SCRUM-40`** | Kiểm thử tích hợp E2E & **Code Freeze MVP P0** | **05/12** | - Thông suốt luồng Login $\to$ Ticket Đồ điện tử $\to$ Claim $\to$ KB $\to$ AI Suggest $\to$ Send; chốt Code Freeze. |
| **Luồng 2**<br>(T3) | **`SCRUM-63`**<br>**`SCRUM-53`** | Lập Test Plan ($\ge 25$ ca) & Chạy Regression Template 3 | **06/12**<br>**07/12** | - Điều phối 4 thành viên viết $\ge 25$ ca (5 chức năng × 5 ca) theo mẫu `template3-testing-requirements.md`.<br>- Chạy thực tế trên Demo App, điền `Actual Output` & `Result` trung thực. |

### 3.3. Nguyễn Đức Lãm (`24120083` — Knowledge Base · Dữ liệu · Release Lead)

| Luồng | Mã Jira | Đầu việc | Hạn chót | Tiêu chí hoàn thành (DoD) & Nguồn tham khảo |
| :---: | :---: | :--- | :---: | :--- |
| **Luồng 1**<br>(T2) | **`SCRUM-58`** | Mục 1 Bảng đánh giá & Mục 2 Mô hình quan niệm (EER) | **23/11** | - Điền Mục 1 và vẽ sơ đồ EER (thực thể ngữ nghĩa, thuộc tính, quan hệ, lực lượng cardinality).<br>- *Lưu ý:* EER là mô hình nghiệp vụ (khác với ERD vật lý). *Tham khảo:* Mục 2 bài mẫu K23 (SmartSpend/Katling). |
| **Luồng 1**<br>(T2) | **`SCRUM-60`** | Mục 4.1 Sơ đồ dữ liệu (ERD) & Mục 4.2 Đặc tả dữ liệu V1–V5 | **23/11** | - Vẽ ERD vật lý có PK/FK/Cardinality, khớp 100% với schema `pgvector`.<br>- Lập bảng đặc tả đủ từng cột (Tên cột, Kiểu, PK/FK, Nullable/Default, Ràng buộc, Mô tả) cho các bảng `V1..V5`. |
| **Luồng 1**<br>(T2) | **`SCRUM-55`** | Chủ trì tổng hợp & xuất bản Template 2 trên GitHub | **25/11** | - Gom bài từ `docs/template2/members/`, kiểm tra lại mục lục/hình ảnh, phối hợp Bình chốt bản final trước **26/11**. |
| **Luồng 2**<br>(MVP) | **`SCRUM-44`** | Flyway Baseline Migrations V1–V5 khớp Template 2 | **22/11** | - Phối hợp 4 owner hoàn thiện `V1__init_identity.sql` đến `V5__add_ticket_message_suggestion_fk.sql` chạy sạch trên PostgreSQL 16 + `pgvector`. |
| **Luồng 2**<br>(MVP) | **`SCRUM-51`** | **Crawl bộ dữ liệu Đồ điện tử** & Chốt `EmbeddingProvider` | **24/11** | - Viết script trong `crawler/scripts/` crawl bộ **FAQ + Chính sách bảo hành/đổi trả Đồ điện tử** vào `crawler/corpus/electronics-faq-policy/`.<br>- Chốt model, số chiều vector và interface `EmbeddingProvider`. |
| **Luồng 2**<br>(MVP) | **`SCRUM-37`** | Code KB (`SKIP LOCKED`, Chunking, pgvector Search) & UI ver3 | **30/11** | - Cài đặt `UC-11..13`: Upload (tối đa 10 MiB), Worker `FOR UPDATE SKIP LOCKED` (retry $\le 3$), Publish/Archive, Vector Cosine Search.<br>- Ghép UI Knowledge Base theo **Figma ver3**. |
| **Luồng 2**<br>(MVP) | **`SCRUM-47`**<br>**`SCRUM-49`** | Test Worker/Vector (`TC-KB`) & Clean Smoke Test + Seed Đồ điện tử | **03/12**<br>**05/12** | - Test lease token, từ chối file giả/PDF scan, Archive loại khỏi search.<br>- Chạy `docker compose` dựng sạch DB + seed corpus Đồ điện tử thành công. |
| **Luồng 2**<br>(T3) | **`SCRUM-64`** | Tổng hợp Báo cáo Kiểm thử cuối kỳ Template 3 | **10/12** | - Gom test cases + kết quả chạy thật + đánh giá AI vào `docs/template3/release/` trước hạn nộp **12/12**. |

### 3.4. Lê Quý Phúc (`24120121` — AI Assistance · CI · UI/UX ver3 Lead)

| Luồng | Mã Jira | Đầu việc | Hạn chót | Tiêu chí hoàn thành (DoD) & Nguồn tham khảo |
| :---: | :---: | :--- | :---: | :--- |
| **Luồng 1**<br>(T2) | **`SCRUM-61`** | Mục 5.1 Sơ đồ màn hình & Mục 5.2 Đặc tả giao diện (Figma ver3) | **23/11** | - Vẽ Screen Flow Diagram (Customer, Agent, Admin) + xuất ảnh màn hình từ **Figma ver3 (`node 111:3978`)**.<br>- Mô tả thành phần màn hình & bảng Xử lý sự kiện (`Event Handling`: Đối tượng, Trigger, Hành vi hệ thống/API).<br>- *Tham khảo:* Mục 5 bài mẫu K23 (SmartSpend/Planora). |
| **Luồng 2**<br>(MVP) | **`SCRUM-43`** | Cấu hình GitHub Actions CI Pipeline | **24/11** | - Chạy tự động Maven test (với PostgreSQL container) và `npm run build` cho Frontend trên mỗi Pull Request. |
| **Luồng 2**<br>(MVP) | **`SCRUM-38`** | Code AI (RAG Đồ điện tử, Citation, Abstention) & UI ver3 | **01/12** | - Cài đặt `UC-14, 15, 18`: Trích ngữ cảnh loại bỏ `INTERNAL_NOTE`, Citation Validation + Snapshot (`BR-12`), từ chối khi thiếu chứng cứ (`BR-13`).<br>- Ghép UI AI Copilot Widget theo **Figma ver3**. |
| **Luồng 2**<br>(MVP) | **`SCRUM-48`** | Test AI RAG Contract & Double-Send Suggestion Race (`TC-AI`) | **03/12** | - Test fail-closed khi nguồn trích dẫn giả, test nhánh `INSUFFICIENT_EVIDENCE` và race condition double-send. |
| **Luồng 2**<br>(T3) | **`QA1-EVAL-01`**<br>(`SCRUM-54`) | Đánh giá chất lượng AI RAG trên bộ $\ge 30$ câu Đồ điện tử | **07/12** | - Tạo bộ $\ge 30$ câu hỏi có nhãn (có nguồn + ngoài phạm vi để test từ chối) tại `crawler/eval/` và đo tỷ lệ chính xác phục vụ Template 3. |

---

## 4. QUY TRÌNH REVIEW CHÉO (24/11) & CHỐT COMMIT (25/11)

### 4.1. Ngày 24/11 — Review chéo trên Google Doc chung
* **Vòng xoay review:** **Bình $\to$ Lãm $\to$ Gia Phúc $\to$ Quý Phúc $\to$ Bình** *(Gia Phúc tổng hợp đối soát chéo toàn bài tại `SCRUM-62`)*.
* **Thao tác:** Dùng chế độ **Suggesting / Comment** trực tiếp trên [Google Doc chung](https://docs.google.com/document/d/1VrXi7rRO8nY6pnksHw7wJgMWs6SoptZQ/edit).
* **4 điểm bắt buộc kiểm tra:**
  1. **EER $\neq$ ERD:** Mục 2 là mô hình quan niệm (nghiệp vụ), không copy bảng khóa ngoại của Mục 4 sang.
  2. **Khớp Schema V1–V5:** Tên bảng, kiểu dữ liệu (`pgvector`), FK ở Mục 4 khớp 100% với SQL migrations.
  3. **Khớp Figma ver3:** Ảnh chụp & bảng sự kiện ở Mục 5 đúng theo **Figma ver3 (`node 111:3978`)**, không lấy ảnh cũ ver1/ver2.
  4. **Đủ nhãn P0/P1:** Chức năng nào thuộc P1 chưa cài đặt ở MVP phải ghi rõ `PLANNED (P1)`.

### 4.2. Ngày 25/11 — Commit GitHub & Tổng hợp chốt trước 26/11
1. Sau khi sửa xong comment trên Google Doc, mỗi thành viên tạo nhánh `docs/t2-<ten>`.
2. Xuất nội dung phần mình sang Markdown + file nguồn sơ đồ (`.drawio`, `.svg`/`.png`) vào đúng thư mục `docs/template2/members/<ten>/`.
3. Cập nhật checklist trong `task/template2/<ten>.md` và ghi nhật ký AI vào `ai-usage/template2/<ten>.md`.
4. Commit gắn mã `SCRUM-xx` và mở PR lên GitHub trong ngày **25/11**.
5. **Nguyễn Đức Lãm** & **Ngô Viết Thanh Bình** gộp bài vào `docs/template2/release/`, kiểm tra dàn trang PDF/Word và chốt bản hoàn chỉnh **trước 26/11** (sẵn sàng nộp trường hạn **28/11**).

