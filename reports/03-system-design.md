# Thiết kế hệ thống — chỉ mục baseline

> Cập nhật 03/11/2026. Thiết kế để cài đặt 09–22/11; chưa phải mô tả mã đã chạy.

Kiến trúc **Modular Monolith**, một backend Spring Boot/Java 21, một PostgreSQL/pgvector, React frontend, ingestion worker trong cùng ứng dụng. Không tách microservice/broker/Redis trong MVP. Tổ chức package và dependency ở [SRS Mục 9–10](SRS-master.md), hợp đồng chi tiết ở [MVP_CONTRACTS](MVP_CONTRACTS.md).

| Dữ liệu | Bảng chuẩn |
|---|---|
| Identity | users, auth_sessions; role là cột users.role |
| Ticket | tickets, ticket_messages, ticket_events |
| Knowledge | knowledge_documents, knowledge_ingestion_jobs, knowledge_chunks |
| AI | ai_suggestions, ai_suggestion_sources |

Không dùng roles/ticket_comments/articles/article_embeddings/audit_logs từ bản khung cũ làm schema mới. Vector dimension/model còn phải chốt DEC-06 trước V3; không mặc định 1536 từ ví dụ.

Lãm điều phối V1–V5, mỗi owner viết phần mình; V2 cột source_suggestion_id nullable, V5 mới thêm FK sau V4. Quý Phúc làm CI, Bình review. Ports không truyền entity/repository chéo module; workflow điều phối Ticket/AI trong cùng transaction, message + APPLIED cùng commit. Claim tăng version; worker nhận/hoàn tất job bằng transaction ngắn có lease/token, provider ngoài transaction.

Clean Architecture không tự được chứng minh bằng sơ đồ ba tầng; MVP cần boundary/transaction/authorization có kiểm thử. ERD, sequence, DTO và error được cập nhật cùng SRS/contract; không chép lại một bộ naming khác trong báo cáo này.

## Bản nộp Template 2 ngày29/11

Nguồn [mẫu được cung cấp](references/template2-design-requirements.md), bảnnộp ở[template2/README.md](template2/README.md). Bổsung conceptual/câyphânrã/architecture/ERD/data dictionary/UI, mỗiowner góp phầnmình từ 09/11; đây là deliverable thiết kế, không phải test report. [Lịch/phâncông](planning/TEMPLATE2_3_ALIGNMENT.md) chốt nội dung26/11, gói 27, nộp 28 trước hạn 29 theo giờcổng.
