# 2. Mô hình quan niệm

## 2.1 Tổng quan Mô hình quan niệm (EER)

Mô hình quan niệm (Conceptual Data Model / Enhanced Entity-Relationship — EER) mô tả bức tranh dữ liệu nghiệp vụ của hệ thống Clarune phục vụ bài toán Chăm sóc khách hàng, Hỗ trợ kỹ thuật và Tra cứu chính sách bảo hành, đổi trả thiết bị điện tử tiêu dùng (Consumer Electronics) ở mức khái niệm, độc lập với hệ quản trị cơ sở dữ liệu PostgreSQL và chưa đưa các cột kỹ thuật cài đặt (như khóa ngoại thuần túy, chỉ mục vector hay bảng trung gian vật lý).

Mô hình áp dụng tổng quát hóa / chuyên biệt hóa (Generalization / Specialization) cho thực thể trung tâm Người dùng (User):

- Thực thể cha (User): Chứa các thuộc tính định danh dùng chung gồm email, fullName, passwordHash, enabled, createdAt.
- Ba thực thể con chuyên biệt (Disjoint, Total theo miền 3 vai trò MVP):

1. Khách hàng (Customer): Tác nhân tạo và theo dõi yêu cầu hỗ trợ (Ticket), gửi tin nhắn công khai, yêu cầu mở lại hoặc đóng yêu cầu.
2. Nhân viên hỗ trợ (Support Agent): Tác nhân xem hàng đợi mở, nhận xử lý (Claim) ticket, soạn ghi chú nội bộ, tra cứu tri thức và kiểm duyệt/đánh giá gợi ý AI.
3. Quản trị viên (System Administrator): Tác nhân quản lý tài khoản nhân viên, tải lên/công bố/lưu trữ tài liệu tri thức, phân công/chuyển giao ticket và xem thống kê vận hành (P1).

## 2.2 Sơ đồ Mô hình quan niệm

Hình 2.1 — Mô hình quan niệm (EER) của hệ thống Clarune theo ký pháp Chen.

Vòng tròn d và đường nối đôi thể hiện mỗi User thuộc đúng một trong ba kiểu con Customer, Support Agent và System Administrator. Cặp (min, max) ở mỗi đầu quan hệ biểu thị số lần tham gia tối thiểu và tối đa của một thể hiện thuộc thực thể tại đầu đó. Nhãn P1 và nét đứt đánh dấu các thực thể và quan hệ thuộc phạm vi mở rộng.

## 2.3 Đặc tả các thực thể ngữ nghĩa và mối quan hệ

### 2.3.1 Danh sách thực thể ngữ nghĩa

| STT | Tên thực thể | Loại thực thể | Thuộc tính nghiệp vụ cốt lõi | Định nghĩa ngữ nghĩa theo bài toán |
| --- | --- | --- | --- | --- |
| 1 | User | Thực thể cha (Supertype) | id, email, fullName, role, enabled, createdAt, updatedAt | Tài khoản định danh duy nhất theo email không phân biệt hoa thường, kiểm soát trạng thái kích hoạt (enabled). |
| 2 | Customer | Thực thể con (Subtype của User) | Kế thừa toàn bộ thuộc tính từ User (role = CUSTOMER) | Khách hàng sở hữu các Ticket của chính mình và chỉ được xem phần trao đổi công khai. |
| 3 | Support Agent | Thực thể con (Subtype của User) | Kế thừa toàn bộ thuộc tính từ User (role = AGENT) | Nhân viên hỗ trợ xem hàng đợi mở, nhận xử lý (claim) ticket, tra cứu tri thức và kiểm duyệt/đánh giá gợi ý AI. |
| 4 | System Administrator | Thực thể con (Subtype của User) | Kế thừa toàn bộ thuộc tính từ User (role = ADMIN) | Quản trị viên điều hành tài khoản Agent, vòng đời tài liệu tri thức, phân công/chuyển giao ticket và thống kê (P1). |
| 5 | AuthSession | Thực thể yếu / phụ thuộc User | id, expiresAt, revokedAt, createdAt, lastUsedAt | Phiên đăng nhập duy trì theo cơ chế xoay vòng mã gia hạn (Refresh Token Rotation). |
| 6 | PasswordResetToken *(P1)* | Thực thể mở rộng (PLANNED) | id, expiresAt, usedAt, createdAt | Mã đặt lại mật khẩu dùng một lần có thời hạn phục vụ UC-16 (P1). |
| 7 | Ticket | Thực thể trung tâm | id, ticketNumber, subject, status, priority, createdAt, updatedAt, resolvedAt, closedAt | Yêu cầu hỗ trợ do khách hàng tạo, có mã hiển thị duy nhất và được xử lý theo máy trạng thái gồm năm trạng thái. Thuộc tính subject tóm tắt vấn đề và có thể chứa mã model thiết bị. Ví dụ minh họa là “TV model TV-55A mất tiếng khi kết nối HDMI”. |
| 8 | TicketMessage | Thực thể phụ thuộc Ticket | id, body, visibility (PUBLIC/INTERNAL), createdAt | Tin nhắn trao đổi công khai (bao gồm nội dung mô tả đầu tiên) hoặc ghi chú nội bộ ẩn với khách hàng. |
| 9 | TicketEvent | Thực thể nhật ký phụ thuộc Ticket | id, eventType, oldValue, newValue, createdAt | Sự kiện lịch sử bất biến (append-only) ghi vết tạo, nhận, phân công và chuyển trạng thái. |
| 10 | KnowledgeDocument | Thực thể độc lập | id, title, originalFilename, mimeType, sizeBytes, status, published, failureCode, publishedAt, archivedAt | Tài liệu tri thức do Admin tải lên, chẳng hạn FAQ, hướng dẫn kỹ thuật hoặc chính sách bảo hành, đổi trả trong lĩnh vực đồ điện tử. Thuộc tính title là tiêu đề hiển thị của tài liệu. Ví dụ minh họa gồm “FAQ xử lý mất tiếng qua HDMI trên TV” và “Chính sách bảo hành và đổi trả TV”. Trạng thái xử lý READY và tình trạng công bố published được theo dõi riêng. |
| 11 | KnowledgeIngestionJob | Thực thể phụ thuộc KnowledgeDocument | id, status, attempts, maxAttempts, nextRunAt, lockedUntil, leaseToken, lastErrorCode | Tác vụ xử lý nền (trích xuất chữ, chia đoạn, tạo vector) có cơ chế lease và thử lại giới hạn tối đa 3 lần. |
| 12 | KnowledgeChunk | Thực thể phụ thuộc KnowledgeDocument | id, chunkIndex, pageNumber, content, createdAt | Đoạn văn bản được cắt kèm số thứ tự, số trang (nếu là PDF) và vector nhúng ngữ nghĩa. |
| 13 | AISuggestion | Thực thể phụ thuộc Ticket | id, status, suggestedText, modelName, promptVersion, latencyMs, errorCode, createdAt, appliedAt | Kết quả một lần yêu cầu AI sinh bản nháp (kể cả trạng thái thiếu căn cứ hoặc lỗi) kèm dấu vết mô hình. |
| 14 | AISuggestionSource | Thực thể liên kết + bản chụp | id, citationOrder, score, documentTitleSnapshot, excerptSnapshot, pageNumberSnapshot | Bản chụp (snapshot) đoạn trích nguồn tại thời điểm sinh gợi ý, đảm bảo lịch sử bất biến khi tài liệu gốc bị lưu trữ. |
| 15 | AISuggestionFeedback *(P1)* | Thực thể đánh giá chất lượng gợi ý AI (Mở rộng P1 — UC-19) | id, rating (HELPFUL/NOT_HELPFUL), createdAt, updatedAt | Đánh giá mức hữu ích hiện hành của nhân viên phụ trách đối với một gợi ý hợp lệ (UC-19, P1). |

### 2.3.2 Bảng mối quan hệ ngữ nghĩa và lực lượng (Cardinalities)

| Quan hệ (Verb) | Thực thể tham gia | Lực lượng (Min, Max) | Ý nghĩa nghiệp vụ &amp; Ràng buộc toàn vẹn |
| --- | --- | --- | --- |
| duy trì | User — AuthSession | (0,n) — (1,1) | Một người dùng có thể có nhiều phiên trên các thiết bị; mỗi phiên thuộc đúng 1 người dùng. |
| gửi (requests) | Customer — Ticket | (0,n) — (1,1) | Một khách hàng có thể tạo nhiều ticket; mỗi ticket bắt buộc do đúng 1 khách hàng tạo. |
| phụ trách (assigned) | Support Agent — Ticket | (0,n) — (0,1) | Một nhân viên hỗ trợ xử lý nhiều ticket; mỗi ticket ở trạng thái OPEN chưa có nhân viên (0), sau khi nhận/gán chỉ có tối đa 1 nhân viên phụ trách. |
| chứa (contains) | Ticket — TicketMessage | (1,n) — (1,1) | Mỗi ticket ngay khi tạo đã có tối thiểu 1 tin nhắn công khai đầu tiên chứa mô tả ban đầu của khách hàng. |
| viết (writes) | User — TicketMessage | (0,n) — (1,1) | Mỗi tin nhắn/ghi chú bắt buộc do đúng 1 người dùng xác thực viết; Customer không được viết INTERNAL. |
| ghi nhận (records) | Ticket — TicketEvent | (1,n) — (1,1) | Ngay khi tạo ticket đã có tối thiểu sự kiện TICKET_CREATED; tác nhân thay đổi có thể null nếu là sự kiện hệ thống. |
| tải lên (uploads) | System Administrator — KnowledgeDocument | (0,n) — (1,1) | Chỉ Admin được tải lên tài liệu; mỗi tài liệu gắn 1 người tải lên (UC-11). |
| được xử lý bởi | KnowledgeDocument — KnowledgeKnowledgeIngestionJob | (1,n) — (1,1) | Mỗi tài liệu sau tải lên tạo tối thiểu 1 tác vụ xử lý nền; tại một thời điểm chỉ có tối đa 1 job đang hoạt động (PENDING/RUNNING). |
| chia thành (contains) | KnowledgeDocument — KnowledgeChunk | (0,n) — (1,1) | Tài liệu chưa xong hoặc lỗi có 0 đoạn; tài liệu READY có 1..n đoạn duy nhất theo (document, chunkIndex). |
| nhận gợi ý (has) | Ticket — AISuggestion | (0,n) — (1,1) | Một ticket có thể yêu cầu AI gợi ý nhiều lần (hoặc 0 lần); mỗi gợi ý gắn cố định với 1 ticket. |
| yêu cầu tạo (requests) | User (Agent/Admin) — AISuggestion | (0,n) — (1,1) | Lưu vết nhân viên hoặc Admin đã bấm tạo gợi ý (requestedBy). |
| chuyển thành (applied as) | AISuggestion — TicketMessage | (0,1) — (0,1) | Một gợi ý tối đa chỉ được áp dụng thành 1 tin nhắn công khai duy nhất (chống áp dụng trùng lặp); tin nhắn soạn tay không gắn gợi ý (0). |
| dẫn nguồn (references) | AISuggestion — AISuggestionSource | (0,n) — (1,1) | Gợi ý INSUFFICIENT_EVIDENCE/FAILED có 0 nguồn; gợi ý GENERATED/APPLIED tham chiếu từ 1 nguồn trở lên. |
| được chụp từ (cited from) | KnowledgeChunk — AISuggestionSource | (0,n) — (1,1) | Lưu bản chụp trích dẫn từ đúng 1 chunk gốc; không xóa cứng chunk đã được trích dẫn. |
| thực hiện (triggers) | User — TicketEvent | (0,n) — (0,1) | Một người dùng có thể thực hiện nhiều sự kiện xử lý. Mỗi sự kiện gắn với tối đa một người dùng. Sự kiện do hệ thống ghi nhận có thể không gắn với người dùng. |
| yêu cầu đặt lại (requests reset - P1) | User — PasswordResetToken | (0,n) — (1,1) | Một người dùng có thể yêu cầu đặt lại mật khẩu nhiều lần; mỗi mã xác nhận khôi phục mật khẩu chỉ thuộc về đúng một người dùng. |
| đánh giá (evaluates - P1) | Support Agent — AISuggestionFeedback | (0,n) — (1,1) | Một nhân viên hỗ trợ có thể đánh giá nhiều gợi ý. Mỗi bản đánh giá thuộc đúng một nhân viên. Chỉ nhân viên đang phụ trách Ticket mới được đánh giá gợi ý của Ticket đó (UC-19). |
| Nhận đánh giá (P1) | AISuggestion — AISuggestionFeedback | (0,n) — (1,1) | Một gợi ý có thể chưa có đánh giá hoặc có nhiều đánh giá từ các nhân viên khác nhau. Mỗi bản đánh giá thuộc đúng một gợi ý. Chỉ gợi ý ở trạng thái GENERATED hoặc APPLIED được đánh giá. Mỗi cặp nhân viên–gợi ý có tối đa một đánh giá hiện hành (UC-19). |
