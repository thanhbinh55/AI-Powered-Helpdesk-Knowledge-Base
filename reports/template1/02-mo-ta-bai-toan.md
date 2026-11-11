# 2 Mô tả bài toán

## 2.1 Bối cảnh và vấn đề

Trong một đơn vị hỗ trợ, khách hàng gửi các câu hỏi, yêu cầu hoặc sự cố cần được tiếp nhận và xử lý có người phụ trách. Nếu trao đổi phân tán qua nhiều nơi, khách hàng khó theo dõi tiến độ; nhân viên dễ nhận trùng yêu cầu, bỏ sót thông tin hoặc mất dấu lịch sử xử lý. Tài liệu chính sách và hướng dẫn phân tán cũng khiến nhân viên mất thời gian tìm căn cứ và có thể trả lời không nhất quán.

Mô hình ngôn ngữ có thể hỗ trợ soạn nội dung nhưng có nguy cơ tạo thông tin thiếu căn cứ. Vì vậy, hệ thống Clarune (AI-Powered Helpdesk &amp; Knowledge Base System) kết hợp quản lý ticket với kho tri thức được kiểm duyệt để tạo gợi ý có nguồn, đồng thời giữ quyền quyết định gửi phản hồi ở nhân viên. Việc xác minh mã nguồn trích dẫn giúp kiểm tra nguồn gốc; nhân viên vẫn cần đối chiếu nội dung vì mã trích dẫn đúng chưa chứng minh toàn bộ câu trả lời đúng.

## 2.2 Mục tiêu, phạm vi và đối tượng sử dụng

Customer tạo và theo dõi ticket của mình, trao đổi công khai với bộ phận hỗ trợ. Agent xem hàng đợi để nhận việc và xử lý ticket được giao. Admin quản lý Agent, phân công ticket và công bố hoặc lưu trữ tài liệu tri thức. Guest là tác nhân trước xác thực, không phải vai trò tài khoản thứ tư.

Kho tri thức tiếp nhận PDF có lớp văn bản, TXT và Markdown. Worker xử lý nền để trích xuất, chia đoạn và tạo embedding. Tài liệu chỉ được dùng cho truy xuất mới khi READY, đã published và chưa archived. Khi có yêu cầu, trợ lý AI sử dụng ngữ cảnh công khai cần thiết và các đoạn nguồn hợp lệ để tạo nháp hoặc trả INSUFFICIENT_EVIDENCE nếu thiếu căn cứ. Nhân viên đọc nguồn, chỉnh sửa và chủ động gửi; AI không tự tạo message, đổi trạng thái hoặc phân công ticket. Khi AI gặp sự cố, các nghiệp vụ ticket vẫn hoạt động.

| Mã | Mục tiêu | Bằng chứng dự kiến |
| --- | --- | --- |
| OBJ-01 | Customer tạo và theo dõi ticket của mình | Demo đầu cuối; kiểm tra dữ liệu hiển thị đúng người sở hữu |
| OBJ-02 | Nhân viên xử lý theo workflow rõ ràng | Kiểm tra chuyển trạng thái và lịch sử ticket |
| OBJ-03 | Không nhận trùng ticket khi nhiều Agent thao tác | Kiểm thử nhận việc đồng thời; chỉ một người thắng |
| OBJ-04 | Admin quản lý tài liệu được dùng cho AI | Demo tải lên, xử lý, công bố, lưu trữ và loại nguồn không hợp lệ |
| OBJ-05 | AI gợi ý có citation và biết thiếu căn cứ | Bộ câu hỏi đánh giá, kiểm nguồn và nhánh abstention |
| OBJ-06 | Có thể chạy lại dự án và truy vết đóng góp | Docker Compose, README, CI và bằng chứng task/PR thực tế |

P0 gồm xác thực và phân quyền, quản lý ticket, kho tri thức và trợ lý AI có người duyệt, bao gồm xem lịch sử gợi ý. P1 gồm các mở rộng như đặt lại mật khẩu, tệp đính kèm, thống kê ticket, OCR/quản lý phiên bản tài liệu và đánh giá gợi ý AI.

## 2.3 Môi trường vận hành và ràng buộc

Hệ thống là ứng dụng web responsive phục vụ một đơn vị, truy cập bằng trình duyệt. Frontend React/TypeScript giao tiếp REST với backend Spring Boot 3 trên Java 21; backend tổ chức theo Modular Monolith. PostgreSQL và pgvector lưu dữ liệu và vector phục vụ truy xuất; tài liệu gốc nằm trong private storage. Docker Compose và hướng dẫn cấu hình phục vụ tái lập môi trường. Dịch vụ AI có chế độ mock để kiểm thử và trình diễn không phụ thuộc provider bên ngoài.

MVP giới hạn ba vai trò Customer, Agent, Admin; kiểm tra quyền ở backend. File tri thức tối đa 10 MiB; chưa xử lý OCR cho PDF scan trong P0. Dữ liệu demo là dữ liệu giả lập hoặc được phép sử dụng; chỉ gửi dữ liệu cần thiết cho model, không gửi INTERNAL notes mặc định hoặc secrets. Không mở rộng sang CRM, thanh toán, tổng đài, SLA phức tạp, multi-tenancy, mobile native hoặc AI tự xử lý ticket.

Các chỉ tiêu hiệu năng và chất lượng cần được đánh giá bằng kiểm thử có ghi nhận điều kiện đo; ảnh giao diện chỉ minh họa thiết kế.
