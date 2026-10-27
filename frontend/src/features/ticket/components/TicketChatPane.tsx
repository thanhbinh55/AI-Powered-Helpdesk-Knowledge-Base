import React, { useState, useRef, useEffect } from 'react';
import { 
  Send, 
  Lock, 
  Paperclip, 
  Image as ImageIcon, 
  Smile, 
  Zap, 
  CheckCheck, 
  Copy, 
  Check 
} from 'lucide-react';
import { Ticket, Message, AISuggestion, Citation } from '../../../types';
import { AISuggestionCard } from './AISuggestionCard';

interface TicketChatPaneProps {
  ticket: Ticket;
  messages: Message[];
  aiSuggestion?: AISuggestion | null;
  isAIDeclined: boolean;
  onAcceptAI: (draft: string) => void;
  onEditAI: (draft: string) => void;
  onDeclineAI: () => void;
  onRestoreAI: () => void;
  onViewCitation: (citation: Citation) => void;
  onSendMessage: (ticketId: string, content: string, isInternal: boolean) => void;
  replyText: string;
  setReplyText: React.Dispatch<React.SetStateAction<string>>;
  textareaRef: React.RefObject<HTMLTextAreaElement>;
}

export const TicketChatPane: React.FC<TicketChatPaneProps> = ({
  ticket,
  messages,
  aiSuggestion,
  isAIDeclined,
  onAcceptAI,
  onEditAI,
  onDeclineAI,
  onRestoreAI,
  onViewCitation,
  onSendMessage,
  replyText,
  setReplyText,
  textareaRef,
}) => {
  const [replyType, setReplyType] = useState<'PUBLIC' | 'INTERNAL'>('PUBLIC');
  const [showEmojiPicker, setShowEmojiPicker] = useState(false);
  const [showCannedMenu, setShowCannedMenu] = useState(false);
  const [copiedMsgId, setCopiedMsgId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const cannedResponses = [
    { title: 'Chào hỏi & Đã tiếp nhận', text: `Chào bạn ${ticket.customer.name},\nMình đã tiếp nhận thông tin yêu cầu của bạn và đang tiến hành kiểm tra trên hệ thống. Sẽ phản hồi kết quả sớm nhất!` },
    { title: 'Yêu cầu bổ sung MSSV / CCCD', text: 'Chào bạn, vui lòng cung cấp thêm Mã số sinh viên (MSSV) và ảnh chụp CCCD 2 mặt để bộ phận hỗ trợ xác thực danh tính nhé.' },
    { title: 'Thông báo đã kích hoạt / xử lý xong', text: 'Chào bạn, sự cố đã được xử lý thành công! Bạn vui lòng đăng nhập lại và kiểm tra giúp mình nhé.' },
  ];

  const emojis = ['👍', '🙏', '😊', '❤️', '🎉', '💡', '✅'];

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleCopyMessage = (content: string, id: string) => {
    navigator.clipboard.writeText(content);
    setCopiedMsgId(id);
    setTimeout(() => setCopiedMsgId(null), 1500);
  };

  const handleSend = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!replyText.trim()) return;
    onSendMessage(ticket.id, replyText, replyType === 'INTERNAL');
    setReplyText('');
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="w-96 lg:w-[410px] shrink-0 flex flex-col h-full bg-white shadow-xs border-l border-slate-200 text-left">
      {/* 1. Chat Header kiểu Messenger */}
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

      {/* 2. Message Stream kiểu Messenger */}
      <div className="flex-1 overflow-y-auto p-3 space-y-3 bg-slate-50/50">
        {messages.map((msg) => {
          const isCustomer = msg.sender.role === 'CUSTOMER';

          if (msg.isInternal) {
            return (
              <div
                key={msg.id}
                className="p-3 bg-amber-50/90 border border-amber-200/90 rounded-2xl shadow-2xs space-y-1 my-1"
              >
                <div className="flex items-center justify-between text-[11px] text-amber-800 font-semibold">
                  <div className="flex items-center space-x-1.5">
                    <Lock className="w-3 h-3 text-amber-600" />
                    <span>Ghi chú nội bộ • {msg.sender.name}</span>
                  </div>
                  <span className="text-[10px] text-amber-600">
                    {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>
                <p className="text-xs text-amber-950 font-normal leading-relaxed whitespace-pre-wrap">
                  {msg.content}
                </p>
              </div>
            );
          }

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

      {/* 3. Card Gợi ý của AI (Tự động hiện ra, 3 actions: Accept, Edit, Decline) */}
      <AISuggestionCard
        suggestion={aiSuggestion}
        isDeclined={isAIDeclined}
        onAccept={() => aiSuggestion && onAcceptAI(aiSuggestion.draftReply)}
        onEdit={() => aiSuggestion && onEditAI(aiSuggestion.draftReply)}
        onDecline={onDeclineAI}
        onRestore={onRestoreAI}
        onViewCitation={onViewCitation}
      />

      {/* 4. Composer (Khung soạn tin nhắn sát đáy) */}
      <div className="p-2.5 bg-white border-t border-slate-200 shrink-0">
        <form onSubmit={handleSend} className="space-y-1.5">
          {/* Toolbar trên ô gõ */}
          <div className="flex items-center justify-between">
            <div className="flex space-x-1 bg-slate-100 p-0.5 rounded-lg border border-slate-200 text-xs">
              <button
                type="button"
                onClick={() => setReplyType('PUBLIC')}
                className={`px-2 py-0.5 rounded-md text-[11px] font-semibold transition ${
                  replyType === 'PUBLIC'
                    ? 'bg-white text-helpdesk-700 shadow-2xs'
                    : 'text-slate-500 hover:text-slate-700'
                }`}
              >
                Khách hàng
              </button>
              <button
                type="button"
                onClick={() => setReplyType('INTERNAL')}
                className={`px-2 py-0.5 rounded-md text-[11px] font-semibold transition flex items-center space-x-1 ${
                  replyType === 'INTERNAL'
                    ? 'bg-amber-100 text-amber-900 shadow-2xs'
                    : 'text-slate-500 hover:text-amber-800'
                }`}
              >
                <Lock className="w-2.5 h-2.5" />
                <span>Ghi chú</span>
              </button>
            </div>

            {/* Mẫu câu trả lời nhanh */}
            <div className="relative">
              <button
                type="button"
                onClick={() => setShowCannedMenu(!showCannedMenu)}
                className="text-[11px] text-slate-500 hover:text-helpdesk-600 font-medium flex items-center space-x-1 px-1.5 py-0.5 rounded hover:bg-slate-100 transition"
              >
                <Zap className="w-3 h-3 text-amber-500" />
                <span>Mẫu câu</span>
              </button>

              {showCannedMenu && (
                <div className="absolute right-0 bottom-full mb-1 w-64 bg-white border border-slate-200 rounded-xl shadow-lg p-1.5 space-y-1 z-30 animate-in fade-in">
                  <div className="text-[10px] font-bold text-slate-400 px-2 py-1 uppercase">
                    Mẫu phản hồi nhanh
                  </div>
                  {cannedResponses.map((res, i) => (
                    <button
                      key={i}
                      type="button"
                      onClick={() => {
                        setReplyText(res.text);
                        setShowCannedMenu(false);
                        textareaRef.current?.focus();
                      }}
                      className="w-full text-left p-1.5 hover:bg-slate-50 rounded-lg text-xs text-slate-700 transition"
                    >
                      <p className="font-semibold text-slate-900 text-[11px]">{res.title}</p>
                      <p className="text-[10px] text-slate-400 truncate">{res.text}</p>
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Ô nhập tin nhắn */}
          <div className="relative">
            <textarea
              ref={textareaRef}
              rows={2}
              value={replyText}
              onChange={(e) => setReplyText(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder={
                replyType === 'INTERNAL'
                  ? 'Viết ghi chú nội bộ (Chỉ nhân viên nhìn thấy)...'
                  : 'Nhập tin nhắn... (Enter gửi, Shift+Enter xuống dòng)'
              }
              className={`w-full p-2.5 text-xs border rounded-xl focus:outline-none focus:ring-2 resize-none transition ${
                replyType === 'INTERNAL'
                  ? 'bg-amber-50/50 border-amber-200 focus:ring-amber-500/20 focus:border-amber-500 placeholder-amber-400'
                  : 'bg-slate-50 border-slate-200 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 placeholder-slate-400'
              }`}
            />
          </div>

          {/* Toolbar dưới: Đính kèm & Nút gửi */}
          <div className="flex items-center justify-between pt-0.5">
            <div className="flex items-center space-x-1">
              <button
                type="button"
                title="Đính kèm file"
                onClick={() => setReplyText(prev => prev + (prev ? '\n' : '') + '[📎 File_tai_lieu.pdf] ')}
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
  );
};
