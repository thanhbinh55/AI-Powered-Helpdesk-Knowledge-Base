# FRONTEND WEB APPLICATION (PLANNED ARCHITECTURE)

> **Công nghệ dự kiến (Mục 9.3 & 15.3 của đặc tả):**  
> React 18+, Vite, TypeScript, TailwindCSS / CSS Modules, Axios / TanStack Query, React Router v6.  
> **Lưu ý:** Thư mục này hiện tại **CHỈ LƯU TRỮ TÀI LIỆU CẤU TRÚC**, chưa khởi tạo mã nguồn ứng dụng theo quy định của đồ án.

---

## CẤU TRÚC THƯ MỤC DỰ KIẾN (PLANNED DIRECTORY STRUCTURE)
```text
frontend/
├── package.json
├── vite.config.ts
├── tsconfig.json
├── index.html
└── src/
    ├── main.tsx                       # React Application root mount
    ├── App.tsx                        # Router layout & providers
    ├── assets/                        # Static assets (images, icons, fonts)
    ├── components/                    # Reusable UI components (buttons, modals, tables)
    ├── features/                      # Domain-driven feature modules
    │   ├── auth/                      # Phân hệ A: Login, Register, Profile, Guard
    │   ├── ticket/                    # Phân hệ B: Ticket list, Create, Detail, Timeline
    │   ├── knowledge/                 # Phân hệ C: KB Explorer, Article detail, Search bar
    │   └── admin/                     # Phân hệ D: SLA metrics, Category management, Analytics
    ├── hooks/                         # Custom React hooks
    ├── services/                      # Axios API clients & endpoints
    ├── types/                         # Shared TypeScript interfaces & types
    └── utils/                         # Date formatters, validators, storage helpers
```
