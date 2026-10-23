import React, { useState, useRef, useEffect } from 'react';
import { 
  Send, 
  Lock, 
  Sparkles, 
  CheckCircle, 
  UserCheck, 
  ExternalLink,
  ShieldCheck,
  Building,
  Mail,
  Clock,
  Inbox,
  Paperclip,
  Image as ImageIcon,
  Smile,
  Zap,
  CheckCheck,
  Copy,
  Check,
  FileText,
  AlertCircle,
  HelpCircle,
  X,
  RotateCcw,
  PanelLeftOpen
} from 'lucide-react';
import { Ticket, Message, AISuggestion, Citation } from '../../types';
import { Badge } from '../../components/common/Badge';

interface TicketWorkspaceProps {
  ticket: Ticket;
  messages: Message[];
  onSendMessage: (ticketId: string, content: string, isInternal: boolean) => void;
  onClaimTicket: (ticketId: string) => void;
  onResolveTicket: (ticketId: string) => void;
  aiSuggestion?: AISuggestion | null;
  isQueueCollapsed?: boolean;
  onToggleQueue?: () => void;
  queueTicketCount?: number;
}

export const TicketWorkspace: React.FC<TicketWorkspaceProps> = ({
  ticket,
  messages,
  onSendMessage,
  onClaimTicket,
  onResolveTicket,
  aiSuggestion,
  isQueueCollapsed = false,
  onToggleQueue,
  queueTicketCount,
}) => {
  const [replyType, setReplyType] = useState<'PUBLIC' | 'INTERNAL'>('PUBLIC');
  const [replyText, setReplyText] = useState('');
  const [isAIDeclined, setIsAIDeclined] = useState(false);
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null);
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const [showCannedMenu, setShowCannedMenu] = useState(false);
  const [copiedMsgId, setCopiedMsgId] = useState<string | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-display AI suggestion whenever switching tickets
  useEffect(() => {
    setIsAIDeclined(false);
  }, [ticket.id]);

  // Auto-scroll messages to bottom when a new message arrives
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages.length]);

  const cannedResponses = [
    { 
      label: '1. Tiếp nhận & Kiểm tra', 
      text: 'Chào bạn, mình đã tiếp nhận thông tin yêu cầu và đang tiến hành kiểm tra trên hệ thống. Mình sẽ phản hồi lại ngay cho bạn nhé!' 
    },
    { 
      label: '2. Yêu cầu ảnh chụp lỗi', 
      text: 'Chào bạn, bạn vui lòng chụp ảnh toàn bộ màn hình lỗi (bao gồm thanh địa chỉ URL) và gửi lại để kỹ thuật viên hỗ trợ nhanh nhất nhé.' 
    },
    { 
      label: '3. Xác nhận hoàn tất', 
      text: 'Vấn đề của bạn đã được hỗ trợ xử lý thành công trên hệ thống. Bạn vui lòng thử lại và phản hồi tại ticket này nếu cần thêm hỗ trợ nhé!' 
    },
  ];

  const emojis = ['😊', '👍', '🤝', '💡', '❓', '🙏', '❤️', '✅'];

  const handleCopyMessage = (content: string, id: string) => {
    navigator.clipboard.writeText(content);
    setCopiedMsgId(id);
    setTimeout(() => setCopiedMsgId(null), 2000);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (replyText.trim()) {
        onSendMessage(ticket.id, replyText, replyType === 'INTERNAL');
        setReplyText('');
      }
    }
  };

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!replyText.trim()) return;
    onSendMessage(ticket.id, replyText, replyType === 'INTERNAL');
    setReplyText('');
  };

  // 3 Action Handlers for AI Suggestion: Accept / Edit / Decline
  const handleAcceptAI = () => {
    if (aiSuggestion) {
      setReplyText(aiSuggestion.draftReply);
      setReplyType('PUBLIC');
      textareaRef.current?.focus();
    }
  };

  const handleEditAI = () => {
    if (aiSuggestion) {
      setReplyText(aiSuggestion.draftReply);
      setReplyType('PUBLIC');
      setTimeout(() => {
        textareaRef.current?.focus();
        textareaRef.current?.setSelectionRange(
          aiSuggestion.draftReply.length,
          aiSuggestion.draftReply.length
        );
      }, 50);
    }
  };

  const handleDeclineAI = () => {
    setIsAIDeclined(true);
  };

  return (
    <div className="flex-1 flex overflow-hidden h-[calc(100vh-3.5rem)] bg-slate-100 select-none">
      {/* ========================================================
          CỘT TRÁI: TICKET DETAIL & ISSUE WORKSPACE (RỘNG RÃI, THOÁNG MẮT, ĐỠ NÉN CHỮ)
          ======================================================== */}
      <div className="flex-1 flex flex-col h-full overflow-y-auto bg-slate-50/70 border-r border-slate-200 text-left">
        {/* 1. Header Toolbar */}
        <div className="bg-white border-b border-slate-200 px-6 py-3.5 shadow-2xs shrink-0">
          <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
            <div className="flex items-center space-x-2">
              {isQueueCollapsed && onToggleQueue && (
                <button
                  type="button"
                  onClick={onToggleQueue}
                  title="Mở lại danh sách hàng đợi ticket"
                  className="inline-flex items-center space-x-1.5 px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg transition mr-1 border border-slate-200/80 shadow-2xs active:scale-95"
                >
                  <PanelLeftOpen className="w-3.5 h-3.5 text-helpdesk-600" />
                  <span>Mở hàng đợi</span>
                  {typeof queueTicketCount === 'number' && queueTicketCount > 0 && (
                    <span className="bg-helpdesk-600 text-white text-[10px] font-bold px-1.5 py-0.2 rounded-full">
                      {queueTicketCount}
                    </span>
                  )}
                </button>
              )}

              <span className="font-mono text-xs font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">
                #{ticket.ticketNumber}
              </span>
              <Badge variant="status" value={ticket.status} />
              <Badge variant="priority" value={ticket.priority} />
              <span className="text-xs text-slate-400">•</span>
              <span className="text-xs font-semibold text-slate-600 bg-slate-100/80 px-2 py-0.5 rounded-md">
                {ticket.category}
              </span>
            </div>

            {/* Actions: Claim / Resolve */}
            <div className="flex items-center space-x-2">
              {!ticket.assignee ? (
                <button
                  onClick={() => onClaimTicket(ticket.id)}
                  className="inline-flex items-center space-x-1.5 px-3.5 py-1.5 bg-helpdesk-600 hover:bg-helpdesk-700 text-white text-xs font-semibold rounded-lg shadow-xs transition active:scale-95"
                >
                  <UserCheck className="w-3.5 h-3.5" />
                  <span>Nhận xử lý (Claim)</span>
                </button>
              ) : (
                <div className="flex items-center space-x-1.5 text-xs text-slate-600 bg-slate-50 border border-slate-200 px-3 py-1.5 rounded-lg">
                  <span className="text-slate-400">Phụ trách:</span>
                  <span className="font-bold text-slate-800">{ticket.assignee.name}</span>
                </div>
              )}

              {ticket.status !== 'RESOLVED' && ticket.status !== 'CLOSED' && (
                <button
                  onClick={() => onResolveTicket(ticket.id)}
                  className="inline-flex items-center space-x-1.5 px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold rounded-lg shadow-xs transition active:scale-95"
                >
                  <CheckCircle className="w-3.5 h-3.5" />
                  <span>Hoàn tất (Resolve)</span>
                </button>
              )}
            </div>
          </div>

          {/* Ticket Title */}
          <h1 className="text-lg font-bold text-slate-900 tracking-tight leading-snug">
            {ticket.title}
          </h1>

          {/* Requester Information Strip */}
          <div className="mt-2.5 pt-2 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-500 gap-y-1">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <div className="relative">
                  <img
                    src={ticket.customer.avatar || 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'}
                    alt={ticket.customer.name}
                    className="w-5 h-5 rounded-full object-cover ring-1 ring-slate-200"
                  />
                  <span className="absolute -bottom-0.5 -right-0.5 w-2 h-2 bg-emerald-500 rounded-full ring-1 ring-white" title="Trực tuyến" />
                </div>
                <span className="font-semibold text-slate-800">{ticket.customer.name}</span>
                <span className="text-slate-400 flex items-center gap-1">
                  <Mail className="w-3 h-3 text-slate-400" /> {ticket.customer.email}
                </span>
              </div>

              <div className="hidden sm:flex items-center space-x-1 text-slate-600">
                <Building className="w-3.5 h-3.5 text-slate-400" />
                <span>{ticket.customer.organization || 'Khoa CNTT'}</span>
              </div>
            </div>

            <div className="flex items-center space-x-3 text-[11px]">
              <span className="text-slate-400">
                Tạo: {new Date(ticket.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} - {new Date(ticket.createdAt).toLocaleDateString()}
              </span>
              <div className="flex items-center space-x-1 text-amber-700 bg-amber-50 border border-amber-200/80 px-2 py-0.5 rounded-full font-medium">
                <Clock className="w-3 h-3" />
                <span>SLA: Còn 4 giờ</span>
              </div>
            </div>
          </div>
        </div>

        {/* 2. Main Content Body: Rộng rãi, không bị nén chữ của issue */}
        <div className="p-6 space-y-5 max-w-4xl w-full">
          {/* Claim Banner nếu ticket chưa ai nhận */}
          {!ticket.assignee && (
            <div className="p-4 bg-blue-50/90 border border-blue-200 rounded-2xl flex flex-wrap items-center justify-between gap-3 shadow-2xs">
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-blue-100 text-blue-700 rounded-xl">
                  <Inbox className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="font-bold text-xs text-blue-950">Ticket đang trong Hàng đợi OPEN</h4>
                  <p className="text-[11px] text-blue-700/90 mt-0.5">
                    Chưa có nhân viên phụ trách. Hãy bấm "Nhận xử lý" để thêm vào danh sách công việc của bạn.
                  </p>
                </div>
              </div>
              <button
                onClick={() => onClaimTicket(ticket.id)}
                className="inline-flex items-center space-x-1.5 px-4 py-2 bg-helpdesk-600 hover:bg-helpdesk-700 text-white text-xs font-semibold rounded-xl shadow-xs transition active:scale-95 shrink-0"
              >
                <UserCheck className="w-3.5 h-3.5" />
                <span>Nhận xử lý ngay</span>
              </button>
            </div>
          )}

          {/* CARD CHI TIẾT SỰ CỐ / YÊU CẦU CỦA KHÁCH HÀNG (TO, RÕ, KHÔNG NÉN) */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3">
            <div className="flex items-center justify-between border-b border-slate-100 pb-2.5">
              <div className="flex items-center space-x-2">
                <div className="p-1.5 bg-helpdesk-50 text-helpdesk-600 rounded-lg">
                  <FileText className="w-4 h-4" />
                </div>
                <h2 className="text-sm font-bold text-slate-900 tracking-tight">
                  Mô tả chi tiết sự cố & Yêu cầu hỗ trợ
                </h2>
              </div>
              <span className="text-[11px] bg-slate-100 text-slate-500 font-medium px-2 py-0.5 rounded-full">
                Nội dung gửi ban đầu
              </span>
            </div>

            {/* Khung nội dung text dài thoải mái, không lo bị nén */}
            <div className="text-slate-800 text-sm leading-relaxed whitespace-pre-wrap font-normal p-3.5 bg-slate-50/60 rounded-xl border border-slate-100">
              {ticket.description}
            </div>

            {/* Tệp đính kèm mô phỏng */}
            <div className="pt-1 flex flex-wrap items-center gap-2 text-xs">
              <span className="text-[11px] font-semibold text-slate-400">Minh chứng đính kèm:</span>
              <div className="inline-flex items-center space-x-1.5 px-3 py-1 bg-white border border-slate-200 rounded-lg text-slate-700 text-xs shadow-2xs hover:border-slate-300 transition">
                <Paperclip className="w-3.5 h-3.5 text-helpdesk-600" />
                <span>screenshot_error_portal.png</span>
                <span className="text-[10px] text-slate-400">(1.2 MB)</span>
              </div>
            </div>
          </div>

          {/* CARD TÀI LIỆU RAG ĐỐI CHIẾU (NẾU CÓ CITATIONS) */}
          {aiSuggestion && aiSuggestion.citations && aiSuggestion.citations.length > 0 && (
            <div className="bg-white border border-purple-200/90 rounded-2xl p-5 shadow-xs space-y-3">
              <div className="flex items-center justify-between border-b border-purple-100 pb-2.5">
                <div className="flex items-center space-x-2">
                  <div className="p-1.5 bg-purple-100 text-purple-700 rounded-lg">
                    <Sparkles className="w-4 h-4" />
                  </div>
                  <div>
                    <h3 className="text-xs font-bold text-purple-950">
                      Tài liệu kiểm chứng từ Kho tri thức (Knowledge Base Grounding)
                    </h3>
                    <p className="text-[11px] text-purple-700/80">
                      RAG pgvector tự động truy xuất các văn bản liên quan có căn cứ pháp lý
                    </p>
                  </div>
                </div>
                <span className="text-[11px] bg-emerald-50 text-emerald-700 font-bold px-2 py-0.5 rounded-full border border-emerald-200">
                  Đã xác minh nguồn
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {aiSuggestion.citations.map((cite, idx) => (
                  <div
                    key={idx}
                    onClick={() => setSelectedCitation(cite)}
                    className="p-3 bg-purple-50/40 hover:bg-purple-50 border border-purple-100 hover:border-purple-300 rounded-xl cursor-pointer transition space-y-1.5 group"
                  >
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-purple-900 truncate max-w-[200px]">
                        {cite.documentTitle}
                      </span>
                      <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100/70 px-1.5 py-0.2 rounded">
                        {Math.round(cite.score * 100)}% khớp
                      </span>
                    </div>
                    <p className="text-[11px] text-slate-600 line-clamp-2 italic font-serif">
                      "{cite.chunkSnippet}"
                    </p>
                    <div className="flex items-center justify-between text-[10px] text-purple-700 pt-1 border-t border-purple-100/60 font-medium">
                      <span>{cite.pageOrSection}</span>
                      <span className="group-hover:underline flex items-center gap-0.5">
                        Xem chi tiết <ExternalLink className="w-2.5 h-2.5" />
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* CARD LỊCH SỬ XỬ LÝ TICKET (AUDIT LOG - FR-TK-09, BR-15) */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3">
            <div className="flex items-center justify-between border-b border-slate-100 pb-2">
              <div className="flex items-center space-x-2">
                <Clock className="w-4 h-4 text-slate-500" />
                <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider">
                  Nhật ký vòng đời xử lý (Audit Trail)
                </h3>
              </div>
              <span className="text-[11px] text-slate-400">Ghi nhận tự động</span>
            </div>

            <div className="space-y-2 text-xs">
              <div className="flex items-start space-x-3 text-slate-600">
                <div className="w-2 h-2 rounded-full bg-blue-500 mt-1.5 shrink-0" />
                <div>
                  <span className="font-semibold text-slate-800">{ticket.customer.name}</span> đã gửi ticket #{ticket.ticketNumber} vào hệ thống.
                  <span className="text-[10px] text-slate-400 ml-2">{new Date(ticket.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                </div>
              </div>

              {ticket.assignee && (
                <div className="flex items-start space-x-3 text-slate-600">
                  <div className="w-2 h-2 rounded-full bg-amber-500 mt-1.5 shrink-0" />
                  <div>
                    Nhân viên <span className="font-semibold text-slate-800">{ticket.assignee.name}</span> đã tiếp nhận (Claim) ticket để xử lý.
                    <span className="text-[10px] text-slate-400 ml-2">Đang xử lý</span>
                  </div>
                </div>
              )}

              {ticket.status === 'RESOLVED' && (
                <div className="flex items-start space-x-3 text-emerald-700">
                  <div className="w-2 h-2 rounded-full bg-emerald-500 mt-1.5 shrink-0" />
                  <div>
                    Ticket đã được đánh dấu <span className="font-semibold">Hoàn tất (Resolved)</span>.
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================
          CỘT PHẢI: KHUNG CHAT TRAO ĐỔI (ĐỘ RỘNG NHỎ LẠI CỠ KHUNG CHAT FB ~400px)
          KÈM AI SUGGESTION AUTO HIỆN RA CHO MỖI CÂU HỎI (ACCEPT, EDIT, DECLINE)
          ======================================================== */}
      <div className="w-96 lg:w-[410px] shrink-0 flex flex-col h-full bg-white shadow-xs border-l border-slate-200 text-left">
        {/* Chat Header kiểu Messenger */}
        <div className="p-3 bg-white border-b border-slate-200 flex items-center justify-between shrink-0">
          <div className="flex items-center space-x-2.5">
            <div className="relative">
              <img
                src={ticket.customer.avatar || 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'}
                alt={ticket.customer.name}
                className="w-8 h-8 rounded-full object-cover ring-1 ring-slate-200"
              />
              <span className="absolute bottom-0 right-0 w-2 h-2 bg-emerald-500 rounded-full ring-1 ring-white" />
            </div>
            <div>
              <h3 className="text-xs font-bold text-slate-900 leading-tight truncate max-w-[170px]">
                {ticket.customer.name}
              </h3>
              <p className="text-[10px] text-emerald-600 font-medium">Hội thoại trực tiếp</p>
            </div>
          </div>

          <div className="flex items-center space-x-1.5 text-xs">
            <span className="text-[11px] text-slate-400 font-mono">#{ticket.ticketNumber}</span>
          </div>
        </div>

        {/* Messages Stream: Bong bóng chat kiểu FB Messenger */}
        <div className="flex-1 overflow-y-auto p-3 space-y-3 bg-slate-50/50">
          {messages.map((msg) => {
            if (msg.isInternal) {
              return (
                <div
                  key={msg.id}
                  className="bg-amber-50 border border-amber-200/90 rounded-xl p-2.5 space-y-1 shadow-2xs text-left"
                >
                  <div className="flex items-center justify-between text-[11px]">
                    <div className="flex items-center space-x-1.5 text-amber-900 font-bold">
                      <Lock className="w-3 h-3 text-amber-700" />
                      <span>Ghi chú nội bộ</span>
                    </div>
                    <span className="text-[10px] text-amber-700/70">
                      {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </span>
                  </div>
                  <p className="text-xs text-slate-800 leading-relaxed whitespace-pre-wrap font-normal">
                    {msg.content}
                  </p>
                </div>
              );
            }

            const isCustomer = msg.sender.role === 'CUSTOMER';
            return (
              <div
                key={msg.id}
                className={`group flex space-x-2 ${isCustomer ? 'mr-auto' : 'ml-auto flex-row-reverse space-x-reverse'}`}
              >
                <img
                  src={msg.sender.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80'}
                  alt={msg.sender.name}
                  className="w-6 h-6 rounded-full ring-1 ring-slate-200 shadow-2xs shrink-0 object-cover mt-auto"
                />
                <div className="space-y-0.5 text-left relative max-w-[280px]">
                  <div className={`flex items-center space-x-1.5 text-[10px] text-slate-400 ${isCustomer ? '' : 'justify-end'}`}>
                    <span className="font-semibold text-slate-700">{msg.sender.name}</span>
                    <span>• {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                    {!isCustomer && (
                      <CheckCheck className="w-3 h-3 text-helpdesk-600 inline ml-0.5" />
                    )}
                  </div>

                  <div className="relative">
                    <div
                      className={`p-2.5 text-xs leading-relaxed shadow-2xs whitespace-pre-wrap ${
                        isCustomer
                          ? 'bg-white text-slate-800 border border-slate-200 rounded-2xl rounded-bl-xs'
                          : 'bg-helpdesk-600 text-white rounded-2xl rounded-br-xs'
                      }`}
                    >
                      {msg.content}
                    </div>

                    {/* Quick hover copy */}
                    <button
                      type="button"
                      onClick={() => handleCopyMessage(msg.content, msg.id)}
                      title="Sao chép"
                      className={`absolute top-1 opacity-0 group-hover:opacity-100 transition-opacity p-1 rounded bg-white shadow-xs border border-slate-200 text-slate-400 hover:text-slate-700 ${
                        isCustomer ? '-right-6' : '-left-6'
                      }`}
                    >
                      {copiedMsgId === msg.id ? (
                        <Check className="w-2.5 h-2.5 text-emerald-600" />
                      ) : (
                        <Copy className="w-2.5 h-2.5" />
                      )}
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
          <div ref={messagesEndRef} />
        </div>

        {/* ========================================================
            CARD GỢI Ý CỦA AI: TỰ ĐỘNG HIỆN RA CHO MỖI CÂU HỎI / TICKET
            KÈM 3 ACTION: ACCEPT, EDIT, DECLINE (LÀM NỔI BẬT TÍNH NĂNG AI)
            ======================================================== */}
        {aiSuggestion && !isAIDeclined && (
          <div className="mx-2.5 mb-2 p-3 bg-gradient-to-br from-purple-50 via-indigo-50/70 to-purple-50/50 border border-purple-200 rounded-2xl shadow-sm text-left space-y-2 animate-in fade-in slide-in-from-bottom-2 duration-150">
            {/* Header gợi ý */}
            <div className="flex items-center justify-between text-xs">
              <div className="flex items-center space-x-1.5">
                <div className="p-1 bg-purple-600 text-white rounded-md shadow-2xs">
                  <Sparkles className="w-3.5 h-3.5" />
                </div>
                <h4 className="font-bold text-purple-950 text-xs">✨ AI Đề xuất câu trả lời</h4>
                <span className="text-[10px] bg-purple-200 text-purple-900 font-bold px-1.5 py-0.2 rounded-full">
                  {Math.round((aiSuggestion.confidence || 0.95) * 100)}% khớp
                </span>
              </div>
              <button
                onClick={handleDeclineAI}
                title="Bỏ qua gợi ý này"
                className="text-slate-400 hover:text-slate-600 p-0.5 rounded transition"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Nội dung câu trả lời nháp */}
            <div className="p-2.5 bg-white/95 border border-purple-100 rounded-xl text-xs text-slate-700 leading-relaxed max-h-32 overflow-y-auto whitespace-pre-wrap shadow-2xs font-normal">
              {aiSuggestion.draftReply}
            </div>

            {/* Trích dẫn nguồn click xem */}
            {aiSuggestion.citations && aiSuggestion.citations[0] && (
              <div 
                onClick={() => setSelectedCitation(aiSuggestion.citations[0])}
                className="flex items-center justify-between p-1.5 bg-white/80 hover:bg-white border border-purple-100 hover:border-purple-300 rounded-lg text-[11px] text-purple-900 cursor-pointer transition shadow-2xs"
              >
                <span className="truncate max-w-[240px] font-medium text-[10px]">
                  📚 {aiSuggestion.citations[0].documentTitle}
                </span>
                <span className="text-purple-600 font-bold text-[10px] shrink-0 flex items-center gap-0.5">
                  Xem nguồn <ExternalLink className="w-2.5 h-2.5" />
                </span>
              </div>
            )}

            {/* 3 Nút hành động nổi bật: Accept (ac), Edit, Decline */}
            <div className="flex items-center space-x-1.5 pt-0.5">
              <button
                type="button"
                onClick={handleAcceptAI}
                title="Chấp nhận bản nháp và đưa vào ô trả lời"
                className="flex-1 py-1.5 px-2 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white rounded-xl text-xs font-semibold shadow-xs transition active:scale-95 flex items-center justify-center space-x-1"
              >
                <Check className="w-3 h-3" />
                <span>Áp dụng (Accept)</span>
              </button>

              <button
                type="button"
                onClick={handleEditAI}
                title="Chỉnh sửa nội dung bản nháp trước khi gửi"
                className="py-1.5 px-3 bg-white hover:bg-purple-50 text-purple-800 border border-purple-200 rounded-xl text-xs font-semibold shadow-xs transition active:scale-95 flex items-center justify-center space-x-1"
              >
                <span>Sửa (Edit)</span>
              </button>

              <button
                type="button"
                onClick={handleDeclineAI}
                title="Từ chối gợi ý này"
                className="py-1.5 px-2.5 text-slate-500 hover:text-rose-600 hover:bg-rose-50 rounded-xl text-xs transition font-medium"
              >
                <span>Từ chối</span>
              </button>
            </div>
          </div>
        )}

        {/* Nút hiện lại nếu lỡ bấm decline */}
        {aiSuggestion && isAIDeclined && (
          <div className="px-3 py-1 flex justify-end">
            <button
              type="button"
              onClick={() => setIsAIDeclined(false)}
              className="inline-flex items-center space-x-1 text-[11px] text-purple-600 hover:text-purple-800 font-medium py-1 px-2 hover:bg-purple-50 rounded-lg transition"
            >
              <RotateCcw className="w-3 h-3" />
              <span>Hiện lại gợi ý AI</span>
            </button>
          </div>
        )}

        {/* Composer (Khung soạn tin nhắn sát đáy) */}
        <div className="p-2.5 bg-white border-t border-slate-200 shrink-0">
          <form onSubmit={handleSend} className="space-y-1.5">
            {/* Toolbar trên ô gõ */}
            <div className="flex items-center justify-between">
              <div className="flex space-x-1 bg-slate-100 p-0.5 rounded-lg border border-slate-200 text-xs">
                <button
                  type="button"
                  onClick={() => setReplyType('PUBLIC')}
                  className={`px-2.5 py-0.5 rounded-md text-[11px] font-medium transition ${
                    replyType === 'PUBLIC'
                      ? 'bg-white text-slate-900 shadow-xs font-semibold'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  Công khai
                </button>
                <button
                  type="button"
                  onClick={() => setReplyType('INTERNAL')}
                  className={`px-2.5 py-0.5 rounded-md text-[11px] font-medium transition flex items-center space-x-1 ${
                    replyType === 'INTERNAL'
                      ? 'bg-amber-100 text-amber-900 shadow-xs font-semibold'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <Lock className="w-2.5 h-2.5 text-amber-700" />
                  <span>Nội bộ</span>
                </button>
              </div>

              {/* Quick macros menu */}
              <div className="relative">
                <button
                  type="button"
                  title="Mẫu trả lời nhanh (Macros)"
                  onClick={() => setShowCannedMenu(!showCannedMenu)}
                  className="inline-flex items-center space-x-1 px-2 py-0.5 text-slate-600 hover:text-helpdesk-700 hover:bg-slate-100 rounded-lg transition text-[11px] font-medium"
                >
                  <Zap className="w-3 h-3 text-amber-500" />
                  <span>Mẫu nhanh</span>
                </button>

                {showCannedMenu && (
                  <div className="absolute bottom-7 right-0 w-64 bg-white border border-slate-200 rounded-xl shadow-xl p-2 z-30 space-y-1 animate-in fade-in text-left">
                    <div className="px-2 py-1 text-[10px] font-bold text-slate-400 uppercase tracking-wider">
                      Mẫu câu phản hồi
                    </div>
                    {cannedResponses.map((item, idx) => (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => {
                          setReplyText(item.text);
                          setShowCannedMenu(false);
                        }}
                        className="w-full text-left p-1.5 hover:bg-slate-50 rounded-lg text-xs text-slate-700 transition space-y-0.5"
                      >
                        <p className="font-semibold text-slate-900 text-xs">{item.label}</p>
                        <p className="text-[10px] text-slate-500 line-clamp-1">{item.text}</p>
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>

            {/* Textarea nhập tin */}
            <div className="relative">
              <textarea
                ref={textareaRef}
                value={replyText}
                onChange={(e) => setReplyText(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={
                  replyType === 'PUBLIC'
                    ? 'Nhập tin nhắn (Enter để gửi)...'
                    : 'Ghi chú nội bộ...'
                }
                rows={2}
                className={`w-full p-2 text-xs rounded-xl border focus:outline-none focus:ring-2 transition resize-none ${
                  replyType === 'INTERNAL'
                    ? 'bg-amber-50/60 border-amber-300 focus:ring-amber-400/30 text-amber-950 placeholder-amber-700/50'
                    : 'bg-slate-50 border-slate-200 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 text-slate-800'
                }`}
              />
            </div>

            {/* Bottom bar: Attachments & Send */}
            <div className="flex items-center justify-between text-xs pt-0.5">
              <div className="flex items-center space-x-1">
                <button
                  type="button"
                  title="Đính kèm tệp"
                  onClick={() => setReplyText(prev => prev + (prev ? '\n' : '') + '[📎 File_dinh_kem.pdf] ')}
                  className="p-1 text-slate-500 hover:text-helpdesk-600 hover:bg-slate-100 rounded-lg transition"
                >
                  <Paperclip className="w-3.5 h-3.5" />
                </button>

                <button
                  type="button"
                  title="Chèn ảnh"
                  onClick={() => setReplyText(prev => prev + (prev ? '\n' : '') + '[🖼️ Anh_chup_loi.png] ')}
                  className="p-1 text-slate-500 hover:text-helpdesk-600 hover:bg-slate-100 rounded-lg transition"
                >
                  <ImageIcon className="w-3.5 h-3.5" />
                </button>

                <div className="relative">
                  <button
                    type="button"
                    title="Emoji"
                    onClick={() => setShowEmojiPicker(!showEmojiPicker)}
                    className="p-1 text-slate-500 hover:text-amber-600 hover:bg-slate-100 rounded-lg transition"
                  >
                    <Smile className="w-3.5 h-3.5" />
                  </button>
                  {showEmojiPicker && (
                    <div className="absolute bottom-8 left-0 bg-white border border-slate-200 rounded-xl shadow-lg p-1.5 flex items-center space-x-1 z-30 animate-in fade-in">
                      {emojis.map((emoji) => (
                        <button
                          key={emoji}
                          type="button"
                          onClick={() => {
                            setReplyText(prev => prev + emoji);
                            setShowEmojiPicker(false);
                          }}
                          className="p-1 hover:bg-slate-100 rounded text-sm transition"
                        >
                          {emoji}
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              </div>

              <button
                type="submit"
                disabled={!replyText.trim()}
                className={`inline-flex items-center space-x-1 px-3 py-1.5 text-xs font-semibold rounded-xl shadow-xs transition ${
                  replyText.trim()
                    ? replyType === 'INTERNAL'
                      ? 'bg-amber-600 hover:bg-amber-700 text-white'
                      : 'bg-helpdesk-600 hover:bg-helpdesk-700 text-white'
                    : 'bg-slate-100 text-slate-400 cursor-not-allowed'
                }`}
              >
                <Send className="w-3 h-3" />
                <span>{replyType === 'INTERNAL' ? 'Lưu' : 'Gửi'}</span>
              </button>
            </div>
          </form>
        </div>
      </div>

      {/* Citation Detail Modal */}
      {selectedCitation && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-lg w-full p-5 space-y-4 shadow-xl border border-slate-200 text-left animate-in fade-in zoom-in-95">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div className="flex items-center space-x-2">
                <Sparkles className="w-4 h-4 text-purple-600" />
                <h3 className="font-bold text-sm text-slate-900">Chi tiết nguồn trích dẫn RAG</h3>
              </div>
              <button
                onClick={() => setSelectedCitation(null)}
                className="text-slate-400 hover:text-slate-600 text-xs px-2 py-1 rounded"
              >
                ✕ Đóng
              </button>
            </div>

            <div className="space-y-3 text-xs">
              <div>
                <span className="text-slate-400 block text-[10px] uppercase font-bold">Tài liệu</span>
                <p className="font-semibold text-purple-950 text-sm">{selectedCitation.documentTitle}</p>
              </div>

              <div>
                <span className="text-slate-400 block text-[10px] uppercase font-bold">Vị trí</span>
                <p className="font-medium text-slate-700">{selectedCitation.pageOrSection}</p>
              </div>

              <div>
                <span className="text-slate-400 block text-[10px] uppercase font-bold">Đoạn trích Vector Chunk</span>
                <div className="p-3 bg-purple-50/70 border border-purple-200 rounded-xl text-slate-800 font-serif leading-relaxed italic">
                  "{selectedCitation.chunkSnippet}"
                </div>
              </div>
            </div>

            <button
              onClick={() => setSelectedCitation(null)}
              className="w-full py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-semibold"
            >
              Đóng xem trước
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
