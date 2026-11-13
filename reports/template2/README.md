# Template 2 — Thiết kế phần mềm

> Nguồn yêu cầu: [mẫu thiết kế](../references/template2-design-requirements.md). Owner release Lãm, reviewer Gia Phúc, Bình xác minh giờ/nộp. Nộp trước 29/11 theo người dùng; kế hoạch nội bộ nộp 28/11 23:59, không tự hiểu hạn 29 làcuốingày.

Luồng làm:09/11 dựngkhung/thiết kếnháp;12/11 conceptual/architecture;18/11 dictionary/ERD;20/11 UI;22/11 đối soátcode;23–25/11 review;26/11 freeze;27/11 kiểm gói;28/11 nộp. CodeMVP vẫn09–22/11. [Đối chiếu mẫu](../planning/TEMPLATE2_3_ALIGNMENT.md), [task cards](../../TASK_PLAYBOOK_TEMPLATE1.md).

| File | Owner điều phối | Người cung cấp nội dung |
|---|---|---|
| 01-contributions.md | Lãm | Từng người xác nhậnthật |
| 02-conceptual-model.md | Lãm | Bốnowner domain |
| 03-architecture.md | Bình | Bốnowner boundary/port |
| 04-data-design.md | Lãm | Mỗiowner bảng/migration mình |
| 05-ui-design.md | Quý Phúc | Mỗiowner màn hình mình, không vẽ lại tấtcả |
| 06-design-consistency.md | Gia Phúc | Findings vềđúngowner, Lãm tổng hợp |

Ảnh/source lưu assets/diagrams vàassets/ui, gói đãkiểm tra lưu release/ theo têncổng xác nhận. Các đường dẫn này là output dựkiến, chưa có source/ảnh/gói nghiệmthu. Nội dung cóTODO phải đượcowner hoànthiện trướcchốt, không coi khung làbàinộp. Bộhình Template 2 độc lập mục đích với sáuhìnhUseCase/Context củaTemplate 1, không có quy định sáuhình làđủ chocảTemplate 2.

Mẫu nhắcUI ởmục tiêu nhưng mục lục chỉđến4.2: dùngmục5UI đểbao phủ vàBình xác nhận cáchtrìnhbày; không tựbỏUI. Sơđồlớp/sequence làbổ sung khi giúpgiải thích, không mặcđịnh phảiđặc tả mọi lớp vì bài năm trước làmvậy. Testplan/cases thuộcTemplate 3, không đợiQA/evaluationđể nộp thiết kế.
