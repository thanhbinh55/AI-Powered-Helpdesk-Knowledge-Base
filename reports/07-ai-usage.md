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
  - `24120269` - `Ngô Viết Thanh Bình`: Khởi tạo và giám sát quy trình tuân thủ AI của nhóm (Nhóm trưởng)
  - Toàn bộ thành viên nhóm: Ghi nhật ký minh bạch mọi hoạt động hỗ trợ từ AI
- **Phạm vi (Scope):** Minh bạch toàn bộ việc sử dụng các công cụ AI (LLMs, Trợ lý lập trình, Tạo sinh mã nguồn/tài liệu) trong suốt vòng đời dự án theo yêu cầu bắt buộc của giảng viên.

---

## 1. NGUYÊN TẮC SỬ DỤNG AI CỦA NHÓM

1. **Minh bạch tuyệt đối:** Bất kỳ đoạn văn bản, mã nguồn, kịch bản hoặc thiết kế nào có sự trợ giúp của AI đều phải được ghi lại ngay trong ngày làm việc.
2. **Trách nhiệm thuộc về con người:** Thành viên đưa mã nguồn/tài liệu do AI tạo sinh vào repository phải tự mình kiểm tra tính đúng đắn, hiểu rõ bản chất và chịu hoàn toàn trách nhiệm trước giảng viên.
3. **Bảo mật thông tin:** Không nhập khóa API thật, mật khẩu, dữ liệu cá nhân nhạy cảm vào các dịch vụ AI công cộng.

---

## 2. NHẬT KÝ CHI TIẾT SỬ DỤNG AI (AI USAGE LOG)

| Ngày       | Công cụ / Model             | Mục đích                                                           | Input tóm tắt                                                         | Output được dùng                                                               | Cách kiểm tra                                                                            | Phần bị sửa / bỏ                                                                   | Người chịu trách nhiệm                |
| :--------- | :-------------------------- | :----------------------------------------------------------------- | :-------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- | :------------------------------------ |
| 2026-10-19 | Google Gemini (Antigravity) | Dựng khung repository, kịch bản CI, githooks và các tài liệu chuẩn | Yêu cầu cấu trúc đồ án NMCNPM Group 4 HCMUS, các ràng buộc giảng viên | Bộ khung thư mục, git hook kiểm tra Jira key, scripts tự động hóa và templates | Chạy thử dry-run, kiểm tra shell script, verify format markdownlint và kiểm tra git hook | Tinh chỉnh thông báo lỗi tiếng Việt, bổ sung xử lý an toàn đường dẫn và regex Jira | `Ngô Viết Thanh Bình` (DevOps / Lead) |
| 2026-10-19 | ChatGPT (GPT-6)             | Hỗ trợ tạo bản nháp Project Proposal cho SCRUM-8                   | Template 0, hướng dẫn nhóm, SRS và phần được phân công                | Bản nháp tham khảo cho trang bìa, Mục 1, Mục 2 và Mục 3.2                      | Cần tự đối chiếu mẫu, SRS và kiểm tra nội dung trước khi đưa vào bản nộp                 | Chưa xác nhận các phần chỉnh sửa hoặc loại bỏ                                      | `Lê Quý Phúc` (SCRUM-8)               |
|2026-10-22 | ChatGPT(GPT-6.1 Sol)  | Hỗ trợ tạo bản nháp Project Proposal cho SCRUM-10  | - chào bạn, tôi đang cần viết phần 3.1.2, kiến trúc tổng thể phần mềm, với nguồn tài liệu được lấy ở Trình bày kiến trúc tổng thể đáp ứng danh sách chức năng ở mục 3.1.1 (sơ đồ kiến trúc + giải thích các thành phần và luồng vận hành). Tham khảo Mục 9.1, 9.3, 9.4, 12.2 và Phụ lục  trong reports/SRS-master.md, hãy dùng skill [$humanizer:humanizer](/home/lam/.codex/skills/humanizer/SKILL.md) viết cho tôi phần này một cách tự nhiên nhất, cho tôi một cell .md  để tôi chèn vào file của mình, không tự ý thay đổi bất kì file nào <br> - ok, tiếp tục với phần Kế hoạch phát triển Trình bày cụ thể kế hoạch phát triển phần mềm qua 5 giai đoạn cùng thành phẩm cụ thể của từng giai đoạn. Tham khảo Mục 14, 15, 17, 21 và Phụ lục G trong reports/SRS-master.md (lấy chuẩn ngày tháng theo phụ lục G) | Bản nháp cho phần 3.1.2 và phần 4 | Cần tự đối chiếu, chỉnh sửa trước khi đưa vào bản nộp | Chưa xác nhận các phần chỉnh sửa hoặc loại bỏ | `Nguyễn Đức Lãm`(SCRUM-10)



_(Mọi thành viên tiếp tục bổ sung dòng mới vào bảng trên ngay khi phát sinh việc sử dụng AI trong các Sprint tiếp theo)_

---

## TÀI LIỆU THAM KHẢO (REFERENCES)

1. Quy định về liêm chính học thuật và sử dụng AI có trách nhiệm - HCMUS.
2. ACM Code of Ethics and Professional Conduct.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)

| Phiên bản | Ngày       | Người sửa       | Nội dung thay đổi                                                               | Mã Task Jira |
| :-------- | :--------- | :-------------- | :------------------------------------------------------------------------------ | :----------- |
| `1.0.0`   | 2026-10-19 | DevOps Engineer | Khởi tạo bảng nhật ký theo dõi sử dụng AI                                       | SCRUM-6      |
| `1.0.1`   | 2026-10-19 | Lê Quý Phúc     | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ soạn bản nháp Project Proposal (SCRUM-8) | SCRUM-8      |
| `1.0.2`   | 2026-10-22 | Nguyễn Đức Lãm  | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ soạn bản nháp Project Proposal (SCRUM-10) | SCRUM-10
