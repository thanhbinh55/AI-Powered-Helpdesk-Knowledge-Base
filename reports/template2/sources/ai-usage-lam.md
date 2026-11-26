# Nhật ký sử dụng AI — Template 2 (Nguyễn Đức Lãm - `24120083`)

> - **Dự án** AI-Powered Helpdesk & Knowledge Base (Clarune).
> - **Nhóm** Nhóm 04, môn Nhập môn Công nghệ Phần mềm (CS10014), Trường ĐHKHTN, ĐHQG-HCM.
> - **Phần em phụ trách** Mục 1 và 2 (`SCRUM-58`), mục 4.1 và 4.2 (`SCRUM-60`).
> - **Thư mục bàn giao** [docs/template2/members/lam/](../../docs/template2/members/lam/)
> - **Chuẩn quy định:** Mỗi phiên ghi đủ 7 trường bắt buộc theo quy định Khoa CNTT & `TEAM_GUIDE_PHASE2.md` (Thời gian, Tác giả, Công cụ/Model, Prompt đã khử dữ liệu nhạy cảm, Nội dung AI tạo, Nội dung tự kiểm chứng & hiệu chỉnh, Minh chứng/Commit).

## 1. Bảng tổng hợp các phiên sử dụng AI

| Mã phiên | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | Phần AI hỗ trợ và kết quả em kiểm tra | Minh chứng / Commit |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **T2-01** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Phác thảo mô hình quan niệm EER (mục 2) | Em xác định phạm vi và yêu cầu thể hiện ISA. Codex hỗ trợ phác thảo sơ đồ Chen và xuất ảnh PNG để em đối chiếu với SRS và đặc tả nghiệp vụ đã được nhóm thống nhất. | `SCRUM-58`, `aeee95e` (nguồn draw.io và PNG) |
| **T2-02** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Phác thảo Physical ERD (mục 4.1) | Em cung cấp quyết định của nhóm về `gemini-embedding-2` với đầu ra 768 chiều. Codex hỗ trợ dựng Hình 4.1 từ đặc tả để em đối chiếu các cột và khóa với mục 4.2. | `SCRUM-60`, `aa7e99c` (nguồn draw.io và PNG) |
| **T2-03** | Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Soạn bản nháp Flyway V1–V5 để đối chiếu mục 4.2 | Em xác nhận tên V2, cách sinh UUID, mô hình nhúng và số chiều đầu ra, rồi cung cấp quy ước V5 của nhóm. Codex dựa trên các thông tin đó để soạn năm tệp SQL nháp. | `SCRUM-60`, bản nháp tại `backend/src/main/resources/db/migration/` |
| **T2-04** | 23/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex, LibreOffice để xem bố cục | Đối chiếu bản nháp Template 2 với kho mã nguồn | Codex liệt kê các điểm chưa nhất quán và lỗi trình bày. Em đối chiếu các nhận xét với quyết định của nhóm, trong đó có tên chỉ mục ở Bảng 4.4. | Báo cáo rà soát bản Word, liên quan `SCRUM-58` và `SCRUM-60` |
| **T2-05** | 26/11/2026 | Nguyễn Đức Lãm (`24120083`) | OpenAI Codex | Chuyển mục 1, 2 và 4 từ bản Word đã chốt sang Markdown | Em chọn bản Word làm nguồn, xác nhận phạm vi chuyển đổi và commit ba tệp bàn giao. Codex hỗ trợ chuyển định dạng và đối chiếu nội dung, bảng và chú thích hình với Word. | `aeee95e` (`SCRUM-58`), `aa7e99c` (`SCRUM-60`) |

## 2. Chi tiết từng phiên sử dụng AI

### Phiên T2-01 — Phác thảo và đối chiếu sơ đồ EER

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Dựa vào SRS và các tài liệu đặc tả nghiệp vụ Clarune đã được nhóm thống nhất, hãy đề xuất danh sách thực thể và quan hệ cho mục 2. Ghi lực lượng min–max và quy tắc nghiệp vụ tương ứng. Phác thảo sơ đồ Chen với quan hệ kế thừa ISA từ `User` đến `Customer`, `Support Agent` và `System Administrator`. Thể hiện quan hệ nghiệp vụ trên hình và bỏ các FK vật lý như `ticket_id`. Chuẩn bị tệp nguồn draw.io và xuất ảnh PNG. Sau khi xuất ảnh, hãy đối chiếu tên thực thể, các nhánh ISA, quan hệ và lực lượng trên PNG với những tài liệu nhóm đã thống nhất. Ghi rõ điểm chưa khớp và nguồn tương ứng để em kiểm tra.

* **5. Nội dung AI tạo** Bản phác thảo EER cho Hình 2.1, gồm tệp nguồn draw.io và ảnh PNG.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em dùng SRS và các tài liệu đặc tả nghiệp vụ nhóm đã thống nhất để đối chiếu tên thực thể, quan hệ và lực lượng trên ảnh PNG. Em kiểm tra phần ISA thể hiện mỗi `User` thuộc đúng một trong ba kiểu con. Các FK vật lý được trình bày ở mục thiết kế dữ liệu.
* **7. Minh chứng / Commit** `SCRUM-58`. Commit `aeee95eb635de08158cc51535531be55fb402e4f` ghi nhận tệp nguồn và ảnh Hình 2.1. [Draw.io](../../docs/template2/assets/diagrams/conceptual-model.drawio) · [PNG](../../docs/template2/assets/diagrams/conceptual-model.png)

### Phiên T2-02 — Phác thảo Physical ERD cho Hình 4.1

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Dùng Data Dictionary ở mục 4.2 để phác thảo Physical ERD cho PostgreSQL. Ghi đủ tên bảng, tên cột, kiểu dữ liệu, khả năng nhận `NULL`, PK, FK và ràng buộc duy nhất. Mô hình nhúng nhóm đã chốt là Google `gemini-embedding-2` với đầu ra 768 chiều, nên cột `knowledge_chunks.embedding` có kiểu `vector(768)`. Thể hiện FK và chỉ mục duy nhất có điều kiện của `source_suggestion_id` được thêm ở V5. Xuất PNG vào `docs/template2/assets/diagrams/physical-erd.png` và liệt kê những chỗ cần đối chiếu với mục 4.2.

* **5. Nội dung AI tạo** Bản draw.io và PNG cho lược đồ 10 bảng P0. Hình ghi kiểu `vector(768)` và đánh dấu liên kết được bổ sung trong V5.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em xác nhận số chiều của vector nhúng trước khi đưa hình vào tài liệu và dùng Data Dictionary để đối chiếu tên cột, kiểu dữ liệu và các khóa trên hình. Em lưu ý `source_suggestion_id` cho phép `NULL`. Mỗi giá trị khác `NULL` chỉ được xuất hiện một lần.
* **7. Minh chứng / Commit** `SCRUM-60`. Commit `aa7e99c5a5b9e5d98c0141d9ea130d7c8299e555` chứa sơ đồ nguồn và ảnh. [Draw.io](../../docs/template2/assets/diagrams/physical-erd.drawio) · [PNG](../../docs/template2/assets/diagrams/physical-erd.png)

### Phiên T2-03 — Soạn bản nháp Flyway V1–V5

* **1. Thời gian** Đợt soạn thiết kế, trước lần rà soát ngày 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Giải thích từng migration V1–V5 và chỉ ra bảng đặc tả tương ứng. Dựa vào đó, soạn bản nháp SQL trong `backend/src/main/resources/db/migration/` để đối chiếu kiểu dữ liệu, giá trị mặc định, khóa và chỉ mục. Dùng tên `V2__init_ticketing.sql` và để ứng dụng sinh UUID. Trong V3, bật pgvector trước khi tạo cột `vector(768)`. V2 khai báo cột `source_suggestion_id` cho phép `NULL`. Sau khi V4 tạo `ai_suggestions`, V5 mới thêm FK và chỉ mục duy nhất có điều kiện theo quy ước của nhóm.

* **5. Nội dung AI tạo** Năm bản nháp `V1__init_identity.sql`, `V2__init_ticketing.sql`, `V3__init_knowledge.sql`, `V4__init_ai.sql` và `V5__add_ticket_message_suggestion_fk.sql`. Bản nháp V5 dùng tên `idx_unique_applied_suggestion` theo ảnh quy ước của nhóm tại thời điểm đó.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em chốt tên V2 và cách sinh UUID trước khi cung cấp yêu cầu cho Codex. Khi rà soát mục 4, em dùng kết quả đối chiếu SQL để kiểm tra lại tên cột, điều kiện của chỉ mục duy nhất và thứ tự thêm FK. Việc chạy Flyway trên PostgreSQL 16 là bước kiểm tra riêng.
* **7. Minh chứng / Commit** `SCRUM-60` và năm bản nháp SQL trong `backend/src/main/resources/db/migration/`. Commit `aa7e99c` là minh chứng cho phần thiết kế mục 4 và Physical ERD.

### Phiên T2-04 — Rà soát bản nháp Word

* **1. Thời gian** 23/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex, LibreOffice để xem bố cục.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Đọc bản nháp Word Template 2 và đối chiếu với SRS, MVP Contracts cùng các tệp hiện có trong kho mã nguồn. Chia nhận xét thành mâu thuẫn nội dung, thông tin chưa rõ hoặc chưa đồng bộ, lỗi định dạng và góp ý cải thiện. Ghi số mục, bảng, hình hoặc trang và nguồn cần xem lại để thành viên phụ trách có căn cứ quyết định cách sửa.

* **5. Nội dung AI tạo** Báo cáo ghi vị trí của từng vấn đề. Trong phần em phụ trách, dòng V1 vẫn nhắc `pgcrypto` dù ứng dụng sinh UUID, tên chỉ mục ở Bảng 4.4 lệch với SQL và tên mô hình nhúng chưa được ghi nhất quán trong phần chữ. Báo cáo cũng đánh dấu những sơ đồ khó đọc khi đặt trên trang dọc.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em đối chiếu các nhận xét về V1 và mô hình nhúng với quyết định của nhóm. Đối với Bảng 4.4, em xác nhận trong trao đổi tên chỉ mục cần dùng là `idx_msg_source_unique_applied_suggession`. Khi chuyển định dạng ở phiên sau, em dùng bản Word đã chốt làm nguồn cho nội dung Markdown.
* **7. Minh chứng / Commit** Bản nháp `[SE - Nhóm 4] Template2-ThietKe-Clarune-04.docx` và báo cáo rà soát ngày 23/11/2026. Hai commit `aeee95e` và `aa7e99c` ghi nhận các tệp em bàn giao.

### Phiên T2-05 — Chuyển mục 1, 2 và 4 từ Word sang Markdown

* **1. Thời gian** 26/11/2026.
* **2. Tác giả** Nguyễn Đức Lãm (MSSV `24120083`).
* **3. Công cụ / Model** OpenAI Codex.
* **4. Prompt đã khử dữ liệu nhạy cảm**

  > Chuyển mục 1, 2 và 4 từ bản Word Template 2 đã chốt sang ba tệp Markdown trong `docs/template2/members/lam/`. Đặt tên theo tiêu đề mục, bỏ dấu và nối các từ bằng gạch ngang. Giữ nguyên thứ tự tiêu đề, câu chữ và nội dung ô bảng. Bỏ ảnh nhúng và giữ chú thích Hình 2.1, Hình 4.1. Đối chiếu nội dung hiển thị trong Markdown với Word và ghi lại kết quả để em xem trước khi commit.

* **5. Nội dung AI tạo** Ba tệp Markdown và kết quả đối chiếu từng đoạn, từng ô của 17 bảng. Hai chú thích hình được giữ ở mục 2.2 và 4.1.
* **6. Nội dung tự kiểm chứng & hiệu chỉnh** Em chọn bản Word đã chốt, xác nhận ba mục cần chuyển và duyệt tên tệp trước khi ghi. Em dựa vào kết quả đối chiếu để xem lại phần bàn giao. Khi chuyển định dạng, em giữ câu chữ theo bản Word, kể cả tên chỉ mục `idx_msg_source_suggestion_unique` ở Bảng 4.4.
* **7. Minh chứng / Commit** Nhánh `docs/t2-lam`. Commit `aeee95e` lúc 09:21:17 (+07:00) chứa mục 1–2 (`SCRUM-58`). Commit `aa7e99c` lúc 09:24:07 (+07:00) chứa mục 4 (`SCRUM-60`). [Mục 1](../../docs/template2/members/lam/danh-gia-dong-gop-cac-thanh-vien.md) · [Mục 2](../../docs/template2/members/lam/mo-hinh-quan-niem.md) · [Mục 4](../../docs/template2/members/lam/thiet-ke-du-lieu.md)
