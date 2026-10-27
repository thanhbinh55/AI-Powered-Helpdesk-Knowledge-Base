import { Ticket, Message, KnowledgeDocument, AISuggestion, User } from '../types';

export const currentUserMock: User = {
  id: 'usr-agent-01',
  name: 'Bình Ngô (Lead Agent)',
  email: 'binh.ngo@hcmus.edu.vn',
  role: 'AGENT',
  avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80',
  active: true,
};

export const mockUsers: User[] = [
  currentUserMock,
  {
    id: 'usr-agent-02',
    name: 'Gia Phúc (Agent)',
    email: 'giaphuc@hcmus.edu.vn',
    role: 'AGENT',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80',
    active: true,
  },
  {
    id: 'usr-agent-03',
    name: 'Đức Lãm (KB Manager)',
    email: 'duclam@hcmus.edu.vn',
    role: 'AGENT',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&auto=format&fit=crop&q=80',
    active: true,
  },
  {
    id: 'usr-admin-01',
    name: 'Quản trị viên Hệ thống (Admin)',
    email: 'admin@helpdesk.edu.vn',
    role: 'ADMIN',
    avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&auto=format&fit=crop&q=80',
    active: true,
  },
  {
    id: 'usr-cust-01',
    name: 'Nguyễn Văn An',
    email: 'an.nguyen@company.com',
    role: 'CUSTOMER',
    avatar: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=100&auto=format&fit=crop&q=80',
    active: true,
  }
];

export const mockTickets: Ticket[] = [
  {
    id: 'tck-001',
    ticketNumber: 'TCK-1029',
    title: 'Không thể kích hoạt tài khoản sinh viên mới',
    description: 'Em vừa nhận email kích hoạt sáng nay nhưng khi bấm vào đường dẫn xác nhận thì hệ thống báo lỗi Token đã hết hạn (Error 401). Nhờ phòng hỗ trợ kiểm tra cấp lại link kích hoạt giúp em.',
    status: 'IN_PROGRESS',
    priority: 'HIGH',
    category: 'Identity & Access',
    customer: {
      name: 'Nguyễn Văn An',
      email: 'an.nguyen@company.com',
      avatar: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=100&auto=format&fit=crop&q=80',
      organization: 'K24 - Khoa CNTT',
    },
    assignee: {
      id: 'usr-agent-01',
      name: 'Bình Ngô',
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80',
    },
    createdAt: '2026-10-22T08:15:00Z',
    updatedAt: '2026-10-22T09:30:00Z',
    slaDeadline: '2026-10-22T14:15:00Z',
    unreadCount: 1,
  },
  {
    id: 'tck-002',
    ticketNumber: 'TCK-1030',
    title: 'Hỏi về chính sách gia hạn thời gian bảo lưu học tập và hoàn phí',
    description: 'Do việc gia đình đột xuất, em muốn làm thủ tục xin tạm hoãn học kỳ 1 và bảo lưu kết quả. Không biết thời hạn nộp đơn là ngày nào và học phí đã đóng có được hoàn trả hoặc chuyển sang kỳ sau không?',
    status: 'OPEN',
    priority: 'NORMAL',
    category: 'Chính sách & Học vụ',
    customer: {
      name: 'Trần Thị Mai',
      email: 'mai.tran@student.edu.vn',
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80',
      organization: 'K23 - Khoa Toán Tin',
    },
    assignee: null,
    createdAt: '2026-10-22T09:45:00Z',
    updatedAt: '2026-10-22T09:45:00Z',
    slaDeadline: '2026-10-22T17:45:00Z',
    unreadCount: 0,
  },
  {
    id: 'tck-003',
    ticketNumber: 'TCK-1031',
    title: 'Lỗi 500 khi nộp bài tập lớn qua cổng trực tuyến',
    description: 'Hệ thống báo Network Internal Error khi tôi tải file zip dung lượng 45MB lên portal. Deadline là 23h59 tối nay.',
    status: 'OPEN',
    priority: 'URGENT',
    category: 'Kỹ thuật Portal',
    customer: {
      name: 'Lê Hoàng Long',
      email: 'long.le@student.edu.vn',
      avatar: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=100&auto=format&fit=crop&q=80',
      organization: 'K22 - Khoa Vật lý',
    },
    assignee: null,
    createdAt: '2026-10-22T10:10:00Z',
    updatedAt: '2026-10-22T10:10:00Z',
    slaDeadline: '2026-10-22T12:10:00Z',
    unreadCount: 0,
  },
  {
    id: 'tck-004',
    ticketNumber: 'TCK-1025',
    title: 'Cấp quyền truy cập VPN phòng thí nghiệm AI Lab',
    description: 'Nhóm nghiên cứu chúng em cần kết nối máy chủ GPU cluster qua VPN để huấn luyện mô hình LLM.',
    status: 'RESOLVED',
    priority: 'LOW',
    category: 'Cơ sở hạ tầng & VPN',
    customer: {
      name: 'Đặng Tuấn Kiệt',
      email: 'kiet.dang@lab.hcmus.edu.vn',
      avatar: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&auto=format&fit=crop&q=80',
      organization: 'AI Research Group',
    },
    assignee: {
      id: 'usr-agent-02',
      name: 'Gia Phúc',
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80',
    },
    createdAt: '2026-10-21T14:00:00Z',
    updatedAt: '2026-10-22T08:00:00Z',
    slaDeadline: '2026-10-22T18:00:00Z',
    unreadCount: 0,
  },
];

export const mockMessagesByTicketId: Record<string, Message[]> = {
  'tck-001': [
    {
      id: 'msg-01',
      ticketId: 'tck-001',
      sender: {
        name: 'Nguyễn Văn An',
        email: 'an.nguyen@company.com',
        role: 'CUSTOMER',
        avatar: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=100&auto=format&fit=crop&q=80',
      },
      content: 'Em vừa nhận email kích hoạt sáng nay nhưng khi bấm vào đường dẫn xác nhận thì hệ thống báo lỗi Token đã hết hạn (Error 401). Nhờ phòng hỗ trợ kiểm tra cấp lại link kích hoạt giúp em ạ.',
      isInternal: false,
      createdAt: '2026-10-22T08:15:00Z',
    },
    {
      id: 'msg-02',
      ticketId: 'tck-001',
      sender: {
        name: 'Bình Ngô (Lead Agent)',
        email: 'binh.ngo@hcmus.edu.vn',
        role: 'AGENT',
        avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80',
      },
      content: 'Đã kiểm tra database identity_users: Link kích hoạt cũ hết hạn sau 24h theo chính sách bảo mật NFR-SEC. Đã kích hoạt cơ chế resend token mới vào queue.',
      isInternal: true, // INTERNAL NOTE - Yellow background
      createdAt: '2026-10-22T08:45:00Z',
    },
    {
      id: 'msg-03',
      ticketId: 'tck-001',
      sender: {
        name: 'Bình Ngô (Lead Agent)',
        email: 'binh.ngo@hcmus.edu.vn',
        role: 'AGENT',
        avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80',
      },
      content: 'Chào bạn An, hệ thống đã cấp lại mã token xác thực mới và gửi vào email an.nguyen@company.com. Bạn vui lòng kiểm tra hộp thư (cả mục Spam/Junk) và bấm kích hoạt trong vòng 24 giờ tới nhé.',
      isInternal: false,
      createdAt: '2026-10-22T09:30:00Z',
    },
  ],
  'tck-002': [
    {
      id: 'msg-11',
      ticketId: 'tck-002',
      sender: {
        name: 'Trần Thị Mai',
        email: 'mai.tran@student.edu.vn',
        role: 'CUSTOMER',
        avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80',
      },
      content: 'Do việc gia đình đột xuất, em muốn làm thủ tục xin tạm hoãn học kỳ 1 và bảo lưu kết quả. Không biết thời hạn nộp đơn là ngày nào và học phí đã đóng có được hoàn trả hoặc chuyển sang kỳ sau không?',
      isInternal: false,
      createdAt: '2026-10-22T09:45:00Z',
    }
  ]
};

export const mockKnowledgeDocuments: KnowledgeDocument[] = [
  {
    id: 'doc-001',
    title: 'Chính sách bảo lưu kết quả học tập & Quy định hoàn phí học vụ',
    filename: 'Chinh-sach-bao-luu-va-hoc-phi-2026.pdf',
    fileSize: '1.8 MB',
    status: 'READY',
    chunkCount: 24,
    isPublished: true,
    uploadedAt: '2026-10-20T10:00:00Z',
    category: 'Quy định đào tạo',
    summary: 'Quy định chi tiết về điều kiện bảo lưu kết quả, hạn nộp đơn trước tuần 4 của học kỳ, và hoàn trả 70% học phí nếu rút trước tuần 2.',
  },
  {
    id: 'doc-002',
    title: 'Hướng dẫn khắc phục lỗi xác thực tài khoản & JWT Token Expired',
    filename: 'Huong-dan-xac-thuc-tai-khoan.md',
    fileSize: '340 KB',
    status: 'READY',
    chunkCount: 12,
    isPublished: true,
    uploadedAt: '2026-10-21T09:30:00Z',
    category: 'Kỹ thuật & Tài khoản',
    summary: 'Cách xử lý link kích hoạt hết hạn (24h), hướng dẫn reset mật khẩu và xóa cache trình duyệt.',
  },
  {
    id: 'doc-003',
    title: 'Quy trình cấp phát tài khoản VPN & Máy chủ thực hành AI Lab',
    filename: 'Quy-trinh-cap-phat-VPN-AILab.pdf',
    fileSize: '2.4 MB',
    status: 'PROCESSING',
    chunkCount: 38,
    isPublished: false,
    uploadedAt: '2026-10-22T07:15:00Z',
    category: 'Cơ sở hạ tầng',
    summary: 'Tài liệu đang trong tiến trình vector hóa embeddings vào pgvector.',
  },
  {
    id: 'doc-004',
    title: 'Quy chế thi kết thúc học phần và phúc khảo điểm trực tuyến',
    filename: 'Quy-che-thi-va-phuc-khao.docx',
    fileSize: '950 KB',
    status: 'PENDING',
    chunkCount: 0,
    isPublished: false,
    uploadedAt: '2026-10-22T10:00:00Z',
    category: 'Khảo thí',
    summary: 'Chờ worker chunking và trích xuất nội dung.',
  }
];

export const mockAISuggestionsByTicketId: Record<string, AISuggestion> = {
  'tck-002': {
    ticketId: 'tck-002',
    draftReply: `Chào bạn Mai,

Dựa theo Quy chế đào tạo và bảo lưu của Nhà trường:
1. **Hạn nộp đơn bảo lưu:** Bạn cần nộp đơn xin tạm hoãn và bảo lưu trước kết thúc **Tuần thứ 4 của học kỳ**.
2. **Về học phí:** Nếu bạn nộp đơn trong 2 tuần đầu học kỳ, bạn sẽ được bảo lưu 100% học phí chuyển sang kỳ học tiếp theo, hoặc hoàn trả 70% tiền mặt theo biểu mẫu hoàn phí.
3. **Thủ tục thực hiện:** Bạn hãy tải mẫu đơn tại Cổng thông tin đào tạo (Mục Biểu mẫu học vụ) và gửi kèm minh chứng lý do gia đình về phòng Đào tạo (phòng A.101).

Nếu cần hỗ trợ thêm, bạn có thể phản hồi trực tiếp tại ticket này nhé!`,
    citations: [
      {
        documentId: 'doc-001',
        documentTitle: 'Chính sách bảo lưu kết quả học tập & Quy định hoàn phí học vụ',
        chunkSnippet: 'Mục 3.2: Sinh viên có nguyện vọng tạm hoãn học kỳ vì lý do cá nhân hoặc gia đình phải nộp đơn trước ngày kết thúc tuần học thứ 4...',
        score: 0.94,
        pageOrSection: 'Trang 4, Mục 3.2',
      },
      {
        documentId: 'doc-001',
        documentTitle: 'Chính sách bảo lưu kết quả học tập & Quy định hoàn phí học vụ',
        chunkSnippet: 'Mục 5.1: Mức hoàn trả hoặc bảo lưu học phí: Rút trước tuần 2 được bảo lưu 100% số tiền sang học kỳ kế tiếp hoặc hoàn trả 70%...',
        score: 0.89,
        pageOrSection: 'Trang 6, Mục 5.1',
      }
    ],
    confidence: 0.95,
    generatedAt: '2026-10-22T09:47:00Z',
  },
  'tck-001': {
    ticketId: 'tck-001',
    draftReply: `Chào bạn An,

Đường dẫn kích hoạt tài khoản có hiệu lực trong vòng 24 giờ kể từ khi phát hành. Nếu đường dẫn báo lỗi hết hạn (Token Expired), bạn có thể truy cập trang Đăng nhập và bấm vào nút "Gửi lại email kích hoạt", hoặc phản hồi để bộ phận hỗ trợ kích hoạt thủ công.`,
    citations: [
      {
        documentId: 'doc-002',
        documentTitle: 'Hướng dẫn khắc phục lỗi xác thực tài khoản & JWT Token Expired',
        chunkSnippet: 'Thời hạn token kích hoạt tài khoản sinh viên là 24 giờ theo tiêu chuẩn bảo mật NFR-SEC-01...',
        score: 0.96,
        pageOrSection: 'Mục 2.1 - Vòng đời mã xác thực',
      }
    ],
    confidence: 0.98,
    generatedAt: '2026-10-22T08:20:00Z',
  },
  'tck-003': {
    ticketId: 'tck-003',
    draftReply: `Chào bạn Long,

Theo Quy chế hạ tầng CNTT và Cổng thông tin nộp bài (Mục 4.1):
1. **Giới hạn dung lượng:** Hệ thống portal giới hạn dung lượng tải lên trực tiếp tối đa là **25 MB** cho mỗi tệp tin. Tệp zip 45MB của bạn vượt quá ngưỡng nên bị máy chủ từ chối (Mã lỗi 500).
2. **Giải pháp khắc phục ngay:** Bạn hãy nén nhỏ tệp tin (loại bỏ thư mục build/node_modules không cần thiết) hoặc tải file lên Google Drive trường (đuôi @student.hcmus.edu.vn) rồi dán liên kết chia sẻ công khai vào phần ghi chú nộp bài trước 23h59 nhé!`,
    citations: [
      {
        documentId: 'doc-002',
        documentTitle: 'Hướng dẫn khắc phục lỗi xác thực tài khoản & JWT Token Expired',
        chunkSnippet: 'Quy định tải tệp Mục 4.1: Dung lượng tải lên tối đa là 25MB cho tệp nộp bài tập lớn...',
        score: 0.92,
        pageOrSection: 'Mục 4.1 - Giới hạn dung lượng tải lên',
      }
    ],
    confidence: 0.93,
    generatedAt: '2026-10-22T10:12:00Z',
  },
  'tck-004': {
    ticketId: 'tck-004',
    draftReply: `Chào bạn Kiệt,

Yêu cầu cấp quyền VPN truy cập máy chủ AI Lab đã được duyệt và cấu hình hoàn tất:
1. **Thông tin truy cập:** Bạn sử dụng tài khoản email sinh viên đăng nhập qua OpenVPN Client theo máy chủ vpn.lab.hcmus.edu.vn (cổng 1194).
2. **Quy định sử dụng:** Chỉ sử dụng cho mục đích huấn luyện mô hình môn học/nghiên cứu; tài khoản sẽ tự động hết hạn sau khi kết thúc học kỳ.`,
    citations: [
      {
        documentId: 'doc-003',
        documentTitle: 'Quy trình cấp phát tài khoản VPN & Máy chủ thực hành AI Lab',
        chunkSnippet: 'Mục 2.3: Thời gian cấp phát tài khoản VPN nghiên cứu là trong vòng 24 giờ sau khi có xác nhận...',
        score: 0.95,
        pageOrSection: 'Mục 2.3 - Quy trình kích hoạt VPN',
      }
    ],
    confidence: 0.96,
    generatedAt: '2026-10-21T14:30:00Z',
  }
};

