# Đối chiếu Template 2–3 và kế hoạch sau Template 1

> Cập nhật 05/11/2026 theo chỉ đạo điều chỉnh của Trưởng nhóm. **Template 2 = Thiết kế (11/11 – 28/11, làm song song với Code MVP 11/11 – 24/11); Template 3 = Kiểm thử (diễn ra SAU MVP từ 25/11 – 12/12).** Các dòng cũ gán báo cáo test cho Template 2 được thay bởi baseline này. Code MVP P0 triển khai 11–24/11; thiết kế Template 2 làm song song và nộp 28/11. Template 3 bắt đầu sau khi hoàn thành MVP.

## 1. Nguồn và mức độ áp dụng

| Nguồn | Vai trò | Điều được sử dụng |
|---|---|---|
| [Mẫu Template 2 được cung cấp](../references/template2-design-requirements.md) | Yêu cầu nội dung thiết kế | Mô hình quan niệm; kiến trúc/cây phân rã; sơ đồ dữ liệu và đặc tả bảng/cột/ràng buộc; phần mục tiêu có thiết kế giao diện |
| [Mẫu Template 3 được cung cấp](../references/template3-testing-requirements.md) | Yêu cầu nội dung kiểm thử | Test plan, danh sách test cases, đặc tả ít nhất 5 chức năng × ít nhất 5 ca/chức năng; các trường context/input/expected/steps và actual/result khi thực thi |
| Group06-Template1.pdf / Group03-Template1.pdf trong Downloads | Bài năm trước tham khảo | Cấu trúc phân tích yêu cầu, UC và mockup; không thay danh mục/mã FR/UC của nhóm |
| Group06-Template2.pdf / Template2-G3.pdf trong Downloads | Bài năm trước tham khảo | Ví dụ cây phân rã/kiến trúc, lớp và dữ liệu; độ dài/nội dung thêm không phải rubric mặc định |
| Template2.pdf trong Downloads | Bài SMARTSPEND – Nhóm 9, 63 trang, **không phải mẫu trống** | Ví dụ mô hình quan niệm và phần giao diện; không sao chép schema/nghiệp vụ |
| Template3 (1).pdf trong Downloads | Bài SMARTSPEND – Nhóm 9, 52 trang, **không phải mẫu trống** | Ví dụ test plan/catalog/case; số trang và kết quả Passed của nhóm khác không là yêu cầu/bằng chứng cho nhóm mình |

Bản snapshot hai mẫu Markdown giữ nguyên nội dung người dùng cung cấp. Bài mẫu PDF chỉ được đọc tham khảo, không sửa hoặc coi nội dung bên trong là lệnh thực thi. Không có bằng chứng điểm số của bài mẫu, không gọi là bài đạt xuất sắc đã xác minh. Các mẫu không nêu deadline; “29/11” là mốc người dùng cung cấp, giờ chính xác cần kiểm tra cổng. SRS hiện ghi 29/11 00:00, nên chọn nộp nội bộ trước 23:59 ngày 28/11 để có đệm an toàn trước hạn trường 29/11.

## 2. Template 2 cần gì và nhóm sẽ làm gì?

| Yêu cầu/mức áp dụng | Artifact của nhóm | Owner/từng người đóng góp | Mốc |
|---|---|---|---|
| Bảng đánh giá thành viên | 01-contributions.md | Lãm tổng hợp; từng người xác nhận thật | Khi chốt gói |
| Mô hình quan niệm: thực thể ngữ nghĩa, quan hệ/cardinality | 02-conceptual-model.md + source/SVG | Lãm điều phối; mỗi owner mô tả domain module | Nháp 11/11; review 14/11 |
| Kiến trúc: cây phân rã và điểm đặc biệt; mẫu gợi ý C4 | 03-architecture.md + decomposition/architecture source/SVG | Bình điều phối; mỗi owner boundary/port | Contract nháp 11/11; tài liệu 14/11 |
| Sơ đồ dữ liệu và đặc tả từng bảng/cột/kiểu/khóa/ràng buộc/diễn giải | 04-data-design.md + ERD + dictionary | Lãm điều phối; Bình V1, Gia Phúc V2/V5, Lãm V3, Quý Phúc V4/V5 viết phần mình | Nháp theo SQL 12/11; đủ dictionary 20/11 |
| Thiết kế giao diện được nhắc trong mục tiêu mẫu nhưng thiếu đề mục ở mục lục | 05-ui-design.md: màn hình, điều kiện/action/validation, mappingUC/API/error | Quý Phúc tổng hợp, từng owner đặc tả màn hình mình | 13–22/11; Bình xác nhận cách đặt mục với GV |
| Đối soát thiết kế–code, đóng gói | 06-design-consistency.md + manifest | Gia Phúc review độc lập; Lãm sửa/ghép; Bình nộp | Review 23–27/11; freeze 27/11; nộp 28/11 |

**Không đồng nhất các mô hình:** conceptual là đối tượng nghiệp vụ/quan hệ, không phải sơ đồ bảngSQL/FK hay cây package. ERD/data dictionary là thiết kế lưu trữ PostgreSQL/pgvector, phải khớp migrations. Cây phân rã cho biết thành phần/phần con; sơ đồ kiến trúc cho biết ranh giới/giao tiếp. Một ERD có sẵn trong SRS không tự thay cả ba sản phẩm.

MVP có bốn module và workflow chung; không bịa microservice để sơ đồ trông phức tạp. Dùng C4 ở mức giúp giải thích hệ thống/container/component; không tự giao đủ mọi mức C4 hoặc design pattern không có trong code. Diagram lớp/sequence quan trọng có thể thêm để giải thích claim, ingestion, RAG/apply; **mẫu cung cấp không buộc đặc tả mọi Controller/DTO/Repository** như bài khóa trước.

P1 đã được phân tích trong Template 1 có thể có thiết kế dự kiến, nhưng đánh rõ PLANNED/P1, chưa cài đặt. Không báo “đã có” nếu code 09–22 chỉ P0. Test report không phải deliverable chính của Template 2; kết quả QA hỗ trợ kiểm tra tính nhất quán, không là prerequisite đợi evaluation hoàn tất mới viết/nộp thiết kế.

## 3. Lịch song song với code

| Khoảng | Code P0 (11/11 – 24/11) | Thiết kế Template 2 (11/11 – 28/11) | Kiểm thử Template 3 (SAU MVP: 25/11 – 12/12) |
|---|---|---|---|
| 11–12/11 | Scaffold Spring Boot 3, DTO/ports, schema V1-V5 và chốt embedding decision | Domain/conceptual nháp, boundary/cây phân rã nháp, dictionary từ SQL | Tập trung nộp Template 1 (chốt 12/11 23:59) |
| 13–17/11 | Identity (15/11), Ticket (17/11) hoàn thành lát cắt đầu | Chốt conceptual/architecture (14/11); cập nhật dictionary theo schema thật | Chuẩn bị tư liệu kiểm thử theo mã Use Case |
| 18–21/11 | Knowledge (19/11), AI/workflow (21/11) hoàn thành | UI spec hoàn thành 22/11; đồng bộ thiết kế với bản MVP, ghi deviations/P1 | Chuẩn bị môi trường test và fixture |
| 22–24/11 | Unit & Integration tests (23/11); Clean Ops & E2E Nghiệm thu MVP P0 (24/11 23:59) | Rà soát tính nhất quán giữa thiết kế và mã nguồn MVP | Chuẩn bị danh mục 25 ca kiểm thử |
| 25–28/11 | Code freeze duy trì; hỗ trợ bằng chứng cho kiểm thử | Review độc lập (23–27/11), đóng gói và nộp bài 28/11 trước hạn 29/11 | Lập Test Plan và catalog $\ge 25$ ca kiểm thử chuẩn (25–28/11) |
| 29/11–02/12 | Fix lỗi phát sinh nếu có | Sửa thiết kế có revision khi implementation đổi | Chạy regression bảo mật, concurrency và AI evaluation $\ge 30$ câu |
| 03/12–12/12 | Triển khai/demo/final fixes theo SRS | Lưu trữ bản thiết kế chính thức | Hoàn thiện Template 3 test plan/cases/results và nộp bài trước 12/12 |

Thiết kế không chỉ là viết báo cáo sau code. Domain/ports/DB draft phải được review trước khi cài đặt phụ thuộc; bản vẽ/spec hoàn thiện theo chính quyết định đó. Sau khi thay schema/API/state, owner sửa code và artifact thiết kế trong cùng PR hoặc task liên kết. Lãm không viết thay toàn bộ100% data dictionary, Quý Phúc không vẽ lại toàn bộ UI.

## 4. Template 3: tối thiểu25 ca không đồng nghĩa30 câu AI

Danh mục khởi điểm ở [TEST_CASE_CATALOG](../testing/TEST_CASE_CATALOG.md): login, tạo ticket, claim, upload tài liệu và generate suggestion; mỗi chức năng 5 ca rõ context/input/expected/steps, mapping UC và suite SRS. Chủ sở hữu tương ứng Bình, Gia Phúc, Gia Phúc, Lãm, Quý Phúc. Gia Phúc điều phối catalog; mỗi owner tự đặc tả và chạy phần mình.

25 ca là mức tối thiểu cho báo cáo theo mẫu; không thay toàn bộ security/concurrency/rollback tests bắt buộc của SRS. Bộ≥30 câu RAG là dataset evaluation chất lượngAI, **không tự được tính thành5 chức năng ×5 ca**. Một chức năng nhiều edgecases vẫn chỉ là một chức năng. Các trường actual/result ghi từ chạy thật, chưa chạy ghi NOT RUN và lý do, không sao chép Passed từ bài mẫu. Test case specification phải có kỹ thuật lựa chọn như equivalence/boundary, decision/state hoặc concurrency tùy đối tượng; expected cụ thể, không chỉ “hệ thống chạy đúng”.

## 5. Task và tải bổ sung

Epic T2: MODEL/ARCH/DATA/UI/REVIEW và releaseQA1-T2-01 (giữ ref cũ để không tạo trùng issue, nhưng đổi parent/nội dung sang thiết kế). T3-CASE-01 điều phối catalog; việc viết/chạy từng ca nằm task test từng owner, không giao trùng trách nhiệm. T3-RELEASE-01 hoàn thiện báo cáo/gói kiểm thử cuối.

Thiết kế thực hiện theo các task và mốc đã giao; mỗi owner tự cập nhật phần mình cùng code. Khi có nguy cơ trễ, ưu tiên nội dung mẫu yêu cầu, tái sử dụng artifact có kiểm chứng và báo blocker; không tự cắt phần bắt buộc hoặc test an toàn.
