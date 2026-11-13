# Đặc tả Use Case — chỉ mục baseline hiện hành

> Cập nhật 12/11/2026 theo [Report.pdf](template1/report/Report.pdf) và [report.md](template1/report/report.md).

Danh mục gồm **UC-01 đến UC-19**, mỗi bảng đủ 9 trường; **16 P0 và 3 P1** (UC-16, UC-17, UC-19).

| Nhóm | Use Cases | Owner | Đặc tả |
|---|---|---|---|
| Identity | UC-01..04, UC-16 P1 | Ngô Viết Thanh Bình | [Module D](template1/04-dac-ta-use-cases/04.2-module-D-identity.md) |
| Ticket | UC-05..10 | Phan Gia Phúc | [Module C](template1/04-dac-ta-use-cases/04.2-module-C-ticket.md) |
| Knowledge | UC-11..13 | Nguyễn Đức Lãm | [Module B](template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md) |
| AI | UC-14/15/18, UC-19 P1 | Lê Quý Phúc | [Module A](template1/04-dac-ta-use-cases/04.2-module-A-ai.md) |
| Thống kê ticket | UC-17 P1 | Lê Quý Phúc; Gia Phúc review nghiệp vụ | [UC-17](template1/04-dac-ta-use-cases/04.2-uc-17-analytics.md) |

[Sáu sơ đồ final](template1/04-dac-ta-use-cases/04.1-so-do-tong-the.md) dùng SVG/drawio trong [report/assets/diagrams](template1/report/assets/diagrams/). UC-17 nằm trong sơ đồ Trợ lý AI và thống kê theo cách trình bày của PDF; chức năng thống kê chỉ tính ticket. UC-19 chỉ dành cho Agent được giao, không dành cho Admin.

Worker/DB/storage là thành phần nội bộ. Customer không tra cứu KB hoặc gọi AI trực tiếp. UC-11 kết thúc xử lý nhưng chưa tự công bố; UC-12 công bố/lưu trữ. UC-14 tạo gợi ý, UC-15 kiểm duyệt/gửi hoặc bỏ gợi ý, UC-18 đọc lịch sử và bản chụp nguồn, UC-19 lưu/đổi đánh giá. AI không tự gửi phản hồi hay thay đổi ticket.
