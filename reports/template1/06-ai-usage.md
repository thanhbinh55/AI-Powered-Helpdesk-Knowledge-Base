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
| **T1-08** | 09/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Rà soát UC-11 — Tải lên và xử lý tài liệu tri thức | AI hỗ trợ rà soát đặc tả theo SRS, chỉ ra nội dung chưa rõ và gợi ý chỉnh sửa. Sinh viên tự kiểm chứng: Đối chiếu quyền tải tài liệu, giới hạn tệp và sự tách biệt giữa xử lý với công bố. |
| **T1-09** | 09/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Rà soát UC-12 — Công bố và lưu trữ tài liệu tri thức | AI hỗ trợ đối chiếu điều kiện, kết quả và các kịch bản với SRS; gợi ý điều chỉnh nội dung và cách diễn đạt. Sinh viên tự kiểm chứng: Đối chiếu hai luồng công bố, lưu trữ và yêu cầu giữ lịch sử trích dẫn. |
| **T1-10** | 09/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Rà soát UC-13 — Tìm kiếm tri thức | AI hỗ trợ rà soát tính nhất quán giữa tác nhân, điều kiện tiên quyết, luồng xử lý và kết quả; gợi ý chỉnh sửa. Sinh viên tự kiểm chứng: Đối chiếu quyền tìm kiếm, điều kiện tài liệu và các nhánh ngoại lệ. |
| **T1-11** | 10/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Trau chuốt lại cách diễn đạt trong báo cáo phần UC-11  | AI gợi ý đơn giản hóa các chi tiết kỹ thuật về tải lên và xử lý tài liệu, giữ ý nghĩa nghiệp vụ. Sinh viên tự kiểm chứng: So sánh trước và sau khi sửa để giữ đúng ý nghĩa nghiệp vụ của UC-11. |
| **T1-12** | 10/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Trau chuốt lại cách diễn đạt trong báo cáo phần UC-12 | AI gợi ý diễn đạt dễ hiểu hơn về điều kiện công bố, lưu trữ và ảnh hưởng của từng thao tác. Sinh viên tự kiểm chứng: Rà soát cách diễn đạt, điều kiện và kết quả công bố, lưu trữ. |
| **T1-13** | 10/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Trau chuốt lại cách diễn đạt trong báo cáo phần UC-13 | AI gợi ý mô tả tìm kiếm ở mức nghiệp vụ, giữ rõ quyền truy cập, điều kiện tìm thấy tài liệu và ngoại lệ. Sinh viên tự kiểm chứng: Rà soát quyền truy cập và các ngoại lệ sau khi đơn giản hóa UC-13. |
| **T1-14** | 11/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Hệ thống lại Danh sách các stakeholder | AI hỗ trợ tổng hợp các bên liên quan và mô tả nhiệm vụ, chức năng theo SRS. Sinh viên tự kiểm chứng: Đối chiếu vai trò và phân loại các bên liên quan với SRS. |
| **T1-15** | 11/10/2026 | Nguyễn Đức Lãm<br>`24120083` | GPT-6.1-Sol<br>OpenAI | Chỉnh sửa Context Diagram | AI hỗ trợ rà soát, gợi ý điều chỉnh tên ứng dụng, tác nhân và đường nối theo bảng các bên liên quan. Sinh viên tự kiểm chứng: Đối chiếu tác nhân, ranh giới hệ thống và bố cục sơ đồ theo quy ước nhóm. |
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

### Phiên T1-08: Rà soát đặc tả UC-11 — Tải lên và xử lý tài liệu tri thức
- **Thời gian:** 09/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy rà soát đặc tả UC-11 trong ảnh, đối chiếu với tài liệu SRS hiện tại. Chỉ ra những nội dung mâu thuẫn, chưa chính xác hoặc chưa rõ ràng và gợi ý chỉnh sửa."*
- **Nội dung AI tạo:**
  - Nhận xét về những điểm chưa thống nhất hoặc chưa rõ trong đặc tả UC-11 và gợi ý điều chỉnh tương ứng.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đối chiếu từng mục của UC-11 với SRS và tài liệu nguồn, tập trung vào quyền tải tài liệu, định dạng được hỗ trợ, giới hạn 10 MiB và các trường hợp xử lý thất bại.
  - Rà soát để phân biệt việc xử lý thành công với việc công bố tài liệu; lựa chọn và điều chỉnh các gợi ý phù hợp với phạm vi Use Case.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-09: Rà soát đặc tả UC-12 — Công bố và lưu trữ tài liệu tri thức
- **Thời gian:** 09/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy tiếp tục rà soát đặc tả UC-12, đối chiếu các điều kiện thực hiện, kết quả, kịch bản chính và kịch bản phụ với tài liệu SRS hiện tại. Chỉ ra những điểm cần điều chỉnh và gợi ý cách diễn đạt phù hợp."*
- **Nội dung AI tạo:**
  - Nhận xét và gợi ý chỉnh sửa điều kiện thực hiện, kết quả, kịch bản chính và kịch bản phụ của UC-12 theo SRS.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đối chiếu hai luồng công bố và lưu trữ với SRS; rà soát quyền quản trị viên, điều kiện tài liệu và các nhánh từ chối thao tác.
  - Kiểm tra cách mô tả việc ngừng sử dụng tài liệu đã lưu trữ cho yêu cầu mới.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-10: Rà soát đặc tả UC-13 — Tìm kiếm tri thức
- **Thời gian:** 09/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy rà soát đặc tả UC-13 và đối chiếu với tài liệu SRS hiện tại. Kiểm tra tính nhất quán giữa tác nhân, điều kiện tiên quyết, các luồng xử lý và kết quả; gợi ý chỉnh sửa những nội dung chưa phù hợp."*
- **Nội dung AI tạo:**
  - Nhận xét và gợi ý điều chỉnh tác nhân, điều kiện tiên quyết, luồng xử lý và kết quả của UC-13.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đối chiếu tác nhân và điều kiện tiên quyết của UC-13 với SRS, bảo đảm mô tả dành cho nhân viên hỗ trợ hoặc quản trị viên có quyền.
  - Rà soát điều kiện tài liệu được tìm thấy, việc kiểm tra lại quyền khi mở chi tiết và các trường hợp không có kết quả hoặc tài liệu không còn khả dụng.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-11: Gợi ý đơn giản hóa cách diễn đạt của UC-11
- **Thời gian:** 10/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Đặc tả UC-11 đang chứa nhiều chi tiết kỹ thuật như READY, FAILED, UPLOADED, PENDING, RUNNING và PROCESSING. Hãy chỉ ra những phần quá sâu về triển khai và gợi ý diễn đạt bằng ngôn ngữ đơn giản, phù hợp với báo cáo, đồng thời giữ đúng ý nghĩa nghiệp vụ."*
- **Nội dung AI tạo:**
  - Gợi ý thay các trạng thái và mô tả xử lý nội bộ bằng cách diễn đạt dễ hiểu ở mức nghiệp vụ.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Rà soát các thuật ngữ kỹ thuật trong UC-11 và lựa chọn cách diễn đạt tiếng Việt phù hợp với báo cáo.
  - Đối chiếu trước và sau khi chỉnh sửa để giữ nguyên ý nghĩa về tiếp nhận, xử lý, thử lại, thông báo lỗi và việc công bố riêng qua UC-12.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-12: Gợi ý đơn giản hóa cách diễn đạt của UC-12
- **Thời gian:** 10/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy tiếp tục rà soát cách diễn đạt trong UC-12. Gợi ý thay thế các thuật ngữ về trạng thái dữ liệu, mã lỗi và xử lý nội bộ bằng lời giải thích dễ hiểu, giữ rõ điều kiện công bố, lưu trữ và ảnh hưởng của từng thao tác."*
- **Nội dung AI tạo:**
  - Gợi ý đơn giản hóa thuật ngữ kỹ thuật trong UC-12, làm rõ điều kiện và kết quả của thao tác công bố, lưu trữ.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đọc lại hai luồng công bố và lưu trữ sau khi đơn giản hóa cách diễn đạt; đối chiếu với SRS để giữ đúng điều kiện thực hiện và kết quả của từng thao tác.
  - Rà soát các nhánh hủy, từ chối và lỗi lưu thay đổi, cùng yêu cầu giữ nguyên lịch sử trích dẫn.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-13: Gợi ý đơn giản hóa cách diễn đạt của UC-13
- **Thời gian:** 10/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy rà soát những phần mô tả quá chi tiết về kỹ thuật tìm kiếm trong UC-13 và gợi ý cách diễn đạt ở mức nghiệp vụ. Nội dung cần dễ hiểu nhưng vẫn thể hiện đúng quyền truy cập, điều kiện tài liệu được tìm thấy và các trường hợp ngoại lệ."*
- **Nội dung AI tạo:**
  - Gợi ý thay mô tả triển khai tìm kiếm bằng mô tả nghiệp vụ về truy cập tài liệu, kết quả tìm kiếm và ngoại lệ.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Rà soát cách diễn đạt của UC-13 sau khi lược bớt chi tiết triển khai tìm kiếm.
  - Đối chiếu với SRS để giữ rõ quyền truy cập, điều kiện sử dụng tài liệu, cách hiển thị kết quả và các trường hợp ngoại lệ; điều chỉnh những câu có thể làm sai ý nghĩa nghiệp vụ.
- **Minh chứng:** File `reports/template1/04-dac-ta-use-cases/04.2-module-B-knowledge.md`

---

### Phiên T1-14: Rà soát stakeholder theo SRS
- **Thời gian:** 11/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy rà soát các stakeholder trong file SRS, xác định những bên liên quan được đề cập và mô tả nhiệm vụ, chức năng của từng bên theo nội dung tài liệu."*
- **Nội dung AI tạo:**
  - Tổng hợp các bên liên quan trong SRS và mô tả nhiệm vụ, chức năng của từng bên.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đối chiếu danh sách các bên liên quan và mô tả vai trò với SRS.
  - Rà soát sự khác nhau giữa bên liên quan của dự án, người dùng tương tác trực tiếp và dịch vụ bên ngoài; kiểm tra để tránh xem worker, cơ sở dữ liệu hoặc nơi lưu trữ nội bộ là tác nhân ngoài hệ thống.
- **Minh chứng:** `reports/template1/03-tong-quan-yeu-cau/03.1-stakeholders.md`

---

### Phiên T1-15: Rà soát và gợi ý điều chỉnh Context Diagram
- **Thời gian:** 11/10/2026
- **Tác giả chịu trách nhiệm:** `24120083` - Nguyễn Đức Lãm (Phân hệ Knowledge Base)
- **Công cụ / Model:** GPT-6.1-Sol, OpenAI
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *"Hãy rà soát hình context_diagram_system và đối chiếu với bảng các bên liên quan được cung cấp. Gợi ý lược bỏ các chi tiết kỹ thuật trong hình chữ nhật trung tâm, chỉ giữ tên ứng dụng Clarune, đồng thời điều chỉnh các tác nhân và đường nối cho phù hợp."*
- **Nội dung AI tạo:**
  - Nhận xét, gợi ý điều chỉnh và bản sửa sơ đồ với tên ứng dụng Clarune ở trung tâm, các tác nhân và đường nối theo bảng các bên liên quan.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Đối chiếu các tác nhân và quan hệ trên sơ đồ với bảng các bên liên quan; rà soát ranh giới hệ thống và tên ứng dụng Clarune.
  - Kiểm tra bố cục, nhãn và đường nối, chú ý tránh chữ đè lên nét vẽ và chừa khoảng cách giữa biểu tượng người que với đường nối; lựa chọn các điều chỉnh phù hợp với quy ước của nhóm.
- **Minh chứng:** `reports/template1/assets/diagrams/context_diagram_system.drawio`, `reports/template1/assets/diagrams/context_diagram_system.png`, `reports/template1/assets/diagrams/context_diagram_system.svg`

---
## 6.4 CAM KẾT ĐẠO ĐỨC HỌC THUẬT

Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:
1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.
2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.