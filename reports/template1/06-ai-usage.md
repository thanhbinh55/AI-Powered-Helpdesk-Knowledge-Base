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
| **T1-08** | 06–11/11/2026 | Lê Quý Phúc<br>`24120121` | Codex, OpenAI | Soạn thảo, rà soát và chuyển phần Template 1 được phân công sang Markdown: Mục 1, Mục 2, UC-14/15/17/18/19 và Mục 5.5 | AI hỗ trợ brainstorm Use Case, đề xuất luồng chính/phụ, viết NFR bằng lời, tạo DOCX highlight và chuyển định dạng. Sinh viên đối chiếu SRS, yêu cầu hiệu chỉnh và chỉnh thủ công bản DOCX; nội dung Markdown được lấy từ bản đã chốt và kiểm tra tự động từng đoạn/ô bảng | `01-danh-gia-thanh-vien.md`, `02-mo-ta-bai-toan.md`, các file đặc tả AI/Analytics, Mục 5.5; commit `af1e190`, PR #10 |

---

## 6.3 CHI TIẾT CÁC PHIÊN LÀM VIỆC VỚI AI TRONG TEMPLATE 1

### Phiên T1-01: Thiết kế giao diện Quiet Workspace Redesign v2 trên Figma — Lê Quý Phúc

- **Thời gian:** 26/10 – 03/11/2026.
- **Thành viên chịu trách nhiệm:** Lê Quý Phúc — `24120121`.
- **Công cụ:** Claude Code, Anthropic; Codex, OpenAI.
- **Mục đích và yêu cầu tóm tắt:** Thiết kế prototype Helpdesk theo phong cách “Bàn làm việc yên tĩnh” (Quiet Workspace), ưu tiên khả năng đọc và xử lý ticket liên tục; bám sát quyền Customer, Agent, Admin và luồng kiểm duyệt gợi ý AI trong SRS.
- **Nội dung AI hỗ trợ:**
  - Đề xuất bố cục, màu sắc, typography, khoảng cách và các thành phần giao diện dùng chung; tổ chức thành Foundations và Components để tái sử dụng trong Figma.
  - Dựng các màn hình cho Agent Workspace, Customer Portal, định danh/tài khoản, Kho tri thức và quản trị; bổ sung các trạng thái đang tải, trống và lỗi.
  - Thiết kế bố cục desktop, tablet, mobile và chế độ sáng/tối; nối các màn hình thành luồng prototype để minh họa thao tác.
  - Xuất ảnh PNG, lập danh mục màn hình và lưu ánh xạ Node Figma để nhóm sử dụng khi viết báo cáo và triển khai giao diện.
- **Nội dung con người kiểm chứng và hiệu chỉnh:**
  - Sinh viên đối chiếu phương án với SRS, lựa chọn hướng Quiet Workspace và yêu cầu chỉnh sửa bố cục, cách trình bày thông tin, thành phần và luồng thao tác.
  - Rà soát cách phân biệt trả lời công khai với ghi chú nội bộ, quyền thao tác theo vai trò và việc chèn gợi ý AI không tự gửi phản hồi.
  - Kiểm tra các màn hình và ảnh xuất phục vụ báo cáo; tiếp nhận phản hồi và hiệu chỉnh phương án trước khi bàn giao cho nhóm.
- **Giới hạn:** Đây là prototype minh họa, không phải bằng chứng backend, xác thực hoặc lưu dữ liệu đã hoạt động. Các kiểm tra bàn phím, screen reader và hành vi đầu cuối của ứng dụng cần thực hiện khi triển khai frontend.
- **Minh chứng:** Figma SE, Node `49:58`; [tài liệu thiết kế](../../docs/design/README.md), [danh mục màn hình](../../docs/design/man-hinh.md), [ánh xạ Node Figma](../../docs/design/figma-map.json), [Design System MASTER](../../design-system/helpdesk-workspace/MASTER.md) và [PR #9](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/9).

---

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

### Phiên T1-08: Soạn thảo và hoàn thiện nội dung Template 1 — Lê Quý Phúc

- **Thời gian:** 06–11/11/2026.
- **Thành viên chịu trách nhiệm:** Lê Quý Phúc — `24120121`.
- **Công cụ:** Codex, OpenAI.
- **Mục đích và yêu cầu tóm tắt:** Hỗ trợ hoàn thiện phần được phân công trong Template 1; phân tích sâu Use Case và ngoại lệ; chỉ chỉnh phần Quý Phúc; trình bày theo UC-01, viết ràng buộc phi chức năng bằng lời; chuyển đúng nội dung đã chốt sang Markdown và chỉ giữ chú thích hình.
- **Nội dung AI hỗ trợ:**
  - Brainstorm và rà soát đặc tả UC-14, UC-15, UC-17, UC-18, UC-19; làm rõ tác nhân, điều kiện, luồng chính/phụ, kết quả và phân quyền.
  - Gợi ý cách trình bày các bảng UC theo UC-01; diễn đạt NFR thành yêu cầu bằng lời; tạo DOCX highlight để người dùng đối chiếu và sửa thủ công.
  - Hỗ trợ biên tập mô tả giao diện Mục 5.5, rà soát hình minh họa và liên kết với các UC tương ứng.
  - Chuyển Mục 1, Mục 2, năm UC và Mục 5.5 từ DOCX đã chốt sang đúng các file Markdown được giao, giữ nguyên câu chữ và chú thích hình.
- **Nội dung con người kiểm chứng và hiệu chỉnh:** Sinh viên đối chiếu từng đề xuất, yêu cầu sửa luồng bỏ gợi ý, cách trình bày NFR và nội dung mockup, rồi chỉnh thủ công trong tài liệu nhóm. Bản DOCX cuối do người dùng cung cấp được dùng làm nguồn chuyển đổi, không lấy các bản gợi ý hoặc highlight cũ làm nội dung nộp.
- **Kiểm tra bằng công cụ:** Đối chiếu từng đoạn/ô bảng giữa DOCX và Markdown; kiểm đủ năm UC, mỗi UC chín trường và 12 chú thích hình ở Mục 5.5; kiểm tra diff để bảo toàn phần của thành viên khác.
- **Giới hạn:** Kiểm tra cấu trúc tài liệu và prototype không chứng minh nghiệp vụ backend đã được triển khai; lượt chuyển Markdown không truy cập Google Docs để kiểm tra cập nhật mới hơn DOCX.
- **Minh chứng:** Các file Markdown phần Quý Phúc trong `reports/template1/`, commit `af1e190` và [PR #10](https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base/pull/10).

---

## 6.4 CAM KẾT ĐẠO ĐỨC HỌC THUẬT

Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:
1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.
2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.
