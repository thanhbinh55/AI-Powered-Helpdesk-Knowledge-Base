# BÁO CÁO KẾT QUẢ KIỂM THỬ (TEST EXECUTION RESULTS)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Mã nhóm:** Group 04  
> **Môn học:** Nhập môn Công nghệ Phần mềm - HCMUS

---

## THÔNG TIN TÀI LIỆU
- **Tiêu đề (Title):** Test Execution Results & Defect Summary
- **Phiên bản (Version):** 1.0.0-draft
- **Ngày tạo (Date):** 2026-10-19
- **Tác giả & Đóng góp (Authors + Contributions):**
  - `24120121` - `Lê Quý Phúc`: Kết quả test Module A (AI Suggestion; Analytics P1 chưa nhận)
  - `24120083` - `Nguyễn Đức Lãm`: Kết quả test Module B (Knowledge Base & Vector Search)
  - `24120503` - `Phan Gia Phúc`: Kết quả test Module C (Tickets & Messages)
  - `24120269` - `Ngô Viết Thanh Bình`: Kết quả test Module D (Auth & Users) *(Nhóm trưởng)*
- **Phạm vi (Scope):** Tổng hợp số lượng test cases thực thi, tỷ lệ pass/fail, độ bao phủ mã (Coverage) và danh sách lỗi phát hiện trong quá trình kiểm thử.

---

## 1. TỔNG HỢP KẾT QUẢ KIỂM THỬ (SUMMARY)
| Phân hệ / Module | Tổng số Test Cases | Passed | Failed | Skipped | Độ bao phủ (Coverage) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Module A (AI Assistance)** | NOT RUN | 0 | 0 | 0 | Chưa đo |
| **Module B (Knowledge Base)** | NOT RUN | 0 | 0 | 0 | Chưa đo |
| **Module C (Ticket & Helpdesk)** | NOT RUN | 0 | 0 | 0 | Chưa đo |
| **Module D (Auth & Users)** | NOT RUN | 0 | 0 | 0 | Chưa đo |
| **TỔNG CỘNG** | **0** | **0** | **0** | **0** | **Chưa đo** |

**Chưa có bằng chứng chạy test ứng dụng trong bản cập nhật tài liệu này.** NOT RUN/coverage chưa đo không có nghĩa đã chạy và fail, cũng không có nghĩa pass. Gia Phúc tổng hợp từ task test riêng của từng owner; Lãm clean-environment smoke. Kế hoạch/ID test ở [05-test-plan.md](05-test-plan.md) và [SRS 14.2](SRS-master.md).

Mỗi lần chạy cần ghi thời điểm, command, commit/PR, mode mock/live, dataset/model/dimension khi có, expected/actual và link artifact. Kiểm tra CSV/dry-run Jira chỉ là kiểm tra kế hoạch, không phải kết quả test ứng dụng.

---

## 2. NHẬT KÝ THEO DÕI LỖI (DEFECT LOG)
| Mã Lỗi (Defect ID) | Tiêu đề lỗi | Module | Mức độ | Người phát hiện | Trạng thái | Jira Bug Key |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *Chưa có lỗi ghi nhận trong giai đoạn khởi tạo cấu trúc dự án* | - | - | - | - | - | - |

---

## TÀI LIỆU THAM KHẢO (REFERENCES)
1. Kế hoạch kiểm thử: `reports/05-test-plan.md`.
2. Tài liệu đặc tả tổng thể: `reports/SRS-master.md`.

---

## NHẬT KÝ THAY ĐỔI (CHANGE LOG)
| Phiên bản | Ngày | Người sửa | Nội dung thay đổi | Mã Task Jira |
| :--- | :--- | :--- | :--- | :--- |
| `0.1.0` | 2026-10-19 | DevOps Engineer | Khởi tạo bảng biểu kết quả kiểm thử | SCRUM-6 |
