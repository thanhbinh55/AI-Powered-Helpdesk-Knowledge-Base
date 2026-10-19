# INFRASTRUCTURE & DEPLOYMENT (PLANNED ARCHITECTURE)

> **Công nghệ dự kiến (Mục 9.3 & 15.3 của đặc tả):**  
> Docker, Docker Compose, PostgreSQL 16 + pgvector, Nginx Reverse Proxy, Mock AI Service.  
> **Lưu ý:** Thư mục này hiện tại **CHỈ LƯU TRỮ TÀI LIỆU CẤU TRÚC**, chưa khởi tạo container cấu hình theo quy định của đồ án.

---

## CẤU TRÚC DỰ KIẾN (PLANNED INFRASTRUCTURE STRUCTURE)
```text
infra/
├── docker-compose.yml                 # Orchestration cho PostgreSQL, Backend, Frontend
├── docker-compose.override.yml        # Development overrides & mock services
├── postgres/
│   ├── init.sql                       # Khởi tạo extension CREATE EXTENSION IF NOT EXISTS vector;
│   └── Dockerfile
├── nginx/
│   ├── nginx.conf                     # Reverse Proxy & SSL termination config
│   └── conf.d/default.conf
└── mock-ai/
    └── mock_server.py                 # Giả lập phản hồi LLM khi không có API key thật
```
