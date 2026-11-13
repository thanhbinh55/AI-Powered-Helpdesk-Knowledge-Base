# Helpdesk Workspace — Design system

**Helpdesk v2 · Neutral lạnh + Xanh coban**, phương án A "Bàn làm việc yên tĩnh" được chọn ngày 28/10/2026, có Light và Dark. Bản này thay bản *Inbox · Warm neutral + Indigo* ngày 27/10/2026. Quy tắc nghiệp vụ nằm ở [SRS](../../reports/SRS-master.md); luồng và bố cục ở [đặc tả inbox](../../docs/design/dac-ta-inbox.md). Riêng token thị giác (màu, font, bo góc), file này thay mục 7 của đặc tả. Quyết định và kế hoạch thiết kế được lưu ngoài repo, trong hồ sơ quá trình.

Trong Figma, bảng trình bày nằm ở page `Redesign v2 / Foundations`, frame `50:85`.

## Bố cục

Desktop 1440 × 900: sidebar 184 + danh sách 320 + hội thoại 936. Mở ngăn ngữ cảnh 320 thì hội thoại còn 616. AI và thông tin dùng cùng ngăn; nguồn có nút quay lại. Các vùng nối nhau bằng đường kẻ `border/default`; không bọc toàn bộ workspace trong card, không dùng gradient trang trí hoặc dashboard số liệu giả.

Từ 1024 đến 1439: rail 72 + list 280 + hội thoại; AI là overlay tối đa 360. Từ 768 đến 1023: rail 72 và một vùng list/detail. Mobile 390 × 844: danh sách, hội thoại, AI, nguồn là các màn hình riêng. Mọi kích thước trên đều có biến `layout/*`.

Customer: navigation ngang và tóm tắt yêu cầu rộng; form tối đa `layout/form` 640. Admin: bảng tài liệu có xử lý/công bố tách biệt và vùng detail; quản lý nhân viên tách khỏi xử lý ticket.

## Token màu

Collection `Helpdesk v2 / Color` (`VariableCollectionId:49:59`), mode Light `49:0` và Dark `49:3`. Token đặt tên theo vai trò. Mỗi biến có tên CSS sẵn: `bg/canvas` là `var(--bg-canvas)`. Chỉ cần đổi mode để chuyển giao diện; component không có màu riêng cho dark.

| Token | Light | Dark | Dùng cho |
| --- | --- | --- | --- |
| `bg/canvas` | `#F6F7F9` | `#0E1218` | Nền trang, vùng ngoài khung |
| `bg/surface` | `#FFFFFF` | `#151A22` | Vùng làm việc, thẻ, dialog |
| `bg/subtle` | `#F0F2F5` | `#1B212B` | Thanh bên, đầu bảng, vùng phụ |
| `bg/hover` | `#EBEEF2` | `#212835` | Hover dòng và mục điều hướng |
| `bg/inverse` | `#1F2533` | `#E7EAF0` | Tooltip, toast |
| `border/default` | `#E3E6EB` | `#2A313D` | Đường chia vùng, viền thẻ |
| `border/strong` | `#C9CED7` | `#3A4352` | Đường chia cần nhấn |
| `border/control` | `#7D8697` | `#788295` | Viền ô nhập, checkbox (≥ 3:1) |
| `text/primary` | `#161B26` | `#E7EAF0` | Chữ chính |
| `text/secondary` | `#566070` | `#A2AABA` | Chữ phụ, thời gian, metadata |
| `text/disabled` | `#A3AAB6` | `#5A6372` | Chữ khi bị vô hiệu |
| `text/inverse` | `#FFFFFF` | `#161B26` | Chữ trên nền inverse |
| `text/on-accent` | `#FFFFFF` | `#0B1020` | Chữ trên nút chính |
| `text/accent` | `#2442C2` | `#A8B8FF` | Liên kết, mục đang chọn |
| `accent/default` | `#2F4FD8` | `#5B76F0` | Nút chính, mục đang chọn |
| `accent/hover` | `#2742BC` | `#7189F3` | Hover nút chính |
| `accent/pressed` | `#1F369E` | `#879BF5` | Nhấn nút chính |
| `accent/subtle` | `#EBEFFD` | `#1D2645` | Nền dòng, mục đang chọn |
| `accent/subtle-hover` | `#DCE3FB` | `#253058` | Hover trên nền đang chọn |
| `focus/ring` | `#2F4FD8` | `#8EA2FF` | Vòng focus bàn phím |
| `ai/fg` | `#5B3CC4` | `#B9A6F7` | Chữ, icon của trợ lý AI |
| `ai/bg` | `#F1EDFC` | `#251F42` | Nền ngăn và thẻ gợi ý AI |
| `ai/border` | `#D8CDF6` | `#3D3370` | Viền thẻ gợi ý AI |
| `status/success/fg` | `#1E7A4C` | `#62C792` | Chữ, icon: Đã giải quyết, Sẵn sàng, Đã công bố |
| `status/success/bg` | `#E7F5EE` | `#10291D` | Nền badge, banner |
| `status/success/border` | `#B5DEC8` | `#1E4A33` | Viền banner |
| `status/warning/fg` | `#8A5A00` | `#E9B556` | Chữ, icon: Chờ khách phản hồi, ghi chú nội bộ, thiếu căn cứ |
| `status/warning/bg` | `#FFF4DB` | `#2C2412` | Nền badge, banner |
| `status/warning/border` | `#F0D59A` | `#54431C` | Viền banner |
| `status/danger/fg` | `#C0362C` | `#F2857A` | Chữ, icon: Lỗi, tạo gợi ý thất bại |
| `status/danger/bg` | `#FDECEA` | `#33191A` | Nền badge, banner |
| `status/danger/border` | `#F3C2BC` | `#5E2B29` | Viền banner |
| `status/info/fg` | `#1D63A3` | `#79B4EC` | Chữ, icon: Mới, thông tin |
| `status/info/bg` | `#E8F1FA` | `#122435` | Nền badge, banner |
| `status/info/border` | `#BCD5EE` | `#24435F` | Viền banner |
| `status/neutral/fg` | `#4B5565` | `#B4BBC8` | Chữ, icon: Đã đóng, Đã lưu trữ |
| `status/neutral/bg` | `#EEF0F3` | `#222935` | Nền badge, banner |
| `status/neutral/border` | `#D5D9E0` | `#3A4352` | Viền banner |
| `danger/solid` | `#C0362C` | `#F2857A` | Nút phá hủy (vô hiệu hóa, lưu trữ) |
| `danger/solid-hover` | `#A42D24` | `#F59D93` | Hover nút phá hủy |
| `text/on-danger` | `#FFFFFF` | `#1F0D0B` | Chữ trên nút phá hủy |
| `overlay/scrim` | `#161B26` 48% | `#000000` 64% | Lớp phủ sau dialog |
| `shadow/soft` | `#161B26` 8% | `#000000` 40% | Bóng gần của lớp nổi |
| `shadow/overlay` | `#161B26` 14% | `#000000` 56% | Bóng xa của lớp nổi |

**Tương phản.** Đã kiểm tra 51 cặp trên cả hai mode, tất cả đều đạt WCAG AA:
- Chữ trên mọi nền từ 4,5:1 trở lên. Ví dụ: `text/secondary` trên `bg/hover` là 5,5 (Light) và 6,3 (Dark); `text/on-accent` trên `accent/default` là 6,5 và 4,8.
- `border/control` và `focus/ring` trên các nền từ 3:1 trở lên.
- `text/disabled` được miễn theo WCAG.

**Quy ước màu.**
- Coban dùng cho thao tác và lựa chọn.
- Tím chỉ dành cho trợ lý AI.
- Amber cho trạng thái chờ và ghi chú nội bộ; xanh lá cho resolved, ready, published; đỏ cho lỗi.
- Trạng thái luôn có chữ, không chỉ chấm màu. Avatar trung tính.
- Ghi chú nội bộ phải có nhãn cho biết ai xem được.

## Typography

Be Vietnam Pro, thiết kế cho tiếng Việt, weight 400/500/600. Collection `Helpdesk v2 / Typography` (`VariableCollectionId:49:61`) chứa `font/family`, `font/weight/*`, `font/size/*` và `font/line/*`. Text style gắn trực tiếp vào các biến này.

| Text style | Cỡ / dòng | Weight | Dùng cho |
| --- | --- | --- | --- |
| `v2 / Display` | 28/36, tracking −1% | SemiBold | Tiêu đề trang Customer, Identity |
| `v2 / H1` | 20/28, tracking −0,5% | SemiBold | Tiêu đề màn, tiêu đề ticket |
| `v2 / H2` | 16/24 | SemiBold | Tiêu đề vùng, dialog, nhóm |
| `v2 / Body L` | 16/24 | Regular | Nội dung mobile, chữ trong ô nhập |
| `v2 / Body L strong` | 16/24 | Medium | Nút cỡ lớn, mobile |
| `v2 / Body reading` | 15/24 | Regular | Nội dung tin nhắn và tài liệu |
| `v2 / Body` | 14/22 | Regular | Mặc định desktop: danh sách, bảng, mô tả |
| `v2 / Body strong` | 14/22 | Medium | Nhãn nút, tên người gửi, dòng chưa đọc |
| `v2 / Label` | 13/20 | Medium | Nhãn trường, tab, mục điều hướng |
| `v2 / Caption` | 12/18 | Regular | Thời gian, metadata, chữ trợ giúp |
| `v2 / Caption strong` | 12/18 | Medium | Badge trạng thái, bộ đếm |
| `v2 / Code` | 13/20 | SemiBold | Mã ticket (HD-1048), mã tài liệu |

Text dài làm phần tử cao lên, không cắt chữ. Tiêu đề trong danh sách tối đa 2 dòng, snippet 1 dòng; màn chi tiết luôn hiện nội dung đầy đủ.

## Kích thước, bo góc, hiệu ứng

Collection `Helpdesk v2 / Dimension` (`VariableCollectionId:49:60`).

- **Khoảng cách** `space/*`: 0, 4, 8, 12, 16, 24, 32, 48, 64. Đệm vùng 24, khoảng giữa các hàng 12.
- **Bo góc:**
  - `radius/none` 0 cho vùng làm việc
  - `radius/badge` 4
  - `radius/control` 6 cho nút và ô nhập
  - `radius/card` 8
  - `radius/dialog` 12
  - `radius/full` cho avatar và chip
- **Control** `size/control/*`:
  - `sm` 32 cho thao tác trong bảng
  - `md` 36 cho thao tác gọn
  - `lg` 44 cho nút chính trên desktop
  - `touch` 48 trên mobile; vùng chạm mobile tối thiểu 44
- **Icon** `size/icon/*`: 16, 20, 24. Icon Lucide outline, nét `stroke/icon` 1,5.
- **Avatar** `size/avatar/*`: 24, 32, 40.
- **Nét** `stroke/*`: viền 1, icon 1,5, focus 2.
- **Dòng ticket mẫu** cao 136 px để đủ chỗ cho tiếng Việt; hàng bảng có thể thấp hơn theo nội dung. Ô composer cao 120 px; frontend cho tăng đến 240 px rồi cuộn.

Effect style:
- `v2 / Elevation / Overlay` gồm hai lớp bóng, `0 1 3` (`shadow/soft`) và `0 12 32` (`shadow/overlay`). Chỉ dùng cho dialog, menu, toast và popover; bề mặt thường không đổ bóng.
- `v2 / Focus ring` gồm khe 2 px màu `bg/surface` rồi viền ngoài 2 px màu `focus/ring`; spread gắn biến `stroke/focus` và `space/4`.
- `v2 / Focus ring / Inset` là viền trong 2 px, dùng cho phần tử nằm sát mép vùng như dòng ticket hay hàng bảng.

Trong Figma, spread chỉ hiện khi frame bật clip content.

## Component

Component v2 nằm trên page `Redesign v2 / Components`, đặt tên `v2 / …`, có variant, auto layout và gắn biến. Đã có:

- `v2 / Icon` — `51:580`; variant `Tên` (39 icon Lucide). Đổi màu bằng cách gắn biến chữ lên lớp `Icon`.
- `v2 / Avatar` — `51:581`; variant `Cỡ` (Sm, Md, Lg); text property `Chữ#51:0`.
- `v2 / Badge` — `51:582`; variant `Tông`; `Nhãn#51:4`, `Chấm#51:12`.
- `v2 / Trạng thái ticket` — `51:630` và `v2 / Trạng thái tài liệu` — `51:631`; variant `Trạng thái`, nhãn và tông gói sẵn theo SRS.
- `v2 / Button` — `51:935`; variant `Kiểu` × `Cỡ` × `Trạng thái` (72 biến thể); `Nhãn#51:20`, `Có icon#51:93`.

- `v2 / Input` — `51:1035`; variant `Loại` × `Trạng thái`; `Nhãn#51:166`, `Giá trị#51:183`, `Trợ giúp#51:200`, `Có trợ giúp#51:217`.
- `v2 / IconButton` — `51:1108`; variant `Kiểu` × `Cỡ` × `Trạng thái`. Đổi icon qua thuộc tính `Tên` của lớp `Icon`; luôn kèm nhãn truy cập và tooltip.
- `v2 / NavItem` — `51:1150`; `Nhãn#51:234`, `Số#51:239`, `Có số#51:244`.
- `v2 / Tab` — `51:1151`; `Nhãn#51:249`. `v2 / Chip` — `51:1152`; `Nhãn#51:253`.

- `v2 / TicketRow` — `51:1381`; `Người gửi#51:257`, `Thời gian#51:262`, `Tiêu đề#51:267`, `Xem trước#51:272`, `Mã#51:277`.
- `v2 / Message` — `51:1382`; variant `Loại` (Khách, Nhân viên, Nội bộ).
- `v2 / ActivityEvent` — `51:1158`.
- `v2 / TicketHeader` — `51:1383`; variant `Trạng thái`, chỉ hiện thao tác Agent được phép; `Mã#51:282`, `Tiêu đề#51:288`.
- `v2 / Composer` — `51:1480`; variant `Loại` × `Trạng thái`.

- `v2 / Banner` — `51:1518`; variant `Tông` (Info, Success, Warning, Danger).
- `v2 / Citation` — `51:1488`.
- `v2 / AIPanel` — `51:1634`; variant `Trạng thái` (Chưa tạo, Đang tạo, Có gợi ý, Thiếu căn cứ, Lỗi, Đã chèn).

- `v2 / Toast` — `51:1728`; variant `Tông` (Thành công, Thông tin, Lỗi); `Có nút đóng#52:7`. Nền `bg/inverse`, chữ/icon `text/inverse`, effect Overlay; rộng mặc định `layout/context` 320, nội dung xuống dòng. Lỗi có "Thử lại", giữ bản nháp và không tự ẩn trước khi người dùng xử lý.
- `v2 / EmptyState` — `51:1729`; variant `Loại` (Hộp thư trống, Không có kết quả); `Có thao tác#52:1` điều khiển nút Xóa bộ lọc ở biến thể không có kết quả. Hộp thư trống không có thao tác giả.
- `v2 / Skeleton` — `51:1730`; variant `Loại` (Dòng ticket, Tin nhắn). Dòng ticket 320 × 149 khớp TicketRow hiện tại; tin nhắn rộng `layout/reading` 760. Các khối dùng `bg/subtle`, bo `radius/badge`; không dùng làm trạng thái lỗi kéo dài.
- `v2 / Dialog` — `51:1731`; variant `Loại` (Xác nhận, Phá hủy); `Có nút đóng#52:4`. Rộng `layout/dialog` 480, bo `radius/dialog`, effect Overlay. Mẫu Xác nhận là đóng ticket RESOLVED bởi Customer/Admin; mẫu Phá hủy là lưu trữ mềm tài liệu, giữ citation lịch sử. Sửa chữ trong instance và nhãn nút qua property của Button lồng.
- `v2 / Tooltip` — `51:1647`; text property `Nội dung#52:0`. Nền `bg/inverse`, chữ `text/inverse`; hiển thị khi hover hoặc focus, không thay nhãn truy cập của nút.

Nhóm phản hồi nằm trên thẻ `51:1635`; mẫu Dark dùng instance trên `52:883`. [Ảnh Light + Dark](../../docs/design/anh/thanh-phan/51-1635.png), [ảnh Dark](../../docs/design/anh/thanh-phan/52-883.png), [kết quả kiểm tra](../../docs/design/kiem-tra/redesign-v2-components-5-audit.json). Khi đưa Dialog vào màn, thêm `overlay/scrim`, giữ focus trong dialog và trả focus về nút mở khi đóng; các hành vi này chưa được mô phỏng ở board component.

Nhóm dữ liệu nằm trên thẻ `52:1339` (Components lượt 6, 01/11/2026):

| Component | ID | Biến thể / thuộc tính |
| --- | --- | --- |
| `v2 / StaffRow` | `52:1564` | Trạng thái Đang hoạt động / Đã vô hiệu hóa; `Họ tên#52:11`, `Email#52:14` |
| `v2 / DocumentRow` | `52:1565` | Trạng thái Đã tải lên / Đang xử lý / Sẵn sàng / Lỗi / Đã công bố / Đã lưu trữ; `Tên tài liệu#52:17`, `Thông tin tệp#52:24` |
| `v2 / Pagination` | `52:1566` | Vị trí Trang đầu / Trang giữa / Trang cuối; sửa phạm vi và số trang trong instance |
| `v2 / LoadMore` | `52:1567` | Trạng thái Còn dữ liệu / Đang tải / Hết danh sách |
| `v2 / UploadZone` | `52:1568` | Trạng thái Chờ / Kéo thả / Đang tải / Lỗi (quá 10 MiB) |
| `v2 / PropertyPair` | `52:1569` | Bố cục Ngang / Dọc; `Nhãn#52:31`, `Giá trị#52:34` |

- Hàng bảng mặc định rộng `layout/screen/tablet` 1024; cột trạng thái/công bố/thao tác dùng `layout/nav` 184 để thẳng cột khi nhãn nút thay đổi. Nội dung dài xuống dòng, hàng tự tăng chiều cao. StaffRow dành cho Admin; thao tác vô hiệu hóa phải mở dialog xác nhận, không cho vô hiệu hóa lại tài khoản đã bị vô hiệu hóa.
- DocumentRow tách trạng thái xử lý và công bố: biến thể Đã công bố vẫn có badge **Sẵn sàng** ở cột xử lý và chữ **Đã công bố** ở cột công bố. Chỉ biến thể Sẵn sàng chưa công bố có nút Công bố. Lỗi dùng Xem lỗi, không mặc định mọi lỗi đều có thể thử lại. Đã lưu trữ ngừng công bố và không dùng cho truy xuất mới.
- Pagination minh họa 20 mục/trang với đầu/giữa/cuối; frontend lấy phạm vi, tổng và trang từ response. LoadMore là lựa chọn cho danh sách ticket, không hiển thị đồng thời với Pagination trên cùng danh sách; trạng thái Đang tải ngăn yêu cầu lặp, Hết danh sách không có nút.
- UploadZone nhận PDF văn bản, TXT, MD, tối đa **10 MiB mỗi tệp**. Có nút chọn tệp bên cạnh kéo thả, nút cao 44 px; trạng thái Đang tải chỉ nói về truyền tệp, chưa phải xử lý hay công bố. Mặc định rộng `layout/form` 640; khi dùng đặt Fill theo vùng chứa. Đã kiểm tra ở 320 px bằng fixture `52:1895`.
- PropertyPair Ngang rộng `layout/reading` 760, nhãn 184; Dọc rộng `layout/context` 320. Cả nhãn lẫn giá trị đều xuống dòng.

[Ảnh dữ liệu Light + Dark](../../docs/design/anh/thanh-phan/52-1339.png), [Dark](../../docs/design/anh/thanh-phan/52-1587.png), [320 px](../../docs/design/anh/thanh-phan/52-1895.png), [audit](../../docs/design/kiem-tra/redesign-v2-components-6-audit.json). Bộ Components theo bước 3 đã hoàn tất; Sidebar, TopNav, Mobile header và Xem nguồn sẽ ghép từ component khi dựng màn. Các component `_doc / …` trên page Foundations chỉ phục vụ bảng trình bày; không dùng chúng trong màn hình.

## Hành vi cần giữ khi triển khai

- Agent nhận OPEN trước khi soạn hoặc gọi AI; Customer chỉ xem own/public. Không dùng INTERNAL làm snippet công khai.
- Tách mở AI và tạo gợi ý. Chèn chỉ sửa PUBLIC draft; có chữ thì xác nhận thay thế; không tự gửi hoặc chuyển trạng thái.
- Ký hiệu nguồn `[n]` chỉ hiển thị trong ngăn AI và lịch sử; khi chèn vào bản nháp phải bỏ ký hiệu, nên tin gửi Customer không chứa `[n]`. Nguồn vẫn được lưu để truy vết.
- Draft theo account/ticket/visibility trong phiên; không tự lưu hỗ trợ nhạy cảm vào localStorage. Gửi lỗi giữ chữ, thành công chỉ xóa draft đã gửi.
- Enter xuống dòng; shortcut gửi, keyboard focus, reduced motion, screen reader và scroll cần kiểm tra trên frontend thật.
- READY khác published; tài liệu archive không dùng cho gợi ý mới nhưng citation lịch sử giữ snapshot.

Xem [bàn giao](../../docs/design/README.md) để biết luồng nào đã nối và giới hạn prototype. Không suy diễn chức năng backend từ ảnh hoặc reaction.

## Màn hình v2 đã bàn giao

Baseline báo cáo hiện hành ngày 12/11/2026: **34 nhóm màn hình chính, 229 frames và 82 flow points**, theo [Report.pdf](../../reports/template1/report/Report.pdf). Report sử dụng 31 ảnh UI; xem [prototype đồng bộ](../../reports/template1/05-prototype-mockup.md). Đoạn dưới ghi lịch sử phiên bản trước, không phải tổng số của bản final.

Ngày 01/11/2026 hoàn tất 33 nhóm màn chính trên 5 page v2, có 5 mẫu Dark; sau rà soát ngày 03/11/2026 có 151 frame. [Bảng ảnh và phạm vi prototype](../../docs/design/man-hinh.md), [manifest](../../docs/design/figma-map.json), [audit cuối](../../docs/design/kiem-tra/redesign-v2-final-audit.json). Bộ biến, styles và cây Components giữ nguyên qua readback trong lượt dựng màn.
