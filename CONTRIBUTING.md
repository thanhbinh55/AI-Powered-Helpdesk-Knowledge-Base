# Quy trình đóng góp

Group 04 — cập nhật 03/11/2026. Quy trình điều hành chi tiết ở [TEAM_GUIDE_TEMPLATE1.md](TEAM_GUIDE_TEMPLATE1.md), baseline scope/deadline ở [kế hoạch](PLAN_TEMPLATE1_AND_DEVELOPMENT.md), contract ở [MVP_CONTRACTS](reports/MVP_CONTRACTS.md).

## Git và task

- Không commit trực tiếp main; dùng PR. Branch protection/quyền thực tế phải được xác minh, không mặc định đã bật.
- Cấu hình tên/email tác giả thật và `git config core.hooksPath .githooks` trên máy cá nhân. Không chỉnh lịch sử hoặc tạo commit rỗng để làm đẹp đóng góp.
- Nhánh `docs/t1-<module>-<ten>`, `feat/<module>-<feature>`, `test/<module>-<scenario>`; tên module identity/ticket/knowledge/ai, không đảo A–D.
- Commit Conventional Commits với Jira key thật ở cuối khi đã có ánh xạ. Hook hiện tại chỉ kiểm tra có chuỗi SCRUM-số, không xác minh issue tồn tại hoặc cả cú pháp.
- Jira theo dõi trạng thái; GitHub issue/PR giữ bằng chứng. Ref CSV → Jira key → GitHub issue phải đối chiếu; không suy số issue theo số Jira. Task có thể có nhiều PR nhỏ theo dependency, mỗi PR phải chỉ rõ phạm vi và task liên quan.

## Review và merge

Bình review Lãm; Lãm review Gia Phúc; Gia Phúc review Quý Phúc; Quý Phúc review Bình. Release của Lãm được Gia Phúc kiểm tra độc lập. Contract/schema liên module cần owner phía nhận tham gia.

Mỗi PR dùng template hiện hành: requirement/test IDs, expected/actual, command hoặc nguồn đối chiếu, một happy path và một nhánh lỗi có ý nghĩa. NOT RUN nếu chưa chạy; không approve chỉ vì đủ dòng/checklist. Reviewer nêu việc đã kiểm tra, không bắt số comment.

Merge bởi người có quyền thực tế, khác tác giả, sau review/checks phù hợp. Không bắt Bình duyệt lại mọi PR; nếu chỉ Bình có quyền thì Bình xử lý thao tác merge trên review đã đủ. Squash giữ mã task thật và link PR/tác giả; giữ PR/Docs vì main không còn mọi commit gốc. Done cần sản phẩm/DoD và bằng chứng được reviewer chấp nhận, không chỉ PR đã merge.

## Mốc và bảo mật

03–08/11 hoàn tất tài liệu/mockup/review/đóng gói; code chỉ từ 09–22/11; QA 23–29/11. Mỗi task một owner, dependency/reviewer, deadline và đầu ra rõ ràng. CSV import chỉ create, không update issue cũ; không xóa cache để tạo lại.

AI log theo người trong [reports/ai-usage](reports/ai-usage/README.md), Lãm tổng hợp; không xóa lịch sử hay xác nhận kiểm chứng thay tác giả. Không commit secrets, `.env`, PII; `.env.example` chỉ chứa placeholder. Tất cả bảo vệ quyền thực hiện server-side; hợp đồng/schema ở SRS và MVP_CONTRACTS phải cập nhật cùng caller/fake/tests.
