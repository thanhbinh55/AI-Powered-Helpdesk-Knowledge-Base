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

> **Tổng số commit ghi nhận trong repository:** 36

| MSSV - Git username | Họ và tên | Vai trò / Phân hệ | Số lượng commit |
| :--- | :--- | :--- | :---: |
| **24120269 - thanhbinh55** | Ngô Viết Thanh Bình | D - Identity & Access (nhom truong) | 33 |
| **24120083 - Lamnguyen-code** | Nguyễn Đức Lãm | B - Knowledge Base | 1 |
| **24120503 - t4lf4n** | Phan Gia Phúc | C - Ticket Management | 1 |
| **24120121 - Shinkiisme** | Lê Quý Phúc | A - AI Assistance | 1 |

---

#### 👤 24120269 - thanhbinh55 (Ngô Viết Thanh Bình)
- **Phân hệ phụ trách:** D - Identity & Access (nhom truong)
- **Tổng số commit:** 33

| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |
| :--- | :--- | :--- | :--- |
| `[228fc4a6]` | 2026-10-28 | docs(ai-usage): cap nhat day du tat ca phien su dung AI cua Thanh Binh SCRUM-11 | <code>reports/07-ai-usage.md</code> |
| `[b952c039]` | 2026-10-28 | docs(reports): tai cau truc bao cao su dung AI theo quy dinh Khoa CNTT va cap nhat git log SCRUM-11 | <code>reports/07-ai-usage.md</code><br><code>reports/08-git-contributions.md</code> |
| `[9f7b9920]` | 2026-10-28 | docs(proposal): chuan hoa noi dung de xuat do an va tao ban nop submit SCRUM-11 | <code>reports/00-project-proposal.md</code><br><code>reports/submit/00-project-proposal.md</code> |
| `[ef74acb2]` | 2026-10-23 | merge: dong bo origin/main vao feat/frontend-ui-prototype SCRUM-10 | *(không có tệp thay đổi)* |
| `[d82788cd]` | 2026-10-23 | refactor(frontend): clean code, tach subcomponents modular va barrel exports SCRUM-10 | <code>frontend/src/App.tsx</code><br><code>frontend/src/components/common/index.ts</code><br><code>frontend/src/components/layout/index.ts</code><br><code>frontend/src/features/admin/index.ts</code><br>*(và 9 tệp khác...)* |
| `[71cba4b9]` | 2026-10-23 | fix(frontend): bo nut floating thua gay de lap tren header workspace SCRUM-10 | <code>frontend/src/features/ticket/TicketWorkspace.tsx</code> |
| `[c7e6f082]` | 2026-10-23 | fix(frontend): tinh gian co che mo rong hang doi kieu Linear va Notion SCRUM-10 | <code>frontend/src/App.tsx</code><br><code>frontend/src/features/ticket/TicketQueue.tsx</code><br><code>frontend/src/features/ticket/TicketWorkspace.tsx</code> |
| `[19daaa3c]` | 2026-10-23 | fix(frontend): giu thanh rail mo rong khi thu gon hang doi ticket SCRUM-10 | <code>frontend/src/features/ticket/TicketQueue.tsx</code> |
| `[e4792fdd]` | 2026-10-23 | feat(frontend): toi uu layout workspace Facebook chat va auto suggest AI SCRUM-10 | <code>.gitignore</code><br><code>frontend/src/components/layout/Navbar.tsx</code><br><code>frontend/src/features/ticket/TicketWorkspace.tsx</code><br><code>frontend/src/mock/data.ts</code> |
| `[56a791a8]` | 2026-10-23 | docs(proposal): khoi phuc bang chuc nang day du va thu gon cua Gia Phuc SCRUM-9 | <code>reports/00-project-proposal.md</code> |
| `[dac005cd]` | 2026-10-23 | feat(customer): bo sung phim tat Enter gui va Shift+Enter xuong dong cho Customer Portal SCRUM-10 | <code>frontend/src/features/customer/CustomerPortal.tsx</code><br><code>reports/assets/ui/05_customer_portal.png</code> |
| `[e4d5447f]` | 2026-10-23 | feat(frontend): sua loi chuyen tab ticket va toi uu UX chat kieu Zalo Messenger SCRUM-10 | <code>frontend/src/App.tsx</code><br><code>frontend/src/features/ticket/TicketWorkspace.tsx</code><br><code>reports/assets/ui/00_agent_open_queue.png</code><br><code>reports/assets/ui/01_agent_workspace.png</code> |
| `[b1704ff2]` | 2026-10-23 | docs(ui): cap nhat screenshots tinh chinh cho bo suu tap UI SCRUM-10 | <code>reports/assets/ui/01_agent_workspace.png</code><br><code>reports/assets/ui/02_agent_ai_copilot.png</code><br><code>reports/assets/ui/04_agent_focus_mode.png</code> |
| `[4957fc27]` | 2026-10-23 | feat(frontend): tinh chinh giao dien gon gang, bo trung lap nut AI va toi uu hop soan thao SCRUM-10 | <code>frontend/src/App.tsx</code><br><code>frontend/src/components/layout/Sidebar.tsx</code><br><code>frontend/src/features/ticket/TicketQueue.tsx</code><br><code>frontend/src/features/ticket/TicketWorkspace.tsx</code> |
| `[de9a6ecd]` | 2026-10-22 | docs(ui): tao bo suu tap UI showcase gallery gom 11 man hinh cho nhom xem xet SCRUM-10 | <code>reports/UI_SHOWCASE.html</code><br><code>reports/UI_SHOWCASE.md</code><br><code>reports/assets/ui/01_agent_workspace.png</code><br><code>reports/assets/ui/02_agent_ai_copilot.png</code><br>*(và 9 tệp khác...)* |
| `[a9f542d2]` | 2026-10-22 | feat(frontend): toi uu hoa workspace rong rai, sidebar va ticket queue thu phong va AI Copilot goc duoi SCRUM-10 | <code>frontend/src/App.tsx</code><br><code>frontend/src/components/layout/Navbar.tsx</code><br><code>frontend/src/components/layout/Sidebar.tsx</code><br><code>frontend/src/features/ticket/TicketQueue.tsx</code><br>*(và 1 tệp khác...)* |
| `[f127d244]` | 2026-10-22 | feat(frontend): khoi tao prototype giao dien 3 cot HelpDesk voi React va Tailwind CSS SCRUM-10 | <code>.gitignore</code><br><code>frontend/index.html</code><br><code>frontend/package-lock.json</code><br><code>frontend/package.json</code><br>*(và 19 tệp khác...)* |
| `[77a88a24]` | 2026-10-22 | docs(members): dong bo phan cong module B cho Lam va C cho Gia Phuc SCRUM-11 | <code>.github/CODEOWNERS</code><br><code>.gitignore</code><br><code>README.md</code><br><code>TEAM_GUIDE_TEMPLATE0.md</code><br>*(và 9 tệp khác...)* |
| `[f5da77da]` | 2026-10-22 | docs(proposal): loai bo cac ghi chu noi bo va tham chieu SRS hoan thien proposal 1.0.0 SCRUM-11 | <code>reports/00-project-proposal.md</code> |
| `[61fc89f1]` | 2026-10-22 | Merge pull request #4 from thanhbinh55/docs/SCRUM-11-nhan-su-chi-phi | *(không có tệp thay đổi)* |
| `[e571f12b]` | 2026-10-22 | docs(proposal): hoan thien muc 5 ke hoach nhan su va chi phi SCRUM-11 | <code>reports/00-project-proposal.md</code><br><code>reports/07-ai-usage.md</code> |
| `[09955a82]` | 2026-10-22 | Merge branch 'docs/SCRUM-10-kien-truc-ke-hoach' into main SCRUM-10 | *(không có tệp thay đổi)* |
| `[f57f60e1]` | 2026-10-22 | Merge branch 'docs/SCRUM-9-bang-chuc-nang' into main SCRUM-9 | *(không có tệp thay đổi)* |
| `[a89f1e22]` | 2026-10-22 | docs(proposal): chuẩn hóa mục lục theo template của Thầy và tích hợp nội dung SCRUM-7 | <code>TEAM_GUIDE_TEMPLATE0.md</code><br><code>reports/00-project-proposal.md</code> |
| `[72212cb5]` | 2026-10-19 | docs(guide): bổ sung tài liệu hướng dẫn quy trình làm việc Template 0 cho thành viên SCRUM-7 | <code>TEAM_GUIDE_TEMPLATE0.md</code> |
| `[d65cc260]` | 2026-10-20 | Merge pull request #1 from thanhbinh55/docs/SCRUM-8-viet-muc-1-2-3.2 | *(không có tệp thay đổi)* |
| `[407a5930]` | 2026-10-19 | docs(members): cập nhật thông tin thành viên, phân công module và deadline Template 0 SCRUM-7 | <code>.github/CODEOWNERS</code><br><code>README.md</code><br><code>members.csv</code><br><code>reports/00-project-proposal.md</code><br>*(và 10 tệp khác...)* |
| `[334f5c28]` | 2026-10-19 | docs(guide): hoàn thiện README và CONTRIBUTING hướng dẫn quy trình SCRUM-6 | <code>CONTRIBUTING.md</code><br><code>README.md</code><br><code>reports/08-git-contributions.md</code><br><code>scripts/git_contributions.py</code> |
| `[4e2cf4b8]` | 2026-10-19 | feat(jira): bổ sung kịch bản tạo task tự động và kịch bản tasks template 0 SCRUM-6 | <code>scripts/jira/README.md</code><br><code>scripts/jira/jira_bulk_create.py</code><br><code>scripts/jira/tasks_template0.csv</code> |
| `[c4496214]` | 2026-10-19 | feat(scripts): bổ sung công cụ render báo cáo, đóng gói và tổng hợp đóng góp SCRUM-6 | <code>scripts/git_contributions.py</code><br><code>scripts/package_submission.py</code><br><code>scripts/render_reports.py</code><br><code>scripts/render_reports.sh</code> |
| `[f7fefb4d]` | 2026-10-19 | docs(reports): thiết lập khung tài liệu báo cáo và cấu trúc dự kiến các phân hệ SCRUM-6 | <code>backend/.gitkeep</code><br><code>backend/README.md</code><br><code>frontend/.gitkeep</code><br><code>frontend/README.md</code><br>*(và 14 tệp khác...)* |
| `[09ae70cf]` | 2026-10-19 | ci(githooks): thiết lập commit-msg hook và github templates SCRUM-6 | <code>.githooks/commit-msg</code><br><code>.github/CODEOWNERS</code><br><code>.github/ISSUE_TEMPLATE/bug.md</code><br><code>.github/ISSUE_TEMPLATE/task.md</code><br>*(và 2 tệp khác...)* |
| `[2da10f72]` | 2026-10-19 | chore(repo): khởi tạo cấu trúc cơ bản và cấu hình môi trường SCRUM-6 | <code>.editorconfig</code><br><code>.env.example</code><br><code>.gitattributes</code><br><code>.gitignore</code><br>*(và 1 tệp khác...)* |

#### 👤 24120083 - Lamnguyen-code (Nguyễn Đức Lãm)
- **Phân hệ phụ trách:** B - Knowledge Base
- **Tổng số commit:** 1

| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |
| :--- | :--- | :--- | :--- |
| `[5405de76]` | 2026-10-22 | docs(proposal): bo sung so do kien truc va ke hoach sprint SCRUM-10 | <code>reports/00-project-proposal.md</code><br><code>reports/07-ai-usage.md</code> |

#### 👤 24120503 - t4lf4n (Phan Gia Phúc)
- **Phân hệ phụ trách:** C - Ticket Management
- **Tổng số commit:** 1

| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |
| :--- | :--- | :--- | :--- |
| `[0bbf775e]` | 2026-10-22 | docs(proposal): cap nhat bang chuc nang functional matrix SCRUM-9 | <code>reports/00-project-proposal.md</code><br><code>reports/07-ai-usage.md</code> |

#### 👤 24120121 - Shinkiisme (Lê Quý Phúc)
- **Phân hệ phụ trách:** A - AI Assistance
- **Tổng số commit:** 1

| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |
| :--- | :--- | :--- | :--- |
| `[520a0f44]` | 2026-10-19 | docs(proposal): hoan thien noi dung muc 1, 2 va 3.2 SCRUM-8 | <code>reports/00-project-proposal.md</code><br><code>reports/07-ai-usage.md</code> |

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
