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
| 2026-10-22 | ChatGPT (GPT-6)             | Hỗ trợ review Phụ lục D                                            | Nội dung từ `reports/SRS-master.md` bao gồm Phụ lục D, Mục 3.3, 4, 5, 7, 8 | Các tham chiếu bổ sung                                                         | Đối chiếu các tham chiếu với nội dung của các cột Nhu cầu/Yêu cầu                        | Làm rõ một số nội dung của cột Nhu cầu; bổ sung các tham chiếu hiện tại có liên quan; gợi ý bổ sung thêm các tham chiếu chưa có để làm rõ nội dung của 1 số chức năng | `Phan Gia Phúc` (SCRUM-9)              |
| 2026-10-22 | ChatGPT (GPT-6.1 Sol)       | Hỗ trợ tạo bản nháp Project Proposal cho SCRUM-10                  | Tham khảo Mục 9.1, 9.3, 9.4, 12.2 (Kiến trúc) và Mục 14, 15, 17, 21, Phụ lục G | Bản nháp cho phần 3.1.2 và phần 4                                              | Đối chiếu với Phụ lục E và Phụ lục G trước khi đưa vào bản nộp                           | Tinh chỉnh thuật ngữ, chuẩn hóa mốc ngày tháng theo lịch tuần                          | `Nguyễn Đức Lãm` (SCRUM-10)            |
| 2026-10-22 | Google Gemini (Antigravity) | Hỗ trợ chuẩn hóa bảng phân công nhân sự và dự toán ngân sách cho SCRUM-11 | **Các prompt trọng tâm từ người dùng:**<br>1. *"phần kế hoạch nhân sự & chi phí có trong SRS trước đó là dựa vào đâu mà soạn nên"*<br>2. *"hiện tại ở giai đoạn sau khi hoàn thành template, bước vào giai đoạn triển khai tiếp theo thì sẽ có những module công việc nào, hiện tại đang phân như nào và có mốc thời gian cụ thể không"*<br>3. *"Theo quy định bắt buộc của môn học, dự án không phân chia theo kiểu tách biệt... mà tất cả 4 thành viên đều tham gia đầy đủ 5 công đoạn phát triển phần mềm (SDLC)... không nên có những phần như thế này, tài liệu proposal trình bày như một bản nộp chuyên nghiệp, các phần câu từ như vậy không nên được sử dụng. Phân công công việc: Lãm làm Knowledge Base, Phan Gia Phúc làm Ticket Management, Lê Quý Phúc làm AI Assistance, tôi là Bình làm Identity & Access..."*<br>4. *"ở bảng cấu trúc nhân sự, không cần MSSV, Không ghi Module A hay B hay C,D. Thay Trách nhiệm chuyên môn xuyên suốt SDLC thành Mô tả công việc. Và có thể liệt kê chi tiết hơn để đảm bảo đủ đúng các công việc thực hiện... thêm ghi chú: Các chi phí được tính toán dựa trên quy mô nhóm nhỏ... và ngoài ra với các chi phí, nếu tìm thấy tài liệu tham khảo chính thức từ các trang web chính thống cho các loại chi phí thì càng tốt"*<br>5. *"DỰA TRÊN NGUỒN THÔNG TIN NÀY, CHỈNH SỬA LẠI CHÍNH XÁC CHO TÔI PHẦN CHI PHÍ CHO ĐÚNG THỰC TẾ CÓ KIỂM CHỨNG NGUỒN: đối chiếu hồ sơ Group 04 kiến trúc Modular Monolith React + Spring Boot + Postgres/pgvector chạy 1 VPS DigitalOcean 48 USD/tháng, Namecheap domain, OpenAI GPT-4o-mini/embedding, Cloudflare SSL 0 đồng, phân định rõ dự toán kinh tế 48,82 triệu và thực chi tiền mặt..."*<br>6. *"những con số lẻ thì làm tròn lên một xíu ví dụ 290 thì lên 300"*<br>7. *"Dựa trên nội dung bảng giá chính thức... sửa lại phép tính chi phí LLM: GPT-6 Luna 0,10 USD input / 0,50 USD output -> 1,95 USD = 49.725 VNĐ, làm tròn dự toán 60.000 VNĐ; Embedding text-embedding-3-small 0,30 USD = 7.650 VNĐ, làm tròn 10.000 VNĐ... chỉnh lại hai mục 4, 5 cho phù hợp"*<br>8. *"Với các số lẻ hãy làm tròn nhẹ lên và thêm dấu ~ trước"* | Bảng ma trận nhân sự 5.1 và bảng chi phí dự toán 5.2 | Đối chiếu trực tiếp với Phụ lục H & I của SRS-master.md và chuẩn hóa thuật ngữ chuyên nghiệp | Loại bỏ các diễn đạt mang tính học đường, gán trách nhiệm kỹ thuật cụ thể cho từng module, tích hợp nguồn tham chiếu chính thức, tính toán kiểm chứng nguồn công khai, làm tròn số lẻ thực tế, cập nhật định mức API OpenAI và thêm tiền tố ~ | `Ngô Viết Thanh Bình` (SCRUM-11) |

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
| `1.0.2`   | 2026-10-22 | Phan Gia Phúc   | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ rà soát Phụ lục D (SCRUM-9)              | SCRUM-9      |
| `1.0.3`   | 2026-10-22 | Nguyễn Đức Lãm  | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ soạn bản nháp Project Proposal (SCRUM-10) | SCRUM-10     |
| `1.0.4`   | 2026-10-22 | Ngô Viết Thanh Bình | Bổ sung nhật ký sử dụng AI hỗ trợ soạn Mục 5 Kế hoạch nhân sự và chi phí (SCRUM-11) | SCRUM-11     |
