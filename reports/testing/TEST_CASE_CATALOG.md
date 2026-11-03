# Catalog test case báo cáo Template 3 — khởi điểm 25 ca

Đây là kế hoạch **5 chức năng × 5 ca**, theo [mẫu kiểm thử](../references/template3-testing-requirements.md), chưa phải báo cáo kết quả. Gia Phúc điều phối T3-CASE-01; mỗi owner tự đặc tả và chạy phần mình. Report IDs RPT-* là dòng báo cáo, liên kết tới suite TC-* trong [SRS 14.2](../SRS-master.md), không đổi nghĩa các mã test hiện có.

Owner cần điền đủ Context, Input Data, Expected Output và Test steps cụ thể trong [Template 3](../template3/03-test-cases.md), review trước 14/11. Actual/Result lấy từ chạy thật; trước đó là NOT RUN. Biên subject 5–150 và description 10–5000 lấy SRS 4.2; thay validation phải cập nhật expected. Với file giả mạo, cần chốt một mã HTTP cụ thể 400 hoặc 415 trong OpenAPI trước khi chạy, không chọn tùy ý khi chấm.

25 ca này không thay toàn bộ test quyền, concurrency, rollback, lease, send/discard của SRS. Dataset ≥30 câu RAG là phép đánh giá chất lượng AI riêng, không tự thay 5 chức năng × 5 ca.

## Đăng nhập — Bình

Related UC UC-01; nguồn FR-ID-02/03/08.

| Report ID | Tên case | Context/input dự kiến | Expected dự kiến cần review | Suite/requirement mapping | Actual/result |
|---|---|---|---|---|---|
| RPT-LOGIN-01 | Thông tin hợp lệ | Email/tài khoản enabled, đúng mật khẩu | 200, access/refresh đúng role, không lộ password | TC-ID-05 | NOT RUN |
| RPT-LOGIN-02 | Sai mật khẩu | Email có thật, mật khẩu sai | 401 generic error, không tạo phiên | TC-ID-02 | NOT RUN |
| RPT-LOGIN-03 | Email không tồn tại | Email không có trong fixture | 401 cùng thông báo generic, không leak existence | TC-ID-02 | NOT RUN |
| RPT-LOGIN-04 | Thiếu mật khẩu | Password rỗng/thiếu | 400 validation, không tạo phiên | FR-ID-02 validation | NOT RUN |
| RPT-LOGIN-05 | Tài khoản disabled | Credential đúng nhưng enabled=false | 403/account disabled theo contract, không cấp phiên | TC-ID-04 | NOT RUN |

## Tạo ticket — Gia Phúc

Related UC UC-05; nguồn FR-TK-01.

| Report ID | Tên case | Context/input dự kiến | Expected dự kiến cần review | Suite/requirement mapping | Actual/result |
|---|---|---|---|---|---|
| RPT-CREATE-01 | Payload hợp lệ | Customer đã login,subject/description hợp lệ | 201 OPEN/NORMAL, ticket + public message đầu + event cùng commit | TC-TK-01 | NOT RUN |
| RPT-CREATE-02 | Subject dưới biên | Subject 4 ký tự | 400 validation,không tạo ticket/message/event | FR-TK-01 validation | NOT RUN |
| RPT-CREATE-03 | Subject vượt biên | Subject 151 ký tự | 400 validation,không tạo dữ liệu | FR-TK-01 validation | NOT RUN |
| RPT-CREATE-04 | Description dưới biên | Description 9 ký tự | 400 validation,không tạo dữ liệu | FR-TK-01 validation | NOT RUN |
| RPT-CREATE-05 | Không xác thực | POST hợp lệ nhưng thiếu token | 401,không tạo ticket | FR-ID-07 | NOT RUN |

## Nhận ticket — Gia Phúc

Related UC UC-07; nguồn FR-TK-04,BR-05/06.

| Report ID | Tên case | Context/input dự kiến | Expected dự kiến cần review | Suite/requirement mapping | Actual/result |
|---|---|---|---|---|---|
| RPT-CLAIM-01 | Claim OPEN hợp lệ | EnabledAgent,OPEN/unassigned | 200/đúngagent,IN_PROGRESS,versiontăng,event cùng commit | TC-TK-05 | NOT RUN |
| RPT-CLAIM-02 | Hai Agent cùng claim | Hai transaction/barriercùngOPEN | Một success,một409,tốiđamộtassignee/eventclaimthắng | TC-CON-01 | NOT RUN |
| RPT-CLAIM-03 | Claim lại | CùngAgent claim lạiticketđãnhận | 409,không eventclaimthứhai | TC-TK-05 conflict | NOT RUN |
| RPT-CLAIM-04 | Customer claim | Customer gọi endpointclaim | 403,không đổidữ liệu | FR-ID-07 | NOT RUN |
| RPT-CLAIM-05 | Ticket không truy cập | Ticketkhôngtồntại hoặc ngoàiownership | 404 thốngnhấtpolicy,không leak | TC-TK-03/FR-ID-07 | NOT RUN |

## Tải lên tài liệu — Lãm

Related UC UC-11; nguồn FR-KB-01..05.

| Report ID | Tên case | Context/input dự kiến | Expected dự kiến cần review | Suite/requirement mapping | Actual/result |
|---|---|---|---|---|---|
| RPT-UPLOAD-01 | PDF text hợp lệ | Admin,PDFtextđúngtype≤10MiB | 202,jobtạo;sauworkerREADY/unpublished | TC-KB-01 | NOT RUN |
| RPT-UPLOAD-02 | Quá dung lượng | File>10MiB | 413,không để file/job mồ côi | TC-KB-02 | NOT RUN |
| RPT-UPLOAD-03 | Giả extension | Exe/khôngPDFđổiđuôi.pdf | Bị reject400/415theoOpenAPIđãchốt,không execute | TC-KB-02 | NOT RUN |
| RPT-UPLOAD-04 | PDF scan | AdminuploadPDFảnhkhôngtext | 202nếuhợp lệ;workerFAILED/UNSUPPORTED_SCANNED_PDF | TC-KB-03 | NOT RUN |
| RPT-UPLOAD-05 | Agent upload | Agentkhông Admin gọi upload | 403,không tạo metadata/job | FR-KB-01/RBAC | NOT RUN |

## Sinh gợi ý AI — Quý Phúc

Related UC UC-14; nguồn FR-AI-01..06/09.

| Report ID | Tên case | Context/input dự kiến | Expected dự kiến cần review | Suite/requirement mapping | Actual/result |
|---|---|---|---|---|---|
| RPT-GENERATE-01 | Có evidence | AssignedAgent+nguồnREADY/published | GENERATED,draft/sourceIDđúng,không tạomessage | TC-AI-01/06 | NOT RUN |
| RPT-GENERATE-02 | Không evidence | Retrieverkết quảrỗng/dướingưỡng | INSUFFICIENT_EVIDENCE,nulltext,citationsrỗng,không bịa | TC-AI-02 | NOT RUN |
| RPT-GENERATE-03 | Citation bị bịa | Providerfake trả sourceID ngoài tập retrieve | Failclosed/AI_INVALID_CITATION,khôngdraftGENERATED | TC-AI-03 | NOT RUN |
| RPT-GENERATE-04 | Provider timeout | Fakeproviderhếttimeoutcókiểmsoát | 504/errorrõ,TicketAPIsvẫnchạybìnhthường | TC-AI-05 | NOT RUN |
| RPT-GENERATE-05 | Agent không assigned | Agentkhácngườiphụtráchgọigenerate | 404ownership,khôngcallprovider/không lộcontext | FR-AI-01/TC-WF-04 | NOT RUN |

