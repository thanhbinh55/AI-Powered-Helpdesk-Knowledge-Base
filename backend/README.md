# Backend — kiến trúc dự kiến

Hiện thư mục chưa có ứng dụng Spring Boot. Kế hoạch cài đặt **09–22/11/2026**, sau khi chốt Template 1 ngày 08/11; không coi các thư mục dự kiến dưới đây là mã đã chạy.

Stack baseline: Java 21, Spring Boot 3, Maven, PostgreSQL 16/pgvector, Flyway, JUnit và kiểm thử tích hợp PostgreSQL. Chốt minor version/phụ thuộc khi khởi tạo ngày 09/11. Model/dimension chưa chốt là blocker trước V3; không hardcode từ ví dụ.

Nguồn chuẩn: [SRS](../reports/SRS-master.md), [MVP_CONTRACTS](../reports/MVP_CONTRACTS.md), [kế hoạch](../PLAN_TEMPLATE1_AND_DEVELOPMENT.md).

```text
src/main/java/vn/edu/hcmus/helpdesk/
  identity/       # Bình: auth, principal, users/sessions
  ticket/         # Gia Phúc: tickets/messages/events
  knowledge/      # Lãm: upload/jobs/retrieval; EmbeddingProvider owner
  ai/             # Quý Phúc: provider live, RAG/suggestions/snapshots
  workflow/       # Gia Phúc + Quý Phúc: apply/discard phối hợp qua public ports
  common/         # lỗi HTTP/security/config; không đặt entity nghiệp vụ dùng chéo
    ai/           # interface/fake do Lãm sở hữu; adapter live Quý Phúc
src/main/resources/db/migration/
  V1__init_identity.sql
  V2__init_ticket.sql
  V3__init_knowledge.sql
  V4__init_ai.sql
  V5__add_ticket_message_suggestion_fk.sql
src/test/         # unit + integration/concurrency trên PostgreSQL
```

Schema nền là PR phối hợp 09–10/11: Lãm điều phối, mỗi owner viết phần mình; V5 FK sau V4. CI Quý Phúc làm, Bình review; từng owner cung cấp command/test module. Gia Phúc điều phối E2E; Lãm chạy clean-environment smoke. Không thêm migration thứ tự thấp hoặc sửa checksum baseline đã dùng chung.

Không repository/entity chéo module; workflow cùng DB/transaction qua ports, message và APPLIED nguyên tử. Worker nhận/hoàn tất job transaction ngắn với lease token; provider ngoài transaction. Test giữ nguyên TC IDs trong SRS, không suy chất lượng AI từ fake. Analytics/reset password là backlog P1, chưa cài đặt trong cam kết trước 22/11.

Khi khởi tạo phải bổ sung lệnh chạy thực tế, biến môi trường mẫu, seed an toàn, cách chạy test và expected output vào README. Chưa có mã nguồn thì không ghi lệnh đã kiểm chứng hoặc trạng thái PASS.
