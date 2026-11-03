# Báo cáo yêu cầu — chỉ mục baseline hiện hành

> Group 04. Cập nhật 03/11/2026. Bản khung 19/10 đã được thay vì dùng mã và chức năng không khớp SRS. Tài liệu này không định nghĩa lại bộ ID yêu cầu.

**Nguồn chuẩn:** [SRS Mục 3–8 và Phụ lục D](SRS-master.md). Bản nộp Template 1 được soạn tại [template1](template1/03-tong-quan-yeu-cau/03.2.1-yeu-cau-chuc-nang.md), chốt 20:00 ngày 08/11. Owner mỗi module cung cấp mapping; Gia Phúc tổng hợp, Lãm review.

- Identity — Bình: xác thực/session/profile, quản lý Agent, RBAC/ownership.
- Ticket — Gia Phúc: tạo/xem/lọc, claim/assign, public/internal, state và audit; đủ WAITING_CUSTOMER.
- Knowledge — Lãm: Admin upload PDF/TXT/MD, xử lý nền, publish/archive, Agent/Admin tra cứu.
- AI — Quý Phúc: RAG dựa nguồn, citation, abstention, duyệt/sửa/gửi thủ công; không tự phân loại/đổi priority hay tự gửi cho Customer.

41 FR dùng mã FR-ID/FR-TK/FR-KB/FR-AI của SRS Mục 4. US-01..30 chỉ theo Phụ lục D; NFR dùng đúng mã, mục tiêu và điều kiện đo của SRS Mục 8. Không dùng mã FR-AUTH/FR-TCK hoặc mục tiêu 500ms/100 concurrent từ bản khung cũ làm cam kết. Attachments, OCR, reset password, Analytics và feedback là P1 theo SRS; các tính năng ngoài SRS cần change request, không tự thêm vào MVP.

Khả năng chạy mock là chế độ test/demo được công bố, không phải tự chuyển từ live sang câu trả lời giả khi provider lỗi. Runtime timeout phải thông báo rõ và Ticket vẫn dùng được.

Truy vết FR → story → UC → BR → mockup/test/PR là nhiều-nhiều; coverage cross-cutting security/privacy không được bỏ sót. Báo cáo này là chỉ mục, chưa chứng minh bản nộp Template 1 đã hoàn tất hoặc NFR đã đo đạt.
