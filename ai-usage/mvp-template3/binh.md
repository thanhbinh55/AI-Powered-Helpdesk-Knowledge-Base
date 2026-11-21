# Nhật ký sử dụng AI — Code MVP & Template 3 (Ngô Viết Thanh Bình - `24120269`)

> Ghi nhận các phiên làm việc với AI phục vụ cài đặt mã nguồn MVP & kiểm thử Template 3.
> Mỗi phiên ghi đủ 7 trường: Thời gian, Tác giả, Công cụ/Model, Prompt đã khử dữ liệu nhạy cảm, Nội dung AI tạo, Nội dung tự kiểm chứng & hiệu chỉnh, Minh chứng/Commit.

---

### Phiên 01 — Khởi tạo Spring Boot 3 Foundation, Supabase Config & ErrorEnvelope (21/11/2026)
* **Thời gian:** 2026-11-21 11:22
* **Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269`)
* **Công cụ & Model:** Antigravity (Gemini 2.5 Flash)
* **Mục đích & Prompt:** "Khởi tạo khung dự án Spring Boot 3 Java 21, cấu hình kết nối PostgreSQL/Supabase Singapore qua biến môi trường JDBC, định nghĩa lớp ActorPrincipal và ErrorEnvelope theo đặc tả MVP_CONTRACTS.md"
* **Nội dung AI tạo ra:**
  - Khung file `backend/pom.xml` với các dependency: Spring Web, Data JPA, PostgreSQL Driver, Flyway, Validation, Lombok, Dotenv.
  - Cấu trúc thư mục `src/main/java/vn/edu/hcmus/helpdesk/common/`.
  - Mã nguồn `ApiResponse.java`, `PageResponse.java`, `ErrorEnvelope.java`, `ErrorCode.java`, `AppException.java`, `GlobalExceptionHandler.java`, `ActorPrincipal.java`, `UserRole.java`, `HealthController.java`.
  - File cấu hình `application.yml` liên kết biến môi trường DB Supabase Singapore với pooling HikariCP.
  - Cấu hình dự phòng `infra/docker-compose.yml` (PostgreSQL 16 + pgvector) và script `infra/postgres/init.sql`.
* **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Kiểm tra tính tương thích của Java 21 và Spring Boot 3.3.5.
  - Đối chiếu cấu trúc JSON của `ErrorEnvelope` khớp 100% với mục 8 của `reports/MVP_CONTRACTS.md` (`error: {code, message, requestId, timestamp, details}`).
  - Kiểm tra `ActorPrincipal` đầy đủ thuộc tính `userId`, `email`, `role`, `enabled` theo đúng Mục 2 `MVP_CONTRACTS.md`.
* **Minh chứng:** Commit trên nhánh `feat/backend-foundation-scrum26` (Jira: `SCRUM-26`).
