# BÁO CÁO ĐÓNG GÓP GIT (GIT COMMIT HISTORY REPORT)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Git Commit History & Individual Contributions Report
- **Phiên bản (Version):** 1.0.0
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - Tự động sinh từ Git commit log dựa trên danh sách thành viên trong `members.csv`
- **Phạm vi (Scope):** Thống kê minh bạch toàn bộ commit, số lượng đóng góp, ngày commit và danh sách file thay đổi của từng thành viên phục vụ giảng viên đánh giá điểm quá trình.

---

> [!NOTE]
> Khu vực bên dưới được tự động tạo và cập nhật bởi kịch bản `python3 scripts/git_contributions.py`.
> Vui lòng **KHÔNG CHỈNH SỬA THỦ CÔNG** khu vực giữa hai thẻ đánh dấu `<!-- GENERATED:START -->
### 📊 Tổng Hợp Lịch Sử Commit Theo Thành Viên (Tự Động Sinh)

> **Tổng số commit ghi nhận trong repository:** 6

| MSSV - Git username | Họ và tên | Vai trò / Phân hệ | Số lượng commit |
| :--- | :--- | :--- | :---: |
| **<MSSV_A> - thanhbinh55** | <Ho ten A> | A - Identity & Access (nhom truong) | 6 |
| **<MSSV_B> - <git_username_B>** | <Ho ten B> | B - Ticket Management | 0 |
| **<MSSV_C> - <git_username_C>** | <Ho ten C> | C - Knowledge Base | 0 |
| **<MSSV_D> - Shinkiisme** | <Ho ten D> | D - AI Assistance | 0 |

---

#### 👤 <MSSV_A> - thanhbinh55 (<Ho ten A>)
- **Phân hệ phụ trách:** A - Identity & Access (nhom truong)
- **Tổng số commit:** 6

| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |
| :--- | :--- | :--- | :--- |
| `[2120b1f8]` | 2026-10-19 | docs(guide): hoàn thiện README và CONTRIBUTING hướng dẫn quy trình SCRUM-6 | <code>CONTRIBUTING.md</code><br><code>README.md</code><br><code>reports/08-git-contributions.md</code><br><code>scripts/git_contributions.py</code> |
| `[4e2cf4b8]` | 2026-10-19 | feat(jira): bổ sung kịch bản tạo task tự động và kịch bản tasks template 0 SCRUM-6 | <code>scripts/jira/README.md</code><br><code>scripts/jira/jira_bulk_create.py</code><br><code>scripts/jira/tasks_template0.csv</code> |
| `[c4496214]` | 2026-10-19 | feat(scripts): bổ sung công cụ render báo cáo, đóng gói và tổng hợp đóng góp SCRUM-6 | <code>scripts/git_contributions.py</code><br><code>scripts/package_submission.py</code><br><code>scripts/render_reports.py</code><br><code>scripts/render_reports.sh</code> |
| `[f7fefb4d]` | 2026-10-19 | docs(reports): thiết lập khung tài liệu báo cáo và cấu trúc dự kiến các phân hệ SCRUM-6 | <code>backend/.gitkeep</code><br><code>backend/README.md</code><br><code>frontend/.gitkeep</code><br><code>frontend/README.md</code><br>*(và 14 tệp khác...)* |
| `[09ae70cf]` | 2026-10-19 | ci(githooks): thiết lập commit-msg hook và github templates SCRUM-6 | <code>.githooks/commit-msg</code><br><code>.github/CODEOWNERS</code><br><code>.github/ISSUE_TEMPLATE/bug.md</code><br><code>.github/ISSUE_TEMPLATE/task.md</code><br>*(và 2 tệp khác...)* |
| `[2da10f72]` | 2026-10-19 | chore(repo): khởi tạo cấu trúc cơ bản và cấu hình môi trường SCRUM-6 | <code>.editorconfig</code><br><code>.env.example</code><br><code>.gitattributes</code><br><code>.gitignore</code><br>*(và 1 tệp khác...)* |

#### 👤 <MSSV_B> - <git_username_B> (<Ho ten B>)
- **Phân hệ phụ trách:** B - Ticket Management
- **Tổng số commit:** 0
*(Chưa có commit nào được ghi nhận với thông tin tác giả này)*

#### 👤 <MSSV_C> - <git_username_C> (<Ho ten C>)
- **Phân hệ phụ trách:** C - Knowledge Base
- **Tổng số commit:** 0
*(Chưa có commit nào được ghi nhận với thông tin tác giả này)*

#### 👤 <MSSV_D> - Shinkiisme (<Ho ten D>)
- **Phân hệ phụ trách:** D - AI Assistance
- **Tổng số commit:** 0
*(Chưa có commit nào được ghi nhận với thông tin tác giả này)*

<!-- GENERATED:END -->`.

<!-- GENERATED:START -->
### 📊 Tổng hợp đóng góp theo thành viên (Được tạo tự động)
*Chưa có dữ liệu commit được sinh. Hãy chạy kịch bản sau để cập nhật:*
```bash
python3 scripts/git_contributions.py
```
<!-- GENERATED:END -->

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. Git Commit History của repository: `AI-Powered-Helpdesk-Knowledge-Base`.
2. Danh sách thành viên đăng ký: `members.csv`.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `1.0.0` | 2026-10-19 | DevOps Engineer | Thiết lập khung báo cáo và marker tự động sinh | SCRUM-6 |
