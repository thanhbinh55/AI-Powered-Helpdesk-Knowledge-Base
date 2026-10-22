# BÁO CÁO ĐỀ XUẤT ĐỒ ÁN (PROJECT PROPOSAL - TEMPLATE 0)

> **Môn học:** Nhập môn Công nghệ Phần mềm (NMCNPM) - Trường ĐH Khoa học Tự nhiên (HCMUS)  
> **Đề tài:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Project Proposal - AI-Powered Helpdesk & Knowledge Base
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Phân công (Authors + Assignments):**
  - `24120121` - `Lê Quý Phúc`: Trang Bìa, Mục 1 (Bảng đánh giá), Mục 2 (Phát biểu bài toán), Mục 3.2 (Phần cứng) — *Jira: `SCRUM-8`*
  - `24120503` - `Phan Gia Phúc`: Mục 3.1.1 (Danh sách chức năng phần mềm) — *Jira: `SCRUM-9`*
  - `24120083` - `Nguyễn Đức Lãm`: Mục 3.1.2 (Kiến trúc tổng thể phần mềm) và Mục 4 (Kế hoạch phát triển) — *Jira: `SCRUM-10`*
  - `24120269` - `Ngô Viết Thanh Bình` *(Lead)*: Mục 5 (Kế hoạch nhân sự & chi phí: 5.1 & 5.2) — *Jira: `SCRUM-11`*

---

## MỤC LỤC
1. [Bảng đánh giá thành viên](#1-bảng-đánh-giá-thành-viên)
2. [Phát biểu bài toán sơ lược](#2-phát-biểu-bài-toán-sơ-lược)  
   2.1. [Bối cảnh và vấn đề đặt ra](#21-bối-cảnh-và-vấn-đề-đặt-ra)  
   2.2. [Ý tưởng giải pháp đề xuất](#22-ý-tưởng-giải-pháp-đề-xuất)  
   2.3. [Môi trường hoạt động dự kiến](#23-môi-trường-hoạt-động-dự-kiến)  
   2.4. [Ràng buộc thiết kế và triển khai](#24-ràng-buộc-thiết-kế-và-triển-khai)  
   2.5. [Mục tiêu và tiêu chí thành công](#25-mục-tiêu-và-tiêu-chí-thành-công)  
   2.6. [Đối tượng sử dụng](#26-đối-tượng-sử-dụng)  
   2.7. [Phạm vi MVP và giá trị sử dụng](#27-phạm-vi-mvp-và-giá-trị-sử-dụng)
3. [Giải pháp đề xuất](#3-giải-pháp-đề-xuất)  
   3.1. [Phần mềm](#31-phần-mềm)  
   &nbsp;&nbsp;&nbsp;&nbsp;3.1.1. [Danh sách các chức năng phần mềm](#311-danh-sách-các-chức-năng-phần-mềm)  
   &nbsp;&nbsp;&nbsp;&nbsp;3.1.2. [Kiến trúc tổng thể phần mềm](#312-kiến-trúc-tổng-thể-phần-mềm)  
   3.2. [Phần cứng](#32-phần-cứng)
4. [Kế hoạch phát triển](#4-kế-hoạch-phát-triển)  
   4.1. [Phân tích yêu cầu](#41-phân-tích-yêu-cầu)  
   4.2. [Thiết kế phần mềm](#42-thiết-kế-phần-mềm)  
   4.3. [Cài đặt (implement) phần mềm](#43-cài-đặt-implement-phần-mềm)  
   4.4. [Kiểm thử phần mềm](#44-kiểm-thử-phần-mềm)  
   4.5. [Triển khai, bảo trì](#45-triển-khai-bảo-trì)
5. [Kế hoạch nhân sự & chi phí](#5-kế-hoạch-nhân-sự--chi-phí)  
   5.1. [Cấu trúc nhân sự](#51-cấu-trúc-nhân-sự)  
   5.2. [Kế hoạch chi phí](#52-kế-hoạch-chi-phí)

---

# 1. Bảng đánh giá thành viên

| MSSV | Họ Tên | % đóng góp (tối đa 100%) | Chữ ký |
| :--- | :--- | :---: | :---: |
| 24120121 | Lê Quý Phúc | *Chờ đánh giá* | *(Bổ sung khi nộp)* |
| 24120503 | Phan Gia Phúc | *Chờ đánh giá* | *(Bổ sung khi nộp)* |
| 24120083 | Nguyễn Đức Lãm | *Chờ đánh giá* | *(Bổ sung khi nộp)* |
| 24120269 | Ngô Viết Thanh Bình | *Chờ đánh giá* | *(Bổ sung khi nộp)* |

*Tỷ lệ đóng góp và chữ ký sẽ được từng thành viên và nhóm trưởng xác nhận chính thức trước khi nộp đồ án.*

---

# 2. Phát biểu bài toán sơ lược

### 2.1. Bối cảnh và vấn đề đặt ra
Trong một đơn vị cung cấp sản phẩm, dịch vụ hoặc hỗ trợ học tập, người dùng thường cần hỏi về cách sử dụng hệ thống, báo lỗi hoặc tra cứu những quy định đã được công bố. Nếu yêu cầu được tiếp nhận qua nhiều kênh rời rạc, người dùng khó theo dõi tiến độ; người hỗ trợ khó xác định ai đang phụ trách; lịch sử trao đổi và cách xử lý cũng không được lưu trữ nhất quán. Khi tài liệu hướng dẫn phân tán ở nhiều tệp, nhân viên còn phải tự tìm thông tin và đối chiếu nguồn trước khi phản hồi.

Các mô hình ngôn ngữ lớn (LLM) có thể hỗ trợ diễn đạt câu trả lời, nhưng câu trả lời được sinh trực tiếp từ mô hình có nguy cơ thiếu căn cứ hoặc không phù hợp với quy định riêng của từng đơn vị. Vì vậy, nhóm không đặt mục tiêu xây dựng một chatbot trả lời tự động độc lập, mà kết hợp **quản lý yêu cầu hỗ trợ (ticket)** với **kho tri thức có kiểm duyệt (knowledge base)** để AI chỉ đưa ra *gợi ý* dựa trên tài liệu được phép sử dụng.

### 2.2. Ý tưởng giải pháp đề xuất
**AI-Powered Helpdesk & Knowledge Base** là ứng dụng web cho phép người dùng tạo và theo dõi ticket; nhân viên hỗ trợ tiếp nhận, trao đổi, phân công và xử lý yêu cầu theo một quy trình thống nhất; quản trị viên quản lý tài khoản nhân viên và tài liệu tri thức. Khi cần phản hồi, nhân viên có thể yêu cầu AI đề xuất nội dung dựa trên các đoạn tài liệu liên quan, kèm nguồn trích dẫn để kiểm tra. **Nhân viên luôn là người xem xét, chỉnh sửa và quyết định gửi phản hồi**; AI không tự gửi tin nhắn hoặc thay đổi trạng thái ticket.

Phạm vi sản phẩm bao gồm bốn nhóm chức năng chính: **Identity & Access**, **Ticket Management**, **Knowledge Base** và **AI Assistance**. Các chức năng được tổ chức thành một hệ thống thống nhất; thành phần AI là khả năng hỗ trợ bổ sung, không phải điều kiện để quy trình xử lý ticket hoạt động.

Một tình huống sử dụng điển hình: (1) quản trị viên tải lên tài liệu hướng dẫn và công bố sau khi xử lý; (2) khách hàng gửi ticket; (3) nhân viên nhận ticket từ hàng đợi; (4) nhân viên yêu cầu AI tìm căn cứ trong tài liệu và đề xuất câu trả lời; (5) nhân viên kiểm tra rồi gửi phản hồi; (6) ticket được chuyển sang đã giải quyết và khách hàng xác nhận đóng hoặc yêu cầu mở lại. Hệ thống lưu lịch sử các thay đổi quan trọng để phục vụ tra cứu.

### 2.3. Môi trường hoạt động dự kiến
- **Người dùng:** Truy cập bằng trình duyệt web hiện đại trên máy tính hoặc thiết bị di động (Chrome, Edge, Firefox, Safari); giao diện responsive, không yêu cầu cài ứng dụng riêng.
- **Máy chủ:** Backend Java 21 / Spring Boot cung cấp REST API; frontend React / TypeScript; PostgreSQL lưu dữ liệu nghiệp vụ và hỗ trợ truy xuất vector với pgvector; tài liệu gốc được lưu ở vùng lưu trữ riêng tư.
- **Tích hợp AI:** Dịch vụ tạo embedding và sinh ngôn ngữ qua API; có chế độ mock để kiểm thử hoặc trình diễn khi không có dịch vụ bên ngoài.
- **Triển khai:** Hướng đến môi trường Docker Compose, cấu hình qua biến môi trường và hướng dẫn chạy lại trên máy phát triển mới.

### 2.4. Ràng buộc thiết kế và triển khai
Để bảo đảm tính khả thi trong học kỳ, phiên bản đầu (MVP) chỉ phục vụ **một đơn vị** với ba vai trò **Customer, Agent, Admin**. Hệ thống tiếp nhận tài liệu PDF có văn bản, TXT và Markdown (tối đa 10 MiB/tệp); chưa hỗ trợ OCR cho PDF dạng ảnh. Dự án không phát triển ứng dụng di động native, microservices, tích hợp tổng đài hay AI agent tự xử lý ticket. Việc kiểm tra quyền truy cập được thực hiện tại backend; dữ liệu dùng để trình diễn là dữ liệu giả lập hoặc dữ liệu được phép sử dụng.

### 2.5. Mục tiêu và tiêu chí thành công

| Mã mục tiêu | Nội dung mục tiêu | Tiêu chí đánh giá / đo lường |
| :--- | :--- | :--- |
| **OBJ-01** | Người dùng gửi yêu cầu và theo dõi phản hồi qua giao diện web thống nhất. | Khách hàng tạo được ticket, nhận câu trả lời và xem lịch sử trao đổi. |
| **OBJ-02** | Phân quyền rõ ràng giữa Customer, Agent và Admin. | Kiểm thử phân quyền API: Customer chỉ xem dữ liệu của mình; Agent xử lý ticket được giao; Admin quản trị hệ thống. |
| **OBJ-03** | Quy trình tiếp nhận, phân công và đóng ticket được ghi nhận đầy đủ. | Lịch sử trạng thái ticket thể hiện đúng các mốc: tạo mới, gán nhân viên, phản hồi, giải quyết và đóng. |
| **OBJ-04** | Quản lý kho tài liệu và tìm kiếm đoạn nội dung liên quan theo ngữ nghĩa. | Tài liệu được tải lên, phân đoạn, tạo embedding và truy xuất được đoạn văn bản liên quan. |
| **OBJ-05** | AI đề xuất phản hồi có trích dẫn, đồng thời từ chối khi thiếu bằng chứng. | Kiểm tra nguồn trích dẫn bằng bộ câu hỏi đánh giá; thử các tình huống không có nguồn. |
| **OBJ-06** | Dự án có thể cài đặt lại, kiểm thử và truy vết đóng góp. | Docker Compose, README, kết quả kiểm thử, Git commit/PR và Jira. |

*Các tiêu chí trên là mục tiêu nghiệm thu của dự án, không phải kết quả đã được xác nhận.*

### 2.6. Đối tượng sử dụng

| Đối tượng | Vai trò và nhu cầu chính |
| :--- | :--- |
| **Guest (khách chưa đăng nhập)** | Truy cập chức năng đăng ký tài khoản Customer và đăng nhập. |
| **Customer (người yêu cầu hỗ trợ)** | Tạo ticket, xem ticket của mình, gửi phản hồi và theo dõi trạng thái; không xem ghi chú nội bộ. |
| **Agent (nhân viên hỗ trợ)** | Xem hàng đợi chưa phân công, nhận và xử lý ticket được giao; tra cứu tài liệu đã công bố và sử dụng gợi ý AI. |
| **Admin (quản trị viên)** | Quản lý tài khoản Agent, phân công ticket, quản lý và công bố tài liệu; giám sát hoạt động hỗ trợ theo quyền quản trị. |

Ngoài các vai trò người dùng, hệ thống có tiến trình xử lý tài liệu nền và sử dụng dịch vụ AI bên ngoài. Đây là **thành phần kỹ thuật**, không phải tài khoản người dùng có quyền độc lập trong hệ thống.

### 2.7. Phạm vi MVP và giá trị sử dụng
MVP tập trung vào bốn nhóm chức năng: (1) tài khoản và phân quyền; (2) quy trình ticket có trao đổi hai chiều; (3) quản lý kho tài liệu và tìm kiếm; (4) trợ lý AI gợi ý phản hồi có dẫn nguồn và bước duyệt của nhân viên. Sản phẩm được thiết kế để chứng minh một luồng sử dụng thực tế, tránh mở rộng sang các nghiệp vụ ít liên quan như CRM, thanh toán hoặc quản lý SLA phức tạp.

Giá trị kỳ vọng của hệ thống là **giúp người dùng theo dõi yêu cầu rõ ràng**, **giúp nhân viên tìm căn cứ nhanh hơn** và **giữ được trách nhiệm của con người đối với nội dung gửi đi**. Mức độ cải thiện thời gian xử lý hoặc chất lượng phản hồi chỉ được kết luận sau khi nhóm tiến hành đo đạc, không giả định sẵn.

---

# 3. Giải pháp đề xuất

## 3.1. Phần mềm

### 3.1.1. Danh sách các chức năng phần mềm
> *Ghi chú nguồn nguyên liệu:* Bảng câu chuyện người dùng (User Story) lý giải sự cần thiết và liệt kê danh sách chức năng cùng quy định liên quan. Tham khảo Mục 3.3, Mục 4, 5, 7 và **Phụ lục D** trong `reports/SRS-master.md`.

## Bảng đầy đủ
| STT | Nhu cầu | Yêu cầu | Tham chiếu | Mức |
|---:|---|---|---|---|
| 1 | Là khách chưa có tài khoản, tôi muốn đăng ký để gửi yêu cầu hỗ trợ. | Đăng ký tài khoản Customer bằng email, tên và mật khẩu; vai trò mặc định là Customer. | FR-ID-01, UC-01, BR-01 | P0 |
| 2 | Là người dùng đã có tài khoản, tôi muốn đăng nhập vào hệ thống. | Đăng nhập bằng email và mật khẩu; cấp access token và refresh token. | FR-ID-02/03, UC-01 | P0 |
| 3 | Là người dùng đã đăng nhập, tôi muốn giữ phiên làm việc và đăng xuất an toàn. | Làm mới token có xoay vòng; đăng xuất thu hồi phiên hiện tại. | FR-ID-04/05, UC-02 | P0 |
| 4 | Là người dùng đã đăng nhập, tôi muốn xem và cập nhật thông tin cá nhân. | Xem/sửa hồ sơ của chính mình; đổi mật khẩu có kiểm tra mật khẩu cũ. | FR-ID-06, UC-03 | P0 |
| 5 | Là quản trị viên, tôi muốn quản lý tài khoản nhân viên hỗ trợ. | Tạo Agent; vô hiệu hóa hoặc kích hoạt lại; tài khoản bị vô hiệu không đăng nhập mới được. | FR-ID-08, UC-04, BR-02/16 | P0 |
| 6 | Là quản trị viên, tôi muốn mỗi vai trò chỉ truy cập đúng dữ liệu được phép. | Phân quyền theo vai trò và theo quyền sở hữu, kiểm tra ở backend. | FR-ID-07, BR-03/04/14 | P0 |
| 7 | Là khách hàng, tôi muốn tạo yêu cầu hỗ trợ để được giúp đỡ. | Tạo ticket gồm tiêu đề và mô tả; hệ thống tạo mã ticket và tin nhắn công khai đầu tiên. | FR-TK-01, UC-05 | P0 |
| 8 | Là khách hàng, tôi muốn xem danh sách và tiến độ các ticket của mình. | Xem danh sách, chi tiết, trạng thái và các tin nhắn công khai; không thấy ghi chú nội bộ. | FR-TK-02/03, UC-06, BR-08 | P0 |
| 9 | Là khách hàng, tôi muốn bổ sung thông tin hoặc trả lời nhân viên trong ticket. | Gửi tin nhắn công khai; khi ticket đang chờ khách phản hồi thì trả lời sẽ chuyển ticket về đang xử lý. | FR-TK-06/08, UC-08/09, BR-07 | P0 |
| 10 | Là khách hàng, tôi muốn xác nhận đóng hoặc yêu cầu mở lại ticket đã giải quyết. | Đóng hoặc mở lại ticket từ trạng thái đã giải quyết. | FR-TK-08, BR-09, UC-09 | P0 |
| 11 | Là nhân viên hỗ trợ, tôi muốn xem hàng đợi và nhận ticket chưa phân công. | Xem ticket OPEN; nhận ticket nguyên tử, chỉ một người nhận được khi nhiều người nhận đồng thời. | FR-TK-04, BR-05/06, UC-07 | P0 |
| 12 | Là quản trị viên, tôi muốn phân công hoặc chuyển ticket cho nhân viên phù hợp. | Gán/chuyển Agent đang hoạt động; ghi lại người cũ và người mới. | FR-TK-05, UC-07, BR-15 | P0 |
| 13 | Là nhân viên được giao ticket, tôi muốn trao đổi công khai với khách hàng. | Gửi phản hồi công khai trên ticket được giao. | FR-TK-06, UC-08, BR-04/07 | P0 |
| 14 | Là nhân viên được giao ticket, tôi muốn ghi chú nội bộ. | Ghi chú nội bộ chỉ Agent được giao và Admin thấy. | FR-TK-07, BR-08, UC-08 | P0 |
| 15 | Là nhân viên được giao ticket, tôi muốn cập nhật trạng thái và mức ưu tiên. | Yêu cầu thêm thông tin, đánh dấu đã giải quyết; đặt ưu tiên LOW/NORMAL/HIGH; chuyển trạng thái theo quy trình, từ chối chuyển không hợp lệ. | FR-TK-08, UC-09; Gợi ý bổ sung FR về việc đặt ưu tiên cụ thể hơn là chỉ nêu ra trong Field MVP | P0 |
| 16 | Là nhân viên nhận ticket hoặc quản trị viên, tôi muốn xem lịch sử xử lý ticket. | Xem sự kiện nhận, phân công, đổi trạng thái (ai, lúc nào, làm gì). | FR-TK-09, BR-15, UC-10 | P0 |
| 17 | Là người dùng, tôi muốn tìm và lọc ticket nhanh. | Lọc theo trạng thái, người phụ trách, ngày tạo; phân trang và sắp xếp. | FR-TK-10, UC-06 | P0 |
| 18 | Là quản trị viên, tôi muốn đưa tài liệu chính sách vào kho tri thức. | Tải lên PDF văn bản, TXT, MD (≤ 10 MiB); hệ thống kiểm tra file và tạo tác vụ xử lý nền. | FR-KB-01/02, UC-11 | P0 |
| 19 | Là quản trị viên, tôi muốn biết tài liệu đã xử lý xong hay lỗi. | Theo dõi trạng thái UPLOADED/PROCESSING/READY/FAILED; thử lại có giới hạn khi lỗi. | FR-KB-03/04/05/09, UC-11 | P0 |
| 20 | Là quản trị viên, tôi muốn kiểm duyệt tài liệu trước khi AI được dùng. | Công bố tài liệu READY; lưu trữ (archive) tài liệu để AI không dùng nữa. | FR-KB-06/08, BR-11, UC-12 | P0 |
| 21 | Là nhân viên hoặc quản trị viên, tôi muốn tra cứu tài liệu đã công bố. | Tìm kiếm trong tài liệu đã công bố, hiển thị đoạn liên quan. | FR-KB-07, UC-13 | P0 |
| 22 | Là nhân viên nhận ticket, tôi muốn AI gợi ý câu trả lời có dẫn nguồn. | Truy xuất đoạn tài liệu liên quan, sinh bản nháp kèm trích dẫn đã được kiểm chứng. | FR-AI-01..05, BR-11/12, UC-14 | P0 |
| 23 | Là nhân viên, tôi muốn AI cho biết khi không đủ căn cứ. | Trả về "không đủ bằng chứng" thay vì tự bịa chính sách. | FR-AI-06, BR-13, UC-14 | P0 |
| 24 | Là nhân viên, tôi muốn giữ quyền kiểm soát nội dung gửi cho khách. | Xem, chỉnh sửa bản nháp rồi mới gửi thủ công; AI không tự gửi. | FR-AI-07, BR-10, UC-15 | P0 |
| 25 | Là nhân viên hoặc quản trị viên, tôi muốn xem lại các gợi ý AI đã tạo. | Lưu lịch sử gợi ý kèm ảnh chụp nguồn trích dẫn tại thời điểm tạo. | FR-AI-08, BR-12; Gợi ý bổ sung FR/UC về logging/interface cho các gợi ý của AI | P0 |
| 26 | Là nhân viên, tôi muốn hệ thống vẫn dùng được khi AI gặp sự cố. | AI lỗi/quá tải trả thông báo rõ; ticket vẫn tạo, xử lý, trả lời bình thường; giới hạn số lần gọi AI. | FR-AI-09, NFR-REL-01 | P0 |
| 27 | Là người dùng quên mật khẩu, tôi muốn đặt lại mật khẩu. | Đặt lại mật khẩu qua token dùng một lần có thời hạn. | FR-ID-09, UC-16 | P1 |
| 28 | Là quản trị viên, tôi muốn xem thống kê tổng quan. | Dashboard số ticket theo trạng thái và theo nhân viên. | FR-TK-12, UC-17 | P1 |
| 29 | Là khách hàng, tôi muốn đính kèm tệp vào ticket. | Tải tệp đính kèm có giới hạn và kiểm tra quyền tải xuống. | FR-TK-11; Gợi ý bổ sung UC về attactchment lúc Customer tạo/phản hồi ticket  | P1 |
| 30 | Là nhân viên, tôi muốn đánh giá chất lượng gợi ý của AI. | Đánh giá hữu ích/không hữu ích và thống kê chất lượng. | FR-AI-10; Gợi ý bổ sung UC về feedback/evaluation câu trả lời của AI từ Agent | P1 |

---
### Bảng thu gọn
| STT | Nhu cầu | Yêu cầu |
| --- | --- | --- |
| 1 | Là khách chưa có tài khoản, tôi muốn đăng ký để gửi yêu cầu hỗ trợ. | Đăng ký tài khoản Customer bằng email, tên và mật khẩu; vai trò mặc định là Customer. |
| 2 | Là người dùng đã có tài khoản, tôi muốn đăng nhập vào hệ thống. | Đăng nhập bằng email và mật khẩu; cấp access token và refresh token. |
| 3 | Là người dùng đã đăng nhập, tôi muốn giữ phiên làm việc và đăng xuất an toàn. | Làm mới token có xoay vòng; đăng xuất thu hồi phiên hiện tại. |
| 4 | Là người dùng đã đăng nhập, tôi muốn xem và cập nhật thông tin cá nhân. | Xem/sửa hồ sơ của chính mình; đổi mật khẩu có kiểm tra mật khẩu cũ. |
| 5 | Là quản trị viên, tôi muốn quản lý tài khoản nhân viên hỗ trợ. | Tạo Agent; vô hiệu hóa hoặc kích hoạt lại; tài khoản bị vô hiệu không đăng nhập mới được. |
| 6 | Là quản trị viên, tôi muốn mỗi vai trò chỉ truy cập đúng dữ liệu được phép. | Phân quyền theo vai trò và theo quyền sở hữu, kiểm tra ở backend. |
| 7 | Là khách hàng, tôi muốn tạo yêu cầu hỗ trợ để được giúp đỡ. | Tạo ticket gồm tiêu đề và mô tả; hệ thống tạo mã ticket và tin nhắn công khai đầu tiên. |
| 8 | Là khách hàng, tôi muốn xem danh sách và tiến độ các ticket của mình. | Xem danh sách, chi tiết, trạng thái và các tin nhắn công khai; không thấy ghi chú nội bộ. |
| 9 | Là khách hàng, tôi muốn bổ sung thông tin hoặc trả lời nhân viên trong ticket. | Gửi tin nhắn công khai; khi ticket đang chờ khách phản hồi thì trả lời sẽ chuyển ticket về đang xử lý. |
| 10 | Là khách hàng, tôi muốn xác nhận đóng hoặc yêu cầu mở lại ticket đã giải quyết. | Đóng hoặc mở lại ticket từ trạng thái đã giải quyết. |
| 11 | Là nhân viên hỗ trợ, tôi muốn xem hàng đợi và nhận ticket chưa phân công. | Xem ticket OPEN; nhận ticket nguyên tử, chỉ một người nhận được khi nhiều người nhận đồng thời. |
| 12 | Là quản trị viên, tôi muốn phân công hoặc chuyển ticket cho nhân viên phù hợp. | Gán/chuyển Agent đang hoạt động; ghi lại người cũ và người mới. |
| 13 | Là nhân viên được giao ticket, tôi muốn trao đổi công khai với khách hàng. | Gửi phản hồi công khai trên ticket được giao. |
| 14 | Là nhân viên được giao ticket, tôi muốn ghi chú nội bộ. | Ghi chú nội bộ chỉ Agent được giao và Admin thấy. |
| 15 | Là nhân viên được giao ticket, tôi muốn cập nhật trạng thái và mức ưu tiên. | Yêu cầu thêm thông tin, đánh dấu đã giải quyết; đặt ưu tiên LOW/NORMAL/HIGH; chuyển trạng thái theo quy trình, từ chối chuyển không hợp lệ. |
| 16 | Là nhân viên nhận ticket hoặc quản trị viên, tôi muốn xem lịch sử xử lý ticket. | Xem sự kiện nhận, phân công, đổi trạng thái (ai, lúc nào, làm gì). |
| 17 | Là người dùng, tôi muốn tìm và lọc ticket nhanh. | Lọc theo trạng thái, người phụ trách, ngày tạo; phân trang và sắp xếp. |
| 18 | Là quản trị viên, tôi muốn đưa tài liệu chính sách vào kho tri thức. | Tải lên PDF văn bản, TXT, MD (≤ 10 MiB); hệ thống kiểm tra file và tạo tác vụ xử lý nền. |
| 19 | Là quản trị viên, tôi muốn biết tài liệu đã xử lý xong hay lỗi. | Theo dõi trạng thái UPLOADED/PROCESSING/READY/FAILED; thử lại có giới hạn khi lỗi. |
| 20 | Là quản trị viên, tôi muốn kiểm duyệt tài liệu trước khi AI được dùng. | Công bố tài liệu READY; lưu trữ (archive) tài liệu để AI không dùng nữa. |
| 21 | Là nhân viên hoặc quản trị viên, tôi muốn tra cứu tài liệu đã công bố. | Tìm kiếm trong tài liệu đã công bố, hiển thị đoạn liên quan. |
| 22 | Là nhân viên nhận ticket, tôi muốn AI gợi ý câu trả lời có dẫn nguồn. | Truy xuất đoạn tài liệu liên quan, sinh bản nháp kèm trích dẫn đã được kiểm chứng. |
| 23 | Là nhân viên, tôi muốn AI cho biết khi không đủ căn cứ. | Trả về "không đủ bằng chứng" thay vì tự bịa chính sách. |
| 24 | Là nhân viên, tôi muốn giữ quyền kiểm soát nội dung gửi cho khách. | Xem, chỉnh sửa bản nháp rồi mới gửi thủ công; AI không tự gửi. |
| 25 | Là nhân viên hoặc quản trị viên, tôi muốn xem lại các gợi ý AI đã tạo. | Lưu lịch sử gợi ý kèm ảnh chụp nguồn trích dẫn tại thời điểm tạo. |
| 26 | Là nhân viên, tôi muốn hệ thống vẫn dùng được khi AI gặp sự cố. | AI lỗi/quá tải trả thông báo rõ; ticket vẫn tạo, xử lý, trả lời bình thường; giới hạn số lần gọi AI. |
| 27 | Là người dùng quên mật khẩu, tôi muốn đặt lại mật khẩu. | Đặt lại mật khẩu qua token dùng một lần có thời hạn. |
| 28 | Là quản trị viên, tôi muốn xem thống kê tổng quan. | Dashboard số ticket theo trạng thái và theo nhân viên. |
| 29 | Là khách hàng, tôi muốn đính kèm tệp vào ticket. | Tải tệp đính kèm có giới hạn và kiểm tra quyền tải xuống. |
| 30 | Là nhân viên, tôi muốn đánh giá chất lượng gợi ý của AI. | Đánh giá hữu ích/không hữu ích và thống kê chất lượng. |

*(Nội dung do `Phan Gia Phúc` biên soạn theo Jira `SCRUM-9`)*

### 3.1.2. Kiến trúc tổng thể phần mềm
> *Ghi chú nguồn nguyên liệu:* Trình bày kiến trúc tổng thể đáp ứng danh sách chức năng ở mục 3.1.1 (sơ đồ kiến trúc + giải thích các thành phần và luồng vận hành). Tham khảo Mục 9.1, 9.3, 9.4, 12.2 và **Phụ lục E** trong `reports/SRS-master.md`.

*(Nội dung do `Nguyễn Đức Lãm` biên soạn theo Jira `SCRUM-10`)*

## 3.2. Phần cứng

### 3.2.1. Yêu cầu phần cứng và môi trường vận hành (Hardware Requirements)

| Môi trường | Cấu hình/điều kiện dự kiến |
| :--- | :--- |
| **Thiết bị người dùng** | Máy tính, máy tính bảng hoặc điện thoại chạy Chrome/Edge/Firefox/Safari tương đối mới; RAM tối thiểu khoảng 4 GB; Internet ổn định; UI hỗ trợ màn hình điện thoại từ khoảng 360 px. |
| **Máy chủ demo — CPU/RAM** | Tối thiểu 2 vCPU, 4 GB RAM; khuyến nghị 4 vCPU, 8 GB RAM khi chạy backend, PostgreSQL và frontend cùng máy. |
| **Máy chủ demo — lưu trữ/hệ điều hành** | Khoảng 50 GB SSD; Linux hoặc hệ điều hành hỗ trợ Docker Engine và Docker Compose; dữ liệu tài liệu được lưu riêng tư. |
| **Kết nối dịch vụ AI** | Máy chủ có khả năng gọi API nhà cung cấp LLM/embedding qua mạng; nếu offline hoặc không có API key, sử dụng chế độ mock phù hợp demo. |
| **GPU** | Không yêu cầu GPU riêng nếu sử dụng mô hình AI qua API bên ngoài. |
| **Máy phát triển** | Windows/Linux/macOS; tối thiểu 8 GB RAM, khuyến nghị 16 GB; khoảng 40 GB dung lượng trống; JDK 21, Node.js LTS, Git, Docker và IDE. |

### 3.2.2. Các yêu cầu chất lượng và tiêu chí kiểm chứng (Bổ trợ NFR)

| Mã tham chiếu | Nhóm yêu cầu | Mục tiêu dự kiến / phương pháp xác minh |
| :--- | :--- | :--- |
| NFR-SEC-01, 02 | Bảo mật, phân quyền | Mật khẩu và refresh token không lưu ở dạng gốc; bí mật cấu hình ngoài mã nguồn; các API bảo vệ có kiểm thử vai trò/quyền sở hữu; Customer không xem được ghi chú `INTERNAL`. |
| NFR-SEC-03, 04 | An toàn dữ liệu đầu vào | Giới hạn tài liệu tải lên 10 MiB, kiểm tra định dạng và nội dung; truy vấn DB được tham số hóa; nội dung được truy xuất cho RAG được xem là dữ liệu không tin cậy. |
| NFR-PRIV-01 | Quyền riêng tư | Dùng dữ liệu demo giả lập; hạn chế thông tin cá nhân không cần thiết gửi đến dịch vụ LLM; không ghi log password, token hoặc API key. |
| NFR-REL-01 | Độ tin cậy | Khi nhà cung cấp AI lỗi hoặc hết thời gian phản hồi, chức năng tạo, xem và xử lý ticket vẫn hoạt động; kiểm thử bằng cách giả lập lỗi dịch vụ AI. |
| NFR-CONS-01, 02 | Tính nhất quán | Thử 20 lần tình huống hai Agent cùng nhận một ticket: mỗi lần chỉ một yêu cầu thành công; cập nhật trạng thái và bản ghi lịch sử cùng một transaction. |
| NFR-PERF-01 | Hiệu năng REST | Mục tiêu p95 dưới 800 ms cho API CRUD thông thường với 20 người dùng ảo, trên môi trường và dữ liệu kiểm thử được công bố. |
| NFR-PERF-02 | Thời gian sinh gợi ý | Mục tiêu p95 dưới 12 giây khi nhà cung cấp AI ổn định; có timeout và trạng thái lỗi rõ ràng. |
| NFR-PERF-03 | Xử lý tài liệu | Mục tiêu xử lý PDF văn bản khoảng 1 MiB trong 60 giây trên môi trường kiểm thử chuẩn; đo thực tế để xác định giới hạn. |
| NFR-AI-01, 02 | Chất lượng câu trả lời AI | Đánh giá ít nhất 30 câu hỏi; mục tiêu citation accuracy từ 90% trên tập có bằng chứng và tỷ lệ từ chối phù hợp từ 80% trên tập thiếu bằng chứng. |
| NFR-AI-03 | An toàn khi sử dụng AI | Dữ liệu nguồn không được điều khiển API nghiệp vụ; kiểm thử tình huống prompt injection từ nội dung tài liệu; AI không có quyền gửi phản hồi hay cập nhật ticket. |
| NFR-OBS-01 | Khả năng theo dõi | Ghi log có request ID, trạng thái xử lý tài liệu và độ trễ AI; thông tin nhạy cảm không được ghi log. |
| NFR-MAIN-01, NFR-TEST-01 | Bảo trì và kiểm thử | Phân chia module rõ; quản lý database migration; kiểm thử tự động cho phân quyền, workflow, concurrency, bộ lọc truy xuất; CI chạy trước khi merge. |
| NFR-DEPLOY-01 | Khả năng triển khai lại | Docker Compose, `.env.example`, dữ liệu demo và README đủ để một máy mới chạy hệ thống theo hướng dẫn. |
| NFR-UX-01 | Khả dụng giao diện | Giao diện responsive; các trạng thái đang tải, rỗng và lỗi có thông báo rõ ràng; các thao tác chính thực hiện trên trình duyệt hiện đại. |

---

# 4. Kế hoạch phát triển
> *Ghi chú nguồn nguyên liệu:* Trình bày cụ thể kế hoạch phát triển phần mềm qua 5 giai đoạn cùng thành phẩm cụ thể của từng giai đoạn. Tham khảo Mục 14, 15, 17, 21 và **Phụ lục G** trong `reports/SRS-master.md` (lấy chuẩn ngày tháng từ 28/09/2026 đến 13/12/2026).

*(Nội dung do `Nguyễn Đức Lãm` biên soạn theo Jira `SCRUM-10`)*

### 4.1. Phân tích yêu cầu
- Thời gian: 28/09/2026 – 11/10/2026
- Thành phẩm: Tài liệu đặc tả yêu cầu SRS v1.0, User stories, Danh mục Use cases.

### 4.2. Thiết kế phần mềm
- Thời gian: 12/10/2026 – 25/10/2026
- Thành phẩm: Kiến trúc hệ thống, ERD CSDL, Đặc tả API Contract, Wireframe UI.

### 4.3. Cài đặt (implement) phần mềm
- Thời gian: 26/10/2026 – 22/11/2026
- Thành phẩm: Mã nguồn Backend Spring Boot, Frontend React, PostgreSQL + pgvector, Module Auth, Ticket, KB, AI Gateway.

### 4.4. Kiểm thử phần mềm
- Thời gian: 23/11/2026 – 06/12/2026
- Thành phẩm: Test plan, Test cases, Báo cáo kết quả unit test / integration test / E2E test.

### 4.5. Triển khai, bảo trì
- Thời gian: 07/12/2026 – 13/12/2026
- Thành phẩm: Docker image, Hướng dẫn cài đặt triển khai (Deployment guide), Báo cáo tổng kết đồ án.

---

# 5. Kế hoạch nhân sự & chi phí
> *Ghi chú nguồn nguyên liệu:* Cấu trúc nhân sự toàn dự án và liệt kê các khoản chi phí dự kiến. Tham khảo Mục 16, 16.1, **Phụ lục H** và **Phụ lục I** trong `reports/SRS-master.md`.

*(Nội dung do `Ngô Viết Thanh Bình` biên soạn theo Jira `SCRUM-11`)*

### 5.1. Cấu trúc nhân sự
> *Ghi chú nguồn nguyên liệu:* Ma trận vai trò, mô tả trách nhiệm và người phụ trách. Tham khảo **Phụ lục H** trong `reports/SRS-master.md`.

### 5.2. Kế hoạch chi phí
> *Ghi chú nguồn nguyên liệu:* Bảng tổng hợp chi phí nhân sự, hạ tầng cloud, API LLM, công cụ và dự phòng rủi ro. Tham khảo **Phụ lục I** trong `reports/SRS-master.md`.

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. Đề cương môn học Nhập môn Công nghệ Phần mềm - HCMUS (Khoa CNTT).
2. Tài liệu đặc tả yêu cầu phần mềm: `reports/SRS-master.md`.
3. Mẫu hướng dẫn đề xuất đồ án (Template 0 - Project Proposal) của Giảng viên.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo cấu trúc khung Template 0 | SCRUM-6 |
| `1.0.0-draft` | 2026-10-19 | Lê Quý Phúc | Hoàn thiện bìa, Mục 1, Mục 2, Mục 3.2 theo phân công | SCRUM-8 |
| `1.0.1` | 2026-10-22 | Ngô Viết Thanh Bình | Chuẩn hóa mục lục khớp 100% template Word của Thầy và tích hợp đầy đủ nội dung SCRUM-8 | SCRUM-11 |
