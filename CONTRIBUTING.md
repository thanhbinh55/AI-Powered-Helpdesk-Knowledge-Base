# QUY TRÌNH PHÁT TRIỂN & ĐÓNG GÓP (CONTRIBUTING GUIDE)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Nhóm thực hiện:** Group 04 - HCMUS | **Jira Project Key:** `SCRUM`

Tài liệu này quy định các chuẩn mực làm việc bắt buộc cho tất cả 4 thành viên nhằm đảm bảo tính minh bạch, khả năng truy vết công việc và xét điểm đóng góp cá nhân từ giảng viên.

---

## 1. THIẾT LẬP MÔI TRƯỜNG GIT CÁ NHÂN
Trước khi thực hiện bất kỳ commit nào trên máy cá nhân, mỗi thành viên **bắt buộc** chạy 2 lệnh sau:

```bash
# 1. Kích hoạt Git hook tự động kiểm tra Jira key
git config core.hooksPath .githooks

# 2. Cấu hình đúng tên và email trùng khớp với thông tin đã đăng ký trong members.csv
git config user.name "<git_username_cua_ban>"
git config user.email "<git_email_cua_ban>"
```

---

## 2. QUY ƯỚC ĐẶT TÊN NHÁNH (BRANCHING STRATEGY)
- **TUYỆT ĐỐI KHÔNG commit trực tiếp vào nhánh `main`.**
- Nhánh `main` được bảo vệ, chỉ nhận code thông qua Pull Request đã được phê duyệt.
- Định dạng tên nhánh: `<type>/SCRUM-<số>-<mô-tả-ngắn>`
  - Các loại `<type>`: `feat`, `fix`, `docs`, `test`, `chore`
  - Ví dụ:
    - `docs/SCRUM-12-viet-muc-3-1-1`
    - `feat/SCRUM-24-xac-thuc-jwt`
    - `fix/SCRUM-35-sua-loi-tim-kiem-vector`

---

## 3. QUY ƯỚC THÔNG ĐIỆP COMMIT (COMMIT CONVENTION)
- Tuân thủ chuẩn **Conventional Commits** và **bắt buộc kết thúc bằng Jira key** `SCRUM-<số>`:
  ```text
  <type>(<scope>): <mô tả ngắn bằng tiếng Việt hoặc tiếng Anh> SCRUM-<số>
  ```
- Ví dụ hợp lệ:
  - `docs(proposal): viết mục 3.1.1 bảng chức năng SCRUM-12`
  - `feat(ticket): bổ sung API tạo ticket mới SCRUM-25`
  - `test(auth): viết unit test cho JwtTokenProvider SCRUM-18`
  - `chore(repo): cấu hình .gitignore và env template SCRUM-6`
> **Lưu ý:** Git hook `.githooks/commit-msg` sẽ tự động chặn mọi commit không chứa mã Jira dạng `SCRUM-<số>`.

---

## 4. QUY TRÌNH PULL REQUEST & REVIEW CHÉO (CODE REVIEW)
1. **Liên kết 1-1 với Jira:** Mỗi PR chỉ giải quyết duy nhất 1 task Jira và phải dẫn link Jira task đó trong nội dung PR.
2. **Reviewer khác người viết:** Người tạo PR tuyệt đối không tự approve/merge PR của mình.
3. **Quy tắc review chéo vòng tròn:**
   - **Thành viên A** (User & Auth) ➔ Review cho **Thành viên B**
   - **Thành viên B** (Ticket) ➔ Review cho **Thành viên C**
   - **Thành viên C** (Knowledge Base) ➔ Review cho **Thành viên D**
   - **Thành viên D** (AI & Analytics) ➔ Review cho **Thành viên A**
4. **Chiến lược Merge:** Sử dụng **Squash and Merge** nhưng **bắt buộc giữ mã Jira key** trong tiêu đề commit gộp cuối cùng.

---

## 5. QUY TRÌNH QUẢN LÝ TRẠNG THÁI TASK TRÊN JIRA
Mỗi thành viên có trách nhiệm cập nhật trạng thái task của mình trên Jira Board theo vòng đời:
```text
[To Do] ──(Bắt đầu làm việc)──> [In Progress] ──(Mở PR & gán Reviewer)──> [In Review] ──(PR được Merge)──> [Done]
```
- Khi bắt đầu làm: Chuyển task sang `In Progress`.
- Khi mở Pull Request: Chuyển task sang `In Review` và đính kèm link PR vào task Jira.
- Khi PR đã merge vào `main`: Chuyển task sang `Done`.

---

## 6. QUY ĐỊNH BẮT BUỘC VỀ SỬ DỤNG AI & BẢO MẬT
- **Ghi nhật ký AI:** Mọi sự hỗ trợ từ AI (ChatGPT, Claude, Gemini, Copilot...) phải được ghi nhận ngay vào bảng trong `reports/07-ai-usage.md`.
- **Bảo mật tuyệt đối:** Không commit file `.env`, API key, token cá nhân hoặc dữ liệu thật vào repository. Mọi dữ liệu mẫu chỉ lưu trong `.env.example`.
