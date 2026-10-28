# BÁO CÁO SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI USAGE REPORT)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm (CS10014 / NMCNPM) — Trường ĐHKHTN, ĐHQG-HCM  
> **Chuẩn quy định:** Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS  

---

## THÔNG TIN TÀI LIỆU

- **Tiêu đề (Title):** AI Usage Transparency & Accountability Report
- **Phiên bản (Version):** 1.1.0
- **Ngày cập nhật (Last Updated):** 2026-10-28
- **Nhóm trưởng & Giám sát tuân thủ:** `24120269` - `Ngô Viết Thanh Bình` (thanhbinh55)
- **Danh sách thành viên:**
  1. `24120269` - `Ngô Viết Thanh Bình` (Git: `thanhbinh55` — Phân hệ D: Identity & Access)
  2. `24120083` - `Nguyễn Đức Lãm` (Git: `Lamnguyen-code` — Phân hệ B: Knowledge Base)
  3. `24120503` - `Phan Gia Phúc` (Git: `t4lf4n` — Phân hệ C: Ticket Management)
  4. `24120121` - `Lê Quý Phúc` (Git: `Shinkiisme` — Phân hệ A: AI Assistance)
- **Phạm vi tài liệu:** Ghi nhận minh bạch toàn bộ quá trình sử dụng các công cụ Trí tuệ nhân tạo (LLM, AI Coding Assistant, Prompt-based generators) trong đồ án theo đúng quy chuẩn bắt buộc của Khoa CNTT - HCMUS.

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
4. **Đạo đức học thuật & Bảo mật:** Kiểm chứng chéo mọi dữ liệu với giáo trình chuẩn (Russell & Norvig, tài liệu môn học); không đưa khóa bí mật (API keys, credentials) vào các dịch vụ AI công cộng.

---

## 2. BẢNG TỔNG HỢP NHẬT KÝ SỬ DỤNG AI (SUMMARY LOG MATRIX)

Bảng dưới đây tổng hợp các phiên tương tác với AI trong quá trình triển khai dự án. Để xem chi tiết câu lệnh prompt và phương pháp kiểm chứng, xem tại [Mục 3: Chi tiết các phiên sử dụng AI](#3-chi-tiết-các-phiên-sử-dụng-ai-chuẩn-trích-dẫn-quy-định).

| ID | Thời gian | Thành viên (MSSV) | Công cụ & Nền tảng | Hạng mục / Vị trí áp dụng | Nội dung AI tạo & Tự kiểm chứng | Minh chứng |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: |
| **#01** | 09h00<br>19/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (2.5 Pro)<br>Google via Antigravity IDE | Khung Repository, kịch bản CI & Git hooks (SCRUM-6) | AI gợi ý cấu trúc thư mục & bash script mẫu; sinh viên tự viết lại regex Jira key, logic kiểm tra an toàn và chạy dry-run | [Chat #01](#entry-01) |
| **#02** | 14h30<br>19/10/2026 | Lê Quý Phúc<br>`24120121` | ChatGPT (GPT-4o)<br>OpenAI via chat.openai.com | Bản nháp Project Proposal Mục 1, 2, 3.2 (SCRUM-8) | AI sinh khung mô tả bài toán; sinh viên đối chiếu template giảng viên, viết lại bằng thuật ngữ dự án Helpdesk | [Chat #02](#entry-02) |
| **#03** | 10h15<br>22/10/2026 | Phan Gia Phúc<br>`24120503` | ChatGPT (GPT-4o)<br>OpenAI via chat.openai.com | Rà soát ma trận chức năng Mục 3.1.1 & Phụ lục D (SCRUM-9) | AI đề xuất tiêu chí phân nhóm yêu cầu; sinh viên đối chiếu 30 User Stories, chuẩn hóa mã US-01..30 và ma trận truy vết | [Chat #03](#entry-03) |
| **#04** | 15h45<br>22/10/2026 | Nguyễn Đức Lãm<br>`24120083` | ChatGPT (GPT-4o)<br>OpenAI via chat.openai.com | Dự thảo Kiến trúc Modular Monolith & Lịch trình 5 pha (SCRUM-10) | AI sinh mô tả giao tiếp các phân hệ; sinh viên hiệu chỉnh sơ đồ Container C4, chuẩn hóa mốc tuần theo lịch học | [Chat #04](#entry-04) |
| **#05** | 20h30<br>22/10/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (2.5 Pro)<br>Google via Antigravity IDE | Chuẩn hóa Ma trận nhân sự 5.1 & Dự toán ngân sách 5.2 (SCRUM-11) | AI tổng hợp bảng chi phí; sinh viên tra cứu biểu giá DigitalOcean/OpenAI, làm tròn số thực tế, chuẩn hóa 4 thành viên xuyên suốt SDLC | [Chat #05](#entry-05) |

---

## 3. CHI TIẾT CÁC PHIÊN SỬ DỤNG AI (CHUẨN TRÍCH DẪN QUY ĐỊNH)

Mỗi mục dưới đây được định dạng tuân thủ nghiêm ngặt **Mục 5.B (Ghi chú sử dụng AI)** của Quy định Khoa CNTT - ĐHKHTN, bao gồm đầy đủ 7 yếu tố bắt buộc.

---

### <a id="entry-01"></a>📌 Phiên ghi nhận #01: Thiết lập cấu trúc Repository và Công cụ CI/Git hooks
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 2.5 Pro, Google, via Antigravity IDE*, truy cập *09h00 ngày 19/10/2026*, prompt: *“Tạo bộ khung cấu trúc dự án phần mềm theo mô hình Modular Monolith React + Spring Boot, script commit-msg git hook kiểm tra định dạng commit có chứa Jira Issue Key dạng [A-Z]+-[0-9]+ và kịch bản python đóng gói báo cáo”*, dùng để hỗ trợ thiết lập hạ tầng dự án ban đầu cho task SCRUM-6, AI sinh đoạn mã shell script git hook và khung cấu trúc thư mục, sinh viên tự kiểm tra, bổ sung logic an toàn đường dẫn, hoàn thiện regex kiểm tra quy cách commit tiếng Việt và chạy kiểm thử dry-run.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Mẫu shell script `commit-msg` cơ bản và kịch bản đóng gói zip.
  - *Nội dung tự thực hiện & kiểm chứng:* Bổ sung xử lý UTF-8, tinh chỉnh thông báo lỗi song ngữ Việt - Anh, cấu hình quyền thực thi `chmod +x` và chạy kiểm thử trực tiếp trên zsh/git client.
  - *Minh chứng:* File script kiểm chứng tại [.githooks/commit-msg](file:///.githooks/commit-msg) và [scripts/package_submission.py](file:///scripts/package_submission.py).

---

### <a id="entry-02"></a>📌 Phiên ghi nhận #02: Soạn thảo bản nháp Mục 1, 2 và 3.2 Đề xuất dự án (SCRUM-8)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-4o, OpenAI, chat.openai.com*, truy cập *14h30 ngày 19/10/2026*, prompt: *“Đề xuất cấu trúc trình bày mục tiêu, bối cảnh thực tế và đối tượng thụ hưởng cho hệ thống AI-Powered Helpdesk dành cho doanh nghiệp SME dựa trên các tiêu chí mẫu đề cương đồ án NMCNPM”*, dùng để hỗ trợ viết Mục 1 (Giới thiệu & Lý do chọn đề tài), Mục 2 (Mục tiêu dự án) và Mục 3.2 (Đối tượng thụ hưởng) trong báo cáo `00-project-proposal.md`, AI sinh mô tả tổng quan và các gạch đầu dòng mục tiêu sơ bộ, sinh viên tự đối chiếu yêu cầu môn học, viết lại hoàn toàn bằng lời văn của nhóm, cụ thể hóa cho bài toán Helpdesk với 4 phân hệ chính.
- **Thành viên chịu trách nhiệm:** `24120121` - Lê Quý Phúc (Phân hệ AI Assistance)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Khung ý tưởng về bài toán hỗ trợ kỹ thuật và phân loại người dùng (End-user, Helpdesk Agent, Administrator).
  - *Nội dung tự thực hiện & kiểm chứng:* Loại bỏ các mô tả chung chung, bổ sung chỉ số mục tiêu cụ thể (giảm 40% thời gian xử lý ticket, phản hồi tự động dưới 5 giây), chỉnh sửa theo mẫu Template 0 của Khoa.
  - *Minh chứng:* Nhật ký commit Git `[520a0f44]` ngày 19/10/2026.

---

### <a id="entry-03"></a>📌 Phiên ghi nhận #03: Rà soát ma trận chức năng và đối chiếu SRS (SCRUM-9)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-4o, OpenAI, chat.openai.com*, truy cập *10h15 ngày 22/10/2026*, prompt: *“Gợi ý cách tổ chức ma trận truy vết chức năng (Traceability Matrix) từ User Stories sang các phân hệ kỹ thuật, kiểm tra tính đầy đủ của các chức năng phân quyền người dùng và quản lý vòng đời ticket”*, dùng để hỗ trợ hoàn thiện Mục 3.1.1 và Phụ lục D trong báo cáo đề xuất, AI sinh cấu trúc bảng phân tích 3 cột và danh sách tiêu chí kiểm tra, sinh viên đối chiếu trực tiếp với tài liệu `reports/SRS-master.md`, tự biên soạn chi tiết 30 User Stories và gán mã định danh phân hệ.
- **Thành viên chịu trách nhiệm:** `24120503` - Phan Gia Phúc (Phân hệ Ticket Management)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Gợi ý tiêu đề các cột của ma trận chức năng và phân định các trạng thái ticket.
  - *Nội dung tự thực hiện & kiểm chứng:* Xây dựng bảng ma trận 30 User Stories với đầy đủ tiêu chí chấp nhận (Acceptance Criteria), ánh xạ chính xác đến 4 phân hệ A, B, C, D của 4 thành viên.
  - *Minh chứng:* Nhật ký commit Git `[0bbf775e]` ngày 22/10/2026.

---

### <a id="entry-04"></a>📌 Phiên ghi nhận #04: Soạn thảo bản nháp Kiến trúc và Kế hoạch phát triển (SCRUM-10)
- **Trích dẫn chuẩn:**
  > **ChatGPT.** *GPT-4o, OpenAI, chat.openai.com*, truy cập *15h45 ngày 22/10/2026*, prompt: *“So sánh ưu nhược điểm của kiến trúc Microservices và Modular Monolith cho hệ thống Helpdesk nhỏ có tích hợp pgvector, và gợi ý phân bổ các mốc giai đoạn phát triển theo mô hình Agile Scrum trong 9 tuần”*, dùng để hỗ trợ viết Mục 3.1.2 (Kiến trúc tổng thể) và Mục 4 (Kế hoạch phát triển hệ thống) trong `00-project-proposal.md`, AI sinh nội dung so sánh lý thuyết và bảng phân bổ sprint dự kiến, sinh viên chọn lọc giải pháp Modular Monolith, vẽ lại biểu đồ kiến trúc Mermaid, căn chỉnh mốc ngày phù hợp với lịch học kỳ tại HCMUS.
- **Thành viên chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Bảng so sánh đặc điểm kiến trúc và khung 5 giai đoạn phát triển (Khởi tạo, Sprint 1, Sprint 2, Sprint 3, Đóng gói).
  - *Nội dung tự thực hiện & kiểm chứng:* Thiết lập chi tiết từng công việc cụ thể cho từng thành viên theo từng tuần, tích hợp công nghệ Postgres pgvector và Spring Boot 3.x, hoàn thiện sơ đồ luồng dữ liệu.
  - *Minh chứng:* Nhật ký commit Git `[5405de76]` ngày 22/10/2026.

---

### <a id="entry-05"></a>📌 Phiên ghi nhận #05: Chuẩn hóa Kế hoạch nhân sự và Dự toán ngân sách thực tế (SCRUM-11)
- **Trích dẫn chuẩn:**
  > **Google Gemini.** *Gemini 2.5 Pro, Google, via Antigravity IDE*, truy cập *20h30 ngày 22/10/2026*, prompt: *“Đối chiếu hồ sơ Group 04 kiến trúc Modular Monolith React + Spring Boot + Postgres/pgvector chạy 1 VPS DigitalOcean 48 USD/tháng, Namecheap domain, OpenAI GPT-4o-mini/embedding, Cloudflare SSL 0 đồng; tính toán bảng dự toán chi phí thực tế có nguồn tham chiếu chính thống, làm tròn số lẻ và trình bày ma trận 4 thành viên cùng tham gia 5 công đoạn SDLC”*, dùng để hỗ trợ hoàn thiện Mục 5.1 và 5.2 trong `00-project-proposal.md`, AI sinh khung bảng chi phí và công thức quy đổi tiền tệ, sinh viên tra cứu trực tiếp bảng giá nhà cung cấp, loại bỏ các diễn đạt học đường, chuẩn hóa định mức API thực tế và bổ sung nguồn trích dẫn đầy đủ.
- **Thành viên chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (DevOps / Lead)
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* Khung bảng tính ngân sách dự toán, công thức tính chi phí token đầu vào/đầu ra.
  - *Nội dung tự thực hiện & kiểm chứng:* Tra cứu trực tiếp bảng giá DigitalOcean Droplets, Namecheap TLD, OpenAI API docs và Cloudflare SSL; làm tròn số lẻ thực tế (~47.840.000 VNĐ bao gồm dự phòng 10%); đảm bảo cả 4 thành viên tham gia đầy đủ 5 công đoạn SDLC theo yêu cầu bắt buộc của Giảng viên.
  - *Minh chứng:* Nhật ký commit Git `[e571f12b]` và `[f5da77da]` ngày 22/10/2026.

---

## 4. KHUNG MẪU GHI NHẬT KÝ DÀNH CHO CÁC THÀNH VIÊN (TEMPLATE FOR NEXT SPRINTS)

Khi bất kỳ thành viên nào sử dụng AI trong các Sprint tiếp theo (lập trình backend/frontend, viết tài liệu kiểm thử, sinh test data), vui lòng thực hiện **2 bước**:

### Bước 1: Thêm một dòng vào Bảng tổng hợp (Mục 2)
```markdown
| **#XX** | [Giờ]h[Phút]<br>[Ngày/Tháng/Năm] | [Họ và tên]<br>`[MSSV]` | [Tên công cụ + Model]<br>[Nền tảng / Hãng] | [Tên mục / File áp dụng] | [Tóm tắt nội dung AI tạo & Tự kiểm chứng] | [Chat #XX](#entry-XX) |
```

### Bước 2: Thêm một mục chi tiết vào Mục 3 theo đúng mẫu trích dẫn của Khoa
```markdown
### <a id="entry-XX"></a>📌 Phiên ghi nhận #XX: [Tiêu đề công việc ngắn gọn]
- **Trích dẫn chuẩn:**
  > **[Tên công cụ].** *[Phiên bản], [Hãng phát triển], [Nền tảng/URL]*, truy cập *[Giờ] ngày [Ngày/Tháng/Năm]*, prompt: *“[Nguyên văn hoặc tóm lược đầy đủ câu lệnh prompt đã dùng]”*, dùng để [Mục đích sử dụng, ví dụ: hỗ trợ viết phần X / gợi ý hàm Y trong tệp Z], AI sinh [Nêu rõ nội dung AI tạo ra], sinh viên [Mô tả chi tiết cách tự chỉnh sửa, bổ sung ví dụ, kiểm thử test case và đối chiếu tài liệu học thuật].
- **Thành viên chịu trách nhiệm:** `[MSSV]` - [Họ và tên] ([Vai trò / Phân hệ])
- **Chi tiết đối soát:**
  - *Nội dung AI tạo:* [Mô tả chi tiết những gì AI đã trả lời]
  - *Nội dung tự thực hiện & kiểm chứng:* [Mô tả cách thức nhóm chạy thử, kiểm tra logic, tối ưu hóa]
  - *Minh chứng:* [Đường dẫn đến file mã nguồn, link chia sẻ chat hoặc ảnh chụp màn hình lưu tại reports/assets/]
```

---

## 5. THAM KHẢO QUY ĐỊNH KHOA CNTT - ĐHKHTN TP.HCM

Nhóm lưu lại các ví dụ minh họa chính thức từ văn bản quy định của Khoa để mọi thành viên dễ dàng đối chiếu khi khai báo:

> ### 📖 Ví dụ 1: ChatGPT (Soạn thảo & Lý thuyết)
> *– ChatGPT. GPT-4, OpenAI, chat.openai.com, truy cập 13h 25/05/2025, prompt: “Giải thích thuật toán A\* và ví dụ minh họa bằng Python”, dùng để hỗ trợ viết phần 3.2 trong báo cáo, AI sinh mô tả và code mẫu, sinh viên tự hiệu chỉnh nội dung, bổ sung ví dụ và kiểm chứng theo giáo trình Russell & Norvig.*

> ### 📖 Ví dụ 2: GitHub Copilot (Lập trình mã nguồn)
> *– GitHub Copilot. Copilot, GitHub via Visual Studio Code, truy cập 23h 26/05/2025, prompt: “Viết hàm tính giá trị heuristic h(n) cho thuật toán A\*”, dùng để sinh đoạn mã gợi ý cho phần 3.3, AI tạo phần khung hàm, sinh viên chỉnh sửa thuật toán theo yêu cầu bài toán và kiểm thử với dữ liệu mẫu.*

> ### 📖 Ví dụ 3: Google Gemini (Phân tích & So sánh)
> *– Gemini. Gemini 1.5, Google, gemini.google.com, truy cập 08h 27/05/2025, prompt: “So sánh ưu và nhược điểm của thuật toán DFS và BFS trong AI”, dùng để viết phần so sánh thuật toán tìm kiếm trong chương 2, AI sinh nội dung thô, sinh viên viết lại bằng ngôn ngữ học thuật, thêm ví dụ và trích dẫn nguồn sách.*

---

## 6. HÀNH VI CẤM THEO QUY ĐỊNH HỌC PHẦN (LƯU Ý QUAN TRỌNG)

Mọi thành viên nhóm cam kết tuân thủ nghiêm ngặt Điều 4.5 và Điều 6 của Quy chế:
1. ❌ **CẤM** dùng AI để viết toàn bộ báo cáo (dù có chỉnh sửa).
2. ❌ **CẤM** sinh kết quả thực nghiệm giả, số liệu kiểm thử giả.
3. ❌ **CẤM** sao chép toàn bộ mã nguồn do AI tạo ra mà không chạy thử, không kiểm tra, không hiểu rõ.
4. ❌ **CẤM** làm sai lệch phần ghi chú sử dụng AI (xóa prompt, che giấu hoặc cung cấp bằng chứng giả).
5. ⚠️ **Quy chế kỷ luật:** Vi phạm lần đầu sẽ bị cảnh cáo văn bản và trừ điểm; vi phạm lần hai sẽ bị **chấm 0 điểm toàn bộ học phần**.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)

1. Khoa Công nghệ Thông tin, Trường Đại học Khoa học Tự Nhiên TP.HCM. *Quy định về việc sử dụng AI - Học phần Tư duy tính toán (CS10014)*. Cập nhật tháng 10/2025.
2. Modern Language Association (MLA). *How Do You Cite Generative AI in MLA Style?* MLA Style Center, 2023. https://style.mla.org/citing-generative-ai/
3. MIT Libraries. *How to Cite Generative AI Tools (like ChatGPT)*. MIT Libraries, 2024. https://libguides.mit.edu/c.php?g=1353444&p=9991326
4. Harvard Library. *Citing Generative AI Tools*. Harvard Library Research Guides, 2024. https://guides.library.harvard.edu/c.php?g=1330621&p=10046069

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)

| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :---: | :---: | :--- | :--- | :---: |
| `1.0.0` | 2026-10-19 | DevOps Engineer | Khởi tạo bảng nhật ký theo dõi sử dụng AI | SCRUM-6 |
| `1.0.1` | 2026-10-19 | Lê Quý Phúc | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ soạn bản nháp Project Proposal | SCRUM-8 |
| `1.0.2` | 2026-10-22 | Phan Gia Phúc | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ rà soát Phụ lục D | SCRUM-9 |
| `1.0.3` | 2026-10-22 | Nguyễn Đức Lãm | Bổ sung nhật ký sử dụng ChatGPT hỗ trợ soạn Kiến trúc & Kế hoạch | SCRUM-10 |
| `1.0.4` | 2026-10-22 | Ngô Viết Thanh Bình | Bổ sung nhật ký sử dụng AI hỗ trợ soạn Mục 5 Nhân sự & Chi phí | SCRUM-11 |
| `1.1.0` | 2026-10-28 | Ngô Viết Thanh Bình | Tái cấu trúc báo cáo theo đúng Quy định sử dụng AI của Khoa CNTT - HCMUS (bảng tổng hợp + trích dẫn chuẩn 7 tiêu chí + hướng dẫn nhóm) | SCRUM-11 |
