# Nhật ký sử dụng AI — Template 2 (Phan Gia Phúc - `24120503`)

> Ghi nhận các phiên làm việc với AI phục vụ thiết kế phần mềm Template 2 (`docs/template2/members/gia-phuc/`).
> Mỗi phiên ghi đủ 7 trường: Thời gian, Tác giả, Công cụ/Model, Prompt đã khử dữ liệu nhạy cảm, Nội dung AI tạo, Nội dung tự kiểm chứng & hiệu chỉnh, Minh chứng/Commit.

### 23/11/2026 — Đối chiếu SRS và chỉnh sửa thiết kế lớp

- **Thời gian** 23/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Đọc SRS, kiểm tra mục 3.2 và 3.3 trong bản thiết kế còn thiếu, dư hoặc sai gì. Có thể bổ sung vào Google Doc và ghi nhật ký.”
- **Nội dung AI tạo** Bảng đối chiếu theo trang và yêu cầu SRS, năm sơ đồ lớp, nội dung bổ sung thêm cho các bảng đặc tả Identity, Ticket, Knowledge, AI và Workflow.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Sinh viên yêu cầu lấy SRS làm căn cứ. Codex đối chiếu hợp đồng các port, thứ tự khóa Ticket rồi Suggestion, phạm vi P0/P1 và quyết định DEC-06. Codex đọc lại Google Doc, kiểm tra hình cùng chú thích trên bản xuất PDF và cập nhật mục lục.
- **Minh chứng/Commit** [Bản thiết kế dùng trong phiên](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u) và [SRS của dự án](../../reports/SRS-master.md).

### 25/11/2026 — Rà soát năm hình và sửa nhãn bị che

- **Thời gian** 25/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Bổ sung vào Hình 3.3a controller gọi AI suggestion service. Tách 2 controller Identity, thêm đường gửi tin soạn tay cho rõ ràng. Rà soát thêm các lỗi hiển thị.”
- **Nội dung AI tạo** Bổ sung nhánh AISuggestionController → AISuggestionApplicationService, tách hai controller ở Identity, bổ sung đường gửi tin soạn tay trong Ticket và đường tiếp nhận tài liệu trong Knowledge. Làm rõ bội số trên hình dữ liệu AI.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Sinh viên chỉ ra các controller bị thiếu. Codex chuyển nhãn xuống dưới các ô lớp, xuất lại PDF và kiểm tra dòng chữ ở trang in 18.
- **Minh chứng/Commit** [Google Doc được rà soát, mục 3.2–3.3](https://docs.google.com/document/d/1s2inl8eKlSDA5KhdDgZFqpT7YM0uKQJDtrFz_QQEk5U/edit?tab=t.0#heading=h.yz9k5ytl267u).

### 26/11/2026 — Trích bản Markdown bàn giao cá nhân

- **Thời gian** 26/11/2026.
- **Tác giả** Phan Gia Phúc (24120503).
- **Công cụ/Model** OpenAI Codex (GPT-6).
- **Prompt đã khử dữ liệu nhạy cảm** “Trích mục 3.2 và 3.3 từ bản Markdown Template 2 của nhóm vào file task.”
- **Nội dung AI tạo** File bàn giao lấy nguyên văn hai mục từ bản Markdown được chỉ định, kèm định nghĩa ảnh của các hình trong hai mục.
- **Nội dung tự kiểm chứng & hiệu chỉnh** Codex kiểm tra ranh giới bằng tiêu đề trong thân bài, so sánh nội dung đã ghi với nguồn, đếm bốn tiểu mục module, năm chú thích hình.
- **Minh chứng/Commit** [Phần bàn giao 3.2–3.3 của Gia Phúc](../../task/template2/gia-phuc.md) tại commit `317dfe6` trên nhánh `docs/t2-giaphuc`.
