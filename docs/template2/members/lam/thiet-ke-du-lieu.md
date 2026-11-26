# 4. Thiết kế dữ liệu

## 4.1 Sơ đồ dữ liệu (Physical ERD)

Cơ sở dữ liệu sử dụng PostgreSQL 16 kết hợp extension pgvector. Lược đồ cơ sở dữ liệu vật lý tuân thủ các quy ước thiết kế nhất quán:

- Khóa chính chuẩn UUID, thời gian chuẩn TIMESTAMPTZ (UTC).
- Email so sánh không phân biệt chữ hoa/thường thông qua chuẩn hóa lowercase và unique index.
- Ánh xạ Enum Java bằng VARCHAR (STRING) kèm CHECK constraint tại SQL (không dùng ordinal integer).
- Quản lý phiên bản schema qua Flyway theo thứ tự tuyến tính V1 → V5. Để tránh tham chiếu vòng giữa ticket_messages (V2) và ai_suggestions (V4), cột nullable ticket_messages.source_suggestion_id được khai báo ở V2 nhưng khóa ngoại và unique partial index chỉ được bổ sung tại V5.

Hình 4.1 — Sơ đồ cơ sở dữ liệu vật lý của hệ thống Clarune.

Sơ đồ mô tả 10 bảng thuộc phạm vi P0 trên PostgreSQL 16 và pgvector. Các đường nối biểu diễn khóa ngoại và lực lượng theo ràng buộc dữ liệu. Ví dụ, ứng dụng tạo ticket cùng tin nhắn công khai đầu tiên và sự kiện tạo trong một giao dịch, dù khóa ngoại riêng lẻ cho phép ticket chưa có bản ghi con. Các giá trị mặc định, ràng buộc CHECK và chỉ mục được trình bày tại Mục 4.2. Sơ đồ và đặc tả bảng đã được thiết kế đồng bộ với bộ script Flyway V1–V5 của hệ thống cơ sở dữ liệu.

### Bảng thứ tự Migration Flyway (V1–V5 &amp; Phần mở rộng P1)

| Phiên bản Migration | Phạm vi bảng / đối tượng | Phụ thuộc &amp; Nguyên tắc kỹ thuật |
| --- | --- | --- |
| V1 (V1__init_identity.sql) | users, auth_sessions | Ứng dụng sinh UUID cho khóa chính trước khi ghi dữ liệu. Tài khoản Admin ban đầu được khởi tạo riêng qua cấu hình môi trường bảo mật của máy chủ |
| V2 (V2__init_ticketing.sql) | tickets, ticket_messages, ticket_events | Tạo cột ticket_messages.source_suggestion_id kiểu uuid, cho phép NULL. V5 bổ sung khóa ngoại và chỉ mục duy nhất có điều kiện sau khi V4 tạo bảng ai_suggestions. \| |
| V3 (V3__init_knowledge.sql) | Extension vector (pgvector), knowledge_documents, knowledge_ingestion_jobs, knowledge_chunks | Extension vector phải khả dụng trước khi tạo bảng knowledge_chunks. Cột knowledge_chunks.embedding được khai báo cố định là vector(768) NOT NULL (tạo từ mô hình nhúng 768 chiều của gemini-embedding-2). |
| V4 (V4__init_ai.sql) | ai_suggestions, ai_suggestion_sources | Tham chiếu tickets(id) (V2) và knowledge_chunks(id) (V3). |
| V5 (V5__add_ticket_message_suggestion_fk.sql) | ticket_messages (ALTER TABLE) | Bổ sung FK (source_suggestion_id) REFERENCES ai_suggestions(id) và UNIQUE INDEX WHERE source_suggestion_id IS NOT NULL chống apply 2 lần. |
| V6+ *(P1 — PLANNED)* | password_reset_tokens (UC-16), ai_suggestion_feedback (UC-19) | Chưa thuộc phạm vi P0; chỉ thêm file migration mới nếu nhóm mở rộng làm P1 (tuyệt đối không sửa đè V1–V5). |

## 4.2 Đặc tả dữ liệu (Data Dictionary)

### Danh mục tổng hợp các bảng

| STT | Tên bảng SQL | Flyway | Module | Mức | Mục đích lưu trữ |
| --- | --- | --- | --- | --- | --- |
| 1 | users | V1 | Identity | P0 | Tài khoản người dùng (Customer, Agent, Admin) |
| 2 | auth_sessions | V1 | Identity | P0 | Phiên Refresh Token dạng băm hỗ trợ xoay vòng &amp; thu hồi |
| 3 | tickets | V2 | Ticket | P0 | Thông tin lõi yêu cầu hỗ trợ, trạng thái và optimistic version |
| 4 | ticket_messages | V2, V5 | Ticket | P0 | Hội thoại công khai (kèm mô tả đầu) và ghi chú nội bộ |
| 5 | ticket_events | V2 | Ticket | P0 | Nhật ký sự kiện xử lý bất biến (append-only) |
| 6 | knowledge_documents | V3 | Knowledge | P0 | Siêu dữ liệu tài liệu tri thức (FAQ, Chính sách Đồ điện tử) |
| 7 | knowledge_ingestion_jobs | V3 | Knowledge | P0 | Hàng đợi &amp; lease job bóc tách, chunking, nhúng vector |
| 8 | knowledge_chunks | V3 | Knowledge | P0 | Các đoạn tri thức và vector nhúng pgvector |
| 9 | ai_suggestions | V4 | AI | P0 | Lịch sử các lần AI gợi ý, mô hình, độ trễ và trạng thái |
| 10 | ai_suggestion_sources | V4 | AI | P0 | Bản chụp trích dẫn nguồn tại thời điểm sinh gợi ý |
| 11 | password_reset_tokens | V6+ (Dự kiến) | Identity | P1 (PLANNED) | Token đặt lại mật khẩu dùng một lần có thời hạn (UC-16) |
| 12 | ai_suggestion_feedback | V6+ (Dự kiến) | AI | P1 (PLANNED) | Đánh giá Hữu ích / Không hữu ích của Agent (UC-19) |

### Bảng 4.1: users (Module Identity)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính định danh người dùng |
| 2 | email | varchar(255) | UNIQUE (normalized), NOT NULL | Địa chỉ email đăng nhập (chuẩn hóa chữ thường, không phân biệt hoa/thường) |
| 3 | password_hash | varchar(255) | NOT NULL | Mật khẩu đã băm một chiều (BCrypt), tuyệt đối không lưu thô |
| 4 | full_name | varchar(120) | NOT NULL | Họ và tên hiển thị của người dùng |
| 5 | role | varchar(20) | NOT NULL, CHECK (role IN ('CUSTOMER', 'AGENT', 'ADMIN')) | Vai trò phân quyền hệ thống |
| 6 | enabled | boolean | NOT NULL, DEFAULT true | Cờ kích hoạt tài khoản (false sẽ chặn login, refresh và access JWT còn hạn) |
| 7 | created_at | timestamptz | NOT NULL | Thời điểm tạo tài khoản (UTC) |
| 8 | updated_at | timestamptz | NOT NULL | Thời điểm cập nhật thông tin gần nhất (UTC) |

Chỉ mục (Indexes): PK(id), UNIQUE INDEX idx_users_email_lower ON users (LOWER(email)).

### Bảng 4.2: auth_sessions (Module Identity)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính phiên đăng nhập |
| 2 | user_id | uuid | FK -> users(id), NOT NULL | Người dùng sở hữu phiên |
| 3 | refresh_token_hash | varchar(128) | UNIQUE, NOT NULL | Mã băm SHA-256 của Refresh Token ngẫu nhiên có entropy cao |
| 4 | expires_at | timestamptz | NOT NULL | Mốc thời gian hết hạn phiên (UTC) |
| 5 | revoked_at | timestamptz | NULL | Thời điểm thu hồi do logout, token rotation hoặc disable tài khoản |
| 6 | created_at | timestamptz | NOT NULL | Thời điểm cấp phiên ban đầu (audit) |
| 7 | last_used_at | timestamptz | NULL | Thời điểm sử dụng gần nhất (audit) |

Chỉ mục (Indexes): PK(id), UNIQUE(refresh_token_hash), INDEX (user_id, revoked_at).

### Bảng 4.3: tickets (Module Ticket)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính định danh ticket |
| 2 | ticket_number | varchar(32) | UNIQUE, NOT NULL | Mã hiển thị duy nhất (VD: HD-1054) |
| 3 | requester_id | uuid | FK -> users(id), NOT NULL | Khách hàng gửi yêu cầu hỗ trợ |
| 4 | assigned_agent_id | uuid | FK -> users(id), NULL (khi OPEN) | Nhân viên hỗ trợ phụ trách hiện tại (NULL khi đang mở hàng đợi) |
| 5 | subject | varchar(150) | NOT NULL, CHECK (char_length(subject) >= 5) | Tiêu đề tóm tắt sự cố thiết bị điện tử (VD: "TV 4K 55 inch không lên nguồn"; mô tả chi tiết ban đầu nằm ở tin nhắn công khai đầu tiên) |
| 6 | status | varchar(30) | NOT NULL, CHECK (status IN ('OPEN', 'IN_PROGRESS', 'WAITING_CUSTOMER', 'RESOLVED', 'CLOSED')) | Trạng thái vòng đời ticket |
| 7 | priority | varchar(10) | NOT NULL, DEFAULT 'NORMAL', CHECK (priority IN ('LOW', 'NORMAL', 'HIGH')) | Mức độ ưu tiên (giá trị URGENT không tồn tại trong MVP; P0 mặc định NORMAL, thao tác đổi mức ưu tiên thuộc Backlog/P1) |
| 8 | version | bigint | NOT NULL, DEFAULT 0 | Số phiên bản phục vụ Optimistic Locking chống double-claim/lost update |
| 9 | created_at | timestamptz | NOT NULL | Thời điểm khởi tạo ticket (UTC) |
| 10 | updated_at | timestamptz | NOT NULL | Thời điểm cập nhật gần nhất (UTC) |
| 11 | resolved_at | timestamptz | NULL | Thời điểm chuyển trạng thái RESOLVED |
| 12 | closed_at | timestamptz | NULL | Thời điểm chuyển trạng thái CLOSED |

Chỉ mục (Indexes): (requester_id, created_at DESC), (assigned_agent_id, status, updated_at DESC), (status, created_at DESC), UNIQUE(ticket_number).

### Bảng 4.4: ticket_messages (Module Ticket)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính tin nhắn |
| 2 | ticket_id | uuid | FK -> tickets(id), NOT NULL | Ticket chứa nội dung trao đổi |
| 3 | author_id | uuid | FK -> users(id), NOT NULL | Tác giả tin nhắn (xác định từ ActorPrincipal) |
| 4 | body | text | NOT NULL | Nội dung tin nhắn (1–5000 ký tự) |
| 5 | visibility | varchar(10) | NOT NULL, CHECK (visibility IN ('PUBLIC', 'INTERNAL')) | Phạm vi hiển thị; Customer chỉ được query visibility = 'PUBLIC' |
| 6 | source_suggestion_id | uuid | NULL, FK -> ai_suggestions(id) (thêm ở V5) | Tham chiếu gợi ý AI nếu tin nhắn gửi qua luồng duyệt AI (UC-15) |
| 7 | created_at | timestamptz | NOT NULL | Thời điểm gửi tin nhắn (UTC) |

Chỉ mục (Indexes): INDEX (ticket_id, created_at, id), UNIQUE INDEX idx_msg_source_suggestion_unique ON ticket_messages (source_suggestion_id) WHERE source_suggestion_id IS NOT NULL (hàng rào DB ngăn chặn gửi lặp từ cùng 1 gợi ý AI).

### Bảng 4.5: ticket_events (Module Ticket)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính sự kiện lịch sử |
| 2 | ticket_id | uuid | FK -> tickets(id), NOT NULL | Ticket phát sinh sự kiện |
| 3 | actor_id | uuid | FK -> users(id), NULL (cho sự kiện hệ thống) | Người thực hiện thao tác |
| 4 | event_type | varchar(40) | NOT NULL | Loại sự kiện lịch sử (TICKET_CREATED, CLAIMED, ASSIGNED, REASSIGNED, STATUS_CHANGED; riêng PRIORITY_CHANGED thuộc Backlog/P1 vì P0 mặc định NORMAL) |
| 5 | old_value | jsonb | NULL | Giá trị cấu trúc trước thay đổi (không lưu secrets) |
| 6 | new_value | jsonb | NULL | Giá trị cấu trúc sau thay đổi (không lưu secrets) |
| 7 | created_at | timestamptz | NOT NULL | Thời điểm ghi nhận sự kiện đồng transaction |

Chỉ mục (Indexes): INDEX (ticket_id, created_at ASC).

### Bảng 4.6: knowledge_documents (Module Knowledge)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính tài liệu tri thức |
| 2 | title | varchar(200) | NOT NULL | Tiêu đề tài liệu hiển thị trên KB &amp; citation |
| 3 | original_filename | varchar(255) | NOT NULL | Tên tệp gốc đã được làm sạch ký tự điều khiển |
| 4 | storage_key | varchar(500) | UNIQUE, NOT NULL | Khóa đường dẫn nội bộ do máy chủ sinh trong Private Storage |
| 5 | mime_type | varchar(100) | NOT NULL | Định dạng MIME thực tế (application/pdf, text/plain, text/markdown) |
| 6 | size_bytes | bigint | NOT NULL, CHECK (size_bytes > 0 AND size_bytes &lt;= 10485760) | Dung lượng tệp tính bằng byte (≤ 10 MiB) |
| 7 | content_hash | varchar(64) | NOT NULL | Mã SHA-256 nội dung hỗ trợ phát hiện file trùng lặp |
| 8 | status | varchar(20) | NOT NULL, CHECK (status IN ('UPLOADED', 'PROCESSING', 'READY', 'FAILED', 'ARCHIVED')) | Trạng thái bóc tách / lưu trữ tài liệu |
| 9 | published | boolean | NOT NULL, DEFAULT false | Chỉ true khi Admin công bố sau khi READY; ràng buộc CHECK: status != \\x27ARCHIVED\\x27 OR published = false |
| 10 | uploaded_by | uuid | FK -> users(id), NOT NULL | Admin tải lên tài liệu |
| 11 | published_at | timestamptz | NULL | Mốc thời gian công bố |
| 12 | archived_at | timestamptz | NULL | Mốc thời gian đưa vào lưu trữ |
| 13 | failure_code | varchar(100) | NULL | Mã lỗi an toàn khi bóc tách thất bại (không lộ stack trace) |
| 14 | created_at | timestamptz | NOT NULL | Thời điểm tạo bản ghi (UTC) |
| 15 | updated_at | timestamptz | NOT NULL | Thời điểm cập nhật trạng thái gần nhất (UTC) |

### Bảng 4.7: knowledge_ingestion_jobs (Module Knowledge)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính tác vụ xử lý nền |
| 2 | document_id | uuid | FK -> knowledge_documents(id), NOT NULL | Tài liệu cần bóc tách và tạo vector |
| 3 | status | varchar(20) | NOT NULL, CHECK (status IN ('PENDING', 'RUNNING', 'COMPLETED', 'FAILED')) | Trạng thái tác vụ xử lý của worker |
| 4 | attempts | int | NOT NULL, DEFAULT 0 | Số lần đã nhận chạy (tăng ngay khi worker nhận job) |
| 5 | max_attempts | int | NOT NULL, DEFAULT 3 | Giới hạn số lần thử tối đa (mặc định 3) |
| 6 | next_run_at | timestamptz | NOT NULL | Thời điểm dự kiến chạy lại theo backoff |
| 7 | locked_until | timestamptz | NULL | Thời điểm hết hạn lease hiện tại |
| 8 | lease_token | uuid | NULL | Token ngẫu nhiên sinh mỗi lần nhận job để chặn worker cũ hết hạn ghi đè |
| 9 | last_error_code | varchar(100) | NULL | Mã lỗi của lần thử gần nhất |
| 10 | created_at | timestamptz | NOT NULL | Thời điểm khởi tạo tác vụ xử lý nền (UTC) |
| 11 | updated_at | timestamptz | NOT NULL | Thời điểm cập nhật trạng thái tác vụ gần nhất (UTC) |

Chỉ mục (Indexes): UNIQUE INDEX idx_ingestion_one_active_job ON knowledge_ingestion_jobs (document_id) WHERE status IN ('PENDING', 'RUNNING') (đảm bảo tối đa 1 job hoạt động cho mỗi tài liệu).

### Bảng 4.8: knowledge_chunks (Module Knowledge)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính đoạn tri thức |
| 2 | document_id | uuid | FK -> knowledge_documents(id), NOT NULL | Tài liệu nguồn sở hữu đoạn trích |
| 3 | chunk_index | int | NOT NULL, CHECK (chunk_index >= 0) | Thứ tự tuần tự của đoạn trong tài liệu |
| 4 | page_number | int | NULL (với TXT/MD) | Số trang trong PDF phục vụ hiển thị vị trí nguồn trích dẫn |
| 5 | content | text | NOT NULL | Nội dung văn bản thuần của đoạn tri thức |
| 6 | embedding | vector(768) | NOT NULL | Vector biểu diễn ngữ nghĩa pgvector dùng cho Cosine Search |
| 7 | created_at | timestamptz | NOT NULL | Thời điểm lập chỉ mục (UTC) |

Chỉ mục (Indexes): UNIQUE (document_id, chunk_index). Lưu ý về chỉ mục Vector (HNSW/IVFFlat): Hệ thống sử dụng phương pháp tìm kiếm láng giềng gần nhất chính xác (exact nearest-neighbor) phù hợp với quy mô tập dữ liệu hiện tại và chỉ khởi tạo chỉ mục HNSW/IVFFlat sau khi đo kiểm hiệu năng thực tế.

Mỗi kho vector sử dụng cùng một mô hình embedding, số chiều và chế độ chạy. Chế độ giả lập (Mock) và thực tế (Live) được phân tách qua cấu hình môi trường của ứng dụng (biến AI_MODE), đảm bảo tính nhất quán của không gian vector trong bảng knowledge_chunks mà không cần lưu phân tách cột vật lý. Khi đổi mô hình hoặc số chiều, cần tạo kho vector riêng hoặc tạo lại embedding cho toàn bộ đoạn tri thức liên quan trước khi dùng kho đó để tìm kiếm.

Với bộ FAQ và chính sách đồ điện tử của MVP, hệ thống dùng tìm kiếm chính xác theo khoảng cách cosine trên các tài liệu đủ điều kiện truy xuất. Nếu đánh giá thực tế cho thấy hệ thống thường bỏ sót mã model hoặc mã lỗi, nhóm có thể khảo sát tìm kiếm lai kết hợp đối sánh từ khóa và vector. Hướng này nằm ngoài baseline V1–V5 và chưa đưa cột tsvector vào thiết kế dữ liệu P0.

### Bảng 4.9: ai_suggestions (Module AI)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính bản ghi gợi ý AI |
| 2 | ticket_id | uuid | FK -> tickets(id), NOT NULL | Ticket cần hỗ trợ sinh phản hồi |
| 3 | requested_by | uuid | FK -> users(id), NOT NULL | Nhân viên hoặc Admin yêu cầu sinh gợi ý |
| 4 | status | varchar(30) | NOT NULL, CHECK (status IN ('GENERATED', 'INSUFFICIENT_EVIDENCE', 'FAILED', 'APPLIED', 'DISCARDED')) | Trạng thái kiểm duyệt/kết quả của gợi ý |
| 5 | suggested_text | text | NULL (khi INSUFFICIENT_EVIDENCE/FAILED) | Bản nháp nội dung câu trả lời AI đề xuất |
| 6 | model_name | varchar(120) | NULL (khi nhánh thiếu căn cứ INSUFFICIENT_EVIDENCE dừng trước khi gọi LLM, khi lỗi hoặc chạy chế độ mô phỏng) | Tên mô hình LLM đã tạo gợi ý |
| 7 | prompt_version | varchar(50) | NOT NULL | Mã phiên bản system prompt |
| 8 | latency_ms | int | NULL | Tổng thời gian thực thi (mili giây) |
| 9 | error_code | varchar(100) | NULL | Mã lỗi an toàn khi provider lỗi/timeout hoặc từ chối citation |
| 10 | created_at | timestamptz | NOT NULL | Thời điểm tạo gợi ý (UTC) |
| 11 | applied_at | timestamptz | NULL | Thời điểm Agent duyệt gửi phản hồi công khai |

Chỉ mục (Indexes): INDEX (ticket_id, created_at DESC).

### Bảng 4.10: ai_suggestion_sources (Module AI)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính nguồn trích dẫn của gợi ý |
| 2 | suggestion_id | uuid | FK -> ai_suggestions(id), NOT NULL | Gợi ý AI sử dụng trích dẫn này |
| 3 | chunk_id | uuid | FK -> knowledge_chunks(id), NOT NULL | Đoạn tri thức gốc (không hard delete khi đã có citation tham chiếu) |
| 4 | citation_order | int | NOT NULL, CHECK (citation_order >= 1) | Thứ tự xuất hiện nguồn (\[1\], \[2\], ...) |
| 5 | score | double precision | NULL | Độ tương đồng cosine tại thời điểm truy xuất |
| 6 | document_title_snapshot | varchar(200) | NOT NULL | Bản chụp tiêu đề tài liệu tại lúc sinh gợi ý |
| 7 | excerpt_snapshot | text | NOT NULL | Bản chụp đoạn trích văn bản (giới hạn độ dài), giữ nguyên dù tài liệu bị archive |
| 8 | page_number_snapshot | int | NULL | Bản chụp số trang tài liệu tại lúc sinh gợi ý |

### Các bảng mở rộng giai đoạn P1

Hai bảng dưới đây phục vụ chức năng khôi phục mật khẩu qua email (UC-16) và đánh giá mức độ hữu ích của gợi ý AI (UC-19) thuộc giai đoạn mở rộng P1 của hệ thống.

### Bảng 4.11: password_reset_tokens (Mở rộng P1 — Module Identity)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính định danh mã khôi phục mật khẩu |
| 2 | user_id | uuid | FK -> users(id), NOT NULL | Tài khoản người dùng yêu cầu đặt lại mật khẩu |
| 3 | token_hash | varchar(128) | UNIQUE, NOT NULL | Mã băm một chiều (SHA-256) của mã xác nhận khôi phục |
| 4 | expires_at | timestamptz | NOT NULL | Thời điểm hết hạn của mã khôi phục (UTC) |
| 5 | used_at | timestamptz | NULL | Thời điểm mã đã được sử dụng thành công (chống dùng lại) |
| 6 | created_at | timestamptz | NOT NULL | Thời điểm phát hành mã khôi phục (UTC) |

### Bảng 4.12: ai_suggestion_feedback (Mở rộng P1 — Module AI)

| STT | Thuộc tính | Kiểu dữ liệu | Khóa / Ràng buộc | Ý nghĩa / Mô tả |
| --- | --- | --- | --- | --- |
| 1 | id | uuid | PK, NOT NULL | Khóa chính bản ghi đánh giá chất lượng gợi ý AI |
| 2 | suggestion_id | uuid | FK -> ai_suggestions(id), NOT NULL | Bản ghi gợi ý AI được nhân viên hỗ trợ đánh giá |
| 3 | agent_id | uuid | FK -> users(id), NOT NULL | Nhân viên hỗ trợ thực hiện đánh giá (UNIQUE cùng suggestion_id) |
| 4 | rating | varchar(20) | NOT NULL, CHECK (rating IN ('HELPFUL', 'NOT_HELPFUL')) | Mức đánh giá chất lượng gợi ý (Hữu ích hoặc Không hữu ích) |
| 5 | created_at | timestamptz | NOT NULL | Thời điểm gửi đánh giá lần đầu (UTC) |
| 6 | updated_at | timestamptz | NOT NULL | Thời điểm cập nhật lựa chọn đánh giá gần nhất (UTC) |
