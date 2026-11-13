> Cập nhật 07/11/2026: thương hiệu Clarune; 229 màn hình, 82 điểm bắt đầu trên 5 page giao diện. Các audit ngày 01–03/11 là hồ sơ của phiên bản trước. [Logo và ảnh hiện tại](brand/README.md).

# Bảng màn hình — Redesign v2

Hoàn tất 01/11/2026, rà soát và sửa 03/11/2026: **34 nhóm màn chính, 229 frame**, gồm các trạng thái phụ, overlay và 5 mẫu Dark. File Figma **SE**; chọn flow trên từng page `Redesign v2 / …` để xem prototype.

> Số lượng theo module trong bảng dưới là snapshot ngày 03/11/2026 (33 nhóm, 151 frame), được giữ để đối soát các audit cũ. Tổng hiện hành là 34 nhóm, 229 frames và 82 flow points theo [Report.pdf](../../reports/template1/report/Report.pdf); bảng này chưa phân bổ lại số frame mới theo module.

| Module | Nhóm chính | Tổng frame | Page Figma | Audit |
| --- | ---: | ---: | --- | --- |
| Agent | 10 | 41 | `54:1987` | [Đạt](kiem-tra/redesign-v2-agent-audit.json) |
| Customer | 7 | 29 | `54:1988` | [Đạt](kiem-tra/redesign-v2-customer-audit.json) |
| Identity | 5 | 18 | `54:1989` | [Đạt](kiem-tra/redesign-v2-identity-audit.json) |
| Knowledge Base | 6 | 33 | `54:1990` | [Đạt](kiem-tra/redesign-v2-knowledge-audit.json) |
| Admin | 5 | 30 | `54:1991` | [Đạt](kiem-tra/redesign-v2-admin-audit.json) |

709 reaction Codex ghi và đọc lại, cộng 17 reaction thêm ngày 03/11 (luồng thao tác trạng thái mobile, hai màn kết quả mobile, dòng HD-1052 ở D-Filtered); 82 điểm bắt đầu gồm màn chính, Dark và các trạng thái kiểm tra. [Manifest](figma-map.json) ghi chính xác các link được nối và những link bị bỏ qua; [kiểm tra cuối](kiem-tra/redesign-v2-final-audit.json) có số liệu và phạm vi.

## Luồng để xem

| Module | Chuỗi thao tác đại diện |
| --- | --- |
| Agent | A01 nhận xử lý → A02 → mở AI → tạo → A03 → nguồn 1/2 → xác nhận thay draft → A-Inserted → A-AISent. A07 gửi vẫn Chờ khách; lỗi, mất quyền và Dark có entry riêng. |
| Customer | C01 → tạo C02 → C-Created; C04 → mở lại HD-1037 hoặc xác nhận đóng C05. C06/C07 và nhánh đóng/mở lại có mẫu mobile riêng. |
| Identity | I01 ↔ I02; I03/I04 và I-AdminProfile có lưu hồ sơ/đổi mật khẩu giữ đúng vai trò. Mật khẩu đã đổi được xóa khỏi form. |
| Knowledge Base | K01 → đọc; K04 → K05 → tải lên → xử lý → READY chưa công bố → công bố. Bốn tài liệu có xác nhận lưu trữ và kết quả đúng bản ghi. |
| Admin | D01 → D03 phân công HD-1054 → D-AssignedDetail; D02 → chuyển người phụ trách / ghi chú / AI; D04 → D05 tạo nhân viên hoặc vô hiệu hóa Nguyễn Minh Anh. |

## Giới hạn đã xác nhận

- Prototype native tĩnh; chưa click-test trong Presentation viewer.
- Figma không hỗ trợ NAVIGATE qua page; dùng entry flow riêng.
- Chưa mô phỏng mọi tổ hợp responsive, tìm kiếm, nhập liệu hoặc phân trang. Chỉ các link trong manifest đã được nối.
- State minh họa theo nhánh; không có persistence, backend, upload hay auth thật.
- Keyboard, scroll, screen reader, focus trap và bàn phím ảo cần kiểm tra khi triển khai frontend.

Các mục điều hướng khác page, đăng nhập tới workspace và đăng xuất được thể hiện bằng màn/entry riêng do giới hạn Figma. Những nhánh trạng thái là các ví dụ độc lập; quay về entry có thể khởi tạo lại dữ liệu mẫu. Các thao tác phụ chưa có link trong manifest là phần đặc tả thị giác. Không dùng prototype này làm bằng chứng backend/RBAC đã triển khai.

## Inventory

Các bảng theo module bên dưới giữ nhãn **chính** và ảnh của snapshot ngày 03/11/2026 để đối soát. Danh mục ảnh dùng trong bản final nằm tại [Mục 5 Template 1](../../reports/template1/05-prototype-mockup.md).

### Agent

| Màn | Figma node | Kích thước | Chế độ | Ảnh |
| --- | --- | --- | --- | --- |
| A01 · Hàng đợi · Nhận xử lý · **chính** | `55:1992` | 1440 × 900 | Light | [PNG](anh/55-1992.png) |
| A02 · Xử lý ticket · AI đóng · **chính** | `55:1993` | 1440 × 900 | Light | [PNG](anh/55-1993.png) |
| A03 · Gợi ý AI có nguồn · **chính** | `55:1994` | 1440 × 900 | Light | [PNG](anh/55-1994.png) |
| A04 · Ghi chú nội bộ · **chính** | `55:2537` | 1440 × 900 | Light | [PNG](anh/55-2537.png) |
| A05 · AI đang tạo gợi ý · **chính** | `55:2538` | 1440 × 900 | Light | [PNG](anh/55-2538.png) |
| A-AIError · AI tạm thời không phản hồi | `55:2539` | 1440 × 900 | Light | [PNG](anh/55-2539.png) |
| A-AIInsufficient · AI thiếu căn cứ | `56:3103` | 1440 × 900 | Light | [PNG](anh/56-3103.png) |
| A06 · Xung đột nhận xử lý · **chính** | `56:3104` | 1440 × 900 | Light | [PNG](anh/56-3104.png) |
| A-Lost · Quyền xử lý đã thay đổi | `56:3105` | 1440 × 900 | Light | [PNG](anh/56-3105.png) |
| A07 · Chờ khách phản hồi · **chính** | `56:3576` | 1440 × 900 | Light | [PNG](anh/56-3576.png) |
| A-WaitingSent · Đã trả lời · Vẫn chờ khách | `62:14459` | 1440 × 900 | Light | [PNG](anh/62-14459.png) |
| A-Resolved · Yêu cầu đã giải quyết | `56:3577` | 1440 × 900 | Light | [PNG](anh/56-3577.png) |
| A08 · Đọc nguồn của gợi ý · **chính** | `56:3578` | 1440 × 900 | Light | [PNG](anh/56-3578.png) |
| A09 · Tablet · AI overlay · **chính** | `56:4106` | 1024 × 768 | Light | [PNG](anh/56-4106.png) |
| A10 · Mobile · Hội thoại · **chính** | `56:4107` | 390 × 844 | Light | [PNG](anh/56-4107.png) |
| A-MobileAI · Mobile · Trợ lý AI | `56:4108` | 390 × 844 | Light | [PNG](anh/56-4108.png) |
| A-MobileActions · Mobile · Thao tác yêu cầu (overlay từ nút "…") | `69:11286` | 390 × 844 | Light | [PNG](anh/69-11286.png) |
| A-MobileWaiting · Mobile · Chờ khách phản hồi (từ "Yêu cầu thêm thông tin") | `69:11313` | 390 × 844 | Light | [PNG](anh/69-11313.png) |
| A-MobileResolved · Mobile · Đã giải quyết (từ "Đánh dấu đã giải quyết") | `69:11382` | 390 × 844 | Light | [PNG](anh/69-11382.png) |
| A-AIIdle · Mở trợ lý · Chưa tạo | `56:4440` | 1440 × 900 | Light | [PNG](anh/56-4440.png) |
| A-Inserted · Đã chèn vào bản nháp | `56:4441` | 1440 × 900 | Light | [PNG](anh/56-4441.png) |
| A-Sent · Đã gửi trả lời công khai | `56:4442` | 1440 × 900 | Light | [PNG](anh/56-4442.png) |
| A-SendError · Gửi lỗi · Giữ bản nháp | `56:5006` | 1440 × 900 | Light | [PNG](anh/56-5006.png) |
| A-DraftB · Đổi ticket · Bản nháp riêng | `56:5007` | 1440 × 900 | Light | [PNG](anh/56-5007.png) |
| A-NoteSaved · Đã lưu ghi chú nội bộ | `56:5008` | 1440 × 900 | Light | [PNG](anh/56-5008.png) |
| A-Info · Thông tin yêu cầu | `56:5516` | 1440 × 900 | Light | [PNG](anh/56-5516.png) |
| A-MobileInserted · Mobile · Đã chèn bản nháp | `56:5517` | 390 × 844 | Light | [PNG](anh/56-5517.png) |
| A-MobileReplace · Mobile · Xác nhận thay bản nháp | `56:5518` | 390 × 844 | Light | [PNG](anh/56-5518.png) |
| A-MobileSource · Mobile · Đọc nguồn | `56:5799` | 390 × 844 | Light | [PNG](anh/56-5799.png) |
| A-TabletClosed · Tablet · AI đóng | `56:5800` | 1024 × 768 | Light | [PNG](anh/56-5800.png) |
| A-MobileNote · Mobile · Ghi chú nội bộ | `56:5801` | 390 × 844 | Light | [PNG](anh/56-5801.png) |
| A-MobileSent · Mobile · Đã gửi trả lời | `56:6044` | 390 × 844 | Light | [PNG](anh/56-6044.png) |
| A-AISent · Đã gửi bản nháp từ AI | `56:6045` | 1440 × 900 | Light | [PNG](anh/56-6045.png) |
| A-MobileAISent · Mobile · Đã gửi bản nháp từ AI | `56:6046` | 390 × 844 | Light | [PNG](anh/56-6046.png) |
| A-MobileList · Mobile · Danh sách yêu cầu | `56:6372` | 390 × 844 | Light | [PNG](anh/56-6372.png) |
| A-Replace · Xác nhận thay thế bản nháp | `56:6373` | 1440 × 900 | Light | [PNG](anh/56-6373.png) |
| A-Dark · Gợi ý AI · Dark | `56:6374` | 1440 × 900 | Dark | [PNG](anh/56-6374.png) |
| A-Source2 · Đọc nguồn thứ hai | `62:14671` | 1440 × 900 | Light | [PNG](anh/62-14671.png) |
| A-MobileSource2 · Mobile · Đọc nguồn thứ hai | `62:14672` | 390 × 844 | Light | [PNG](anh/62-14672.png) |
| A-MobileGenerating · Mobile · Đang tạo gợi ý | `62:14875` | 390 × 844 | Light | [PNG](anh/62-14875.png) |
| A-MobileNoteSaved · Mobile · Đã lưu ghi chú | `62:14876` | 390 × 844 | Light | [PNG](anh/62-14876.png) |

### Customer

| Màn | Figma node | Kích thước | Chế độ | Ảnh |
| --- | --- | --- | --- | --- |
| C01 · Yêu cầu của tôi · **chính** | `58:6763` | 1440 × 900 | Light | [PNG](anh/58-6763.png) |
| C02 · Tạo yêu cầu · **chính** | `58:6764` | 1440 × 900 | Light | [PNG](anh/58-6764.png) |
| C03 · Chi tiết · Đang xử lý · **chính** | `58:6765` | 1440 × 900 | Light | [PNG](anh/58-6765.png) |
| C04 · Đã giải quyết · Chờ xác nhận · **chính** | `62:6953` | 1440 × 900 | Light | [PNG](anh/62-6953.png) |
| C05 · Yêu cầu đã đóng · **chính** | `62:6954` | 1440 × 900 | Light | [PNG](anh/62-6954.png) |
| C06 · Mobile · Yêu cầu của tôi · **chính** | `62:6955` | 390 × 844 | Light | [PNG](anh/62-6955.png) |
| C07 · Mobile · Chi tiết yêu cầu · **chính** | `62:7174` | 390 × 844 | Light | [PNG](anh/62-7174.png) |
| C-Empty · Chưa có yêu cầu | `62:7175` | 1440 × 900 | Light | [PNG](anh/62-7175.png) |
| C-FilteredEmpty · Không có yêu cầu cần phản hồi | `62:7176` | 1440 × 900 | Light | [PNG](anh/62-7176.png) |
| C-Filtered · Lọc yêu cầu đã giải quyết | `62:7329` | 1440 × 900 | Light | [PNG](anh/62-7329.png) |
| C-Loading · Đang tải yêu cầu | `62:7330` | 1440 × 900 | Light | [PNG](anh/62-7330.png) |
| C-ListError · Lỗi tải danh sách | `62:7331` | 1440 × 900 | Light | [PNG](anh/62-7331.png) |
| C-Validation · Tạo yêu cầu · Có lỗi nhập liệu | `62:7502` | 1440 × 900 | Light | [PNG](anh/62-7502.png) |
| C-Created · Đã tạo yêu cầu mới | `62:7503` | 1440 × 900 | Light | [PNG](anh/62-7503.png) |
| C-Replied · Đã gửi phản hồi | `62:7504` | 1440 × 900 | Light | [PNG](anh/62-7504.png) |
| C-MobileReplied · Mobile · Đã gửi phản hồi | `62:7710` | 390 × 844 | Light | [PNG](anh/62-7710.png) |
| C-Reopened · Đã yêu cầu xử lý tiếp HD-1037 | `62:7711` | 1440 × 900 | Light | [PNG](anh/62-7711.png) |
| C-ReopenedSent · Đã phản hồi yêu cầu mở lại HD-1037 | `62:8586` | 1440 × 900 | Light | [PNG](anh/62-8586.png) |
| C-CreatedList · Danh sách sau khi tạo yêu cầu | `62:7712` | 1440 × 900 | Light | [PNG](anh/62-7712.png) |
| C-MobileCreate · Mobile · Tạo yêu cầu | `62:7950` | 390 × 844 | Light | [PNG](anh/62-7950.png) |
| C-MobileCreated · Mobile · Đã tạo yêu cầu | `62:7951` | 390 × 844 | Light | [PNG](anh/62-7951.png) |
| C-MobileCreatedList · Mobile · Danh sách sau khi tạo yêu cầu | `62:7952` | 390 × 844 | Light | [PNG](anh/62-7952.png) |
| C-Close · Xác nhận đóng HD-1037 | `62:8114` | 1440 × 900 | Light | [PNG](anh/62-8114.png) |
| C-Dark · Chi tiết yêu cầu · Dark | `62:8115` | 1440 × 900 | Dark | [PNG](anh/62-8115.png) |
| C-MobileResolved · Mobile · Yêu cầu đã giải quyết | `62:14971` | 390 × 844 | Light | [PNG](anh/62-14971.png) |
| C-MobileClosed · Mobile · Yêu cầu đã đóng | `62:14972` | 390 × 844 | Light | [PNG](anh/62-14972.png) |
| C-MobileReopened · Mobile · Tiếp tục xử lý HD-1037 | `62:14973` | 390 × 844 | Light | [PNG](anh/62-14973.png) |
| C-MobileReopenedSent · Mobile · Đã phản hồi HD-1037 | `62:15155` | 390 × 844 | Light | [PNG](anh/62-15155.png) |
| C-MobileClose · Mobile · Xác nhận đóng HD-1037 | `62:15156` | 390 × 844 | Light | [PNG](anh/62-15156.png) |

### Identity

| Màn | Figma node | Kích thước | Chế độ | Ảnh |
| --- | --- | --- | --- | --- |
| I01 · Đăng nhập · **chính** | `62:8214` | 1440 × 900 | Light | [PNG](anh/62-8214.png) |
| I02 · Đăng ký khách hàng · **chính** | `62:8215` | 1440 × 900 | Light | [PNG](anh/62-8215.png) |
| I03 · Hồ sơ khách hàng · **chính** | `62:8216` | 1440 × 900 | Light | [PNG](anh/62-8216.png) |
| I04 · Hồ sơ nhân viên / quản trị viên · **chính** | `62:8328` | 1440 × 900 | Light | [PNG](anh/62-8328.png) |
| I05 · Mobile · Đăng nhập · **chính** | `62:8329` | 390 × 844 | Light | [PNG](anh/62-8329.png) |
| I-LoginError · Sai thông tin đăng nhập | `62:8330` | 1440 × 900 | Light | [PNG](anh/62-8330.png) |
| I-RegisterError · Lỗi đăng ký | `62:8447` | 1440 × 900 | Light | [PNG](anh/62-8447.png) |
| I-MobileRegister · Mobile · Đăng ký | `62:8448` | 390 × 844 | Light | [PNG](anh/62-8448.png) |
| I-ProfileSaved · Đã lưu hồ sơ | `62:8449` | 1440 × 900 | Light | [PNG](anh/62-8449.png) |
| I-CustomerSaved · Đã lưu hồ sơ khách hàng | `62:8680` | 1440 × 900 | Light | [PNG](anh/62-8680.png) |
| I-ProfileError · Lỗi lưu hồ sơ | `62:8681` | 1440 × 900 | Light | [PNG](anh/62-8681.png) |
| I-PasswordError · Sai mật khẩu hiện tại | `62:8682` | 1440 × 900 | Light | [PNG](anh/62-8682.png) |
| I-PasswordSaved · Đã đổi mật khẩu | `62:8878` | 1440 × 900 | Light | [PNG](anh/62-8878.png) |
| I-Dark · Đăng nhập · Dark | `62:8879` | 1440 × 900 | Dark | [PNG](anh/62-8879.png) |
| I-CustomerPasswordSaved · Đã đổi mật khẩu khách hàng | `62:14150` | 1440 × 900 | Light | [PNG](anh/62-14150.png) |
| I-AdminProfile · Hồ sơ quản trị viên | `62:14151` | 1440 × 900 | Light | [PNG](anh/62-14151.png) |
| I-AdminSaved · Đã lưu hồ sơ quản trị viên | `62:14152` | 1440 × 900 | Light | [PNG](anh/62-14152.png) |
| I-AdminPasswordSaved · Đã đổi mật khẩu quản trị viên | `62:14361` | 1440 × 900 | Light | [PNG](anh/62-14361.png) |

### Knowledge Base

| Màn | Figma node | Kích thước | Chế độ | Ảnh |
| --- | --- | --- | --- | --- |
| K01 · Tìm kiếm tri thức · **chính** | `62:9092` | 1440 × 900 | Light | [PNG](anh/62-9092.png) |
| K02 · Không có kết quả tìm kiếm · **chính** | `62:9093` | 1440 × 900 | Light | [PNG](anh/62-9093.png) |
| K03 · Đọc tài liệu đã công bố · **chính** | `62:9094` | 1440 × 900 | Light | [PNG](anh/62-9094.png) |
| K04 · Quản lý tài liệu · **chính** | `62:9240` | 1440 × 900 | Light | [PNG](anh/62-9240.png) |
| K05 · Tải tài liệu · **chính** | `62:9241` | 1440 × 900 | Light | [PNG](anh/62-9241.png) |
| K06 · Chi tiết tài liệu đã công bố · **chính** | `62:9242` | 1440 × 900 | Light | [PNG](anh/62-9242.png) |
| K-SecurityRead · Đọc tài liệu đã công bố | `62:9482` | 1440 × 900 | Light | [PNG](anh/62-9482.png) |
| K-Uploading · Đang tải tệp lên | `62:9483` | 1440 × 900 | Light | [PNG](anh/62-9483.png) |
| K-Uploaded · Tải lên thành công · Chờ xử lý | `62:9484` | 1440 × 900 | Light | [PNG](anh/62-9484.png) |
| K-Processing · Tài liệu đang xử lý | `62:9620` | 1440 × 900 | Light | [PNG](anh/62-9620.png) |
| K-TooLarge · Tệp vượt quá 10 MiB | `62:9621` | 1440 × 900 | Light | [PNG](anh/62-9621.png) |
| K-ScanFailed · PDF bản quét không được hỗ trợ | `62:9622` | 1440 × 900 | Light | [PNG](anh/62-9622.png) |
| K-ProcessError · Lỗi xử lý · Có thể thử lại | `62:9782` | 1440 × 900 | Light | [PNG](anh/62-9782.png) |
| K-ReadyDetail · Sẵn sàng nhưng chưa công bố | `62:9783` | 1440 × 900 | Light | [PNG](anh/62-9783.png) |
| K-PublishedDetail · Đã công bố tài liệu | `62:9784` | 1440 × 900 | Light | [PNG](anh/62-9784.png) |
| K-UploadReady · Tài liệu mới đã xử lý xong | `62:10444` | 1440 × 900 | Light | [PNG](anh/62-10444.png) |
| K-UploadPublished · Tài liệu mới đã công bố | `62:10445` | 1440 × 900 | Light | [PNG](anh/62-10445.png) |
| K-PublishedList · Quản lý tài liệu | `62:10446` | 1440 × 900 | Light | [PNG](anh/62-10446.png) |
| K-UploadedList · Quản lý tài liệu | `62:10887` | 1440 × 900 | Light | [PNG](anh/62-10887.png) |
| K-ArchivedDetail · Tài liệu đã lưu trữ | `62:10888` | 1440 × 900 | Light | [PNG](anh/62-10888.png) |
| K-ArchivedList · Quản lý tài liệu | `62:10889` | 1440 × 900 | Light | [PNG](anh/62-10889.png) |
| K-Archive · Xác nhận lưu trữ tài liệu | `62:11218` | 1440 × 900 | Light | [PNG](anh/62-11218.png) |
| K-Dark · Kho tri thức · Dark | `62:11220` | 1440 × 900 | Dark | [PNG](anh/62-11220.png) |
| K-SecurityDetail · Chi tiết tài liệu bảo vệ tài khoản | `62:11219` | 1440 × 900 | Light | [PNG](anh/62-11219.png) |
| K-ArchiveUnlock · Xác nhận lưu trữ Quy trình mở khóa tài khoản | `62:11346` | 1440 × 900 | Light | [PNG](anh/62-11346.png) |
| K-ArchivedUnlock · Đã lưu trữ Quy trình mở khóa tài khoản | `62:11347` | 1440 × 900 | Light | [PNG](anh/62-11347.png) |
| K-ArchivedListUnlock · Quản lý tài liệu | `62:11348` | 1440 × 900 | Light | [PNG](anh/62-11348.png) |
| K-ArchivePayment · Xác nhận lưu trữ Chính sách thanh toán | `62:11556` | 1440 × 900 | Light | [PNG](anh/62-11556.png) |
| K-ArchivedPayment · Đã lưu trữ Chính sách thanh toán | `62:11557` | 1440 × 900 | Light | [PNG](anh/62-11557.png) |
| K-ArchivedListPayment · Quản lý tài liệu | `62:11558` | 1440 × 900 | Light | [PNG](anh/62-11558.png) |
| K-ArchiveSecurity · Xác nhận lưu trữ Bảo vệ tài khoản khi đăng nhập | `62:11766` | 1440 × 900 | Light | [PNG](anh/62-11766.png) |
| K-ArchivedSecurity · Đã lưu trữ Bảo vệ tài khoản khi đăng nhập | `62:11767` | 1440 × 900 | Light | [PNG](anh/62-11767.png) |
| K-ArchivedListSecurity · Quản lý tài liệu | `62:11768` | 1440 × 900 | Light | [PNG](anh/62-11768.png) |

### Admin

| Màn | Figma node | Kích thước | Chế độ | Ảnh |
| --- | --- | --- | --- | --- |
| D01 · Tất cả yêu cầu · **chính** | `62:9943` | 1440 × 900 | Light | [PNG](anh/62-9943.png) |
| D02 · Xử lý và lịch sử yêu cầu · **chính** | `62:9944` | 1440 × 900 | Light | [PNG](anh/62-9944.png) |
| D03 · Phân công nhân viên · **chính** | `62:9945` | 1440 × 900 | Light | [PNG](anh/62-9945.png) |
| D04 · Quản lý nhân viên · **chính** | `62:10225` | 1440 × 900 | Light | [PNG](anh/62-10225.png) |
| D05 · Tạo nhân viên · **chính** | `62:10226` | 1440 × 900 | Light | [PNG](anh/62-10226.png) |
| D-OpenDetail · Xử lý và lịch sử yêu cầu | `62:10227` | 1440 × 900 | Light | [PNG](anh/62-10227.png) |
| D-AssignedDetail · Xử lý và lịch sử yêu cầu | `62:10691` | 1440 × 900 | Light | [PNG](anh/62-10691.png) |
| D-InvoiceDetail · Xử lý và lịch sử yêu cầu | `62:10692` | 1440 × 900 | Light | [PNG](anh/62-10692.png) |
| D-Reassign · Chuyển người phụ trách | `62:10693` | 1440 × 900 | Light | [PNG](anh/62-10693.png) |
| D-Reassigned · Xử lý và lịch sử yêu cầu | `62:11976` | 1440 × 900 | Light | [PNG](anh/62-11976.png) |
| D-Internal · Xử lý và lịch sử yêu cầu | `62:11977` | 1440 × 900 | Light | [PNG](anh/62-11977.png) |
| D-NoteSaved · Xử lý và lịch sử yêu cầu | `62:11978` | 1440 × 900 | Light | [PNG](anh/62-11978.png) |
| D-Filtered · Tất cả yêu cầu | `62:12398` | 1440 × 900 | Light | [PNG](anh/62-12398.png) |
| D-Empty · Tất cả yêu cầu | `62:12399` | 1440 × 900 | Light | [PNG](anh/62-12399.png) |
| D-Loading · Tất cả yêu cầu | `62:12400` | 1440 × 900 | Light | [PNG](anh/62-12400.png) |
| D-ListError · Tất cả yêu cầu | `62:12690` | 1440 × 900 | Light | [PNG](anh/62-12690.png) |
| D-StaffActive · Quản lý nhân viên | `62:12691` | 1440 × 900 | Light | [PNG](anh/62-12691.png) |
| D-StaffInactive · Quản lý nhân viên | `62:12692` | 1440 × 900 | Light | [PNG](anh/62-12692.png) |
| D-StaffEmpty · Quản lý nhân viên | `62:12932` | 1440 × 900 | Light | [PNG](anh/62-12932.png) |
| D-StaffCreated · Quản lý nhân viên | `62:12933` | 1440 × 900 | Light | [PNG](anh/62-12933.png) |
| D-StaffDisabled · Quản lý nhân viên | `62:12934` | 1440 × 900 | Light | [PNG](anh/62-12934.png) |
| D-StaffEnabled · Quản lý nhân viên | `62:13236` | 1440 × 900 | Light | [PNG](anh/62-13236.png) |
| D-CreateError · Email nhân viên đã tồn tại | `62:13237` | 1440 × 900 | Light | [PNG](anh/62-13237.png) |
| D-Disable · Xác nhận vô hiệu hóa nhân viên | `62:13238` | 1440 × 900 | Light | [PNG](anh/62-13238.png) |
| D-Dark · Tất cả yêu cầu | `62:13392` | 1440 × 900 | Dark | [PNG](anh/62-13392.png) |
| D-PublicSent · Xử lý và lịch sử yêu cầu | `62:13390` | 1440 × 900 | Light | [PNG](anh/62-13390.png) |
| D-AI · Xử lý và lịch sử yêu cầu | `62:13391` | 1440 × 900 | Light | [PNG](anh/62-13391.png) |
| D-AIInserted · Xử lý và lịch sử yêu cầu | `62:13844` | 1440 × 900 | Light | [PNG](anh/62-13844.png) |
| D-AISent · Xử lý và lịch sử yêu cầu | `62:13845` | 1440 × 900 | Light | [PNG](anh/62-13845.png) |
| D-AIReplace · Thay bản nháp từ gợi ý AI | `62:13846` | 1440 × 900 | Light | [PNG](anh/62-13846.png) |

## Prototype bổ sung ngày 07/11/2026

| Màn | Node | Ảnh |
| --- | --- | --- |
| A11 · UC-18 · Lịch sử gợi ý AI | `81:7585` | [Xem](anh/81-7585.png) |
| A-HistoryLoading · UC-18 · Đang tải | `81:7878` | [Xem](anh/81-7878.png) |
| A-HistoryEmpty · UC-18 · Chưa có lịch sử | `81:8153` | [Xem](anh/81-8153.png) |
| A-HistoryError · UC-18 · Lỗi tải lịch sử | `81:8428` | [Xem](anh/81-8428.png) |
| A12 · UC-18/19 · Gợi ý đã sử dụng | `81:8707` | [Xem](anh/81-8707.png) |
| A-HistoryFailed · UC-18 · Lần tạo thất bại | `81:9018` | [Xem](anh/81-9018.png) |
| A-HistoryInsufficient · UC-18 · Lần tạo thiếu căn cứ | `81:9294` | [Xem](anh/81-9294.png) |
| A-HistoryDiscarded · UC-18 · Gợi ý đã bỏ | `81:9570` | [Xem](anh/81-9570.png) |
| A-HistorySource1 · UC-18 · Snapshot nguồn | `82:9864` | [Xem](anh/82-9864.png) |
| A-HistorySource2 · UC-18 · Snapshot nguồn | `82:10141` | [Xem](anh/82-10141.png) |
| A-FeedbackError · UC-19 P1 · Lỗi lưu đánh giá | `82:10422` | [Xem](anh/82-10422.png) |
| A-MobileHistory · UC-18 · Lịch sử gợi ý | `82:12970` | [Xem](anh/82-12970.png) |
| A-MobileHistoryDetail · UC-18 · APPLIED | `82:13099` | [Xem](anh/82-13099.png) |
| A-MobileHistoryDetail · UC-18 · FAILED | `82:13245` | [Xem](anh/82-13245.png) |
| A-MobileHistoryDetail · UC-18 · INSUFFICIENT_EVIDENCE | `82:13356` | [Xem](anh/82-13356.png) |
| A-MobileHistoryDetail · UC-18 · DISCARDED | `82:13467` | [Xem](anh/82-13467.png) |
| A-MobileHistorySource1 · UC-18 · Snapshot | `82:13593` | [Xem](anh/82-13593.png) |
| A-MobileHistorySource2 · UC-18 · Snapshot | `82:13705` | [Xem](anh/82-13705.png) |
| A-TabletHistory · UC-18 · Lịch sử gợi ý | `82:13948` | [Xem](anh/82-13948.png) |
| A-TabletHistoryDetail · UC-18 · APPLIED | `82:14233` | [Xem](anh/82-14233.png) |
| A-TabletHistoryDetail · UC-18 · FAILED | `82:14535` | [Xem](anh/82-14535.png) |
| A-TabletHistoryDetail · UC-18 · INSUFFICIENT_EVIDENCE | `82:14802` | [Xem](anh/82-14802.png) |
| A-TabletHistoryDetail · UC-18 · DISCARDED | `82:15069` | [Xem](anh/82-15069.png) |
| A-TabletHistorySource1 · UC-18 · Snapshot | `82:15351` | [Xem](anh/82-15351.png) |
| A-TabletHistorySource2 · UC-18 · Snapshot | `82:15619` | [Xem](anh/82-15619.png) |
| A-DarkHistory · UC-18 · Lịch sử gợi ý | `82:15952` | [Xem](anh/82-15952.png) |
| A-DarkHistoryDetail · UC-18 · APPLIED | `82:16247` | [Xem](anh/82-16247.png) |
| A-DarkHistoryDetail · UC-18 · FAILED | `82:16559` | [Xem](anh/82-16559.png) |
| A-DarkHistoryDetail · UC-18 · INSUFFICIENT_EVIDENCE | `82:16836` | [Xem](anh/82-16836.png) |
| A-DarkHistoryDetail · UC-18 · DISCARDED | `82:17113` | [Xem](anh/82-17113.png) |
| A-DarkHistorySource1 · UC-18 · Snapshot | `82:17405` | [Xem](anh/82-17405.png) |
| A-DarkHistorySource2 · UC-18 · Snapshot | `82:17683` | [Xem](anh/82-17683.png) |
| A-HistoryLost · UC-18/19 · Quyền truy cập đã thay đổi | `82:17965` | [Xem](anh/82-17965.png) |
| A-HistorySourceError · UC-18 · Lỗi tải snapshot | `82:18066` | [Xem](anh/82-18066.png) |
| A-DiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:14771` | [Xem](anh/91-14771.png) |
| A-Discarded · UC-15 · Gợi ý đã bỏ | `91:15058` | [Xem](anh/91-15058.png) |
| A-HistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:15346` | [Xem](anh/91-15346.png) |
| A-InsertedDiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:15641` | [Xem](anh/91-15641.png) |
| A-InsertedDiscarded · UC-15 · Gợi ý đã bỏ | `91:15904` | [Xem](anh/91-15904.png) |
| A-InsertedHistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:16177` | [Xem](anh/91-16177.png) |
| A-MobileDiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:16472` | [Xem](anh/91-16472.png) |
| A-MobileDiscarded · UC-15 · Gợi ý đã bỏ | `91:16589` | [Xem](anh/91-16589.png) |
| A-MobileHistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:16712` | [Xem](anh/91-16712.png) |
| A-TabletDiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:16842` | [Xem](anh/91-16842.png) |
| A-TabletDiscarded · UC-15 · Gợi ý đã bỏ | `91:17118` | [Xem](anh/91-17118.png) |
| A-TabletHistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:17397` | [Xem](anh/91-17397.png) |
| A-DarkDiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:17683` | [Xem](anh/91-17683.png) |
| A-DarkDiscarded · UC-15 · Gợi ý đã bỏ | `91:17969` | [Xem](anh/91-17969.png) |
| A-DarkHistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:18258` | [Xem](anh/91-18258.png) |
| A-ManualAfterDiscard · UC-15 · Tiếp tục soạn thủ công | `91:19215` | [Xem](anh/91-19215.png) |
| A-ManualSentAfterDiscard · UC-08 · Đã gửi thủ công | `91:19477` | [Xem](anh/91-19477.png) |
| A-DiscardError · UC-15 · Lỗi bỏ gợi ý | `91:19649` | [Xem](anh/91-19649.png) |
| D-AIHistory · UC-18 · Lịch sử gợi ý | `82:10789` | [Xem](anh/82-10789.png) |
| D-AIHistoryEmpty · UC-18 · Chưa có lịch sử | `82:11013` | [Xem](anh/82-11013.png) |
| D-AIHistoryError · UC-18 · Lỗi tải | `82:11219` | [Xem](anh/82-11219.png) |
| D-AIHistoryDetail · UC-18 · APPLIED | `82:11429` | [Xem](anh/82-11429.png) |
| D-AIHistoryDetail · UC-18 · FAILED | `82:11646` | [Xem](anh/82-11646.png) |
| D-AIHistoryDetail · UC-18 · INSUFFICIENT_EVIDENCE | `82:11852` | [Xem](anh/82-11852.png) |
| D-AIHistoryDetail · UC-18 · DISCARDED | `82:12058` | [Xem](anh/82-12058.png) |
| D-AIHistorySource1 · UC-18 · Snapshot | `82:12281` | [Xem](anh/82-12281.png) |
| D-AIHistorySource2 · UC-18 · Snapshot | `82:12489` | [Xem](anh/82-12489.png) |
| D-AIGenerating · UC-14 · Đang tạo lại | `82:12703` | [Xem](anh/82-12703.png) |
| D-AIDiscardConfirm · UC-15 · Xác nhận bỏ gợi ý | `91:18554` | [Xem](anh/91-18554.png) |
| D-AIDiscarded · UC-15 · Gợi ý đã bỏ | `91:18770` | [Xem](anh/91-18770.png) |
| D-AIHistoryAfterDiscard · UC-18 · Lịch sử sau khi bỏ | `91:18989` | [Xem](anh/91-18989.png) |
| D06 · UC-17 · Thống kê ticket | `91:19910` | [Xem](anh/91-19910.png) |
| D-AnalyticsLoading · UC-17 · Đang tải | `91:20120` | [Xem](anh/91-20120.png) |
| D-AnalyticsEmpty · UC-17 · Chưa có dữ liệu | `91:20309` | [Xem](anh/91-20309.png) |
| D-AnalyticsError · UC-17 · Lỗi tải | `91:20498` | [Xem](anh/91-20498.png) |
| D-AnalyticsForbidden · UC-17 · Không có quyền | `91:20659` | [Xem](anh/91-20659.png) |
| D-MobileAnalytics · UC-17 · Thống kê ticket | `91:20820` | [Xem](anh/91-20820.png) |
| D-TabletAnalytics · UC-17 · Thống kê ticket | `91:20884` | [Xem](anh/91-20884.png) |
| D-DarkAnalytics · UC-17 · Thống kê ticket | `91:21094` | [Xem](anh/91-21094.png) |
| D-AnalyticsEntry · UC-17 · Lối mở thống kê | `91:21306` | [Xem](anh/91-21306.png) |
| D-AnalyticsLogin · UC-17 · Đăng nhập lại | `91:21450` | [Xem](anh/91-21450.png) |
| D-MobileAnalyticsLoading · UC-17 · Đang tải | `91:21488` | [Xem](anh/91-21488.png) |
| D-TabletAnalyticsLoading · UC-17 · Đang tải | `91:21533` | [Xem](anh/91-21533.png) |
| D-DarkAnalyticsLoading · UC-17 · Đang tải | `91:21724` | [Xem](anh/91-21724.png) |
