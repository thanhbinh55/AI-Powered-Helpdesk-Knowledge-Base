import React, { useState } from 'react';
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
  Loader2,
  X,
  Clock,
  Inbox,
  Paperclip,
  Image as ImageIcon,
  Smile,
  Zap,
  CheckCheck,
  Copy,
  Check
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
}) => {
  const [replyType, setReplyType] = useState<'PUBLIC' | 'INTERNAL'>('PUBLIC');
  const [replyText, setReplyText] = useState('');
  const [isGeneratingAI, setIsGeneratingAI] = useState(false);
  const [isCopilotOpen, setIsCopilotOpen] = useState(false);
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null);
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const [showCannedMenu, setShowCannedMenu] = useState(false);
  const [copiedMsgId, setCopiedMsgId] = useState<string | null>(null);

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

  const handleToggleAI = () => {
    if (!isCopilotOpen) {
      setIsGeneratingAI(true);
      setIsCopilotOpen(true);
      setTimeout(() => {
        setIsGeneratingAI(false);
      }, 500);
    } else {
      setIsCopilotOpen(false);
    }
  };

  const handleApplyAISuggestion = () => {
    if (aiSuggestion) {
      setReplyText(aiSuggestion.draftReply);
      setReplyType('PUBLIC');
      setIsCopilotOpen(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col bg-slate-100 overflow-hidden h-[calc(100vh-3.5rem)] relative">
      {/* 1. Header: Rộng rãi, sạch sẽ */}
      <div className="bg-white border-b border-slate-200 px-6 py-3 shadow-2xs shrink-0 text-left">
        {/* Top line: Meta & Actions */}
        <div className="flex flex-wrap items-center justify-between gap-2 mb-1">
          <div className="flex items-center space-x-2">
            {/* Button to reopen Queue if collapsed */}
            {isQueueCollapsed && onToggleQueue && (
              <button
                onClick={onToggleQueue}
                title="Mở lại hàng đợi ticket"
                className="inline-flex items-center space-x-1.5 px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg transition mr-1"
              >
                <Inbox className="w-3.5 h-3.5 text-helpdesk-600" />
                <span>Mở hàng đợi</span>
              </button>
            )}

            <span className="font-mono text-xs font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">
              #{ticket.ticketNumber}
            </span>
            <Badge variant="status" value={ticket.status} />
            <Badge variant="priority" value={ticket.priority} />
            <span className="text-xs text-slate-400">•</span>
            <span className="text-xs font-medium text-slate-600">{ticket.category}</span>
          </div>

          {/* Action Buttons: Claim / Resolve */}
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
                <span className="text-slate-400">Người phụ trách:</span>
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

        {/* Title */}
        <h1 className="text-base font-bold text-slate-900 tracking-tight leading-snug">
          {ticket.title}
        </h1>

        {/* Customer Information Strip */}
        <div className="mt-2 pt-2 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-500 gap-y-1">
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
              <span className="text-[10px] text-emerald-600 bg-emerald-50 px-1.5 py-0.5 rounded-full font-medium hidden sm:inline">
                ● Trực tuyến
              </span>
              <span className="text-slate-400 flex items-center gap-1">
                <Mail className="w-3 h-3 text-slate-400" /> {ticket.customer.email}
              </span>
            </div>

            <div className="hidden md:flex items-center space-x-1 text-slate-600">
              <Building className="w-3.5 h-3.5 text-slate-400" />
              <span>{ticket.customer.organization || 'Khoa CNTT'}</span>
            </div>
          </div>

          <div className="flex items-center space-x-3 text-[11px]">
            <span className="text-slate-400">Tạo: {new Date(ticket.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
            <div className="flex items-center space-x-1 text-amber-700 bg-amber-50 border border-amber-200/80 px-2 py-0.5 rounded-full font-medium">
              <Clock className="w-3 h-3" />
              <span>SLA: Còn 4 giờ</span>
            </div>
          </div>
        </div>
      </div>

      {/* OPEN QUEUE CLAIM BANNER (Nếu ticket chưa ai nhận) */}
      {!ticket.assignee && (
        <div className="mx-6 mt-3 p-3.5 bg-blue-50/90 border border-blue-200 rounded-2xl flex flex-wrap items-center justify-between gap-3 shadow-2xs text-left animate-in fade-in">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-blue-100 text-blue-700 rounded-xl">
              <Inbox className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h4 className="font-bold text-xs text-blue-950">Ticket đang trong Hàng đợi chờ tiếp nhận</h4>
                <span className="text-[10px] bg-blue-200/70 text-blue-800 px-2 py-0.5 rounded-full font-semibold">
                  Hàng đợi OPEN
                </span>
              </div>
              <p className="text-[11px] text-blue-700/90 mt-0.5">
                Chưa có nhân viên phụ trách. Hãy nhận xử lý để chuyển ticket vào mục "Đang xử lý" của bạn và bắt đầu trả lời khách hàng.
              </p>
            </div>
          </div>
          <button
            onClick={() => onClaimTicket(ticket.id)}
            className="inline-flex items-center space-x-1.5 px-4 py-2 bg-helpdesk-600 hover:bg-helpdesk-700 text-white text-xs font-semibold rounded-xl shadow-xs transition active:scale-95 shrink-0"
          >
            <UserCheck className="w-3.5 h-3.5" />
            <span>Nhận xử lý ngay (Claim)</span>
          </button>
        </div>
      )}

      {/* 2. Message Thread: Tối ưu diện tích cuộn lớn hơn, bong bóng kiểu Zalo/Messenger */}
      <div className="flex-1 overflow-y-auto px-6 lg:px-12 py-4 space-y-4">
        {messages.map((msg) => {
          if (msg.isInternal) {
            return (
              <div
                key={msg.id}
                className="max-w-3xl mx-auto bg-amber-50/80 border border-amber-200/90 rounded-2xl p-3.5 space-y-1.5 shadow-2xs text-left"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <div className="p-1 bg-amber-200 text-amber-800 rounded-md">
                      <Lock className="w-3 h-3" />
                    </div>
                    <span className="text-xs font-bold text-amber-900">
                      Ghi chú nội bộ (Chỉ Agent & Admin thấy)
                    </span>
                    <span className="text-xs text-amber-700 font-medium">• {msg.sender.name}</span>
                  </div>
                  <span className="text-[10px] text-amber-700/80">
                    {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>
                <p className="text-xs text-slate-800 leading-relaxed font-normal whitespace-pre-wrap pl-6">
                  {msg.content}
                </p>
              </div>
            );
          }

          const isCustomer = msg.sender.role === 'CUSTOMER';
          return (
            <div
              key={msg.id}
              className={`group flex space-x-3 max-w-3xl ${isCustomer ? 'mr-auto' : 'ml-auto flex-row-reverse space-x-reverse'}`}
            >
              <img
                src={msg.sender.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80'}
                alt={msg.sender.name}
                className="w-7 h-7 rounded-full ring-2 ring-white shadow-xs shrink-0 object-cover"
              />
              <div className="space-y-1 text-left relative max-w-xl">
                <div className={`flex items-center space-x-2 text-[11px] ${isCustomer ? '' : 'justify-end'}`}>
                  <span className="font-semibold text-slate-800">{msg.sender.name}</span>
                  <Badge variant="role" value={msg.sender.role} />
                  <span className="text-slate-400">
                    {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                  {!isCustomer && (
                    <span title="Đã gửi & đã nhận">
                      <CheckCheck className="w-3.5 h-3.5 text-helpdesk-600 inline ml-0.5" />
                    </span>
                  )}
                </div>

                <div className="relative">
                  <div
                    className={`p-3 text-xs leading-relaxed shadow-xs whitespace-pre-wrap ${
                      isCustomer
                        ? 'bg-white text-slate-800 border border-slate-200/90 rounded-2xl rounded-tl-xs'
                        : 'bg-helpdesk-600 text-white rounded-2xl rounded-tr-xs'
                    }`}
                  >
                    {msg.content}
                  </div>

                  {/* Quick hover action: Copy message (như Zalo/Messenger) */}
                  <button
                    type="button"
                    onClick={() => handleCopyMessage(msg.content, msg.id)}
                    title="Sao chép tin nhắn"
                    className={`absolute top-1 opacity-0 group-hover:opacity-100 transition-opacity p-1 rounded-md text-slate-400 hover:text-slate-700 bg-white/90 shadow-2xs border border-slate-200 ${
                      isCustomer ? '-right-7' : '-left-7'
                    }`}
                  >
                    {copiedMsgId === msg.id ? (
                      <Check className="w-3 h-3 text-emerald-600" />
                    ) : (
                      <Copy className="w-3 h-3" />
                    )}
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* 3. Message Composer: Đặt sát đáy, tinh gọn, tích hợp phím Enter & thanh công cụ nhanh */}
      <div className="bg-white border-t border-slate-200 px-6 py-2.5 shrink-0 shadow-sm relative">
        <form onSubmit={handleSend} className="max-w-4xl mx-auto space-y-2">
          {/* Toolbar: Tabs & AI & Quick Actions */}
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="flex space-x-1 bg-slate-100 p-0.5 rounded-lg border border-slate-200 text-xs">
                <button
                  type="button"
                  onClick={() => setReplyType('PUBLIC')}
                  className={`px-3 py-1 rounded-md font-medium transition ${
                    replyType === 'PUBLIC'
                      ? 'bg-white text-slate-900 shadow-xs font-semibold'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  Trả lời công khai
                </button>
                <button
                  type="button"
                  onClick={() => setReplyType('INTERNAL')}
                  className={`px-3 py-1 rounded-md font-medium transition flex items-center space-x-1.5 ${
                    replyType === 'INTERNAL'
                      ? 'bg-amber-100 text-amber-900 shadow-xs font-semibold'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <Lock className="w-3 h-3 text-amber-700" />
                  <span>Ghi chú nội bộ</span>
                </button>
              </div>

              {/* Quick Attachment Icons (Zalo / Messenger Style) */}
              <div className="hidden sm:flex items-center space-x-1 pl-1 border-l border-slate-200">
                <button
                  type="button"
                  title="Đính kèm tệp / tài liệu"
                  onClick={() => setReplyText(prev => prev + (prev ? '\n' : '') + '[📎 Dinh_kem_minh_chung.pdf] ')}
                  className="p-1.5 text-slate-500 hover:text-helpdesk-600 hover:bg-slate-100 rounded-lg transition"
                >
                  <Paperclip className="w-3.5 h-3.5" />
                </button>
                <button
                  type="button"
                  title="Gửi ảnh / Ảnh chụp màn hình lỗi"
                  onClick={() => setReplyText(prev => prev + (prev ? '\n' : '') + '[🖼️ Anh_chup_loi_portal.png] ')}
                  className="p-1.5 text-slate-500 hover:text-helpdesk-600 hover:bg-slate-100 rounded-lg transition"
                >
                  <ImageIcon className="w-3.5 h-3.5" />
                </button>
                
                {/* Emoji Picker Button */}
                <div className="relative">
                  <button
                    type="button"
                    title="Chèn biểu tượng cảm xúc"
                    onClick={() => {
                      setShowEmojiPicker(!showEmojiPicker);
                      setShowCannedMenu(false);
                    }}
                    className="p-1.5 text-slate-500 hover:text-amber-600 hover:bg-slate-100 rounded-lg transition"
                  >
                    <Smile className="w-3.5 h-3.5" />
                  </button>
                  {showEmojiPicker && (
                    <div className="absolute bottom-9 left-0 bg-white border border-slate-200 rounded-xl shadow-lg p-2 flex items-center space-x-1.5 z-30 animate-in fade-in">
                      {emojis.map((emoji) => (
                        <button
                          key={emoji}
                          type="button"
                          onClick={() => {
                            setReplyText(prev => prev + emoji);
                            setShowEmojiPicker(false);
                          }}
                          className="p-1 hover:bg-slate-100 rounded text-base transition"
                        >
                          {emoji}
                        </button>
                      ))}
                    </div>
                  )}
                </div>

                {/* Quick Canned Responses / Macros Button */}
                <div className="relative">
                  <button
                    type="button"
                    title="Mẫu trả lời nhanh (Macros)"
                    onClick={() => {
                      setShowCannedMenu(!showCannedMenu);
                      setShowEmojiPicker(false);
                    }}
                    className="inline-flex items-center space-x-1 px-2 py-1 text-slate-600 hover:text-helpdesk-700 hover:bg-slate-100 rounded-lg transition text-[11px] font-medium"
                  >
                    <Zap className="w-3 h-3 text-amber-500" />
                    <span>Mẫu nhanh</span>
                  </button>

                  {showCannedMenu && (
                    <div className="absolute bottom-9 left-0 w-72 bg-white border border-slate-200 rounded-xl shadow-xl p-2 z-30 space-y-1 animate-in fade-in text-left">
                      <div className="px-2 py-1 text-[10px] font-bold text-slate-400 uppercase tracking-wider">
                        Mẫu câu phản hồi nhanh
                      </div>
                      {cannedResponses.map((item, idx) => (
                        <button
                          key={idx}
                          type="button"
                          onClick={() => {
                            setReplyText(item.text);
                            setShowCannedMenu(false);
                          }}
                          className="w-full text-left p-2 hover:bg-slate-50 rounded-lg text-xs text-slate-700 transition space-y-0.5"
                        >
                          <p className="font-semibold text-slate-900">{item.label}</p>
                          <p className="text-[11px] text-slate-500 line-clamp-1">{item.text}</p>
                        </button>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* DUY NHẤT 1 VỊ TRÍ MỞ AI COPILOT */}
            <button
              type="button"
              onClick={handleToggleAI}
              className={`inline-flex items-center space-x-1.5 px-3 py-1 text-xs font-semibold rounded-lg shadow-xs transition active:scale-95 ${
                isCopilotOpen
                  ? 'bg-purple-100 text-purple-900 border border-purple-300'
                  : 'bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white'
              }`}
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>{isCopilotOpen ? 'Đóng AI Copilot' : '✨ AI Gợi ý phản hồi'}</span>
            </button>
          </div>

          {/* Textarea: Chiều cao vừa vặn, không chiếm chỗ, Enter để gửi */}
          <div className="relative">
            <textarea
              value={replyText}
              onChange={(e) => setReplyText(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                replyType === 'PUBLIC'
                  ? 'Nhập nội dung phản hồi gửi đến khách hàng (Enter để gửi, Shift+Enter để xuống dòng)...'
                  : 'Nhập ghi chú nội bộ (chỉ nhân viên hỗ trợ và quản trị viên xem được)...'
              }
              rows={2}
              className={`w-full p-2.5 text-xs rounded-xl border focus:outline-none focus:ring-2 transition resize-none ${
                replyType === 'INTERNAL'
                  ? 'bg-amber-50/60 border-amber-300 focus:ring-amber-400/30 text-amber-950 placeholder-amber-700/50'
                  : 'bg-slate-50 border-slate-200 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 text-slate-800'
              }`}
            />
          </div>

          {/* Bottom Toolbar: Sát đáy, Nút gửi không bị che */}
          <div className="flex items-center justify-between text-xs">
            <span className="text-[11px] text-slate-400 flex items-center space-x-1">
              <span>Nhấn</span>
              <kbd className="px-1.5 py-0.5 bg-slate-100 border border-slate-200 rounded text-[10px] font-mono font-bold text-slate-600">Enter</kbd>
              <span>để gửi •</span>
              <kbd className="px-1.5 py-0.5 bg-slate-100 border border-slate-200 rounded text-[10px] font-mono text-slate-500">Shift + Enter</kbd>
              <span>xuống dòng</span>
            </span>

            <button
              type="submit"
              disabled={!replyText.trim()}
              className={`inline-flex items-center space-x-1.5 px-4 py-1.5 text-xs font-semibold rounded-xl shadow-xs transition ${
                replyText.trim()
                  ? replyType === 'INTERNAL'
                    ? 'bg-amber-600 hover:bg-amber-700 text-white'
                    : 'bg-helpdesk-600 hover:bg-helpdesk-700 text-white'
                  : 'bg-slate-100 text-slate-400 cursor-not-allowed'
              }`}
            >
              <Send className="w-3.5 h-3.5" />
              <span>{replyType === 'INTERNAL' ? 'Lưu ghi chú' : 'Gửi cho khách'}</span>
            </button>
          </div>
        </form>
      </div>

      {/* 4. AI COPILOT POPUP DOCK (Chỉ mở khi bấm nút, vị trí bottom-24 không bao giờ che nút gửi) */}
      {isCopilotOpen && (
        <div className="absolute bottom-20 right-8 z-40 w-96 max-w-[90vw] bg-white rounded-2xl shadow-2xl border border-purple-200 flex flex-col overflow-hidden animate-in fade-in slide-in-from-bottom-3 duration-150 text-left">
          {/* Header */}
          <div className="bg-gradient-to-r from-purple-700 to-indigo-700 px-4 py-2.5 text-white flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Sparkles className="w-4 h-4 text-purple-200" />
              <h3 className="font-bold text-xs">Trợ lý AI Copilot</h3>
              <span className="text-[10px] bg-white/20 text-purple-100 px-2 py-0.5 rounded-full font-medium">
                Khớp 95%
              </span>
            </div>
            <button
              onClick={() => setIsCopilotOpen(false)}
              className="text-white/80 hover:text-white p-1 rounded-md hover:bg-white/10 transition"
              title="Đóng ô trợ lý"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Body */}
          <div className="p-3.5 space-y-3 max-h-[60vh] overflow-y-auto bg-slate-50/50">
            {/* Warning tag */}
            <div className="bg-purple-100/70 border border-purple-200 rounded-lg p-2 flex items-center space-x-2 text-[11px] text-purple-900 font-medium">
              <ShieldCheck className="w-4 h-4 text-purple-600 shrink-0" />
              <span>Gợi ý tạo bởi AI — hãy duyệt trước khi gửi</span>
            </div>

            {/* AI Draft Text */}
            {isGeneratingAI ? (
              <div className="py-6 text-center space-y-2 text-slate-500">
                <Loader2 className="w-5 h-5 animate-spin mx-auto text-purple-600" />
                <p className="text-xs font-medium">RAG pgvector đang sinh câu trả lời...</p>
              </div>
            ) : aiSuggestion ? (
              <div className="space-y-2.5">
                <div className="bg-white border border-purple-100 rounded-xl p-3 text-xs text-slate-700 leading-relaxed whitespace-pre-wrap max-h-40 overflow-y-auto shadow-2xs">
                  {aiSuggestion.draftReply}
                </div>

                <button
                  onClick={handleApplyAISuggestion}
                  className="w-full py-1.5 bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold rounded-xl shadow-xs transition flex items-center justify-center space-x-1.5"
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Áp dụng vào khung trả lời (Apply Draft)</span>
                </button>

                {/* Citations List */}
                <div className="space-y-1.5 pt-1">
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
                    Nguồn trích dẫn (Citations)
                  </span>
                  {aiSuggestion.citations.map((cite, idx) => (
                    <div
                      key={idx}
                      onClick={() => setSelectedCitation(cite)}
                      className="p-2.5 bg-white border border-slate-200 hover:border-purple-300 rounded-xl cursor-pointer transition text-left space-y-1"
                    >
                      <div className="flex items-center justify-between text-[11px]">
                        <span className="font-semibold text-purple-900 truncate max-w-[210px]">
                          {cite.documentTitle}
                        </span>
                        <span className="text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.2 rounded text-[10px]">
                          {Math.round(cite.score * 100)}% match
                        </span>
                      </div>
                      <p className="text-[10px] text-slate-500 line-clamp-2 italic">
                        "{cite.chunkSnippet}"
                      </p>
                      <div className="flex items-center space-x-1 text-[10px] text-purple-600 font-medium">
                        <ExternalLink className="w-2.5 h-2.5" />
                        <span>{cite.pageOrSection || 'Xem đoạn trích RAG'}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div className="text-center py-6 text-slate-400 space-y-1">
                <Sparkles className="w-6 h-6 mx-auto text-purple-300" />
                <p className="text-xs">Chưa có gợi ý nào cho ticket này</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Citation Detail Modal */}
      {selectedCitation && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-lg w-full p-5 space-y-4 shadow-xl border border-slate-200 text-left">
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
