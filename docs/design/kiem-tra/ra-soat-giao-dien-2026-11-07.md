# Rà soát giao diện prototype — 07/11/2026

Rà soát 229 frame trên 5 page `Redesign v2 / …` của file Figma SE, đối chiếu với [MASTER](../../../design-system/helpdesk-workspace/MASTER.md), đặc tả UC-15/17/18/19 và các tiêu chí UI/UX về tương phản, tương tác, bố cục.

**Kết luận:** giữ phương án "Bàn làm việc yên tĩnh", không thiết kế lại. Hướng này khớp khuyến nghị Minimalism & Swiss Style cho công cụ B2B; điểm yếu nằm ở các chi tiết lặp lại nên được sửa tại chỗ. Token và component không đổi.

## Đã sửa

| Nhóm | Thay đổi | Phạm vi |
|---|---|---|
| Dòng thời gian | Sự kiện "đã nhận xử lý" từ 09:48 thành 09:45, vì các lần tạo gợi ý bắt đầu từ 09:46 và cần người phụ trách | 93 node |
| Trạng thái gợi ý | Chữ trạng thái dùng token `status/*/fg`: Sẵn sàng (success), Đã sử dụng (info), Thiếu căn cứ (warning), Tạo thất bại (danger), Đã bỏ (neutral) | 145 node |
| Nút quay lại | "Quay lại trợ lý/lịch sử/lần tạo" dùng `Ghost`, `Md`, icon `arrow-left`, cùng mẫu với A08 | 47 instance |
| Mobile UC-18 | Ẩn khối "Quay lại hội thoại" + tiêu đề, để mỗi màn chỉ còn một nút quay lại | 8 frame |
| Dữ liệu `APPLIED` | Thêm tin đã gửi lúc 09:49 vào hội thoại Agent; đồng bộ nội dung và giờ ở Admin | 10 + 3 frame |
| Bỏ gợi ý (UC-15) | Nút cùng độ rộng; ẩn tin 09:50 mâu thuẫn với bản nháp; bỏ dòng "Đã bỏ" lặp; bản nháp và tin gửi không còn `[1]`, `[2]`; A-Inserted desktop và mobile cũng ẩn tin mâu thuẫn | 17 frame |
| Lối vào Thống kê | Thêm mục "Thống kê" vào điều hướng Admin. 37 mục trên page Admin nối tới D06; 27 mục ở Kho tri thức và Hồ sơ không có đường nối, giống các mục điều hướng khác ở đó, vì Figma không cho nối khác page | 64 frame |
| Ký hiệu nguồn | Bản nháp đã chèn và tin gửi khách không còn `[1]`, `[2]`; ngăn AI và lịch sử vẫn giữ để Agent đối chiếu | 23 node |
| Thống kê (UC-17) | Thêm icon nav; hai thẻ cao bằng nhau; thẳng lề; ghi chú chuyển vào thẻ người phụ trách; gom cụm tiêu đề; "Tải lại" disabled khi đang tải, bỏ khi lỗi và khi không có quyền | 12 frame |

Đã xuất lại ảnh trong [anh/](../anh/).

## Đã kiểm tra

- Xem lại 32 frame sau khi sửa, gồm desktop, tablet, mobile và dark.
- Đường nối của nút sau khi đổi biến thể: kiểm mẫu 7 trên 76 node đã đổi biến thể hoặc độ rộng, đều còn nguyên. Với 64 mục Thống kê mới, batch đặt reaction trả về thành công và mẫu đã đọc lại.
- Danh sách flow vẫn đủ, tên không còn trùng lặp.

Chưa kiểm tra: chạy thử prototype trong Figma Present, bàn phím và screen reader.

## Quyết định đã chốt

1. **"Thiếu căn cứ" dùng tông warning.** Đây là kết quả từ chối trả lời hợp lệ theo BR-13, không phải lỗi; "Tạo thất bại" dùng danger. MASTER đã cập nhật.
2. **Điều hướng Admin có mục Thống kê.** UC-17 vẫn là P1. Thư viện `v2 / Icon` chưa có icon biểu đồ nên tạm dùng `ticket`; nên bổ sung `chart-column` khi cập nhật Components.
3. **Tin gửi Customer không chứa ký hiệu nguồn.** SRS không cấm ký hiệu này, đây là quyết định thiết kế vì Customer không có danh sách nguồn. Khi code, frontend phải bỏ ký hiệu lúc chèn gợi ý vào bản nháp; nguồn vẫn lưu để truy vết.

## Chưa làm

- Thêm chevron cho thẻ lần tạo: cần đổi cấu trúc thẻ ở nhiều frame, lợi ích thấp.
- Thu nav `D-TabletAnalytics` về rail 72: Admin chưa có mẫu tablet khác để đối chiếu.
- Frontend chưa áp dụng các thay đổi này.
