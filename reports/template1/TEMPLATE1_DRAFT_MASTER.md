# BÁO CÁO PHÂN TÍCH YÊU CẦU PHẦN MỀM (REQUIREMENTS ANALYSIS SPECIFICATION)
## ĐỒ ÁN: AI-POWERED HELPDESK & KNOWLEDGE BASE SYSTEM
### Môn học: Nhập môn Công nghệ Phần mềm — Giảng viên: Khoa CNTT, Trường ĐH Khoa học Tự nhiên (HCMUS)
**Nhóm thực hiện: Nhóm 04**

---

# 1. BẢNG ĐÁNH GIÁ THÀNH VIÊN

| STT | MSSV | Họ và tên | Nhiệm vụ chính đảm nhiệm | Tỷ lệ đóng góp | Chữ ký |
| :---: | :---: | :--- | :--- | :---: | :---: |
| 1 | 24120269 | **Ngô Viết Thanh Bình** | **Trưởng nhóm** · Phụ trách Module D (Identity, Access Management & System Foundation, RBAC, CI/CD). Đặc tả Use Case UC-01, 02, 03, 04, 16. | 100% | *(Đã ký)* |
| 2 | 24120503 | **Phan Gia Phúc** | Phụ trách Module C (Ticket Management, State Machine & Concurrency Claim Lock). Đặc tả Use Case UC-05, 06, 07, 08, 09, 10. | 100% | *(Đã ký)* |
| 3 | 24120083 | **Nguyễn Đức Lãm** | Phụ trách Module B (Knowledge Base, Vector Embedding, Ingestion Worker & Search). Đặc tả Use Case UC-11, 12, 13. | 100% | *(Đã ký)* |
| 4 | 24120121 | **Lê Quý Phúc** | Phụ trách Module A (AI Assistance, RAG Pipeline, Human-in-the-loop, Analytics P1 & UI Prototype Lead). Đặc tả Use Case UC-14, 15, 17. | 100% | *(Đã ký)* |

---

# 2. PHÁT BIỂU BÀI TOÁN SƠ LƯỢC (PROBLEM STATEMENT)

## 2.1 Bối cảnh và Tính cấp thiết
Trong kỷ nguyên số, dịch vụ chăm sóc khách hàng và hỗ trợ kỹ thuật đóng vai trò sống còn đối với sự phát triển bền vững của doanh nghiệp. Tuy nhiên, các hệ thống Helpdesk truyền thống hiện nay đang đối mặt với những thách thức nghiêm trọng:
1. **Quá tải yêu cầu và thời gian phản hồi chậm:** Số lượng yêu cầu hỗ trợ (tickets) tăng trưởng theo cấp số nhân khiến đội ngũ nhân viên hỗ trợ (Support Agents) rơi vào tình trạng quá tải liên tục. Khách hàng phải chờ đợi hàng giờ, thậm chí nhiều ngày để nhận được câu trả lời cho các vấn đề lặp đi lặp lại.
2. **Cơ sở tri thức phân mảnh và thiếu đồng bộ:** Tài liệu hướng dẫn, quy trình vận hành và chính sách dịch vụ thường nằm rải rác ở nhiều định dạng (PDF, Word, Wiki, Google Docs), khiến nhân viên mất từ 30% đến 40% thời gian chỉ để tìm kiếm thông tin đối soát trước khi trả lời.
3. **Hiện tượng "Ảo giác" (Hallucination) và Thiếu tin cậy của AI sinh (Generative AI):** Nhiều tổ chức nôn nóng ứng dụng Chatbot AI tự động nhưng phải gánh chịu rủi ro pháp lý và uy tín do mô hình AI tự bịa đặt chính sách bảo hành, hoàn tiền hoặc cung cấp giải pháp kỹ thuật sai lệch mà không có cơ chế đối soát nguồn gốc dữ liệu.

## 2.2 Mục tiêu và Giải pháp đề xuất
Đề tài **"AI-Powered Helpdesk & Knowledge Base System" (Nhóm 04)** được nghiên cứu và xây dựng nhằm mang đến một giải pháp toàn diện, cân bằng giữa hiệu suất xử lý tự động và độ an toàn nghiệp vụ tối đa:
- **Tập trung hóa quy trình quản lý Ticket:** Xây dựng máy trạng thái hữu hạn (State Machine) chặt chẽ cho toàn bộ vòng đời của ticket (`OPEN` $\to$ `IN_PROGRESS` $\to$ `WAITING_CUSTOMER` $\to$ `RESOLVED` $\to$ `CLOSED`), hỗ trợ cơ chế giải quyết xung đột nhận việc đồng thời (**Concurrency Claim Lock**) bằng khóa lạc quan (Optimistic Locking).
- **Hệ thống Quản trị tri thức thông minh (Knowledge Ingestion & Vector Search):** Tự động hóa quy trình trích xuất văn bản từ tài liệu PDF/Markdown/Text, phân đoạn ngữ nghĩa (Semantic Chunking) và lưu trữ vector đa chiều trong PostgreSQL thông qua phần mở rộng `pgvector`.
- **Trợ lý AI hỗ trợ nhân viên (AI Copilot with Human-in-the-Loop):** Ứng dụng mô hình RAG (Retrieval-Augmented Generation) để tự động phân tích ngữ cảnh ticket, truy xuất chính xác các phân đoạn tri thức đã được kiểm duyệt và tạo bản thảo câu trả lời có **dẫn chứng nguồn gốc (Citations)** rõ ràng. **Nguyên tắc bất biến:** AI không bao giờ tự ý gửi tin nhắn ra ngoài hoặc thay đổi trạng thái ticket; bản nháp AI bắt buộc phải được nhân viên hỗ trợ kiểm tra, chỉnh sửa và chủ động bấm gửi.

## 2.3 Đối tượng sử dụng và Môi trường vận hành
Hệ thống phục vụ 4 nhóm đối tượng chính:
1. **Khách hàng (Customer):** Gửi yêu cầu hỗ trợ, theo dõi tiến độ xử lý và phản hồi trực tiếp trên giao diện web thân thiện.
2. **Nhân viên hỗ trợ (Support Agent):** Làm việc tập trung trên giao diện "Bàn làm việc yên tĩnh" (Quiet Workspace), nhận xử lý ticket, ghi chú nội bộ, tra cứu tri thức và sử dụng trợ lý AI.
3. **Tác giả tri thức (Knowledge Author / Agent cấp cao):** Soạn thảo, tải lên và cập nhật các bài viết cẩm nang, tài liệu chính sách.
4. **Quản trị viên hệ thống (Administrator):** Quản lý tài khoản, phân quyền, cấu hình hệ thống, kiểm duyệt xuất bản tri thức và xem báo cáo phân tích hiệu suất.

**Môi trường vận hành kỹ thuật:**
- **Kiến trúc phần mềm:** Modular Monolith (Spring Boot 3, Java 21) dễ dàng mở rộng và bảo trì.
- **Cơ sở dữ liệu:** PostgreSQL 16 tích hợp extension `pgvector` phục vụ tìm kiếm tương đồng vector (Cosine Distance).
- **Giao diện người dùng:** Ứng dụng web Single Page Application (React, TypeScript, Tailwind CSS), thiết kế chuẩn WCAG 2.1 AA hỗ trợ Responsive đa thiết bị (Desktop, Tablet, Mobile) và chế độ Dark/Light Mode.
- **Hạ tầng triển khai:** Đóng gói Docker Container, quy trình CI/CD tự động qua GitHub Actions.

---

# 3. TỔNG QUAN YÊU CẦU HỆ THỐNG

## 3.1 Danh sách các Stakeholder & Tác nhân (Actors)

### 3.1.1 Bảng danh sách các bên liên quan (Stakeholders)
| STT | Stakeholder | Vai trò & Trách nhiệm đối với hệ thống |
| :---: | :--- | :--- |
| 1 | **Chủ đầu tư / Ban Giám đốc** | Đưa ra mục tiêu chiến lược, kỳ vọng giảm 50% thời gian xử lý ticket lặp lại và nâng cao chỉ số hài lòng khách hàng (CSAT). |
| 2 | **Khách vãng lai (Guest)** | Người dùng ngoài hệ thống, truy cập trang đăng nhập hoặc tự đăng ký tài khoản khách hàng mới. |
| 3 | **Khách hàng (Customer)** | Tạo yêu cầu hỗ trợ, bổ sung thông tin, nhận câu trả lời công khai và quyết định đóng hoặc mở lại ticket. |
| 4 | **Nhân viên hỗ trợ (Support Agent)** | Tiếp nhận ticket từ hàng đợi, tương tác với khách hàng, trao đổi ghi chú nội bộ và khai thác gợi ý từ trợ lý AI. |
| 5 | **Quản trị viên (System Administrator)** | Quản lý vòng đời tài khoản nhân viên, kiểm duyệt xuất bản bài viết tri thức, phân công ticket và giám sát toàn hệ thống. |
| 6 | **Nhà cung cấp dịch vụ AI (OpenAI API / Cloud LLM)** | Dịch vụ ngoài cung cấp mô hình ngôn ngữ lớn (LLM) và Text Embedding; là hệ thống ngoại vi, không có quyền can thiệp vào DB nội bộ. |

### 3.1.2 Sơ đồ bối cảnh hệ thống (Context Diagram)
Hệ thống Helpdesk Knowledge Base nằm ở vị trí trung tâm, tiếp nhận yêu cầu từ Customer, Agent và Admin thông qua giao thức HTTPS bảo mật; đồng thời kết nối an toàn với AI Provider bên ngoài qua REST API để thực hiện tác vụ sinh câu trả lời có kiểm soát.

---

## 3.2 Danh sách các yêu cầu

### 3.2.1 Ma trận Yêu cầu chức năng (41 FRs) ↔ User Stories (30 USs) ↔ Use Case (17 UCs)

#### Nhóm 1: Quản lý Định danh & Phân quyền (Module D — Phụ trách: Ngô Viết Thanh Bình)
| Mã FR | Yêu cầu chức năng (FR) | Mã Story | Nội dung User Story (US) | Use Case liên quan | Mức độ |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-ID-01** | Đăng ký tài khoản Customer bằng email, họ tên, mật khẩu. | **US-01** | Là khách, tôi muốn đăng ký tài khoản để gửi yêu cầu hỗ trợ. | UC-01 | P0 |
| **FR-ID-02** | Đăng nhập hệ thống bằng email và mật khẩu. | **US-02** | Là người dùng, tôi muốn đăng nhập an toàn vào hệ thống. | UC-01 | P0 |
| **FR-ID-03** | Mã hóa băm mật khẩu an toàn bằng BCrypt/Argon2. | **US-02** | Hệ thống phải đảm bảo mật khẩu không bao giờ lưu dưới dạng bản rõ. | UC-01 | P0 |
| **FR-ID-04** | Cấp phát và xoay vòng Refresh Token (Token Rotation). | **US-03** | Là người dùng, tôi muốn duy trì phiên làm việc liên tục mà không phải đăng nhập lại nhiều lần. | UC-02 | P0 |
| **FR-ID-05** | Đăng xuất và thu hồi Refresh Token trên thiết bị. | **US-03** | Là người dùng, tôi muốn đăng xuất an toàn để kết thúc phiên làm việc. | UC-02 | P0 |
| **FR-ID-06** | Xem và cập nhật thông tin hồ sơ cá nhân; đổi mật khẩu. | **US-04** | Là người dùng, tôi muốn đổi thông tin cá nhân và mật khẩu khi cần. | UC-03 | P0 |
| **FR-ID-07** | Phân quyền truy cập dựa trên vai trò (RBAC) và quyền sở hữu (Ownership). | **US-06** | Là quản trị viên, tôi muốn kiểm soát quyền truy cập tài nguyên nghiêm ngặt. | UC-01, 04, 06 | P0 |
| **FR-ID-08** | Quản trị viên tạo tài khoản, khóa hoặc mở khóa tài khoản Agent. | **US-05** | Là quản trị viên, tôi muốn quản lý danh sách nhân sự hỗ trợ. | UC-04 | P0 |
| **FR-ID-09** | Khôi phục mật khẩu thông qua mã xác thực một lần (Reset Token). | **US-27** | Là người dùng quên mật khẩu, tôi muốn đặt lại mật khẩu an toàn. | UC-16 | P1 |

#### Nhóm 2: Quản lý Ticket & Phân luồng hỗ trợ (Module C — Phụ trách: Phan Gia Phúc)
| Mã FR | Yêu cầu chức năng (FR) | Mã Story | Nội dung User Story (US) | Use Case liên quan | Mức độ |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-TK-01** | Customer tạo ticket mới gồm tiêu đề, mô tả và tệp đính kèm. | **US-07** | Là khách hàng, tôi muốn gửi ticket để yêu cầu bộ phận hỗ trợ xử lý. | UC-05 | P0 |
| **FR-TK-02** | Xem danh sách ticket được phân quyền theo vai trò. | **US-08, 11** | Là người dùng, tôi muốn thấy danh sách ticket thuộc phạm vi của mình. | UC-06 | P0 |
| **FR-TK-03** | Xem chi tiết tiến trình xử lý và luồng trao đổi trong ticket. | **US-08** | Là người dùng, tôi muốn xem toàn bộ lịch sử tin nhắn của ticket. | UC-06 | P0 |
| **FR-TK-04** | Agent tiếp nhận (Claim) ticket chưa phân công từ hàng đợi OPEN. | **US-11** | Là Agent, tôi muốn nhận xử lý ticket OPEN một cách tức thời, không bị trùng. | UC-07 | P0 |
| **FR-TK-05** | Admin chỉ định hoặc chuyển giao ticket cho Agent khác xử lý. | **US-12** | Là Admin, tôi muốn phân công ticket cho nhân viên phù hợp nhất. | UC-07 | P0 |
| **FR-TK-06** | Gửi phản hồi tin nhắn công khai (Public Message). | **US-09, 13** | Là Customer/Agent, tôi muốn trao đổi công khai để giải quyết vấn đề. | UC-08 | P0 |
| **FR-TK-07** | Thêm ghi chú nội bộ (Internal Note) chỉ dành riêng cho Agent/Admin. | **US-14** | Là Agent, tôi muốn ghi chú nghiệp vụ bí mật mà khách hàng không thấy. | UC-08 | P0 |
| **FR-TK-08** | Chuyển đổi trạng thái ticket tuân thủ nghiêm ngặt State Machine. | **US-10, 15** | Là người dùng, tôi muốn cập nhật trạng thái ticket theo đúng luồng xử lý. | UC-09 | P0 |
| **FR-TK-09** | Ghi nhận nhật ký kiểm toán và chuỗi sự kiện ticket (Audit Trail). | **US-16** | Là Admin/Agent, tôi muốn kiểm tra ai đã làm gì vào thời điểm nào trên ticket. | UC-10 | P0 |
| **FR-TK-10** | Bộ lọc, tìm kiếm và phân trang danh sách ticket. | **US-17** | Là người dùng, tôi muốn tìm kiếm ticket nhanh theo trạng thái, người nhận. | UC-06 | P0 |
| **FR-TK-11** | Hỗ trợ tải tệp đính kèm tài liệu, ảnh chụp lỗi màn hình (P1). | **US-29** | Là khách hàng, tôi muốn gửi kèm ảnh chụp lỗi để Agent dễ hiểu bài toán. | UC-05 | P1 |
| **FR-TK-12** | Bảng điều khiển thống kê tổng quan ticket (Analytics P1). | **US-28** | Là Admin, tôi muốn xem biểu đồ số lượng ticket theo trạng thái và năng suất. | UC-17 | P1 |

#### Nhóm 3: Quản lý Cơ sở tri thức - Knowledge Base (Module B — Phụ trách: Nguyễn Đức Lãm)
| Mã FR | Yêu cầu chức năng (FR) | Mã Story | Nội dung User Story (US) | Use Case liên quan | Mức độ |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-KB-01** | Admin/Author tải lên tệp tài liệu định dạng PDF, TXT, MD ($\le 10$ MB). | **US-18** | Là quản trị viên, tôi muốn nạp tài liệu hướng dẫn vào hệ thống. | UC-11 | P0 |
| **FR-KB-02** | Lưu trữ tệp an toàn và tạo tác vụ xử lý nền (Async Ingestion Job). | **US-18** | Hệ thống phải ghi nhận tác vụ nạp tri thức mà không làm nghẽn giao diện. | UC-11 | P0 |
| **FR-KB-03** | Tiến trình nền (Worker) trích xuất văn bản từ tệp nguồn. | **US-19** | Hệ thống tự động đọc văn bản và báo lỗi nếu gặp file scan không có chữ. | UC-11 | P0 |
| **FR-KB-04** | Phân mảnh văn bản (Chunking) và tạo Vector Embeddings đa chiều. | **US-19** | Hệ thống phải cắt nhỏ tài liệu và nhúng vector vào PostgreSQL pgvector. | UC-11 | P0 |
| **FR-KB-05** | Quản lý trạng thái xử lý tài liệu (`UPLOADED` $\to$ `PROCESSING` $\to$ `READY`/`FAILED`). | **US-19** | Là Admin, tôi muốn biết tài liệu nào đã xử lý xong, tài liệu nào bị lỗi. | UC-11 | P0 |
| **FR-KB-06** | Admin kiểm duyệt và xuất bản tài liệu (`PUBLISH`). | **US-20** | Là Admin, tôi muốn chủ động xuất bản tài liệu READY để AI được phép dùng. | UC-12 | P0 |
| **FR-KB-07** | Tìm kiếm tri thức kết hợp từ khóa ngữ văn và tìm kiếm tương đồng vector. | **US-21** | Là Agent, tôi muốn tra cứu nhanh các giải pháp tương đồng trong kho tri thức. | UC-13 | P0 |
| **FR-KB-08** | Lưu trữ (Archive) tài liệu đã lỗi thời khỏi phạm vi truy xuất AI. | **US-20** | Là Admin, tôi muốn ẩn các chính sách cũ để AI không lấy nhầm dữ liệu. | UC-12 | P0 |
| **FR-KB-09** | Xem danh mục toàn bộ tài liệu tri thức kèm phân trang và lọc trạng thái. | **US-19** | Là Admin, tôi muốn quản trị danh mục tri thức trực quan. | UC-11 | P0 |
| **FR-KB-10** | Đánh giá độ hữu ích của bài viết tri thức (Feedback Helpful/Not Helpful). | **US-30** | Là Agent/Khách hàng, tôi muốn đánh giá bài viết có thực sự hữu ích không. | UC-12 | P1 |

#### Nhóm 4: Trợ lý AI & Phân tích giải pháp thông minh (Module A — Phụ trách: Lê Quý Phúc)
| Mã FR | Yêu cầu chức năng (FR) | Mã Story | Nội dung User Story (US) | Use Case liên quan | Mức độ |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **FR-AI-01** | Agent yêu cầu AI phân tích ticket và gợi ý bản thảo câu trả lời (Suggest Reply). | **US-22** | Là Agent, tôi muốn AI đề xuất câu trả lời chuẩn xác dựa trên tài liệu. | UC-14 | P0 |
| **FR-AI-02** | Trích xuất ngữ cảnh ticket an toàn (bảo vệ quyền riêng tư PII, bỏ Internal Notes). | **US-22** | Hệ thống đảm bảo không bao giờ gửi ghi chú nội bộ cho mô hình AI bên ngoài. | UC-14 | P0 |
| **FR-AI-03** | Truy xuất các đoạn tri thức (Chunks) tương đồng qua pgvector Cosine Similarity. | **US-22** | AI chỉ được phép tham khảo tài liệu đã được kiểm duyệt và công bố. | UC-14 | P0 |
| **FR-AI-04** | Tạo câu trả lời có cấu trúc, phân biệt rõ ràng câu lệnh hệ thống với ngữ cảnh. | **US-22** | Câu trả lời AI phải mạch lạc, bám sát vấn đề của khách hàng. | UC-14 | P0 |
| **FR-AI-05** | Xác thực trích dẫn nguồn (Citation Validation) và chụp ảnh tức thời (Snapshot). | **US-22** | Bản thảo AI phải đính kèm link/ID đoạn tri thức dẫn chứng cụ thể. | UC-14 | P0 |
| **FR-AI-06** | Cơ chế từ chối trả lời an toàn khi thiếu chứng cứ (`INSUFFICIENT_EVIDENCE`). | **US-23** | Khi không có tài liệu liên quan, AI phải từ chối thay vì tự bịa câu trả lời. | UC-14 | P0 |
| **FR-AI-07** | Cơ chế Human-in-the-loop: Agent toàn quyền xem, sửa bản nháp trước khi bấm gửi. | **US-24** | AI không bao giờ tự ý gửi tin nhắn; chỉ Agent mới có quyền gửi cho khách. | UC-15 | P0 |
| **FR-AI-08** | Ghi nhật ký yêu cầu AI, bản nháp, trạng thái áp dụng và nguồn trích dẫn. | **US-25** | Hệ thống lưu vết chi tiết để kiểm toán độ tin cậy của mô hình AI. | UC-14, 15 | P0 |
| **FR-AI-09** | Xử lý lỗi ngoại lệ khi AI Provider bị quá tải, timeout hoặc hết hạn ngạch. | **US-26** | Khi AI gặp sự cố, hệ thống vẫn hoạt động bình thường, không làm gián đoạn ticket. | UC-14 | P0 |
| **FR-AI-10** | Tự động phân loại danh mục và đề xuất độ ưu tiên cho ticket (Ticket Auto-Triage). | **US-22** | Là Agent/Admin, tôi muốn AI gợi ý phân loại đúng phòng ban xử lý. | UC-14 | P1 |

---

### 3.2.2 Đặc tả Yêu cầu phi chức năng (Non-Functional Requirements - NFRs)

| Mã NFR | Phân loại | Tiêu chí yêu cầu chi tiết | Chỉ số đo lường (Metric) |
| :--- | :--- | :--- | :--- |
| **NFR-PERF-01** | Hiệu năng | Thời gian phản hồi cho các thao tác giao dịch CRUD cơ bản (tạo ticket, nhận ticket, gửi tin nhắn). | $\le 1.0$ giây trong điều kiện tải bình thường ($95^{th}$ percentile). |
| **NFR-PERF-02** | Hiệu năng | Thời gian tìm kiếm tương đồng vector trên kho tri thức qua `pgvector`. | $\le 500$ ms cho kho dữ liệu dưới 100.000 chunks vector. |
| **NFR-PERF-03** | Hiệu năng | Thời gian sinh gợi ý bản nháp AI (bao gồm truy xuất vector + gọi LLM API). | $\le 5.0$ giây (có thanh tiến trình / spinner thông báo trạng thái trên UI). |
| **NFR-SEC-01** | Bảo mật | Mã hóa mật khẩu người dùng trong cơ sở dữ liệu. | Thuật toán BCrypt với độ phức tạp $cost \ge 12$ hoặc Argon2id. |
| **NFR-SEC-02** | Bảo mật | Quản lý phiên làm việc bằng JSON Web Token (JWT). | Access Token có thời hạn 15 phút; Refresh Token 7 ngày có cơ chế xoay vòng. |
| **NFR-SEC-03** | Bảo mật | Phân tách ranh giới dữ liệu và bảo vệ ghi chú nội bộ (Data Isolation). | Không bao giờ trả dữ liệu `INTERNAL_NOTE` qua API cho vai trò Customer. |
| **NFR-SEC-04** | Bảo mật | Toàn bộ đường truyền mạng giữa Client và Backend Server phải được bảo vệ. | Giao thức HTTPS / TLS 1.3 bắt buộc trong môi trường triển khai thực tế. |
| **NFR-REL-01** | Độ tin cậy | Độ sẵn sàng hoạt động của hệ thống (System Availability). | Đạt tối thiểu $99.5\%$ thời gian hoạt động; cơ chế Fallback an toàn khi AI lỗi. |
| **NFR-REL-02** | Độ tin cậy | Toàn vẹn dữ liệu giao dịch và tính nhất quán khi nhận việc đồng thời. | Đảm bảo tính ACID; áp dụng khóa lạc quan `@Version` chống mất dữ liệu (Lost Update). |
| **NFR-USE-01** | Tính khả dụng | Khả năng tiếp cận và thân thiện người dùng trên giao diện web. | Đạt chuẩn **WCAG 2.1 AA**; hỗ trợ đầy đủ Desktop, Tablet và Mobile. |
| **NFR-USE-02** | Tính khả dụng | Hỗ trợ chuyển đổi giao diện nền Sáng / Tối (Light Mode / Dark Mode). | Lưu tùy chọn vào LocalStorage; thời gian đổi theme diễn ra tức thời ($\le 100$ ms). |
| **NFR-MAINT-01** | Bảo trì | Cấu trúc mã nguồn module hóa, dễ dàng kiểm thử và mở rộng. | Kiến trúc Modular Monolith; độ bao phủ kiểm thử tự động (Unit Test Coverage) $\ge 80\%$. |

---

# 4. PHÂN TÍCH YÊU CẦU (USE CASE MODEL & SPECIFICATIONS)

## 4.1 Mô hình Use Case (Use Case Model)

### 4.1.0 Sơ đồ Use Case Tổng thể Hệ thống
Hệ thống Helpdesk Knowledge Base gồm 17 Use Case nghiệp vụ chính được phân bổ vào 4 phân hệ liên kết chặt chẽ:
- **Phân hệ D (Identity & Access Management):** Đảm bảo an toàn định danh và phân quyền.
- **Phân hệ C (Ticket Management & Routing):** Vận hành luồng xử lý yêu cầu cốt lõi.
- **Phân hệ B (Knowledge Base Management):** Quản trị kho tài liệu và tri thức số.
- **Phân hệ A (AI Assistance & Analytics):** Hỗ trợ trí tuệ nhân tạo tăng tốc độ xử lý.

*(Chèn Sơ đồ Use Case Tổng thể: `reports/template1/assets/diagrams/use-case-overall.svg`)*

### 4.1.1 Sơ đồ Use Case Phân hệ D — Quản lý Định danh & Người dùng
*(Chèn Sơ đồ Use Case Phân hệ D: `reports/template1/assets/diagrams/uc_module_d_identity.svg` / `uc_module_d_identity.drawio`)*

### 4.1.2 Sơ đồ Use Case Phân hệ C — Quản lý Ticket & Phân luồng hỗ trợ
*(Chèn Sơ đồ Use Case Phân hệ C: `reports/template1/assets/diagrams/use-case-module-c.svg`)*

### 4.1.3 Sơ đồ Use Case Phân hệ B — Quản lý Cơ sở tri thức (Knowledge Base)
*(Chèn Sơ đồ Use Case Phân hệ B: `reports/template1/assets/diagrams/use-case-module-b.svg`)*

### 4.1.4 Sơ đồ Use Case Phân hệ A — Trợ lý AI & Báo cáo thống kê
*(Chèn Sơ đồ Use Case Phân hệ A: `reports/template1/assets/diagrams/use-case-module-a.svg`)*

---

## 4.2 Đặc tả Use Case chi tiết

---

### 4.2.1. Đăng ký & Đăng nhập hệ thống [UC-01]
*(Thành viên phụ trách: Ngô Viết Thanh Bình — Module D: Identity & Access)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-01** |
| **Tên Use Case** | **Đăng ký tài khoản và Đăng nhập hệ thống** |
| **Tóm tắt** | Cho phép khách vãng lai (Guest) đăng ký tài khoản khách hàng mới bằng email/mật khẩu, hoặc người dùng đã có tài khoản thực hiện xác thực đăng nhập để nhận mã thông báo truy cập (Access Token & Refresh Token). |
| **Tác nhân** | Khách chưa có tài khoản khi đăng ký (Guest / Unauthenticated User).<br>Customer, Support Agent, System Administrator ở trạng thái chưa xác thực phiên khi đăng nhập. |
| **Điều kiện tiên quyết** | - Thiết bị người dùng có kết nối mạng Internet và truy cập được ứng dụng web.<br>- Đối với đăng nhập: Tài khoản đã được tạo và đang ở trạng thái kích hoạt (`enabled = true`). |
| **Kết quả** | - Đăng ký: Tài khoản mới được ghi nhận trong cơ sở dữ liệu với vai trò mặc định là `CUSTOMER`.<br>- Đăng nhập: Cấp phát cặp Access Token (JWT 15 phút) và Refresh Token (7 ngày), chuyển hướng người dùng đến màn hình làm việc tương ứng với vai trò. |
| **Kịch bản chính** | **Kịch bản A: Đăng ký tài khoản mới**<br>1. Người dùng chọn liên kết "Đăng ký tài khoản" trên giao diện.<br>2. Hệ thống hiển thị biểu mẫu đăng ký yêu cầu nhập: Họ tên, Email, Mật khẩu và Xác nhận mật khẩu.<br>3. Người dùng điền đầy đủ thông tin và bấm nút "Đăng ký".<br>4. Hệ thống kiểm tra định dạng email, độ mạnh mật khẩu và đối soát tính duy nhất của email trong DB.<br>5. Hệ thống thực hiện băm mật khẩu bằng BCrypt, gán vai trò mặc định là `ROLE_CUSTOMER` (Quy tắc BR-01).<br>6. Hệ thống lưu tài khoản vào cơ sở dữ liệu và hiển thị thông báo đăng ký thành công, tự động chuyển sang màn hình Đăng nhập.<br><br>**Kịch bản B: Đăng nhập hệ thống**<br>1. Người dùng truy cập trang Đăng nhập, nhập Email và Mật khẩu.<br>2. Người dùng nhấn nút "Đăng nhập".<br>3. Hệ thống tiếp nhận thông tin, kiểm tra sự tồn tại của email và so khớp mật khẩu bằng `PasswordEncoder`.<br>4. Hệ thống kiểm tra trạng thái tài khoản: tài khoản phải đang hoạt động (`status = ACTIVE` hoặc `enabled = true`).<br>5. Hệ thống sinh Access Token (JWT chứa claim: `userId`, `role`, `email`, hết hạn sau 15 phút) và Refresh Token ngẫu nhiên (lưu bản băm trong bảng `refresh_sessions`).<br>6. Hệ thống trả về token qua Header/Cookie bảo mật và chuyển hướng người dùng đến trang đích theo quyền (Customer vào cổng yêu cầu, Agent vào hàng đợi Inbox, Admin vào bảng điều khiển). |
| **Kịch bản phụ** | - **4a. Dữ liệu đăng ký không hợp lệ (Lỗi HTTP 400 `VALIDATION_ERROR`):** Email sai định dạng hoặc mật khẩu dưới 8 ký tự $\to$ Hệ thống báo lỗi chi tiết tại từng ô nhập liệu.<br>- **4b. Email đã tồn tại trong hệ thống (Lỗi HTTP 409 `EMAIL_ALREADY_EXISTS`):** Hệ thống thông báo email đã được đăng ký và đề xuất chuyển sang Đăng nhập hoặc Quên mật khẩu.<br>- **3a. Sai thông tin đăng nhập (Lỗi HTTP 401 `INVALID_CREDENTIALS`):** Sai email hoặc sai mật khẩu $\to$ Hệ thống trả thông báo lỗi chung: "Email hoặc mật khẩu không chính xác" (bảo mật, không tiết lộ sự tồn tại của email).<br>- **4c. Tài khoản bị vô hiệu hóa / Khóa (Lỗi HTTP 403 `ACCOUNT_DISABLED`):** Hệ thống từ chối đăng nhập và hiển thị thông báo: "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ quản trị viên." |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ liên quan:** BR-01 (Tài khoản tự đăng ký luôn là Customer), BR-14 (Xác thực danh tính qua Principal), BR-16 (Chặn triệt để tài khoản disabled).<br>- **Giao diện ánh xạ:** Màn hình `I01` (Đăng nhập - Node Figma `62:8214`, file `62-8214.png`), Màn hình `I02` (Đăng ký - Node Figma `62:8215`, file `62-8215.png`).<br>- **Mã kiểm thử:** TC-ID-01 (Register với role ADMIN trong body), TC-ID-02 (Login password sai), TC-ID-05 (Register/login hợp lệ); TC-SEC-01 (Mã giữ để đối soát; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt).<br>- **Thời gian phản hồi:** Quá trình xác thực đăng nhập phải hoàn tất trong vòng $\le 1.0$ giây. |

---

### 4.2.2. Làm mới phiên làm việc & Đăng xuất [UC-02]
*(Thành viên phụ trách: Ngô Viết Thanh Bình — Module D: Identity & Access)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-02** |
| **Tên Use Case** | **Làm mới phiên làm việc (Refresh Token) và Đăng xuất (Logout)** |
| **Tóm tắt** | Tự động gia hạn Access Token khi sắp hết hạn thông qua cơ chế xoay vòng Refresh Token an toàn, hoặc cho phép người dùng chủ động đăng xuất để hủy bỏ phiên làm việc trên thiết bị hiện tại. |
| **Tác nhân** | Người dùng đã đăng nhập (Customer, Support Agent, System Administrator). |
| **Điều kiện tiên quyết** | Người dùng đang trong phiên làm việc hợp lệ và sở hữu Refresh Token còn hiệu lực. |
| **Kết quả** | - Làm mới phiên: Cấp Access Token mới và Refresh Token mới thay thế token cũ.<br>- Đăng xuất: Phiên làm việc trong DB bị thu hồi (`revoked = true`), token client bị xóa, người dùng quay về trang đăng nhập. |
| **Kịch bản chính** | **Kịch bản A: Tự động làm mới phiên làm việc (Token Rotation)**<br>1. Client phát hiện Access Token hết hạn (nhận mã 401 hoặc kiểm tra thời gian client).<br>2. Client gửi yêu cầu `POST /api/v1/auth/refresh` kèm Refresh Token hiện tại.<br>3. Hệ thống tìm kiếm bản ghi session tương ứng trong cơ sở dữ liệu và kiểm tra: Token chưa hết hạn và chưa bị thu hồi.<br>4. Hệ thống kiểm tra trạng thái tài khoản người dùng: tài khoản vẫn đang hoạt động (`enabled = true`).<br>5. Hệ thống thu hồi Refresh Token cũ và phát hành một Refresh Token mới (cơ chế xoay vòng 1 lần).<br>6. Hệ thống tạo Access Token mới với thông tin vai trò cập nhật nhất.<br>7. Hệ thống trả về cặp token mới cho Client tiếp tục các tác nghiệp liền mạch.<br><br>**Kịch bản B: Đăng xuất khỏi hệ thống**<br>1. Người dùng nhấn vào menu đại diện cá nhân và chọn "Đăng xuất".<br>2. Client gửi yêu cầu `POST /api/v1/auth/logout` lên server.<br>3. Server đánh dấu bản ghi Refresh Token của thiết bị đó thành đã thu hồi (`revoked = true`).<br>4. Client xóa bỏ Access Token và Refresh Token khỏi bộ nhớ lưu trữ trình duyệt.<br>5. Hệ thống chuyển hướng người dùng về màn hình Đăng nhập công khai. |
| **Kịch bản phụ** | - **3a. Refresh Token không hợp lệ hoặc đã bị thu hồi trước đó (Lỗi HTTP 401 `INVALID_REFRESH_TOKEN`):** Phát hiện nguy cơ tấn công đánh cắp token $\to$ Hệ thống lập tức thu hồi toàn bộ các phiên làm việc của tài khoản này và yêu cầu đăng nhập lại.<br>- **4a. Tài khoản người dùng đã bị Admin vô hiệu hóa trong khi đang hoạt động (Lỗi HTTP 403 `ACCOUNT_DISABLED`):** Hệ thống từ chối cấp token mới, buộc đăng xuất ngay lập tức.<br>- **3b. Mất kết nối mạng khi đăng xuất:** Client chủ động xóa token cục bộ và chuyển người dùng về màn hình đăng nhập (Fallback an toàn). |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-16 (Disabled user bị thu hồi phiên ngay lập tức), FR-ID-04 (Token rotation chống Replay Attack).<br>- **Hiệu năng:** Thao tác Refresh Token phải diễn ra hoàn toàn ngầm dưới nền, thời gian phản hồi $\le 300$ ms.<br>- **Mã kiểm thử:** TC-ID-03 (Refresh token đã rotate), TC-ID-04 (Disabled Agent refresh/login), TC-ID-06 (Refresh đồng thời, cookie/CSRF và Axios single-flight). |

---

### 4.2.3. Xem và Chỉnh sửa hồ sơ cá nhân [UC-03]
*(Thành viên phụ trách: Ngô Viết Thanh Bình — Module D: Identity & Access)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-03** |
| **Tên Use Case** | **Xem và Chỉnh sửa hồ sơ cá nhân (Manage Profile)** |
| **Tóm tắt** | Cho phép người dùng xem thông tin chi tiết tài khoản của chính mình, cập nhật họ tên, số điện thoại liên lạc, ảnh đại diện và thực hiện đổi mật khẩu đăng nhập định kỳ. |
| **Tác nhân** | Mọi người dùng đã xác thực (Customer, Support Agent, Administrator). |
| **Điều kiện tiên quyết** | Người dùng đã đăng nhập thành công vào hệ thống. |
| **Kết quả** | Thông tin hồ sơ cá nhân hoặc mật khẩu mới được cập nhật thành công vào cơ sở dữ liệu. |
| **Kịch bản chính** | 1. Người dùng chọn mục "Hồ sơ cá nhân" từ thanh điều hướng.<br>2. Hệ thống truy vấn thông tin người dùng từ DB dựa trên `userId` trích xuất từ Access Token.<br>3. Hệ thống hiển thị giao diện hồ sơ gồm: Email (chỉ đọc), Họ tên, Số điện thoại, Vai trò hiện tại và Ngày tham gia.<br>4. Người dùng chỉnh sửa họ tên hoặc số điện thoại và nhấn "Lưu thay đổi".<br>5. Hệ thống xác thực tính hợp lệ của dữ liệu nhập (họ tên từ 2 đến 100 ký tự, định dạng số điện thoại chuẩn).<br>6. Hệ thống cập nhật dữ liệu mới vào DB và thông báo "Cập nhật hồ sơ thành công".<br><br>*(Nếu người dùng chọn Đổi mật khẩu):*<br>7. Người dùng nhập Mật khẩu hiện tại, Mật khẩu mới và Nhập lại mật khẩu mới.<br>8. Hệ thống kiểm tra mật khẩu hiện tại có khớp với mật khẩu đang lưu trữ.<br>9. Hệ thống kiểm tra mật khẩu mới phải khác mật khẩu cũ và đạt tiêu chuẩn bảo mật ($\ge 8$ ký tự, có chữ hoa, số).<br>10. Hệ thống băm mật khẩu mới bằng BCrypt, cập nhật vào DB và ghi nhật ký thay đổi an toàn. |
| **Kịch bản phụ** | - **5a. Dữ liệu chỉnh sửa không hợp lệ:** Hệ thống hiển thị cảnh báo đỏ bên dưới trường thông tin lỗi.<br>- **8a. Mật khẩu hiện tại không chính xác (Lỗi HTTP 400 `INVALID_CURRENT_PASSWORD`):** Hệ thống từ chối đổi mật khẩu và yêu cầu người dùng nhập lại đúng mật khẩu cũ.<br>- **9a. Mật khẩu mới trùng với mật khẩu cũ:** Hệ thống cảnh báo: "Mật khẩu mới không được trùng với mật khẩu hiện tại". |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-14 (Chỉ được phép xem/sửa hồ sơ của chính mình theo Principal).<br>- **Bảo mật:** Mật khẩu cũ và mới bắt buộc phải được che phủ (dấu `●`) trên giao diện người dùng.<br>- **Giao diện:** Màn hình `I03` (Hồ sơ khách hàng - Node `62:8216`), Màn hình `I04` (Hồ sơ nhân viên - Node `62:8328`).<br>- **Mã kiểm thử:** [Chờ định nghĩa test suite chi tiết ở Template 3; không dùng thay thế bằng TC-ID-05/06 vốn là ca test register/login và refresh token]. |

---

### 4.2.4. Quản lý tài khoản nhân viên hỗ trợ (Admin Manage Agents) [UC-04]
*(Thành viên phụ trách: Ngô Viết Thanh Bình — Module D: Identity & Access)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-04** |
| **Tên Use Case** | **Quản lý danh sách nhân viên hỗ trợ (Admin Manage Agents)** |
| **Tóm tắt** | Quản trị viên hệ thống (Admin) thực hiện tạo tài khoản mới cho nhân viên hỗ trợ (Agent), thiết lập phòng ban chuyên trách, hoặc tạm thời vô hiệu hóa (khóa)/kích hoạt lại tài khoản nhân viên. |
| **Tác nhân** | Quản trị viên hệ thống (System Administrator). |
| **Điều kiện tiên quyết** | Quản trị viên đã đăng nhập và sở hữu quyền hạn `ROLE_ADMIN`. |
| **Kết quả** | Tài khoản Agent mới được tạo lập, hoặc trạng thái hoạt động của nhân viên được cập nhật trong DB. |
| **Kịch bản chính** | 1. Quản trị viên truy cập mục "Quản trị người dùng" $\to$ chọn tab "Nhân viên hỗ trợ (Agents)".<br>2. Hệ thống tải và hiển thị danh sách toàn bộ Agent hiện có kèm trạng thái hoạt động (`ACTIVE` / `DISABLED`).<br>3. Để thêm mới, Admin nhấn nút "Thêm nhân viên mới".<br>4. Admin điền thông tin: Họ tên, Email công vụ, Mật khẩu khởi tạo ban đầu, Chức danh hỗ trợ.<br>5. Hệ thống kiểm tra email chưa tồn tại trong hệ thống, thực hiện gán vai trò `ROLE_AGENT` và băm mật khẩu an toàn.<br>6. Hệ thống lưu tài khoản mới vào cơ sở dữ liệu và hiển thị trong danh sách quản lý.<br><br>*(Trường hợp khóa tài khoản Agent):*<br>7. Admin nhấn nút "Vô hiệu hóa" bên cạnh tài khoản Agent cần khóa.<br>8. Hệ thống hiển thị hộp thoại xác nhận lý do khóa.<br>9. Admin xác nhận $\to$ Hệ thống cập nhật cờ `enabled = false` và thu hồi tức thời toàn bộ phiên đăng nhập của Agent này. |
| **Kịch bản phụ** | - **5a. Email nhân viên đã tồn tại:** Hệ thống hiển thị thông báo lỗi trùng lặp email.<br>- **7a. Admin cố tình tự khóa tài khoản của chính mình:** Hệ thống chặn thao tác và cảnh báo: "Không thể tự vô hiệu hóa tài khoản quản trị viên hiện tại".<br>- **9a. Agent bị khóa đang phụ trách các ticket chưa xong:** Hệ thống hiển thị cảnh báo liệt kê các ticket đang giao cho Agent này và đề xuất chuyển giao cho nhân viên khác xử lý tiếp. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-02 (Không cho phép tự đăng ký tài khoản Agent công khai; chỉ Admin mới có quyền tạo Agent), BR-16 (Khóa Agent thu hồi quyền tức thì).<br>- **Bảo mật:** Ghi nhật ký kiểm toán (Audit Log) đầy đủ: Admin nào đã thực hiện tạo hoặc khóa tài khoản nào.<br>- **Mã kiểm thử:** TC-ID-07, TC-ID-08 (Mã giữ để đối soát; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt). |

---

### 4.2.5. Đặt lại mật khẩu (Forgot / Reset Password) [UC-16]
*(Thành viên phụ trách: Ngô Viết Thanh Bình — Module D: Identity & Access)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-16** |
| **Tên Use Case** | **Khôi phục và Đặt lại mật khẩu (Reset Password - P1)** |
| **Tóm tắt** | Cho phép người dùng bị quên mật khẩu yêu cầu cấp mã khôi phục gửi về email cá nhân đã đăng ký, sau đó xác thực mã để thiết lập lại mật khẩu đăng nhập mới. |
| **Tác nhân** | Khách hàng hoặc Nhân viên bị quên mật khẩu (Unauthenticated User). |
| **Điều kiện tiên quyết** | Người dùng nhớ địa chỉ email đã đăng ký tài khoản trong hệ thống. |
| **Kết quả** | Mật khẩu tài khoản được đặt lại thành công; mã khôi phục cũ bị vô hiệu hóa hoàn toàn. |
| **Kịch bản chính** | 1. Người dùng chọn liên kết "Quên mật khẩu?" tại trang Đăng nhập.<br>2. Hệ thống hiển thị màn hình yêu cầu nhập email tài khoản.<br>3. Người dùng nhập email và nhấn "Gửi mã xác thực".<br>4. Hệ thống kiểm tra nếu email tồn tại trong DB, sinh một mã khôi phục ngẫu nhiên (Reset Token có hạn dùng 15 phút) và gửi email hướng dẫn cho người dùng.<br>5. *(Bảo mật)* Hệ thống luôn hiển thị thông báo thành công: "Nếu email của bạn tồn tại trong hệ thống, chúng tôi đã gửi hướng dẫn đặt lại mật khẩu".<br>6. Người dùng kiểm tra hòm thư, nhấp vào liên kết khôi phục (chứa token) chuyển về giao diện Đặt lại mật khẩu.<br>7. Người dùng nhập Mật khẩu mới và Xác nhận mật khẩu mới, sau đó nhấn "Lưu mật khẩu mới".<br>8. Hệ thống xác thực token: hợp lệ, chưa hết hạn và chưa từng sử dụng.<br>9. Hệ thống băm mật khẩu mới, cập nhật vào DB, đánh dấu token đã dùng (`used = true`) và chuyển người dùng về trang Đăng nhập. |
| **Kịch bản phụ** | - **4a. Người dùng gửi yêu cầu liên tục (Spam Rate Limit):** Nếu gửi quá 3 yêu cầu trong vòng 5 phút $\to$ Hệ thống tạm khóa chức năng gửi mail của IP đó và trả mã HTTP 429 `TOO_MANY_REQUESTS`.<br>- **8a. Token hết hạn hoặc không hợp lệ (Lỗi HTTP 400 `INVALID_RESET_TOKEN`):** Hệ thống báo lỗi "Liên kết đặt lại mật khẩu đã hết hạn hoặc không hợp lệ" và yêu cầu thực hiện lại từ bước 1. |
| **Ràng buộc phi chức năng** | - **Bảo mật:** Không bao giờ để lộ thông tin email có tồn tại trong hệ thống hay không tại bước gửi yêu cầu.<br>- **Mã kiểm thử:** TC-ID-09 (Mã giữ để đối soát P1; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt). |

---

### 4.2.6. Tạo yêu cầu hỗ trợ mới (Create Ticket) [UC-05]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-05** |
| **Tên Use Case** | **Tạo yêu cầu hỗ trợ mới (Create Ticket)** |
| **Tóm tắt** | Khách hàng (Customer) gửi một yêu cầu hỗ trợ kỹ thuật hoặc thắc mắc dịch vụ mới vào hệ thống, bao gồm tiêu đề, mô tả chi tiết vấn đề và đính kèm tệp tin hình ảnh/tài liệu liên quan. |
| **Tác nhân** | Khách hàng đã đăng nhập (`ROLE_CUSTOMER`). |
| **Điều kiện tiên quyết** | Khách hàng đã xác thực hợp lệ; tài khoản đang hoạt động. |
| **Kết quả** | - Một bản ghi Ticket mới được tạo trong cơ sở dữ liệu với trạng thái ban đầu là `OPEN`, độ ưu tiên mặc định `NORMAL`, mã ticket duy nhất dạng `TK-YYYYMMDD-XXXX`.<br>- Nội dung mô tả ban đầu được lưu thành tin nhắn công khai (`PUBLIC`) đầu tiên trong tiến trình hội thoại. |
| **Kịch bản chính** | 1. Khách hàng nhấn nút "Tạo yêu cầu mới" (New Ticket) trên thanh điều hướng.<br>2. Hệ thống hiển thị biểu mẫu tạo ticket gồm: Tiêu đề yêu cầu (Subject), Danh mục vấn đề (Category), Mô tả chi tiết (Description) và Vùng đính kèm tệp tin (Attachment Dropzone).<br>3. Khách hàng nhập tiêu đề (5 đến 150 ký tự), chọn danh mục, điền mô tả (từ 10 đến 5000 ký tự) và có thể chọn tệp đính kèm (ảnh PNG/JPG hoặc PDF $\le 5$ MB).<br>4. Khách hàng nhấn nút "Gửi yêu cầu".<br>5. Hệ thống tiếp nhận, trích xuất `userId` của khách hàng từ token, thực hiện kiểm tra tính hợp lệ của toàn bộ dữ liệu.<br>6. Trong **cùng một Transaction cơ sở dữ liệu** (Quy tắc BR-15):<br>   - Sinh mã ticket duy nhất.<br>   - Lưu thông tin ticket với trạng thái `OPEN`, `priority = NORMAL`, `assigned_agent_id = NULL`.<br>   - Lưu mô tả vào bảng `ticket_messages` với thuộc tính `visibility = PUBLIC`.<br>   - Ghi nhận sự kiện kiểm toán đầu tiên `TICKET_CREATED` vào bảng `ticket_events`.<br>7. Hệ thống cam kết (Commit) transaction, trả về mã HTTP 201 Created và điều hướng khách hàng đến màn hình Chi tiết ticket vừa tạo. |
| **Kịch bản phụ** | - **3a. Tiêu đề hoặc mô tả để trống hoặc không đủ độ dài (Lỗi HTTP 400 `VALIDATION_ERROR`):** Hệ thống cảnh báo đỏ yêu cầu nhập tiêu đề tối thiểu 5 ký tự và mô tả tối thiểu 10 ký tự.<br>- **3b. Tệp đính kèm vượt quá dung lượng hoặc sai định dạng (Lỗi HTTP 413 `FILE_TOO_LARGE`):** Hệ thống từ chối tệp và nhắc nhở giới hạn kích thước tối đa 5 MB.<br>- **5a. Lỗi hệ thống cơ sở dữ liệu trong quá trình tạo:** Transaction tự động Rollback hoàn toàn, không tạo ticket rác; hiển thị thông báo "Không thể tạo yêu cầu lúc này, vui lòng thử lại sau". |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-03 (Khách hàng là người sở hữu ticket), BR-05 (Ticket OPEN bắt buộc có người phụ trách là NULL), BR-15 (Ghi nhận event cùng transaction).<br>- **Giao diện:** Màn hình `C02` (Tạo yêu cầu mới - Node Figma `58:6764`, file `58-6764.png`).<br>- **Hiệu năng:** Thời gian phản hồi tạo ticket $\le 1.0$ giây.<br>- **Mã kiểm thử:** TC-TK-01, TC-TK-02. |

---

### 4.2.7. Xem danh sách và chi tiết Ticket (List/View Tickets) [UC-06]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-06** |
| **Tên Use Case** | **Xem danh sách và chi tiết Ticket (List and View Tickets)** |
| **Tóm tắt** | Cho phép người dùng duyệt danh sách ticket được phân quyền theo vai trò, sử dụng bộ lọc tìm kiếm nâng cao và xem toàn bộ luồng hội thoại, tiến trình xử lý chi tiết của một ticket cụ thể. |
| **Tác nhân** | Khách hàng (Customer), Nhân viên hỗ trợ (Support Agent), Quản trị viên (Admin). |
| **Điều kiện tiên quyết** | Người dùng đã đăng nhập vào hệ thống. |
| **Kết quả** | Hiển thị đúng danh sách ticket và chi tiết nội dung mà người dùng có thẩm quyền truy cập; bảo mật tuyệt đối các ghi chú nội bộ đối với khách hàng. |
| **Kịch bản chính** | 1. Người dùng chọn mục "Hộp thư / Danh sách Ticket".<br>2. Hệ thống kiểm tra vai trò người dùng để áp dụng bộ lọc quyền dữ liệu nghiêm ngặt:<br>   - **Customer:** Chỉ truy vấn các ticket do chính khách hàng đó tạo (`requester_id = current_user_id`).<br>   - **Agent:** Hiển thị 2 danh sách riêng biệt: Hàng đợi ticket chung chưa nhận (`status = OPEN` và `assigned_agent_id IS NULL`) và Danh sách ticket do chính Agent đang trực tiếp xử lý (`assigned_agent_id = current_user_id`).<br>   - **Admin:** Hiển thị toàn bộ ticket của tất cả phòng ban trong hệ thống.<br>3. Hệ thống trả về danh sách có hỗ trợ phân trang (mặc định 20 ticket/trang), sắp xếp theo mức độ ưu tiên hoặc ngày cập nhật mới nhất.<br>4. Người dùng có thể lọc theo trạng thái (`OPEN`, `IN_PROGRESS`, `WAITING_CUSTOMER`, `RESOLVED`, `CLOSED`), theo mức ưu tiên (`LOW`, `NORMAL`, `HIGH`), hoặc tìm kiếm từ khóa tiêu đề.<br>5. Người dùng nhấn vào một dòng ticket để xem chi tiết.<br>6. Hệ thống tải thông tin tổng quan ticket và luồng hội thoại tin nhắn:<br>   - Nếu người dùng là **Customer:** Hệ thống chỉ tải các tin nhắn có `visibility = PUBLIC`. Tuyệt đối không truy vấn hoặc trả về các tin nhắn `INTERNAL_NOTE` (Quy tắc BR-08).<br>   - Nếu người dùng là **Agent phụ trách hoặc Admin:** Hệ thống hiển thị đầy đủ cả tin nhắn công khai lẫn các thẻ ghi chú nội bộ màu vàng đặc trưng. |
| **Kịch bản phụ** | - **2a. Customer cố tình nhập ID ticket của khách hàng khác trên URL (Lỗi HTTP 404 / 403 `ACCESS_DENIED`):** Hệ thống kiểm tra quyền sở hữu, từ chối truy cập và chuyển hướng về trang danh sách của chính họ để tránh lộ dữ liệu.<br>- **3a. Không tìm thấy ticket nào khớp với bộ lọc:** Hệ thống hiển thị màn hình trống thân thiện (Empty State): "Không tìm thấy yêu cầu hỗ trợ nào phù hợp". |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-03 (Customer chỉ đọc ticket của mình), BR-04 (Agent chỉ thao tác trên ticket của mình hoặc queue OPEN), BR-08 (Bảo vệ ghi chú nội bộ).<br>- **Giao diện:** Màn hình `C01` (Danh sách của khách - Node `58:6763`), `A01` (Hàng đợi của Agent - Node `55:1992`), `C03` (Chi tiết ticket - Node `58:6765`).<br>- **Mã kiểm thử:** TC-TK-02 (Customer đọc ticket người khác $\to$ 404), TC-TK-03 (Agent mở ticket assigned của Agent khác $\to$ bị từ chối), TC-TK-04 (Customer xem messages $\to$ không có INTERNAL notes); TC-SEC-02 (Mã giữ để đối soát; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt). |

---

### 4.2.8. Tiếp nhận và Phân công Ticket (Claim / Assign Ticket) [UC-07]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-07** |
| **Tên Use Case** | **Tiếp nhận xử lý (Claim) và Phân công Ticket (Assign)** |
| **Tóm tắt** | Cho phép nhân viên hỗ trợ tiếp nhận một ticket đang mở từ hàng đợi chung để trực tiếp xử lý, hoặc cho phép quản trị viên phân công/chuyển giao ticket cho nhân viên phù hợp. Đây là Use Case có yêu cầu cao nhất về kiểm soát tranh chấp đồng thời (**Concurrency Control**). |
| **Tác nhân** | Nhân viên hỗ trợ (Support Agent - thao tác Claim), Quản trị viên (Admin - thao tác Assign/Reassign). |
| **Điều kiện tiên quyết** | - Đối với Agent Claim: Ticket đang ở trạng thái `OPEN` và chưa có người phụ trách (`assigned_agent_id IS NULL`). Tài khoản Agent đang hoạt động.<br>- Đối với Admin Assign: Tài khoản Agent được chỉ định phải đang ở trạng thái kích hoạt. |
| **Kết quả** | - Ticket được gán cho duy nhất một Agent phụ trách.<br>- Trạng thái ticket tự động chuyển từ `OPEN` sang `IN_PROGRESS`.<br>- Sự kiện `TICKET_CLAIMED` hoặc `TICKET_ASSIGNED` được ghi nhận vào lịch sử kiểm toán. |
| **Kịch bản chính** | **Kịch bản A: Agent tiếp nhận ticket từ hàng đợi (Claim Ticket)**<br>1. Agent mở danh sách hàng đợi chung các ticket `OPEN`.<br>2. Agent chọn một ticket và nhấn nút "Nhận xử lý" (Claim Ticket).<br>3. Hệ thống thực thi một câu lệnh cập nhật có điều kiện nguyên tử (Atomic Conditional Update) kèm khóa lạc quan:<br>   `UPDATE tickets SET assigned_agent_id = :agentId, status = 'IN_PROGRESS', version = version + 1 WHERE id = :ticketId AND status = 'OPEN' AND assigned_agent_id IS NULL AND version = :expectedVersion;`<br>4. Hệ thống kiểm tra số dòng bị ảnh hưởng:<br>   - Nếu số dòng cập nhật $= 1$: Thao tác thành công tuyệt đối.<br>5. Trong cùng transaction, hệ thống ghi nhận sự kiện `TICKET_CLAIMED` vào bảng `ticket_events` gồm thời gian, ID của Agent.<br>6. Hệ thống cam kết transaction và cập nhật giao diện: Ticket chuyển sang danh sách "Đang xử lý của tôi", nút Claim đổi thành trạng thái "Đang phụ trách".<br><br>**Kịch bản B: Admin phân công hoặc chuyển giao ticket (Assign / Reassign)**<br>1. Admin mở chi tiết ticket bất kỳ và nhấn "Phân công người xử lý".<br>2. Hệ thống hiển thị danh sách các Agent đang hoạt động.<br>3. Admin chọn một Agent và nhấn "Xác nhận".<br>4. Hệ thống kiểm tra Agent được chọn có `enabled = true`.<br>5. Hệ thống cập nhật `assigned_agent_id = newAgentId`, trạng thái chuyển thành `IN_PROGRESS` (nếu đang là OPEN), ghi sự kiện `TICKET_ASSIGNED` ghi rõ người phân công và người nhận mới. |
| **Kịch bản phụ** | - **4a. Xung đột nhận việc đồng thời - Hai Agent cùng bấm Claim một lúc (Lỗi HTTP 409 `TICKET_ALREADY_CLAIMED` - Concurrency Conflict):**<br>   Agent A bấm trước vài mili-giây và thắng transaction $\to$ Lệnh của Agent B tác động 0 dòng $\to$ Hệ thống phát hiện xung đột, hủy transaction của Agent B và trả thông báo đỏ trên giao diện: "Ticket này vừa được nhân viên [Tên Agent A] tiếp nhận cách đây vài giây. Vui lòng chọn ticket khác trong hàng đợi!" (Quy tắc BR-06).<br>- **4b. Admin phân công cho Agent đã bị vô hiệu hóa (Lỗi HTTP 400 `AGENT_DISABLED`):** Hệ thống từ chối phân công và yêu cầu chọn nhân viên khác đang hoạt động. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ cốt lõi:** BR-05 (Ticket OPEN chưa có người nhận), BR-06 (**Tuyệt đối không để xảy ra tình trạng 2 Agent cùng nhận 1 ticket** - Zero Double Claiming), BR-15 (Ghi event đồng thời).<br>- **Giao diện ánh xạ:** Màn hình `A06` (Cảnh báo xung đột Claim Conflict - Node `56:3104`, file `56-3104.png`), Màn hình `D03` (Admin phân công - Node `62:9945`).<br>- **Mã kiểm thử Concurrency:** TC-CON-01, TC-TK-05. |

---

### 4.2.9. Trao đổi tin nhắn công khai & Ghi chú nội bộ [UC-08]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-08** |
| **Tên Use Case** | **Trao đổi tin nhắn công khai và Ghi chú nội bộ (Send Message / Internal Note)** |
| **Tóm tắt** | Cho phép khách hàng và nhân viên hỗ trợ trao đổi phản hồi qua lại công khai; đồng thời cho phép nhân viên ghi chú nội bộ các phát hiện kỹ thuật mà chỉ nhân sự nội bộ (Agent/Admin) xem được. |
| **Tác nhân** | Khách hàng sở hữu ticket, Nhân viên được phân công phụ trách, Quản trị viên. |
| **Điều kiện tiên quyết** | Ticket chưa ở trạng thái đóng vĩnh viễn (`CLOSED`). Người gửi có thẩm quyền tương ứng với ticket. |
| **Kết quả** | Tin nhắn hoặc ghi chú mới được lưu trữ và hiển thị ngay lập tức trong tiến trình thảo luận của ticket. |
| **Kịch bản chính** | **Kịch bản A: Gửi tin nhắn công khai (Public Message)**<br>1. Người dùng nhập nội dung phản hồi vào khung soạn thảo.<br>2. Người dùng nhấn nút "Gửi phản hồi" (với visibility mặc định là `PUBLIC`).<br>3. Hệ thống tiếp nhận, trích xuất danh tính người gửi từ token, kiểm tra ticket chưa bị đóng (`status != CLOSED`).<br>4. Nếu người gửi là **Customer** và ticket đang ở trạng thái `WAITING_CUSTOMER`, hệ thống tự động kích hoạt chuyển trạng thái ticket về `IN_PROGRESS` trong cùng transaction.<br>5. Hệ thống lưu tin nhắn vào bảng `ticket_messages` và ghi sự kiện `MESSAGE_ADDED` tương ứng.<br>6. Tin nhắn hiển thị ngay lập tức trên màn hình cho cả hai bên cùng theo dõi.<br><br>**Kịch bản B: Agent tạo ghi chú nội bộ (Internal Note)**<br>1. Agent phụ trách chuyển tab soạn thảo sang chế độ "Ghi chú nội bộ" (giao diện đổi sang viền vàng cảnh báo).<br>2. Agent nhập nội dung phân tích nghiệp vụ, trao đổi chuyên môn.<br>3. Agent nhấn nút "Lưu ghi chú nội bộ".<br>4. Hệ thống kiểm tra vai trò người gửi bắt buộc phải là `ROLE_AGENT` hoặc `ROLE_ADMIN` (Quy tắc BR-08).<br>5. Hệ thống lưu tin nhắn với thuộc tính `visibility = INTERNAL`.<br>6. Thẻ ghi chú nội bộ màu vàng hiển thị trong luồng trao đổi của Agent/Admin, hoàn toàn ẩn đối với phía Customer. |
| **Kịch bản phụ** | - **3a. Khách hàng cố tình gửi tin nhắn khi ticket đã CLOSED (Lỗi HTTP 409 `TICKET_CLOSED`):** Hệ thống từ chối lưu và hiển thị thông báo: "Yêu cầu này đã được đóng hoàn tất. Vui lòng mở ticket mới nếu cần hỗ trợ thêm."<br>- **4a. Customer gửi request với thuộc tính visibility=INTERNAL (Lỗi HTTP 403 `FORBIDDEN`):** Hệ thống phát hiện vi phạm quyền, chặn đứng thao tác và ghi log cảnh báo bảo mật.<br>- **1a. Nội dung tin nhắn rỗng:** Nút gửi bị vô hiệu hóa cho đến khi có ít nhất 1 ký tự. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-07 (Không nhắn tin khi CLOSED), BR-08 (Bảo mật tuyệt đối Internal Note), BR-14 (Xác minh tác giả từ Principal).<br>- **Giao diện:** Màn hình `A04` (Ghi chú nội bộ - Node Figma `55:2537`, file `55-2537.png`), Màn hình `C03` (Chi tiết trao đổi - Node `58:6765`).<br>- **Mã kiểm thử:** TC-TK-04, TC-TK-06, TC-TK-07. |

---

### 4.2.10. Chuyển đổi trạng thái Ticket theo quy trình [UC-09]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-09** |
| **Tên Use Case** | **Chuyển đổi trạng thái Ticket (Transition Ticket State)** |
| **Tóm tắt** | Điều hướng vòng đời của ticket qua các trạng thái xử lý tuân thủ nghiêm ngặt máy trạng thái hữu hạn (State Machine), ngăn chặn mọi hành vi chuyển trạng thái nhảy cóc hoặc bất hợp lệ. |
| **Tác nhân** | Nhân viên hỗ trợ được giao ticket, Quản trị viên, Khách hàng sở hữu ticket (chỉ thao tác Reopen hoặc Close). |
| **Điều kiện tiên quyết** | Ticket đang ở trạng thái hợp lệ để thực hiện hành động chuyển đổi tiếp theo. |
| **Kết quả** | Trạng thái ticket được cập nhật chính xác; lịch sử chuyển trạng thái được ghi nhận đầy đủ. |
| **Kịch bản chính** | 1. Người dùng chọn hành động chuyển trạng thái trên thanh công cụ ticket:<br>   - **Agent/Admin chọn:** "Yêu cầu thêm thông tin" (Request Info), "Giải quyết xong" (Resolve Ticket).<br>   - **Customer chọn:** "Đóng ticket" (Close Ticket) hoặc "Mở lại ticket" (Reopen Ticket - chỉ khi ticket đang RESOLVED).<br>2. Hệ thống tiếp nhận mã hành động (Action Enum), tải bản ghi ticket kèm khóa phiên bản `@Version`.<br>3. Hệ thống đối soát ma trận chuyển trạng thái hợp lệ:<br>   - `IN_PROGRESS` $\to$ `WAITING_CUSTOMER` (khi Agent yêu cầu khách cung cấp thêm chứng cứ).<br>   - `WAITING_CUSTOMER` $\to$ `IN_PROGRESS` (khi khách phản hồi tin nhắn).<br>   - `IN_PROGRESS` $\to$ `RESOLVED` (khi Agent xác nhận đã khắc phục xong lỗi).<br>   - `RESOLVED` $\to$ `CLOSED` (khi khách hàng hài lòng xác nhận đóng hoặc sau thời gian timeout).<br>   - `RESOLVED` $\to$ `IN_PROGRESS` (khi khách hàng báo sự cố chưa được khắc phục triệt để).<br>4. Hệ thống kiểm tra thẩm quyền của người thực hiện tương ứng với hành động.<br>5. Trong cùng transaction, hệ thống cập nhật `status = newStatus`, tăng `version = version + 1`, ghi nhận sự kiện `STATUS_CHANGED` vào bảng `ticket_events` (lưu rõ trạng thái cũ, trạng thái mới, lý do và người thực hiện).<br>6. Hệ thống cam kết transaction và cập nhật giao diện người dùng theo trạng thái mới. |
| **Kịch bản phụ** | - **3a. Chuyển trạng thái bất hợp lệ (Lỗi HTTP 409 `INVALID_TICKET_TRANSITION`):** Ví dụ Agent cố tình chuyển trực tiếp từ `OPEN` sang `RESOLVED` mà chưa Claim $\to$ Hệ thống chặn lại và báo lỗi vi phạm quy trình.<br>- **4a. Khách hàng cố tình chuyển ticket sang RESOLVED:** Hệ thống báo lỗi 403: "Chỉ nhân viên phụ trách mới có quyền đánh dấu giải quyết yêu cầu".<br>- **2a. Xung đột phiên bản dữ liệu (Lỗi HTTP 409 `TICKET_VERSION_CONFLICT`):** Hai người cùng thao tác đồng thời trên một ticket $\to$ Người bấm sau nhận thông báo tải lại dữ liệu mới nhất. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-07, BR-09 (Khách chỉ được Close/Reopen từ Resolved), BR-15 (Kiểm toán đầy đủ).<br>- **Toàn vẹn dữ liệu:** Bắt buộc áp dụng cơ chế State Machine ở tầng Service, không chỉ phụ thuộc giao diện.<br>- **Mã kiểm thử:** TC-TK-08, TC-WF-01, TC-WF-02. |

---

### 4.2.11. Xem lịch sử xử lý và Nhật ký sự kiện Ticket [UC-10]
*(Thành viên phụ trách: Phan Gia Phúc — Module C: Ticket Management)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-10** |
| **Tên Use Case** | **Xem lịch sử xử lý và Nhật ký sự kiện Ticket (View Ticket Event History)** |
| **Tóm tắt** | Cung cấp cho nhân viên hỗ trợ và quản trị viên cái nhìn toàn diện, minh bạch về toàn bộ chuỗi sự kiện kiểm toán (Audit Trail) đã diễn ra trên ticket từ lúc khởi tạo đến thời điểm hiện tại. |
| **Tác nhân** | Nhân viên hỗ trợ được phân công, Quản trị viên hệ thống. |
| **Điều kiện tiên quyết** | Người dùng có quyền truy cập vào ticket đang xét. |
| **Kết quả** | Dòng thời gian (Timeline) các sự kiện được hiển thị tuần tự, trực quan với đầy đủ mốc giờ, người thực hiện và dữ liệu thay đổi. |
| **Kịch bản chính** | 1. Agent hoặc Admin mở trang chi tiết của một ticket và chọn tab "Lịch sử sự kiện / Timeline".<br>2. Hệ thống kiểm tra quyền hạn của người dùng (Agent phụ trách hoặc Admin).<br>3. Hệ thống truy vấn bảng `ticket_events` được sắp xếp theo thời gian tăng dần (`created_at ASC`).<br>4. Hệ thống render giao diện dòng thời gian trực quan gồm các sự kiện:<br>   - Thời điểm tạo ticket và danh tính khách hàng khởi tạo (`TICKET_CREATED`).<br>   - Thời điểm Agent tiếp nhận ticket (`TICKET_CLAIMED`).<br>   - Các lần Admin chuyển giao hoặc phân công nhân viên (`TICKET_ASSIGNED`).<br>   - Các lần chuyển đổi trạng thái ticket kèm lý do chi tiết (`STATUS_CHANGED`).<br>   - Thời điểm áp dụng gợi ý từ AI (`AI_SUGGESTION_APPLIED`).<br>5. Người dùng có thể nhấn vào từng sự kiện để xem chi tiết thông tin thay đổi (Payload JSON). |
| **Kịch bản phụ** | - **2a. Khách hàng tìm cách truy cập API lịch sử sự kiện nội bộ:** Hệ thống trả lỗi HTTP 403 `FORBIDDEN` do luồng timeline chi tiết chứa các thông tin phân công nội bộ không công khai cho khách hàng. |
| **Ràng buộc phi chức năng** | - **Bảo mật & Toàn vẹn:** Bảng `ticket_events` là bảng ghi duy nhất chỉ thêm mới (Append-Only), nghiêm cấm mọi thao tác sửa hoặc xóa (`UPDATE` / `DELETE`) từ API.<br>- **Mã kiểm thử:** TC-TK-09 (Mã giữ để đối soát; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt). |

---

### 4.2.12. Tải lên và Xử lý tài liệu tri thức (Upload & Process Document) [UC-11]
*(Thành viên phụ trách: Nguyễn Đức Lãm — Module B: Knowledge Base)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-11** |
| **Tên Use Case** | **Tải lên và Xử lý tài liệu tri thức (Upload & Process Knowledge Document)** |
| **Tóm tắt** | Quản trị viên tải lên các tệp tài liệu chính sách, cẩm nang nghiệp vụ (định dạng PDF văn bản, TXT, MD) để hệ thống tự động trích xuất nội dung, phân đoạn ngữ nghĩa và tạo vector nhúng đa chiều trong tiến trình xử lý nền không đồng bộ. |
| **Tác nhân** | Quản trị viên hệ thống (System Administrator). |
| **Điều kiện tiên quyết** | Admin đã đăng nhập; tệp tài liệu tuân thủ định dạng hỗ trợ và dung lượng $\le 10$ MiB. |
| **Kết quả** | - Tệp tài liệu được lưu an toàn vào vùng lưu trữ riêng biệt (Private Storage Volume).<br>- Tác vụ xử lý nền (Ingestion Job) được khởi tạo và chuyển đổi trạng thái thành `READY` khi hoàn tất hoặc `FAILED` nếu có lỗi. |
| **Kịch bản chính** | 1. Admin truy cập trang Quản lý tri thức $\to$ nhấn "Tải lên tài liệu mới".<br>2. Hệ thống hiển thị vùng kéo thả tệp (Upload Dropzone).<br>3. Admin chọn tệp tài liệu từ máy tính (ví dụ: `Chinh-sach-doi-tra.pdf`) và bấm "Bắt đầu tải lên".<br>4. Hệ thống kiểm tra tính hợp lệ: phần mở rộng tệp, kiểu MIME type thực tế, dung lượng $\le 10$ MiB.<br>5. Hệ thống lưu tệp vào Private Storage, tạo bản ghi trong bảng `knowledge_documents` với trạng thái ban đầu là `UPLOADED` và tạo một tác vụ nền trong bảng `ingestion_jobs`.<br>6. Hệ thống phản hồi ngay mã HTTP 202 Accepted cho Admin kèm ID tài liệu (không làm đơ giao diện).<br>7. **Tiến trình xử lý nền (Background Worker):**<br>   - Worker nhận job, cập nhật trạng thái tài liệu sang `PROCESSING`.<br>   - Worker trích xuất văn bản (Text Extraction) từ các trang tài liệu.<br>   - Worker thực hiện phân chia văn bản thành các đoạn nhỏ (Chunks) có kích thước tối ưu (500–1000 tokens) kèm metadata `page_number`, `chunk_index`.<br>   - Worker gọi Embedding Provider tạo vector nhúng cho từng chunk.<br>   - Worker lưu các chunk và vector vào bảng `document_chunks` trong PostgreSQL (cột `embedding vector(1536)`).<br>   - Worker hoàn tất, cập nhật trạng thái tài liệu sang `READY` (`published = false`).<br>8. Admin nhận được thông báo tài liệu đã sẵn sàng kiểm duyệt xuất bản. |
| **Kịch bản phụ** | - **4a. Tệp tải lên quá 10 MiB (Lỗi HTTP 413 `FILE_TOO_LARGE`):** Hệ thống từ chối nhận tệp và cảnh báo giới hạn dung lượng.<br>- **7a. Tệp PDF là ảnh scan, không trích xuất được văn bản (Lỗi `UNSUPPORTED_SCANNED_PDF`):** Worker phát hiện không có chữ $\to$ Cập nhật trạng thái sang `FAILED` kèm lý do: "Tài liệu PDF là dạng ảnh quét, hệ thống chưa hỗ trợ OCR trong phiên bản này. Vui lòng tải lên PDF dạng văn bản".<br>- **7b. Dịch vụ Embedding bị quá tải hoặc rớt mạng:** Worker tự động thử lại tối đa 3 lần theo lũy thừa thời gian (Exponential Backoff). Nếu vẫn thất bại $\to$ Đánh dấu `FAILED` an toàn. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-11 (Tài liệu READY mới chỉ ở dạng lưu nháp, chưa tự động kích hoạt cho AI dùng cho đến khi Publish).<br>- **Kiến trúc:** Tuyệt đối không chạy tác vụ trích xuất và gọi LLM bên trong HTTP Request của giao diện (tránh nghẽn thread pool).<br>- **Giao diện:** Màn hình `K05` (Tải lên tài liệu - Node Figma `62:9241`, file `62-9241.png`).<br>- **Mã kiểm thử:** TC-KB-01 (Upload PDF text-based $\to$ READY unpublished), TC-KB-02 (Upload exe giả .pdf / file quá lớn $\to$ rejected), TC-KB-03 (PDF không có text $\to$ FAILED), TC-KB-04 (Retry job bị lỗi $\to$ max attempts, không duplicate chunks), TC-KB-06 (Crash và completion bằng lease cũ), TC-KB-07 (TXT/MD, file private và retry trùng). |

---

### 4.2.13. Công bố và Lưu trữ tài liệu tri thức (Publish / Archive Document) [UC-12]
*(Thành viên phụ trách: Nguyễn Đức Lãm — Module B: Knowledge Base)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-12** |
| **Tên Use Case** | **Công bố (Publish) và Lưu trữ (Archive) tài liệu tri thức** |
| **Tóm tắt** | Cho phép quản trị viên xem xét nội dung tài liệu sau khi hệ thống xử lý xong, chính thức công bố tài liệu để phục vụ truy xuất câu trả lời cho AI; hoặc lưu trữ ẩn tài liệu khi chính sách đã hết hạn. |
| **Tác nhân** | Quản trị viên hệ thống (System Administrator). |
| **Điều kiện tiên quyết** | - Thao tác Publish: Tài liệu đang ở trạng thái `READY` và chưa được công bố (`published = false`).<br>- Thao tác Archive: Tài liệu đang được công bố và chưa bị lưu trữ. |
| **Kết quả** | - Công bố: Tài liệu chuyển sang `published = true`, mốc giờ `published_at` được ghi nhận; các đoạn chunk ngay lập tức tham gia vào kho tìm kiếm của AI.<br>- Lưu trữ: Tài liệu chuyển sang trạng thái `ARCHIVED`, `published = false`; ngay lập tức bị loại bỏ khỏi mọi truy xuất AI mới. |
| **Kịch bản chính** | **Kịch bản A: Công bố tài liệu (Publish Document)**<br>1. Admin xem danh sách tài liệu trong kho tri thức, lọc theo trạng thái `READY`.<br>2. Admin mở xem chi tiết các đoạn chunk văn bản đã được bóc tách để kiểm tra chất lượng.<br>3. Admin nhấn nút "Công bố tài liệu" (Publish).<br>4. Hệ thống kiểm tra điều kiện trạng thái tài liệu là `READY`.<br>5. Hệ thống cập nhật `published = true`, `published_at = CURRENT_TIMESTAMP` và ghi nhật ký kiểm toán.<br>6. Hệ thống hiển thị thông báo "Tài liệu đã được công bố thành công. Trợ lý AI đã có thể khai thác tri thức này".<br><br>**Kịch bản B: Lưu trữ tài liệu hết hiệu lực (Archive Document)**<br>1. Admin chọn tài liệu chính sách đã cũ và nhấn nút "Lưu trữ" (Archive).<br>2. Hệ thống hiển thị cảnh báo xác nhận việc ẩn tài liệu khỏi trợ lý AI.<br>3. Admin xác nhận thao tác.<br>4. Hệ thống cập nhật trạng thái `status = 'ARCHIVED'`, `published = false` (Áp dụng cơ chế xóa mềm - Soft Delete để giữ nguyên vẹn bằng chứng lịch sử các câu trả lời cũ của AI).<br>5. Hệ thống thông báo lưu trữ thành công. |
| **Kịch bản phụ** | - **4a. Admin cố tình nhấn Publish khi tài liệu đang ở trạng thái PROCESSING hoặc FAILED (Lỗi HTTP 409 `DOCUMENT_NOT_READY`):** Hệ thống từ chối thao tác và thông báo tài liệu chưa được xử lý xong.<br>- **5a. Lỗi hệ thống cơ sở dữ liệu:** Thao tác bị hủy, giữ nguyên trạng thái cũ của tài liệu. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-11 (Chỉ tài liệu READY + published + chưa archive mới được truy xuất), BR-12 (Giữ nguyên snapshot các đoạn trích cũ sau khi tài liệu mẹ bị archive).<br>- **Giao diện:** Màn hình `K06` (Chi tiết tài liệu & Công bố - Node `62:9242`), Màn hình `K04` (Bảng quản trị tài liệu tri thức - Node `62:9240`).<br>- **Mã kiểm thử:** TC-KB-05 (Archive document $\to$ vector search sau đó không trả tài liệu archive; không dùng thay thế bằng TC-KB-04 vốn là ca test retry job ingestion). |

---

### 4.2.14. Tìm kiếm bài viết trong kho tri thức (Search Knowledge) [UC-13]
*(Thành viên phụ trách: Nguyễn Đức Lãm — Module B: Knowledge Base)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-13** |
| **Tên Use Case** | **Tìm kiếm bài viết trong kho tri thức (Search Knowledge)** |
| **Tóm tắt** | Cho phép nhân viên hỗ trợ và quản trị viên tra cứu nhanh các bài viết cẩm nang, chính sách nghiệp vụ thông qua thanh tìm kiếm thông minh kết hợp giữa tìm kiếm từ khóa và tìm kiếm ngữ nghĩa vector. |
| **Tác nhân** | Nhân viên hỗ trợ (Support Agent), Quản trị viên (Admin). |
| **Điều kiện tiên quyết** | Người dùng đã đăng nhập vào hệ thống; kho tri thức có ít nhất 1 tài liệu đã công bố. |
| **Kết quả** | Danh sách các bài viết và đoạn trích dẫn phù hợp nhất được hiển thị kèm điểm tương đồng (Similarity Score) và đánh dấu từ khóa. |
| **Kịch bản chính** | 1. Người dùng truy cập trang "Cơ sở tri thức (Knowledge Base)" hoặc mở thanh công cụ tra cứu nhanh bên cạnh màn hình xử lý ticket.<br>2. Người dùng nhập câu hỏi hoặc từ khóa cần tìm kiếm (ví dụ: "Chính sách đổi trả trong vòng 7 ngày") vào ô tìm kiếm.<br>3. Người dùng nhấn phím Enter hoặc nút Tìm kiếm.<br>4. Hệ thống tiếp nhận truy vấn, thực hiện chuẩn hóa chuỗi tìm kiếm.<br>5. Hệ thống tạo vector nhúng cho câu truy vấn và thực hiện truy vấn kết hợp (Hybrid Search):<br>   - Tìm kiếm văn bản toàn văn (Full-Text Search) trên tiêu đề và nội dung.<br>   - Tìm kiếm khoảng cách Cosine trên cột `embedding` qua toán tử `<=>` của `pgvector` trên các chunk thỏa điều kiện `published = true AND status = 'READY'`.<br>6. Hệ thống tổng hợp kết quả, lọc bỏ các đoạn có điểm tương đồng dưới ngưỡng cấu hình ($threshold < 0.7$), lấy ra top $K$ kết quả cao nhất.<br>7. Hệ thống hiển thị danh sách các bài viết liên quan, làm nổi bật đoạn văn bản khớp ngữ nghĩa.<br>8. Người dùng nhấn vào một kết quả để đọc toàn bộ nội dung bài viết gốc. |
| **Kịch bản phụ** | - **6a. Không tìm thấy tài liệu phù hợp (Điểm tương đồng đều dưới ngưỡng):** Hệ thống hiển thị thông báo "Không tìm thấy tài liệu nào phù hợp với từ khóa của bạn" và gợi ý điều chỉnh lại câu truy vấn.<br>- **4a. Người dùng nhập câu truy vấn quá ngắn ($< 2$ ký tự):** Hệ thống yêu cầu nhập từ khóa tối thiểu 2 ký tự. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-11 (Chỉ tìm kiếm trên tài liệu hợp lệ).<br>- **Hiệu năng:** Thời gian truy vấn vector và trả kết quả hiển thị trên giao diện phải đạt $\le 500$ ms.<br>- **Giao diện:** Màn hình `K01` (Tìm kiếm tri thức - Node `62:9092`), Màn hình `K03` (Đọc chi tiết bài viết - Node `62:9094`).<br>- **Mã kiểm thử:** TC-KB-05 (Đối soát truy xuất sau archive/publish), TC-AI-01/02 (Truy xuất có/không có evidence); [Chờ định nghĩa test suite chi tiết cho giao diện tìm kiếm ở Template 3; không dùng thay thế bằng TC-KB-06/07 vốn là ca test crash/lease và parser private file của worker]. |

---

### 4.2.15. Tự động sinh gợi ý câu trả lời bằng AI (Generate AI Suggestion) [UC-14]
*(Thành viên phụ trách: Lê Quý Phúc — Module A: AI Assistance)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-14** |
| **Tên Use Case** | **Tự động sinh gợi ý câu trả lời bằng AI (Generate AI Suggestion)** |
| **Tóm tắt** | Hỗ trợ nhân viên đang xử lý ticket tự động phân tích câu hỏi của khách hàng, truy xuất tài liệu tri thức liên quan thông qua mô hình RAG và tạo ra một bản nháp câu trả lời hoàn chỉnh kèm **dẫn chứng nguồn gốc (Citations)** rõ ràng. |
| **Tác nhân** | Nhân viên hỗ trợ được giao ticket (Assigned Agent), Quản trị viên (Admin). |
| **Điều kiện tiên quyết** | - Ticket đang ở trạng thái được phép xử lý (`OPEN` sau khi nhận, `IN_PROGRESS`, `WAITING_CUSTOMER`), chưa bị đóng (`CLOSED`).<br>- Kho tri thức có tài liệu đã công bố; Dịch vụ AI Provider được cấu hình hoạt động. |
| **Kết quả** | Một bản ghi Gợi ý câu trả lời (`ai_suggestions`) được tạo với trạng thái `GENERATED`, hiển thị trên ngăn trợ lý AI của Agent; **tuyệt đối không tạo tin nhắn công khai và không thay đổi trạng thái ticket**. |
| **Kịch bản chính** | 1. Agent mở trang chi tiết ticket đang phụ trách, nhấn nút "Gợi ý câu trả lời AI" (Suggest Reply) tại ngăn trợ lý bên phải màn hình.<br>2. Hệ thống kiểm tra quyền: Agent hiện tại phải đúng là người được phân công xử lý ticket này (`assigned_agent_id = current_user_id`) hoặc có vai trò Admin.<br>3. Hệ thống thu thập ngữ cảnh cuộc hội thoại: Trích xuất tiêu đề ticket, mô tả ban đầu và các tin nhắn `PUBLIC` gần nhất; **tuyệt đối loại bỏ mọi ghi chú nội bộ `INTERNAL_NOTE`** để đảm bảo an toàn dữ liệu.<br>4. Hệ thống tạo câu truy vấn ngữ nghĩa, thực hiện tìm kiếm Top-$K$ (ví dụ: 3 đến 5) đoạn chunk tri thức tương đồng nhất trong PostgreSQL bằng `pgvector`.<br>5. Hệ thống kiểm tra độ tin cậy của tài liệu truy xuất:<br>   - Nếu không có chunk nào vượt qua ngưỡng tin cậy ($threshold \ge 0.75$) $\to$ Chuyển sang kịch bản phụ 5a (Từ chối trả lời an toàn).<br>6. Hệ thống xây dựng Prompt có cấu trúc nghiêm ngặt gồm: Chỉ dẫn hệ thống (System Instructions), Câu hỏi của khách hàng và Nội dung các chunk tài liệu kèm mã định danh nguồn (Source IDs).<br>7. Hệ thống gọi mô hình AI sinh câu trả lời.<br>8. Hệ thống kiểm tra tính hợp lệ của trích dẫn (Citation Verification): Xác minh toàn bộ các trích dẫn trong văn bản trả về đều trỏ chính xác đến các chunk đã cung cấp ở bước 4 (Quy tắc BR-12).<br>9. Hệ thống lưu bản ghi vào bảng `ai_suggestions` kèm ảnh chụp tức thời (Snapshot) nội dung nguồn trích dẫn tại thời điểm sinh.<br>10. Hệ thống hiển thị bản nháp câu trả lời cùng danh sách các nguồn dẫn chứng lên ngăn Trợ lý AI trên giao diện của Agent. |
| **Kịch bản phụ** | - **5a. Không đủ tài liệu bằng chứng để trả lời (Quy tắc BR-13 `INSUFFICIENT_EVIDENCE`):**<br>   Hệ thống không cố ép mô hình bịa đặt thông tin; lập tức trả về thông báo an toàn: "Hệ thống chưa tìm thấy tài liệu chính sách phù hợp để trả lời vấn đề này. Vui lòng tự soạn thảo câu trả lời hoặc tra cứu thêm trong kho tri thức!" (Trạng thái suggestion: `ABSTAINED`).<br>- **7a. Mô hình AI gặp lỗi quá tải hoặc timeout (Lỗi `AI_PROVIDER_TIMEOUT` / HTTP 429):** Hệ thống hiển thị thông báo lỗi thân thiện: "Dịch vụ AI tạm thời gián đoạn. Tiến trình ticket vẫn diễn ra bình thường, Agent có thể tiếp tục trả lời thủ công".<br>- **8a. Mô hình AI sinh trích dẫn sai lệch (Fail-Closed Enforcement):** Nếu AI tự tạo trích dẫn giả không có trong danh sách chunk $\to$ Hệ thống đánh dấu trạng thái `FAILED`, hủy bản nháp, không hiển thị cho Agent để ngăn ngừa sai sót. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ sống còn:** BR-10 (**AI không bao giờ tự động gửi tin nhắn hoặc chuyển trạng thái ticket**), BR-12 (Trích dẫn phải được xác minh và lưu snapshot), BR-13 (Từ chối khi thiếu dữ liệu).<br>- **Giao diện:** Màn hình `A03` (Gợi ý AI có trích dẫn nguồn - Node Figma `55:1994`, file `55-1994.png`), Màn hình `A05` (Trạng thái AI đang suy nghĩ - Node `55:2538`).<br>- **Thời gian xử lý:** Toàn bộ chuỗi xử lý RAG hoàn tất trong $\le 5.0$ giây.<br>- **Mã kiểm thử:** TC-AI-01, TC-AI-02, TC-AI-03, TC-AI-04, TC-AI-05. |

---

### 4.2.16. Kiểm duyệt, Chỉnh sửa và Áp dụng gợi ý AI (Review, Edit & Send AI Suggestion) [UC-15]
*(Thành viên phụ trách: Lê Quý Phúc — Module A: AI Assistance)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-15** |
| **Tên Use Case** | **Kiểm duyệt, Chỉnh sửa và Gửi câu trả lời AI (Review, Edit and Apply AI Suggestion)** |
| **Tóm tắt** | Hiện thực hóa quy trình **Human-in-the-loop**: Nhân viên hỗ trợ trực tiếp kiểm tra tính xác thực của câu trả lời AI gợi ý, đọc đối soát tài liệu trích dẫn nguồn, chỉnh sửa câu chữ theo ý muốn và chủ động bấm nút gửi cho khách hàng. |
| **Tác nhân** | Nhân viên hỗ trợ được giao ticket (Assigned Agent), Quản trị viên (Admin). |
| **Điều kiện tiên quyết** | Đã có bản nháp gợi ý AI được tạo thành công cho ticket này (`status = GENERATED`). |
| **Kết quả** | - Nội dung do Agent phê duyệt được gửi thành tin nhắn công khai (`PUBLIC`) đến khách hàng.<br>- Bản ghi gợi ý AI được chuyển trạng thái sang `APPLIED` để phục vụ đánh giá chất lượng. |
| **Kịch bản chính** | 1. Agent đọc kỹ bản thảo câu trả lời do AI gợi ý trên ngăn Trợ lý.<br>2. Agent nhấp vào các thẻ trích dẫn nguồn (Source Citations) để mở cửa sổ đọc đối chiếu đoạn văn bản gốc trong tài liệu mẹ nhằm đảm bảo tính chính xác 100%.<br>3. Agent thực hiện một trong các hành động sau:<br>   - **Hành động A (Chấp nhận và chỉnh sửa):** Agent nhấn nút "Sử dụng bản nháp này" (Insert to Editor) $\to$ Nội dung được đưa vào khung soạn thảo tin nhắn công khai; Agent chỉnh sửa, thêm bớt lời chào hoặc bổ sung thông tin cá nhân hóa.<br>   - **Hành động B (Bỏ qua):** Agent thấy không phù hợp, nhấn "Bỏ qua gợi ý" (Discard) $\to$ Trạng thái suggestion cập nhật thành `DISCARDED`, không làm ảnh hưởng đến ticket.<br>4. Sau khi hoàn thiện nội dung trong khung soạn thảo, Agent chủ động nhấn nút "Gửi phản hồi cho khách".<br>5. Hệ thống tiếp nhận yêu cầu gửi tin nhắn, lưu tin nhắn vào bảng `ticket_messages` với vai trò tác giả là chính Agent.<br>6. Hệ thống liên kết `suggestionId` tương ứng và cập nhật trạng thái bản ghi AI thành `APPLIED`.<br>7. Khách hàng nhìn thấy tin nhắn phản hồi chính thức từ nhân viên hỗ trợ. |
| **Kịch bản phụ** | - **3a. Ticket đã bị khách hàng đóng trong lúc Agent đang kiểm duyệt (Lỗi HTTP 409 `TICKET_CLOSED`):** Hệ thống từ chối gửi tin nhắn và thông báo ticket đã kết thúc.<br>- **5a. Mất kết nối mạng khi bấm gửi:** Giao diện hiển thị nút "Thử lại" mà không làm mất nội dung văn bản Agent vừa chỉnh sửa. |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** BR-10 (Bắt buộc Human-in-the-loop; khách hàng chỉ nhận nội dung do con người duyệt), BR-12 (Lưu vết audit phục vụ đánh giá độ hữu ích của AI).<br>- **Giao diện:** Màn hình `A08` (Đọc chi tiết tài liệu nguồn trích dẫn - Node Figma `56:3578`, file `56-3578.png`), Màn hình `A02` (Màn hình xử lý ticket - Node `55:1993`).<br>- **Mã kiểm thử:** TC-AI-06, TC-AI-07, TC-WF-03, TC-WF-04. |

---

### 4.2.17. Báo cáo thống kê và Phân tích hiệu suất (Ticket Analytics P1) [UC-17]
*(Thành viên phụ trách: Lê Quý Phúc — Module A: AI Assistance & Analytics Lead)*

| Trường thông tin | Nội dung chi tiết |
| :--- | :--- |
| **Use case ID** | **UC-17** |
| **Tên Use Case** | **Xem báo cáo thống kê và Phân tích hiệu suất (View Ticket Analytics & Performance - P1)** |
| **Tóm tắt** | Cung cấp cho Quản trị viên hệ thống cái nhìn tổng quan về khối lượng công việc, tỷ lệ ticket theo trạng thái, năng suất tiếp nhận xử lý của từng nhân viên và tỷ lệ phản hồi hiệu quả của trợ lý AI. |
| **Tác nhân** | Quản trị viên hệ thống (System Administrator). |
| **Điều kiện tiên quyết** | Quản trị viên đã đăng nhập và sở hữu quyền `ROLE_ADMIN`. |
| **Kết quả** | Bảng điều khiển (Dashboard) hiển thị trực quan các thẻ chỉ số KPI chính và biểu đồ phân bổ dữ liệu theo mốc thời gian tùy chọn. |
| **Kịch bản chính** | 1. Quản trị viên truy cập mục "Báo cáo thống kê (Analytics)" từ thanh điều hướng chính.<br>2. Hệ thống tải dữ liệu tổng hợp và hiển thị các khối chỉ số quan trọng (KPI Cards):<br>   - Tổng số ticket tiếp nhận trong kỳ.<br>   - Số lượng ticket theo từng trạng thái: `OPEN`, `IN_PROGRESS`, `WAITING_CUSTOMER`, `RESOLVED`, `CLOSED`.<br>   - Thời gian giải quyết trung bình (MTTR - Mean Time to Resolve).<br>   - Chỉ số năng suất nhân viên: Số ticket đã giải quyết của từng Agent.<br>   - Tỷ lệ ứng dụng AI: Tỷ lệ bản nháp AI được Agent sử dụng (`Applied Rate`).<br>3. Admin có thể thay đổi bộ lọc thời gian: "Hôm nay", "7 ngày qua", "30 ngày qua" hoặc chọn khoảng ngày tùy chỉnh.<br>4. Hệ thống thực thi các truy vấn tổng hợp dữ liệu (Aggregated Queries) có phân chỉ mục tối ưu và cập nhật lại biểu đồ hiển thị.<br>5. Admin có thể xuất báo cáo thống kê ra định dạng tệp chuẩn (CSV/PDF) để báo cáo cấp quản lý. |
| **Kịch bản phụ** | - **4a. Khoảng thời gian chọn không có dữ liệu ticket nào:** Hệ thống hiển thị biểu đồ rỗng kèm chú thích: "Không có dữ liệu phát sinh trong khoảng thời gian đã chọn". |
| **Ràng buộc phi chức năng** | - **Quy tắc nghiệp vụ:** Quyền hạn chỉ dành riêng cho Admin; dữ liệu thống kê không làm ảnh hưởng đến hiệu năng xử lý ticket trực tiếp.<br>- **Giao diện:** Màn hình `D01` (Bảng điều khiển quản trị - Node Figma `62:9943`, file `62-9943.png`).<br>- **Hiệu năng:** Tải toàn bộ bảng thống kê trong vòng $\le 2.0$ giây.<br>- **Mã kiểm thử:** TC-TK-12 (Mã giữ để đối soát P1; chưa được định nghĩa trong Test Matrix SRS 14.2, không coi là ca kiểm thử đã phê duyệt). |

---

# 5. BẢN MẪU PROTOTYPE & THIẾT KẾ GIAO DIỆN (UI PROTOTYPE & DESIGN SYSTEM)

Bộ giao diện tham chiếu: Quiet Workspace, Redesign v2; 33 nhóm màn hình chính, 151 frames và 56 prototype flows theo danh mục thiết kế. Light/Dark Mode và responsive là định hướng thiết kế; các hành vi tương tác phải tuân thủ quyền và workflow ở Mục 4.
[Mở thiết kế Figma chính thức - Node 49:58](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)
Ảnh nguồn sử dụng đường dẫn `docs/design/anh/` và `docs/design/anh/thanh-phan/`. Mỗi mục dưới ghi đúng Node Figma, tệp nguồn và vị trí chèn ảnh tương ứng.

---

### 5.1 Giao diện định danh và tài khoản
Thành viên phụ trách: Ngô Viết Thanh Bình

#### 5.1.1 Đăng nhập hệ thống
Biểu mẫu email và mật khẩu, thông báo lỗi chung, chuyển hướng theo vai trò. Không đưa Google OAuth vào phạm vi đăng nhập MVP.
Use Case: UC-01 | Node Figma: 62:8214
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-8214&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-8214.png
Vị trí chèn ảnh 62-8214.png
*Hình 5.1 Đăng nhập hệ thống*

#### 5.1.2 Đăng ký Customer
Biểu mẫu đăng ký dành cho khách chưa có tài khoản; hệ thống tự gán vai trò CUSTOMER ở phía máy chủ.
Use Case: UC-01 | Node Figma: 62:8215
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-8215&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-8215.png
Vị trí chèn ảnh 62-8215.png
*Hình 5.2 Đăng ký Customer*

#### 5.1.3 Hồ sơ cá nhân (Customer & Nhân viên/Quản trị viên)
Xem và cập nhật thông tin được phép của chính mình; đổi mật khẩu có kiểm tra mật khẩu hiện tại, không cho phép tự đổi vai trò.
Use Case: UC-03 | Node Figma: 62:8216, 62:8328
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-8216&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-8216.png, docs/design/anh/62-8328.png
Vị trí chèn ảnh 62-8216.png
*Hình 5.3a Hồ sơ cá nhân (Customer)*
Vị trí chèn ảnh 62-8328.png
*Hình 5.3b Hồ sơ cá nhân (Nhân viên / Quản trị viên)*

#### 5.1.4 Quản lý danh sách tài khoản Agent (Admin)
Quản trị viên xem danh sách nhân viên hỗ trợ, lọc theo trạng thái hoạt động và kích hoạt/vô hiệu hóa tài khoản Agent.
Use Case: UC-04 | Node Figma: 62:10225
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-10225&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-10225.png
Vị trí chèn ảnh 62-10225.png
*Hình 5.4 Quản lý danh sách nhân viên (Admin)*

#### 5.1.5 Tạo tài khoản Agent mới và Vô hiệu hóa tài khoản (Admin)
Quản trị viên tạo mới tài khoản Support Agent hoặc xác nhận vô hiệu hóa tài khoản Agent (thu hồi phiên đăng nhập hiện hành).
Use Case: UC-04 | Node Figma: 62:10226, 62:13238
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-10226&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-10226.png, docs/design/anh/62-13238.png
Vị trí chèn ảnh 62-10226.png
*Hình 5.5a Biểu mẫu tạo tài khoản nhân viên mới*
Vị trí chèn ảnh 62-13238.png
*Hình 5.5b Xác nhận vô hiệu hóa tài khoản nhân viên*

---

### 5.2 Giao diện Customer Portal
Thành viên phụ trách: Phan Gia Phúc và Lê Quý Phúc

#### 5.2.1 Danh sách yêu cầu của tôi
Chỉ hiển thị ticket do Customer hiện tại tạo; có phân trang, lọc và trạng thái rỗng.
Use Case: UC-09 | Node Figma: 58:6763
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=58-6763&m=dev)
Tệp ảnh nguồn: docs/design/anh/58-6763.png
Vị trí chèn ảnh 58-6763.png
*Hình 5.6 Danh sách yêu cầu của tôi*

#### 5.2.2 Tạo yêu cầu hỗ trợ
Nhập tiêu đề và mô tả. Đính kèm tệp thuộc P1, không phải điều kiện bắt buộc để tạo ticket P0.
Use Case: UC-05 | Node Figma: 58:6764
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=58-6764&m=dev)
Tệp ảnh nguồn: docs/design/anh/58-6764.png
Vị trí chèn ảnh 58-6764.png
*Hình 5.7 Tạo yêu cầu hỗ trợ*

#### 5.2.3 Chi tiết và hội thoại công khai (Đang xử lý)
Chỉ hiển thị PUBLIC messages; ẩn hoàn toàn INTERNAL notes đối với Customer.
Use Case: UC-09 | Node Figma: 58:6765
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=58-6765&m=dev)
Tệp ảnh nguồn: docs/design/anh/58-6765.png
Vị trí chèn ảnh 58-6765.png
*Hình 5.8 Chi tiết và hội thoại công khai (Đang xử lý)*

#### 5.2.4 Xác nhận Đóng hoặc Mở lại yêu cầu ( khi RESOLVED)
Khi ticket ở trạng thái RESOLVED, Customer được chọn xác nhận Đóng yêu cầu (CLOSE) hoặc Yêu cầu xử lý tiếp (REOPEN).
Use Case: UC-10 | Node Figma: 62:6953
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-6953&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-6953.png
Vị trí chèn ảnh 62-6953.png
*Hình 5.9 Yêu cầu đã giải quyết — Chờ Customer xác nhận Đóng hoặc Mở lại*

#### 5.2.5 Chi tiết yêu cầu đã đóng (CLOSED — Chỉ đọc)
Khi ticket đã chuyển sang trạng thái CLOSED, toàn bộ hội thoại chuyển sang chế độ chỉ đọc (read-only), khóa ô nhập phản hồi.
Use Case: UC-09, UC-10 | Node Figma: 62:6954
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-6954&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-6954.png
Vị trí chèn ảnh 62-6954.png
*Hình 5.10 Yêu cầu đã đóng (Chế độ chỉ đọc)*

---

### 5.3 Giao diện Agent Workspace
Thành viên phụ trách: Phan Gia Phúc

#### 5.3.1 Hàng đợi và nhận xử lý
Hiển thị OPEN queue; thao tác Claim nhận ticket nguyên tử. Chưa claim thì khóa soạn phản hồi của Agent.
Use Case: UC-06, UC-07 | Node Figma: 55:1992
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=55-1992&m=dev)
Tệp ảnh nguồn: docs/design/anh/55-1992.png
Vị trí chèn ảnh 55-1992.png
*Hình 5.11 Hàng đợi và nhận xử lý*

#### 5.3.2 Xử lý ticket và ghi chú nội bộ
Phân biệt PUBLIC và INTERNAL; chỉ Assigned Agent/Admin được tạo và xem INTERNAL notes.
Use Case: UC-07 | Node Figma: 55:2537
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=55-2537&m=dev)
Tệp ảnh nguồn: docs/design/anh/55-2537.png
Vị trí chèn ảnh 55-2537.png
*Hình 5.12 Xử lý ticket và ghi chú nội bộ*

#### 5.3.3 Xung đột nhận ticket
Thông báo ticket vừa được nhận, tải lại queue; không cho Agent thua claim tiếp tục xử lý ticket ngoài quyền.
Use Case: UC-06, UC-07 | Node Figma: 56:3104
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=56-3104&m=dev)
Tệp ảnh nguồn: docs/design/anh/56-3104.png
Vị trí chèn ảnh 56-3104.png
*Hình 5.13 Xung đột nhận ticket*

---

### 5.4 Giao diện Knowledge Base
Thành viên phụ trách: Đinh Vũ Nhật Huỳnh / Nguyễn Đức Lãm

#### 5.4.1 Tìm kiếm tri thức
Người dùng tìm trong tài liệu READY, published và chưa archive; hỗ trợ empty/error states.
Use Case: UC-13 | Node Figma: 62:9092
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9092&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9092.png
Vị trí chèn ảnh 62-9092.png
*Hình 5.14 Tìm kiếm tri thức*

#### 5.4.2 Đọc tài liệu tri thức
Hiển thị nội dung tài liệu được phép. Đánh giá bài viết không được dùng thay cho FR-AI-10 hoặc US-30 về đánh giá gợi ý AI.
Use Case: UC-13 | Node Figma: 62:9094
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9094&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9094.png
Vị trí chèn ảnh 62-9094.png
*Hình 5.15 Đọc tài liệu tri thức*

#### 5.4.3 Quản trị danh mục tài liệu
Admin xem danh mục và trạng thái; READY không đồng nghĩa đã published. Upload, publish và archive theo quyền.
Use Case: UC-11, UC-12 | Node Figma: 62:9240
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9240&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9240.png
Vị trí chèn ảnh 62-9240.png
*Hình 5.16 Quản trị danh mục tài liệu*

#### 5.4.4 Tải tài liệu mới lên Knowledge Base (Upload)
Biểu mẫu chọn tệp tài liệu (PDF/DOCX/TXT/MD, giới hạn kích thước $\le 10$ MiB) để đưa vào hàng đợi bóc tách và lập chỉ mục Vector bất đồng bộ.
Use Case: UC-11 | Node Figma: 62:9241
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9241&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9241.png
Vị trí chèn ảnh 62-9241.png
*Hình 5.17 Tải tài liệu mới lên Knowledge Base*

#### 5.4.5 Chi tiết tài liệu đã xử lý xong nhưng chưa công bố (READY — Unpublished)
Minh họa trạng thái tài liệu đã hoàn tất bóc tách và nhúng Vector (`READY`) nhưng đang chờ kiểm duyệt, chưa được công bố (`is_published = false`) cho tìm kiếm hoặc RAG.
Use Case: UC-11, UC-12 | Node Figma: 62:9783
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9783&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9783.png
Vị trí chèn ảnh 62-9783.png
*Hình 5.18 Chi tiết tài liệu ở trạng thái READY nhưng chưa công bố*

---

### 5.5 Giao diện AI và tham chiếu quản trị
Thành viên phụ trách: Lê Quý Phúc / Võ Minh Quân

#### 5.5.1 Gợi ý AI và trích dẫn
Agent chủ động yêu cầu tạo gợi ý; đọc nguồn, chèn và sửa trong editor. Chèn bản nháp không tự gửi.
Use Case: UC-08 | Node Figma: 55:1994
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=55-1994&m=dev)
Tệp ảnh nguồn: docs/design/anh/55-1994.png
Vị trí chèn ảnh 55-1994.png
*Hình 5.19 Gợi ý AI và trích dẫn*

#### 5.5.2 Đối chiếu nguồn trích dẫn
Mở nguồn/snapshot được phép để kiểm tra trước khi gửi; lịch sử nguồn giữ nguyên khi tài liệu archive.
Use Case: UC-08 | Node Figma: 56:3578
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=56-3578&m=dev)
Tệp ảnh nguồn: docs/design/anh/56-3578.png
Vị trí chèn ảnh 56-3578.png
*Hình 5.20 Đối chiếu nguồn trích dẫn*

#### 5.5.3 Danh sách tất cả yêu cầu (Admin)
Danh mục thiết kế ghi D01 là danh sách tất cả yêu cầu có bộ lọc toàn hệ thống dành cho Admin. Không xác nhận Node này là Dashboard Analytics; khung minh họa riêng cho Dashboard thống kê chưa được cung cấp trong bộ ảnh Redesign v2.
Use Case: UC-06, UC-09; tham chiếu UC-15 | Node Figma: 62:9943
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9943&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9943.png
Vị trí chèn ảnh 62-9943.png
*Hình 5.21 Danh sách tất cả yêu cầu quản trị (D01)*

#### 5.5.4 Xử lý, lịch sử yêu cầu và Phân công nhân viên (Admin)
Quản trị viên xem toàn bộ lịch sử xử lý (bao gồm cả INTERNAL notes) và thực hiện gán / chuyển người phụ trách (Assign / Reassign Agent) thủ công cho ticket.
Use Case: UC-06, UC-09, UC-10 | Node Figma: 62:9944, 62:9945
[Mở màn hình trong Figma](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=62-9944&m=dev)
Tệp ảnh nguồn: docs/design/anh/62-9944.png, docs/design/anh/62-9945.png
Vị trí chèn ảnh 62-9944.png
*Hình 5.22a Chi tiết xử lý và lịch sử yêu cầu (Admin — D02)*
Vị trí chèn ảnh 62-9945.png
*Hình 5.22b Biểu mẫu phân công nhân viên phụ trách (Admin — D03)*


