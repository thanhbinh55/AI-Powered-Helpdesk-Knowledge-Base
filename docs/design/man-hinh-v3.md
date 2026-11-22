# Bảng màn hình — Redesign v3 "Phiếu bảo hành"

Cập nhật 19/11/2026. File Figma **SE**, các page `Redesign v3 / …`. Quy tắc thị giác, token và component xem [DESIGN.md](../../DESIGN.md) mục "Ngôn ngữ thị giác v3". Bản v2 ở [man-hinh.md](man-hinh.md) đã bàn giao, không sửa.

**105 frame** trên 5 page giao diện. Mỗi màn chính có bản Dark nếu ghi "Dark". Ảnh PNG từng frame ở [anh/v3/](anh/v3/), tên file là ID node (`113-819.png` là node `113:819`).

| Page | ID |
| --- | --- |
| Redesign v3 / Foundations | `111:863` |
| Redesign v3 / Components | `111:864` |
| Redesign v3 / Agent | `111:1699` |
| Redesign v3 / Customer | `111:2663` |
| Redesign v3 / Knowledge Base | `111:3671` |
| Redesign v3 / Identity | `111:3978` |
| Redesign v3 / Admin | `112:2027` |

## Agent (46 frame)

| Màn | Node |
| --- | --- |
| A01 · Phiếu mới · Nhận xử lý | `132:5524` |
| A02 · Xử lý phiếu · Trợ lý AI đóng | `132:5676` |
| A03 · Xử lý phiếu · Trợ lý AI đã mở | `111:1700` |
| A03 · Xử lý phiếu · Dark | `115:2152` |
| A03-Internal · Soạn ghi chú nội bộ | `115:2017` |
| A05 · AI đang tạo gợi ý | `118:2229` |
| A05 · AI đang tạo gợi ý · Dark | `118:3811` |
| A03-Đóng dấu · Motion · Đã giải quyết | `116:2536` |
| A-AIError · AI tạm thời không phản hồi | `118:2508` |
| A-AIError · AI tạm thời không phản hồi · Dark | `118:4088` |
| A-SendError · Gửi lỗi · Giữ bản nháp | `118:2785` |
| A06 · Xung đột nhận xử lý | `118:3245` |
| A-SendError · Gửi lỗi · Giữ bản nháp · Dark | `118:4363` |
| A07 · Chờ khách phản hồi | `118:3523` |
| A07 · Chờ khách phản hồi · Dark | `118:4881` |
| A06 · Xung đột nhận xử lý · Dark | `118:4642` |
| A10 · Mobile · Hội thoại | `118:5192` |
| A10 · Mobile · Hội thoại · Dark | `118:5933` |
| A12 · Mobile · Trợ lý AI (bảng trượt) | `119:16873` |
| A12 · Mobile · Trợ lý AI (bảng trượt) · Dark | `119:17003` |
| A13 · Mobile · Lịch sử gợi ý AI | `119:17179` |
| A13 · Mobile · Lịch sử gợi ý AI · Dark | `119:17602` |
| A-DiscardConfirm · Mobile · Xác nhận bỏ gợi ý | `119:17225` |
| A-DiscardConfirm · Mobile · Dark | `119:17740` |
| A-DiscardError · Mobile · Lỗi bỏ gợi ý | `119:17271` |
| A-DiscardError · Mobile · Dark | `119:17863` |
| A09 · Tablet · Trợ lý AI nổi | `118:5368` |
| A09 · Tablet · Trợ lý AI nổi · Dark | `118:5651` |
| A11 · Lịch sử gợi ý AI | `118:6210` |
| A11-Rỗng · Chưa có gợi ý | `118:6489` |
| A11-Đang tải · Đang tải lịch sử | `118:6794` |
| A11-Lỗi · Lỗi tải lịch sử | `118:7071` |
| A11 · Lịch sử gợi ý AI · Dark | `118:7365` |
| A11-Rỗng · Chưa có gợi ý · Dark | `118:7660` |
| A11-Đang tải · Đang tải lịch sử · Dark | `118:7937` |
| A11-Lỗi · Lỗi tải lịch sử · Dark | `118:8217` |
| A-DiscardConfirm · Xác nhận bỏ gợi ý | `118:8823` |
| A-DiscardError · Lỗi bỏ gợi ý | `118:9088` |
| A-DiscardConfirm · Xác nhận bỏ gợi ý · Dark | `118:9399` |
| A-DiscardError · Lỗi bỏ gợi ý · Dark | `118:9558` |
| A-ManualAfterDiscard · Tiếp tục soạn thủ công | `118:14515` |
| A-HistorySourceError · Lỗi tải bản chụp nguồn | `118:14804` |
| A-HistoryLost · Quyền truy cập đã thay đổi | `118:15089` |
| A-ManualAfterDiscard · Tiếp tục soạn thủ công · Dark | `118:15373` |
| A-HistorySourceError · Lỗi tải bản chụp nguồn · Dark | `118:15655` |
| A-HistoryLost · Quyền truy cập đã thay đổi · Dark | `118:15934` |

## Customer (8 frame)

| Màn | Node |
| --- | --- |
| C01 · Yêu cầu của tôi | `111:2664` |
| C01 · Dark | `115:1412` |
| C02 · Tạo yêu cầu | `132:6237` |
| C03 · Chi tiết yêu cầu, đang xử lý | `111:2763` |
| C04 · Đã giải quyết · Chờ xác nhận | `132:6339` |
| C05 · Yêu cầu đã đóng | `132:6441` |
| C06 · Mobile, yêu cầu của tôi | `111:3570` |
| C07 · Mobile, chi tiết yêu cầu | `111:3571` |

## Knowledge Base (13 frame)

| Màn | Node |
| --- | --- |
| K01 · Kết quả tìm kiếm | `111:3691` |
| K04 · Quản lý tài liệu (sổ tài liệu) | `111:4066` |
| K04-Lưu trữ · Xác nhận lưu trữ | `112:1457` |
| K04 · Dark | `112:1583` |
| K05 · Tải tài liệu lên | `113:693` |
| K05-Lỗi · Tệp vượt quá 10 MB | `113:1812` |
| K05-Sai định dạng · Tệp không được hỗ trợ | `113:2235` |
| K05 · Dark | `113:2410` |
| K06 · Chi tiết tài liệu (xấp phiếu thư mục) | `113:819` |
| K06-Đang xử lý | `113:1899` |
| K06-Thất bại | `113:1977` |
| K06-Lưu trữ · Xác nhận lưu trữ | `113:2323` |
| K06 · Dark | `113:2497` |

## Identity (12 frame)

| Màn | Node |
| --- | --- |
| I01 · Đăng nhập | `113:4387` |
| I01-Lỗi · Sai thông tin đăng nhập | `114:4833` |
| I01 · Dark | `114:5012` |
| I02 · Đăng ký khách hàng | `114:4766` |
| I02-Lỗi · Email đã được dùng | `114:4900` |
| I02 · Dark | `114:5079` |
| I03 · Hồ sơ khách hàng | `113:3580` |
| I03 · Dark | `115:882` |
| I04 · Hồ sơ nhân viên / quản trị viên | `113:3461` |
| I04-Lỗi · Sai mật khẩu hiện tại | `115:531` |
| I04-Thành công · Đã đổi mật khẩu | `115:648` |
| I04 · Dark | `115:765` |

## Admin (26 frame)

| Màn | Node |
| --- | --- |
| D01 · Tất cả yêu cầu | `112:1709` |
| D01-Phân công · Hộp thoại phân công nhân viên | `133:7972` |
| D02 · Nhân viên | `112:2142` |
| D03 · Thống kê | `112:2268` |
| D03-Cấm · Không có quyền xem thống kê | `118:10067` |
| D03-Cấm · Không có quyền xem thống kê · Dark | `118:10198` |
| D-AIHistory · Lịch sử gợi ý AI (Admin) | `118:10738` |
| D02-Vô hiệu hóa · Xác nhận | `112:2883` |
| D-AIHistoryEmpty · Chưa có gợi ý (Admin) | `118:11051` |
| D03-Đang tải · Thống kê | `112:2550` |
| D-AIHistoryError · Lỗi tải lịch sử (Admin) | `118:11263` |
| D03 · Mobile · Thống kê | `118:10322` |
| D03 · Mobile · Thống kê · Dark | `118:10449` |
| D-AIHistoryLoading · Đang tải lịch sử (Admin) | `118:12613` |
| D-AIHistory · Lịch sử gợi ý AI (Admin) · Dark | `118:11829` |
| D02-Thêm · Thêm nhân viên | `112:2985` |
| D-AIHistoryEmpty · Chưa có gợi ý (Admin) · Dark | `118:12041` |
| D03-Rỗng · Thống kê | `112:2657` |
| D-AIHistoryError · Lỗi tải lịch sử (Admin) · Dark | `118:12326` |
| D-Detail · Chi tiết phiếu · Lịch sử yêu cầu (Admin) | `118:13090` |
| D-AIHistoryLoading · Đang tải lịch sử (Admin) · Dark | `118:13399` |
| D02-Thêm-Lỗi · Email đã dùng | `112:3117` |
| D03-Lỗi · Thống kê | `112:2764` |
| D-Detail · Chi tiết phiếu · Lịch sử yêu cầu (Admin) · Dark | `118:13687` |
| D03 · Tablet · Thống kê | `118:13979` |
| D03 · Tablet · Thống kê · Dark | `118:14112` |

## Thay đổi ngày 18/11/2026

- Token mới `bg/paper` cho mặt giấy tờ (tờ phiếu, tờ hồ sơ, sổ, phiếu thư mục, giấy note, hộp thoại dạng phiếu). Nền màn vẫn `bg/canvas`.
- D01 và K04 thành kiểu sổ: đầu sổ, lề đỏ đôi, các dòng phẳng.
- K06: danh sách đoạn thành các phiếu thư mục rời, phẳng.
- D02: thẻ nhân viên làm lại (tên một dòng, số phiếu đang mở là điểm nhấn, vạch trung bình nhóm, dấu mộc trạng thái tài khoản). Ba hộp thoại D02 và hai hộp thoại lưu trữ ở K04/K06 thành dạng phiếu.
- Component: `v3 / Button` thêm `Kiểu=Danger`; `v3 / Dấu mộc` thêm `Tài khoản hoạt động`, `Tài khoản vô hiệu hóa`; text style `v3 / Display/Tên thẻ`.
- Rail bỏ "gờ tab" ở mục chưa chọn.
- Dải đầu trang C01/C06: dòng "SỔ BẢO HÀNH CỦA BẠN", hai chip trạng thái, xấp phiếu trống "Tạo yêu cầu mới" (desktop).
- Hội thoại C03, C07 và 4 frame A03: bong bóng chat (tin của mình canh phải nền `carbon/subtle`, bên kia canh trái nền giấy), sự kiện đổi trạng thái là dấu mộc ở giữa, ghi chú nội bộ là bong bóng hồng; khung soạn nền giấy có đường xé phía trên nút gửi.
- Chuyển động "đóng dấu" khi đổi trạng thái: spec trong DESIGN.md, mẫu ở frame `116:2536`.

## Thay đổi ngày 19/11/2026

- Agent: thêm trạng thái AI đang tạo, lỗi AI, lỗi gửi, xung đột nhận xử lý, chờ khách, tablet (A09), mobile (A10), lịch sử gợi ý (A11 và biến thể), xác nhận/lỗi bỏ gợi ý (UC-15). Mọi màn có Light/Dark.
- Admin: thêm D03-Cấm (không có quyền, nhìn từ tài khoản nhân viên), D03 mobile và tablet, chi tiết phiếu (D-Detail) có khối "Lịch sử yêu cầu", lịch sử gợi ý AI (D-AIHistory và biến thể). Có Light/Dark.
- Token `ink/form` (mực in sẵn, nâu) cho nhãn in sẵn; giấy kem `bg/paper` chỉ ở tờ chính của mỗi màn; nút Ghost có chữ gạch chân.

## Sửa sau rà trợ năng (19/11/2026)

- Token `border/input` cho viền ô nhập (đạt 3:1); mode **Cảm ứng** (nút, tab, mục rail 44px) áp cho A09, A10, A12, D03 tablet/mobile.
- A09 và A12: lớp mờ nền; A12 là panel AI mobile. D-Detail có nút "Xem lịch sử gợi ý AI"; lịch sử Admin ghi "← Về chi tiết phiếu".
- Frame mẫu focus `119:16853` trên page `Redesign v3 / Components`. Quy tắc chi tiết ở DESIGN.md, mục "Trợ năng và cảm ứng v3".
- Thêm icon cảnh báo trước thông báo lỗi (16 chỗ, Light/Dark); mobile của lịch sử gợi ý (A13) và xác nhận/lỗi bỏ gợi ý; thanh số liệu D03 tablet/mobile co giãn theo tỉ lệ (ràng buộc SCALE).

## Palette mở rộng và K06 làm lại (19/11/2026)

- Thêm 12 token `ai/*` (mực tím), `kraft/*` (bìa kraft), `teal/*` (xanh dầu), `priority/high/*` (cam); `Clarune v3 / Color` có 46 token. Vai trò từng họ ở DESIGN.md, mục "Palette mở rộng".
- K06 làm lại (K06, K06-Lưu trữ, K06 Dark): các đoạn xếp một cột, mỗi đoạn là phiếu thư mục trắng có cuống trái kraft in số đoạn lớn, đường đục lỗ dọc có hai khuyết, nhãn số trang `ai/fg` để thẳng, tờ lót kraft lệch phía sau. Dải thông tin tài liệu nền trắng, viền kraft.
- Kho chính sách: kraft chỉ ở mảng nhỏ (cuống K01/K06, dải đầu sổ K04, tờ lót); thẻ kết quả K01, tờ biểu mẫu và vùng kéo thả K05 nền trắng (vùng kéo thả viền nét đứt `kraft/fg`). "Đang xử lý" của tài liệu dùng `ai/fg`.
- K05: khối "Sau khi tải lên" thành thẻ trắng có đường xé dưới tiêu đề và trên chú thích, vòng số 28px (áp cho cả bốn biến thể K05).
- AI (mực tím): thẻ gợi ý, trích dẫn, các nút thao tác trên gợi ý, lịch sử gợi ý (A11, D-AIHistory), các màn bỏ gợi ý / soạn thủ công / lỗi bản chụp nguồn, nút "Trợ lý AI" mobile, skeleton đang tải lịch sử. Nút đánh giá gợi ý dùng `text/secondary`.
- Khách hàng (xanh dầu): bong bóng tin của khách ở Agent, Admin, Customer; cuống thẻ khách hàng I03. Thanh theo người phụ trách ở D02/D03 cũng dùng teal; hue tách khỏi xanh lá "Đã giải quyết".
- Lỗi dưới ô nhập ở K05-Lỗi, K05-Sai định dạng, D02-Thêm-Lỗi có icon cảnh báo.
- A01, A02 (19/11/2026): A01 là phiếu Mới chưa phân công (nút Primary "Nhận xử lý", khung soạn và nút gửi bị khóa, thẻ AI ghi "Nhận xử lý phiếu để dùng trợ lý AI"); A02 là phiếu đang xử lý khi chưa tạo gợi ý (thẻ AI "Chưa tạo gợi ý" và nút "Tạo gợi ý trả lời").
- C02, C04, C05 (19/11/2026), theo SRS: C02 là "PHIẾU YÊU CẦU BẢO HÀNH · LIÊN 1" với ô Tiêu đề và ô Mô tả vấn đề (giới hạn 5–150 và 10–5000 ký tự, nhắc không gửi mật khẩu), cột phụ "Sau khi gửi" và tờ "Khi gửi yêu cầu bảo hành, nên có sẵn". C04: dấu ĐÃ GIẢI QUYẾT, tiến trình ở bước 3, khung trả lời thay bằng "PHIẾU ĐÃ GIẢI QUYẾT · CHỜ BẠN XÁC NHẬN" với "Mở lại yêu cầu" và "Xác nhận đóng" (khách không nhắn được khi phiếu đã giải quyết, BR-07). C05: dấu ĐÃ ĐÓNG, đủ 4 bước, "PHIẾU ĐÃ ĐÓNG" không cho nhắn tiếp, có nút "Tạo yêu cầu mới".
- D01-Phân công (19/11/2026), theo UC-07 luồng B: hộp thoại "PHIẾU PHÂN CÔNG · SỐ 1063" trên nền D01. Ô Khách hàng và ô Sau khi lưu (Đang xử lý). Danh sách chỉ có nhân viên đang hoạt động, xếp theo số phiếu đang mở; dòng đang chọn nền `carbon/subtle`, viền `carbon/default` 2px. Nút chính ghi tên người được giao.
- Sửa lỗi: chữ nút Primary "Đánh dấu đã giải quyết", "Về hàng đợi" ở 39 frame Agent bị gạch chân (chỉ nút Ghost được gạch chân); 8 frame mobile A12, A13, A-Discard mobile được đổi sang màu `ai`, `teal` như các màn desktop.
- Họ `priority/high` để dự phòng: theo field MVP của SRS, ưu tiên mặc định `NORMAL` và thao tác đổi ưu tiên chưa được đặc tả, nên không màn nào hiển thị hay cho chọn mức ưu tiên.
- Màn khách (C01, C01 Dark, C03, C06, C07): cuống phiếu, mã biên nhận và bong bóng tin của khách dùng `teal`; dải đầu trang giữ xanh mực thương hiệu. Màn nhân viên giữ cuống `carbon`.
- Component mới `v3 / Phiếu đoạn` (`120:7444`, page Foundations) với thuộc tính chữ Số đoạn, Nội dung, Trang; 12 phiếu đoạn ở 3 frame K06 là instance của component này.
- Bảng màu trên page Foundations: `Bảng màu v3 · Light` (`120:7589`) và bản Dark (`120:7809`), đủ 46 token chia theo vai trò.

## Prototype v3 (19/11/2026)

Liên kết bấm (chuyển cảnh mờ dần 200 ms):

| Từ | Bấm | Tới |
| --- | --- | --- |
| C01 `111:2664` | Phiếu HD-1048 | C03 `111:2763` |
| C03 | "Yêu cầu của tôi" | C01 |
| C06 `111:3570` | Phiếu HD-1048 | C07 `111:3571` |
| K01 `111:3691` | "Đọc tài liệu" (kết quả 1) | K06 `113:819` |
| K04 `111:4066` | "Tải tài liệu lên" | K05 `113:693` |
| K04 | "Lưu trữ" (dòng 01) | K04-Lưu trữ `112:1457` |
| K04 | "Xem chi tiết" (dòng 06) | K06-Thất bại `113:1977` |
| K05, K06 | "Quản lý tài liệu" | K04 |
| K06 | "Lưu trữ tài liệu" | K06-Lưu trữ `113:2323` |
| A01 `132:5524` | "Nhận xử lý" | A02 `132:5676` |
| A02 | "Tạo gợi ý trả lời" | A05 `118:2229` |
| A03 `111:1700` | "Lịch sử (3)" | A11 `118:6210` |
| A11 | "Quay lại trợ lý" | A03 |
| A03 | "Bỏ gợi ý" | A-DiscardConfirm `118:8823` |
| C01 | Tờ "Tạo yêu cầu mới" | C02 `132:6237` |
| C02 | "Gửi yêu cầu" / "Hủy" | C03 / C01 |
| C04 `132:6339` | "Xác nhận đóng" / "Mở lại yêu cầu" | C05 `132:6441` / C03 |
| C05 | "Tạo yêu cầu mới" | C02 |
| C02, C04, C05 | "Yêu cầu của tôi" | C01 |
| D01 | "Phân công" ở phiếu 1063 | D01-Phân công `133:7972` |
| D01-Phân công | "Hủy" / "Giao cho Thu Trang" | D01 |
| D-Detail `118:13090` | "Xem lịch sử gợi ý AI" | D-AIHistory `118:10738` |
| D-AIHistory | "Về chi tiết phiếu" | D-Detail |

Flow: C01, C06, C04 (Customer); K04, K01 (Knowledge Base); A01, A03 (Agent); D01, D-Detail (Admin).

## Giới hạn

- Chưa có bản v3 cho tablet và mobile phía khách hàng và quản trị (trừ D03). Màn v2 A04, D04, D05, D06 đã có bản v3 tương ứng là A03-Internal, D02, D02-Thêm, D03.
- Các màn dựng ngày 19/11/2026 (Agent A05–A11, UC-15, UC-18; Admin D03-Cấm, D03 mobile/tablet, D-AIHistory, D-Detail) nhân bản từ khung đã có, nội dung thông báo lấy từ bản v2 nên cần đối chiếu SRS. Thanh số liệu thống kê ở D03 mobile/tablet có chiều rộng cố định.
- Prototype mới nối các luồng chính ở bảng trên; trạng thái lỗi, Dark và mobile chưa nối.
- Frame Motion chỉ minh họa một lần đổi trạng thái. Figma Motion là bản beta; khi code dùng spec trong DESIGN.md.
- Chưa kiểm tra bàn phím, screen reader và focus; kiểm tra khi code frontend.
