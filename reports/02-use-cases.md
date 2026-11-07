# Đặc tả Use Case — chỉ mục baseline

> Cập nhật 03/11/2026. Bản khung UC01..UC07 cũ bị thay vì trái SRS; không dùng để triển khai hoặc nộp.

Danh mục chuẩn là **UC-01..UC-17** tại [SRS Mục 3.3](SRS-master.md); các đặc tả trọng tâm ở Mục 6. Bản Template 1 có owner/reviewer và chín trường tại [template1/04-dac-ta-use-cases](template1/04-dac-ta-use-cases/04.1-so-do-tong-the.md).

| Nhóm | Use Cases | Owner |
|---|---|---|
| Identity | UC-01..04, UC-16 P1 | Bình |
| Ticket | UC-05..10 | Gia Phúc |
| Knowledge | UC-11..13 | Lãm |
| AI | UC-14/15 | Quý Phúc |
| Analytics nghiệp vụ Ticket | UC-17 P1, file đặc tả riêng | Quý Phúc; Gia Phúc review |

Actor: Guest, Customer, Agent, Admin và dịch vụ ngoài khi có tương tác. Worker/DB/storage là thành phần nội bộ. Customer không tra cứu KB hay gọi AI trực tiếp; Agent chỉ xử lý ticket được giao, Admin quản trị KB. Không dùng auto-classification/auto-priority hoặc Customer chat AI từ bản khung cũ làm yêu cầu.

UC gộp có luồng riêng theo trigger/actor/state; hậu điều kiện thất bại và BR/test phải rõ. Tạo ticket dùng UC-05, gồm ticket + public message đầu + event trong một transaction. UC-11 kết thúc READY chưa publish; UC-12 publish/archive. UC-14 không gửi message; UC-15 chỉ gửi text đã được Agent duyệt. Sơ đồ tham khảo và quy tắc boundary ở [kế hoạch Mục 5](../PLAN_TEMPLATE1_AND_DEVELOPMENT.md); đây chưa phải bộ ảnh đã vẽ/xuất hoàn chỉnh.
