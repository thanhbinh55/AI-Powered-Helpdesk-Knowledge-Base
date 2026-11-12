# 6. NHẬT KÝ SỬ DỤNG AI (GIAI ĐOẠN TEMPLATE 1)

> **Dự án:** AI-Powered Helpdesk & Knowledge Base (Clarune)  
> **Nhóm thực hiện:** Nhóm 04 — Lớp Nhập môn Công nghệ Phần mềm (CS10014), Trường ĐHKHTN, ĐHQG-HCM  
> **Kho lưu trữ:** https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base  
> **Chuẩn quy định:** Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS  
> **Phạm vi tài liệu:** Nhật ký ghi nhận các phiên sử dụng công cụ AI phục vụ trực tiếp cho Báo cáo Template 1 (kế thừa và tiếp nối độc lập sau khi đã nộp hoàn tất Template 0).  

---

## 6.1 NGUYÊN TẮC MINH BẠCH & KIỂM CHỨNG TRONG TEMPLATE 1

1. **Minh bạch câu lệnh (Prompts):** Toàn bộ các câu prompt đưa vào AI đều được ghi nhận trung thực, tóm tắt rõ mục đích và đã khử các thông tin nhạy cảm (secrets/credentials/PII).
2. **Không sao chép máy móc:** Mọi sơ đồ UML, ma trận yêu cầu chức năng (FR), Use Case và giao diện do AI hỗ trợ đề xuất đều được các thành viên nhóm hiểu rõ, đối chiếu chéo với `SRS-master.md`, tài liệu nhóm Google Docs (`NMCNPM - Clarune - 04`) và chỉnh sửa thủ công trước khi đưa vào báo cáo.
3. **Phân định trách nhiệm cá nhân:** Tác giả từng phân hệ chịu trách nhiệm trực tiếp về phần nội dung con người đã kiểm chứng, không có tình trạng tạo dữ liệu giả hoặc nghiệm thu hình thức.

---

## 6.2 BẢNG TỔNG HỢP CÁC PHIÊN SỬ DỤNG AI PHỤC VỤ TEMPLATE 1

| STT | Thời gian | Thành viên (MSSV) | Công cụ & Nền tảng | Nội dung công việc trong Template 1 | Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: |
| **T1-01** | 26/10 - 03/11/2026 | Lê Quý Phúc<br>`24120121` | Claude Code (Claude Opus 5.5), Anthropic<br>Codex, OpenAI | Thiết kế giao diện Quiet Workspace Redesign v2 trên Figma (`docs/design/`) | AI hỗ trợ dựng component và flow prototype theo phong cách B2B Minimalism; sinh viên trực tiếp đối chiếu SRS, duyệt phương án và chỉnh sửa | Figma Node `49:58`, PR #9 |
| **T1-02** | 10h00 - 20h30<br>03/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>via Antigravity IDE | Kế hoạch chi tiết Giai đoạn 2 (Template 1 & Cài đặt mã nguồn MVP) & Bộ khung tài liệu | AI hỗ trợ tổng hợp yêu cầu kỹ thuật từ SRS-master.md, thiết lập cấu trúc Use Case và kịch bản CSV Jira; sinh viên đối soát logic nghiệp vụ và phân chia task | `PLAN_TEMPLATE1_AND_DEVELOPMENT.md`, `tasks_template1.csv` |
| **T1-03** | 14h00 - 18h30<br>06/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Khởi tạo bản thảo Template 1 Master & Rà soát mã kiểm thử truy vết | AI khởi tạo `TEMPLATE1_DRAFT_MASTER.md` với 41 FRs, 30 USs, NFRs; phân tích quy chuẩn mã kiểm thử TC P0 vs P1; sinh viên đối chiếu SRS-master.md và Google Docs, hiệu chỉnh tác nhân UC-01 | `reports/template1/TEMPLATE1_DRAFT_MASTER.md` |
| **T1-04** | 18h30 06/11<br>- 01h30 07/11 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Thiết kế Sơ đồ Use Case UML 2.5 đơn sắc & Quy chuẩn thiết kế sơ đồ nhóm | AI sinh mã Mermaid và tệp .drawio/.svg sơ đồ Định danh; phân tích UML 2.5 về Actor kế thừa và lý do không lạm dụng include/extend; soạn 6 quy tắc sơ đồ đơn sắc; sinh viên chọn phong cách tối giản đen trắng, tích hợp vào kế hoạch nhóm | Commit `58986ee`, `uc_module_identity.svg` |
| **T1-05** | 03h00 - 12h00<br>07/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Chuẩn hóa 6 Sơ đồ UML đơn sắc toàn hệ thống & Ánh xạ giao diện Mục 5 theo Figma Redesign v2 | AI tạo trọn bộ 6 sơ đồ đơn sắc (.drawio, .svg, .png scale 2x); ánh xạ 33 nhóm màn hình Redesign v2 vào Mục 5; bổ sung link tham khảo K23; sinh viên trực tiếp kiểm tra độ nét ảnh PNG và tính hợp lệ của đường dẫn ảnh | Commit `58986ee`, thư mục `assets/diagrams/` |
| **T1-06** | 21h30 07/11<br>- 00h30 08/11 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Mở rộng 19 Use Cases theo Clarune Docs, Loại bỏ nhãn Module ABCD & Hoàn thiện UI 5.5.5 - 5.5.8 | AI xóa bỏ nhãn Module A/B/C/D đổi thành 4 Phân hệ; vẽ lại Sơ đồ 1 (19 UCs) và Sơ đồ 5 (5 UCs); thêm đặc tả UC-18, UC-19 và giao diện mục 5.5.5 đến 5.5.8; sinh viên rà soát ma trận quyền (Agent duyệt UC-19, Admin không có quyền; UC-18 cho cả Agent và Admin) | Commit `dc7231c`, `uc_overall_19_usecases.svg` |
| **T1-07** | 08h45 - 08h55<br>09/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Review và Merge Pull Request #9 (Clarune Design v2), Sửa lỗi CI Marker Đóng góp Git | AI hỗ trợ merge PR #9 trên GitHub qua gh cli, rebase nhánh main, khắc phục lỗi thiếu cặp thẻ marker GENERATED trong script và báo cáo đóng góp git; đẩy lên remote và xác nhận GitHub Actions PASS xanh | Commit `43c725f`, PR #9 GitHub |
| **T1-08** | 7h00<br>08/11/2026 - 11h40<br>12/11/2026 | Phan Gia Phúc<br>`24120503` | OpenAI - ChatGPT, Codex | Đặc tả các UC-05 đến UC-10, các FR/NFR, mô tả giao diện Customer Portal, Agent Workspace; Tổng kết các nội dung cho đặc tả các UC đang phụ trách, các nội dung cho phần 5.2, 5.3 cho phần 5 Prototype trong Template1 | Gợi ý cách trình bày nội dung/bảng cho phần 3.2 cho Template1, cho các UC-05 đến UC-10, cho các mô tả của phần 5.2, 5.3 trong Template1; AI kiểm tra/so sánh lại với SRS và siên viên tự review lại.  | Commit `5c0fbe2` trên nhánh docs/t1-ticket-giaphuc |
---

## 6.3 CHI TIẾT CÁC PHIÊN LÀM VIỆC VỚI AI TRONG TEMPLATE 1

### Phiên T1-03: Khởi tạo bản thảo Template 1 Master & Đối soát mã kiểm thử truy vết
- **Thời gian:** 14h00 - 18h30 ngày 06/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm · Phân hệ Định danh và phân quyền)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Soạn thảo cực kỳ chi tiết, đầy đủ bản thảo tổng hợp Template 1 theo cấu trúc mẫu: Mục 1 Đánh giá đóng góp thành viên, Mục 2 Mô tả bài toán, Mục 3 Tổng quan yêu cầu (41 FRs, 30 USs, NFRs), Mục 4 Mô hình Use Case. Rà soát ý nghĩa của mã TC là gì, các mã TC trong bản thảo nhưng chưa có ở Test Matrix SRS (TC-ID-07..09, TC-TK-12, TC-KB-07, TC-AI-08..10), xác định rõ phạm vi trách nhiệm của Thanh Bình và nghiêm cấm tự ý commit khi chưa kiểm tra.”*
- **Nội dung AI tạo:**
  - Khung file `TEMPLATE1_DRAFT_MASTER.md` tổng hợp toàn diện các nội dung đã thống nhất.
  - Phân tích và phân loại các mã Test Case: làm rõ các mã TC thuộc Core MVP P0 (đã có kịch bản kiểm thử chính thức trong SRS 14.2) và các mã TC thuộc Post-MVP P1 (mã giữ chỗ đối soát, chưa có ca kiểm thử chính thức).
  - Phân định rõ trách nhiệm của Thanh Bình: phụ trách Phân hệ Định danh và phân quyền, sơ đồ tổng thể, rà soát ma trận quyền và điều phối Template 1.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên trực tiếp đối chiếu từng mã FR, US với tài liệu `SRS-master.md` và Google Docs của nhóm (`NMCNPM - Clarune - 04`).
  - Sửa đổi điều kiện tiên quyết và tác nhân trong `4.2.1 [UC-01]` (làm rõ tác nhân Khách chưa có tài khoản khi đăng ký).
  - Nghiêm cấm AI commit tự động khi chưa được kiểm tra bằng tay.
- **Minh chứng:** File `reports/template1/TEMPLATE1_DRAFT_MASTER.md`.

---

### Phiên T1-04: Thiết kế Sơ đồ Use Case UML 2.5 đơn sắc & Bộ quy chuẩn thiết kế sơ đồ nhóm
- **Thời gian:** 18h30 ngày 06/11/2026 - 01h30 ngày 07/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm · Phân hệ Định danh và phân quyền)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Vẽ Sơ đồ Use Case Phân hệ Định danh và phân quyền chuẩn với hệ thống của nhóm. Cung cấp mã Mermaid và tệp XML drawio/svg. Giải thích tại sao UC-16 lại elip nét đứt, tại sao hệ thống bài khác dùng «include»/«extend», phân biệt P0 và P1. Thiết kế lại theo hướng tối giản, ít màu sắc, cơ bản dễ quan sát (trắng đen monochrome). Xây dựng bộ quy tắc thiết kế sơ đồ để đưa vào kế hoạch hướng dẫn các thành viên khác vẽ đồng nhất.”*
- **Nội dung AI tạo:**
  - Mã Mermaid và tệp `uc_module_d_identity.drawio`, `.svg`.
  - Phân tích chuẩn UML 2.5: không lạm dụng `«include»`/`«extend»` khi các ca sử dụng là mục tiêu độc lập; giải thích cơ chế kế thừa tác nhân trừu tượng `Authenticated User`.
  - Dự thảo 6 nguyên tắc thiết kế sơ đồ đơn sắc đen - trắng (#FFFFFF/#000000, viền 1.5pt, không bóng mờ, xuất song song .drawio và .svg).
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên phản biện, yêu cầu loại bỏ màu sắc sặc sỡ, chuyển toàn bộ sang phong cách tài liệu kỹ thuật đơn sắc đen - trắng chuẩn mực.
  - Sửa lại UC-16 vẽ bằng nét liền elip chuẩn UML (chỉ ghi chú `(P1)` bằng văn bản chứ không vẽ nét đứt gây sai lệch chuẩn UML).
  - Đưa quy chuẩn vào Mục 6 của `PLAN_TEMPLATE1_AND_DEVELOPMENT.md` để các thành viên khác tuân thủ.
- **Minh chứng:** Tệp `reports/template1/assets/diagrams/uc_module_d_identity.svg` và commit `58986ee`.

---

### Phiên T1-05: Chuẩn hóa 6 Sơ đồ UML đơn sắc toàn hệ thống & Ánh xạ giao diện Mục 5 theo Figma Redesign v2
- **Thời gian:** 03h00 - 12h00 ngày 07/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Kéo bản PLAN_TEMPLATE1_AND_DEVELOPMENT.md mới nhất từ GitHub xuống, bổ sung và vẽ lại toàn bộ các sơ đồ Use Case theo quy chuẩn đơn sắc đã thống nhất. Tích hợp link thư mục Google Drive chứa các bài mẫu tham khảo K23 vào kế hoạch. Ánh xạ danh mục 33 nhóm màn hình Redesign v2 (Quiet Workspace) vào Mục 5, ghi đúng Node Figma, tệp ảnh nguồn và vị trí chèn ảnh.”*
- **Nội dung AI tạo:**
  - Trọn bộ 6 sơ đồ đơn sắc: Sơ đồ 0 (Bối cảnh), Sơ đồ 1 (Tổng thể), Sơ đồ 2 (Định danh), Sơ đồ 3 (Ticket), Sơ đồ 4 (Tri thức), Sơ đồ 5 (Trợ lý AI và thống kê).
  - Cấu hình script headless Google Chrome render ảnh PNG độ phân giải cao 2x tránh vỡ nét khi chèn báo cáo.
  - Cấu trúc Mục 5 trong `TEMPLATE1_DRAFT_MASTER.md` từ Hình 5.1 đến Hình 5.22b đối chiếu chính xác Node Figma và tệp ảnh trong `docs/design/anh/`.
  - Bổ sung link Google Drive bài mẫu K23 vào tài liệu kế hoạch.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên trực tiếp kiểm tra độ sắc nét ảnh PNG render bằng Chrome headless, kiểm tra tính đầy đủ của các tệp sơ đồ.
  - Đối chiếu danh sách tệp trong `docs/design/anh/` với từng Node Figma để đảm bảo không lỗi đường dẫn ảnh.
- **Minh chứng:** Thư mục `reports/template1/assets/diagrams/` và commit `58986ee`.

---

### Phiên T1-06: Mở rộng 19 Use Cases theo Clarune Docs, Loại bỏ nhãn Module ABCD & Hoàn thiện UI 5.5.5 - 5.5.8
- **Thời gian:** 21h30 ngày 07/11/2026 - 00h30 ngày 08/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Đối chiếu với file doc nhóm đang chỉnh sửa NMCNPM - Clarune - 04. Nhóm đã mở rộng phạm vi lên 19 Use Cases (thêm UC-18 Lịch sử gợi ý AI và UC-19 Đánh giá gợi ý AI). Tôi không muốn giữ lại ký hiệu nội bộ Module A/B/C/D nữa mà đổi thành Phân hệ chức năng. Vẽ lại sơ đồ tổng thể 19 Use Cases, sơ đồ Trợ lý AI 5 Use Cases, thêm đặc tả chi tiết UC-18, UC-19 và bổ sung các mục giao diện 5.5.5 đến 5.5.8 (Hình 5.23a đến Hình 5.27).”*
- **Nội dung AI tạo:**
  - Thay thế toàn bộ tiền tố Module A/B/C/D thành tên gọi 4 Phân hệ chức năng chính thức trong toàn bộ sơ đồ và tài liệu.
  - Vẽ mới `uc_overall_19_usecases.svg` (.drawio, .png) chứa trọn vẹn 19 Use Cases.
  - Cập nhật `uc_module_ai_analytics.svg` (.drawio, .png) gồm 5 Use Cases: phân quyền Agent thao tác UC-19 (Admin không có quyền); UC-18 cho cả Agent và Admin; UC-17 cho Admin.
  - Thêm 2 bảng đặc tả chi tiết `4.2.18 [UC-18]` và `4.2.19 [UC-19]`.
  - Hoàn thiện Mục 5.5.5 đến 5.5.8 (Hình 5.23a đến Hình 5.27), trích xuất linh kiện `81-7560.png` vào `docs/design/anh/thanh-phan/`.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên rà soát tính logic của ma trận quyền truy cập đối với UC-18 và UC-19 theo đúng nghiệp vụ Helpdesk.
  - Chạy headless Chrome xuất lại ảnh PNG cho toàn bộ sơ đồ mới; kiểm tra cú pháp commit-msg hook đạt chuẩn.
- **Minh chứng:** File `reports/template1/TEMPLATE1_DRAFT_MASTER.md`, `PLAN_TEMPLATE1_AND_DEVELOPMENT.md` và commit `dc7231c`.

---

### Phiên T1-07: Review và Merge Pull Request #9 (Clarune Design v2), Sửa lỗi CI Marker Đóng góp Git
- **Thời gian:** 08h45 - 08h55 ngày 09/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“merge nhánh của phúc đang yêu cầu PR”*
- **Nội dung AI tạo:**
  - Kiểm tra thông tin PR #9 từ nhánh `docs/t1-ai-quyphuc`, phân tích nguyên nhân lỗi CI của GitHub Actions (`Documentation & Reports Quality Assurance` fail do thiếu cặp thẻ marker `<!-- GENERATED:START -->` và `<!-- GENERATED:END -->`).
  - Thực hiện lệnh merge PR #9 trên GitHub thông qua `gh pr merge 9 --merge`.
  - Rebase nhánh `main` cục bộ lên `origin/main` giữ trọn vẹn lịch sử commit và các cập nhật 19 Use Cases trước đó.
  - Chỉnh sửa `scripts/git_contributions.py` để tự động tạo đúng cặp thẻ marker và chạy cập nhật `reports/08-git-contributions.md`.
  - Đẩy lên `origin/main`, theo dõi workflow GitHub Actions chạy đạt kết quả xanh (`✓ PASS`).
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên xác nhận PR #9 đã được đóng trên GitHub với đầy đủ các màn hình prototype Clarune Redesign v2.
  - Kiểm tra trạng thái CI GitHub Actions chuyển sang trạng thái xanh (PASS 100%).
- **Minh chứng:** Pull Request #9 trên GitHub, commit `43c725f`.

---

### Phiên T1-08: Đặc tả phân hệ Quản lý ticket & Mô tả giao diện Customer Portal, Agent Workspace
- **Thời gian:** 07h00 ngày 08/11/2026 - 11h40 ngày 12/11/2026
- **Tác giả chịu trách nhiệm:** `24120503` - Phan Gia Phúc (Phân hệ Quản lý ticket)
- **Công cụ / Nền tảng:** ChatGPT và Codex, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm (tổng hợp lại từ các yêu cầu trong phiên):**
  > *“Đọc SRS của nhóm và đối chiếu với nội dung tôi đang soạn cho phân hệ Quản lý ticket trong Template 1. Gợi ý cách trình bày bảng yêu cầu chức năng ở Mục 3.2 và hoàn thiện cách diễn đạt các đặc tả UC-05 đến UC-10 theo mẫu 9 trường: mã, tên, tóm tắt, tác nhân, điều kiện tiên quyết, kết quả, kịch bản chính, kịch bản phụ và ràng buộc phi chức năng. Kiểm tra quyền của Customer, Agent, Admin; việc nhận ticket đồng thời chỉ cho một người thành công; phạm vi tin nhắn công khai, ghi chú nội bộ; các thao tác chuyển trạng thái và quyền xem lịch sử. Phân biệt yêu cầu P0 với phần mở rộng P1, không tự thêm chức năng hoặc số liệu ngoài tài liệu nguồn. Với phần bản mẫu, hỗ trợ trình bày mô tả Customer Portal ở Mục 5.2 và Agent Workspace ở Mục 5.3, bảo đảm các thao tác khớp với Use Case phụ trách. Tổng hợp nội dung từ bản báo cáo tôi cung cấp, thay các ký hiệu ảnh bằng đường dẫn PNG tương ứng trong kho mã nguồn. Chỉ bổ sung phần của Phan Gia Phúc, giữ nguyên nội dung có sẵn và chỉ ra điểm chưa thống nhất để tôi tự rà soát trước khi đưa vào báo cáo.”*
- **Nội dung AI tạo:**
  - Gợi ý cấu trúc bảng và cách diễn đạt các yêu cầu chức năng thuộc phân hệ Quản lý ticket trong Mục 3.2 của Template 1.
  - Hỗ trợ trình bày 6 bảng đặc tả UC-05 đến UC-10, gồm luồng chính, luồng phụ và các ràng buộc phi chức năng liên quan đến phân quyền, tính toàn vẹn, xử lý đồng thời và trải nghiệm người dùng.
  - Hỗ trợ đối chiếu các quy tắc nghiệp vụ với SRS: quyền sở hữu ticket, nhận và phân công xử lý, phân biệt PUBLIC/INTERNAL, chuyển trạng thái và xem lịch sử sự kiện.
  - Tổng hợp mô tả 5 màn hình Customer Portal và 3 màn hình Agent Workspace từ bản báo cáo được cung cấp; thay 8 ký hiệu ảnh bằng đường dẫn PNG trong `05-prototype-mockup.md`.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên tự review nội dung AI gợi ý, đối chiếu các FR/NFR và đặc tả UC-05 đến UC-10 với `reports/SRS-master.md` trước khi sử dụng trong báo cáo.
  - Rà soát quyền thao tác theo vai trò và trạng thái ticket: Customer không xem ghi chú nội bộ hoặc lịch sử nội bộ; Agent chưa nhận ticket không được xử lý; ticket CLOSED chỉ được xem lại và không được mở lại.
  - Đối chiếu mô tả Customer Portal, Agent Workspace với các Use Case phụ trách; yêu cầu chỉ lấy phần 5.2, 5.3 từ file nguồn và bổ sung vào cuối file đích, giữ nguyên nội dung có sẵn.
  - Yêu cầu AI hỗ trợ trình bày và kiểm tra tính nhất quán; sinh viên tự rà soát, chỉnh sửa và chịu trách nhiệm về nội dung cuối cùng.
- **Minh chứng:** Các file `reports/template1/03-tong-quan-yeu-cau/03.2.1-yeu-cau-chuc-nang.md`, `reports/template1/04-dac-ta-use-cases/04.2-module-C-ticket.md`, `reports/template1/05-prototype-mockup.md`; commit `5c0fbe2` trên nhánh `docs/t1-ticket-giaphuc` ghi nhận phần bổ sung mô tả giao diện 5.2, 5.3.

---

## 6.4 CAM KẾT ĐẠO ĐỨC HỌC THUẬT

Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:
1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.
2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.
