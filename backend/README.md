# BACKEND SERVICE (PLANNED ARCHITECTURE)

> **Công nghệ dự kiến (Mục 9.3 & 15.3 của đặc tả):**  
> Java 21, Spring Boot 3.x, Spring Data JPA, Spring Security (JWT), Spring AI / REST Client, PostgreSQL với pgvector.  
> **Lưu ý:** Thư mục này hiện tại **CHỈ LƯU TRỮ TÀI LIỆU CẤU TRÚC**, chưa khởi tạo mã nguồn ứng dụng theo quy định của đồ án.

---

## CẤU TRÚC GÓI DỰ KIẾN (PLANNED PACKAGE STRUCTURE)
```text
backend/
├── pom.xml / build.gradle
├── mvnw / gradlew
└── src/
    ├── main/
    │   ├── java/vn/edu/hcmus/helpdesk/
    │   │   ├── Application.java               # Spring Boot Application entrypoint
    │   │   ├── auth/                          # Phân hệ A: User, Authentication & RBAC
    │   │   │   ├── controller/
    │   │   │   ├── service/
    │   │   │   ├── repository/
    │   │   │   └── dto/
    │   │   ├── ticket/                        # Phân hệ B: Ticket Management & Workflow
    │   │   │   ├── controller/
    │   │   │   ├── service/
    │   │   │   ├── repository/
    │   │   │   └── dto/
    │   │   ├── knowledge/                     # Phân hệ C: Knowledge Base & Vector Search
    │   │   │   ├── controller/
    │   │   │   ├── service/
    │   │   │   ├── repository/
    │   │   │   └── dto/
    │   │   ├── ai/                            # Phân hệ D: AI Provider & Prompt Engineering
    │   │   │   ├── client/                    # OpenAI / Local LLM / Mock Adapter
    │   │   │   └── service/
    │   │   ├── analytics/                     # Phân hệ D: Thống kê SLA & Báo cáo
    │   │   │   ├── controller/
    │   │   │   └── service/
    │   │   └── common/                        # Common exceptions, security filters, configs
    │   └── resources/
    │       ├── application.yml
    │       ├── application-dev.yml
    │       └── db/migration/                  # Liquibase / Flyway migration SQL scripts
    └── test/
        └── java/vn/edu/hcmus/helpdesk/        # Unit & Integration Tests (JUnit 5, Mockito)
```
