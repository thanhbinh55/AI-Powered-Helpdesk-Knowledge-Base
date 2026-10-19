# BÁO CÁO SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI USAGE REPORT)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** AI Usage Transparency & Accountability Report
- **Phiên bản (Version):** 1.0.0
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `<mssv_A>` - `<name_A>`: Khởi tạo và giám sát quy trình tuân thủ AI của nhóm
  - Toàn bộ thành viên nhóm: Ghi nhật ký minh bạch mọi hoạt động hỗ trợ từ AI
- **Phạm vi (Scope):** Minh bạch toàn bộ việc sử dụng các công cụ AI (LLMs, Trợ lý lập trình, Tạo sinh mã nguồn/tài liệu) trong suốt vòng đời dự án theo yêu cầu bắt buộc của giảng viên.

---

## 1. NGUYÊN TẮC SỬ DỤNG AI CỦA NHÓM
1. **Minh bạch tuyệt đối:** Bất kỳ đoạn văn bản, mã nguồn, kịch bản hoặc thiết kế nào có sự trợ giúp của AI đều phải được ghi lại ngay trong ngày làm việc.
2. **Trách nhiệm thuộc về con người:** Thành viên đưa mã nguồn/tài liệu do AI tạo sinh vào repository phải tự mình kiểm tra tính đúng đắn, hiểu rõ bản chất và chịu hoàn toàn trách nhiệm trước giảng viên.
3. **Bảo mật thông tin:** Không nhập khóa API thật, mật khẩu, dữ liệu cá nhân nhạy cảm vào các dịch vụ AI công cộng.

---

## 2. NHẬT KÝ CHI TIẾT SỬ DỤNG AI (AI USAGE LOG)

| Ngày | Công cụ / Model | Mục đích | Input tóm tắt | Output được dùng | Cách kiểm tra | Phần bị sửa / bỏ | Người chịu trách nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-10-19 | Google Gemini (Antigravity) | Dựng khung repository, kịch bản CI, githooks và các tài liệu chuẩn | Yêu cầu cấu trúc đồ án NMCNPM Group 4 HCMUS, các ràng buộc giảng viên | Bộ khung thư mục, git hook kiểm tra Jira key, scripts tự động hóa và templates | Chạy thử dry-run, kiểm tra shell script, verify format markdownlint và kiểm tra git hook | Tinh chỉnh thông báo lỗi tiếng Việt, bổ sung xử lý an toàn đường dẫn và regex Jira | `<name_A>` (DevOps / Lead) |

*(Mọi thành viên tiếp tục bổ sung dòng mới vào bảng trên ngay khi phát sinh việc sử dụng AI trong các Sprint tiếp theo)*

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. Quy định về liêm chính học thuật và sử dụng AI có trách nhiệm - HCMUS.
2. ACM Code of Ethics and Professional Conduct.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `1.0.0` | 2026-10-19 | DevOps Engineer | Khởi tạo bảng nhật ký theo dõi sử dụng AI | SCRUM-6 |
