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
| **T1-02** | 11h30 03/11<br>- 18h10 05/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Google Gemini (Gemini 3.8 Flash Medium)<br>via Antigravity IDE | Kế hoạch chi tiết Giai đoạn 2 (Template 1 & Cài đặt mã nguồn MVP), Bộ khung tài liệu & Công cụ tạo Sprint Jira | AI hỗ trợ tổng hợp yêu cầu kỹ thuật từ SRS-master.md, thiết lập cấu trúc Use Case, task `T1-DOC-MD` và script tạo Sprint Jira; sinh viên đối soát logic nghiệp vụ, thống nhất mốc 23:59 và phân chia task trên Jira | Commit `2ffb371`, `0534ad4`, `48b1042`, `0e785ce`, `bed75c1` |
| **T1-03** | 19h50 - 23h30<br>06/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Khởi tạo bản thảo Template 1 Master & Rà soát mã kiểm thử truy vết | AI khởi tạo `TEMPLATE1_DRAFT_MASTER.md` với 41 FRs, 30 USs, NFRs; phân tích quy chuẩn mã kiểm thử TC P0 vs P1; sinh viên đối chiếu SRS-master.md và Google Docs, hiệu chỉnh tác nhân UC-01 | `reports/template1/TEMPLATE1_DRAFT_MASTER.md`, Commit `58986ee` |
| **T1-04** | 00h45 - 01h50<br>07/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Thiết kế Sơ đồ Use Case UML 2.5 đơn sắc & Quy chuẩn thiết kế sơ đồ nhóm | AI sinh mã Mermaid và tệp .drawio/.svg sơ đồ Định danh; phân tích UML 2.5 về Actor kế thừa và lý do không lạm dụng include/extend; soạn 6 quy tắc sơ đồ đơn sắc; sinh viên chọn phong cách tối giản đen trắng, tích hợp vào kế hoạch nhóm | Commit `58986ee`, `uc_module_d_identity.svg` |
| **T1-05** | 10h05 - 10h50<br>07/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Chuẩn hóa 6 Sơ đồ UML đơn sắc toàn hệ thống & Ánh xạ giao diện Mục 5 theo Figma Redesign v2 | AI tạo trọn bộ 6 sơ đồ đơn sắc (.drawio, .svg, .png scale 2x); ánh xạ 33 nhóm màn hình Redesign v2 vào Mục 5; bổ sung link tham khảo K23; sinh viên trực tiếp kiểm tra độ nét ảnh PNG và tính hợp lệ của đường dẫn ảnh | Commit `58986ee`, thư mục `assets/diagrams/` |
| **T1-06** | 21h45 - 22h15<br>07/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Mở rộng 19 Use Cases theo Clarune Docs, Loại bỏ nhãn Module ABCD & Hoàn thiện UI 5.5.5 - 5.5.8 | AI xóa bỏ nhãn Module A/B/C/D đổi thành 4 Phân hệ; vẽ lại Sơ đồ 1 (19 UCs) và Sơ đồ 5 (5 UCs); thêm đặc tả UC-18, UC-19 và giao diện mục 5.5.5 đến 5.5.8; sinh viên rà soát ma trận quyền (Agent duyệt UC-19, Admin không có quyền; UC-18 cho cả Agent và Admin) | Commit `dc7231c`, `uc_overall_19_usecases.svg` |
| **T1-07** | 08h45 - 08h55<br>09/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Review và Merge Pull Request #9 (Clarune Design v2), Sửa lỗi CI Marker Đóng góp Git | AI hỗ trợ merge PR #9 trên GitHub qua gh cli, rebase nhánh main, khắc phục lỗi thiếu cặp thẻ marker GENERATED trong script và báo cáo đóng góp git; đẩy lên remote và xác nhận GitHub Actions PASS xanh | Commit `1b6fc76`, `43c725f`, PR #9 GitHub |
| **T1-08** | 08h50 - 09h20<br>09/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Tách biệt hồ sơ AI Usage Template 1 (`06-ai-usage.md`), Chuẩn hóa chỉ dẫn vị trí nộp file Markdown & Đồng bộ sơ đồ | AI hỗ trợ tách nhật ký AI Template 1 khỏi hồ sơ Template 0 đã đóng băng, lập bảng tra cứu vị trí file nộp bài theo từng đầu mục tại Mục 1.1 kế hoạch và cập nhật 4 biên bản bàn giao `inputs/`; sinh viên kiểm tra tính độc lập của hồ sơ Template 0, rà soát đường dẫn file và duyệt commit | Commit `a47f41f`, `06-ai-usage.md`, `PLAN_TEMPLATE1_AND_DEVELOPMENT.md` |
| **T1-09** | 10h15 - 11h45<br>10/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Review chéo nội dung Template 1 (Phần của Nguyễn Đức Lãm & Toàn bộ các mục trên Google Docs), Chuẩn hóa UC-01..04, UC-16 | AI hỗ trợ đối chiếu bản nháp Google Docs với `SRS-master.md` và bài mẫu K23, chỉ ra các điểm cần chỉnh sửa ở bảng Stakeholder (Mục 3.1), sơ đồ bối cảnh và các Use Case; sinh viên trực tiếp thẩm định, lọc các góp ý xác đáng để nhận xét trên Google Docs, chuẩn hóa đánh số kịch bản phụ (`A.1a`, `A.4a`) và lược bỏ chi tiết kỹ thuật tầng dưới khỏi UC-02 | Bản review chéo trên Google Docs, `TEMPLATE1_DRAFT_MASTER.md` |
| **T1-10** | 10h20 - 11h20<br>11/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 3.8 Flash)<br>via Antigravity IDE | Điều phối giao task chuyển đổi Markdown (`T1-DOC-MD` / `SCRUM-65`), Chuẩn hóa Bảng 3.1 Stakeholders (9 bên) & Rà soát ghi chú nội bộ | AI hỗ trợ cập nhật quy tắc chuyển đổi Markdown (giữ nguyên nội dung đã chốt, chỉ ghi tiêu đề hình ảnh) vào kế hoạch và 4 file `inputs/`, tạo Jira Issue `SCRUM-65`, định dạng bảng 9 Stakeholders & Actors và quét các ghi chú nội bộ/typo còn sót trong bản thảo; sinh viên kiểm chứng chéo với SRS Mục 3.1, yêu cầu giữ nguyên các file thành viên khác phụ trách và chỉ cập nhật trên bản nháp tổng hợp | Jira `SCRUM-65`, `TEMPLATE1_DRAFT_MASTER.md`, `inputs/*.md` |

---

## 6.3 CHI TIẾT CÁC PHIÊN LÀM VIỆC VỚI AI TRONG TEMPLATE 1

### Phiên T1-02: Xây dựng Kế hoạch chi tiết Giai đoạn 2 (Template 1 & Cài đặt mã nguồn MVP), Bộ khung tài liệu & Công cụ tạo Sprint Jira
- **Thời gian:** 11h30 ngày 03/11/2026 - 18h10 ngày 05/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm · Phân hệ Định danh và phân quyền)
- **Công cụ / Model:** Google Gemini (Gemini 3.8 Flash Medium, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Dựa vào SRS-master.md và các phản hồi rà soát kỹ thuật (5 trạng thái ticket, worker quét job SKIP LOCKED retry <= 3, 41 FRs, 17 Use Cases chuẩn hóa, tách Flyway V1-V5, interface chuẩn SRS), xây dựng kế hoạch hành động toàn diện cho Giai đoạn 2 (Template 1 và code MVP 4 module), thiết lập sổ tay hướng dẫn nhóm theo quy trình 2 giai đoạn Google Docs -> Git Markdown, chuẩn hóa danh mục task CSV cho Jira bulk create, tạo cấu trúc thư mục rỗng reports/template1/, bổ sung task T1-DOC-MD và công cụ tạo Sprint Jira tự động.”*
- **Nội dung AI tạo:**
  - Khung tài liệu `PLAN_TEMPLATE1_AND_DEVELOPMENT.md`, file backlog `scripts/jira/tasks_template1.csv`, công cụ quản lý Sprint Jira và cấu trúc thư mục `reports/template1/`.
  - Sơ đồ lộ trình Gantt tổng thể và hướng dẫn quy trình phối hợp 2 giai đoạn (soạn thảo trên Google Docs trước, chuyển đổi sang Markdown trên Git sau).
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên trực tiếp đối soát từng điều khoản với `SRS-master.md`, loại bỏ các use case ngoài phạm vi, chuẩn hóa thuật ngữ các tác nhân (Guest, Customer, Support Agent, System Administrator).
  - Cân bằng khối lượng công việc giữa 4 thành viên, thống nhất mốc hạn chót 23:59 và chạy kiểm thử kịch bản tạo Sprint / gán task trên Jira.
- **Minh chứng:** File `PLAN_TEMPLATE1_AND_DEVELOPMENT.md`, `scripts/jira/tasks_template1.csv` và chuỗi commit `2ffb371`, `0534ad4`, `48b1042`, `0e785ce`, `bed75c1`.

---

### Phiên T1-03: Khởi tạo bản thảo Template 1 Master & Đối soát mã kiểm thử truy vết
- **Thời gian:** 19h50 - 23h30 ngày 06/11/2026
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
- **Minh chứng:** File `reports/template1/TEMPLATE1_DRAFT_MASTER.md` và commit `58986ee`.

---

### Phiên T1-04: Thiết kế Sơ đồ Use Case UML 2.5 đơn sắc & Bộ quy chuẩn thiết kế sơ đồ nhóm
- **Thời gian:** 00h45 - 01h50 ngày 07/11/2026
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
- **Thời gian:** 10h05 - 10h50 ngày 07/11/2026
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
- **Thời gian:** 21h45 - 22h15 ngày 07/11/2026
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
- **Minh chứng:** Pull Request #9 trên GitHub, commit `1b6fc76` và `43c725f`.

---

### Phiên T1-08: Tách biệt hồ sơ AI Usage Template 1, Chuẩn hóa chỉ dẫn vị trí nộp file Markdown & Đồng bộ sơ đồ
- **Thời gian:** 08h50 - 09h20 ngày 09/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Phần nội dung đã nộp cho Template 0 thì giữ nguyên, các nội dung bổ sung thì bắt đầu tiếp tục với Template 1 riêng tại reports/template1/06-ai-usage.md. Rà soát xem đã có lưu ý về việc thêm nội dung AI usage trong phần giao task cho các thành viên chưa để họ biết được cần bổ sung ở đâu, và bổ sung bảng chỉ dẫn trong file Plan để các thành viên upload nội dung đúng file tương ứng (01-danh-gia-thanh-vien, 02-mo-ta-bai-toan, 03-tong-quan-yeu-cau, 04-dac-ta-use-cases, 05-prototype-mockup).”*
- **Nội dung AI tạo:**
  - Khởi tạo và chuẩn hóa cấu trúc tệp `reports/template1/06-ai-usage.md` dành riêng cho giai đoạn Template 1, tách biệt hoàn toàn với hồ sơ Template 0 (`reports/07-ai-usage.md`).
  - Lập bảng chỉ dẫn tra cứu vị trí file nộp bài cho từng đầu mục báo cáo tại Mục 1.1 và Mục 1.2 của `PLAN_TEMPLATE1_AND_DEVELOPMENT.md`.
  - Cập nhật checklist nghiệm thu bàn giao trong cả 4 tệp `reports/template1/inputs/{binh,gia-phuc,lam,quy-phuc}.md` và đồng bộ tên tệp bộ 6 sơ đồ UML trong `reports/template1/assets/diagrams/`.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên kiểm tra trạng thái git đảm bảo hồ sơ Template 0 giữ nguyên vẹn 100%, không bị ghi đè.
  - Đối chiếu đường dẫn từng file Markdown trong bảng chỉ dẫn khớp chính xác với cấu trúc thư mục `reports/template1/` trước khi cho phép commit và push.
- **Minh chứng:** File `reports/template1/06-ai-usage.md`, `PLAN_TEMPLATE1_AND_DEVELOPMENT.md` và commit `a47f41f`.

---

### Phiên T1-09: Review chéo nội dung Template 1 trên Google Docs & Chuẩn hóa đặc tả Phân hệ Định danh
- **Thời gian:** 10h15 - 11h45 ngày 10/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm · Reviewer chéo cho Nguyễn Đức Lãm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Dựa trên tài liệu hệ thống hiện tại và nghiệp vụ, giúp tôi review phần bài làm của Lãm (Mục 3.1, 3.2.2, 4.1.4, UC-11..13, 5.4) và nhận xét tổng thể các nội dung còn lại trong bản thảo của nhóm: chỉ ra những chỗ chưa hợp lý, cần sửa lại như thế nào kèm bằng chứng cụ thể. Đồng thời đối soát các góp ý nhận xét cho phần của Bình (tách Guest và Authenticated User trên sơ đồ tổng thể 4.1, sửa đánh số kịch bản phụ A.1a/A.4a trong UC-04 và lược bỏ từ ngữ kỹ thuật sâu ở UC-02).”*
- **Nội dung AI tạo:**
  - Bản phân tích đối chiếu phần bài làm của Nguyễn Đức Lãm với `SRS-master.md` (góp ý làm rõ sự khác biệt giữa Stakeholder dự án và Actor hệ thống tại Mục 3.1, lược bỏ các thành phần nội bộ khỏi hộp trung tâm của Sơ đồ bối cảnh Hình 3.1, rà soát điều kiện tài liệu `READY` vs `published` ở UC-11..13).
  - Nhận xét tổng thể các mục còn lại trong tài liệu nhóm trên Google Docs để đảm bảo tính nhất quán về thuật ngữ, số lượng 19 Use Cases và quy tắc phân quyền.
  - Gợi ý chỉnh sửa văn phong nghiệp vụ hộp đen cho `UC-02` và chuẩn hóa quy tắc đánh số kịch bản phụ (`A.1a`, `A.4a`) khớp với bước kịch bản chính trong `UC-01`..`UC-04`, `UC-16`.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên trực tiếp đọc thẩm định từng điểm nhận xét, chọn lọc các góp ý xác đáng để phản hồi review chéo cho Lãm và các thành viên trên Google Docs.
  - Kiểm tra lại sơ đồ `uc_overall_19_usecases.svg` xác nhận đã tách bạch rõ `Guest` (chỉ nối `UC-01`, `UC-16`) và `Authenticated User` (nối `UC-02`, `UC-03` kèm mũi tên kế thừa tam giác rỗng từ `Customer`, `Support Agent`, `Admin`).
  - Trực tiếp chỉnh sửa câu chữ các bảng đặc tả `UC-01`..`UC-04`, `UC-16` trên Google Docs theo đúng chuẩn nghiệp vụ.
- **Minh chứng:** Các nhận xét review chéo và lịch sử chỉnh sửa trên Google Docs nhóm (`NMCNPM - Clarune - 04`), `reports/template1/TEMPLATE1_DRAFT_MASTER.md`.

---

### Phiên T1-10: Điều phối giao task chuyển đổi Markdown (`SCRUM-65`), Chuẩn hóa Bảng 3.1 Stakeholders & Rà soát tổng thể bản thảo
- **Thời gian:** 10h20 - 11h20 ngày 11/11/2026
- **Tác giả chịu trách nhiệm:** `24120269` - Ngô Viết Thanh Bình (Trưởng nhóm)
- **Công cụ / Model:** Antigravity AI (Gemini 3.8 Flash, Google DeepMind) via Antigravity IDE
- **Prompt đã khử dữ liệu nhạy cảm:**
  > *“Cập nhật lưu ý vào phần giao task: yêu cầu các thành viên chuyển nội dung tương ứng phần mình đảm nhiệm từ Google Docs thành file .md (giữ nguyên 100% nội dung đã chốt; những phần có ảnh chỉ cần ghi tiêu đề ảnh, ảnh thật trưởng nhóm sẽ tự thêm vào bản tổng hợp sau; cập nhật nhật ký AI vào 06-ai-usage.md). Tạo thông báo giao task này trên Jira (deadline trước 23h). Đồng thời đối chiếu đề xuất bảng 9 Stakeholders & Actors với SRS-master.md (chỉ lưu trong bản draft, không đụng vào file riêng của thành viên khác) và kiểm tra toàn bộ nội dung bản thảo để phát hiện các ghi chú nội bộ hoặc lỗi typo còn sót lại.”*
- **Nội dung AI tạo:**
  - Cập nhật quy định chuyển đổi Markdown vào `PLAN_TEMPLATE1_AND_DEVELOPMENT.md` và 4 biên bản bàn giao `reports/template1/inputs/*.md`; khởi tạo Jira Issue `SCRUM-65` thông báo phân công cho cả nhóm.
  - Định dạng bảng 3.1 gồm 9 bên liên quan và tác nhân (bổ sung *Giảng viên hướng dẫn & Bộ môn CNPM*, *Nhóm phát triển phần mềm - Nhóm 4*, *Đơn vị vận hành*, cùng các tác nhân chính và tác nhân ngoài) trong `TEMPLATE1_DRAFT_MASTER.md`.
  - Danh sách rà soát toàn diện các ghi chú phân công nội bộ còn sót lại trong các mục kỹ thuật, các lỗi gõ phím (typo) và điểm cần đồng bộ chú thích hình ảnh trước khi xuất bản.
- **Nội dung tự kiểm chứng & hiệu chỉnh:**
  - Sinh viên yêu cầu hoàn tác ngay thay đổi trên file riêng `03.1-stakeholders.md` để tôn trọng phạm vi công việc của thành viên phụ trách (Lãm), chỉ lưu bảng đề xuất trong `TEMPLATE1_DRAFT_MASTER.md`.
  - Kiểm tra nội dung Jira Issue `SCRUM-65` và gửi thông báo hướng dẫn chi tiết cho các thành viên trong nhóm.
  - Đối chiếu danh sách các ghi chú nội bộ và lỗi chính tả để làm sạch bản thảo chính thức.
- **Minh chứng:** Jira Issue `SCRUM-65`, `reports/template1/TEMPLATE1_DRAFT_MASTER.md`, `reports/template1/inputs/binh.md`.

---

## 6.4 CAM KẾT ĐẠO ĐỨC HỌC THUẬT

Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:
1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.
2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.
