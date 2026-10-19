## 🔗 Liên kết Jira Task
- Jira Issue: [SCRUM-XXX](https://your-domain.atlassian.net/browse/SCRUM-XXX) *(Thay XXX bằng số task tương ứng)*

---

## 🎯 Phạm vi thay đổi (Scope)
<!-- Mô tả tóm tắt nội dung thay đổi và mục đích của Pull Request này -->
- [ ] Tài liệu báo cáo (Reports / Docs)
- [ ] Cấu hình hệ thống / DevOps / Scripts
- [ ] Module A: User & Auth
- [ ] Module B: Ticket & Helpdesk
- [ ] Module C: Knowledge Base & Vector Search
- [ ] Module D: AI Service & Analytics

**Chi tiết nội dung thực hiện:**
- ...

---

## 📸 Ảnh chụp màn hình / Mẫu API (Screenshots / API Payloads)
<!-- Nếu là giao diện, đính kèm ảnh chụp màn hình hoặc GIF. Nếu là API, đính kèm JSON request/response mẫu -->
```json
// Request / Response mẫu (nếu có)
```

---

## 🧪 Các bước kiểm thử (Test Steps)
<!-- Hướng dẫn cụ thể cách reviewer chạy và kiểm tra kết quả -->
1. Checkout nhánh: `git checkout <tên_nhánh>`
2. Thực hiện lệnh kiểm tra: `...`
3. Kết quả mong đợi: `...`

---

## 🗄️ Ảnh hưởng Migration / Database (Migration Impact)
- [ ] Không có thay đổi CSDL / schema.
- [ ] Có thay đổi CSDL / Liquibase / Flyway migration script (mô tả chi tiết bên dưới):
  - ...

---

## 🔒 Ảnh hưởng bảo mật (Security Impact)
- [ ] Đã kiểm tra: Không để lộ API Key, Secret Token, file `.env` hoặc thông tin nhạy cảm.
- [ ] Không có lỗ hổng bảo mật mới (SQL Injection, XSS, IDOR, v.v.).
- [ ] Đã tuân thủ phân quyền người dùng (Role-based Access Control).

---

## ✅ Checklist Definition of Done (DoD)
- [ ] Tiêu đề PR và thông điệp commit tuân thủ Conventional Commits và có chứa mã `SCRUM-<số>`.
- [ ] Nội dung tài liệu Markdown (.md) hiển thị tốt, không có lỗi định dạng (`markdownlint`).
- [ ] Đã ghi nhận việc sử dụng AI (nếu có) vào `reports/07-ai-usage.md`.
- [ ] Code/Tài liệu đã được tự kiểm tra (Self-review) trước khi mở PR.
- [ ] Đã chỉ định Reviewer khác người viết theo quy tắc xoay vòng:
  - **A** (User & Auth) ➔ review cho **B**
  - **B** (Ticket) ➔ review cho **C**
  - **C** (Knowledge Base) ➔ review cho **D**
  - **D** (AI Service) ➔ review cho **A**

---

## 👥 Người thực hiện & Người review
- **Người tạo PR:** `@<git_username_author>`
- **Reviewer được chỉ định:** `@<git_username_reviewer>` *(Bắt buộc khác người tạo PR)*
