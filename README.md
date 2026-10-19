# AI-POWERED HELPDESK & KNOWLEDGE BASE

[![Docs Quality Check](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/actions/workflows/docs-check.yml/badge.svg)](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/actions)
[![Course](https://img.shields.io/badge/Course-HCMUS%20Intro%20to%20Software%20Engineering-blue)](https://www.fit.hcmus.edu.vn/)
[![Group](https://img.shields.io/badge/Group-04-emerald)](members.csv)
[![Jira](https://img.shields.io/badge/Jira-SCRUM-0052CC?logo=jira)](https://your-domain.atlassian.net)

Hệ thống Hỗ trợ Kỹ thuật & Kho Tri thức Doanh nghiệp Thông minh tích hợp Trí tuệ Nhân tạo (AI-Powered Helpdesk & Knowledge Base).  
Đồ án môn học: **Nhập môn Công nghệ Phần mềm** - Khoa Công nghệ Thông tin, Trường ĐH Khoa học Tự nhiên, ĐHQG-HCM (HCMUS).

---

## 📌 1. THÀNH VIÊN NHÓM & PHÂN CÔNG (GROUP 04)

Thông tin chi tiết được quản lý tại tệp [members.csv](file:///Users/ngovietthanhbinh/Project/AI-Powered-Helpdesk-Knowledge-Base/members.csv):

| MSSV | Họ và tên | Git Username | Phân hệ phụ trách (Module) |
| :--- | :--- | :--- | :--- |
| `<mssv_A>` | `<name_A>` | `<git_username_A>` | **Module A:** User & Authentication *(Nhóm trưởng)* |
| `<mssv_B>` | `<name_B>` | `<git_username_B>` | **Module B:** Ticket & Helpdesk Workflow |
| `<mssv_C>` | `<name_C>` | `<git_username_C>` | **Module C:** Knowledge Base & Vector Search (RAG) |
| `<mssv_D>` | `<name_D>` | `<git_username_D>` | **Module D:** AI Service & Analytics Dashboard |

---

## 🌳 2. SƠ ĐỒ CẤU TRÚC THƯ MỤC (REPOSITORY STRUCTURE)

```text
/
├── README.md                      # Giới thiệu dự án, hướng dẫn cài đặt và sơ đồ repo
├── CONTRIBUTING.md                # Quy định làm việc nhóm, chuẩn Git, Jira và review chéo
├── .gitignore                     # Loại trừ file nhạy cảm, build artifacts và cache
├── .gitattributes                 # Chuẩn hóa line endings (LF) và mã hoá UTF-8
├── .editorconfig                  # Cấu hình chuẩn định dạng mã nguồn nhất quán
├── .env.example                   # Biến môi trường mẫu (chứa giá trị giả định)
├── members.csv                    # Danh sách thành viên nhóm và phân công module
├── .githooks/
│   └── commit-msg                 # Hook chặn commit thiếu mã Jira SCRUM-<số>
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md   # Mẫu PR chuẩn (Jira link, scope, DoD, reviewer)
│   ├── ISSUE_TEMPLATE/            # Mẫu task.md và bug.md
│   ├── CODEOWNERS                 # Phân chia quyền sở hữu module A-D
│   └── workflows/
│       └── docs-check.yml         # CI kiểm tra sự hiện diện của báo cáo và markdownlint
├── reports/                       # Báo cáo đồ án dạng Markdown (.md)
│   ├── 00-project-proposal.md     # Đề xuất đồ án theo chuẩn Template 0
│   ├── 01-requirements.md         # Đặc tả yêu cầu phần mềm (SRS)
│   ├── 02-use-cases.md            # Đặc tả ca sử dụng và sơ đồ Mermaid
│   ├── 03-system-design.md        # Thiết kế kiến trúc và mô hình dữ liệu
│   ├── 04-api-contract.md         # Đặc tả giao ước RESTful API
│   ├── 05-test-plan.md            # Kế hoạch kiểm thử phần mềm
│   ├── 06-test-results.md         # Bảng tổng hợp kết quả test và defect log
│   ├── 07-ai-usage.md             # Nhật ký minh bạch việc sử dụng công cụ AI
│   ├── 08-git-contributions.md    # Báo cáo đóng góp Git (tự động cập nhật qua script)
│   ├── SRS-master.md              # Bản sao nguyên vẹn file đặc tả gốc
│   ├── assets/                    # Hình ảnh, biểu đồ minh hoạ
│   └── rendered/                  # Thư mục đầu ra HTML / PDF để nộp bài
├── backend/                       # Tài liệu cấu trúc Spring Boot dự kiến (Mục 9.3 & 15.3)
├── frontend/                      # Tài liệu cấu trúc React Vite dự kiến (Mục 9.3 & 15.3)
├── infra/                         # Tài liệu hạ tầng Docker Compose dự kiến
└── scripts/                       # Bộ công cụ DevOps tự động hóa
    ├── render_reports.sh (.py)    # Render báo cáo Markdown sang HTML/PDF tự chứa
    ├── git_contributions.py       # Tổng hợp git log và ghi đè vào 08-git-contributions.md
    ├── package_submission.py      # Đóng gói GroupID.zip kiểm tra ràng buộc môn học
    └── jira/
        ├── jira_bulk_create.py    # Tự động tạo Epic và Task trên Jira Cloud API v3
        ├── tasks_template0.csv    # Dữ liệu công việc mẫu Template 0
        └── README.md              # Hướng dẫn chi tiết sử dụng kịch bản Jira
```

---

## ⚡ 3. HƯỚNG DẪN BẮT ĐẦU (QUICK START)

### 3.1. Clone Repository & Cấu hình Git Hook
```bash
# 1. Clone repository về máy cá nhân
git clone https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base.git
cd AI-Powered-Helpdesk-Knowledge-Base

# 2. Cài đặt Git hook bắt buộc (kiểm tra Jira key trong commit-msg)
git config core.hooksPath .githooks

# 3. Cấu hình thông tin tác giả khớp với members.csv
git config user.name "<git_username_cua_ban>"
git config user.email "<git_email_cua_ban>"
```

### 3.2. Cấu hình biến môi trường
```bash
cp .env.example .env
# Chỉnh sửa file .env với thông tin Jira token và cơ sở dữ liệu trên máy cá nhân
```

---

## 📝 4. BỘ CÔNG CỤ TỰ ĐỘNG HÓA (DEVOPS SCRIPTS)

### 4.1. Render báo cáo sang HTML / PDF
Chuyển đổi toàn bộ tài liệu trong `reports/*.md` sang HTML tự chứa (self-contained, nhúng CSS và hiển thị đúng tiếng Việt):
```bash
./scripts/render_reports.sh
# Hoặc chạy trực tiếp bằng python:
python3 scripts/render_reports.py
```
*Kết quả xuất ra tại:* `reports/rendered/*.html`. Bạn có thể mở bằng trình duyệt và chọn **Print -> Save as PDF** để nộp bài.

### 4.2. Tự động tổng hợp lịch sử đóng góp Git
Đọc `members.csv` và `git log`, tự động thống kê số commit, danh sách commit và cập nhật vào khu vực marker trong [reports/08-git-contributions.md](file:///Users/ngovietthanhbinh/Project/AI-Powered-Helpdesk-Knowledge-Base/reports/08-git-contributions.md):
```bash
python3 scripts/git_contributions.py
```

### 4.3. Đóng gói tệp nộp bài (`GroupID.zip`)
Tự động đóng gói, loại trừ các file rác (`.git`, `.env`, `node_modules`...) và kiểm tra 2 ràng buộc bắt buộc từ Giảng viên (Tối đa **20 file** và mỗi file **<= 20 MB**):
```bash
python3 scripts/package_submission.py --group-id Group04
```

### 4.4. Tự động tạo Task trên Jira
Chạy thử nghiệm mô phỏng:
```bash
python3 scripts/jira/jira_bulk_create.py --dry-run
```
Tạo thực tế trên Jira Cloud (sau khi đã cập nhật `.env`):
```bash
python3 scripts/jira/jira_bulk_create.py
```

---

## ⚖️ 5. RÀNG BUỘC MÔN HỌC (ACADEMIC INTEGRITY & SUBMISSION RULES)
- **Định dạng báo cáo:** Bắt buộc viết bằng Markdown (.md), render ra HTML hoặc PDF. Tuyệt đối không dùng file `.docx`.
- **Đóng góp cá nhân:** Điểm số từng thành viên được đánh giá thông qua lịch sử Git commit và tiến độ trên Jira (project key `SCRUM`). Mọi commit phải có tác giả chính xác và mã Jira hợp lệ.
- **Sử dụng AI:** Mọi sự hỗ trợ từ AI đều phải khai báo minh bạch tại [reports/07-ai-usage.md](file:///Users/ngovietthanhbinh/Project/AI-Powered-Helpdesk-Knowledge-Base/reports/07-ai-usage.md).
- **Gói nộp bài:** Nộp file nén `GroupID.zip` chứa tối đa 20 file, mỗi file <= 20 MB, không chèn link Google Drive.
