# BÁO CÁO ĐỀ XUẤT ĐỒ ÁN (PROJECT PROPOSAL - TEMPLATE 0)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - Trường ĐH Khoa học Tự nhiên (HCMUS)

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Project Proposal - AI-Powered Helpdesk & Knowledge Base
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `24120121` - `Lê Quý Phúc`: Phụ trách Bìa, Mục 1, Mục 2, Mục 3.2
  - `24120503` - `Phan Gia Phúc`: Phụ trách Mục 3.1.1 (Bảng chức năng chi tiết)
  - `24120083` - `Nguyễn Đức Lãm`: Phụ trách Mục 3.1.2 (Luồng người dùng) và Mục 4 (Kiến trúc & Công nghệ)
  - `24120269` - `Ngô Viết Thanh Bình`: Phụ trách Mục 5.1 (WBS & Phân công) và Mục 5.2 (Kế hoạch Sprint) *(Nhóm trưởng)*
- **Phạm vi (Scope):** Đề xuất tổng quan, mục tiêu, phạm vi chức năng, kiến trúc kỹ thuật và kế hoạch triển khai của hệ thống Helpdesk thông minh tích hợp AI Knowledge Base.

---

## 1. GIỚI THIỆU ĐỀ TÀI VÀ BỐI CẢNH (PROBLEM STATEMENT & BACKGROUND)

### 1.1. Bối cảnh và vấn đề đặt ra

Trong một đơn vị cung cấp sản phẩm, dịch vụ hoặc hỗ trợ học tập, người dùng thường cần hỏi về cách sử dụng hệ thống, báo lỗi hoặc tra cứu những quy định đã được công bố. Nếu yêu cầu được tiếp nhận qua nhiều kênh rời rạc, người dùng khó theo dõi tiến độ; người hỗ trợ khó xác định ai đang phụ trách; lịch sử trao đổi và cách xử lý cũng không được lưu trữ nhất quán. Khi tài liệu hướng dẫn phân tán ở nhiều tệp, nhân viên còn phải tự tìm thông tin và đối chiếu nguồn trước khi phản hồi.

Các mô hình ngôn ngữ lớn (LLM) có thể hỗ trợ diễn đạt câu trả lời, nhưng câu trả lời được sinh trực tiếp từ mô hình có nguy cơ thiếu căn cứ hoặc không phù hợp với quy định riêng của từng đơn vị. Vì vậy, nhóm không đặt mục tiêu xây dựng một chatbot trả lời tự động độc lập, mà kết hợp **quản lý yêu cầu hỗ trợ (ticket)** với **kho tri thức có kiểm duyệt (knowledge base)** để AI chỉ đưa ra *gợi ý* dựa trên tài liệu được phép sử dụng.

### 1.2. Giải pháp đề xuất

**AI-Powered Helpdesk & Knowledge Base** là ứng dụng web cho phép người dùng tạo và theo dõi ticket; nhân viên hỗ trợ tiếp nhận, trao đổi, phân công và xử lý yêu cầu theo một quy trình thống nhất; quản trị viên quản lý tài khoản nhân viên và tài liệu tri thức. Khi cần phản hồi, nhân viên có thể yêu cầu AI đề xuất nội dung dựa trên các đoạn tài liệu liên quan, kèm nguồn trích dẫn để kiểm tra. **Nhân viên luôn là người xem xét, chỉnh sửa và quyết định gửi phản hồi**; AI không tự gửi tin nhắn hoặc thay đổi trạng thái ticket.

Phạm vi sản phẩm bao gồm bốn nhóm chức năng chính: **Identity & Access**, **Ticket Management**, **Knowledge Base** và **AI Assistance**. Các chức năng được tổ chức thành một hệ thống thống nhất; thành phần AI là khả năng hỗ trợ bổ sung, không phải điều kiện để quy trình xử lý ticket hoạt động.

Một tình huống sử dụng điển hình: (1) quản trị viên tải lên tài liệu hướng dẫn và công bố sau khi xử lý; (2) khách hàng gửi ticket; (3) nhân viên nhận ticket từ hàng đợi; (4) nhân viên yêu cầu AI tìm căn cứ trong tài liệu và đề xuất câu trả lời; (5) nhân viên kiểm tra rồi gửi phản hồi; (6) ticket được chuyển sang đã giải quyết và khách hàng xác nhận đóng hoặc yêu cầu mở lại. Hệ thống lưu lịch sử các thay đổi quan trọng để phục vụ tra cứu.

### 1.3. Môi trường hoạt động dự kiến

- **Người dùng:** Truy cập bằng trình duyệt web hiện đại trên máy tính hoặc thiết bị di động; giao diện responsive, không yêu cầu cài ứng dụng riêng.
- **Máy chủ:** Backend Java 21/Spring Boot cung cấp REST API; frontend React/TypeScript; PostgreSQL lưu dữ liệu nghiệp vụ và hỗ trợ truy xuất vector với pgvector; tài liệu gốc được lưu ở vùng lưu trữ riêng tư.
- **Tích hợp AI:** Dịch vụ tạo embedding và sinh ngôn ngữ qua API; có chế độ mock để kiểm thử hoặc trình diễn khi không có dịch vụ bên ngoài.
- **Triển khai:** Hướng đến môi trường Docker Compose, cấu hình qua biến môi trường và hướng dẫn chạy lại trên máy phát triển mới.

### 1.4. Giới hạn thiết kế và triển khai

Để bảo đảm tính khả thi trong học kỳ, phiên bản đầu (MVP) chỉ phục vụ **một đơn vị** với ba vai trò **Customer, Agent, Admin**. Hệ thống tiếp nhận tài liệu PDF có văn bản, TXT và Markdown (tối đa 10 MiB/tệp); chưa hỗ trợ OCR cho PDF dạng ảnh. Dự án không phát triển ứng dụng di động native, microservices, tích hợp tổng đài hay AI agent tự xử lý ticket. Việc kiểm tra quyền truy cập được thực hiện tại backend; dữ liệu dùng để trình diễn là dữ liệu giả lập hoặc dữ liệu được phép sử dụng.

### 1.5. Thông tin thành viên và đóng góp

| MSSV | Họ và tên | Vai trò phụ trách chính | % đóng góp | Chữ ký |
| :--- | :--- | :--- | :---: | :---: |
| 24120121 | Lê Quý Phúc | AI Assistance | *Chờ đánh giá* | *Bổ sung khi nộp* |
| 24120503 | Phan Gia Phúc | Knowledge Base | *Chờ đánh giá* | *Bổ sung khi nộp* |
| 24120083 | Nguyễn Đức Lãm | Ticket Management | *Chờ đánh giá* | *Bổ sung khi nộp* |
| 24120269 | Ngô Viết Thanh Bình | Identity & Access (Nhóm trưởng) | *Chờ đánh giá* | *Bổ sung khi nộp* |

*Bảng này phục vụ phần đánh giá thành viên trong mẫu gốc. Tỷ lệ đóng góp và chữ ký cần được từng thành viên/nhóm trưởng xác nhận trước khi nộp; không mặc định 100% khi chưa đánh giá.*

---

## 2. MỤC TIÊU DỰ ÁN VÀ ĐỐI TƯỢNG SỬ DỤNG (PROJECT OBJECTIVES & TARGET USERS)

### 2.1. Mục tiêu tổng quát

Xây dựng một hệ thống Helpdesk dạng web có thể sử dụng xuyên suốt từ lúc người dùng gửi yêu cầu đến khi yêu cầu được giải quyết, đồng thời thử nghiệm cách tích hợp AI theo mô hình **Retrieval-Augmented Generation (RAG)** để hỗ trợ nhân viên tìm thông tin và soạn phản hồi có dẫn nguồn. Sản phẩm hướng đến một quy trình rõ ràng, có kiểm soát quyền hạn, có khả năng kiểm thử và vận hành được ngay cả khi dịch vụ AI tạm thời không khả dụng.

### 2.2. Mục tiêu cụ thể và tiêu chí nghiệm thu dự kiến

| Mã | Mục tiêu | Cách kiểm chứng dự kiến |
| :--- | :--- | :--- |
| OBJ-01 | Khách hàng tạo, xem và theo dõi ticket của chính mình. | Demo luồng tạo ticket, phản hồi, xem trạng thái và kiểm tra quyền sở hữu. |
| OBJ-02 | Nhân viên nhận, xử lý và cập nhật ticket theo quy tắc trạng thái. | Kiểm thử các chuyển trạng thái hợp lệ/không hợp lệ và lịch sử xử lý. |
| OBJ-03 | Bảo đảm một ticket chưa phân công không bị hai nhân viên nhận thành công cùng lúc. | Integration test tạo hai yêu cầu nhận ticket đồng thời. |
| OBJ-04 | Quản trị viên đưa tài liệu vào kho tri thức và kiểm soát tài liệu được AI sử dụng. | Demo tải tài liệu, xử lý, công bố, lưu trữ và tìm kiếm. |
| OBJ-05 | AI đề xuất phản hồi có trích dẫn, đồng thời từ chối khi thiếu bằng chứng. | Kiểm tra nguồn trích dẫn bằng bộ câu hỏi đánh giá; thử các tình huống không có nguồn. |
| OBJ-06 | Dự án có thể cài đặt lại, kiểm thử và truy vết đóng góp. | Docker Compose, README, kết quả kiểm thử, Git commit/PR và Jira. |

*Các tiêu chí trên là mục tiêu nghiệm thu của dự án, không phải kết quả đã được xác nhận.*

### 2.3. Đối tượng sử dụng

| Đối tượng | Vai trò và nhu cầu chính |
| :--- | :--- |
| **Guest (khách chưa đăng nhập)** | Truy cập chức năng đăng ký tài khoản Customer và đăng nhập. |
| **Customer (người yêu cầu hỗ trợ)** | Tạo ticket, xem ticket của mình, gửi phản hồi và theo dõi trạng thái; không xem ghi chú nội bộ. |
| **Agent (nhân viên hỗ trợ)** | Xem hàng đợi chưa phân công, nhận và xử lý ticket được giao; tra cứu tài liệu đã công bố và sử dụng gợi ý AI. |
| **Admin (quản trị viên)** | Quản lý tài khoản Agent, phân công ticket, quản lý và công bố tài liệu; giám sát hoạt động hỗ trợ theo quyền quản trị. |

Ngoài các vai trò người dùng, hệ thống có tiến trình xử lý tài liệu nền và sử dụng dịch vụ AI bên ngoài. Đây là **thành phần kỹ thuật**, không phải tài khoản người dùng có quyền độc lập trong hệ thống.

### 2.4. Phạm vi MVP và giá trị sử dụng

MVP tập trung vào bốn nhóm chức năng: (1) tài khoản và phân quyền; (2) quy trình ticket có trao đổi hai chiều; (3) quản lý kho tài liệu và tìm kiếm; (4) trợ lý AI gợi ý phản hồi có dẫn nguồn và bước duyệt của nhân viên. Sản phẩm được thiết kế để chứng minh một luồng sử dụng thực tế, tránh mở rộng sang các nghiệp vụ ít liên quan như CRM, thanh toán hoặc quản lý SLA phức tạp.

Giá trị kỳ vọng của hệ thống là **giúp người dùng theo dõi yêu cầu rõ ràng**, **giúp nhân viên tìm căn cứ nhanh hơn** và **giữ được trách nhiệm của con người đối với nội dung gửi đi**. Mức độ cải thiện thời gian xử lý hoặc chất lượng phản hồi chỉ được kết luận sau khi nhóm tiến hành đo đạc, không giả định sẵn.

---

## 3. PHẠM VI VÀ ĐẶC TẢ YÊU CẦU (SCOPE & SPECIFICATIONS)

### 3.1. Yêu cầu chức năng (Functional Specifications)
#### 3.1.1. Bảng chức năng chi tiết (Functional Matrix)
> *Ghi chú nguồn nguyên liệu:* Tham khảo Phụ lục C trong `SRS-master.md` (Danh mục các tính năng của Module A: Auth, B: Ticket, C: Knowledge Base, D: AI).

*(Nội dung do `Phan Gia Phúc` biên soạn theo task Jira)*

#### 3.1.2. Luồng tương tác người dùng & Quy trình nghiệp vụ (User Flows & Workflows)
> *Ghi chú nguồn nguyên liệu:* Tham khảo Phụ lục D trong `SRS-master.md` (Quy trình tạo ticket, luồng AI đề xuất giải pháp, luồng gán nhân viên hỗ trợ).

*(Nội dung do `Nguyễn Đức Lãm` biên soạn theo task Jira)*

### 3.2. Yêu cầu phi chức năng (Non-Functional Requirements)

#### 3.2.1. Các yêu cầu chất lượng và tiêu chí kiểm chứng

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

#### 3.2.2. Yêu cầu phần cứng và môi trường vận hành (Hardware Requirements)

| Môi trường | Cấu hình/điều kiện dự kiến |
| :--- | :--- |
| **Thiết bị người dùng** | Máy tính, máy tính bảng hoặc điện thoại chạy Chrome/Edge/Firefox/Safari tương đối mới; RAM tối thiểu khoảng 4 GB; Internet ổn định; UI hỗ trợ màn hình điện thoại từ khoảng 360 px. |
| **Máy chủ demo — CPU/RAM** | Tối thiểu 2 vCPU, 4 GB RAM; khuyến nghị 4 vCPU, 8 GB RAM khi chạy backend, PostgreSQL và frontend cùng máy. |
| **Máy chủ demo — lưu trữ/hệ điều hành** | Khoảng 50 GB SSD; Linux hoặc hệ điều hành hỗ trợ Docker Engine và Docker Compose; dữ liệu tài liệu được lưu riêng tư. |
| **Kết nối dịch vụ AI** | Máy chủ có khả năng gọi API nhà cung cấp LLM/embedding qua mạng; nếu offline hoặc không có API key, sử dụng chế độ mock phù hợp demo. |
| **GPU** | Không yêu cầu GPU riêng nếu sử dụng mô hình AI qua API bên ngoài. |
| **Máy phát triển** | Windows/Linux/macOS; tối thiểu 8 GB RAM, khuyến nghị 16 GB; khoảng 40 GB dung lượng trống; JDK 21, Node.js LTS, Git, Docker và IDE. |

#### 3.2.3. Nguyên tắc đánh giá

Các chỉ số hiệu năng và chất lượng AI chỉ được đánh dấu **đạt/chưa đạt** sau khi nhóm chạy kiểm thử. Báo cáo kiểm thử cần ghi rõ cấu hình máy, phiên bản phần mềm, dữ liệu đầu vào, số lần chạy, cách đo và kết quả. Đối với các chỉ số liên quan dịch vụ AI bên ngoài, nhóm phải phân biệt lỗi do hệ thống và biến động từ nhà cung cấp.

---

## 4. KIẾN TRÚC HỆ THỐNG VÀ CÔNG NGHỆ DỰ KIẾN (SYSTEM ARCHITECTURE & TECH STACK)
> *Ghi chú nguồn nguyên liệu:* Tham khảo Mục 9.3 và Phụ lục F trong `SRS-master.md` (Kiến trúc phân tầng Backend Spring Boot, Frontend React, PostgreSQL + pgvector, AI Gateway/Mock).

*(Nội dung do `Nguyễn Đức Lãm` biên soạn theo task Jira)*

---

## 5. KẾ HOẠCH TRIỂN KHAI VÀ PHÂN CÔNG CÔNG VIỆC (IMPLEMENTATION & WORK BREAKDOWN)

### 5.1. Phân chia Module và WBS (Module Breakdown & Assignment)
> *Ghi chú nguồn nguyên liệu:* Tham khảo Phụ lục G trong `SRS-master.md` (Ma trận RACI, cấu trúc phân rã công việc WBS cho 4 thành viên A-B-C-D).

*(Nội dung do `Ngô Viết Thanh Bình` biên soạn theo task Jira)*

### 5.2. Kế hoạch Sprint và Mốc thời gian (Sprint Plan & Milestones)
> *Ghi chú nguồn nguyên liệu:* Tham khảo Phụ lục H trong `SRS-master.md` (Tiến độ môn học: Sprint 1 - Proposal & Kiến trúc; Sprint 2 - Core Services; Sprint 3 - AI & Tích hợp; Sprint 4 - Kiểm thử & Hoàn thiện).

*(Nội dung do `Ngô Viết Thanh Bình` biên soạn theo task Jira)*

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. Đề cương môn học Nhập môn Công nghệ Phần mềm - HCMUS (Khoa CNTT).
2. Tài liệu đặc tả yêu cầu phần mềm: `reports/SRS-master.md`.
3. Atlassian Scrum Guide & Best Practices trong quản lý dự án Jira.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo cấu trúc khung Template 0 | SCRUM-6 |
| `1.0.0-draft` | 2026-10-19 | Lê Quý Phúc | Hoàn thiện bìa, Mục 1, Mục 2, Mục 3.2 theo phân công; chờ nhóm review | SCRUM-8 |