# API Contract — chỉ mục baseline

> Cập nhật 03/11/2026. Gia Phúc điều phối OpenAPI/DTO/ports 09–10/11; mỗi owner viết phần mình, owner phía nhận review. Chưa có OpenAPI hoàn chỉnh được chạy kiểm chứng.

Nguồn chuẩn: [SRS Mục 11](SRS-master.md), [MVP_CONTRACTS](MVP_CONTRACTS.md). Prefix `/api/v1`, JSON camelCase, UTC ISO 8601; wrapper data/page/error theo SRS. Principal lấy JWT đã xác minh, enabled kiểm tra server-side; cookie/CSRF/refresh theo contract.

| Method | Endpoint đầy đủ | Quyền / kết quả |
|---|---|---|
| POST | /api/v1/auth/login | Public, kiểm tra credential/disabled |
| POST | /api/v1/tickets | Customer, 201; không cho Agent tự tạo |
| GET | /api/v1/tickets | Theo role/ownership, phân trang |
| POST | /api/v1/tickets/{id}/claim | Agent/Admin, atomic claim và 409 khi tranh chấp |
| POST | /api/v1/knowledge/documents | Admin, multipart upload 202 |
| GET | /api/v1/knowledge/search | Agent/Admin; nguồn READY + published |
| POST | /api/v1/tickets/{id}/ai-suggestions | Assigned Agent/Admin, không tự gửi message |
| GET | /api/v1/tickets/{id}/ai-suggestions | Quyền ticket hiện tại, không Customer |
| POST | /api/v1/tickets/{id}/messages | Body/visibility/suggestionId; recheck quyền/state, message+APPLIED nguyên tử |
| POST | /api/v1/ai-suggestions/{id}/discard | Assigned Agent/Admin; GENERATED → DISCARDED |

Không dùng `/articles/*`, `/ai/classify-ticket` hoặc KB search public của bản khung cũ. Mẫu JSON, nullability, pagination, timeout và mapping prototype có trong SRS/contract; phải bổ sung fixtures/OpenAPI và chạy fake/real cùng contract trước khi coi xong DEV-0.

HTTP: 400 validation, 401 token sai/thiếu, 403 sai role/disabled, 404 không tồn tại hoặc không có quyền tài nguyên, 409 state/version, 413 upload quá lớn, 429 quota, 502 provider/output lỗi, 504 timeout. Không lộ raw secrets/provider error. Suggestion sourceId là **chunk UUID**, suggestionId là JSON còn source_suggestion_id là cột DB.
