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
| Bỏ gợi ý (UC-15) | Nút cùng độ rộng; ẩn tin 09:50 mâu thuẫn với bản nháp; bỏ dòng "Đã bỏ" lặp; tin gửi thủ công bỏ `[1]`, `[2]` và màn trước có nhắc xóa ký hiệu nguồn | 15 frame |
| Thống kê (UC-17) | Thêm icon nav; hai thẻ cao bằng nhau; thẳng lề; ghi chú chuyển vào thẻ người phụ trách; gom cụm tiêu đề; "Tải lại" disabled khi đang tải, bỏ khi lỗi và khi không có quyền | 12 frame |

Đã xuất lại ảnh trong [anh/](../anh/).

## Đã kiểm tra

- Xem lại 32 frame sau khi sửa, gồm desktop, tablet, mobile và dark.
- Đường nối của nút sau khi đổi biến thể: kiểm mẫu 7 trên 76 node đã đổi biến thể hoặc độ rộng, đều còn nguyên.
- Danh sách flow vẫn đủ, tên không còn trùng lặp.

Chưa kiểm tra: chạy thử prototype trong Figma Present, bàn phím và screen reader.

## Cần nhóm quyết định

1. **Lệch tài liệu về "Thiếu căn cứ":** MASTER xếp vào tông danger, còn màn A-AIInsufficient đã bàn giao dùng warning. Lượt này theo warning để khớp màn đó, vì đây không phải lỗi hệ thống. Cần chốt rồi sửa MASTER hoặc màn hình.
2. **Lối vào Thống kê:** chỉ các frame UC-17 và `D-AnalyticsEntry` có mục nav "Thống kê". D01–D05 và các màn Kho tri thức của Admin thì chưa, vì UC-17 là P1. Nếu đưa UC-17 vào bản chính thức thì cần thêm mục này cho toàn bộ nav Admin.
3. **Icon Thống kê:** thư viện `v2 / Icon` chưa có icon biểu đồ nên tạm dùng `ticket`. Nên bổ sung `chart-column` khi cập nhật Components.
4. **Ký hiệu nguồn gửi cho khách:** A-AISent gửi cả `[1]`, `[2]`, nhưng màn Customer không hiển thị danh sách nguồn. Cần chốt có giữ ký hiệu trong tin công khai hay không.

## Chưa làm

- Thêm chevron cho thẻ lần tạo: cần đổi cấu trúc thẻ ở nhiều frame, lợi ích thấp.
- Thu nav `D-TabletAnalytics` về rail 72: Admin chưa có mẫu tablet khác để đối chiếu.
- Frontend chưa áp dụng các thay đổi này.
