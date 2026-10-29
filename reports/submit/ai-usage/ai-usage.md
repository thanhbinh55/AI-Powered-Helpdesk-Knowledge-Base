# BÁO CÁO SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI USAGE REPORT)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm (CS10014) — Trường ĐHKHTN, ĐHQG-HCM  
> **Kho lưu trữ (Repository):** https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base  
> **Chuẩn quy định:** Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS  

---

## 1. NGUYÊN TẮC CỐT LÕI & TUYÊN BỐ SỬ DỤNG AI

Căn cứ theo văn bản **"Quy định về việc sử dụng AI"** của Khoa CNTT, Trường Đại học Khoa học Tự Nhiên TP.HCM:

### 1.1. Tuyên bố bắt buộc của nhóm (Theo Mục 5 - Yêu cầu bắt buộc)
> **Tuyên bố sử dụng công cụ AI (Mục 5.B):**  
> *"Trong suốt quá trình thực hiện đồ án, nhóm có sử dụng các công cụ Trí tuệ nhân tạo (bao gồm ChatGPT của OpenAI, Google Gemini / Antigravity IDE của Google, GitHub Copilot) với mục đích hỗ trợ tra cứu kiến thức, gợi ý cấu trúc báo cáo, rà soát ngôn ngữ, và gợi ý khung mã nguồn. Tất cả các nội dung do AI đề xuất đều được các thành viên nhóm hiểu rõ bản chất, đối chiếu với tài liệu học thuật chính thống, chỉnh sửa bổ sung bằng năng lực cá nhân, chạy thử nghiệm test case thực tế và chịu hoàn toàn trách nhiệm về tính đúng đắn trước Giảng viên."*

### 1.2. Bốn nguyên tắc cốt lõi được nhóm cam kết thực hiện
1. **Minh bạch:** Ghi chép đầy đủ tên công cụ, phiên bản, thời gian truy cập, câu prompt, mục đích, kết quả AI sinh và cách sinh viên tự hiệu chỉnh/kiểm chứng.
2. **Hiểu rõ nội dung:** Mọi thành viên phải hiểu sâu sắc và có khả năng giải thích, bảo vệ toàn bộ mã nguồn và báo cáo nộp bài trong buổi vấn đáp.
3. **Không sao chép máy móc:** Tuyệt đối không dán nguyên văn mã nguồn hoặc văn bản do AI sinh ra mà không qua thẩm định, chỉnh sửa chuyên môn.
4. **Đạo đức học thuật & Bảo mật:** Kiểm chứng chéo mọi dữ liệu với giáo trình chuẩn (Russell & Norvig, giáo trình CNPM); không đưa khóa bí mật (API keys, credentials) vào các dịch vụ AI công cộng.

---

## 2. BẢNG TỔNG HỢP NHẬT KÝ SỬ DỤNG AI (SUMMARY LOG MATRIX)

Bảng dưới đây tổng hợp toàn bộ các phiên tương tác với AI trong quá trình triển khai dự án từ giai đoạn khởi tạo đến hiện tại.

| ID | Thời gian | Thành viên (MSSV) | Công cụ & Nền tảng | Hạng mục / Vị trí áp dụng | Nội dung AI tạo & Tự kiểm chứng | Minh chứng |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: |
| **#01** | 09h00 - 17h30<br>19/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Khung Repository, kịch bản CI, Git hooks & Script đóng gói (SCRUM-6) | AI gợi ý cấu trúc thư mục, script git hook & đóng gói; sinh viên tự kiểm tra lại regex Jira key, xử lý UTF-8 và chạy dry-run | [Chi tiết #01](#entry-01) |
| **#02** | 18h30<br>19/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Hướng dẫn làm việc nhóm & Quy trình Template 0 (SCRUM-7) | AI đề xuất cấu trúc tài liệu hướng dẫn nhóm; sinh viên đối chiếu quy định môn học, thiết lập quy chuẩn git branch/commit và deadline nội bộ | [Chi tiết #02](#entry-02) |
| **#03** | 14h30<br>19/10/2026 | Lê Quý Phúc<br>`24120121` | ChatGPT (GPT-6)<br>OpenAI via chat.openai.com | Bản nháp Project Proposal Mục 1, 2, 3.2 (SCRUM-8) | AI sinh bản nháp tham khảo cho trang bìa, Mục 1, 2 và 3.2 từ tài liệu SRS và hướng dẫn nhóm; sinh viên tự đối chiếu mẫu và kiểm tra nội dung trước khi đưa vào bản nộp | [Chi tiết #03](#entry-03) |
| **#04** | 10h15<br>22/10/2026 | Phan Gia Phúc<br>`24120503` | ChatGPT (GPT-6)<br>OpenAI via chat.openai.com | Rà soát Phụ lục D & Ma trận chức năng (SCRUM-9) | AI đề xuất các tham chiếu bổ sung từ SRS-master.md; sinh viên đối chiếu với cột Nhu cầu/Yêu cầu, làm rõ nội dung và bổ sung tham chiếu | [Chi tiết #04](#entry-04) |
| **#05** | 09h30<br>22/10/2026 | Nguyễn Đức Lãm<br>`24120083` | ChatGPT (GPT-6.1 Sol)<br>OpenAI via chat.openai.com | Bản nháp Kiến trúc 3.1.2 & Kế hoạch phát triển Mục 4 (SCRUM-10) | AI sinh bản nháp từ tài liệu kiến trúc và Phụ lục G; sinh viên đối chiếu Phụ lục E & G, tinh chỉnh thuật ngữ và chuẩn hóa mốc ngày tháng | [Chi tiết #05](#entry-05) |
| **#06** | 00h30<br>22/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Chuẩn hóa mục lục Proposal khớp mẫu Word của Giảng viên & Hợp nhất nội dung nhóm (SCRUM-7 & SCRUM-11) | AI rà soát mục lục đối sánh template Word của Thầy; sinh viên tự tay hợp nhất nội dung từ nhánh các thành viên, sửa xung đột định dạng | [Chi tiết #06](#entry-06) |
| **#07** | 15h30<br>22/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Chuẩn hóa Ma trận nhân sự 5.1 & Dự toán ngân sách 5.2 (SCRUM-11) | AI tổng hợp bảng chi phí; sinh viên tra cứu biểu giá DigitalOcean/OpenAI, làm tròn số thực tế, chuẩn hóa 4 thành viên xuyên suốt SDLC | [Chi tiết #07](#entry-07) |
| **#08** | 21h30 22/10<br>- 00h30 23/10 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Xây dựng Prototype Giao diện 3 cột HelpDesk với React & Tailwind CSS (SCRUM-10) | AI sinh các React components mẫu (Queue, Workspace, Chat, Copilot); sinh viên tự cấu hình Tailwind, tối ưu layout Zalo/Linear, tinh chỉnh responsive | [Chi tiết #08](#entry-08) |
| **#09** | 07h30<br>28/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Rà soát nhất quán đề xuất dự án và tạo bản nộp hoàn thiện tại `reports/submit/` (SCRUM-11) | AI hỗ trợ kiểm tra ngữ pháp tiếng Việt, tính nhất quán của thuật ngữ kỹ thuật; sinh viên kiểm tra chéo với SRS-master.md và tạo file nộp | [Chi tiết #09](#entry-09) |
| **#10** | 08h20<br>28/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>Google via Antigravity IDE | Tái cấu trúc Báo cáo sử dụng AI theo Quy định của Khoa CNTT - HCMUS (SCRUM-11) | AI đối chiếu cấu trúc 7 trường thông tin của Khoa; sinh viên biên soạn bảng ma trận và hệ thống trích dẫn chuẩn cho toàn nhóm | [Chi tiết #10](#entry-10) |
| **#11** | 19h30<br>28/10/2026 | Nguyễn Đức Lãm<br>`24120083` | ChatGPT (GPT-6.1 Sol)<br>OpenAI via chat.openai.com | Rà soát, kiểm tra nội dung của phần 5 | AI kiểm tra và đưa ra những điểm còn chưa rõ ràng, mâu thuẫn với tài liệu gốc (SCRUM-14) | [Chi tiết #11](#entry-11) |
---

## 3. CHI TIẾT CÁC PHIÊN SỬ DỤNG AI (CHUẨN TRÍCH DẪN QUY ĐỊNH)

Mỗi mục dưới đây tuân thủ nghiêm ngặt **Mục 5.B (Ghi chú sử dụng AI)** của Quy định Khoa CNTT - ĐHKHTN, bao gồm đầy đủ 7 yếu tố bắt buộc.

---

### <a id="entry-01"></a>Phiên ghi nhận #01: Thiết lập cấu trúc Repository và Công cụ CI/Git hooks
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *09h00 - 17h30 ngày 19/10/2026*, prompt: *“Tạo bộ khung cấu trúc dự án phần mềm theo mô hình Modular Monolith React + Spring Boot, script commit-msg git hook kiểm tra định dạng commit có chứa Jira Issue Key dạng [A-Z]+-[0-9]+, và kịch bản Python render báo cáo Markdown sang HTML tự chứa kèm script đóng gói đồ án zip”*, dùng để hỗ trợ thiết lập hạ tầng dự án ban đầu cho task SCRUM-6, AI sinh đoạn mã shell script git hook và khung cấu trúc thư mục, sinh viên tự kiểm tra, bổ sung logic an toàn đường dẫn, hoàn thiện regex kiểm tra quy cách commit tiếng Việt và chạy kiểm thử dry-run.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Mẫu shell script `commit-msg` cơ bản, script `render_reports.py` và kịch bản đóng gói `package_submission.py`.
  - *Nội dung tự thực hiện & kiểm chứng:* Bổ sung xử lý UTF-8 tiếng Việt, tinh chỉnh thông báo lỗi song ngữ Việt - Anh, cấu hình quyền thực thi `chmod +x` và chạy kiểm thử trực tiếp trên zsh/git client.
  - *Minh chứng:* Nhật ký commit Git `[09ae70cf]` và `[c4496214]`.

---

### <a id="entry-02"></a>Phiên ghi nhận #02: Soạn thảo tài liệu Hướng dẫn làm việc nhóm & Quy trình Template 0
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *18h30 ngày 19/10/2026*, prompt: *“Xây dựng tài liệu hướng dẫn quy trình làm việc Agile Scrum chi tiết cho nhóm sinh viên 4 người thực hiện đồ án NMCNPM theo Template 0, bao gồm quy định đặt tên nhánh git, cú pháp commit kèm Jira key, quy trình Review chéo và các mốc deadline nội bộ”*, dùng để hỗ trợ soạn thảo tài liệu `TEAM_GUIDE_TEMPLATE0.md` cho task SCRUM-7, AI sinh khung tài liệu hướng dẫn và các bước quy trình, sinh viên đối chiếu lịch trình môn học và phân công cụ thể cho từng thành viên theo ma trận module.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Khung tài liệu hướng dẫn Scrum cơ bản và quy ước Git Flow.
  - *Nội dung tự thực hiện & kiểm chứng:* Gán chính xác địa chỉ email Jira, tài khoản Git, mã số sinh viên, và phân công vai trò 4 phân hệ (A, B, C, D) cho từng thành viên; thiết lập các mốc thời gian chi tiết từ ngày 19/10 đến 29/10/2026.
  - *Minh chứng:* Nhật ký commit Git `[72212cb5]`.

---

### <a id="entry-03"></a>Phiên ghi nhận #03: Soạn thảo bản nháp Mục 1, 2 và 3.2 Đề xuất dự án (SCRUM-8)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-6, OpenAI, chat.openai.com*, truy cập *ngày 19/10/2026*, input: *“Template 0, hướng dẫn nhóm, SRS và phần được phân công”*, dùng để hỗ trợ tạo bản nháp Project Proposal cho SCRUM-8 (Mục 1, Mục 2 và Mục 3.2), AI sinh bản nháp tham khảo cho trang bìa, Mục 1, Mục 2 và Mục 3.2, sinh viên tự đối chiếu mẫu, SRS và kiểm tra nội dung trước khi đưa vào bản nộp.
- **Thành viên chịu trách nhiệm:** `24120121` - Lê Quý Phúc (Phân hệ AI Assistance)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Bản nháp tham khảo cho trang bìa, Mục 1, Mục 2 và Mục 3.2.
  - *Nội dung tự thực hiện & kiểm chứng:* Đối chiếu mẫu template giảng viên và SRS-master.md trước khi đưa vào bản nộp.
  - *Minh chứng:* Nhật ký commit Git `[520a0f44]` ngày 19/10/2026.

---

### <a id="entry-04"></a>Phiên ghi nhận #04: Rà soát Phụ lục D và Bảng chức năng (SCRUM-9)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-6, OpenAI, chat.openai.com*, truy cập *ngày 22/10/2026*, input: *“Nội dung từ reports/SRS-master.md bao gồm Phụ lục D, Mục 3.3, 4, 5, 7, 8”*, dùng để hỗ trợ review Phụ lục D và Mục 3.1.1, AI sinh các tham chiếu bổ sung, sinh viên đối chiếu các tham chiếu với nội dung của các cột Nhu cầu/Yêu cầu, làm rõ một số nội dung của cột Nhu cầu, bổ sung các tham chiếu hiện tại có liên quan, gợi ý bổ sung thêm các tham chiếu chưa có để làm rõ nội dung của 1 số chức năng.
- **Thành viên chịu trách nhiệm:** `24120503` - Phan Gia Phúc (Phân hệ Ticket Management)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Các tham chiếu bổ sung.
  - *Nội dung tự thực hiện & kiểm chứng:* Đối chiếu các tham chiếu với nội dung của các cột Nhu cầu/Yêu cầu; làm rõ nội dung cột Nhu cầu, bổ sung tham chiếu có liên quan.
  - *Minh chứng:* Nhật ký commit Git `[0bbf775e]` ngày 22/10/2026.

---

### <a id="entry-05"></a>Phiên ghi nhận #05: Soạn thảo bản nháp Kiến trúc và Kế hoạch phát triển (SCRUM-10)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-6.1 Sol, OpenAI, chat.openai.com*, truy cập *09h30 ngày 22/10/2026*, prompt: *“chào bạn, tôi đang cần viết phần 3.1.2, kiến trúc tổng thể phần mềm, với nguồn tài liệu được lấy ở Trình bày kiến trúc tổng thể đáp ứng danh sách chức năng ở mục 3.1.1 (sơ đồ kiến trúc + giải thích các thành phần và luồng vận hành). Tham khảo Mục 9.1, 9.3, 9.4, 12.2 và Phụ lục trong reports/SRS-master.md, hãy dùng skill humanizer viết cho tôi phần này một cách tự nhiên nhất, cho tôi một cell .md để tôi chèn vào file của mình, không tự ý thay đổi bất kì file nào; tiếp tục với phần Kế hoạch phát triển Trình bày cụ thể kế hoạch phát triển phần mềm qua 5 giai đoạn cùng thành phẩm cụ thể của từng giai đoạn. Tham khảo Mục 14, 15, 17, 21 và Phụ lục G trong reports/SRS-master.md (lấy chuẩn ngày tháng theo phụ lục G)”*, dùng để hỗ trợ tạo bản nháp Project Proposal cho phần 3.1.2 và phần 4, AI sinh bản nháp cho phần 3.1.2 và phần 4, sinh viên đối chiếu với Phụ lục E và Phụ lục G trước khi đưa vào bản nộp, tinh chỉnh thuật ngữ, chuẩn hóa mốc ngày tháng theo lịch tuần.
- **Thành viên chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Chi tiết các câu prompt nguyên văn do thành viên khai báo (trích lục từ commit Git `[5405de76]`):**
  1. *"- chào bạn, tôi đang cần viết phần 3.1.2, kiến trúc tổng thể phần mềm, với nguồn tài liệu được lấy ở Trình bày kiến trúc tổng thể đáp ứng danh sách chức năng ở mục 3.1.1 (sơ đồ kiến trúc + giải thích các thành phần và luồng vận hành). Tham khảo Mục 9.1, 9.3, 9.4, 12.2 và Phụ lục trong reports/SRS-master.md, hãy dùng skill $humanizer:humanizer viết cho tôi phần này một cách tự nhiên nhất, cho tôi một cell .md để tôi chèn vào file của mình, không tự ý thay đổi bất kì file nào"*
  2. *"- ok, tiếp tục với phần Kế hoạch phát triển Trình bày cụ thể kế hoạch phát triển phần mềm qua 5 giai đoạn cùng thành phẩm cụ thể của từng giai đoạn. Tham khảo Mục 14, 15, 17, 21 và Phụ lục G trong reports/SRS-master.md (lấy chuẩn ngày tháng theo phụ lục G)"*
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Bản nháp cho phần 3.1.2 và phần 4.
  - *Nội dung tự thực hiện & kiểm chứng:* Đối chiếu với Phụ lục E và Phụ lục G trước khi đưa vào bản nộp; tinh chỉnh thuật ngữ, chuẩn hóa mốc ngày tháng theo lịch tuần.
  - *Minh chứng:* Nhật ký commit Git `[5405de76]` ngày 22/10/2026.

---

### <a id="entry-06"></a>Phiên ghi nhận #06: Chuẩn hóa mục lục Proposal theo mẫu Word của Giảng viên & Hợp nhất nội dung nhóm
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *00h30 ngày 22/10/2026*, prompt: *“Đối chiếu cấu trúc mục lục của file 00-project-proposal.md với bản mẫu Word chính thức của Giảng viên môn NMCNPM HCMUS, định dạng lại toàn bộ heading từ Mục 1 đến Mục 5 đảm bảo chuẩn phân cấp, và hỗ trợ giải quyết xung đột khi tích hợp nội dung của các thành viên”*, dùng để hỗ trợ chuẩn hóa cấu trúc đề xuất dự án cho task SCRUM-7 & SCRUM-11, AI sinh mục lục gợi ý và phát hiện các mục bị lệch cấu trúc, sinh viên tự kiểm tra, hợp nhất nội dung từ nhánh của 3 thành viên và căn chỉnh đúng số thứ tự mục.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Phân tích đối chiếu cấu trúc mục lục và đề xuất chỉnh sửa tiêu đề mục.
  - *Nội dung tự thực hiện & kiểm chứng:* Trực tiếp giải quyết conflict git, sắp xếp lại các phần Bìa, Mục 1, 2, 3.1.1, 3.1.2, 3.2, 4, 5 đúng theo mẫu chuẩn của trường, kiểm tra việc hiển thị trên file Markdown.
  - *Minh chứng:* Commit Git `[a89f1e22]` ngày 22/10/2026.

---

### <a id="entry-07"></a>Phiên ghi nhận #07: Kế hoạch nhân sự và Dự toán ngân sách thực tế có kiểm chứng
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *15h30 ngày 22/10/2026*, prompt: *“Đối chiếu hồ sơ Group 04 kiến trúc Modular Monolith React + Spring Boot + Postgres/pgvector chạy 1 VPS DigitalOcean 48 USD/tháng, Namecheap domain, OpenAI GPT-4o-mini/embedding, Cloudflare SSL 0 đồng; tính toán bảng dự toán chi phí thực tế có nguồn tham chiếu chính thống, làm tròn số lẻ và trình bày ma trận 4 thành viên cùng tham gia 5 công đoạn SDLC”*, dùng để hỗ trợ hoàn thiện Mục 5.1 và 5.2 trong `00-project-proposal.md`, AI sinh khung bảng chi phí và công thức quy đổi tiền tệ, sinh viên tra cứu trực tiếp bảng giá nhà cung cấp, loại bỏ các diễn đạt học đường, chuẩn hóa định mức API thực tế và bổ sung nguồn trích dẫn đầy đủ.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết 8 câu prompt nguyên văn do thành viên khai báo (trích lục từ commit Git `[e571f12b]`):**
  1. *“phần kế hoạch nhân sự & chi phí có trong SRS trước đó là dựa vào đâu mà soạn nên”*
  2. *“hiện tại ở giai đoạn sau khi hoàn thành template, bước vào giai đoạn triển khai tiếp theo thì sẽ có những module công việc nào, hiện tại đang phân như nào và có mốc thời gian cụ thể không”*
  3. *“Theo quy định bắt buộc của môn học, dự án không phân chia theo kiểu tách biệt... mà tất cả 4 thành viên đều tham gia đầy đủ 5 công đoạn phát triển phần mềm (SDLC)... không nên có những phần như thế này, tài liệu proposal trình bày như một bản nộp chuyên nghiệp, các phần câu từ như vậy không nên được sử dụng. Phân công công việc: Lãm làm Knowledge Base, Phan Gia Phúc làm Ticket Management, Lê Quý Phúc làm AI Assistance, tôi là Bình làm Identity & Access...”*
  4. *“ở bảng cấu trúc nhân sự, không cần MSSV, Không ghi Module A hay B hay C,D. Thay Trách nhiệm chuyên môn xuyên suốt SDLC thành Mô tả công việc. Và có thể liệt kê chi tiết hơn để đảm bảo đủ đúng các công việc thực hiện... thêm ghi chú: Các chi phí được tính toán dựa trên quy mô nhóm nhỏ... và ngoài ra với các chi phí, nếu tìm thấy tài liệu tham khảo chính thức từ các trang web chính thống cho các loại chi phí thì càng tốt”*
  5. *“DỰA TRÊN NGUỒN THÔNG TIN NÀY, CHỈNH SỬA LẠI CHÍNH XÁC CHO TÔI PHẦN CHI PHÍ CHO ĐÚNG THỰC TẾ CÓ KIỂM CHỨNG NGUỒN: đối chiếu hồ sơ Group 04 kiến trúc Modular Monolith React + Spring Boot + Postgres/pgvector chạy 1 VPS DigitalOcean 48 USD/tháng, Namecheap domain, OpenAI GPT-4o-mini/embedding, Cloudflare SSL 0 đồng, phân định rõ dự toán kinh tế 48,82 triệu và thực chi tiền mặt...”*
  6. *“những con số lẻ thì làm tròn lên một xíu ví dụ 290 thì lên 300”*
  7. *“Dựa trên nội dung bảng giá chính thức... sửa lại phép tính chi phí LLM: GPT-6 Luna 0,10 USD input / 0,50 USD output -> 1,95 USD = 49.725 VNĐ, làm tròn dự toán 60.000 VNĐ; Embedding text-embedding-3-small 0,30 USD = 7.650 VNĐ, làm tròn 10.000 VNĐ... chỉnh lại hai mục 4, 5 cho phù hợp”*
  8. *“Với các số lẻ hãy làm tròn nhẹ lên và thêm dấu ~ trước”*
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Khung bảng tính ngân sách dự toán, công thức tính chi phí token đầu vào/đầu ra.
  - *Nội dung tự thực hiện & kiểm chứng:* Tra cứu trực tiếp bảng giá DigitalOcean Droplets, Namecheap TLD, OpenAI API docs và Cloudflare SSL; làm tròn số lẻ thực tế (~47.840.000 VNĐ bao gồm dự phòng 10%); đảm bảo cả 4 thành viên tham gia đầy đủ 5 công đoạn SDLC theo yêu cầu bắt buộc của Giảng viên.
  - *Minh chứng:* Nhật ký commit Git `[e571f12b]` và `[f5da77da]`.

---

### <a id="entry-08"></a>Phiên ghi nhận #08: Xây dựng & Tinh chỉnh Prototype Giao diện 3 cột HelpDesk với React & Tailwind CSS
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *21h30 ngày 22/10/2026 đến 00h30 ngày 23/10/2026*, prompt: *“Khởi tạo ứng dụng React + TypeScript + Tailwind CSS cho hệ thống AI-Powered Helpdesk theo bố cục 3 cột (Sidebar điều hướng, Ticket Queue list hỗ trợ thu phóng kiểu Linear/Notion, Workspace xử lý ticket tích hợp AI Copilot bar góc dưới, Customer Portal chat hỗ trợ phím tắt Enter gửi và Shift+Enter xuống dòng, bộ lọc bài viết Knowledge Base và trang quản trị người dùng Admin)”*, dùng để hỗ trợ phát triển nguyên mẫu giao diện nhanh (UI Prototype) phục vụ minh họa cho đề xuất dự án (SCRUM-10), AI sinh mã nguồn khởi tạo các component React và dữ liệu mock mẫu, sinh viên tự cấu hình Tailwind, tối ưu lại trải nghiệm người dùng tương tự Zalo/Facebook Messenger, sửa lỗi chuyển tab ticket, chụp 11 ảnh minh chứng và đóng gói thành trang `UI_SHOWCASE.html`.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Khung các component `TicketWorkspace.tsx`, `TicketQueue.tsx`, `CustomerPortal.tsx`, `AdminUserView.tsx` và file dữ liệu `mock/data.ts`.
  - *Nội dung tự thực hiện & kiểm chứng:* Tối ưu bố cục responsive, loại bỏ các nút AI trùng lặp, khắc phục lỗi mất thanh rail khi co giãn danh sách ticket, bổ sung xử lý sự kiện bàn phím gửi tin nhắn, tách nhỏ subcomponents theo kiến trúc modular, chạy thử nghiệm trực tiếp trên trình duyệt bằng `npm run dev`.
  - *Minh chứng:* Chuỗi commit Git `[f127d244]`, `[a9f542d2]`, `[de9a6ecd]`, `[e4d5447f]`, `[dac005cd]`, `[d82788cd]`.

---

### <a id="entry-09"></a>Phiên ghi nhận #09: Rà soát nhất quán đề xuất dự án và tạo bản nộp hoàn thiện
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *07h30 ngày 28/10/2026*, prompt: *“Rà soát toàn bộ văn bản 00-project-proposal.md để phát hiện các lỗi chính tả, câu từ không chuẩn học thuật, các ghi chú nháp còn sót lại; đối chiếu tính nhất quán của số liệu chi phí, ngày tháng các sprint và phân công module với tài liệu SRS-master.md”*, dùng để hỗ trợ rà soát chất lượng trước khi nộp đề xuất dự án (SCRUM-11), AI sinh danh sách các điểm cần làm rõ và gợi ý hiệu chỉnh câu từ, sinh viên tự đối chiếu lại từng số liệu, làm sạch các dòng ghi chú nội bộ và tạo bản sao chính thức tại `reports/submit/00-project-proposal.md`.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Gợi ý các vị trí câu từ có thể tối ưu diễn đạt và lưu ý định dạng bảng.
  - *Nội dung tự thực hiện & kiểm chứng:* Đọc soát toàn bộ tài liệu hơn 400 dòng, đảm bảo 100% số liệu chi phí khớp với bảng 5.2, đảm bảo 30 User Stories khớp với SRS-master, kiểm tra tính hợp lệ của bản nộp.
  - *Minh chứng:* Nhật ký commit Git `[9f7b9920]` ngày 28/10/2026.

---

### <a id="entry-10"></a>Phiên ghi nhận #10: Tái cấu trúc Báo cáo sử dụng AI theo Quy định của Khoa CNTT - HCMUS
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 3.8 Flash Medium, Google, via Antigravity IDE*, truy cập *08h20 ngày 28/10/2026*, prompt: *“Phân tích tài liệu Quy định về việc sử dụng AI của Khoa CNTT Trường ĐHKHTN TP.HCM (học phần Tư duy tính toán CS10014), tái cấu trúc bảng theo dõi AI hiện tại thành bảng ma trận chuẩn không bị vỡ layout khi render HTML/PDF, và trích dẫn chi tiết từng phiên sử dụng tuân thủ đủ 7 yêu cầu bắt buộc”*, dùng để chuẩn hóa báo cáo sử dụng AI theo chuẩn bắt buộc của nhà trường (SCRUM-11), AI đề xuất cấu trúc phân chia 2 tầng (Bảng tổng hợp nhanh + Bản ghi trích dẫn chi tiết), sinh viên tự biên soạn nội dung, kiểm tra đối soát với toàn bộ lịch sử commit Git và xây dựng form mẫu cho nhóm.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Cấu trúc phân cấp tài liệu và gợi ý định dạng bảng Markdown tương thích bộ sinh HTML.
  - *Nội dung tự thực hiện & kiểm chứng:* Bóc tách các prompt dài trước đây khỏi ô bảng, trích lục lịch sử commit của cả 4 thành viên, chạy script `render_reports.py` để xác thực tính tương thích hiển thị trên trình duyệt và bản in PDF.
  - *Minh chứng:* Nhật ký commit Git `[b952c039]` ngày 28/10/2026.

---

### <a id="entry-11"></a>Phiên ghi nhận #11: Rà soát, kiểm tra nội dung của phần 5
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-6.1 Sol, OpenAI, chat.openai.com*, truy cập *19h30 ngày 28/10/2026*, prompt: *“đây là nội dung phần 5 do bạn tôi viết bạn hãy đọc, và kiểm tra lại thật kỹ xem 1. có chỗ nào bị mâu thuẫn so với file SRS không theo nội dung tham khảo như sau: # 5. Kế hoạch nhân sự & chi phí\
   \> \*Ghi chú nguồn nguyên liệu:\* Cấu trúc nhân sự toàn dự án và liệt kê các khoản chi phí dự kiến. Tham khảo Mục 16, 16.1, \*\*Phụ lục H\*\* và \*\*Phụ lục I\*\* trong \`reports/SRS-master.md\`.\
   \
   \*(Nội dung do \`Ngô Viết Thanh Bình\` biên soạn theo Jira \`SCRUM-11\`)\*\
   \
   \### 5.1. Cấu trúc nhân sự\
   \> \*Ghi chú nguồn nguyên liệu:\* Ma trận vai trò, mô tả trách nhiệm và người phụ trách. Tham khảo \*\*Phụ lục H\*\* trong \`reports/SRS-master.md\`.\
   \
   \### 5.2. Kế hoạch chi phí\
   \> \*Ghi chú nguồn nguyên liệu:\* Bảng tổng hợp chi phí nhân sự, hạ tầng cloud, API LLM, công cụ và dự phòng rủi ro. Tham khảo \*\*Phụ lục I\*\* trong \`reports/SRS-master.md\`. 2. có chỗ nào cách viết bị quá máy móc, theo kiẻu của AI quá không, dùng skill $humanizer:humanizer để gợi ý cho tôi các sửa(chỉ gợi ý chỗ bị lỗi và cách sửa, không tự sửa)”*

- **Thành viên chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Chi tiết các câu prompt nguyên văn do thành viên khai báo:**
  1. *"- đây là nội dung phần 5 do bạn tôi viết bạn hãy đọc, và kiểm tra lại thật kỹ xem có chỗ nào bị mâu thuẫn so với file SRS không theo nội dung tham khảo như sau: # 5. Kế hoạch nhân sự & chi phí\
   \> \*Ghi chú nguồn nguyên liệu:\* Cấu trúc nhân sự toàn dự án và liệt kê các khoản chi phí dự kiến. Tham khảo Mục 16, 16.1, \*\*Phụ lục H\*\* và \*\*Phụ lục I\*\* trong \`reports/SRS-master.md\`.\
   \
   \*(Nội dung do \`Ngô Viết Thanh Bình\` biên soạn theo Jira \`SCRUM-11\`)\*\
   \
   \### 5.1. Cấu trúc nhân sự\
   \> \*Ghi chú nguồn nguyên liệu:\* Ma trận vai trò, mô tả trách nhiệm và người phụ trách. Tham khảo \*\*Phụ lục H\*\* trong \`reports/SRS-master.md\`.\
   \
   \### 5.2. Kế hoạch chi phí\
   \> \*Ghi chú nguồn nguyên liệu:\* Bảng tổng hợp chi phí nhân sự, hạ tầng cloud, API LLM, công cụ và dự phòng rủi ro. Tham khảo \*\*Phụ lục I\*\* trong \`reports/SRS-master.md\`.
 có chỗ nào cách viết bị quá máy móc, theo kiẻu của AI quá không, dùng skill $humanizer:humanizer để gợi ý cho tôi các sửa(chỉ gợi ý chỗ bị lỗi và cách sửa, không tự sửa)"*
  2. *"nhìn chung, thì phần 5.1 đang mô tả quá chi tiết, mở rộng so với bản SRS đúng không"*
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Nhận xét cho phần 5.
  - *Nội dung tự thực hiện & kiểm chứng:* Kiểm chứng và đối chiếu với mục 16., 16.1, phụ lục H, phụ lục I trong file SRS-master.md.
  - *Minh chứng:* Phiên rà soát phản biện được thực hiện trực tiếp trên bản thảo Google Docs nội bộ của nhóm (không phát sinh commit mã nguồn riêng trên Git).

---

## 4. CAM KẾT TUÂN THỦ QUY CHẾ VÀ HÀNH VI CẤM

Mọi thành viên nhóm cam kết tuân thủ nghiêm ngặt Điều 4.5 và Điều 6 của Quy chế học phần:
1. **CẤM** dùng AI để viết toàn bộ báo cáo (dù có chỉnh sửa).
2. **CẤM** sinh kết quả thực nghiệm giả, số liệu kiểm thử giả.
3. **CẤM** sao chép toàn bộ mã nguồn do AI tạo ra mà không chạy thử, không kiểm tra, không hiểu rõ.
4. **CẤM** làm sai lệch phần ghi chú sử dụng AI (xóa prompt, che giấu hoặc cung cấp bằng chứng giả).
5. **Quy chế kỷ luật:** Vi phạm lần đầu sẽ bị cảnh cáo văn bản và trừ điểm; vi phạm lần hai sẽ bị **chấm 0 điểm toàn bộ học phần**.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)

1. Khoa Công nghệ Thông tin, Trường Đại học Khoa học Tự Nhiên TP.HCM. *Quy định về việc sử dụng AI - Học phần Tư duy tính toán (CS10014)*. Cập nhật tháng 10/2025.

