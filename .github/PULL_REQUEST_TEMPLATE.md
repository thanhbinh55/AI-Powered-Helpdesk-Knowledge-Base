## Vấn đề và kết quả

<!-- Trigger, hành vi trước/sau hoặc nội dung tài liệu được sửa. Không tick mục chưa làm. -->

- Task ref / Jira key đã xác minh:
- Jira link:
- GitHub issue thật (nếu có): Closes #...
- FR / US (SRS Phụ lục D) / UC / BR / TC liên quan:
- Owner / reviewer / owner phía nhận contract:

## Phạm vi

- [ ] identity
- [ ] ticket / workflow
- [ ] knowledge / EmbeddingProvider
- [ ] ai
- [ ] Tài liệu / mockup / quy trình
- [ ] Schema / CI / môi trường

<!-- Chỉ đánh dấu phạm vi thay đổi thực tế. A–D không dùng làm định danh module. -->

## Bằng chứng kiểm tra

| Kịch bản | Command / fixture / trang đối chiếu | Expected | Actual / PASS / FAIL / NOT RUN |
|---|---|---|---|
| Happy path có ý nghĩa | | | |
| Nhánh lỗi / quyền / state | | | |

- Mode: fake / mock embedding / live (chọn đúng); dataset/model/dimension nếu có:
- CI checks đã chạy và link kết quả (nếu chưa cấu hình, ghi chưa có):
- Với Docs: actor, trigger/precondition, luồng thay thế/hậu điều kiện, BR và mockup đã đối soát:
- Với UI/API: screenshot / JSON success, empty, error; adapter có đổi không:
- Reviewer ghi điều đã kiểm tra và kết quả, không chỉ Approve hoặc tick checklist. NOT RUN cần nêu phần còn thiếu, không suy PASS từ build.

## Schema / contract / quyền

- Migration mới, version/dependency, kiểm tra fresh DB và upgrade (hoặc không áp dụng):
- Thay đổi DTO/error/enum/port; fake/caller/OpenAPI đã đồng bộ (hoặc không áp dụng):
- Authorization/ownership/reassign/disabled; rollback/concurrency và internal note (hoặc không áp dụng):
- Nếu send suggestion: same ticket, GENERATED, quyền hiện tại, PUBLIC; message+APPLIED cùng transaction, double-send/send-discard và rollback:
- Không commit secrets/PII; không đưa internal note vào Customer DTO/prompt; log lỗi đã khử dữ liệu nhạy cảm:

## Truy vết và review

- AI Usage: link log cá nhân/phiên, điều AI tạo và kiểm chứng thực tế; không xác nhận thay người chưa kiểm tra.
- Nội dung còn thiếu / blocker / P1 hoãn:
- Reviewer mặc định: Bình review Lãm; Lãm review Gia Phúc; Gia Phúc review Quý Phúc; Quý Phúc review Bình. Release Lãm do Gia Phúc kiểm tra. Contract liên module cần owner phía nhận.
- Merge bởi người có quyền thực tế, khác tác giả, sau review/checks. Không mặc định branch protection đã bật hoặc mọi PR phải chờ Bình duyệt lại. Giữ liên kết task/PR/tác giả nếu squash.
