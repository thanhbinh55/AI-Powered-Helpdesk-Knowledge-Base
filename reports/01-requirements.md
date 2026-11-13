# Báo cáo yêu cầu — chỉ mục baseline hiện hành

> Cập nhật 12/11/2026 theo [Report.pdf](template1/report/Report.pdf). Bản Markdown đối chiếu: [report.md](template1/report/report.md). PDF final được ưu tiên khi có khác biệt với nguồn soạn thảo cũ.

Bộ yêu cầu gồm **41 FR, 19 NFR và 19 Use Case**. Các bản theo mục đã đồng bộ:

- [Mô tả bài toán và phạm vi P0/P1](template1/02-mo-ta-bai-toan.md).
- [Stakeholder và sơ đồ bối cảnh P0](template1/03-tong-quan-yeu-cau/03.1-stakeholders.md); Email đặt lại mật khẩu là P1 tại UC-16.
- [41 yêu cầu chức năng](template1/03-tong-quan-yeu-cau/03.2.1-yeu-cau-chuc-nang.md).
- [19 yêu cầu phi chức năng](template1/03-tong-quan-yeu-cau/03.2.2-yeu-cau-phi-chuc-nang.md); giữ nguyên mục tiêu của PDF, chưa phải kết quả đo đạt.
- [Prototype](template1/05-prototype-mockup.md): 34 nhóm màn hình, 229 frames, 82 flow points; bản report dùng 31 ảnh UI.

FR–TK–03 bao gồm tìm kiếm/lọc/phân trang; FR–TK–09 quy định chuyển trạng thái hợp lệ; FR–TK–10 là lịch sử xử lý. FR–KB–05 theo dõi tiến trình và thử lại tối đa 3 lần kể cả lần đầu; FR–KB–09 xem danh mục tài liệu. FR–AI–10 chỉ đánh giá Hữu ích/Không hữu ích, không yêu cầu dashboard chất lượng AI.

[SRS](SRS-master.md) giữ chi tiết triển khai và 30 user stories. [MVP contracts](MVP_CONTRACTS.md) mô tả giao tiếp kỹ thuật. Attachments, OCR/quản lý phiên bản, reset password, thống kê ticket và đánh giá AI là P1. Xem lịch sử gợi ý AI (UC-18) thuộc P0. Không tự mở rộng phạm vi hoặc dùng mock/prototype làm bằng chứng tính năng thật đã hoạt động.
