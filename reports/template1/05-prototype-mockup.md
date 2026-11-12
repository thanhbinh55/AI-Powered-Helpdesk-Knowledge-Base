> Đồng bộ theo [Report.pdf](report/Report.pdf) ngày 12/11/2026. Nội dung trích từ [report.md](report/report.md); ảnh dùng chung với bản final.

<a id="5-bản-mẫu-(prototype)"></a>

# **5 Bản mẫu (Prototype)**

Bộ giao diện tham chiếu: Redesign v2; 34 nhóm màn hình chính, 229 frames và 82 flow points theo danh mục thiết kế. Light/Dark Mode và responsive là định hướng thiết kế; các hành vi tương tác phải tuân thủ quyền và workflow ở Mục 4\.

[Mở thiết kế Figma chính thức \- Node 49:58](https://www.figma.com/design/Ofvm9udw9coBOxadTN4PXB/SE?node-id=49-58&p=f&m=dev)

<a id="5.1-giao-diện-định-danh-và-tài-khoản"></a>

## **5.1 Giao diện định danh và tài khoản**

<a id="5.1.1-đăng-nhập-hệ-thống"></a>

### **5.1.1 Đăng nhập hệ thống**

Biểu mẫu email và mật khẩu, thông báo lỗi chung, chuyển hướng theo vai trò. Không đưa Google OAuth vào phạm vi đăng nhập MVP.

![](report/assets/ui/62-8214.png)

**Hình 5.1  Đăng nhập hệ thống**

<a id="5.1.2-đăng-ký-customer"></a>

### **5.1.2 Đăng ký Customer**

Nhập họ tên, email, mật khẩu và xác nhận; tài khoản tự đăng ký luôn mang vai trò CUSTOMER.

![](report/assets/ui/62-8215.png)

**Hình 5.2  Đăng ký Customer**

<a id="5.1.3-hồ-sơ-cá-nhân"></a>

### **5.1.3 Hồ sơ cá nhân**

Xem và cập nhật thông tin được phép của chính mình; đổi mật khẩu có kiểm tra mật khẩu hiện tại.

![](report/assets/ui/62-8328.png)

**Hình 5.3  Hồ sơ cá nhân**

<a id="5.1.4-quản-lý-danh-sách-tài-khoản-agent-(admin)"></a>

### **5.1.4 Quản lý danh sách tài khoản Agent (Admin)**

Quản trị viên xem danh sách nhân viên hỗ trợ, lọc theo trạng thái hoạt động và kích hoạt/vô hiệu hóa tài khoản Agent.

![](report/assets/ui/62-10225.png)

**Hình 5.4 Quản lý danh sách nhân viên (Admin)**

<a id="5.1.5-tạo-tài-khoản-agent-mới-và-vô-hiệu-hóa-tài-khoản-(admin)"></a>

### **5.1.5 Tạo tài khoản Agent mới và Vô hiệu hóa tài khoản (Admin)**

Quản trị viên tạo mới tài khoản Support Agent hoặc xác nhận vô hiệu hóa tài khoản Agent (thu hồi phiên đăng nhập hiện hành).

![](report/assets/ui/62-10226.png)

**Hình 5.5a Biểu mẫu tạo tài khoản nhân viên mới**

![](report/assets/ui/62-13238.png)

**Hình 5.5b Xác nhận vô hiệu hóa tài khoản nhân viên**

<a id="5.2-giao-diện-customer-portal"></a>

## **5.2 Giao diện Customer Portal**

<a id="5.2.1-danh-sách-yêu-cầu-của-tôi"></a>

### **5.2.1 Danh sách yêu cầu của tôi**

Màn hình hiển thị các yêu cầu hỗ trợ do Customer hiện tại tạo, kèm trạng thái xử lý để khách hàng theo dõi tiến độ. Người dùng có thể tìm kiếm, lọc, chuyển trang và chọn một yêu cầu để xem chi tiết.

Giao diện phân biệt các trạng thái đang tải, chưa có yêu cầu, không có kết quả phù hợp và lỗi tải dữ liệu.

![](report/assets/ui/58-6763.png)

**Hình 5.6  Danh sách yêu cầu của tôi**

<a id="5.2.2-tạo-yêu-cầu-hỗ-trợ"></a>

### **5.2.2 Tạo yêu cầu hỗ trợ**

Customer nhập tiêu đề và nội dung mô tả, sau đó chọn Gửi yêu cầu. Hệ thống kiểm tra dữ liệu và hiển thị lỗi tại nội dung cần điều chỉnh nếu thông tin không hợp lệ.

Khi tạo thành công, yêu cầu có trạng thái Mới tạo (OPEN), chưa có nhân viên phụ trách và được mở ở trang chi tiết. Nội dung mô tả xuất hiện trong hội thoại công khai đầu tiên.

![](report/assets/ui/58-6764.png)

**Hình 5.7  Tạo yêu cầu hỗ trợ**

<a id="5.2.3-chi-tiết-và-hội-thoại-công-khai"></a>

### **5.2.3 Chi tiết và hội thoại công khai**

Customer xem thông tin, trạng thái xử lý và các tin nhắn công khai của yêu cầu thuộc sở hữu của mình. Giao diện không hiển thị ghi chú INTERNAL hoặc lịch sử sự kiện nội bộ.

Khách hàng gửi phản hồi khi trạng thái yêu cầu cho phép. Nếu yêu cầu đang Chờ khách hàng phản hồi (WAITING\_CUSTOMER), việc gửi phản hồi thành công đưa yêu cầu về Đang xử lý (IN\_PROGRESS).

Khi yêu cầu chuyển sang Đã giải quyết (RESOLVED), giao diện cung cấp lựa chọn xác nhận đóng hoặc yêu cầu xử lý tiếp theo Mục 5.2.4.

![](report/assets/ui/58-6765.png)

**Hình 5.8 Chi tiết và hội thoại công khai khi yêu cầu đang được xử lý**

<a id="5.2.4-xác-nhận-đóng-hoặc-mở-lại-yêu-cầu"></a>

#### **5.2.4 Xác nhận đóng hoặc mở lại yêu cầu**

Khi yêu cầu ở trạng thái Đã giải quyết (RESOLVED), Customer xem lại nội dung xử lý và lựa chọn:

\- Đóng yêu cầu (CLOSE): Xác nhận vấn đề đã được giải quyết, chuyển yêu cầu sang CLOSED.

\- Yêu cầu xử lý tiếp (REOPEN): Thông báo vấn đề chưa được giải quyết, chuyển yêu cầu về IN\_PROGRESS.

Hệ thống kiểm tra quyền sở hữu và trạng thái hiện tại trước khi thực hiện. Nếu thao tác thất bại hoặc trạng thái đã thay đổi, giao diện thông báo phù hợp và không hiển thị kết quả thành công.

![](report/assets/ui/62-6953.png)

**Hình 5.9 Yêu cầu đã giải quyết, chờ Customer xác nhận đóng hoặc mở lại**

<a id="5.2.5-chi-tiết-yêu-cầu-đã-đóng"></a>

#### **5.2.5 Chi tiết yêu cầu đã đóng**

Khi yêu cầu ở trạng thái Đã đóng (CLOSED), Customer vẫn được xem thông tin và hội thoại công khai của yêu cầu thuộc sở hữu của mình.

Giao diện chuyển sang chế độ chỉ đọc, khóa ô soạn phản hồi và không cho phép gửi thêm tin nhắn hoặc mở lại yêu cầu đã đóng. Trạng thái CLOSED được hiển thị rõ để khách hàng phân biệt với yêu cầu đang chờ xác nhận giải quyết.

![](report/assets/ui/62-6954.png)

**Hình 5.10 Chi tiết yêu cầu đã đóng ở chế độ chỉ đọc**

<a id="5.3-giao-diện-agent-workspace"></a>

## **5.3 Giao diện Agent Workspace**

<a id="5.3.1-hàng-đợi-và-nhận-xử-lý"></a>

### **5.3.1 Hàng đợi và nhận xử lý**

Hiển thị hàng đợi các ticket đang mở (OPEN), có thể chọn xem nội dung chi tiết từng ticket, có thể tìm kiếm ticket thông qua ô tìm yêu cầu; Mã ticket và trạng thái “Mới” được hiển thị rõ; Thao tác với nút “Nhận xử lý” để nhận ticket; Ticket chưa được Agent đang đăng nhập nhận thì Agent này không được soạn phản hồi → các tính năng liên quan đến xử lý ticket bị khóa (giao diện soạn phản hồi, sử dụng Trợ lý AI, xem/soạn ghi chú nội bộ).

![](report/assets/ui/55-1992.png)

**Hình 5.11  Hàng đợi và nhận xử lý**

<a id="5.3.2-xử-lý-ticket-và-ghi-chú-nội-bộ"></a>

### **5.3.2 Xử lý ticket và ghi chú nội bộ**

Ticket đang được xử lý có thể được đánh dấu đã giải quyết hoặc yêu cầu thêm thông tin từ Customer, Agent có thể dùng tính năng Trợ lý AI để hỗ trợ xử lý ticket. Trạng thái của ticket khi này được hiển thị rõ “Đang xử lý”.

Chỉ Agent được giao ticket/Admin được tạo và xem ghi chú nội bộ. Vùng soạn ghi chú/ghi chú đã thêm được hiển thị nổi bật trên giao diện.

![](report/assets/ui/55-2537.png)

**Hình 5.12  Xử lý ticket và ghi chú nội bộ**

<a id="5.3.3-xung-đột-nhận-ticket"></a>

### **5.3.3 Xung đột nhận ticket**

Thông báo ticket đã có Agent khác nhận xử lý, thao tác với nút “Về hàng đợi” để tải lại hàng đợi ticket → Agent thua claim không được tiếp tục xử lý ticket ngoài quyền.

![](report/assets/ui/56-3104.png)

**Hình 5.13  Xung đột nhận ticket**

<a id="5.4-giao-diện-knowledge-base"></a>

## **5.4 Giao diện Knowledge Base**

<a id="5.4.1-tìm-kiếm-tri-thức"></a>

### **5.4.1 Tìm kiếm tri thức**

Agent/Admin tìm kiếm tài liệu

![](report/assets/ui/62-9092.png)

**Hình 5.14  Tìm kiếm tri thức**

<a id="5.4.2-đọc-tài-liệu-tri-thức"></a>

### **5.4.2 Đọc tài liệu tri thức**

Hiển thị nội dung tài liệu được phép.

![](report/assets/ui/62-9094.png)

**Hình 5.15  Đọc tài liệu tri thức**

<a id="5.4.3-quản-trị-và-công-bố-tài-liệu"></a>

### **5.4.3 Quản trị và công bố tài liệu**

Admin xem danh mục và trạng thái; READY không đồng nghĩa đã published. Upload, publish và archive theo quyền Admin.

![](report/assets/ui/62-9240.png)

**Hình 5.16  Quản trị và công bố tài liệu**

<a id="5.4.4-tải-tài-liệu-mới-lên-knowledge-base-(upload)"></a>

#### **5.4.4 Tải tài liệu mới lên Knowledge Base (Upload)**

Biểu mẫu chọn tệp tài liệu (PDF/TXT/MD, giới hạn kích thước \<= 10 MiB) để đưa vào hàng đợi bóc tách và lập chỉ mục Vector bất đồng bộ.

![](report/assets/ui/62-9241.png)

***Hình 5.17 Tải tài liệu mới lên Knowledge Base***

<a id="5.4.5-chi-tiết-tài-liệu-đã-xử-lý-xong-nhưng-chưa-công-bố-(ready-—-unpublished)"></a>

#### **5.4.5 Chi tiết tài liệu đã xử lý xong nhưng chưa công bố (READY — Unpublished)**

Minh họa trạng thái tài liệu đã hoàn tất bóc tách và nhúng vector nhưng đang chờ kiểm duyệt, chưa được công bố cho tìm kiếm hoặc RAG.

![](report/assets/ui/62-9783.png)

***Hình 5.18 Chi tiết tài liệu ở trạng thái sẵn sàng nhưng chưa công bố***

<a id="5.5-giao-diện-ai-và-tham-chiếu-quản-trị"></a>

## **5.5 Giao diện AI và tham chiếu quản trị**

<a id="5.5.1-gợi-ý-ai-và-trích-dẫn"></a>

### **5.5.1 Gợi ý AI và trích dẫn**

Agent tạo gợi ý, đọc nguồn và chủ động chèn vào bản nháp để kiểm duyệt trước khi gửi. Ngăn AI có lối mở lịch sử và thao tác đánh giá gợi ý; thao tác chèn hoặc đánh giá không tự gửi phản hồi.

![](report/assets/ui/55-1994.png)

**Hình 5.19 Gợi ý AI, nguồn trích dẫn và thao tác hỗ trợ nhân viên**

<a id="5.5.2-xem-nguồn-trích-dẫn"></a>

### **5.5.2 Xem nguồn trích dẫn**

Người dùng mở đoạn nguồn để kiểm tra nội dung gợi ý. Bản chụp đã lưu tại thời điểm tạo được giữ nguyên, kể cả khi tài liệu nguồn hiện đã lưu trữ; quyền tải tài liệu gốc được kiểm tra riêng.

![](report/assets/ui/56-3578.png)

**Hình 5.20 Xem đoạn nguồn trích dẫn của gợi ý**

<a id="5.5.3-danh-sách-yêu-cầu-quản-trị"></a>

### **5.5.3 Danh sách yêu cầu quản trị**

Admin xem danh sách toàn bộ ticket và sử dụng bộ lọc để tìm yêu cầu cần theo dõi hoặc xử lý.

![](report/assets/ui/62-9943.png)

**Hình 5.21 Danh sách yêu cầu quản trị**

<a id="5.5.4-xử-lý,-lịch-sử-yêu-cầu-và-phân-công-nhân-viên"></a>

### **5.5.4 Xử lý, lịch sử yêu cầu và phân công nhân viên**

Quản trị viên xem toàn bộ lịch sử xử lý, bao gồm ghi chú nội bộ (INTERNAL), và thực hiện gán hoặc chuyển người phụ trách ticket.

![](report/assets/ui/62-9944.png)

**Hình 5.22a Chi tiết xử lý và lịch sử yêu cầu (Admin — D02)**

![](report/assets/ui/62-9945.png)

**Hình 5.22b Biểu mẫu phân công nhân viên phụ trách (Admin — D03)**

<a id="5.5.5-lịch-sử-gợi-ý-ai"></a>

### **5.5.5 Lịch sử gợi ý AI**

Agent được giao ticket và Admin xem các lần tạo gợi ý, người yêu cầu, thời điểm và kết quả đã lưu. Người dùng chọn một lần tạo để đọc lại nội dung và bản chụp nguồn. Giao diện có các trạng thái đang tải, trống, lỗi và mất quyền.

![](report/assets/ui/81-7585.png)

**Hình 5.23a Danh sách các lần tạo gợi ý AI**

![](report/assets/ui/81-8707.png)

**Hình 5.23b Chi tiết gợi ý AI đã lưu**

<a id="5.5.6-đánh-giá-gợi-ý-ai-(p1)"></a>

### **5.5.6 Đánh giá gợi ý AI (P1)**

Agent được giao ticket chọn Hữu ích hoặc Không hữu ích trên gợi ý ở trạng thái GENERATED hoặc APPLIED. Giao diện hiển thị lựa chọn đã lưu, cho phép đổi lựa chọn và thử lại khi lưu lỗi. Đánh giá không tự gửi phản hồi hoặc thay đổi trạng thái gợi ý. Admin không có thao tác đánh giá.

![](report/assets/ui/81-7560.png)

**Hình 5.24a Trạng thái đã lưu đánh giá hữu ích**

![](report/assets/ui/82-10422.png)

**Hình 5.24b Thông báo lỗi lưu đánh giá và thao tác thử lại**

<a id="5.5.7-bỏ-gợi-ý-và-tiếp-tục-soạn-thủ-công"></a>

### **5.5.7 Bỏ gợi ý và tiếp tục soạn thủ công**

Người dùng xác nhận trước khi bỏ gợi ý ở trạng thái GENERATED. Sau khi bỏ, gợi ý chuyển sang DISCARDED và vẫn được lưu trong lịch sử; bản nháp được giữ nguyên, không có phản hồi nào được gửi. Nếu bản nháp đã được chèn từ gợi ý, người dùng phải chọn Tiếp tục soạn thủ công trước khi kiểm duyệt và gửi. Việc gửi thủ công không chuyển gợi ý đã bỏ thành APPLIED.

![](report/assets/ui/91-15641.png)

**Hình 5.25 Xác nhận bỏ gợi ý AI**

![](report/assets/ui/91-15904.png)

**Hình 5.26 Đã bỏ gợi ý AI và lựa chọn tiếp tục soạn thủ công**

<a id="5.5.8-thống-kê-ticket-(p1)"></a>

### **5.5.8 Thống kê ticket (P1)**

Admin xem tổng số ticket, phân bố theo trạng thái và người phụ trách hiện tại, cùng thời điểm lấy dữ liệu. Ticket chưa được giao hiển thị thành nhóm riêng; nhân viên đã vô hiệu hóa vẫn được giữ trong thống kê nếu còn ticket. Tổng các nhóm trong mỗi bảng bằng tổng số ticket. Giao diện hỗ trợ tải lại dữ liệu và có các trạng thái đang tải, không có dữ liệu, lỗi và không đủ quyền.

![](report/assets/ui/91-19910.png)

**Hình 5.27 Thống kê ticket theo trạng thái và người phụ trách**
