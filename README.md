# CLARUNE — AI-POWERED HELPDESK & KNOWLEDGE BASE

[![Docs Quality Check](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/actions/workflows/docs-check.yml/badge.svg)](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/actions)
[![Course](https://img.shields.io/badge/Course-HCMUS%20Intro%20to%20Software%20Engineering-blue)](https://www.fit.hcmus.edu.vn/)
[![Group](https://img.shields.io/badge/Group-04%20(Clarune)-emerald)](members.csv)
[![Phase](https://img.shields.io/badge/Current%20Phase-Phase%202%3A%20Template%202%20%26%20MVP%20Code-orange)](TEAM_GUIDE_PHASE2.md)
[![Domain](https://img.shields.io/badge/Domain%20Knowledge-Electronics%20FAQ%20%26%20Policy-teal)](crawler/corpus/electronics-faq-policy)
[![Jira](https://img.shields.io/badge/Jira-SCRUM-0052CC?logo=jira)](https://ngovietthanhbinh2006-1790671331599.atlassian.net)

**Clarune** là hệ thống quản lý yêu cầu hỗ trợ khách hàng (Helpdesk) và cơ sở tri thức tích hợp trợ lý AI (RAG có trích dẫn nguồn, kiểm soát con người duyệt trước khi gửi — *Human-in-the-loop*).  
Đồ án môn **Nhập môn Công nghệ Phần mềm** — Khoa Công nghệ Thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS).

---

## TRỌNG TÂM HIỆN TẠI — GIAI ĐOẠN 2 (TỪ 20/11/2026)

Nhóm đang triển khai song song **Luồng 1 (Thiết kế phần mềm — Template 2)** và **Luồng 2 (Code MVP P0 + Crawler Đồ điện tử + Kiểm thử Template 3)**:

| Tài nguyên trọng tâm | Liên kết trực tiếp | Mục đích & Hạn chót |
| :--- | :--- | :--- |
| **Hướng dẫn giao việc & Checklist Giai đoạn 2** | [`TEAM_GUIDE_PHASE2.md`](TEAM_GUIDE_PHASE2.md) | Đọc trong 3 phút để nắm timeline, vị trí commit riêng & checklist từng thành viên |
| **Bản mẫu Draft Master Template 2** | [`docs/template2/TEMPLATE2_DRAFT_MASTER.md`](docs/template2/TEMPLATE2_DRAFT_MASTER.md) · [`docs/template2/README.md`](docs/template2/README.md) | Bản nháp đầy đủ Mục 1–6 khớp 100% `SRS-master` & `MVP_CONTRACTS` |
| **Google Doc chung Template 2** | [[SE - Nhóm 4] Template2-ThietKe-Clarune-04](https://docs.google.com/document/d/1xI8hj6xi6dqKEPklbn9H8nXUGhvN8OpxdDhpVNPSLc8/edit?tab=t.0) | Hoàn thiện nội dung (**23/11**) · Review chéo (**24/11**) · Chốt nộp (**25–26/11**, hạn trường **28/11**) |
| **Thiết kế UI/UX chính thức (Figma ver3)** | [Figma SE — Bản ver3 (`node-id=111-3978`)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=111-3978&p=f&m=dev) | UI/UX chuẩn dùng cho Template 2 và cài đặt Frontend MVP *(tham chiếu [Redesign v2](docs/design/man-hinh.md))* |
| **Đặc tả & Hợp đồng kỹ thuật chuẩn** | [`reports/SRS-master.md`](reports/SRS-master.md) · [`reports/MVP_CONTRACTS.md`](reports/MVP_CONTRACTS.md) | Chuẩn schema Flyway `V1–V5`, State Machine, Public Ports, REST API `/api/v1/*` |
| **Quản lý công việc (Jira Cloud)** | [Bảng SCRUM Jira](https://ngovietthanhbinh2006-1790671331599.atlassian.net) · [`task/jira/tasks_phase2_updated.csv`](task/jira/tasks_phase2_updated.csv) | Theo dõi tiến độ **Code Freeze MVP P0 (05/12)** & **Template 3 (12/12)** |
| **Kho bài mẫu tham khảo K23** | [Thư mục Google Drive K23](https://drive.google.com/drive/folders/1Vk7wPTVLxhoxhTLnqAhIQlQxfslToMGU?usp=sharing) | Đối chiếu chuẩn trình bày Template 2 & Template 3 |

---

## 1. LỘ TRÌNH & TÀI LIỆU CÁC GIAI ĐOẠN (PROJECT PHASES)

| Giai đoạn | Hạn nộp | Trạng thái | Tài liệu & Sản phẩm đầu ra chính |
| :--- | :---: | :---: | :--- |
| **Template 0**<br/>*Project Proposal* | 31/10/2026 | **Đã hoàn thành** | [`reports/00-project-proposal.md`](reports/00-project-proposal.md) · [`reports/template0/`](reports/template0/) · [`TEAM_GUIDE_TEMPLATE0.md`](TEAM_GUIDE_TEMPLATE0.md) |
| **Template 1**<br/>*Requirements & Prototype* | 12/11/2026 | **Đã hoàn thành** | [`Report.pdf`](reports/template1/report/Report.pdf) · [`report.md`](reports/template1/report/report.md) · [Bộ 6 sơ đồ UML](reports/template1/report/assets/diagrams/) · [AI Usage T1](reports/template1/06-ai-usage.md) · [Gói Template 1](reports/template1/README.md) |
| **Template 2** *(Luồng 1)*<br/>*Software Design* | **28/11/2026**<br/>*(Nội bộ < 26/11)* | **Đang thực hiện** | [`TEAM_GUIDE_PHASE2.md`](TEAM_GUIDE_PHASE2.md) · [`docs/template2/TEMPLATE2_DRAFT_MASTER.md`](docs/template2/TEMPLATE2_DRAFT_MASTER.md) · [`docs/template2/members/`](docs/template2/members/) · [`task/template2/`](task/template2/) · [`ai-usage/template2/`](ai-usage/template2/) |
| **MVP Code & Template 3** *(Luồng 2)*<br/>*Implementation & Testing* | **05/12** *(MVP)*<br/>**12/12** *(Nộp T3)* | **Đang thực hiện** | [`backend/`](backend/) · [`frontend/`](frontend/) · [`crawler/`](crawler/) *(FAQ & Policy Đồ điện tử)* · [`docs/template3/`](docs/template3/) · [`task/mvp-template3/`](task/mvp-template3/) · [`ai-usage/mvp-template3/`](ai-usage/mvp-template3/) |

### Các cột mốc bắt buộc sắp tới
- **21/11 – 22/11:** Dựng xong khung Spring Boot 3 + Docker `pgvector` (`SCRUM-26`), chốt Flyway `V1–V5` (`SCRUM-44`) & OpenAPI Contract (`SCRUM-42`).
- **23/11:** Hoàn tất 100% nội dung và hình vẽ **Template 2** trên Google Doc chung.
- **24/11:** Review chéo cả ngày trên Google Doc (vòng Bình $\to$ Lãm $\to$ Gia Phúc $\to$ Quý Phúc); xong GitHub Actions CI (`SCRUM-43`) và crawl xong bộ **FAQ/Policy Đồ điện tử** (`SCRUM-51`).
- **25/11 (Chốt trước 26/11):** Commit tài liệu/sơ đồ/AI log lên GitHub, Leader & Lãm đóng gói bản hoàn chỉnh **Template 2** (nộp trường hạn **28/11**).
- **27/11 – 01/12:** Hoàn thành code 4 phân hệ & workflow theo Figma ver3: `identity` (`27/11`), `ticket` (`29/11`), `knowledge` (`30/11`), `ai + workflow` (`01/12`).
- **03/12 – 05/12:** Hoàn tất Unit/Integration/Concurrency Tests, kiểm thử tích hợp E2E và **Code Freeze MVP P0 (05/12)**.
- **06/12 – 12/12:** Lập Test Plan ($\ge 25$ ca kiểm thử), chạy Regression & Đánh giá chất lượng AI ($\ge 30$ câu Đồ điện tử), hoàn tất báo cáo **Template 3 & Demo App (nộp 12/12)**.

---

## 2. THÀNH VIÊN NHÓM 04 & KHÔNG GIAN LÀM VIỆC ĐỘC LẬP

Thông tin tài khoản đồng bộ tại [`members.csv`](members.csv). Mỗi thành viên làm việc và commit vào **đúng thư mục riêng** để tránh conflict khi phát triển song song:

| MSSV | Họ và tên | Git Username | Phân hệ phụ trách chính | Thư mục `docs/` & `task/` & `ai-usage/` cá nhân |
| :---: | :--- | :--- | :--- | :--- |
| `24120269` | **Ngô Viết Thanh Bình** *(Trưởng nhóm)* | `thanhbinh55` | `identity` & Hạ tầng Spring Boot / Docker | [`docs/template2/members/binh/`](docs/template2/members/binh/) · [`task/template2/binh.md`](task/template2/binh.md) · [`ai-usage/template2/binh.md`](ai-usage/template2/binh.md) |
| `24120503` | **Phan Gia Phúc** | `t4lf4n` | `ticket` · `workflow` · QA Lead & Đối soát | [`docs/template2/members/gia-phuc/`](docs/template2/members/gia-phuc/) · [`task/template2/gia-phuc.md`](task/template2/gia-phuc.md) · [`ai-usage/template2/gia-phuc.md`](ai-usage/template2/gia-phuc.md) |
| `24120083` | **Nguyễn Đức Lãm** | `Lamnguyen-code` | `knowledge` · Crawler · Flyway & Release Lead | [`docs/template2/members/lam/`](docs/template2/members/lam/) · [`task/template2/lam.md`](task/template2/lam.md) · [`ai-usage/template2/lam.md`](ai-usage/template2/lam.md) |
| `24120121` | **Lê Quý Phúc** | `Shinkiisme` | `ai` · CI Pipeline · UI/UX Figma ver3 | [`docs/template2/members/quy-phuc/`](docs/template2/members/quy-phuc/) · [`task/template2/quy-phuc.md`](task/template2/quy-phuc.md) · [`ai-usage/template2/quy-phuc.md`](ai-usage/template2/quy-phuc.md) |

> **Quy tắc nhánh & commit:** Đặt tên nhánh `docs/t2-<ten>`, `docs/t3-<ten>`, `feat/<phan-he>-<tinh-nang>`, `test/<phan-he>-<tinh-nang>`; mọi commit message **bắt buộc** có mã Jira `SCRUM-<số>` (hook [`.githooks/commit-msg`](.githooks/commit-msg) sẽ chặn nếu thiếu).

---

## 3. SƠ ĐỒ CẤU TRÚC THƯ MỤC (REPOSITORY STRUCTURE)

```text
/
├── README.md                              # Cổng điều hướng tổng dự án & các giai đoạn
├── TEAM_GUIDE_PHASE2.md                   # Hướng dẫn giao việc, timeline & checklist Giai đoạn 2
├── PLAN_TEMPLATE1_AND_DEVELOPMENT.md      # Kế hoạch tổng thể & đặc tả quy trình giai đoạn 1–2
├── CONTRIBUTING.md                        # Quy chuẩn Git branch, PR, review chéo & Jira
├── DESIGN.md                              # Quy tắc UI/UX & thứ tự ưu tiên tài liệu thiết kế
├── members.csv                            # Danh sách MSSV, Git/Jira email & module của 4 thành viên
├── .githooks/commit-msg                   # Git hook bắt buộc mã SCRUM-<số> trong commit message
├── .github/                               # PR/Issue templates, CODEOWNERS & CI docs-check.yml
│
├── docs/                                  # Tài liệu thiết kế, UI & kiểm thử giai đoạn mới
│   ├── design/                            # Danh mục màn hình Figma & audit UI (229 frames)
│   ├── template2/                         # Khu vực làm việc Template 2 (Thiết kế phần mềm)
│   │   ├── README.md                      # Tóm tắt phạm vi & phân công Template 2
│   │   ├── TEMPLATE2_DRAFT_MASTER.md      # Bản nháp hoàn chỉnh Mục 1–6 sẵn sàng đưa lên Google Doc
│   │   ├── assets/                        # Chứa diagrams (.drawio/.png/.svg) & ảnh UI Figma ver3
│   │   ├── members/{binh,gia-phuc,lam,quy-phuc}/  # Bài xuất Markdown & sơ đồ riêng từng người
│   │   └── release/                       # Gói bản hoàn chỉnh tổng hợp chốt trước 26/11
│   └── template3/                         # Khu vực làm việc Template 3 (Kiểm thử phần mềm)
│       ├── members/{binh,gia-phuc,lam,quy-phuc}/  # Test case & bằng chứng chạy thực tế riêng
│       └── release/                       # Báo cáo kiểm thử tổng hợp nộp 12/12
│
├── task/                                  # Checklist cá nhân & file đồng bộ Jira
│   ├── jira/tasks_phase2_updated.csv      # Dữ liệu Epic/Task đã đồng bộ lại ngày 20/11
│   ├── template2/<ten>.md                 # Checklist Template 2 riêng từng thành viên
│   └── mvp-template3/<ten>.md             # Checklist Code MVP & Template 3 riêng từng thành viên
│
├── ai-usage/                              # Nhật ký sử dụng AI tách riêng theo giai đoạn & thành viên
│   ├── template2/<ten>.md                 # Log AI giai đoạn Thiết kế Template 2
│   └── mvp-template3/<ten>.md             # Log AI giai đoạn Code MVP & Kiểm thử Template 3
│
├── crawler/                               # Dữ liệu tri thức miền Đồ điện tử (FAQ & Policy)
│   ├── scripts/                           # Script thu thập dữ liệu FAQ, bảo hành, đổi trả
│   ├── corpus/electronics-faq-policy/     # Corpus tài liệu sạch phục vụ Knowledge Base MVP
│   └── eval/                              # Bộ >= 30 câu hỏi có nhãn đánh giá AI RAG
│
├── backend/                               # Mã nguồn Backend Spring Boot 3 (Java 21, Modular Monolith)
├── frontend/                              # Mã nguồn Frontend React + TypeScript + Vite (Figma ver3)
├── infra/                                 # Cấu hình Docker Compose (PostgreSQL 16 + pgvector)
│
├── reports/                               # Kho báo cáo gốc & bản nộp các giai đoạn
│   ├── SRS-master.md                      # Đặc tả SRS tổng hợp (24 mục)
│   ├── MVP_CONTRACTS.md                   # Hợp đồng kỹ thuật P0 giữa 4 phân hệ & API
│   ├── template0/                         # Hồ sơ nộp Template 0 (Proposal)
│   ├── template1/                         # Hồ sơ nộp Template 1 (Report.pdf, diagrams, AI log)
│   └── template2/                         # Khung khởi tạo & bản đồng bộ draft Template 2
│
└── scripts/                               # Công cụ tự động hóa render, đóng gói & đồng bộ Jira
    ├── render_reports.sh (.py)            # Render Markdown sang HTML/PDF tiếng Việt
    ├── git_contributions.py               # Tổng hợp lịch sử commit theo members.csv
    ├── package_template1.py               # Đóng gói & kiểm tra giới hạn file nộp bài
    └── jira/                              # Script đồng bộ Jira Cloud API v3
```

---

## 4. HƯỚNG DẪN BẮT ĐẦU (QUICK START)

### 4.1. Clone Repository & Cài đặt Git Hook (Bắt buộc)
```bash
# 1. Clone repository về máy cá nhân
git clone https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base.git
cd AI-Powered-Helpdesk-Knowledge-Base

# 2. Kích hoạt Git hook kiểm tra mã Jira (SCRUM-<số>) trong commit message
git config core.hooksPath .githooks

# 3. Cấu hình tên và email tác giả khớp với members.csv
git config user.name "<git_username_cua_ban>"
git config user.email "<git_email_cua_ban>"
```

### 4.2. Cấu hình biến môi trường
```bash
cp .env.example .env
# Điền thông tin DB, JWT secret, AI provider mode (mock/live) hoặc Jira API token (không commit .env)
```

### 4.3. Bộ công cụ tự động hóa (DevOps Scripts)
- **Render báo cáo HTML/PDF:** `./scripts/render_reports.sh` hoặc `python3 scripts/render_reports.py` (xuất ra `reports/rendered/*.html`).
- **Tổng hợp đóng góp Git:** `python3 scripts/git_contributions.py` (đọc `members.csv` và `git log`).
- **Kiểm tra & đóng gói nộp bài:** `python3 scripts/package_submission.py --group-id Group04` (hoặc `python3 scripts/package_template1.py` đối với cấu trúc gói Template 1).

---

## 5. RÀNG BUỘC MÔN HỌC & QUY TRÌNH LÀM VIỆC

- **Định dạng tài liệu nộp:** Các báo cáo chính thức nộp trường đều được xuất bản từ Markdown/tài liệu chuẩn sang **PDF/HTML**; không nộp file tạm chứa link Google Drive trong gói zip.
- **Đóng góp cá nhân minh bạch:** Điểm số từng thành viên được truy vết xuyên suốt qua lịch sử Git commit (đúng `git_email` trong [`members.csv`](members.csv)), Pull Request có review chéo và tiến độ task trên Jira (`SCRUM-*`).
- **Khai báo AI Usage:** Mọi phiên hỗ trợ từ công cụ AI đều phải ghi đủ 7 trường quy định vào `ai-usage/template2/<ten>.md` và `ai-usage/mvp-template3/<ten>.md`, kèm đối chiếu kiểm chứng thủ công.
- **Quy tắc gói nộp bài (`GroupID.zip`):** Tối đa **20 tệp**, mỗi tệp **$\le$ 20 MB**, chạy kiểm thử sạch qua Docker Compose trước khi đóng gói bàn giao.
