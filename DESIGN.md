# Helpdesk — hướng dẫn thiết kế

Tài liệu đầu vào cho người và AI khi làm giao diện dự án. Đọc file này trước khi đề xuất hoặc sửa UI.

- **Figma Design chính thức:** [SE – Figma (Node 49:58)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)
- **Tài liệu làm việc nhóm (Google Docs):** [[SE - Nhóm 4] template1](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0)
- **Báo cáo Mục 5 Template 1:** [05-prototype-mockup.md](reports/template1/05-prototype-mockup.md)
- **Bối cảnh sản phẩm:** [PRODUCT.md](PRODUCT.md) (chuỗi bán lẻ điện máy, người dùng, nguyên tắc).

## Hai phiên bản thiết kế

| Phiên bản | Page Figma | Trạng thái | Dùng cho |
| --- | --- | --- | --- |
| **v3 "Phiếu bảo hành"** | `Redesign v3 / …` | Đang làm (từ 16/11/2026): A03 (Light/Dark), A03 ghi chú nội bộ, A03-Đóng dấu (Motion), Agent bổ sung 17–19/11/2026, mọi màn đều có Light/Dark: A05, A-AIError, A-SendError, A06, A07, A09 (tablet), A10 (mobile), A12 (panel AI mobile dạng bảng trượt), A13 (lịch sử gợi ý trên mobile), A-DiscardConfirm và A-DiscardError bản mobile, A11 (lịch sử gợi ý AI) cùng biến thể rỗng, đang tải, lỗi tải, lỗi bản chụp nguồn và quyền đã đổi, A-DiscardConfirm, A-DiscardError, A-ManualAfterDiscard (UC-15, khối xác nhận nằm trong panel AI); Admin bổ sung: D03-Cấm (không có quyền xem thống kê, nhìn từ tài khoản nhân viên nên rail không có Nhân viên và Thống kê), D03 mobile và D03 tablet (1024×768, rail icon), D-AIHistory (UC-18, kèm rỗng, đang tải, lỗi tải) và D-Detail (chi tiết phiếu có khối "Lịch sử yêu cầu"), C01 (Light/Dark), C03, C06 và C07 (mobile), K01, K04 (Light/Dark, xác nhận lưu trữ), K05 (Light/Dark, tải lên, đã chọn tệp, lỗi vượt 10 MiB, lỗi sai định dạng), K06 (Light/Dark, chi tiết tài liệu đã công bố kèm danh sách đoạn có số trang, xác nhận lưu trữ, Đang xử lý, Thất bại), I01, I02, I01–I02 (Light/Dark, xấp phiếu ba liên), I01-Lỗi, I02-Lỗi, I03 (Light/Dark, thẻ khách hàng), I04 (Light/Dark, thẻ quản trị viên, quyền của vai trò), I04-Lỗi, I04-Thành công, D01, D02 (kèm hộp thoại thêm, lỗi email, vô hiệu hóa), D03 (Đang tải, Rỗng, Lỗi) | Thiết kế mới, frontend sau này |
| v2 "Bàn làm việc yên tĩnh" | `Redesign v2 / …` | Đã bàn giao, không sửa | Báo cáo Template 1 đã nộp |

Màn chưa có bản v3 thì tham khảo luồng ở v2, nhưng dựng lại bằng token và component v3.

## Thứ tự áp dụng

1. [SRS](reports/SRS-master.md): quyền, nghiệp vụ và trạng thái ticket.
2. [Đặc tả Inbox](docs/design/dac-ta-inbox.md): luồng, bố cục, responsive và hành vi AI.
3. Thiết kế v3: token `Clarune v3 / …`, component `v3 / …` trên page `Redesign v3 / Components` và mục "Ngôn ngữ thị giác v3" dưới đây.
4. [Bộ thiết kế v2](docs/design/README.md) và [MASTER v2](design-system/helpdesk-workspace/MASTER.md): tham khảo luồng và trạng thái; không lấy token thị giác từ đây cho màn mới.

Từ 16/11/2026, token thị giác lấy theo v3, thay cho MASTER v2. Luồng, bố cục, responsive và hành vi AI vẫn theo đặc tả Inbox.

Không tự thay thiết kế đã được duyệt bằng mẫu tham khảo bên ngoài. Khi các tài liệu dự án mâu thuẫn, nêu rõ mâu thuẫn trước khi thay đổi quy tắc liên quan.

## Ngôn ngữ thị giác v3: "Phiếu bảo hành liên giấy than"

Mỗi yêu cầu là một **phiếu tiếp nhận bảo hành**: có cuống ghi số phiếu, ô thông tin có nhãn, trạng thái là dấu mộc. Không dùng kiểu helpdesk trắng-xám chỉ một màu nhấn.

- **Rail và thanh trên** tô kín xanh mực giấy than `nav/bg` (#1D3FA8).
- **Cuống phiếu:** nền `carbon/subtle`, ngăn với phần thân bằng đường xé nét đứt 2px. Hai đầu đường xé có vết khuyết bán nguyệt. Số phiếu dùng chữ condensed đậm, màu xanh mực.
- **Dấu mộc trạng thái:** viền 2px, chữ in hoa condensed. Trong cuống phiếu chi tiết, dấu nghiêng −4° và đóng chồng lên góc phải vùng thông tin. Trong danh sách, dấu thẳng.
- **Liên hồng (ghi chú nội bộ):** nền `internal/bg` (#FCE9EC), nhãn "LIÊN LƯU · GHI CHÚ NỘI BỘ". Khi soạn ghi chú, khung soạn chuyển sang nền hồng và hiện dòng "khách không thấy".
- **Nền màn:** trắng xanh lạnh `bg/canvas` (#F5F7FC). Không dùng texture giấy, không tô kem cho nền màn.
- **Mặt giấy tờ (18/11/2026):** tờ phiếu, tờ hồ sơ, sổ, giấy note và hộp thoại dạng phiếu dùng `bg/paper` (riêng module Kho chính sách từ 19/11/2026 dùng thân trắng + điểm nhấn kraft, xem "Palette mở rộng") (Light #FFF9EC, Dark #1C1E28) để nổi lên trên nền lạnh như giấy đặt trên bàn. Ô nhập, khung soạn tin, cột panel, thẻ nhân viên (thẻ nhựa) và nút giữ `bg/surface`. Component `v3 / Cuống phiếu` và biến thể Mặc định của `v3 / Thẻ phiếu` đã gắn `bg/paper`.
- **Chữ:** Encode Sans cho nội dung, Encode Sans Condensed cho nhãn ô (in hoa), số phiếu và dấu mộc. Số liệu dùng chữ số đều cột (tabular).
- **Icon:** bộ `v2 / Icon` (nét Lucide 1.5px), đổi màu nét sang token v3 trên từng instance. Icon thiếu thì thêm component `v3 / Icon / …` cùng nét (hiện có `chart-column` cho Thống kê).

### Màu trạng thái và cách gọi

| Trạng thái SRS | Màu dấu | Nhân viên thấy | Khách thấy |
| --- | --- | --- | --- |
| Mới tạo | `carbon/default` (xanh mực) | MỚI | Đã tiếp nhận (bước 1 tiến trình) |
| Đang xử lý | `stamp/default` (#C8102E, đỏ) | ĐANG XỬ LÝ | ĐANG XỬ LÝ |
| Chờ khách phản hồi | `status/warning/fg` (nâu vàng) | CHỜ KHÁCH | CẦN BẠN TRẢ LỜI |
| Đã giải quyết | `status/success/fg` (xanh lá) | ĐÃ GIẢI QUYẾT | ĐÃ GIẢI QUYẾT |
| Đã đóng | `status/neutral/fg` (xám) | ĐÃ ĐÓNG | ĐÃ ĐÓNG |

- Màu đỏ `stamp/default` chỉ dùng cho trạng thái "Đang xử lý" và cảnh báo quá hạn (ví dụ "Quá 2 giờ").
- Màu đỏ không dùng để đánh dấu phiếu đang chọn. Phiếu đang chọn dùng nền `carbon/subtle` và viền xanh mực.
- Màu xanh lá dùng cho dấu "Đã giải quyết" và các bước đã xong trên tiến trình của khách.
- Tài liệu kho chính sách (FR-KB-05/06/08):
  - Trạng thái xử lý ghi bằng chữ có màu, không dùng dấu: Sẵn sàng (xanh lá), Đang xử lý (xanh mực, kèm "Lần thử n/3"), Thất bại (đỏ, kèm lý do).
  - Tình trạng công bố dùng dấu mộc: biến thể `Tài liệu đã công bố` (xanh lá) và `Tài liệu đã lưu trữ` (xám) của `v3 / Dấu mộc`, tách khỏi biến thể trạng thái ticket. "Chưa công bố" ghi bằng chữ thường.
  - Dung lượng ghi bằng MB ở mọi chỗ, kể cả giới hạn "Tối đa 10 MB". SRS quy định 10 MiB (≈10,5 MB), nên con số hiển thị không bao giờ hứa nhận tệp mà hệ thống sẽ từ chối.
  - Nút phân trang không dùng được (ví dụ "Trang trước" ở trang đầu) dùng biến thể Disabled.
  - Đăng nhập, đăng ký (I01–I02): nền `nav/bg` kín màn, số phiếu "HD-0001" cỡ `v3 / Display/Hero` (220px, màu `nav/item-active`) tràn mép trên làm nền trang trí. Giữa là một tờ phiếu 960×600. Cuống trái 400px nền `nav/item-active`, mọi chữ dùng `nav/fg` (`nav/fg-muted` trên nền này chỉ đạt 4,3:1). Một dấu ĐANG XỬ LÝ cỡ chữ 36px nghiêng −6° đóng chồng lên góc trên phải của phiếu. Đường xé dọc có vết khuyết màu `nav/bg`.
  - I01 (mẫu chuẩn, 16/11–17/11/2026): số "HD-0001" dạng chữ viền rỗng (viền `nav/fg-muted`). Sau tờ phiếu là liên hồng (`internal/bg`, nhãn "LIÊN 2 · LƯU NỘI BỘ") và liên vàng (`status/warning/bg`, nhãn "LIÊN 3 · KHÁCH GIỮ") nghiêng lệch. Phiếu và hai liên dùng effect style `v3 / Bóng giấy` (gắn `overlay/scrim` và `shadow/soft`). Cuống có tiến trình ba bước (chấm trắng / `stamp/default` / `status/success/fg` kèm nhãn chữ) và mã vạch trang trí. Phần form có dòng đầu phiếu "PHIẾU ĐĂNG NHẬP · LIÊN 1" kẻ dưới.
  - `v3 / Display/Hero` và biến `font/size/hero` chỉ dùng cho số trang trí, không dùng cho nội dung cần đọc. Form ở phần còn lại của phiếu, nút Primary rộng hết form. Chỉ dùng dữ liệu mẫu ("Khách hàng mẫu", khachhang.mau@vidu.vn).
  - Dải đầu trang của portal khách: bên trái là tiêu đề, bên phải là "PHIẾU ĐANG MỞ" với các cuống phiếu nhỏ (số phiếu, sản phẩm, đường xé, dấu trạng thái) và liên kết "Xem tất cả". Mép dưới là hàng lỗ đục (chấm `bg/canvas` 10px, cách 36px) như mép tập giấy xé. Không để dải cao mà trống.
  - C01/C06 (18/11/2026): trên lời chào là dòng đầu phiếu "SỔ BẢO HÀNH CỦA BẠN · KHÁCH HÀNG TỪ dd/mm/yyyy" (`v3 / Label/Ô`, `nav/fg`; mobile bỏ ngày). Dòng tóm tắt thay bằng hai chip kiểu dấu (`v3 / Stamp`, viền 2px, bo `radius/stamp`): "n YÊU CẦU CẦN BẠN TRẢ LỜI" tô `status/warning/bg`, viền và chữ `status/warning/fg`; "n YÊU CẦU ĐANG XỬ LÝ" chỉ viền và chữ `nav/fg`; mobile cho chip xuống dòng. Desktop thay nút "Tạo yêu cầu mới" bằng "xấp phiếu trống": tờ trên `bg/paper` nghiêng −1°, `v3 / Bóng giấy`, nhãn "PHIẾU TRỐNG · LIÊN 1" và "+ Tạo yêu cầu mới" (`v3 / Heading/H2`, `carbon/default`), hai tờ lót lệch phía sau. Mobile giữ nút rộng hết màn. Hàng lỗ đục luôn đặt ở mép dưới dải.
  - Hàng lỗ đục dùng effect style `v3 / Lỗ đục` (bóng tối vào trong ở mép trên, viền sáng `nav/item-active` ở mép dưới), lỗ 14px. Ở thanh trên của C03/C07, lỗ nằm vắt qua mép dưới thành các khuyết bán nguyệt.
  - C01: phiếu cần khách trả lời được nâng lên (bóng giấy, nghiêng 0,6°), các phiếu khác giữ phẳng. Cột phải gồm tờ "Khi gửi yêu cầu bảo hành, nên có sẵn" dán băng dính và thẻ "CÁCH ĐỌC DẤU TRÊN PHIẾU" giải thích bốn dấu khách thấy.
  - C03/C07: phiếu khách xem được lót liên vàng "LIÊN 3 · KHÁCH GIỮ"; cột phụ C03 có mã vạch số phiếu ở chân thẻ thông tin.
  - **Hội thoại (C03, C07, A03, 18/11/2026):** bong bóng chat quen thuộc, không dùng bảng hay lề sổ. Tin của người đang xem canh phải, tin của bên kia canh trái; bên đối diện chừa khoảng trống (240px ở C03, 96px ở A03, 48px mobile). Bong bóng bo `radius/card`, góc phía người gửi bo `radius/stamp`, padding 10/14/12/14. Dòng đầu bong bóng ghi người viết và giờ bằng `v3 / Label/Ô` (ví dụ "BẠN · 09:42", "TRẦN QUỐC BẢO · NHÂN VIÊN HỖ TRỢ · 09:50"); nội dung `v3 / Body/Md`. Tin của khách luôn nền `teal/bg` (dòng đầu `teal/fg`): ở màn khách là tin của mình, không viền; ở màn nhân viên và admin có viền `teal/border`. Tin của nhân viên: ở màn khách nền `bg/surface` viền `border/default`; ở màn nhân viên (tin của chính mình, canh phải) nền `carbon/subtle`, không viền. Ghi chú nội bộ (chỉ nhân viên thấy) là bong bóng nền `internal/bg`, viền `internal/border`, dòng đầu "GHI CHÚ NỘI BỘ · tên". Đổi trạng thái là dòng giữa: dấu mộc nghiêng 3° và câu ngắn kèm giờ `text/secondary`. Vạch ngày ở giữa có vạch hai bên.
  - **Khung soạn:** nền `bg/paper`; nhãn "TRẢ LỜI NHÂN VIÊN HỖ TRỢ" (khách, `v3 / Label/Ô` `carbon/default`) hoặc tab Trả lời khách / Ghi chú nội bộ (nhân viên); ô nhập `bg/surface`; chân khung có đường xé nét đứt `border/strong` (ghi chú nội bộ dùng `internal/border`) và một dòng chú thích bên trái.
  - A03 (cả A03-Internal, A03 Dark): phiếu đang xử lý nổi trên liên hồng "LIÊN 2 · LƯU NỘI BỘ" (nhân viên làm việc trên liên lưu); hội thoại theo mẫu bong bóng ở trên; gợi ý AI có kẹp giấy (bản nháp đính kèm, chưa gửi); thẻ đơn hàng có mã vạch "HĐ 7781203". Hàng đợi giữ phẳng.
  - Vùng trống ở cột phụ chỉ được lấp bằng nội dung có ích, ví dụ "GHI CHÚ BẢO MẬT" dạng giấy note vàng (`status/warning/bg`, băng dính `border/default`), nghiêng nhẹ, có bóng giấy.
  - I03 (mẫu chuẩn hồ sơ): thẻ khách hàng tách khỏi luồng, nghiêng 2°, đè lên mép dải xanh đầu trang, có `v3 / Bóng giấy`, lỗ bấm ở góc và mã vạch màu `carbon/default` (không lặp số yêu cầu vì đã có ở dải đầu trang). Tờ hồ sơ có đầu phiếu "HỒ SƠ KHÁCH HÀNG · LIÊN 1", số mục 01/02 kiểu biểu mẫu, bóng giấy và liên hồng "LIÊN 2 · LƯU HỒ SƠ" lót sau, lệch −1,2°.
  - Hồ sơ (I03–I04): bên trái là "thẻ tài khoản" theo kiểu cuống phiếu (nhãn THẺ KHÁCH HÀNG / THẺ QUẢN TRỊ VIÊN, tên chữ condensed lớn, đường xé nét đứt có vết khuyết, ô Vai trò và Tham gia; khách có thêm số yêu cầu). Bên phải là một "tờ hồ sơ" chia hai phần Thông tin cá nhân và Mật khẩu bằng đường xé, mỗi phần một nút Primary căn phải.
  - K04 (18/11/2026) là "sổ đăng ký tài liệu": cột SỐ 01–07 ở lề trái (`v3 / Label/Số`, `text/secondary`); định dạng tệp in thành nhãn viền (PDF/MD, `v3 / Label/Ô`, viền `border/strong`) trước dung lượng và số đoạn. Tài liệu đang chờ quản trị viên công bố nằm phẳng như mọi dòng (không nâng, không nghiêng, không bóng: một dòng nổi giữa sổ sẽ chia sổ thành hai khúc) và có cờ "CHỜ CÔNG BỐ" (`status/warning/bg`, viền và chữ `status/warning/fg`) dán ở mép trên dòng.
  - **Kiểu sổ (D01, K04):** bảng nền `bg/paper`, dải đầu sổ cao 40px (trái: "SỔ TIẾP NHẬN · CHUỖI CLARUNE" / "SỔ TÀI LIỆU · KHO CHÍNH SÁCH" màu `carbon/default`; phải: số trang hoặc số tài liệu và ngày, `text/secondary`; cả hai `v3 / Label/Ô`). Lề đỏ đôi (hai nét 1px `internal/border`, cách 3px) chạy dọc ngay sau cột số, từ hàng tiêu đề cột tới trên hàng phân trang. Các dòng vẫn phẳng.
  - K01: cụm khớp với câu tìm trong đoạn trích in đậm màu `text/primary` (không dùng `carbon/default` vì dễ nhầm với link). Cột phụ là "Tài liệu đang áp dụng" (tài liệu đã công bố, phạm vi tìm kiếm theo FR-KB-07) và giấy note "Lưu ý phiên bản". Không hiện danh sách "hay được tra cứu" vì SRS không có thống kê tra cứu.
  - K05: thẻ biểu mẫu là "PHIẾU NHẬN TÀI LIỆU · LIÊN 1" có `v3 / Bóng giấy`, lót liên hồng "LIÊN 2 · LƯU NỘI BỘ" (tài liệu kho là tài liệu nội bộ). Tệp đã chọn có góc gấp ở góc trên phải. Cột "Sau khi tải lên" dùng vòng số 24px nối bằng nét đứt.
  - K06 (19/11/2026): danh sách đoạn xếp một cột, mỗi đoạn là một tấm phiếu thư mục trắng (`bg/surface`, viền `border/default`, đổ bóng nhẹ) đặt trên một tờ lót `kraft/bg` viền `kraft/border` lệch 6px xuống dưới và sang phải. Cuống trái rộng 104px nền `kraft/bg`, ghi "ĐOẠN" (`v3 / Label/Ô`) và số đoạn cỡ `v3 / Display/Số phiếu`, cả hai màu `kraft/fg`; ngăn với thân bằng đường đục lỗ dọc nét đứt `kraft/border` có hai khuyết tròn ở mép trên và mép dưới. Số trang là nhãn viền `ai/fg` để thẳng ở cuối thân phiếu (trích dẫn của AI theo trang); không nghiêng vì dấu nghiêng trong hệ thống là trạng thái. Khi tài liệu đang xử lý hoặc thất bại, hiện "TIẾN TRÌNH XỬ LÝ": bước xong tô kín `carbon/default`, bước đang xử lý nền `ai/bg` viền và chữ `ai/fg`, bước thất bại viền và chữ `stamp/default`, bước chưa tới viền `border/strong`.
  - D01: cột SỐ PHIẾU in số phiếu bằng `v3 / Label/Số` màu `carbon/default` ở lề trái, cột kế tiếp là "Khách hàng · Sản phẩm". Cụm "Quá 2 giờ" màu `stamp/default`; phiếu quá 2 giờ chưa phân công có cờ "QUÁ 2 GIỜ · CHƯA PHÂN CÔNG" cùng kiểu cờ "CHỜ CÔNG BỐ" ở K04.
  - D02 (18/11/2026): tủ thẻ nhân viên. Tên một dòng bằng `v3 / Display/Tên thẻ` (24/32, căn trên). Dưới đường xé: "PHIẾU ĐANG MỞ" in số cỡ `v3 / Display/Số phiếu` và "NGÀY TẠO". Thanh tải dùng thang cố định 20 phiếu, có vạch 2px `text/primary` ở mức trung bình nhóm; chân trang chú thích "Vạch đen trên thanh: trung bình n phiếu/người". Không tô màu cảnh báo vì SRS không có ngưỡng quá tải. Trạng thái tài khoản là dấu mộc ở chân thẻ (xem quy tắc trạng thái tài khoản), hành động là nút Ghost: "Vô hiệu hóa" chữ `text/secondary`, "Kích hoạt lại" chữ `carbon/default`. Tài khoản đã vô hiệu hóa: thẻ nền `bg/subtle`, số 0 màu `text/disabled`. Chân trang ghi tổng phiếu đang mở đã giao và số phiếu chưa phân công.
  - D03: hai bảng nằm trên một tờ "BẢNG THỐNG KÊ PHIẾU · LIÊN 1", giờ lấy số liệu in ở góc phải đầu phiếu, hai cột ngăn bằng nét đứt, `v3 / Bóng giấy`, lót liên hồng "LIÊN 2 · LƯU NỘI BỘ". Thanh theo trạng thái giữ màu dấu tương ứng; thanh theo người phụ trách (và thanh tải ở D02) dùng `teal/fg` trên rãnh `teal/bg`, riêng "Chưa phân công" xám. Khi lỗi vẫn chỉ hiện khung báo lỗi (A.3b).
  - Chi tiết tài liệu (K06) dùng dải thông tin phẳng nền `bg/surface` viền `kraft/border`, dấu công bố để thẳng. Mỗi phiếu đoạn là instance của component `v3 / Phiếu đoạn` (thuộc tính chữ Số đoạn, Nội dung, Trang).
- Màn công khai (đăng nhập, đăng ký) chỉ dùng dữ liệu mẫu rõ ràng ("Khách hàng mẫu", HD-0001), không dùng tên khách giống các màn đã đăng nhập.
- Lỗi đăng nhập là một thông báo chung, không chỉ ra sai email hay sai mật khẩu (FR-ID-02).
- Phiếu chưa có người phụ trách ghi "Chưa phân công" bằng chữ phụ `text/secondary`. Không dùng đỏ, và không dùng xanh mực vì dễ nhầm với link.
- Số đếm phải khớp giữa các màn: số trên rail "Phiếu tiếp nhận" là số phiếu chưa phân công, tổng các tab bằng tab "Tất cả".
- Thao tác khó hoàn tác (lưu trữ tài liệu, vô hiệu hóa tài khoản) có hộp thoại xác nhận nêu tên đối tượng và hệ quả.
- **Hộp thoại dạng phiếu (18/11/2026):** nền `bg/paper`; dòng đầu "PHIẾU XÁC NHẬN" (xác nhận) hoặc "PHIẾU CẤP THẺ NHÂN VIÊN" (thêm nhân viên) bằng `v3 / Label/Ô` `text/secondary`; đường xé nét đứt `border/strong` ngay trên hàng nút. Hệ quả chính in thành ô có nhãn như thẻ (ví dụ "TÀI KHOẢN" · "CHUYỂN VỀ CHƯA PHÂN CÔNG"), phần mô tả chỉ một câu. Thao tác phá hủy (vô hiệu hóa) dùng `v3 / Button` `Kiểu=Danger`; lưu trữ tài liệu giữ Primary.
- Trạng thái tài khoản nhân viên là dấu mộc biến thể `Tài khoản hoạt động` (HOẠT ĐỘNG, xanh lá) và `Tài khoản vô hiệu hóa` (VÔ HIỆU HÓA, xám) của `v3 / Dấu mộc`, nghiêng 2–4° ở chân thẻ D02. Không dùng `stamp/default` cho tài khoản vì màu đỏ đã dành cho "Đang xử lý".
- Thống kê (UC-17) chỉ gồm số phiếu theo trạng thái và theo người phụ trách. Có nhóm "Chưa phân công" riêng, dòng tổng, và thời điểm lấy số liệu. Không thêm chỉ số SRS chưa có. Khi lỗi lấy số liệu thì ẩn số và hiện khung báo lỗi kèm nút Tải lại; không hiện 0 thay cho dữ liệu lỗi (A.3b).

### Token và component

- **Biến:**
  - `Clarune v3 / Color` có 46 token, mode Light và Dark (thêm `border/input` cho viền ô nhập; 19/11/2026 thêm 4 họ màu, xem "Palette mở rộng" bên dưới). `overlay/scrim` là lớp phủ sau hộp thoại; `bg/paper` là mặt giấy tờ. `ink/form` (nâu, Light #7A5C45, Dark #D4B9A0) là mực in sẵn: dùng cho nhãn in sẵn như đầu phiếu, nhãn ô, tiêu đề cột. Dữ liệu điền vào vẫn dùng mực than (xanh). Giấy kem `bg/paper` chỉ dùng cho tờ chính của mỗi màn, thẻ và component còn lại nền trắng.
  - **Palette mở rộng (19/11/2026):** xanh mực và kem không còn là hai màu duy nhất. Mỗi họ có `bg`, `border`, `fg` (chữ `fg` đạt ≥ 5:1 trên `bg` của họ, trên `bg/surface` và `bg/paper`, cả Light lẫn Dark). Mỗi họ gắn với một vai trò, không dùng để trang trí.
    - `ai/*` mực tím (Light fg #6236B0, bg #F3EEFC; Dark fg #C4A9F7, bg #221A3A): mọi thứ trợ lý AI tạo ra hoặc dẫn tới AI: thẻ gợi ý AI, số trích dẫn [1], nút "Chèn vào bản nháp", "Tạo lại", "Bỏ gợi ý", "Giữ gợi ý", "Thử lại" trong panel AI, nút "Trợ lý AI" (mobile), link "Quay lại trợ lý" / "Xem lịch sử gợi ý AI", viền thẻ lịch sử gợi ý (A11, D-AIHistory), khung ghi chú bản nháp khi bỏ gợi ý, skeleton đang tải lịch sử (`ai/bg`), trạng thái "Đang xử lý" khi lập chỉ mục tài liệu, nhãn số trang ở K06. Chữ trạng thái trong thẻ lịch sử vẫn theo màu trạng thái (Sẵn sàng xanh lá, Thiếu căn cứ vàng, Tạo thất bại đỏ). Nút đánh giá "Hữu ích" / "Không hữu ích" dùng `text/secondary` để cột AI không bị tím dày; mỗi cột AI chỉ có thẻ gợi ý và các nút thao tác trên gợi ý mang màu tím. Xanh mực vẫn là mực của dữ liệu do người nhập.
    - `kraft/*` bìa kraft (Light fg #6B4C24, bg #E8D5B2; Dark fg #D9BF94, bg #29221A): module Kho chính sách, **chỉ cho mảng nhỏ làm điểm nhấn**: cuống phiếu tài liệu (K01, K06; mọi chữ trong cuống dùng `kraft/fg`), dải đầu sổ K04, tờ lót sau phiếu đoạn. Mảng lớn (dải thông tin tài liệu K06, vùng kéo thả K05, thân phiếu) nền `bg/surface`, chỉ lấy `kraft/border` hoặc `kraft/fg` cho viền (vùng kéo thả: nét đứt `kraft/fg`, ≥ 3:1). Kraft phủ mảng lớn sẽ ngả be như kem nên không dùng.
    - `teal/*` xanh dầu (Light fg #0B6680, bg #E1F2F8, border #96CFE0; Dark fg #74CCE6, bg #0E2732, border #23495A): phía khách hàng (bong bóng tin của khách ở mọi màn, cuống "THẺ KHÁCH HÀNG" ở I03, cuống phiếu và mã biên nhận trên màn của khách C01/C03/C06/C07; màn nhân viên giữ cuống `carbon`) và chuỗi số liệu theo người phụ trách ở D02/D03. Hue ~193°, cố ý tách khỏi xanh lá "Đã giải quyết" (~150°) và xanh mực (~225°) vì hai thanh này đứng cạnh nhau trên D03.
    - `priority/high/*` cam (Light fg #AE4508, bg #FDEEE3; Dark fg #FFA066, bg #33200F): dự phòng cho ưu tiên HIGH. Theo field MVP của SRS (ưu tiên mặc định `NORMAL`, thao tác đổi ưu tiên chưa được đặc tả), không màn nào hiển thị hay cho chọn mức ưu tiên. Nếu sau này SRS chốt chức năng này thì dùng họ cam, không dùng đỏ hay vàng.
    - Bảng màu đầy đủ (Light và Dark) nằm trên page `Redesign v3 / Foundations`, frame `Bảng màu v3 · Light` và `Bảng màu v3 · Dark`.
    - Đỏ `stamp/default` vẫn chỉ cho "Đang xử lý" và quá hạn; vàng `status/warning` cho "cần trả lời"; xanh lá cho đã xong.
  - `Clarune v3 / Dimension` gồm khoảng cách theo bậc 4/8, bo góc (stamp 4, control 6, card 8) và cột (nav 220, list/context 320–360).
  - `Clarune v3 / Typography` chứa font, độ đậm, cỡ và dòng.
  - Mọi biến có tên CSS (`var(--…)`).
- **Text style** `v3 / …`: Display/Số phiếu, Display/Tên thẻ, Display/Hero, Heading H1/H2, Body Md/Sm/Strong, Caption, Label/Ô, Label/Số, Stamp, Button, Nav.
- **Component:**
  - `v3 / Button` có 6 kiểu: Primary, Secondary, Tonal, Ghost, Disabled, Danger (nền `stamp/default`, chữ `text/on-carbon`). Ghost có chữ gạch chân để phân biệt với nhãn in sẵn (gạch chân đặt trên chữ của từng instance, không truyền từ component chính).
  - `v3 / Tab`.
  - `v3 / Dấu mộc` có 9 biến thể: 5 trạng thái ticket, 2 tình trạng tài liệu, 2 trạng thái tài khoản.
  - `v3 / Thẻ phiếu` (dòng hàng đợi, có dấu trạng thái).
  - `v3 / Cuống phiếu` (đầu ticket, có thuộc tính "Hiện nhãn phiếu").
- **Thứ bậc nút:** mỗi vùng chỉ có một nút Primary. Trong panel AI, "Chèn vào bản nháp" dùng kiểu Tonal để không tranh với nút gửi của vùng soạn.
- **Lưu thành công trong biểu mẫu:** hiện ngay cạnh nút vừa bấm một dòng chữ `status/success/fg` kèm icon circle-check 16px (ví dụ I04-Thành công). Sau khi đổi mật khẩu, xóa trống các ô mật khẩu. "Lưu thay đổi" ở thẻ thông tin cá nhân dùng cùng mẫu ("Đã lưu thông tin.").
- **Nút bị khóa:** dùng biến thể `Kiểu=Disabled` của `v3 / Button` (nền `status/neutral/bg`, viền `border/default`, chữ `text/disabled`). Luôn kèm một dòng giải thích vì sao nút bị khóa.

### Chuyển động: đóng dấu khi đổi trạng thái (18/11/2026)

Mẫu: frame "A03-Đóng dấu v3 · Motion · Đã giải quyết" (trang Agent). Khi phiếu đổi trạng thái, dấu mới đập xuống chỗ dấu cũ ở cuống phiếu; dấu cũ ẩn ngay lúc bắt đầu.

| Thuộc tính | 0 ms | 180 ms | 350 ms |
| --- | --- | --- | --- |
| scale | 2,4 | 0,92 (ease-in) | 1 (ease-out) |
| opacity | 0 | 1 (đạt ở 120 ms, ease-in) | 1 |
| rotate (CSS) | 12° | 3° (ease-in) | 4° (ease-out) |

- Tổng 350 ms, chạy một lần, không lặp. Bản demo có thêm 500 ms chờ ở đầu chỉ để người xem kịp nhìn.
- Chỉ dùng khi người dùng vừa đổi trạng thái (bấm "Đánh dấu đã giải quyết", "Nhận xử lý"…), không dùng khi tải trang.
- Tôn trọng `prefers-reduced-motion`: khi bật, đổi dấu ngay không có chuyển động.

### Tư duy thiết kế áp cho mọi màn v3 (17/11/2026)

**Quy ước màu liên:** liên trắng là bản gốc (LIÊN 1), liên hồng `internal/bg` là liên lưu nội bộ (ghi chú nội bộ, hồ sơ lưu), liên vàng `status/warning/bg` là liên khách giữ. Màn của khách chỉ dùng liên trắng và liên vàng; không để khách thấy liên hồng ngoài vai trò "lưu hồ sơ" ở hồ sơ cá nhân.

**Nguyên tắc gốc:** làm mọi thứ thật chi tiết. Không có chi tiết nào thừa (mỗi chi tiết phải nói đúng một sự thật của nghiệp vụ hoặc giúp người dùng làm việc), cũng không có chỗ nào thiếu (không để khoảng trống vô nghĩa, không để trạng thái hay thông tin cần thiết bị bỏ qua). Phải đủ sáng tạo nhưng nằm trong concept chung "phiếu bảo hành liên giấy than". Không làm hời hợt dẫn đến thiết kế đơn điệu, nhàm chán, tẻ nhạt hay quá đơn giản. Trước khi coi một màn là xong, rà lại từng vùng: vùng nào trống, vùng nào phẳng, chi tiết nào không có lý do tồn tại.

Không sao chép giao diện I01 sang màn khác. Mỗi màn tự trả lời bốn câu:

1. **Ẩn dụ:** màn này tương ứng với tờ giấy hay vật gì ở quầy bảo hành (phiếu, liên giấy than, sổ, thẻ)?
2. **Chiều sâu:** lớp nào nằm trên lớp nào? Dùng `v3 / Bóng giấy` cho bề mặt chính, các lớp phía sau lệch nhẹ. Bảng và danh sách giữ phẳng để đọc nhanh.
3. **Chi tiết in có nghĩa:** đầu phiếu, số liên, mã vạch, nhãn ô in hoa. Chỉ thêm chi tiết khi nó nói đúng sự thật của nghiệp vụ.
4. **Một điểm nhấn mạnh tay:** số khổng lồ viền rỗng, dấu mộc lớn hoặc màu liên. Mỗi màn chỉ một điểm nhấn chính.

### Trợ năng và cảm ứng v3 (19/11/2026)

Kết quả rà ui-ux-pro-max cho các màn Agent và Admin mới. Áp dụng cho mọi màn v3.

- **Viền ô nhập:** dùng token `border/input` (Light #7585B2, Dark #66769E), tương phản tối thiểu 3:1 với mọi nền. `border/default` và `border/strong` chỉ dành cho đường kẻ, thẻ và đường xé, không dùng làm viền khung nhập.
- **Vùng chạm:** collection `Clarune v3 / Dimension` có mode **Cảm ứng**, trong đó `size/control/md` = 44px (mode Mặc định là 40px). Đặt mode Cảm ứng cho frame tablet và mobile (A09, A10, A12, D03 tablet, D03 mobile). Tab và mục rail ở frame cảm ứng cao 44px; khoảng cách giữa hai vùng chạm tối thiểu 8px.
- **Trạng thái focus:** mọi điều khiển nhận focus bàn phím hiện vòng 2px `focus/ring`, cách viền 2px, không đổi màu nền hay chữ. Mẫu ở frame `v3 · Trạng thái focus (mẫu)` trên page Components. Khi code, thứ tự Tab theo thứ tự đọc; panel nổi không được che điều khiển đang focus.
- **Panel AI nổi (A09 tablet, A12 mobile):** có lớp mờ `overlay/scrim` phía sau, nút đóng (X) cao 44px, đóng bằng Esc và chạm vào lớp mờ. Khi mở, focus chuyển vào panel và bị giữ trong đó; khi đóng, focus trả về nút "Trợ lý AI".
- **Nhãn truy cập cho điều khiển chỉ có icon:** rail thu gọn dùng nhãn "Phiếu tiếp nhận", "Kho chính sách", "Khách hàng", "Nhân viên", "Thống kê", "Đăng xuất"; nút X ở panel AI là "Đóng trợ lý AI"; mục đang chọn ghi `aria-current="page"`.
- **Trạng thái đang tải:** vùng chờ có `aria-busy="true"` và một dòng chữ "Đang tải…" trong vùng `aria-live="polite"`. Thông báo lỗi dùng `role="alert"`, thông báo thành công dùng `role="status"`.
- **Ô nhập trên mobile:** cỡ chữ 16px (tránh iOS tự phóng to); khung soạn cách đáy ít nhất 34px để không dính thanh Home.
- **Nút bị tắt phải nói lý do:** ví dụ A07 ghi "Nhập nội dung để gửi" ở chân khung soạn.
- **Thanh số liệu thống kê (D03 tablet và mobile):** thanh nền giãn theo chiều rộng hàng; thanh tô dùng ràng buộc `SCALE` nên giữ đúng tỉ lệ giá trị / giá trị lớn nhất (21 phiếu = 100%). Khi code, đặt chiều rộng thanh bằng phần trăm.
- **Thông báo lỗi và cảnh báo** có icon cảnh báo đứng trước tiêu đề (đỏ cho lỗi, vàng cho cảnh báo), không chỉ dựa vào màu.
- **Chưa làm trong thiết kế:** màn mobile cho phiếu Admin (chi tiết phiếu, lịch sử gợi ý phía Admin). Danh sách cập nhật ở `docs/design/man-hinh-v3.md`, mục "Giới hạn".

## Quy tắc cho màn làm việc

- Rail nhân viên/quản trị viên (18/11/2026) theo kiểu "tab phân mục tập hồ sơ":
  - Đầu rail: "Clarune" và dòng "SỔ TIẾP NHẬN BẢO HÀNH", ngăn với menu bằng nét đứt `nav/item-active`.
  - Mục đang chọn là một tab giấy chạm mép phải rail: nền trùng nền vùng nội dung (`bg/canvas` ở Kho chính sách, Admin, Hồ sơ; `bg/surface` ở A03), bo trái 6, chữ `v3 / Body/Strong` và icon `carbon/default`, số đếm trong ô viền.
  - Mục chưa chọn không có gờ hay vạch ở mép phải (bỏ "gờ tab" 5×24 ngày 18/11/2026: ở cỡ 5px nó đọc như mảnh thừa chứ không ra mép tab giấy).
  - Cuối rail: "thẻ nhân viên" (FR-ID-05: mở Hồ sơ) rồi mục "Đăng xuất". Thẻ nền `nav/item-active`, chữ `nav/fg`, nghiêng −1,5°, `v3 / Bóng giấy`, khe đeo dây ở mép trên (style `v3 / Lỗ đục`), đường xé có hai vết khuyết màu `nav/bg`. Nhân viên: "THẺ NHÂN VIÊN", Vai trò · Chi nhánh. Quản trị viên: "THẺ QUẢN TRỊ VIÊN", Vai trò · Phạm vi "Tất cả".
  - Ở trang Hồ sơ (I04) không mục menu nào được chọn; thẻ ở chân rail chuyển sang giấy trắng (`bg/surface`, chữ `carbon/default` và `text/secondary`).
  - Không đặt bộ lọc trạng thái trong rail: hàng đợi đã có tab lọc riêng. Khoảng trống giữa rail là bình thường, không lấp bằng trang trí.
  - Portal khách đặt "Đăng xuất" trên thanh trên.

- Agent: điều hướng → danh sách ticket → hội thoại. **AI mặc định đóng, mở theo yêu cầu** (đặc tả Inbox). Frame A03 v3 là trạng thái "Trợ lý AI đã mở", không phải mặc định. Bố cục hẹp tuân theo đặc tả Inbox.
- Giữ bản nháp theo ticket và PUBLIC/INTERNAL. Chèn gợi ý AI không tự gửi tin nhắn.
- Customer không thấy ghi chú nội bộ. Giữ quyền nhận việc và chuyển trạng thái theo SRS.
- Trạng thái luôn có chữ; màu không phải dấu hiệu duy nhất. Có focus bàn phím rõ, nhãn cho icon và vùng chạm mobile phù hợp.
- Dùng token và text style v3; không hardcode màu, cỡ chữ, khoảng cách.
- Giao diện có Light và Dark; kiểm tra tương phản và trạng thái ở cả hai mode. Chữ phụ và placeholder đạt tối thiểu 4,5:1.
- Kiểm tra loading, empty, error, disabled, văn bản tiếng Việt dài và responsive khi triển khai. Prototype không chứng minh các trạng thái đã hoạt động trong frontend.
- Portal khách hàng xưng "bạn". Nhân viên trả lời khách theo giọng tự nhiên ("chị/anh").

## Chưa chốt

- Quyết định của nhóm (16/11/2026), SRS chưa ghi: khi vô hiệu hóa nhân viên, các phiếu đang mở của người đó trả về nhóm "Chưa phân công". Cần bổ sung vào UC-04/FR-ID-08. Lưu ý mâu thuẫn: UC-17 A.4 ghi "Ticket vẫn được thống kê ngay cả khi tài khoản của nhân viên phụ trách đã bị vô hiệu hóa", ngầm hiểu phiếu vẫn đứng tên người cũ. Hộp thoại D02-Vô hiệu hóa đang theo quyết định của nhóm; khi sửa SRS cần thống nhất hai chỗ này.
- Hồ sơ (I03–I04) khóa ô Email theo bản v2. SRS (FR-ID-06) chưa nói email có được đổi không; cần nhóm chốt.
- Panel "Đơn hàng" (hóa đơn, chi nhánh, bảo hành còn lại) là đề xuất. SRS chưa có thực thể đơn hàng.
- Logo Clarune mới chưa vẽ; hiện dùng chữ tạm.
- Agent đã có A09 (tablet 1024×768, panel AI nổi bên phải, rail thu thành icon) và A10 (mobile 390×844, nút "Trợ lý AI" ở thanh trên), cả hai có Light/Dark. Chưa có bản v3 cho tablet và mobile phía quản trị, Admin D04–D06.
- Form đăng nhập/đăng ký không có "Quên mật khẩu" và không ghi quy tắc độ dài mật khẩu, vì SRS chưa quy định.
- Đính kèm ảnh/video là chức năng giai đoạn mở rộng trong SRS, chưa vẽ.

Các file này là tài liệu hướng dẫn, không tự đổi giao diện hoặc cài component vào frontend.
