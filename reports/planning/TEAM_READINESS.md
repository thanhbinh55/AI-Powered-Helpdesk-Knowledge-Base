# Bảng sẵn sàng nhận việc và blocker

> Baseline rà soát 03/11/2026. Chỉ phản ánh bằng chứng trong repo, chưa kiểm tra Jira/Docs/Figma/cổng. Không mặc định thành viên chưa làm ở nơi khác. Owner cập nhật trạng thái/link thật khi nhận task; bảng này không thay trạng thái Jira.

Nguồn: [task cards](../../TASK_PLAYBOOK_TEMPLATE1.md), [kế hoạch](../../PLAN_TEMPLATE1_AND_DEVELOPMENT.md), [CSV](../../scripts/jira/tasks_template1.csv).

## 1. Thông tin cần xác nhận trước khi phân công được coi là cam kết

| Thông tin | Owner cung cấp | Hạn | Trạng thái / bằng chứng |
|---|---|---|---|
| Rubric/template1 gốc và danh mục/định dạng sơ đồ | Bình | 04/11 | UNVERIFIED; cần link/path + phiên bản |
| Link Docs chung, quyền thành viên và snapshot chuẩn | Bình | 04/11 | **VERIFIED:** [[SE - Nhóm 4] template1 - Google Docs](https://docs.google.com/document/d/1vSMrk5GCPtOlhbWMRMqZvDq8575tSIz2IXgcp-K0WAg/edit?tab=t.0) |
| Figma file/prototype chung, quyền export/view | Quý Phúc; Bình hỗ trợ quyền | 04/11 | **VERIFIED:** [SE – Figma (Node 49:58 - Redesign v2)](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev) & 151 ảnh PNG tại `docs/design/anh/` |
| Git/Jira usernames, quyền review/merge và ref → issue keys | Bình; từng người xác nhận | 04/11 | UNVERIFIED; không suy Jira key từ ref hoặc số GitHub Issue |
| Tên gói, hạn/timezone/giới hạn nộp và tài khoản có quyền | Bình; Gia Phúc dự phòng | 04/11 | UNVERIFIED; SRS A.2 hiện ghi15/11 00:00, cần đối chiếu cổng |
| Embedding model/dimension/corpus mode/quota | Lãm + Quý Phúc | 10/11 12:00 | OPEN DEC-06, task T1-EMBED-01; secrets không đưa vào bảng |
| Template 2/3: mẫu nội dung đã được cung cấp; giờcổng/rubricchi tiết | Bình xác minh; Lãm nhận | 09/11 phần mẫuUI; trước nộp kiểmgiờ | Mẫu2=Thiết kế/3=Kiểm thử đã có reports/references; cần xác nhận mụcUI, giờ/tênzip, không đợi23/11 mới thiết kế |

## 2. Xác nhận đã nhận task

Mỗi thành viên chỉ cần xác nhận đã hiểu phạm vi, đầu ra, deadline, reviewer và người nhận bàn giao; không yêu cầu kê khai giờ làm.

| Người | Đã nhận/hiểu task | Đầu vào hoặc quyền còn thiếu | Blocker cần xử lý | Xác nhận/ngày |
|---|---|---|---|---|
| Bình | Chưa xác nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa có |
| Gia Phúc | Chưa xác nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa có |
| Lãm | Chưa xác nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa có |
| Quý Phúc | Chưa xác nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa có |

## 3. Những sản phẩm hiện chưa có bằng chứng nghiệm thu trong repo

| Nhóm | Bằng chứng hiện thấy | Owner bổ sung | Cách đóng mục |
|---|---|---|---|
| Template 1 | Có file khung; chưa đủ UC chi tiết, SVG/drawio/mockup/link thật | DOC owners; Lãm tổng hợp | PR reviewer approve, artifact thật và kiểm tra trực quan |
| Input mapping/module và mockup | Mới tạo mẫu inputs/<ten>.md, chưa xác nhận dữ liệu | Từng owner | Mapping05/11 và link/ảnh06/11; Gia Phúc/Quý Phúc nhận |
| Backend/schema/CI/API contract chạy thật | Có thiết kế/README; chưa có nghiệm thu ứng dụng | DEV/CONTRACT/SCHEMA/CI owners | Log chạy/PR/test theo các gate09–22/11 |
| Source provider/model và chất lượng AI | DEC-06 OPEN; chưa có kết quả live/evaluation | Lãm + Quý Phúc | Decision10/11, smoke19/11, evaluation23–28/11 |
| Gói nộp/biên nhận Template 1 | Chưa có gói đã duyệt/biên nhận được xác minh | Lãm → Gia Phúc → Bình | PUB20:00 và SUBMIT21:00 08/11 |
| Test/E2E/OPS/QA | Báo cáo đang NOT RUN/chưa có artifact ứng dụng | Từng test owner, Gia Phúc điều phối | Expected/actual, command/mode, artifact, reviewer |

Không biến bảng này thành lời khẳng định thành viên chưa bắt đầu công việc; khi có tiến độ ngoài repo cần đưa link/phiên bản/bằng chứng vào task. Không đánh Done chỉ vì có văn bản kế hoạch.

## 4. Nhật ký blocker và bàn giao

| Ngày/giờ | Task / artifact cần | Người đang chờ | Người phải giao | Hạn cần | Việc vẫn làm được | Phương án/giờ kiểm tra lại | Link bằng chứng / trạng thái |
|---|---|---|---|---|---|---|---|
| Chưa ghi nhận blocker live | — | — | — | — | — | — | Không đồng nghĩa không có blocker |

Khi thiếu input: ghi rõ artifact thay vì “đang chờ bạn”; ping owner trong kênh nhóm của nhóm, kèm ref/deadline (bản rà soát này không tự gửi tin nhắn). Nếu quá mốc, báo Bình và người nhận ngay trước buổi làm tiếp theo, chốt phân công lại trong ngày. Thay fake bằng thật phải ghi phiên bản contract và kết quả chạy, không chỉ trạng thái Done.


## 5. Bổ sung sau khi nhận mẫu Template 2–3

- Đã có snapshot nội dung2/3 và đối chiếu tại[TEMPLATE2_3_ALIGNMENT](TEMPLATE2_3_ALIGNMENT.md). Các bước cũ coiTemplate 2làtest report bị thay, không chuyển mất phần thiết kế bắt buộc.
- Chưa có conceptual/architecture/data dictionary/UI artifacts củaTemplate 2 được nghiệmthu; taskT2 làm09–22, review/nộp23–28. Khung trongreports/template2 chưa làbài hoànthành.
- Đã có catalog25ca dựkiến, chưa có25specs chi tiết/actual được chạy: ownerTST điềntheoT3-CASE từ 09/11, không báoPassed. ≥30 câuAIevaluationriêng.
- Theo dõi task thiết kế/kiểm thử bằng deadline và sản phẩm bàn giao; báo blocker khi có nguy cơ trễ.
