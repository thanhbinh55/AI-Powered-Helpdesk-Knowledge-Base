# 5. BẢN MẪU GIAO DIỆN

> **Hướng dẫn nhận việc:** [T1-UI-01 — nguồn đọc, từng bước, đầu ra và bàn giao](../../TASK_PLAYBOOK_TEMPLATE1.md#t1-ui-01). File khung chưa phải bằng chứng task đã hoàn thành.


> **Tổng hợp:** Lê Quý Phúc; từng owner tự làm màn hình module mình. Bản nháp 06/11, tổng hợp/review 07/11, sửa cuối trước 20:00 08/11.

**Figma prototype:** TODO — chưa có link file/prototype thật được xác minh. Không dùng trang chủ Figma làm minh chứng.

| Module | Người làm | Màn hình/nhánh phải có | Minh chứng |
|---|---|---|---|
| Identity | Bình | Register/login/profile/Agent management; invalid credentials, disabled, validation | TODO |
| Ticket | Gia Phúc | Customer ticket, queue/workspace; claim conflict, WAITING_CUSTOMER, public/internal và quyền | TODO |
| Knowledge | Lãm | Upload, PROCESSING/READY unpublished/FAILED, publish/archive; file không hỗ trợ | TODO |
| AI | Quý Phúc | Generated/citations, insufficient evidence, timeout, review/edit/send/discard | TODO |
| Analytics P1 | Quý Phúc; Gia Phúc review | Thống kê ticket theo state/Agent; không gán thành code P0 | TODO |

Ảnh lưu `assets/mockups/`, hiển thị rõ ở A4; mỗi flow có loading/error/empty/disabled phù hợp. Gắn UC/FR cho màn hình; screenshot prototype không phải bằng chứng backend chạy. Lãm/Gia Phúc kiểm tra Figma bằng tài khoản ngoài nhóm và kiểm tra ảnh sau giải nén trước khi chốt. Không đánh Done khi còn TODO.
