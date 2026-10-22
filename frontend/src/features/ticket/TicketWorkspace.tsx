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
  Maximize2,
  Minimize2,
  Clock,
  FileText
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
}

export const TicketWorkspace: React.FC<TicketWorkspaceProps> = ({
  ticket,
  messages,
  onSendMessage,
  onClaimTicket,
  onResolveTicket,
  aiSuggestion,
}) => {
  const [replyType, setReplyType] = useState<'PUBLIC' | 'INTERNAL'>('PUBLIC');
  const [replyText, setReplyText] = useState('');
  const [isGeneratingAI, setIsGeneratingAI] = useState(false);
  
  // Floating AI Copilot Widget state (Bottom Right Dock)
  const [isCopilotOpen, setIsCopilotOpen] = useState(false);
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!replyText.trim()) return;
    onSendMessage(ticket.id, replyText, replyType === 'INTERNAL');
    setReplyText('');
  };

  const handleGenerateAI = () => {
    setIsGeneratingAI(true);
    setIsCopilotOpen(true);
    setTimeout(() => {
      setIsGeneratingAI(false);
    }, 600);
  };

  const handleApplyAISuggestion = () => {
    if (aiSuggestion) {
      setReplyText(aiSuggestion.draftReply);
      setReplyType('PUBLIC');
      setIsCopilotOpen(false); // minimize after applying
    }
  };

  return (
    <div className="flex-1 flex flex-col bg-slate-100 overflow-hidden h-[calc(100vh-3.5rem)] relative">
      {/* 1. Header: Rộng rãi, mạch lạc, không bị vỡ layout */}
      <div className="bg-white border-b border-slate-200 px-6 py-3.5 shadow-2xs shrink-0 text-left">
        {/* Top line: Meta & Actions */}
        <div className="flex flex-wrap items-center justify-between gap-2 mb-1.5">
          <div className="flex items-center space-x-2">
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
        <h1 className="text-base sm:text-lg font-bold text-slate-900 tracking-tight leading-snug">
          {ticket.title}
        </h1>

        {/* Customer Information Strip (Tích hợp ngang tinh gọn) */}
        <div className="mt-2.5 pt-2 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-500 gap-y-1">
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <img
                src={ticket.customer.avatar || 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'}
                alt={ticket.customer.name}
                className="w-5 h-5 rounded-full object-cover ring-1 ring-slate-200"
              />
              <span className="font-semibold text-slate-800">{ticket.customer.name}</span>
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

      {/* 2. Message Thread: Rộng rãi, cuộn mượt */}
      <div className="flex-1 overflow-y-auto px-6 lg:px-12 py-5 space-y-4">
        {messages.map((msg) => {
          if (msg.isInternal) {
            // INTERNAL NOTE: Vàng amber nhạt, ổ khóa, cách ly trực quan
            return (
              <div
                key={msg.id}
                className="max-w-3xl mx-auto bg-amber-50/80 border border-amber-200/90 rounded-2xl p-4 space-y-2 shadow-2xs text-left"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <div className="p-1 bg-amber-200 text-amber-800 rounded-md">
                      <Lock className="w-3.5 h-3.5" />
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

          // PUBLIC MESSAGES (Customer vs Agent)
          const isCustomer = msg.sender.role === 'CUSTOMER';
          return (
            <div
              key={msg.id}
              className={`flex space-x-3 max-w-3xl ${isCustomer ? 'mr-auto' : 'ml-auto flex-row-reverse space-x-reverse'}`}
            >
              <img
                src={msg.sender.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80'}
                alt={msg.sender.name}
                className="w-8 h-8 rounded-full ring-2 ring-white shadow-xs shrink-0 object-cover"
              />
              <div className="space-y-1 text-left">
                <div className={`flex items-center space-x-2 text-[11px] ${isCustomer ? '' : 'justify-end'}`}>
                  <span className="font-semibold text-slate-800">{msg.sender.name}</span>
                  <Badge variant="role" value={msg.sender.role} />
                  <span className="text-slate-400">
                    {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>

                <div
                  className={`p-3.5 rounded-2xl text-xs leading-relaxed shadow-xs whitespace-pre-wrap max-w-xl ${
                    isCustomer
                      ? 'bg-white text-slate-800 border border-slate-200/90 rounded-tl-sm'
                      : 'bg-helpdesk-600 text-white rounded-tr-sm'
                  }`}
                >
                  {msg.content}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* 3. Message Composer: Thiết kế thông thoáng, chuyên nghiệp */}
      <div className="bg-white border-t border-slate-200 px-6 py-4 shrink-0 shadow-lg">
        <form onSubmit={handleSend} className="max-w-4xl mx-auto space-y-3">
          {/* Tabs switch: Public reply vs Internal Note */}
          <div className="flex items-center justify-between">
            <div className="flex space-x-1 bg-slate-100 p-0.5 rounded-lg border border-slate-200 text-xs">
              <button
                type="button"
                onClick={() => setReplyType('PUBLIC')}
                className={`px-3 py-1.5 rounded-md font-medium transition ${
                  replyType === 'PUBLIC'
                    ? 'bg-white text-slate-900 shadow-xs font-semibold'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                Trả lời công khai (Khách thấy)
              </button>
              <button
                type="button"
                onClick={() => setReplyType('INTERNAL')}
                className={`px-3 py-1.5 rounded-md font-medium transition flex items-center space-x-1.5 ${
                  replyType === 'INTERNAL'
                    ? 'bg-amber-100 text-amber-900 shadow-xs font-semibold'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                <Lock className="w-3.5 h-3.5 text-amber-700" />
                <span>Ghi chú nội bộ</span>
              </button>
            </div>

            {/* Quick Button to open Floating AI Copilot */}
            <button
              type="button"
              onClick={handleGenerateAI}
              className="inline-flex items-center space-x-1.5 px-3 py-1.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white text-xs font-semibold rounded-lg shadow-xs transition active:scale-95"
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>✨ Mở Trợ lý AI Copilot</span>
            </button>
          </div>

          {/* Text Area */}
          <div className="relative">
            <textarea
              value={replyText}
              onChange={(e) => setReplyText(e.target.value)}
              placeholder={
                replyType === 'PUBLIC'
                  ? 'Nhập nội dung phản hồi gửi đến khách hàng...'
                  : 'Nhập ghi chú nội bộ (chỉ nhân viên hỗ trợ và quản trị viên xem được)...'
              }
              rows={3}
              className={`w-full p-3.5 text-xs rounded-xl border focus:outline-none focus:ring-2 transition resize-none ${
                replyType === 'INTERNAL'
                  ? 'bg-amber-50/60 border-amber-300 focus:ring-amber-400/30 text-amber-950 placeholder-amber-700/50'
                  : 'bg-slate-50 border-slate-200 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 text-slate-800'
              }`}
            />
          </div>

          {/* Bottom Toolbar */}
          <div className="flex items-center justify-between text-xs pt-0.5">
            <span className="text-[11px] text-slate-400">
              Nhấn <kbd className="px-1.5 py-0.5 bg-slate-100 border border-slate-200 rounded text-[10px] font-mono">Ctrl + Enter</kbd> để gửi
            </span>

            <button
              type="submit"
              disabled={!replyText.trim()}
              className={`inline-flex items-center space-x-1.5 px-4 py-2 text-xs font-semibold rounded-xl shadow-xs transition ${
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

      {/* 4. FLOATING AI COPILOT DOCK (Góc Dưới Bên Phải) */}
      {/* Floating Trigger Button (Always visible when minimized) */}
      {!isCopilotOpen && (
        <button
          onClick={() => setIsCopilotOpen(true)}
          className="fixed bottom-6 right-6 z-40 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white px-4 py-2.5 rounded-full shadow-xl flex items-center space-x-2 text-xs font-bold transition-all hover:scale-105 active:scale-95 group"
        >
          <div className="p-1 bg-white/20 rounded-full">
            <Sparkles className="w-4 h-4 text-white animate-spin-slow" />
          </div>
          <span>AI Copilot</span>
          <span className="bg-white/20 text-white text-[10px] px-1.5 py-0.2 rounded-full">1 sẵn sàng</span>
        </button>
      )}

      {/* Floating Copilot Modal/Drawer (Góc dưới phải khi mở ra) */}
      {isCopilotOpen && (
        <div className="fixed bottom-6 right-6 z-40 w-96 max-w-[90vw] bg-white rounded-2xl shadow-2xl border border-purple-200 flex flex-col overflow-hidden animate-in fade-in slide-in-from-bottom-5 duration-200 text-left">
          {/* Header */}
          <div className="bg-gradient-to-r from-purple-700 to-indigo-700 px-4 py-3 text-white flex items-center justify-between">
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
              title="Thu nhỏ ô trợ lý"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Body */}
          <div className="p-4 space-y-3 max-h-[70vh] overflow-y-auto bg-slate-50/50">
            {/* Warning tag */}
            <div className="bg-purple-100/70 border border-purple-200 rounded-lg p-2 flex items-center space-x-2 text-[11px] text-purple-900 font-medium">
              <ShieldCheck className="w-4 h-4 text-purple-600 shrink-0" />
              <span>Gợi ý tạo bởi AI — hãy duyệt trước khi gửi</span>
            </div>

            {/* AI Draft Text */}
            {isGeneratingAI ? (
              <div className="py-8 text-center space-y-2 text-slate-500">
                <Loader2 className="w-6 h-6 animate-spin mx-auto text-purple-600" />
                <p className="text-xs font-medium">RAG pgvector đang sinh câu trả lời...</p>
              </div>
            ) : aiSuggestion ? (
              <div className="space-y-3">
                <div className="bg-white border border-purple-100 rounded-xl p-3 text-xs text-slate-700 leading-relaxed whitespace-pre-wrap max-h-48 overflow-y-auto shadow-2xs">
                  {aiSuggestion.draftReply}
                </div>

                <button
                  onClick={handleApplyAISuggestion}
                  className="w-full py-2 bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold rounded-xl shadow-xs transition flex items-center justify-center space-x-1.5"
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
