# Helpdesk — hướng dẫn thiết kế

Tài liệu đầu vào cho người và AI khi làm giao diện dự án. Đọc file này trước khi đề xuất hoặc sửa UI.

- **Figma Design chính thức:** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)
- **Tài liệu làm việc nhóm (Google Docs):** [[SE - Nhóm 4] template1](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0)
- **Báo cáo Mục 5 Template 1:** [05-prototype-mockup.md](reports/template1/05-prototype-mockup.md)

## Thứ tự áp dụng

1. [SRS](reports/SRS-master.md): quyền, nghiệp vụ và trạng thái ticket.
2. [Đặc tả Inbox](docs/design/dac-ta-inbox.md): luồng, bố cục, responsive và hành vi AI.
3. [Design system Helpdesk v2](design-system/helpdesk-workspace/MASTER.md): token, typography, component.
4. [Bộ thiết kế v2](docs/design/README.md): bảng màn hình, prototype và giới hạn đã biết.

Từ 28/10/2026, token thị giác (màu, font, cỡ chữ, bo góc, đổ bóng) lấy theo MASTER v2, thay cho mục 7 "Ngôn ngữ thị giác" của đặc tả Inbox. Luồng, bố cục, responsive và hành vi AI vẫn theo đặc tả.

Không tự thay thiết kế đã được duyệt bằng mẫu tham khảo bên ngoài. Khi các tài liệu dự án mâu thuẫn, nêu rõ mâu thuẫn trước khi thay đổi quy tắc liên quan.

## Ngôn ngữ thị giác

Phương án A "Bàn làm việc yên tĩnh": chữ phân cấp rõ, bề mặt sáng, viền mảnh, ít trang trí. Font Be Vietnam Pro, accent xanh coban `#2F4FD8`. Không đưa hero lớn, pricing card hoặc khoảng cách kiểu trang marketing vào workspace.

## Quy tắc cho màn làm việc

- Agent: điều hướng → danh sách ticket → hội thoại; AI mặc định đóng, mở theo yêu cầu. Bố cục hẹp tuân theo đặc tả Inbox.
- Giữ bản nháp theo ticket và PUBLIC/INTERNAL; chèn gợi ý AI không tự gửi tin nhắn.
- Customer không thấy ghi chú nội bộ; giữ quyền nhận việc và chuyển trạng thái theo SRS.
- Trạng thái có chữ; màu không phải dấu hiệu duy nhất. Có focus bàn phím rõ, nhãn cho icon và vùng chạm mobile phù hợp.
- Dùng token v2 (`Helpdesk v2 / Color`, `Dimension`, `Typography`) và text style `v2 / …`; không hardcode màu, cỡ chữ, khoảng cách. Giá trị và tên CSS ở MASTER.
- Giao diện có Light và Dark; kiểm tra tương phản và trạng thái ở cả hai mode.
- Kiểm tra loading, empty, error, disabled, văn bản tiếng Việt dài và responsive khi triển khai; prototype không chứng minh các trạng thái đã hoạt động trong frontend.

Các file này là tài liệu hướng dẫn, không tự đổi giao diện hoặc cài component vào frontend.
