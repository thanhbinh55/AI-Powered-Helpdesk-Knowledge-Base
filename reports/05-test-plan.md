# Kế hoạch kiểm thử — baseline MVP P0

> Cập nhật 03/11/2026. Test từng module cùng code 09–21/11; E2E tăng dần 12–22/11; QA/evaluation tổng thể 23–29/11. Mã test chuẩn và kỳ vọng ở [SRS 14.2](SRS-master.md), chi tiết transaction/fault cases ở [MVP_CONTRACTS Mục 9](MVP_CONTRACTS.md).

| Owner | Task ref | Coverage bắt buộc |
|---|---|---|
| Bình | T1-TST-ID | TC-ID-01..06: role escalation, credential sai, rotation/disabled, happy path và cookie/CSRF |
| Gia Phúc | T1-TST-TK | TC-TK-01..08, TC-CON-01/02: ownership/internal note, state, version và event rollback |
| Lãm | T1-TST-KB | TC-KB-01..07: parser/file security, publish/archive, lease/retry/crash/stale completion |
| Quý Phúc + Gia Phúc hỗ trợ workflow | T1-TST-AI | TC-AI-01..07, TC-WF-01..04: RAG/citation/failures, apply/discard races, rollback và quyền hiện tại |
| Lãm | T1-OPS-01 | TC-OPS-01: README/môi trường sạch, migration, volume và lỗi provider |
| Gia Phúc điều phối | T1-TST-01 / T1-INT-01 | Tổng hợp kết quả và E2E; không viết thay test của mọi người |

Unit test cho pure rules/fake provider; integration/concurrency dùng PostgreSQL/pgvector thật, không thay bằng H2 để chứng minh lock/vector. Hai transaction/connection + barrier cho claim/version/send races. Frontend mới có build script; nếu chọn công cụ test phải cấu hình và chứng minh chạy, không ghi Jest/Vitest là đã có.

Mock provider kiểm tra orchestration/DTO/lỗi, không chứng minh semantic retrieval hay grounded answer. Live smoke không thay evaluation ≥30 câu có nhãn. Provider live lỗi phải trả lỗi rõ, Ticket vẫn dùng; không âm thầm chuyển sang câu trả lời mock. Mỗi kết quả ghi mode/model/dimension/dataset và actual/expected.

DoD: test liên quan pass và có bằng chứng, không còn blocker P0, quyền/transaction/AI lỗi được kiểm tra. Không áp đặt coverage 70% chưa có căn cứ; nếu đo thì ghi command/công cụ/kết quả thật. NFR AI/hiệu năng chỉ kết luận sau phép đo theo SRS 8/12; chưa chạy là NOT RUN. Kết quả tại [06-test-results.md](06-test-results.md), không suy PASS từ task Done hoặc PR merge.

## Template 3 — yêu cầu báo cáo và sốcase

[Mẫu kiểm thử](references/template3-testing-requirements.md) yêu cầu ít nhất5 chức năng, mỗi chức năng5ca được đặc tả. [Catalog](testing/TEST_CASE_CATALOG.md) có25 dòngkhởiđiểm trên5 chức năng; từng owner phải điền form context/input/expected/steps vàactual/resulttheo chạy thật trong[template3/03-test-cases.md](template3/03-test-cases.md). Gia PhúcT3-CASE-01 điềuphối09–14/11; không đếm≥30 câuRAG thay5 chức năng. Template 2nộp29/11 là thiết kế, test artifacts dành Template 3.
