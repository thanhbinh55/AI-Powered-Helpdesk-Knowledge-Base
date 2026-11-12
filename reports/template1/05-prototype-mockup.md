# 5. BẢN MẪU GIAO DIỆN (UI PROTOTYPE & DESIGN SYSTEM)

> **Thông tin điều phối:**
> - **Người phụ trách tổng hợp UI:** Lê Quý Phúc (Module A - AI Assistance & Frontend UI Lead).
> - **Tài liệu làm việc nhóm (Google Docs):** [[SE - Nhóm 4] template1 - Google Tài liệu](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0)
> - **File thiết kế chính thức (Figma SE):** [SE – Figma (Node 49:58 - Redesign v2)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)
> - **Tài liệu đặc tả liên quan:** [DESIGN.md](../../DESIGN.md) · [Đặc tả Inbox Workspace](../../docs/design/dac-ta-inbox.md) · [Design System MASTER v2](../../design-system/helpdesk-workspace/MASTER.md) · [Danh mục màn hình chi tiết](../../docs/design/man-hinh.md).

---

## 5.1 TỔNG QUAN PHƯƠNG ÁN THIẾT KẾ (REDESIGN V2)

Giao diện hệ thống Helpdesk được thiết kế theo **Phương án A: "Bàn làm việc yên tĩnh" (Quiet Workspace)**, tối ưu hóa cho nhân viên hỗ trợ (Agent) và quản trị viên (Admin) xử lý liên tục nhiều yêu cầu mà không bị mỏi mắt hay phân tâm. Hệ thống hỗ trợ hoàn chỉnh cả **Light Mode** và **Dark Mode**, tuân thủ nghiêm ngặt chuẩn tiếp cận người dùng **WCAG 2.1 AA** (độ tương phản chữ tối thiểu 4.5:1, viền điều khiển $\ge 3:1$).

* **Quy mô thiết kế:** Gồm **33 nhóm màn hình chính** với **151 frames**, 56 luồng tương tác (prototype flows) và 709 reactions được thiết lập trên Figma.
* **Toàn bộ ảnh chụp màn hình (PNG):** Được lưu trữ trực tiếp trong kho mã nguồn tại thư mục [`docs/design/anh/`](../../docs/design/anh/) và [`docs/design/anh/thanh-phan/`](../../docs/design/anh/thanh-phan/).
* **Thích ứng màn hình (Responsive Breakpoints):**
  - **Desktop (1440 × 900 px):** Bố cục 3 cột liền mạch: Điều hướng (184px) + Danh sách ticket (320px) + Vùng hội thoại (936px). Ngăn Trợ lý AI / Ngữ cảnh rộng 320px mở theo yêu cầu.
  - **Tablet (1024 × 768 px):** Thanh ray thu gọn (72px) + Danh sách (280px) + Hội thoại; Ngăn AI hiển thị dạng Overlay (tối đa 360px).
  - **Mobile (390 × 844 px):** Tách thành các màn hình độc lập (Danh sách, Chi tiết hội thoại, Trợ lý AI, Đọc nguồn) với nút điều hướng quay lại rõ ràng.

> **Nguyên tắc kế thừa và tinh chỉnh:** Bộ thiết kế Redesign v2 do Lê Quý Phúc khởi tạo đóng vai trò là **Bộ khung nền tảng (Baseline)** đảm bảo tính nhất quán về Design Tokens, Typography và Layout cho toàn hệ thống. Từng thành viên phụ trách phân hệ (Module Owner) có toàn quyền chủ động rà soát, tinh chỉnh hoặc vẽ bổ sung các màn hình, luồng tương tác và trạng thái biên trên Figma để đáp ứng chính xác nhất kịch bản nghiệp vụ của Use Case mình phụ trách.

---

## 5.2 BẢNG MA TRẬN 33 NHÓM MÀN HÌNH CHÍNH & ÁNH XẠ USE CASE

| STT | Phân hệ | Nhóm màn hình chính | Node ID (Figma) | Chế độ | Use Case ánh xạ | Ảnh minh họa (PNG) |
|:---:|:---|:---|:---:|:---:|:---|:---:|
| **01** | **Agent** | A01 · Hàng đợi · Nhận xử lý | `55:1992` | Light | UC-07, UC-08 | [`55-1992.png`](../../docs/design/anh/55-1992.png) |
| **02** | Agent | A02 · Xử lý ticket · AI đóng | `55:1993` | Light | UC-07, UC-10 | [`55-1993.png`](../../docs/design/anh/55-1993.png) |
| **03** | Agent | A03 · Gợi ý AI có trích dẫn nguồn | `55:1994` | Light | UC-14, UC-15 | [`55-1994.png`](../../docs/design/anh/55-1994.png) |
| **04** | Agent | A04 · Ghi chú nội bộ (Internal Note) | `55:2537` | Light | UC-10 | [`55-2537.png`](../../docs/design/anh/55-2537.png) |
| **05** | Agent | A05 · AI đang tạo gợi ý | `55:2538` | Light | UC-14 | [`55-2538.png`](../../docs/design/anh/55-2538.png) |
| **06** | Agent | A06 · Xung đột nhận xử lý (Claim Conflict) | `56:3104` | Light | UC-08 | [`56-3104.png`](../../docs/design/anh/56-3104.png) |
| **07** | Agent | A07 · Yêu cầu thêm thông tin (Chờ khách) | `56:3576` | Light | UC-07 | [`56-3576.png`](../../docs/design/anh/56-3576.png) |
| **08** | Agent | A08 · Đọc chi tiết nguồn của gợi ý | `56:3578` | Light | UC-14 | [`56-3578.png`](../../docs/design/anh/56-3578.png) |
| **09** | Agent | A09 · Tablet · AI Drawer Overlay | `56:4106` | Light | UC-07, UC-14 | [`56-4106.png`](../../docs/design/anh/56-4106.png) |
| **10** | Agent | A10 · Mobile · Hội thoại xử lý ticket | `56:4107` | Light | UC-07, UC-10 | [`56-4107.png`](../../docs/design/anh/56-4107.png) |
| **11** | **Customer** | C01 · Danh sách yêu cầu của tôi | `58:6763` | Light | UC-06 | [`58-6763.png`](../../docs/design/anh/58-6763.png) |
| **12** | Customer | C02 · Tạo yêu cầu hỗ trợ mới | `58:6764` | Light | UC-05 | [`58-6764.png`](../../docs/design/anh/58-6764.png) |
| **13** | Customer | C03 · Chi tiết yêu cầu · Đang xử lý | `58:6765` | Light | UC-06, UC-09 | [`58-6765.png`](../../docs/design/anh/58-6765.png) |
| **14** | Customer | C04 · Yêu cầu đã giải quyết (Chờ xác nhận) | `62:6953` | Light | UC-06, UC-09 | [`62-6953.png`](../../docs/design/anh/62-6953.png) |
| **15** | Customer | C05 · Yêu cầu đã đóng (Closed - Readonly) | `62:6954` | Light | UC-06 | [`62-6954.png`](../../docs/design/anh/62-6954.png) |
| **16** | Customer | C06 · Mobile · Danh sách yêu cầu | `62:6955` | Light | UC-06 | [`62-6955.png`](../../docs/design/anh/62-6955.png) |
| **17** | Customer | C07 · Mobile · Chi tiết yêu cầu | `62:7174` | Light | UC-06, UC-09 | [`62-7174.png`](../../docs/design/anh/62-7174.png) |
| **18** | **Identity** | I01 · Đăng nhập hệ thống (Login) | `62:8214` | Light | UC-02 | [`62-8214.png`](../../docs/design/anh/62-8214.png) |
| **19** | Identity | I02 · Đăng ký tài khoản khách hàng | `62:8215` | Light | UC-01 | [`62-8215.png`](../../docs/design/anh/62-8215.png) |
| **20** | Identity | I03 · Hồ sơ cá nhân khách hàng | `62:8216` | Light | UC-03 | [`62-8216.png`](../../docs/design/anh/62-8216.png) |
| **21** | Identity | I04 · Hồ sơ nhân viên / Quản trị viên | `62:8328` | Light | UC-03 | [`62-8328.png`](../../docs/design/anh/62-8328.png) |
| **22** | Identity | I05 · Mobile · Đăng nhập | `62:8329` | Light | UC-02 | [`62-8329.png`](../../docs/design/anh/62-8329.png) |
| **23** | **Knowledge** | K01 · Tìm kiếm tri thức (Search KB) | `62:9092` | Light | UC-13 | [`62-9092.png`](../../docs/design/anh/62-9092.png) |
| **24** | Knowledge | K02 · Không có kết quả tìm kiếm | `62:9093` | Light | UC-13 | [`62-9093.png`](../../docs/design/anh/62-9093.png) |
| **25** | Knowledge | K03 · Đọc tài liệu tri thức đã công bố | `62:9094` | Light | UC-13 | [`62-9094.png`](../../docs/design/anh/62-9094.png) |
| **26** | Knowledge | K04 · Bảng quản trị tài liệu tri thức | `62:9240` | Light | UC-11, UC-12 | [`62-9240.png`](../../docs/design/anh/62-9240.png) |
| **27** | Knowledge | K05 · Tải lên tài liệu mới (UploadZone) | `62:9241` | Light | UC-11 | [`62-9241.png`](../../docs/design/anh/62-9241.png) |
| **28** | Knowledge | K06 · Chi tiết tài liệu · Thao tác Công bố | `62:9242` | Light | UC-12 | [`62-9242.png`](../../docs/design/anh/62-9242.png) |
| **29** | **Admin** | D01 · Danh sách tất cả yêu cầu (Filter) | `62:9943` | Light | UC-07, UC-10 | [`62-9943.png`](../../docs/design/anh/62-9943.png) |
| **30** | Admin | D02 · Chi tiết yêu cầu và lịch sử thay đổi | `62:9944` | Light | UC-07, UC-10 | [`62-9944.png`](../../docs/design/anh/62-9944.png) |
| **31** | Admin | D03 · Phân công nhân viên phụ trách | `62:9945` | Light | UC-08 | [`62-9945.png`](../../docs/design/anh/62-9945.png) |
| **32** | Admin | D04 · Quản lý danh sách nhân viên | `62:10225` | Light | UC-04 | [`62-10225.png`](../../docs/design/anh/62-10225.png) |
| **33** | Admin | D05 · Tạo tài khoản nhân viên mới | `62:10226` | Light | UC-04 | [`62-10226.png`](../../docs/design/anh/62-10226.png) |

---

## 5.3 CÁC MÀN HÌNH ĐẶC THÙ: TRẠNG THÁI BIÊN, NGOẠI LỆ & DARK MODE

Bên cạnh 33 màn hình chính, hệ thống đã thiết kế chi tiết các màn hình xử lý trạng thái biên, thông báo lỗi và chế độ nền tối (Dark Mode):

1. **Nhánh ngoại lệ AI & Trợ lý ảo (FR-AI-01..10):**
   - `A-AIError` (`55:2539`): Thông báo AI tạm thời không phản hồi / timeout, nhân viên vẫn soạn tin nhắn thủ công bình thường.
   - `A-AIInsufficient` (`56:3103`): AI phát hiện thiếu căn cứ (độ tương đồng vector dưới ngưỡng hoặc tài liệu không đủ dữ kiện - tuân thủ BR-03).
   - `A-Replace` (`56:6373`): Hộp thoại xác nhận ghi đè khi nhân viên bấm chèn gợi ý AI vào ô soạn thảo đã có sẵn nội dung.
2. **Nhánh quản trị tài liệu & Ingestion Worker (FR-KB-01..10):**
   - `K-TooLarge` (`62:9621`): Cảnh báo tệp vượt quá dung lượng tối đa cho phép (10 MiB).
   - `K-ScanFailed` (`62:9622`): Từ chối tệp PDF dạng ảnh quét không có text layer (tuân thủ BR-06).
   - `K-ReadyDetail` (`62:9783`): Tài liệu đã ingestion thành công (`READY`), chờ Admin duyệt bấm nút "Công bố" (Published).
   - `K-Archive` (`62:11218`): Xác nhận lưu trữ (Archive) tài liệu đã công bố để loại trừ khỏi tìm kiếm và RAG.
3. **Chế độ nền tối (Dark Mode):**
   - `A-Dark` (`56:6374`): Giao diện xử lý ticket và gợi ý AI chế độ Dark.
   - `C-Dark` (`62:8115`): Giao diện chi tiết yêu cầu khách hàng chế độ Dark.
   - `I-Dark` (`62:8879`): Giao diện đăng nhập chế độ Dark.
   - `K-Dark` (`62:11220`): Kho tri thức chế độ Dark.
   - `D-Dark` (`62:13392`): Danh sách yêu cầu quản trị chế độ Dark.

---

## 5.4 KẾT QUẢ KIỂM ĐỊNH TỰ ĐỘNG (AUDIT & SEMANTIC CHECKS)

Toàn bộ 151 frames và bộ Design System đã được kiểm định tự động thông qua các công cụ phân tích tĩnh:
* **Kiểm tra độ tương phản màu (WCAG 2.1 AA):** 100% các cặp màu chữ chính (`text/primary`), chữ phụ (`text/secondary`) và nhãn nút trên nền surface/subtle đạt tỉ lệ tương phản $\ge 4.74:1$ (vượt ngưỡng yêu cầu $4.5:1$). Viền ô nhập liệu (`border/control`) đạt $\ge 3.27:1$ (vượt ngưỡng $3:1$).
* **Kiểm tra logic nghiệp vụ (`redesign-v2-semantic-checks.json`):**
  - Khóa ô soạn thảo khi chưa Claim: `openComposerLocked = true`.
  - Chèn gợi ý AI không tự động gửi: `aiInsertAndSendExact = true`.
  - Khách hàng không thấy ghi chú nội bộ hoặc AI: `noCustomerInternalOrAI = true`.
  - Tách bạch trạng thái kỹ thuật `READY` và kinh doanh `Đã công bố`: `publicationSeparate = true`.
  - Mật khẩu đã đổi tự động xóa khỏi form: `passwordClearedAndDisabled = true`.

## 5.5 Giao diện AI và tham chiếu quản trị

### 5.5.1 Gợi ý AI và trích dẫn

Agent tạo gợi ý, đọc nguồn và chủ động chèn vào bản nháp để kiểm duyệt trước khi gửi. Ngăn AI có lối mở lịch sử và thao tác đánh giá gợi ý; thao tác chèn hoặc đánh giá không tự gửi phản hồi.

*Hình 5.19 Gợi ý AI, nguồn trích dẫn và thao tác hỗ trợ nhân viên*

### 5.5.2 Xem nguồn trích dẫn

Người dùng mở đoạn nguồn để kiểm tra nội dung gợi ý. Bản chụp đã lưu tại thời điểm tạo được giữ nguyên, kể cả khi tài liệu nguồn hiện đã lưu trữ; quyền tải tài liệu gốc được kiểm tra riêng.

*Hình 5.20 Xem đoạn nguồn trích dẫn của gợi ý*

### 5.5.3 Danh sách yêu cầu quản trị

Admin xem danh sách toàn bộ ticket và sử dụng bộ lọc để tìm yêu cầu cần theo dõi hoặc xử lý.

*Hình 5.21 Danh sách yêu cầu quản trị*

### 5.5.4 Xử lý, lịch sử yêu cầu và phân công nhân viên

Quản trị viên xem toàn bộ lịch sử xử lý, bao gồm ghi chú nội bộ (INTERNAL), và thực hiện gán hoặc chuyển người phụ trách ticket.

*Hình 5.22a Chi tiết xử lý và lịch sử yêu cầu (Admin — D02)*

*Hình 5.22b Biểu mẫu phân công nhân viên phụ trách (Admin — D03)*

### 5.5.5 Lịch sử gợi ý AI

Agent được giao ticket và Admin xem các lần tạo gợi ý, người yêu cầu, thời điểm và kết quả đã lưu. Người dùng chọn một lần tạo để đọc lại nội dung và bản chụp nguồn. Giao diện có các trạng thái đang tải, trống, lỗi và mất quyền.

*Hình 5.23a Danh sách các lần tạo gợi ý AI*

*Hình 5.23b Chi tiết gợi ý AI đã lưu*

### 5.5.6 Đánh giá gợi ý AI (P1)

Agent được giao ticket chọn Hữu ích hoặc Không hữu ích trên gợi ý ở trạng thái GENERATED hoặc APPLIED. Giao diện hiển thị lựa chọn đã lưu, cho phép đổi lựa chọn và thử lại khi lưu lỗi. Đánh giá không tự gửi phản hồi hoặc thay đổi trạng thái gợi ý. Admin không có thao tác đánh giá.

*Hình 5.24a Trạng thái đã lưu đánh giá hữu ích*

*Hình 5.24b Thông báo lỗi lưu đánh giá và thao tác thử lại*

### 5.5.7 Bỏ gợi ý và tiếp tục soạn thủ công

Người dùng xác nhận trước khi bỏ gợi ý ở trạng thái GENERATED. Sau khi bỏ, gợi ý chuyển sang DISCARDED và vẫn được lưu trong lịch sử; bản nháp được giữ nguyên, không có phản hồi nào được gửi. Nếu bản nháp đã được chèn từ gợi ý, người dùng phải chọn Tiếp tục soạn thủ công trước khi kiểm duyệt và gửi. Việc gửi thủ công không chuyển gợi ý đã bỏ thành APPLIED.

*Hình 5.25 Xác nhận bỏ gợi ý AI*

*Hình 5.26 Đã bỏ gợi ý AI và lựa chọn tiếp tục soạn thủ công*

### 5.5.8 Thống kê ticket (P1)

Admin xem tổng số ticket, phân bố theo trạng thái và người phụ trách hiện tại, cùng thời điểm lấy dữ liệu. Ticket chưa được giao hiển thị thành nhóm riêng; nhân viên đã vô hiệu hóa vẫn được giữ trong thống kê nếu còn ticket. Tổng các nhóm trong mỗi bảng bằng tổng số ticket. Giao diện hỗ trợ tải lại dữ liệu và có các trạng thái đang tải, không có dữ liệu, lỗi và không đủ quyền.

*Hình 5.27 Thống kê ticket theo trạng thái và người phụ trách*
