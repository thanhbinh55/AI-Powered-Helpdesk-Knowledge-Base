# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Clarune phục vụ một **chuỗi bán lẻ điện máy lớn** (nhiều chi nhánh, nhiều nhóm hàng, lượng yêu cầu lớn). Hai nhóm người dùng được ưu tiên ngang nhau:

- **Khách hàng mua hàng:** tự tạo và theo dõi yêu cầu bảo hành, đổi trả, hỏi cách sử dụng. Thường dùng lần đầu, trên điện thoại hoặc máy tính, và có thể đang bực vì sản phẩm lỗi.
- **Nhân viên CSKH:** nhận và xử lý ticket cả ngày, tra chính sách trong kho tri thức, dùng gợi ý AI để trả lời nhanh và đúng.
- **Quản trị viên:** phân công ticket, quản lý nhân viên và tài liệu kho tri thức, xem thống kê.

## Product Purpose

Giúp chuỗi bán lẻ trả lời yêu cầu sau bán hàng nhanh, đúng chính sách và nhất quán giữa các chi nhánh. Thành công là khách nhận được câu trả lời đúng chính sách bảo hành/đổi trả hiện hành, và nhân viên trả lời được mà không phải tự tìm trong tài liệu dài.

## Positioning

AI gợi ý câu trả lời **dựa trên tài liệu chính sách đã công bố, có trích dẫn nguồn** (mục, trang), và **không bao giờ tự gửi cho khách**: nhân viên phụ trách đọc, đối chiếu nguồn, sửa rồi mới gửi. Khi thiếu căn cứ, AI nói rõ là không đủ thông tin thay vì đoán. (Theo SRS FR-AI-07, UC-14/15.)

## Operating Context

- Ticket đi qua các trạng thái: Mới tạo → Đang xử lý → Chờ khách phản hồi → Đã giải quyết → Đã đóng (khách có thể mở lại). Chi tiết ở [SRS](reports/SRS-master.md).
- Trao đổi gồm tin nhắn công khai và ghi chú nội bộ; khách không bao giờ thấy ghi chú nội bộ.
- Kho tri thức chứa tài liệu PDF/MD (chính sách bảo hành, đổi trả, hướng dẫn xử lý lỗi), qua bước xử lý rồi mới công bố.
- Chính sách điện máy có nhiều mốc thời gian và mức phí theo nhóm hàng (ví dụ: đổi miễn phí tháng đầu, phí theo tháng sau đó, hàng trưng bày, hàng chỉ bán online), và có phiên bản cũ/mới cùng tồn tại.

## Capabilities and Constraints

- Phạm vi chức năng theo [SRS](reports/SRS-master.md) (41 FR, 19 Use Case). Luồng, quyền và trạng thái không thay đổi khi làm lại giao diện.
- Toàn bộ nội dung giao diện bằng tiếng Việt có dấu; font phải hỗ trợ đầy đủ tiếng Việt.
- Có Light và Dark; desktop, tablet và mobile.
- Đồ án môn học: không có backend thật trong prototype; dữ liệu demo là giả lập hoặc có quyền sử dụng.
- Chưa quyết định: thông tin đơn hàng/sản phẩm/hạn bảo hành của khách sẽ hiển thị ở đâu và lấy từ đâu (SRS hiện chưa có thực thể đơn hàng).

## Brand Commitments

- Giữ tên **Clarune**. Logo hiện tại ([docs/design/brand/](docs/design/brand/)) sẽ được thiết kế lại theo phong cách mới.

## Evidence on Hand

- Chính sách bảo hành/đổi trả công khai của các chuỗi điện máy đã khảo sát (ví dụ Điện Máy Xanh) dùng làm tham khảo để viết tài liệu mẫu. Không chép nguyên văn; tài liệu demo là của một chuỗi giả định.
- Chưa có khách hàng thật, đánh giá, số liệu sử dụng hay kết quả test người dùng. Không được bịa các nội dung này.

## Product Principles

1. Đúng chính sách trước, nhanh sau: mọi câu trả lời phải truy được về tài liệu nguồn.
2. Con người quyết định: AI chỉ gợi ý, người có quyền mới gửi.
3. Khách luôn biết yêu cầu của mình đang ở đâu và bước tiếp theo là gì.
4. Nhân viên thấy đủ bối cảnh (khách, sản phẩm, lịch sử) mà không phải rời ticket.

## Accessibility & Inclusion

- Tương phản chữ từ 4,5:1 ở cả Light và Dark; trạng thái luôn có chữ, không chỉ dựa vào màu.
- Focus bàn phím rõ, nhãn cho icon, vùng chạm mobile tối thiểu 44×44px.
