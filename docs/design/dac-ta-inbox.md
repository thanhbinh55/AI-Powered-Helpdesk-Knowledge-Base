# Helpdesk — Thiết kế lại theo luồng hộp thư

> **Ghi chú 03/11/2026:** tài liệu này là đặc tả luồng, bố cục, responsive và hành vi AI. Ngôn ngữ thị giác (mục 7) đã được thay bằng [MASTER v2](../../design-system/helpdesk-workspace/MASTER.md). Bản Figma Inbox 27/10 đã xóa; thiết kế hiện hành là các page `Redesign v2 / …`, xem [bảng màn hình](man-hinh.md).

Ngày: 2026-10-27. **Trạng thái: hướng A và bản đặc tả đã được người dùng duyệt trong chat ngày 2026-10-27.** Đã dựng native Figma và xuất bộ preview; phạm vi prototype, kết quả kiểm tra và các hành vi cần triển khai tiếp được ghi tại [bàn giao](README.md).

## 1. Mục tiêu và phạm vi

Người dùng cho phép thay cấu trúc, layout, component và bảng màu để nâng chất lượng giao diện; ưu tiên nhân viên xử lý nhiều ticket liên tiếp, chuyển nhanh giữa các yêu cầu. Thành công được đánh giá bằng độ rõ của nội dung, khả năng chuyển việc và tính nhất quán giữa màn hình, cùng chất lượng thị giác khi có dữ liệu thực dài.

Đầu ra là thiết kế native Figma qua Figwright, prototype các luồng tiêu biểu, design system và bộ preview đồng bộ. Repository hiện chỉ có tài liệu frontend; đợt này tổ chức lại thiết kế và tài liệu bàn giao, chưa triển khai ứng dụng hoặc thay hợp đồng API.

Nguồn nghiệp vụ: [SRS](../../reports/SRS-master.md), đặc biệt FR-TK-01..10, FR-KB-01..09, FR-AI-01..09 và BR-01..16. Đặc tả cũ ngày 25/10/2026 (lưu ngoài repo) là mốc đối chiếu phạm vi và inventory; những quyết định thị giác mới nằm trong tài liệu này. [MASTER hiện hành](../../design-system/helpdesk-workspace/MASTER.md) và [Figma map](figma-map.json) đã đồng bộ với bản Redesign v2; đặc tả vẫn chứa các yêu cầu frontend chưa thể chứng minh bằng prototype.

Giả định tiếp tục áp dụng: một tổ chức, tiếng Việt, ba vai trò Customer/Agent/Admin; Agent/Admin ưu tiên desktop, Customer dùng được trên mobile. Dữ liệu minh họa dùng tên giả và email example.com. Dashboard thống kê, SLA, attachment, Kanban kéo thả, OCR và automation chưa thuộc phạm vi P0 này.

## 2. Lựa chọn bố cục và đánh đổi

| Phương án | Lợi ích | Đánh đổi |
| --- | --- | --- |
| A — Danh sách liền hội thoại, đã chọn | Giữ hàng đợi, bộ lọc và vị trí khi chuyển ticket | Cần quản lý không gian khi mở AI/nguồn và giữ đúng bản nháp từng ticket |
| B — Hội thoại toàn màn hình | Thuận tiện đọc trao đổi dài | Chuyển ticket mất ngữ cảnh danh sách |
| C — Bảng và ngăn xem nhanh | So sánh và phân công thuận tiện | Phản hồi khách hàng trở thành thao tác trong vùng phụ |

Agent dùng A làm trải nghiệm chính. Admin vẫn dùng bảng khi cần so sánh tài liệu/nhân viên; mở ticket sử dụng cùng workspace hội thoại. Không ép mọi loại dữ liệu vào một kiểu danh sách.

## 3. Cấu trúc thông tin

| Vai trò | Điều hướng chính | Nội dung mặc định |
| --- | --- | --- |
| Agent | Yêu cầu; Kho tri thức; menu hồ sơ | Yêu cầu, nhóm Của tôi; có nhóm Chưa phân công |
| Admin | Yêu cầu; Kho tri thức; Nhân viên; menu hồ sơ | Danh sách yêu cầu với lọc người phụ trách và trạng thái |
| Customer | Yêu cầu của tôi; Hồ sơ | Yêu cầu của chính mình và hành động tiếp theo |

Nhóm Chờ khách phản hồi là bộ lọc của các ticket được quyền xem, không phải luồng hay trạng thái mới. Các con số chỉ xuất hiện khi có dữ liệu tổng tương ứng; không dùng số lượng trang hiện tại như tổng toàn bộ. Không bổ sung dấu chưa đọc hoặc SLA đếm ngược khi chưa có dữ liệu hỗ trợ.

Loại bỏ header toàn cục trùng với tiêu đề vùng làm việc. Tên tổ chức ở đầu điều hướng; hồ sơ ở chân điều hướng. Tìm kiếm nằm trong danh sách đang thao tác, kèm bộ lọc có nhãn và trạng thái đang áp dụng.

## 4. Workspace Agent/Admin

### 4.1 Bố cục desktop

Mẫu chính 1440 × 900 px. Điều hướng sáng rộng 184 px; danh sách ticket rộng 320 px; vùng hội thoại dùng phần còn lại. Các vùng nối nhau bằng đường phân cách mảnh, không bọc từng vùng trong thẻ bo góc nổi trên nền.

AI/nguồn mặc định đóng. Khi mở ở viewport từ 1440 px, ngăn ngữ cảnh rộng 320 px; tại 1440 px hội thoại còn 616 px. Đóng ngăn trả lại diện tích cho hội thoại. Ngăn dùng tab Thông tin / Trợ lý AI; xem trích dẫn thay nội dung bên trong ngăn, có nút quay lại bản nháp, không mở nhiều ngăn xếp ngang.

```text
Mặc định:  [ Điều hướng 184 ][ Ticket 320 ][ Hội thoại 936            ]
Mở AI:     [ Điều hướng 184 ][ Ticket 320 ][ Hội thoại 616 ][ Ngữ cảnh 320 ]
```

Header mỗi vùng giữ tại đầu vùng; danh sách và thread cuộn độc lập. Composer ở đáy vùng hội thoại, tham gia layout và không phủ tin nhắn. Nội dung đọc giới hạn khoảng 760 px khi vùng hội thoại rộng; khoảng đệm ngang 24–32 px theo chiều rộng còn lại.

### 4.2 Danh sách ticket

Một mục có người gửi và thời gian, tiêu đề tối đa hai dòng, một dòng nội dung công khai gần nhất, mã và trạng thái. Metadata dùng màu chữ phụ; ưu tiên cao có cả icon và nhãn. Mục đang chọn dùng nền nhấn nhẹ và chỉ dấu cạnh; không chỉ dựa vào màu để nhận biết.

Chiều cao mục mẫu 104–120 px; nội dung dài có thể tăng chiều cao. Preview chỉ lấy nội dung công khai được phép xem, không để ghi chú nội bộ xuất hiện trong preview Customer. Nếu dữ liệu danh sách chưa có tin nhắn gần nhất, dùng mô tả công khai đã có; hợp đồng trả preview cần xác nhận khi làm frontend, không truy vấn riêng từng dòng chỉ để lấy snippet.

Chọn mục mở chi tiết tại chỗ và cập nhật định danh ticket trong điều hướng. Bộ lọc, phân trang, vị trí cuộn và lựa chọn được giữ khi quay lại. Không tự chọn ticket khác khi hàng đợi cập nhật. Nếu ticket đang xem rời bộ lọc sau một hành động hợp lệ, giữ chi tiết và hiển thị lời giải thích cùng nút quay về kết quả.

### 4.3 Hội thoại và hành động

Header gồm mã, tiêu đề, trạng thái, người phụ trách và thao tác phù hợp quyền. Tiêu đề xuống dòng tự nhiên. Thông tin ít dùng đặt trong ngăn Thông tin. Nội dung gồm public message, internal note phân biệt rõ bằng nhãn/nền, và các sự kiện nhận/phân công/đổi trạng thái dạng dòng thời gian gọn.

Composer có hai tab Phản hồi công khai / Ghi chú nội bộ, nhãn người nhận hoặc đối tượng xem, và nút Gửi. Ô nhập ban đầu cao khoảng 120 px; tăng theo nội dung tới 240 px ở desktop rồi cuộn bên trong. Trên viewport thấp, giới hạn theo không gian còn lại để vẫn đọc được tin nhắn. Không đặt vùng nhập trống cao cố định chiếm phần lớn thread.

Gửi là hành động nhấn chính khi đang soạn. Các thao tác Yêu cầu bổ sung, Đánh dấu đã giải quyết và Phân công giữ nhãn rõ và chỉ xuất hiện khi hợp lệ. Không tự gửi khi Enter; xuống dòng là hành vi mặc định. Mọi phím tắt bổ sung phải có hướng dẫn và không thay thế nút hiển thị.

### 4.4 Chuyển ticket và bản nháp

Yêu cầu UX cho frontend: giữ bản nháp trong phiên ứng dụng theo khóa tài khoản + ticket + PUBLIC/INTERNAL. Đổi ticket hoặc đổi tab không làm mất nội dung. Không hứa đồng bộ đa thiết bị hoặc khôi phục sau reload; không tự ghi nội dung hỗ trợ vào localStorage. Khi rời/reload trang có nội dung chưa gửi, frontend cần cảnh báo theo khả năng trình duyệt.

Gửi thành công chỉ xóa phần nội dung đã gửi của đúng ticket và đúng tab. Khi đang gửi, khóa thao tác gửi lặp và nội dung đang gửi; vẫn có thể chuyển sang ticket khác. Phản hồi mạng quay về phải gắn đúng ticket/request, không xóa hoặc ghi đè composer hiện tại của ticket khác. Gửi lỗi giữ nguyên bản nháp và cho thử lại tại chỗ.

Nếu quyền thay đổi hoặc ticket bị chuyển cho người khác, đóng khả năng sửa/gửi, thông báo và rời dữ liệu không còn được phép xem; không để bản nháp nội bộ tiếp tục hiện dưới ticket khác. Xóa bản nháp trong bộ nhớ khi đăng xuất hoặc đổi tài khoản. Đây là yêu cầu thiết kế hành vi, chưa phải tính năng đã được triển khai.

### 4.5 Nhận việc, trạng thái và lỗi

- Ticket OPEN: đọc nội dung theo quyền; Agent phải Nhận xử lý thành công trước khi soạn hoặc gọi AI. Conflict 409 hiện thông báo ngay tại chi tiết và cập nhật danh sách; không giả lập nhận thành công.
- IN_PROGRESS: Agent được giao/Admin có thể gửi, yêu cầu thông tin hoặc đánh dấu giải quyết. Gửi bình thường không tự chuyển trạng thái.
- WAITING_CUSTOMER: Agent được giao/Admin vẫn có thể phản hồi; Customer trả lời sẽ chuyển về IN_PROGRESS. Không cung cấp RESOLVE trực tiếp từ trạng thái này vì bảng transition SRS không cho phép.
- RESOLVED: Customer thấy Mở lại / Xác nhận đóng, Admin có thể đóng theo SRS. Không hiện composer gửi trực tiếp. CLOSED là chỉ đọc.
- Admin có Phân công cho OPEN và chuyển người phụ trách ở IN_PROGRESS/WAITING_CUSTOMER; Agent thường không có thao tác này.
- Loading giữ khung; empty không có kết quả khác với chưa có ticket; lỗi tải chi tiết có thử lại và giữ danh sách dùng được. Khi chọn ticket B, nội dung A phải được thay bằng loading của B, không hiển thị lẫn danh tính và nội dung.

## 5. Trợ lý AI và nguồn

Nút mở Trợ lý AI có nhãn ở vùng ticket/composer; mở ngăn không tự gọi sinh câu trả lời. Tạo gợi ý là hành động riêng, chỉ hoạt động sau khi kiểm tra quyền. Trạng thái gồm chưa tạo, đang tạo, bản nháp có nguồn, thiếu bằng chứng, lỗi và đã chèn.

Bản nháp và danh sách trích dẫn cùng xuất hiện trong ngăn; nhãn Cần kiểm tra trước khi gửi luôn nhìn thấy. Nguồn hiển thị tên tài liệu, trang/mục nếu có và đoạn trích. Mở nguồn giữ lại ticket, composer và bản nháp. Chỉ có một nguồn đang đọc trong ngăn tại một thời điểm.

Chèn vào phản hồi chỉ đặt nội dung vào bản nháp PUBLIC của ticket tương ứng. Nếu bản nháp đó đã có chữ, mở xác nhận Thay thế / Hủy. Nếu đang ở tab nội bộ, hành động chỉ chuyển sang PUBLIC sau khi xử lý xác nhận; nội dung nội bộ được giữ riêng. Chèn không gửi tin, đổi trạng thái hoặc ghi suggestion là APPLIED; APPLIED chỉ liên quan lần gửi thành công theo hợp đồng nghiệp vụ.

Kết quả sinh AI gắn với ticket/request đã gọi. Chuyển ticket trong lúc chờ không đưa gợi ý sang ticket mới. Lỗi AI không chặn soạn và gửi thủ công. Không có nguồn thì hiển thị thiếu căn cứ; không dựng citation hoặc phần trăm tin cậy giả. Nguồn lịch sử dùng snapshot theo SRS, kể cả khi tài liệu hiện tại đã archive.

## 6. Customer, Knowledge Base và các màn hình phụ

**Customer:** navigation ngang gọn. Danh sách dạng các hàng tóm tắt rộng, thể hiện trạng thái, trao đổi gần nhất và việc cần làm. Có lối lọc yêu cầu cần phản hồi; không tự đổi thứ tự người dùng đang chọn. Trên desktop, trang chi tiết có thread và thông tin phụ gọn; trên mobile, thông tin phụ thu lại dưới header. Tạo yêu cầu dùng form một cột, nhãn ngoài ô nhập và trợ giúp tại trường. Customer không thấy internal note, AI, KB nội bộ hoặc mức ưu tiên có thể chỉnh.

**Knowledge Base:** Agent có danh sách tài liệu công bố và vùng đọc; Admin có bảng xử lý/công bố và ngăn chi tiết. Tên tài liệu là điểm nhấn chính. Trạng thái xử lý tách cột với trạng thái công bố. Upload có một hành động chính và khu vực hiển thị kết quả nhận/xử lý file. PDF có văn bản/TXT/MD tối đa 10 MiB; file scan và lỗi ingestion có lý do, hành động hợp lệ. Archive xác nhận theo đúng tài liệu và giữ nguồn lịch sử.

**Nhân viên:** bảng gọn, bộ lọc hoạt động và dialog tạo/vô hiệu hóa theo người được chọn. **Hồ sơ:** nhóm thông tin và đổi mật khẩu với trạng thái lỗi/lưu rõ ràng. **Auth:** form dễ đọc, nhận diện Helpdesk tiết chế, bỏ trang trí mô phỏng số liệu hoặc lời chứng thực. Đăng ký công khai chỉ dành cho Customer.

## 7. Ngôn ngữ thị giác

> **Đã thay bằng redesign v2 (28/10/2026).** Bảng màu, font Inter và bo góc control 8 trong mục này chỉ còn là hồ sơ của bản 27/10. Token hiện hành (Be Vietnam Pro, xanh coban `#2F4FD8`, Light/Dark) nằm ở [MASTER.md](../../design-system/helpdesk-workspace/MASTER.md). Các nguyên tắc về nhịp chữ, đường kẻ và cách tránh trang trí thừa vẫn áp dụng.

Sidebar sáng, nền xám ấm nhẹ và vùng nội dung trắng. Tính nhất quán đến từ nhịp chữ, đường căn và mức nhấn. Tránh gradient trang trí, glow, icon ngôi sao lặp lại cho AI, badge màu cho mọi dữ liệu và card lồng nhau không có tác dụng.

| Token đề xuất | Giá trị | Vai trò |
| --- | --- | --- |
| canvas | #F7F7F5 | Nền ứng dụng |
| surface | #FFFFFF | Hội thoại, danh sách, form |
| sidebar | #F3F2EF | Điều hướng sáng |
| text | #23262F | Nội dung chính |
| muted | #646875 | Nội dung phụ |
| border | #DFE1E5 | Phân cách trang trí |
| control | #7C8291 | Biên control cần nhận biết |
| accent | #4056C7 | Hành động chính, link và focus |
| selected | #EEF0FF | Mục đang chọn |

Màu trạng thái tiếp tục dùng cặp semantic đã có: processing #335EAA/#EDF2FC; positive #23724D/#EAF5EF; amber #875700/#FFF5DF; red #B23939/#FCECEC. Luôn kèm chữ/icon có ý nghĩa. Alias token cũ được ánh xạ có chủ đích trong kế hoạch thực hiện; không đổi token nav tối sang sáng mà bỏ sót chữ trắng của instance cũ.

Tương phản tính từ mã màu sRGB: text/surface 15,11:1; muted/surface 5,56:1; muted/sidebar 4,96:1; surface/accent 6,22:1; accent/selected 5,50:1; control/surface 3,85:1. Đây là kiểm tra palette đề xuất, chưa xác nhận toàn bộ layer Figma sau đổi màu.

Font Inter hỗ trợ nội dung tiếng Việt. Tiêu đề trang 24/32 semibold, tiêu đề ticket 20/28 semibold, section 16/24 semibold, nội dung hội thoại 15/24; mobile/form input 16/24; danh sách 14/22, nhãn 13/20, metadata 12/18. Khoảng cách 4/8/12/16/24/32. Control radius 8, dialog 12; các vùng workspace phân cách phẳng. Icon outline thống nhất; icon thao tác độc lập có nhãn truy cập và tooltip.

UI/UX Pro Max được đối chiếu với kết quả Minimalism & Swiss Style phù hợp công cụ làm việc. Kết quả tự động thiên về landing page ở lần tìm design-system không được dùng làm bố cục ứng dụng. Các lựa chọn palette và hình học ở đây là thiết kế cho dự án, không phải kết quả nghiên cứu người dùng đã được xác thực.

## 8. Responsive và khả năng tiếp cận

| Chiều rộng viewport | Bố cục |
| --- | --- |
| Từ 1440 px | Điều hướng 184; danh sách 320; hội thoại co giãn; ngăn AI 320 dock khi mở |
| 1024–1439 px | Điều hướng 72 có tooltip/nhãn truy cập; danh sách 280; hội thoại còn lại; AI/nguồn mở overlay tối đa 360 |
| 768–1023 px | Điều hướng 72; danh sách hoặc chi tiết chiếm phần còn lại, có Quay lại; ngăn phụ dạng overlay |
| Dưới 768 px | Một màn hình mỗi bước; menu điều hướng mở từ header; AI/nguồn toàn màn hình phụ |

Ở layout rộng, mở AI chỉ giảm vùng hội thoại, không tự ẩn danh sách. Ở layout overlay, khi mở thì quản lý focus trong overlay; Escape/Đóng trả focus về nút gọi. Quay về danh sách giữ vị trí và bộ lọc. Các ngưỡng là quy tắc thiết kế cần kiểm chứng trong frontend, không phải kết quả kiểm thử responsive đã có.

Desktop control thường 40 px, hành động chính 44 px; mobile vùng chạm tối thiểu 44 × 44 px và hành động chính 48 px. Giữ khoảng cách giữa các mục thao tác, không chỉ xuất hiện khi hover. Focus có outline rõ; Enter/Space mở mục phù hợp ngữ nghĩa, Back quay lại đúng ngữ cảnh.

Mobile composer và bàn phím phải chừa không gian cho nhau, tính safe area; không cố định chiều cao theo ảnh mẫu. Văn bản dài, zoom và chiều cao viewport thấp phải reflow. Chuyển trạng thái ngắn, không dùng animation bắt buộc để hiểu nội dung; giảm chuyển động theo cài đặt người dùng.

## 9. Tổ chức lại Figma và bàn giao

Giữ năm page theo vai trò hiện hành. Tái sử dụng icon và component đúng mục đích; tổ chức lại component cho NavigationItem, TicketListItem, TicketHeader, Message, ActivityEvent, ReplyComposer, ContextPanel và SourceCitation. Trạng thái visual, nhãn và dữ liệu có property rõ; layout co giãn bằng Auto Layout/constraints. UI chia theo trách nhiệm thay vì sao chép nguyên màn hình cho mỗi trạng thái.

Mỗi component cần xác định đầu vào và sự kiện: TicketList nhận kết quả được phân quyền + lựa chọn/bộ lọc; Conversation nhận ticket/thread hiện tại; Composer nhận bản nháp theo ticket và visibility + trạng thái gửi; ContextPanel nhận thông tin/gợi ý/nguồn của đúng ticket. Trạng thái chọn ticket, bộ lọc và bản nháp thuộc workspace điều phối, không nằm rải rác trong các hàng danh sách. Đây là cấu trúc handoff, chưa tạo component frontend.

Ưu tiên giữ ID các root có cùng chức năng để giảm đứt liên kết. Số 29 root/66 reactions của bản cũ là inventory kiểm kê, không phải ràng buộc giới hạn thiết kế mới. Chỉ thêm frame cần cho trạng thái có ý nghĩa: AI đóng/mở, chuyển ticket có draft, kích thước hẹp. Cập nhật map cho mọi ID và reaction thay đổi; kiểm tra nguồn/đích prototype. Không xóa page, file hoặc artifact cũ trong đợt này khi chưa có yêu cầu dọn riêng.

Prototype cần biểu diễn được: chọn ticket; nhận việc; soạn A → mở B → quay lại A còn nội dung; mở AI → xem nguồn → chèn → sửa → chủ động gửi; bản nháp đã có chữ → xác nhận thay thế; xung đột nhận việc; lỗi gửi giữ chữ. Native Figma mô phỏng bằng frame/variant/overlay và ghi rõ dữ liệu minh họa; không tuyên bố thực hiện lưu draft hoặc gọi API thật.

Khi hoàn tất mới cập nhật MASTER, handoff, Figma map và gallery/PNG hiện hành. Đặc tả cũ được giữ làm lịch sử với liên kết tới bản thay thế; không có nhiều bộ preview được trình bày cùng là bản hiện hành. Bản map mới ghi phạm vi đã dựng, số frame/reaction thực tế và giới hạn còn lại.

## 10. Tiêu chí nghiệm thu và rủi ro

| Kiểm tra | Điều kiện đạt |
| --- | --- |
| Chuyển việc | Chọn ticket trong danh sách mở bên cạnh; giữ bộ lọc/vị trí và có trạng thái chọn rõ |
| Draft | Demo A → B → A giữ đúng nội dung; PUBLIC/INTERNAL tách biệt; gửi lỗi không mất chữ |
| Quyền/state | Không soạn hoặc gọi AI trước claim; không có transition ngoài SRS; Customer không thấy dữ liệu nội bộ |
| AI | Xem nguồn quay lại đúng bản nháp; chèn không gửi; thay chữ có xác nhận; lỗi AI vẫn soạn tay được |
| Thị giác | Rà ảnh ở 1440 × 900, 1024 × 768 và 390 × 844; không tràn/chồng/cắt chữ; trạng thái dài và nhiều dòng vẫn đọc được |
| Token/component | Kiểm tra binding và màu thực của instance, đặc biệt đổi sidebar sáng; không còn chữ trắng trên nền trắng |
| Tương phản | Chữ thường tối thiểu 4,5:1; chữ lớn và chỉ dấu control phù hợp tối thiểu 3:1; ghi riêng control disabled |
| Prototype | Đọc lại mọi reaction, đúng đích và nút đóng/quay lại; không có liên kết mồ côi |
| Bàn giao | Map/PNG đúng kích thước và số lượng; gallery mở/lọc/phóng ảnh được; link nội bộ và cú pháp script hợp lệ |

Kiểm tra nội dung dài gồm tiêu đề 150 ký tự, tên người dài, message gần giới hạn 5000 ký tự và nhiều nguồn. Không mở rộng chiều cao vô hạn tới mức mất thao tác chính; vùng dài cuộn rõ ràng. Kiểm thử keyboard, screen reader, zoom, bàn phím mobile và race giữa request phải thực hiện lại khi có frontend; ảnh Figma không chứng minh các hành vi này.

Rủi ro chính là workspace nhiều cột bị chật, bản nháp/gợi ý gắn sai ticket khi chuyển nhanh và token cũ để lại override màu. Bố cục overlay ở màn hình hẹp, quy tắc state theo ticket/request và audit binding là các biện pháp thiết kế tương ứng. Dữ liệu preview tin nhắn và tổng bộ lọc còn phụ thuộc hợp đồng API; dùng fallback đã nêu thay vì thêm dữ liệu không có.

## 11. Mốc review

Hướng A, ưu tiên xử lý liên tiếp và bản đặc tả đã được người dùng xác nhận. Bản đặc tả đã được tự rà về phạm vi, quyền, transition, hình học, bản nháp và tương phản palette trước khi review. Bước tiếp theo là review kế hoạch thực hiện qua Figwright (kế hoạch, lưu ngoài repo) và chọn cách thực hiện. Không tạo commit hoặc đổi branch khi chưa được yêu cầu.
