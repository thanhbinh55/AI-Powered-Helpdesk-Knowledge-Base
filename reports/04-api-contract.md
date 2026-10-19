# BÁO CÁO ĐẶC TẢ GIAO DIỆN LẬP TRÌNH (API SPECIFICATION & CONTRACT)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** RESTful API Contract & OpenAPI Specification
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `<mssv_A>` - `<name_A>`: API Authentication & Profile (`/api/v1/auth/*`, `/api/v1/users/*`)
  - `<mssv_B>` - `<name_B>`: API Ticket Management (`/api/v1/tickets/*`)
  - `<mssv_C>` - `<name_C>`: API Knowledge Base & Semantic Search (`/api/v1/articles/*`)
  - `<mssv_D>` - `<name_D>`: API AI Suggestion & Analytics (`/api/v1/ai/*`, `/api/v1/analytics/*`)
- **Phạm vi (Scope):** Định nghĩa cấu trúc Endpoint, HTTP Method, Request Header, Request Body, Response Code và JSON Schema chuẩn cho toàn bộ hệ thống.

---

## 1. QUY ƯỚC CHUNG (GENERAL CONVENTIONS)
- **Base URL:** `/api/v1`
- **Định dạng dữ liệu:** `application/json; charset=UTF-8`
- **Xác thực:** Header `Authorization: Bearer <jwt_token>` đối với các API yêu cầu đăng nhập.
- **Mã phản hồi chuẩn:**
  - `200 OK`: Truy vấn hoặc xử lý thành công.
  - `201 Created`: Tạo mới tài nguyên thành công.
  - `400 Bad Request`: Dữ liệu đầu vào không hợp lệ.
  - `401 Unauthorized`: Chưa đăng nhập hoặc token hết hạn.
  - `403 Forbidden`: Không có quyền truy cập tài nguyên.
  - `404 Not Found`: Không tìm thấy tài nguyên.
  - `500 Internal Server Error`: Lỗi máy chủ nội bộ.

---

## 2. DANH SÁCH ENDPOINT TIÊU BIỂU
| Method | Endpoint | Mô tả | Quyền truy cập |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/v1/auth/login` | Đăng nhập và lấy JWT token | Public |
| `GET` | `/api/v1/tickets` | Danh sách ticket có phân trang | Authenticated |
| `POST` | `/api/v1/tickets` | Tạo mới một ticket hỗ trợ | End-User, Agent |
| `GET` | `/api/v1/articles/search` | Tìm kiếm bài viết (hỗ trợ ngữ nghĩa) | Public |
| `POST` | `/api/v1/ai/classify-ticket`| Phân loại ticket và gợi ý giải pháp | Agent, Admin |

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. OpenAPI Specification v3.1.0.
2. REST API Design Rulebook - Mark Masse (O'Reilly).
3. Tài liệu đặc tả tổng thể: `reports/SRS-master.md`.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo khung tài liệu giao ước API | SCRUM-6 |
