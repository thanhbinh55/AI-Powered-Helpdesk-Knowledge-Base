# Bộ thiết kế giao diện — Redesign v2

Thiết kế giao diện Helpdesk cho ba vai trò Customer, Agent và Admin, dựng trên file Figma **SE** bằng Figwright. Đọc [DESIGN.md](../../DESIGN.md) trước để biết thứ tự ưu tiên giữa các tài liệu.

- **Figma Design chính thức:** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)
- **Tài liệu làm việc nhóm (Google Docs):** [[SE - Nhóm 4] template1](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0)
- **Báo cáo Mục 5 Template 1:** [05-prototype-mockup.md](../../reports/template1/05-prototype-mockup.md)

## Nội dung thư mục

| Đường dẫn | Nội dung |
| --- | --- |
| [man-hinh.md](man-hinh.md) | Bảng 151 frame theo module, ảnh từng màn, luồng prototype và giới hạn |
| [dac-ta-inbox.md](dac-ta-inbox.md) | Đặc tả luồng, bố cục, responsive và hành vi AI; mục 7 (thị giác) đã thay bằng MASTER |
| [figma-map.json](figma-map.json) | Manifest: ID page/frame Figma, reaction đã nối và link bị bỏ qua |
| [anh/](anh/) | Ảnh PNG từng frame, tên file là ID node (`55-1992.png` là node `55:1992`) |
| [anh/thanh-phan/](anh/thanh-phan/) | Ảnh các nhóm component trên page Components |
| [kiem-tra/](kiem-tra/) | Kết quả kiểm tra: audit từng module, components, tương phản token, kiểm tra nghiệp vụ |

Token, typography và component nằm trong [MASTER](../../design-system/helpdesk-workspace/MASTER.md).

## File Figma

| Page | ID |
| --- | --- |
| Redesign v2 / Foundations | `49:58` |
| Redesign v2 / Components | `50:802` |
| Redesign v2 / Agent — Xử lý ticket | `54:1987` |
| Redesign v2 / Customer | `54:1988` |
| Redesign v2 / Identity | `54:1989` |
| Redesign v2 / Knowledge Base | `54:1990` |
| Redesign v2 / Admin | `54:1991` |

Biến nằm trong 3 collection `Helpdesk v2 / Color` (Light, Dark), `Dimension` và `Typography`; chữ dùng 12 text style `v2 / …`. Page gốc 01–05, page đề xuất phương án và biến/style của bản cũ đã xóa ngày 03/11/2026.

## Trạng thái

- 33 nhóm màn chính, 151 frame, 5 mẫu Dark, 56 flow prototype. Hoàn tất 01/11/2026, rà soát và sửa 03/11/2026.
- Prototype tĩnh: không có backend, auth, upload hay lưu trạng thái thật. Không dùng prototype làm bằng chứng backend hoặc phân quyền đã triển khai.
- Chưa kiểm tra bàn phím, screen reader, focus trap, scroll và bàn phím ảo; các phần này kiểm tra khi code frontend.

## Dùng khi code frontend

1. Tìm màn trong [man-hinh.md](man-hinh.md) và lấy ID node.
2. Đọc chi tiết bằng Figwright (`get_design_context` với ID đó, cần plugin Figwright đang mở trong Figma). Không đo kích thước từ ảnh.
3. Dùng token CSS trong MASTER, ví dụ `var(--bg-surface)`, `var(--space-16)`; không hardcode giá trị.
4. Đối chiếu quyền và trạng thái ticket với [SRS](../../reports/SRS-master.md); prototype không thay thế SRS.
