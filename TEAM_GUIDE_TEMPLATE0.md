# 🚀 HƯỚNG DẪN THỰC HIỆN ĐỀ XUẤT ĐỒ ÁN (TEMPLATE 0)
> **Dự án:** AI-Powered Helpdesk & Knowledge Base  
> **Nhóm:** Group 04 — Môn học: Nhập môn Công nghệ Phần mềm (HCMUS)  
> **Thời hạn hoàn thành:** **23:59 ngày 29/10/2026**

---

## 📌 1. BẢNG PHÂN CÔNG CÔNG VIỆC CHI TIẾT

| Thành viên | Phân hệ (Module) | Mã Task Jira | Phần việc chính phụ trách | Nguồn tài liệu (`reports/SRS-master.md`) |
| :--- | :--- | :---: | :--- | :--- |
| **Lê Quý Phúc**<br>`24120121` | **Module A**<br>AI Assistance | **`SCRUM-8`** | - Trang Bìa<br>- Mục 1: Bảng đánh giá thành viên<br>- Mục 2: Phát biểu bài toán sơ lược<br>- Mục 3.2: Phần cứng | Phụ lục A, C, F *(chỉ viết mức sơ lược, không sao chép nguyên văn)* |
| **Phan Gia Phúc**<br>`24120503` | **Module C**<br>Ticket Management | **`SCRUM-9`** | - Mục 3.1.1: Danh sách các chức năng phần mềm (User Stories) | Phụ lục D *(bảng câu chuyện người dùng, kèm quy định liên quan)* |
| **Nguyễn Đức Lãm**<br>`24120083` | **Module B**<br>Knowledge Base | **`SCRUM-10`** | - Mục 3.1.2: Kiến trúc tổng thể phần mềm<br>- Mục 4: Kế hoạch phát triển (5 giai đoạn) | Phụ lục E và Phụ lục G *(lấy chuẩn ngày tháng)* |
| **Ngô Viết Thanh Bình**<br>`24120269` *(Lead)* | **Module D**<br>Identity & Access | **`SCRUM-11`** | - Mục 5.1: Cấu trúc nhân sự<br>- Mục 5.2: Kế hoạch chi phí dự án | Phụ lục H và Phụ lục I |

---

## 📅 2. MỐC THỜI GIAN & DEADLINE NỘI BỘ

| Giai đoạn | Nội dung | Hạn chót | Lưu ý |
| :--- | :--- | :---: | :--- |
| **1. Soạn thảo** | Mỗi bạn hoàn thành bản nháp phần mình | **23/10/2026** | Commit lên nhánh cá nhân, mở Pull Request |
| **2. Review chéo** | Đọc và nhận xét chéo bài của đồng đội | **26/10/2026** | Comment trực tiếp trên GitHub PR hoặc Jira |
| **3. Chỉnh sửa** | Tiếp thu nhận xét và hoàn thiện nội dung | **27/10/2026** | Đẩy bản sửa đổi lên lại nhánh |
| **4. Hợp nhất** | Rà soát tính nhất quán số liệu & format | **28/10/2026** | Nhóm trưởng rà soát lần cuối và merge |
| **5. Nộp bài** | Đóng gói `Group04.zip` và nộp bài | **29/10/2026** | Kiểm tra $\le 20$ files và $\le 20$ MB |

> **Quy tắc review chéo vòng tròn:**  
> `Quý Phúc` review cho `Gia Phúc` $\to$ `Gia Phúc` review cho `Đức Lãm` $\to$ `Đức Lãm` review cho `Thanh Bình` $\to$ `Thanh Bình` review cho `Quý Phúc`.

---

## 🛠️ 3. QUY TRÌNH 5 BƯỚC THỰC HIỆN (BẮT BUỘC)

### Bước 1: Clone Repository & Cấu hình Git môi trường cá nhân
Chạy lần lượt các lệnh sau trong Terminal (chỉ làm 1 lần đầu tiên):
```bash
# 1. Clone dự án về máy
git clone https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base.git
cd AI-Powered-Helpdesk-Knowledge-Base

# 2. Cài đặt Git Hook bắt buộc (Hook chặn commit nếu thiếu mã Jira)
git config core.hooksPath .githooks

# 3. Cấu hình đúng Username và Email khớp với members.csv (để tính điểm Git cá nhân)
git config user.name "<Git_Username_của_bạn>"
git config user.email "<Git_Email_của_bạn>"
```

*(Ví dụ cấu hình cho từng bạn):*
* **Lê Quý Phúc:**  
  `git config user.name "Shinkiisme"`  
  `git config user.email "quyphuc0306@gmail.com"`
* **Phan Gia Phúc:**  
  `git config user.name "t4lf4n"`  
  `git config user.email "24120503@student.hcmus.edu.vn"`
* **Nguyễn Đức Lãm:**  
  `git config user.name "Lamnguyen-code"`  
  `git config user.email "lamnguyenduc0118@gmail.com"`

---

### Bước 2: Tạo nhánh (Branch) làm việc riêng
> ⚠️ **TUYỆT ĐỐI KHÔNG commit trực tiếp lên nhánh `main`!**

```bash
# Luôn lấy code mới nhất từ main
git checkout main
git pull origin main

# Tạo nhánh riêng theo mã task Jira của bạn:
# - Quý Phúc:
git checkout -b docs/SCRUM-8-viet-muc-1-2

# - Gia Phúc:
git checkout -b docs/SCRUM-9-bang-chuc-nang

# - Đức Lãm:
git checkout -b docs/SCRUM-10-kien-truc-ke-hoach
```

---

### Bước 3: Soạn thảo nội dung & Ghi nhật ký sử dụng AI
1. Mở tệp `reports/00-project-proposal.md` và viết trực tiếp vào các mục thuộc phần mình được phân công.
2. Tham khảo các phụ lục tương ứng trong tệp `reports/SRS-master.md`.
3. ⚠️ **Nếu có dùng AI (ChatGPT, Gemini, Claude...):**  
   Mở tệp `reports/07-ai-usage.md`, thêm 1 dòng vào bảng với nội dung: *Ngày dùng, Công cụ, Mục đích, Cách kiểm tra và Tên bạn*. (Đây là yêu cầu bắt buộc của Giảng viên để đảm bảo liêm chính học thuật).

---

### Bước 4: Commit mã nguồn kèm mã Jira
Git hook sẽ kiểm tra định dạng commit. Thông điệp commit **bắt buộc phải kết thúc bằng mã Jira** của task:
```bash
# Thêm file đã sửa
git add reports/00-project-proposal.md reports/07-ai-usage.md

# Commit (Cú pháp: docs(proposal): <nội dung ngắn> SCRUM-<mã_task>)
# Ví dụ của Quý Phúc:
git commit -m "docs(proposal): hoan thien noi dung muc 1 va 2 SCRUM-8"

# Ví dụ của Gia Phúc:
git commit -m "docs(proposal): cap nhat bang chuc nang functional matrix SCRUM-9"

# Ví dụ của Đức Lãm:
git commit -m "docs(proposal): bo sung so do kien truc va ke hoach sprint SCRUM-10"

# Đẩy nhánh lên GitHub
git push -u origin <tên-nhánh-của-bạn>
```

---

### Bước 5: Tạo Pull Request (PR) & Bắt đầu Review chéo
1. Truy cập [GitHub Repository](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base) $\to$ Bấm nút **Compare & pull request**.
2. Đặt tiêu đề PR: `docs(proposal): hoàn thiện phần viết [Mã task]`.
3. Tại ô **Reviewers**, tag bạn chịu trách nhiệm review chéo theo phân công ở Mục 2.
4. Sau khi người review bấm **Approve**, Nhóm trưởng sẽ kiểm tra lần cuối và Merge vào nhánh `main`.
5. Đăng nhập [Jira Cloud](https://ngovietthanhbinh2006-1790671331599.atlassian.net) để kéo task của mình sang cột **Done**.
