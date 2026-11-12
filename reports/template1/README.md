# Gói nộp Template 1 — Clarune — Nhóm 04

- `report/Report.pdf`: bản final do trưởng nhóm xuất từ Google Docs, là nguồn chuẩn về nội dung.
- `report/report.md`: bản Markdown đã đối chiếu với PDF final; ảnh dùng đường dẫn tương đối vào `report/assets/`.
- Các file mục 01–05 và `TEMPLATE1_DRAFT_MASTER.md`: bản trích đồng bộ từ report hiện hành, không còn là khung chờ soạn.
- `report/assets/ui/`: chỉ 31 ảnh giao diện có trong report, giữ nguyên tệp ảnh nguồn theo mã Figma.
- `report/assets/diagrams/`: 6 sơ đồ SVG sắc nét và mã nguồn drawio tương ứng; Hình 3.1 giữ nguyên bản Lãm nộp, 5 sơ đồ Use Case chỉnh theo bản final.
- `ai-usage/ai-usage.md` và `.html`: tổng hợp theo tác giả, đánh số phiên thống nhất và áp dụng các hiệu chỉnh do trưởng nhóm xác nhận; giữ nguồn gốc để đối soát.
- `git-contributions/git-contributions.md` và `.html`: snapshot lịch sử Git Template 1, gồm cả nhánh nộp bài chưa merge. Nhóm nhiều tệp được gom thành thư mục kèm số lượng; danh sách đầy đủ giữ trong sources/git-snapshot.json.
- `sources/`: bản final gốc có ảnh nhúng, draft dùng tra mã ảnh, nguyên bản nhật ký theo người và snapshot metadata Git; dùng đối soát, không thay thế nội dung report.

**PDF report:** dùng đúng tên `report/Report.pdf` (phân biệt chữ hoa/thường). Công cụ không tạo hoặc sửa PDF. Việc có PDF không phải bằng chứng đã nộp lên cổng trường.

## Nguồn và quy ước trình bày

- Nguồn chuẩn là `report/Report.pdf`. Bản chữ đã đối chiếu dùng để đóng gói là `sources/template1-final-current.md`; SHA-256 và các quyết định đồng bộ nằm tại `sources/report-baseline.json`.
- `sources/template1-final-original.md`, `sources/TEMPLATE1_DRAFT_MASTER.md`, các bản trong `sources/history/` và bản xuất Markdown `(1).md` là nguồn lưu trữ trước khi chốt; không dùng ghi đè nội dung hiện hành.
- AI usage đã thu thập của cả 4 thành viên. Gia Phúc đã nộp cả dòng tổng hợp T1-08 và phần chi tiết mục 6.3 tại commit 3eb4181; giữ nguyên nội dung tác giả đã nộp.
- Bản nộp dùng mã phiên duy nhất T1-01…T1-22 theo nhóm thành viên. Bảng và phần chi tiết khớp từng mã; bảng ánh xạ mã gốc nằm tại sources/ai-session-index.json. Nguồn lưu trữ giữ nguyên mã ban đầu.
- Trưởng nhóm xác nhận 8 phiên của Lãm diễn ra 09–11/11/2026; bản nộp đã sửa tháng 10 thành tháng 11, nguyên bản lưu trữ giữ nguyên. Hai phiên Codex ngày 12/11 chỉ ghi ngày và tên công cụ theo xác nhận của trưởng nhóm.
- Các PR nguồn chưa được tác vụ đóng gói này merge vào main; trạng thái ghi trong báo cáo Git là trạng thái tại snapshot. Nhánh docs/t1-ticket-giaphuc đã có 5 commit của Gia Phúc; tại lần thu thập chưa thấy PR tương ứng. Snapshot ban đầu được lưu ở sources/history/git-snapshot-initial.json.
- Mục lục Markdown đã bỏ số trang từ Google Docs theo yêu cầu trưởng nhóm; giữ nguyên tên mục và liên kết đến nội dung.
- Ảnh hồ sơ trong bản final là `62-8328.png`; draft nêu cả `62-8216` và `62-8328`, chỉ lấy ảnh thực sự xuất hiện trong final.
- Tệp `report/assets/manifest.json` ghi đủ 37 ánh xạ hình và SHA-256, trong đó 1 sơ đồ bối cảnh lấy nguyên tệp của Lãm, 5 sơ đồ Use Case được dựng lại và 31 hình UI sao chép nguyên tệp.

## Quy tắc sơ đồ

Hình 3.1 dùng nguyên văn SVG/drawio của Lãm tại commit 979179b, theo lựa chọn của trưởng nhóm; không vẽ lại hoặc thêm actor Mail Service. Sơ đồ thể hiện P0; đoạn giải thích bên dưới hình dẫn dịch vụ Email P1 tới UC-16 và sơ đồ Định danh và phân quyền. Nguồn được lưu tại sources/diagrams cùng SHA-256. Năm sơ đồ Use Case còn lại dựa vào graph của các tệp drawio hiện có; cập nhật tên Use Case theo 19 bảng đặc tả final. Người dùng là actor người que, Use Case là ellipse bên trong ranh giới hệ thống, actor/dịch vụ ngoài ranh giới. Association nét liền không mũi tên; generalization nét liền với tam giác rỗng hướng về actor cha. Không tự thêm include/extend. Worker, CSDL và storage là thành phần nội bộ, không vẽ thành actor. Các mô tả P1 và quyền hạn được đối chiếu với bản final.

Sơ đồ tổng thể và module dùng cùng nguồn tên UC và quan hệ; thay tên lỗi của graph tổng thể cũ (đặc biệt UC-07..10), sửa generalization Admin→Authenticated User bị thiếu target trong mã cũ, giữ UC-19 riêng cho Agent và UC-17 riêng cho Admin. Bản vẽ gốc vẫn còn nguyên ở thư mục assets/diagrams cũ; gói nộp trỏ tới bản đã chỉnh trong report/assets/diagrams.

## Tạo lại và kiểm tra

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/template1/requirements.txt
.venv/bin/python scripts/package_template1.py --report-only
.venv/bin/python scripts/verify_template1.py
```

Kiểm tra thêm bố cục bằng trình duyệt (tùy chọn): cài `playwright`, sau đó chạy `python scripts/verify_template1.py --browser`; cần Chrome/Chromium cục bộ.

Lệnh `--report-only` cập nhật report, các mục 01–05, master và metadata mà không tạo lại nhật ký AI hoặc lịch sử Git. Chạy không có cờ này chỉ khi cần tạo lại cả gói. Khi PDF thay đổi, đối chiếu và cập nhật `sources/template1-final-current.md` cùng `sources/report-baseline.json` trước khi chạy; không sửa nguồn tác giả lưu trữ. Snapshot Git được cố định để việc render lại không thay số liệu. Muốn chốt snapshot mới, lưu lại snapshot cũ trước khi cập nhật. HTML dùng kiểu bìa, Times New Roman, A4, header/footer của Template 0; nội dung được đọc đầy đủ từ Markdown, không dùng các trường hợp hard-code commit/phiên của Template 0.

Bản nguồn lưu trữ giữ nguyên cả khoảng trắng và Markdown hard-break của tác giả; không tự sửa các dòng này để làm sạch diff. Kết quả kiểm tra nội dung/ảnh nằm ở `verification.json`, kiểm tra HTML ở `browser-validation.json`.
