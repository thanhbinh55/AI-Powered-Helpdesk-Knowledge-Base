# Frontend — prototype React hiện có

Repo đã có Vite/React/TypeScript/Tailwind và các màn hình chạy bằng dữ liệu mock trong `src/mock/data.ts`. Đây chưa phải frontend tích hợp backend; role switch trong prototype không phải kiểm soát truy cập.

03–08/11 hoàn thiện mockup/tài liệu Template 1; cài đặt API/adapter và UI P0 từ **09–22/11**. Dùng giao diện hiện có làm đầu vào; không viết lại toàn bộ chỉ để giống mockup.

Các script đang khai báo trong package.json:

```bash
npm ci
npm run dev
npm run build
```

Chưa có script lint/test frontend; không coi các mục đó là checks đã cấu hình. Khi bổ sung phải ghi command và kết quả thật.

| Phần việc | Owner | Hợp đồng cần theo |
|---|---|---|
| Auth/profile/Agent management và Axios session | Bình | Principal server-side, cookie/CSRF, access memory, single-flight refresh |
| Ticket/Customer UI | Gia Phúc | subject/body/visibility, đủ WAITING_CUSTOMER, priority LOW/NORMAL/HIGH |
| Knowledge UI | Lãm | document UPLOADED/PROCESSING/READY/FAILED/ARCHIVED, published boolean; PENDING chỉ là job |
| AI panel/citations/provider errors | Quý Phúc | id/status/suggestedText nullable, sourceId là chunk UUID; không coi confidence mock là xác suất đúng |
| CI build frontend/backend | Quý Phúc | Từng owner cung cấp lệnh, Bình review |

Chi tiết API DTO, mẫu lỗi, mapping view model và tests ở [MVP_CONTRACTS Mục 8](../reports/MVP_CONTRACTS.md) và [SRS Mục 11](../reports/SRS-master.md). Types/fixtures hiện có còn thiếu state và khác naming; mỗi owner sửa trong task tích hợp module mình từ 09/11, không tự thay API cho khớp mock. Tạo DTO API và adapter rõ ràng, không truyền sender/role từ browser làm nguồn quyền. Loading/error/empty/disabled cần thể hiện cả trong mockup lẫn UI.

Analytics UI có sẵn chỉ là prototype P1; không tạo cam kết backend Analytics trước 22/11. Auth thật, download nguồn và mọi endpoint cần kiểm tra quyền ở backend. Nút Send khóa khi đang gửi nhưng server vẫn phải chống double-send.
