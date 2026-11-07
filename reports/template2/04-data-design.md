# 4. Thiết kế dữ liệu

> Task [T2-DATA-01](../../TASK_PLAYBOOK_TEMPLATE1.md#t2-data-01), Lãm điều phối, bốn owner tựđiềnbảngmình; nhápđicùngSQL 10/11, đủdictionary 18/11. Nguồn [mẫu](../references/template2-design-requirements.md)4.1/4.2, [SRS](../SRS-master.md)10 và[MVP_CONTRACTS](../MVP_CONTRACTS.md)3.

## 4.1. Sơ đồ dữ liệu

TODO: ERD vật lý,PK/FK/cardinality/check/enum, thểhiệnquan hệ nhưngđừngchồngnhãn ởA4. Khớpmigrations thực tếvàvector model/dimension đãchốt. Source/SVG ởassets/diagrams/data-erd.drawio/.svg.

## 4.2. Đặc tả dữ liệu

| Bảng | Owner đặc tả | Nguồn schema |
|---|---|---|
| users, auth_sessions | Bình | V1 |
| tickets, ticket_messages, ticket_events | Gia Phúc | V2; FKsuggestion V5 |
| knowledge_documents, knowledge_ingestion_jobs, knowledge_chunks | Lãm | V3 |
| ai_suggestions, ai_suggestion_sources | Quý Phúc | V4; phối hợpV5 |

Với **mỗi bảng/mỗi cột** dùngmẫu: không chỉghi tênbảng. SQL/ORMkhông tựthaydiễngiảinghiệp vụ.

| Cột | Kiểu PostgreSQL | Ý nghĩa | Nullable/default | PK/FK/unique/check/domain | Index/lý do | Implementation/PLANNED |
|---|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO | TODO |

TODO: metadata/privatefile/volume, phạmvivectorcorpus, lease/attempts/uniqueactivejob, source snapshots vàuniqueapply. Khônglog/đínhsecrets. NếuP1 chưa cómigration thì ghiPLANNED, không làmnhư bảngđãtồn tại.
