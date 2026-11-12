# Hợp đồng kỹ thuật MVP P0 — baseline để triển khai 09–22/11/2026

> Cập nhật 03/11/2026. Đây là thiết kế cần cài đặt và kiểm chứng, không phải báo cáo tính năng đã chạy. Yêu cầu nghiệp vụ và ID chuẩn ở [SRS-master.md](SRS-master.md); lịch và phân công ở [kế hoạch](../PLAN_TEMPLATE1_AND_DEVELOPMENT.md). P1 vẫn có đặc tả nhưng chưa nằm trong cam kết code trước 22/11.

> Đồng bộ nghiệp vụ ngày 12/11/2026 theo [Report.pdf](template1/report/Report.pdf) và [report.md](template1/report/report.md). UC-18 (lịch sử gợi ý) là P0; UC-16/17/19 là P1. FR-AI-10 chỉ lưu/đổi đánh giá Hữu ích/Không hữu ích, không có dashboard chất lượng AI.

## 1. Chủ sở hữu và cách thay đổi contract

| Phạm vi | Người thực hiện chính | Người phối hợp / review |
|---|---|---|
| Principal, security, Identity, Axios auth | Bình | Quý Phúc review; các owner kiểm tra quyền module mình |
| DTO/error/OpenAPI và luồng gửi suggestion | Gia Phúc điều phối; mỗi owner viết phần mình | Bình review quyền; Quý Phúc review suggestion; Lãm review nguồn |
| Flyway baseline V1–V5 | Lãm điều phối; owner viết schema module mình | Bình review thứ tự/FK; Gia Phúc kiểm tra clean DB |
| CI | Quý Phúc | Bình review; mỗi owner cung cấp command test của mình |
| Test PostgreSQL, smoke môi trường sạch | Gia Phúc điều phối test, Lãm chạy clean environment | Bình hỗ trợ cấu hình |
| Ingestion/retrieval và EmbeddingProvider | Lãm sở hữu API và fake; Quý Phúc làm adapter live dùng chung | Bình review transaction/config; không có provider thứ hai trong module AI |
| RAG và suggestion lifecycle | Quý Phúc | Gia Phúc review apply; Lãm hỗ trợ bộ dữ liệu có nhãn |

Tên chính là `identity`, `ticket`, `knowledge`, `ai`. Chữ A–D chỉ là nhãn tài liệu cũ. Không truyền entity JPA hoặc dùng repository chéo module. Đổi contract cần cập nhật SRS, JSON/OpenAPI, fake, caller và test trong cùng PR hoặc chuỗi PR có thứ tự rõ. Mỗi contract phải có mẫu thành công, empty và lỗi; fake và triển khai thật chạy cùng kiểm tra contract. API dùng camelCase, SQL dùng snake_case.

## 2. Principal, phiên và quyền

- `Actor(userId, role)` lấy từ access JWT đã xác minh, không nhận `actorId`, `authorId`, `role` từ request để cấp quyền. Backend kiểm tra `users.enabled` cho mỗi request cần xác thực; disabled từ chối cả access token còn hạn, refresh và login. `enabled` không chỉ lấy từ claim cũ.
- Access token tối đa 15 phút (cấu hình được). Logout thu hồi refresh session; access token đã cấp có thể còn hạn tới 15 phút theo FR-ID-05. Không tuyên bố logout thu hồi access token tức thì.
- Refresh token ngẫu nhiên entropy cao, chỉ lưu hash ở DB, rotation nguyên tử; token cũ không dùng lại. Thiết kế browser: access token trong memory; refresh trong cookie HttpOnly, SameSite=Lax, Secure khi HTTPS. Refresh/logout dùng POST và bảo vệ CSRF, whitelist origin khi dùng credentials; local HTTP phải có cấu hình dev riêng. Không lưu refresh token vào localStorage. Chốt cấu hình origin/cookie/CSRF trước DEV-0; kiểm tra cả trường hợp cookie không được gửi.
- Axios refresh dùng một request đang chạy chung cho các 401 đồng thời; chỉ retry request gốc một lần. Không refresh đệ quy cho login/refresh, không retry mù request gửi message; lỗi cuối xóa phiên phía client và yêu cầu đăng nhập lại.
- Chỉ register/login/refresh và các endpoint public đã liệt kê được cấu hình public ở HTTP layer. Profile/change-password phải authenticated; logout phải xác thực refresh session và CSRF. Không dùng `permitAll('/auth/**')` thay cho thiết kế quyền từng endpoint.
- Policy tài nguyên: thiếu token/không hợp lệ → 401; sai role ở endpoint chung hoặc account disabled → 403; tài nguyên không tồn tại hoặc không có quyền theo ownership → 404 với body thống nhất. Không để kết quả claim tiết lộ ticket Agent khác đang giữ.

| Tài nguyên / thao tác | Customer | Agent | Admin |
|---|---|---|---|
| Ticket list/detail | Chỉ own, public thread | OPEN queue để quyết định claim; ticket đang assigned cho mình | Tất cả |
| Message public / transition | Own và đúng state | Assigned và đúng state | Đúng state |
| Internal note / event history | Không có quyền | Chỉ assigned | Có quyền |
| Suggestion list/detail/generate/discard/apply và citation snapshot | Không có quyền | Chỉ ticket hiện đang assigned; generate/apply phải chưa CLOSED | Theo state và nghiệp vụ |
| KB list/detail/download | Không có quyền | Chỉ READY + published + chưa archive | Quản trị tài liệu |
| Upload/publish/archive/retry | Không có quyền | Không có quyền | Có quyền, kiểm tra state |

Reassign làm Agent cũ mất quyền truy cập các endpoint suggestion, snapshot và file của ticket đó ngay ở request kế tiếp. Agent mới có thể duyệt suggestion đã GENERATED của ticket; `requested_by` là audit, không thay thế quyền assigned hiện tại. Recheck quyền tại transaction gửi/discard, không tin quyền lúc generate. Snapshot nguồn lịch sử có thể xem theo quyền ticket dù document đã archive; nó không mở quyền download file gốc đã bị ẩn. Customer chỉ nhận text Agent chủ động gửi, không nhận raw prompt, internal note hoặc snapshot nội bộ tự động.

## 3. Schema và Flyway

[SRS Mục 10](SRS-master.md) là từ điển SQL chuẩn:

| Dữ liệu | Tên chuẩn |
|---|---|
| Ticket | `requester_id`, `subject`, `version`; description ban đầu lấy từ public message đầu tiên |
| Message | `author_id`, `body`, `visibility=PUBLIC/INTERNAL`, `source_suggestion_id` |
| Document | `original_filename`, `storage_key`, `size_bytes`, `status`, `published` boolean |
| Job | `status=PENDING/RUNNING/COMPLETED/FAILED`, `attempts`, `max_attempts`, `next_run_at`, `locked_until`, `lease_token`, `last_error_code` |
| Chunk | `content`, `chunk_index`, `page_number`, `embedding` |
| Suggestion | `requested_by`, `suggested_text`, `status` gồm cả FAILED; metadata model/prompt/error |
| Source snapshot | `document_title_snapshot`, `excerpt_snapshot`, `page_number_snapshot`, `chunk_id` |

Không tạo thêm `publish_status`, job `PROCESSING`, `retry_count` hoặc `content_text` theo kế hoạch cũ. Document dùng PROCESSING; job dùng RUNNING. Enum Java ánh xạ string. Document ARCHIVED thì `published=false`; publish chỉ khi READY. Không hard delete document/chunk đã được citation tham chiếu. MVP không hỗ trợ re-ingest tài liệu READY; muốn thay nội dung phải upload document mới để giữ nguồn cũ.

09–10/11: một PR phối hợp schema nền, chạy theo V1 Identity → V2 Ticket → V3 Knowledge → V4 AI → V5 FK `ticket_messages.source_suggestion_id`. V2 tạo cột nullable chưa gắn FK AI; V5 thêm FK sau V4. Extension `vector` phải tồn tại trước cột vector. Lãm xác nhận model/dimension với Quý Phúc trước khi áp dụng V3; `D` là ký hiệu thiết kế, không phải literal SQL hay biến môi trường có thể đổi schema lúc chạy. Nếu chưa chốt phải ghi blocker, không giả vờ DEC-06 đã đóng.

Mỗi version duy nhất; sau khi áp dụng baseline chung chỉ thêm migration mới. Không bật `outOfOrder`, dùng `repair` hay xóa volume chung để che lỗi. Thứ tự merge không tự gây checksum mismatch: file đã chạy bị sửa mới có thể làm lệch checksum; migration thấp hơn đến sau là vấn đề thứ tự khác. CI kiểm tra DB sạch và nâng cấp từ baseline trước khi có migration tiếp theo. [Flyway versioned migrations](https://documentation.red-gate.com/fd/versioned-migrations-273973333.html).

## 4. Ticket mutation và claim

Mỗi mutation kiểm tra actor enabled, role/ownership, state và ghi event trong cùng transaction. Tất cả đường cập nhật ticket phải tương thích `@Version`. Claim dùng conditional update có `status='OPEN' AND assigned_agent_id IS NULL`, gán người nhận và **tăng `version=version+1`**; kiểm tra expected version khi endpoint có nhận version. Số dòng cập nhật phải đúng 1. Nếu 0, phân loại không tồn tại/không có quyền trước khi trả 409 `TICKET_ALREADY_CLAIMED` hoặc `TICKET_VERSION_CONFLICT` theo contract.

Bulk update bỏ qua optimistic locking tự động; không dựa riêng vào annotation `@Version`. Flush thay đổi cần thiết và clear/refresh persistence context đúng lúc; không clear làm mất thay đổi chưa flush. Không giữ entity stale rồi save lại sau claim. Event CLAIMED và ticket update cùng transaction; event lỗi thì claim rollback. [Jakarta Persistence 3.1, Bulk Update/Delete](https://jakarta.ee/specifications/persistence/3.1/jakarta-persistence-spec-3.1.html).

Transition không hợp lệ → **409 INVALID_TICKET_TRANSITION**; validation payload → 400. Tạo ticket trả 201, tạo message PUBLIC đầu tiên và event TICKET_CREATED nguyên tử. WAITING_CUSTOMER + customer reply → message + chuyển IN_PROGRESS + event nguyên tử. Hai update cùng version phải có đúng một winner hoặc một conflict phù hợp; test dùng PostgreSQL thật, hai connection/transaction và barrier, không chỉ mock repository hoặc hy vọng thread tự chạy cùng lúc.

## 5. Ingestion worker tối giản nhưng phục hồi được

MVP một worker tuần tự, tối đa một job active/document; không thêm broker hoặc worker service riêng. `FOR UPDATE SKIP LOCKED` chỉ giúp nhận hàng không tranh chấp, không bảo đảm retry/exactly-once. [PostgreSQL 16 SELECT](https://www.postgresql.org/docs/16/sql-select.html).

1. **Transaction nhận job ngắn:** chọn PENDING đã tới `next_run_at`, hoặc RUNNING có lease hết hạn; lock hàng. Nếu attempts đã hết thì chuyển job/document FAILED. Nếu còn lượt, tăng attempts **ngay khi nhận** (tổng tối đa 3 lần thực hiện), đặt RUNNING, UUID `lease_token` mới và `locked_until`; document PROCESSING; commit. Index/constraint bảo đảm một job PENDING/RUNNING mỗi document.
2. **Ngoài transaction:** đọc file private, parse PDFBox/TXT/MD, chunk theo trang/heading, gọi một EmbeddingProvider dùng chung. Giới hạn kích thước, số trang/chunks, timeout mỗi call và deadline toàn job; không giữ connection/row lock khi gọi provider. Chunk 500–800 token/overlap 80–120 là tham số ban đầu; ký tự không tương đương số token cố định, đặc biệt tiếng Việt. Nếu approximate phải ghi rõ và đo. Timeout cả job phải hữu hạn và nhỏ hơn lease hoặc có gia hạn lease hợp lệ.
3. **Transaction hoàn tất ngắn:** lock job và đối chiếu RUNNING + lease_token + lease còn hạn. Chỉ owner hiện tại được insert chunks và đặt document READY, `published=false`, job COMPLETED. Unique `(document_id, chunk_index)`; mọi insert và đổi trạng thái cùng transaction. Worker cũ mất lease không được ghi kết quả.
4. **Thất bại:** dưới cùng kiểm tra lease, nếu attempts < max thì job PENDING, đặt `next_run_at` có backoff, lưu mã lỗi an toàn; document vẫn PROCESSING trong thời gian chờ thử tự động. Hết lượt hoặc lỗi vĩnh viễn (PDF scan/loại file sai) → job và document FAILED. Không giữ mãi RUNNING sau exception; lần poll sau phục hồi lease hết hạn, kể cả lần cuối đã hết attempts.
5. **Manual retry:** Admin chỉ retry document FAILED nếu còn attempts của cùng job, không reset counter vô hạn hoặc tạo job song song. Hết 3 lượt trả 409 INGESTION_ATTEMPTS_EXHAUSTED; thao tác khôi phục vận hành đặc biệt phải có biên bản, ngoài UI MVP.

File lưu ngoài public web root, storage_key do server sinh; kiểm tra MIME/nội dung và size ≤10 MiB, không chỉ extension. PDF không có text → FAILED/UNSUPPORTED_SCANNED_PDF; TXT/MD có pageNumber=null. DB và filesystem không có chung transaction: cần dọn file mồ côi/metadata lỗi theo quy trình, không tuyên bố upload nguyên tử xuyên hai hệ thống. Lưu volume phải tồn tại qua restart. Giới hạn worker/provider concurrency để Ticket còn tài nguyên; cảnh báo Hikari connection giữ lâu là tín hiệu chẩn đoán, không tự chứng minh leak và tăng pool không sửa được transaction sai.

## 6. Giao diện Ticket → AI và Knowledge → AI

Các kiểu sau là contract thiết kế (không phải yêu cầu tạo mã trước 09/11):

```text
TicketContextProvider.getForSuggestion(ticketId, Actor)
  -> TicketContext(ticketId, ticketVersion, subject, publicMessages[])
  publicMessages: {id, body, createdAt}; thứ tự ổn định, giới hạn lịch sử/token
KnowledgeRetriever.search(queryText, Actor, limit, minSimilarity)
  -> RetrievedChunk[] {sourceId=chunk UUID, documentId, documentTitle,
                      content, pageNumber nullable, chunkIndex, similarity}
EmbeddingProvider.embed(text) -> {model, dimension, vector}
```

Các implementation kiểm tra quyền ở service, không chỉ controller. Ticket context không có entity, internal note, session hoặc email/PII thừa. Description của ticket là public message ban đầu, không tự thêm một cột mô tả khác.

Retriever tự gọi EmbeddingProvider cho query, AI **không embed cùng query lần thứ hai**. Lọc SQL `status='READY' AND published=true` và quyền trước LIMIT/top-k; cosine distance càng nhỏ càng gần, `similarity=1-distance` càng lớn càng gần. Threshold cấu hình và được hiệu chỉnh trên dữ liệu có nhãn; không coi score là xác suất đúng. Giới hạn k (mặc định 5, tối đa 20). Exact search đủ cho dữ liệu nhỏ; chưa làm HNSW/IVFFlat khi chưa có nhu cầu đo được.

Mỗi namespace/vector corpus dùng cùng model, dimension và mode. Không trộn hash/mock embedding với live, hoặc hai model có cùng dimension. Khi đổi model/mode phải chuyển DB/namespace riêng hoặc re-index theo quy trình trước khi search. Fake vector phải hữu hạn, đúng dimension, không zero vector cho cosine; chỉ chứng minh luồng/kiểu dữ liệu, không chứng minh chất lượng ngữ nghĩa.

## 7. RAG và apply suggestion

- Không có evidence hoặc score không đạt ngưỡng → INSUFFICIENT_EVIDENCE, suggestedText=null, citations=[]; không gọi LLM để bịa câu trả lời. Source ID lạ hoặc output sai schema → fail closed với errorCode, không trả một draft mất citation mà vẫn báo GENERATED.
- Tách instructions và dữ liệu ticket/tài liệu; không cho LLM gọi hành động, không tự gửi message. Kiểm tra sourceId thuộc tập retrieve là kiểm tra cấu trúc, **không chứng minh entailment**. Bộ đánh giá có evidence/no-evidence/archive/injection và kiểm tra nội dung được nguồn hỗ trợ.
- Generate đọc context trong transaction ngắn, gọi provider ngoài transaction, rồi kiểm tra lại quyền và ticketVersion trước khi lưu/return. Nếu ticket thay đổi, trả 409 TICKET_VERSION_CONFLICT để generate lại, không âm thầm dùng context cũ. Tái kiểm tra nguồn còn READY/published khi lưu; nếu nguồn vừa archive thì fail có kiểm soát. Lịch sử snapshot cũ không bị sửa theo nguồn mới.
- Provider timeout/quota có errorCode rõ, retry hữu hạn trong deadline; giới hạn token/concurrency/rate. Ticket APIs không gọi model trong transaction của mình. Smoke live là bằng chứng kết nối/luồng; đánh giá ≥30 câu ở 23–29/11 mới cung cấp số liệu chất lượng, không suy ra từ mock.

**Gửi từ suggestion:** API `POST /tickets/{ticketId}/messages`, body `{body, visibility:"PUBLIC", suggestionId}`. `suggestionId` là tên JSON; `source_suggestion_id` chỉ là tên SQL. Một application service trong `workflow/` điều phối Ticket và AI qua public ports; không module nào import repository/entity của module kia và không tạo vòng dependency.

Trong **một transaction DB**, lock ticket trước rồi suggestion (mọi đường send/discard/reassign phải theo thứ tự tương thích), recheck actor/quyền/state hiện tại, suggestion thuộc ticket và GENERATED, text đã duyệt không rỗng. Ghi message đúng body Agent gửi; cập nhật suggestion APPLIED/applied_at và event nghiệp vụ cần thiết; commit chung hoặc rollback chung. Không gọi LLM ở đây. Visibility INTERNAL kèm suggestionId bị từ chối 400; suggestion khác ticket/không có quyền → 404; APPLIED/DISCARDED/INSUFFICIENT_EVIDENCE/FAILED → 409 SUGGESTION_NOT_APPLICABLE. Repeated send chỉ tạo một message, request thua trả 409; UI khóa nút không thay thế bảo vệ server. Unique partial index `ticket_messages(source_suggestion_id) WHERE source_suggestion_id IS NOT NULL` là hàng rào bổ sung.

Discard dùng cùng kiểm tra quyền/state; chỉ GENERATED → DISCARDED. Send/discard tranh chấp chỉ một thao tác thắng. Suggestion ownership policy dựa quyền ticket hiện tại, không chỉ requested_by. Ports dùng propagation tham gia transaction hiện tại, không REQUIRES_NEW; ngoài monolith/same DB thì contract nguyên tử này không còn áp dụng.

## 8. HTTP và adapter frontend

API wrapper `{data:...}`, pagination `{data:[],page:{number,size,totalElements,totalPages}}`, error `{error:{code,message,requestId}}`; timestamps UTC ISO 8601. TicketStatus gồm **WAITING_CUSTOMER**; priority chỉ LOW/NORMAL/HIGH. HTTP 400 validation, 401 auth, 403 role/disabled, 404 resource/ownership, 409 state/version, 413 size, 429 quota; 502 output/provider lỗi, 504 AI timeout. Không trả raw provider error chứa secrets.

Prototype React đang có dữ liệu mock; chưa coi `frontend/src/types/index.ts` là API contract. Trong task frontend của từng module, tạo API DTO và adapter vào view model; không đổi tên SQL/DTO cho khớp mock một cách tự phát.

| Prototype hiện có | API chuẩn / việc phải làm từ 09/11 |
|---|---|
| `title`, customer/assignee object | `subject`, requester/assigned IDs và DTO hiển thị có quyền; adapter ánh xạ |
| TicketStatus thiếu WAITING_CUSTOMER, có priority URGENT | Bổ sung WAITING_CUSTOMER; bỏ URGENT khỏi UI P0 và fixtures, không silently hạ mức |
| Message `content`, `isInternal` | `body`, `visibility`; author lấy principal, không tin sender từ browser |
| Document `PENDING`, `isPublished`, fileSize string | status document UPLOADED/PROCESSING/READY/FAILED/ARCHIVED, `published`, `sizeBytes` số; PENDING là job |
| AI `draftReply`, `confidence` | `id`, `ticketId`, `status`, `suggestedText` nullable, `needsHumanReview`; không hiển thị confidence như độ chính xác |
| Citation `documentId`, `chunkSnippet` | `sourceId` là chunk UUID, `documentId`, `excerpt`, `pageNumber` nullable; không đánh đồng document và chunk |

Mẫu GENERATED và INSUFFICIENT_EVIDENCE ở SRS 11.5; bổ sung sample FAILED/timeout, empty page và 409 khi viết OpenAPI ngày 09–10/11. Không fabricate link Figma/screenshot hay coi role switch của mock UI là kiểm soát truy cập. Chuẩn bị loading/error/empty/disabled và lỗi quyền trong từng mockup.

## 9. Bằng chứng nghiệm thu tối thiểu

- Identity: giữ nguyên TC-ID-01..04; thêm happy path bằng mã mới. Disabled access test, refresh rotation concurrent và cookie/CSRF phải có bằng chứng.
- Ticket: TC-TK-01..08, TC-CON-01/02 trên PostgreSQL; rollback event và reassign/recheck quyền.
- KB: TC-KB-01..05; thêm crash/lease cũ, hết attempts, duplicate completion, file private và trường hợp TXT/MD. Search archive kiểm tra ở SQL/corpus thật, không chỉ fake luôn lọc đúng.
- AI/workflow: TC-AI-01..07; thêm cross-ticket suggestion, double-send, send/discard race, rollback APPLIED/message, stale version, quyền lịch sử/citation sau reassign, nguồn archive trong lúc generate.
- Ops: clean DB migrate, nâng cấp baseline khi có migration mới, README trên máy khác; test timeout AI trong khi Ticket vẫn dùng được.
- Mỗi kết quả ghi mode, dataset, model/dimension nếu live, command, actual/expected và liên kết PR. Chưa chạy phải ghi NOT RUN, không đánh PASS dựa trên task Done hoặc checklist đã tick.
