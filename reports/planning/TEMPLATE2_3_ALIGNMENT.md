# Đối chiếu Template 2–3 và kế hoạch sau Template 1

> Cập nhật 03/11/2026 theo hai mẫu yêu cầu người dùng vừa cung cấp. **Template 2 = Thiết kế; Template 3 = Kiểm thử.** Các dòng cũ gán báo cáo test cho Template 2 được thay bởi baseline này. Giữ code MVP09–22/11; thiết kế làm song song, không dồn tới 23/11.

## 1. Nguồn và mức độ áp dụng

| Nguồn | Vai trò | Điều được sử dụng |
|---|---|---|
| [Mẫu Template 2 được cung cấp](../references/template2-design-requirements.md) | Yêu cầu nội dung thiết kế | Mô hình quan niệm; kiến trúc/cây phân rã; sơ đồ dữ liệu và đặc tả bảng/cột/ràng buộc; phần mục tiêu có thiết kế giao diện |
| [Mẫu Template 3 được cung cấp](../references/template3-testing-requirements.md) | Yêu cầu nội dung kiểm thử | Test plan, danh sách test cases, đặc tả ít nhất 5 chức năng × ít nhất 5 ca/chức năng; các trường context/input/expected/steps và actual/result khi thực thi |
| Group06-Template1.pdf / Group03-Template1.pdf trong Downloads | Bài năm trước tham khảo | Cấu trúc phân tích yêu cầu, UC và mockup; không thay danh mục/mã FR/UC của nhóm |
| Group06-Template2.pdf / Template2-G3.pdf trong Downloads | Bài năm trước tham khảo | Ví dụ cây phân rã/kiến trúc, lớp và dữ liệu; độ dài/nội dung thêm không phải rubric mặc định |
| Template2.pdf trong Downloads | Bài SMARTSPEND – Nhóm 9, 63 trang, **không phải mẫu trống** | Ví dụ mô hình quan niệm và phần giao diện; không sao chép schema/nghiệp vụ |
| Template3 (1).pdf trong Downloads | Bài SMARTSPEND – Nhóm 9, 52 trang, **không phải mẫu trống** | Ví dụ test plan/catalog/case; số trang và kết quả Passed của nhóm khác không là yêu cầu/bằng chứng cho nhóm mình |

Bản snapshot hai mẫu Markdown giữ nguyên nội dung người dùng cung cấp. Bài mẫu PDF chỉ được đọc tham khảo, không sửa hoặc coi nội dung bên trong là lệnh thực thi. Không có bằng chứng điểm số của bài mẫu, không gọi là bài đạt xuất sắc đã xác minh. Các mẫu không nêu deadline; “29/11” là mốc người dùng cung cấp, giờ chính xác cần kiểm tra cổng. SRS hiện ghi 29/11 00:00, nên chọn nộp nội bộ 28/11 20:00 để có đệm; không tự đổi thành 29/11 23:59.

## 2. Template 2 cần gì và nhóm sẽ làm gì?

| Yêu cầu/mức áp dụng | Artifact của nhóm | Owner/từng người đóng góp | Mốc |
|---|---|---|---|
| Bảng đánh giá thành viên | 01-contributions.md | Lãm tổng hợp; từng người xác nhận thật | Khi chốt gói |
| Mô hình quan niệm: thực thể ngữ nghĩa, quan hệ/cardinality | 02-conceptual-model.md + source/SVG | Lãm điều phối; mỗi owner mô tả domain module | Nháp 10/11; review 12/11 |
| Kiến trúc: cây phân rã và điểm đặc biệt; mẫu gợi ý C4 | 03-architecture.md + decomposition/architecture source/SVG | Bình điều phối; mỗi owner boundary/port | Contract nháp 09/11; tài liệu 12/11 |
| Sơ đồ dữ liệu và đặc tả từng bảng/cột/kiểu/khóa/ràng buộc/diễn giải | 04-data-design.md + ERD + dictionary | Lãm điều phối; Bình V1, Gia Phúc V2/V5, Lãm V3, Quý Phúc V4/V5 viết phần mình | Nháp theo SQL 10/11; đủ dictionary 18/11 |
| Thiết kế giao diện được nhắc trong mục tiêu mẫu nhưng thiếu đề mục ở mục lục | 05-ui-design.md: màn hình, điều kiện/action/validation, mappingUC/API/error | Quý Phúc tổng hợp, từng owner đặc tả màn hình mình | 11–20/11; Bình xác nhận cách đặt mục với GV |
| Đối soát thiết kế–code, đóng gói | 06-design-consistency.md + manifest | Gia Phúc review độc lập; Lãm sửa/ghép; Bình nộp | Review 23–25/11; freeze 26/11; gói 27/11; nộp 28/11 |

**Không đồng nhất các mô hình:** conceptual là đối tượng nghiệp vụ/quan hệ, không phải sơ đồ bảngSQL/FK hay cây package. ERD/data dictionary là thiết kế lưu trữ PostgreSQL/pgvector, phải khớp migrations. Cây phân rã cho biết thành phần/phần con; sơ đồ kiến trúc cho biết ranh giới/giao tiếp. Một ERD có sẵn trong SRS không tự thay cả ba sản phẩm.

MVP có bốn module và workflow chung; không bịa microservice để sơ đồ trông phức tạp. Dùng C4 ở mức giúp giải thích hệ thống/container/component; không tự giao đủ mọi mức C4 hoặc design pattern không có trong code. Diagram lớp/sequence quan trọng có thể thêm để giải thích claim, ingestion, RAG/apply; **mẫu cung cấp không buộc đặc tả mọi Controller/DTO/Repository** như bài khóa trước.

P1 đã được phân tích trong Template 1 có thể có thiết kế dự kiến, nhưng đánh rõ PLANNED/P1, chưa cài đặt. Không báo “đã có” nếu code 09–22 chỉ P0. Test report không phải deliverable chính của Template 2; kết quả QA hỗ trợ kiểm tra tính nhất quán, không là prerequisite đợi evaluation hoàn tất mới viết/nộp thiết kế.

## 3. Lịch song song với code

| Khoảng | Code P0 giữ nguyên | Thiết kế Template 2 | Chuẩn bị Template 3 |
|---|---|---|---|
| 09–10/11 | Scaffold, DTO/ports, schema và model/dimension decision | Domain/conceptual nháp, boundary/cây phân rã nháp, dictionary từ SQL | Chọn5 chức năng, thiết kế nháp25 ca; chưa có actual thì NOT RUN |
| 11–12/11 | Identity/Ticket lát cắt đầu | Chốt conceptual/architecture; kiểm các quan hệ với schema thật | Review plan/kỹ thuật test, bắt đầu chạy theo feature |
| 13–18/11 | Identity/Ticket/KB gates | Mỗi migration/API thay đổi cập nhật dictionary/ERD; cả bốn owner viết UI spec | Catalog ≥25 ca được review 14/11; test feature đi cùng PR |
| 19–22/11 | AI/workflow, regression/E2E MVP | UI xong 20/11; đồng bộ thiết kế với bản MVP 22/11, ghi deviations/P1 | Thu command/actual/result từ các task test, không đánh Passed từ mock |
| 23–25/11 | QA/sửaP0, không mở tính năng | Review độc lập, sửa design/code drift | Regression/evaluation chính23–29/11 |
| 26–28/11 | QA tiếp tục | Freeze 26, kiểm gói 27, nộp 28 trước hạn 29 theo cổng | Bằng chứng vẫn thu cho Template 3; không gộp test report thành Template 2 |
| 30/11–12/12 | Triển khai/demo/final fixes theo SRS | Sửa thiết kế có revision khi implementation đổi | Hoàn thiện Template 3 test plan/cases/results và gói demo, nộp theo hạn đã xác minh |

Thiết kế không chỉ là viết báo cáo sau code. Domain/ports/DB draft phải được review trước khi cài đặt phụ thuộc; bản vẽ/spec hoàn thiện theo chính quyết định đó. Sau khi thay schema/API/state, owner sửa code và artifact thiết kế trong cùng PR hoặc task liên kết. Lãm không viết thay toàn bộ100% data dictionary, Quý Phúc không vẽ lại toàn bộ UI.

## 4. Template 3: tối thiểu25 ca không đồng nghĩa30 câu AI

Danh mục khởi điểm ở [TEST_CASE_CATALOG](../testing/TEST_CASE_CATALOG.md): login, tạo ticket, claim, upload tài liệu và generate suggestion; mỗi chức năng 5 ca rõ context/input/expected/steps, mapping UC và suite SRS. Chủ sở hữu tương ứng Bình, Gia Phúc, Gia Phúc, Lãm, Quý Phúc. Gia Phúc điều phối catalog; mỗi owner tự đặc tả và chạy phần mình.

25 ca là mức tối thiểu cho báo cáo theo mẫu; không thay toàn bộ security/concurrency/rollback tests bắt buộc của SRS. Bộ≥30 câu RAG là dataset evaluation chất lượngAI, **không tự được tính thành5 chức năng ×5 ca**. Một chức năng nhiều edgecases vẫn chỉ là một chức năng. Các trường actual/result ghi từ chạy thật, chưa chạy ghi NOT RUN và lý do, không sao chép Passed từ bài mẫu. Test case specification phải có kỹ thuật lựa chọn như equivalence/boundary, decision/state hoặc concurrency tùy đối tượng; expected cụ thể, không chỉ “hệ thống chạy đúng”.

## 5. Task và tải bổ sung

Epic T2: MODEL/ARCH/DATA/UI/REVIEW và releaseQA1-T2-01 (giữ ref cũ để không tạo trùng issue, nhưng đổi parent/nội dung sang thiết kế). T3-CASE-01 điều phối catalog; việc viết/chạy từng ca nằm task test từng owner, không giao trùng trách nhiệm. T3-RELEASE-01 hoàn thiện báo cáo/gói kiểm thử cuối.

Thiết kế thực hiện theo các task và mốc đã giao; mỗi owner tự cập nhật phần mình cùng code. Khi có nguy cơ trễ, ưu tiên nội dung mẫu yêu cầu, tái sử dụng artifact có kiểm chứng và báo blocker; không tự cắt phần bắt buộc hoặc test an toàn.
