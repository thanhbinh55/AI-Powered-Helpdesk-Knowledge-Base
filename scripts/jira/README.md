# CÔNG CỤ TẠO NHIỆM VỤ JIRA HÀNG LOẠT (JIRA BULK CREATE)

Thư mục này chứa kịch bản Python hỗ trợ tự động tạo Epic và các Task cho dự án môn học trên Jira Cloud (REST API v3), phục vụ truy vết tiến độ và xét đóng góp cá nhân theo quy định của môn Nhập môn Công nghệ Phần mềm - HCMUS.

---

## 1. CÁC FILE TRONG THƯ MỤC
- `jira_bulk_create.py`: Kịch bản Python tự động hoá việc tạo issue trên Jira.
- `tasks_template0.csv`: Danh sách nhiệm vụ mẫu cho Template 0 (Project Proposal).
- `tasks_created.csv`: File cache tự động sinh lưu vết các `ref -> Jira key` đã tạo thành công để tránh tạo trùng khi chạy lại (đã nằm trong `.gitignore`).

---

## 2. CẤU HÌNH BIẾN MÔI TRƯỜNG
Tạo file `.env` tại thư mục gốc repository (sao chép từ `.env.example`) và điền các thông tin:
```bash
# Jira Cloud Integration
JIRA_BASE=https://your-domain.atlassian.net
JIRA_EMAIL=your_email@domain.com
JIRA_TOKEN=your_atlassian_api_token_here
JIRA_PROJECT=SCRUM
```

### Cách lấy Atlassian API Token:
1. Đăng nhập vào: https://id.atlassian.com/manage-profile/security/api-tokens
2. Nhấn **Create API token**.
3. Đặt nhãn (Label), ví dụ: `hcmus-helpdesk-token`.
4. Sao chép chuỗi token vừa tạo và dán vào biến `JIRA_TOKEN` trong `.env`.
> **CẢNH BÁO:** TUYỆT ĐỐI KHÔNG commit file `.env` hoặc token lên Git!

---

## 3. CẤU TRÚC FILE CSV (`tasks_template0.csv`)
File CSV gồm 8 cột chuẩn:
```csv
ref,type,summary,description,assignee_email,parent_ref,labels,duedate
```
- `ref`: Mã định danh nội bộ trong file (ví dụ: `T0`, `W-A`, `W-B`).
- `type`: Loại issue (`Epic`, `Task`, `Bug`...). Lưu ý dòng `Epic` phải nằm trước các `Task` trực thuộc.
- `summary`: Tiêu đề ngắn gọn của công việc.
- `description`: Nội dung mô tả chi tiết và chỉ dẫn nguồn nguyên liệu (Phụ lục trong `SRS-master.md`). Kịch bản sẽ tự chuyển đổi sang định dạng ADF (Atlassian Document Format) của Jira API v3.
- `assignee_email`: Email tài khoản Jira của người được giao. Trước khi chạy thật, thay `<email_A>` ... `<email_D>` bằng email tài khoản Atlassian của 4 thành viên.
- `parent_ref`: Mã `ref` của Epic cha (ví dụ: `T0`). Kịch bản sẽ tự động ánh xạ sang Jira Key vừa tạo (ví dụ: `SCRUM-1`).
- `labels`: Các nhãn gắn với task, phân tách bằng dấu chấm phẩy `;` (ví dụ: `DOC;REQ`).
- `duedate`: Hạn hoàn thành định dạng `YYYY-MM-DD`.

---

## 4. HƯỚNG DẪN SỬ DỤNG

### Bước 1: Cài đặt thư viện requests (tùy chọn nhưng khuyến nghị)
Kịch bản hỗ trợ sẵn cả thư viện chuẩn `urllib` và `requests`. Để có trải nghiệm tốt nhất:
```bash
pip install requests
```

### Bước 2: Chạy thử nghiệm ở chế độ mô phỏng (--dry-run)
Chế độ này kiểm tra tính hợp lệ của file CSV, logic liên kết Epic-Task và chuyển đổi ADF mà **KHÔNG gọi API thật** và **KHÔNG cần kết nối mạng**:
```bash
python3 scripts/jira/jira_bulk_create.py --dry-run
```

### Bước 3: Tạo issue thực tế trên Jira Cloud
Khi đã cấu hình đầy đủ file `.env` và cập nhật email thành viên trong CSV:
```bash
python3 scripts/jira/jira_bulk_create.py
```

### Bước 4: Thêm issue vào Sprint (tùy chọn)
Nếu bạn đã tạo sẵn Sprint trên Scrum Board (ví dụ Sprint 1 có ID là `12`):
```bash
python3 scripts/jira/jira_bulk_create.py --sprint-id 12
```

---

## 5. CƠ CHẾ CHỐNG TẠO TRÙNG LẶP (IDEMPOTENCY)
Mỗi khi tạo thành công một issue, kịch bản sẽ ghi một dòng `ref,key` vào file `tasks_created.csv`. Trong những lần chạy tiếp theo, các dòng có `ref` đã xuất hiện trong file này sẽ tự động được bỏ qua (`[BỎ QUA]`), giúp bạn an tâm chạy lại nhiều lần mà không sợ sinh trùng lặp task trên Jira.


## Backlog Template 1 và MVP — baseline 03/11/2026

Dùng file `tasks_template1.csv`: tài liệu chốt 08/11, code/test 09–22/11. Schema vẫn tám cột; description chứa start/dependency/reviewer/DoD. `ref` là định danh ổn định, không phải Jira key; mã mới chỉ biết sau khi tạo thật. Các task test/schema/CI/contract/ops đã tách owner, xem kế hoạch và TEAM_GUIDE.

```bash
python3 scripts/jira/jira_bulk_create.py --csv scripts/jira/tasks_template1.csv --dry-run
```

**Script chỉ tạo issue; không cập nhật issue đã có.** Ref trong cache bị bỏ qua, nên sửa CSV không đổi deadline, assignee hoặc description trên Jira. Phải đối chiếu cache/ref với issue thật rồi cập nhật issue cũ riêng; không xóa cache để import lại. Cache không thay thế bảng liên kết Jira–GitHub; số GitHub Issue không tự bằng số Jira. Dry-run mô phỏng không xác minh account/permission trên Jira, và không phải bằng chứng board đã cập nhật.

Baseline file giữ phạm vi/deadline; Jira theo dõi trạng thái; GitHub PR giữ bằng chứng. Không chạy live/cập nhật board hoặc gửi thông báo nếu chưa được yêu cầu. Quyền repo phải được nhóm xác nhận.


## Cách giao task sau rà soát khả năng nhận việc

[Task cards](../../TASK_PLAYBOOK_TEMPLATE1.md) và CSV cùng có nguồn đọc theo mục, bước làm, output, người nhận và gate bắt đầu/chốt. CSV vẫn tám cột, description có newline; importer chuyển mỗi dòng thành paragraph ADF. Dependency nêu theo artifact/mốc, không máy móc đợi toàn task upstream Done.

Giữ các ref cũ; bổ sung READY/EMBED/SUBMIT/WF và Epic QA1 cùng ba task QA. T1 chốt22/11, QA1 đến29/11. Issue cũ cần cập nhật description/deadline/assignee riêng theo key thật; dry-run không làm việc đó. Lưu snapshot/biên nhận trong task, không tự đánh công việc ngoài repo đã xong.

## Mẫu Template 2–3 mới: điều chỉnh phân công

Template 2=Thiết kế, làm song song09–22/11, review/nộp23–28 trước mốc29; Template 3=Kiểm thử, ≥5 chức năng×5ca. Thêm Epic T2 vàT3/các task thiết kế/cases/release; giữ ref QA1-T2-01 nhưng đổi parent T2/summary/description từ test report sang release thiết kế. Script create không update issue cũ, nên không xóa cache/tạo trùng; update issue thật cần đối chiếu key. QA1 chỉ regression/evaluation choTemplate 3, không làgate chờ nộp Template 2.
