# Gói nộp Template 1 — Clarune — Nhóm 04

- `report/report.md`: toàn bộ bản final xuất từ Google Docs, giữ nguyên câu chữ; ảnh dùng đường dẫn tương đối vào `report/assets/`.
- `report/assets/ui/`: chỉ 31 ảnh giao diện có trong report, giữ nguyên tệp ảnh nguồn theo mã Figma.
- `report/assets/diagrams/`: 6 sơ đồ SVG sắc nét và mã nguồn drawio tương ứng, chỉnh theo bản final.
- `ai-usage/ai-usage.md` và `.html`: tổng hợp theo tác giả, giữ nguyên nội dung các phiên đã nộp.
- `git-contributions/git-contributions.md` và `.html`: snapshot lịch sử Git Template 1, gồm cả nhánh nộp bài chưa merge.
- `sources/`: bản final gốc có ảnh nhúng, draft dùng tra mã ảnh, nguyên bản nhật ký theo người và snapshot metadata Git; dùng đối soát, không thay thế nội dung report.

**PDF report:** trưởng nhóm tự xuất từ Google Docs và đặt tại `report/report.pdf`. Công cụ này không tạo hoặc giả lập PDF đã nộp.

## Nguồn và các điểm cần xác nhận

- Bản chữ duy nhất dùng đóng report là `sources/template1-final-original.md`; không lấy draft hoặc nội dung PR ghi đè bản final.
- AI usage đã thu thập của Bình, Lãm và Quý Phúc. Chưa tìm thấy bản Template 1 của Gia Phúc; bản tổng hợp ghi đúng trạng thái này, không suy diễn thành “không dùng AI”.
- Các mã phiên T1-08… bị trùng giữa tác giả được giữ nguyên, đặt dưới tên tác giả để không đổi dữ liệu nguồn.
- Ngày 09–11/10/2026 trong nhật ký Lãm được giữ nguyên theo bản đã nộp, chưa có xác nhận đổi sang tháng 11.
- Các PR nguồn #10/#11/#12 chưa được tác vụ đóng gói này merge vào main; trạng thái ghi trong báo cáo Git là trạng thái tại snapshot.
- Markdown gốc có mục lục kèm số trang từ Google Docs. Giữ nguyên các nhãn/số trang theo yêu cầu bảo toàn nội dung; đây không phải số trang do Markdown tự tính.
- Ảnh hồ sơ trong bản final là `62-8328.png`; draft nêu cả `62-8216` và `62-8328`, chỉ lấy ảnh thực sự xuất hiện trong final.
- Tệp `report/assets/manifest.json` ghi đủ 37 ánh xạ hình và SHA-256, trong đó 6 hình là sơ đồ được dựng lại, 31 hình là UI sao chép nguyên tệp.

## Quy tắc sơ đồ

Dựa vào graph của các tệp drawio hiện có; cập nhật tên Use Case theo 19 bảng đặc tả final. Người dùng là actor người que, Use Case là ellipse bên trong ranh giới hệ thống, actor/dịch vụ ngoài ranh giới. Association nét liền không mũi tên; generalization nét liền với tam giác rỗng hướng về actor cha. Không tự thêm include/extend. Worker, CSDL và storage là thành phần nội bộ, không vẽ thành actor. Các mô tả P1 và quyền hạn được đối chiếu với bản final.

Sơ đồ tổng thể và module dùng cùng nguồn tên UC và quan hệ; thay tên lỗi của graph tổng thể cũ (đặc biệt UC-07..10), sửa generalization Admin→Authenticated User bị thiếu target trong mã cũ, giữ UC-19 riêng cho Agent và UC-17 riêng cho Admin. Bản vẽ gốc vẫn còn nguyên ở thư mục assets/diagrams cũ; gói nộp trỏ tới bản đã chỉnh trong report/assets/diagrams.

## Tạo lại và kiểm tra

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/template1/requirements.txt
.venv/bin/python scripts/package_template1.py
.venv/bin/python scripts/verify_template1.py
```

Kiểm tra thêm bố cục bằng trình duyệt (tùy chọn): cài `playwright`, sau đó chạy `python scripts/verify_template1.py --browser`; cần Chrome/Chromium cục bộ.

Không sửa thủ công nguồn trong `sources/` nếu chưa có bản nộp mới của tác giả. Snapshot Git được cố định để việc render lại không thay số liệu. Muốn chốt snapshot mới, lưu lại snapshot cũ trước khi cập nhật. HTML dùng kiểu bìa, Times New Roman, A4, header/footer của Template 0; nội dung được đọc đầy đủ từ Markdown, không dùng các trường hợp hard-code commit/phiên của Template 0.

Bản nguồn lưu trữ giữ nguyên cả khoảng trắng và Markdown hard-break của tác giả; không tự sửa các dòng này để làm sạch diff. Kết quả kiểm tra nội dung/ảnh nằm ở `verification.json`, kiểm tra HTML ở `browser-validation.json`.
