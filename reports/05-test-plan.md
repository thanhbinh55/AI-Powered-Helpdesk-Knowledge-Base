# KẾ HOẠCH KIỂM THỬ PHẦN MỀM (TEST PLAN)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Master Test Plan - AI-Powered Helpdesk & Knowledge Base
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `24120121` - `Lê Quý Phúc`: Kế hoạch kiểm thử AI Fallback/Mock Mode & Prompt Accuracy (Module A)
  - `24120503` - `Phan Gia Phúc`: Kế hoạch kiểm thử tìm kiếm Knowledge Base & Vector Accuracy (Module B)
  - `24120083` - `Nguyễn Đức Lãm`: Kế hoạch kiểm thử nghiệp vụ Ticket (Ticket Workflow Test Cases) (Module C)
  - `24120269` - `Ngô Viết Thanh Bình`: Kế hoạch kiểm thử bảo mật, phân quyền RBAC & Tích hợp E2E (Module D) *(Nhóm trưởng)*
- **Phạm vi (Scope):** Chiến lược kiểm thử, cấp độ kiểm thử (Unit Test, Integration Test, E2E), môi trường kiểm thử và tiêu chí dừng/chấp nhận.

---

## 1. CHIẾN LƯỢC KIỂM THỬ (TEST STRATEGY)
- **Unit Testing:** Kiểm thử đơn vị các Service logic bằng JUnit 5 và Mockito trên Backend; Jest / Vitest trên Frontend. Đảm bảo độ bao phủ mã nguồn (Code Coverage) tối thiểu 70%.
- **Integration Testing:** Kiểm thử tích hợp tầng Repository với PostgreSQL và REST Controllers qua `@SpringBootTest` và `Testcontainers`.
- **AI Reliability Testing:** Kiểm thử cơ chế fallback: Khi AI service ngoại tuyến hoặc quá tải, hệ thống phải tự động chuyển sang quy trình thủ công hoặc Mock service mà không gây crash ứng dụng.
- **Security & Authorization Testing:** Kiểm tra chặt chẽ các trường hợp truy cập chéo dữ liệu người dùng (IDOR) và phân quyền RBAC.

---

## 2. TIÊU CHÍ CHẤP NHẬN (ACCEPTANCE CRITERIA)
- 100% các Test Case mức độ Critical (đăng nhập, tạo ticket, tìm bài viết) phải Pass.
- Không có lỗi nghiêm trọng (Blocker/Critical bug) còn tồn đọng trước khi nộp đồ án.
- Tài liệu kiểm thử và kết quả chạy test được lưu trữ đầy đủ trong `reports/06-test-results.md`.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. IEEE Std 829-2008, Standard for Software and System Test Documentation.
2. Tài liệu đặc tả tổng thể: `reports/SRS-master.md`.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo khung kế hoạch kiểm thử | SCRUM-6 |
