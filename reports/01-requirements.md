# BÁO CÁO ĐẶC TẢ YÊU CẦU PHẦN MỀM (SOFTWARE REQUIREMENTS SPECIFICATION)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Software Requirements Specification (SRS)
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `24120121` - `Lê Quý Phúc`: Yêu cầu phân hệ Trợ lý AI & Báo cáo phân tích (Module A)
  - `24120083` - `Nguyễn Đức Lãm`: Yêu cầu phân hệ Kho tri thức (Knowledge Base) & Vector Search (Module B)
  - `24120503` - `Phan Gia Phúc`: Yêu cầu phân hệ Quản lý Ticket & Luồng xử lý sự cố (Module C)
  - `24120269` - `Ngô Viết Thanh Bình`: Yêu cầu phân hệ Quản trị & Xác thực người dùng (Module D) *(Nhóm trưởng)*
- **Phạm vi (Scope):** Chi tiết hóa các yêu cầu chức năng, phi chức năng, ràng buộc kỹ thuật và tiêu chuẩn nghiệm thu của toàn bộ hệ thống.

---

## 1. YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)
### 1.1. Phân hệ A: Trợ lý AI & Báo cáo phân tích (Module A)
- **FR-AI-01:** Tự động gợi ý bài viết tri thức liên quan khi người dùng nhập nội dung ticket.
- **FR-AI-02:** Tự động phân loại mức độ ưu tiên và phòng ban xử lý bằng mô hình ngôn ngữ lớn (LLM).
- **FR-AI-03:** Thống kê SLA, thời gian phản hồi trung bình và tỷ lệ giải quyết ticket.

### 1.2. Phân hệ B: Kho tri thức (Knowledge Base) (Module B)
- **FR-KB-01:** Quản lý bài viết hướng dẫn (FAQ / Articles) theo cây chuyên mục.
- **FR-KB-02:** Tìm kiếm toàn văn và tìm kiếm ngữ nghĩa (Semantic Vector Search).
- **FR-KB-03:** Đánh giá độ hữu ích của bài viết (Thích / Không thích / Bình chọn).

### 1.3. Phân hệ C: Quản lý Ticket & Helpdesk (Module C)
- **FR-TCK-01:** Tạo mới ticket với phân loại danh mục, mức độ ưu tiên và đính kèm tệp.
- **FR-TCK-02:** Quy trình chuyển trạng thái ticket: *Open -> In Progress -> Resolved -> Closed*.
- **FR-TCK-03:** Bình luận, trao đổi giữa người dùng và nhân viên hỗ trợ.

### 1.4. Phân hệ D: Quản trị & Xác thực người dùng (Module D)
- **FR-AUTH-01:** Đăng ký, đăng nhập hệ thống và xác thực qua JWT.
- **FR-AUTH-02:** Phân quyền theo vai trò (Admin, Support Agent, End-user).
- **FR-AUTH-03:** Quản lý thông tin hồ sơ và nhật ký đăng nhập.

---

## 2. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS)
- **NFR-SEC-01:** Mã hóa mật khẩu người dùng bằng thuật toán an toàn (BCrypt).
- **NFR-PERF-01:** Thời gian phản hồi của các API tra cứu không vượt quá 500ms dưới tải 100 concurrent requests.
- **NFR-AVAIL-01:** Hệ thống hỗ trợ chế độ Mock AI khi không có kết nối Internet hoặc chưa cấu hình API Key.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. IEEE Std 830-1998, Recommended Practice for Software Requirements Specifications.
2. Tài liệu đặc tả tổng thể: `reports/SRS-master.md`.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo khung tài liệu yêu cầu | SCRUM-6 |
