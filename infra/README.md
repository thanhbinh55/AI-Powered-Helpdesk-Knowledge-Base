# INFRASTRUCTURE & DEPLOYMENT (CLARUNE)

> **Cơ sở dữ liệu chính (Primary DB):**  
> Dự án sử dụng **Supabase Cloud (PostgreSQL 15/16 + pgvector)** đặt tại Region **Singapore (`ap-southeast-1`)** để toàn bộ thành viên trong nhóm dùng chung dữ liệu thực tế, không cần cấu hình và duy trì Docker daemon DB trên từng máy cá nhân.
>
> **Môi trường cục bộ dự phòng (Local Dev Fallback):**  
> Docker Compose (PostgreSQL 16 + pgvector) được cung cấp dưới dạng tùy chọn dự phòng khi phát triển offline hoặc chạy isolated integration test.

---

## 1. CẤU HÌNH SUPABASE (SINGAPORE)
- **Region:** Southeast Asia (Singapore) - `ap-southeast-1`
- **Vector Extension:** Đã tích hợp sẵn, kích hoạt bằng lệnh:
  ```sql
  CREATE EXTENSION IF NOT EXISTS vector;
  ```
- **Chuỗi kết nối JDBC (Spring Boot):**
  - **Direct connection (Port 5432):** `jdbc:postgresql://db.<project-ref>.supabase.co:5432/postgres?sslmode=require`
  - **Connection Pooling (IPv4 / Port 5432):** `jdbc:postgresql://aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres?sslmode=require`
  - **Username mặc định:** `postgres`

---

## 2. CẤU TRÚC DỰ KIẾN (INFRASTRUCTURE STRUCTURE)
```text
infra/
├── docker-compose.yml                 # (Tùy chọn) Orchestration PostgreSQL pgvector local dev
├── postgres/
│   ├── init.sql                       # CREATE EXTENSION IF NOT EXISTS vector;
│   └── Dockerfile
└── mock-ai/
    └── mock_server.py                 # Giả lập phản hồi LLM khi không có API key thật
```
