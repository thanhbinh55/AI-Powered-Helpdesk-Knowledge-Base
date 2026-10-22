import { useState } from 'react';
import { 
  Send, 
  Lock, 
  Sparkles, 
  CheckCircle, 
  UserCheck, 
  ExternalLink,
  ChevronRight,
  ShieldCheck,
  Building,
  Mail,
  Loader2
} from 'lucide-react';
import { Ticket, Message, User, AISuggestion, Citation } from '../../types';
import { Badge } from '../../components/common/Badge';

interface TicketWorkspaceProps {
  ticket: Ticket;
  messages: Message[];
  currentUser: User;
  onSendMessage: (ticketId: string, content: string, isInternal: boolean) => void;
  onClaimTicket: (ticketId: string) => void;
  onResolveTicket: (ticketId: string) => void;
  aiSuggestion?: AISuggestion | null;
}

export const TicketWorkspace: React.FC<TicketWorkspaceProps> = ({
  ticket,
  messages,
  currentUser,
  onSendMessage,
  onClaimTicket,
  onResolveTicket,
  aiSuggestion,
}) => {
  const [replyType, setReplyType] = useState<'PUBLIC' | 'INTERNAL'>('PUBLIC');
  const [replyText, setReplyText] = useState('');
  const [isGeneratingAI, setIsGeneratingAI] = useState(false);
  const [showRightPanel, setShowRightPanel] = useState(true);
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null);

  const handleSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!replyText.trim()) return;
    onSendMessage(ticket.id, replyText, replyType === 'INTERNAL');
    setReplyText('');
  };

  const handleGenerateAI = () => {
    setIsGeneratingAI(true);
    setTimeout(() => {
      setIsGeneratingAI(false);
    }, 800);
  };

  const handleApplyAISuggestion = () => {
    if (aiSuggestion) {
      setReplyText(aiSuggestion.draftReply);
      setReplyType('PUBLIC');
    }
  };

  return (
    <div className="flex-1 flex overflow-hidden h-[calc(100vh-3.5rem)] bg-[#F5F7F9]">
      {/* Central Column: Ticket Thread & Composer (Column 3) */}
      <div className="flex-1 flex flex-col bg-white border-r border-slate-200 overflow-hidden">
        {/* Workspace Header */}
        <div className="px-5 py-3 border-b border-slate-200 flex items-center justify-between bg-white shrink-0">
          <div className="space-y-1">
            <div className="flex items-center space-x-2">
              <span className="text-xs font-bold text-slate-400">#{ticket.ticketNumber}</span>
              <Badge variant="status" value={ticket.status} />
              <Badge variant="priority" value={ticket.priority} />
              <span className="text-xs text-slate-400">•</span>
              <span className="text-xs font-medium text-slate-600">{ticket.category}</span>
            </div>
            <h1 className="text-base font-bold text-slate-900 tracking-tight">{ticket.title}</h1>
          </div>

          {/* Quick Actions */}
          <div className="flex items-center space-x-2">
            {!ticket.assignee ? (
              <button
                onClick={() => onClaimTicket(ticket.id)}
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 bg-helpdesk-600 hover:bg-helpdesk-700 text-white text-xs font-semibold rounded-lg shadow-sm transition"
              >
                <UserCheck className="w-3.5 h-3.5" />
                <span>Nhận xử lý (Claim)</span>
              </button>
            ) : (
              <div className="flex items-center space-x-1.5 text-xs text-slate-600 bg-slate-50 border border-slate-200 px-2.5 py-1.5 rounded-lg">
                <span className="text-slate-400">Phụ trách:</span>
                <span className="font-semibold text-slate-800">{ticket.assignee.name}</span>
              </div>
            )}

            {ticket.status !== 'RESOLVED' && ticket.status !== 'CLOSED' && (
              <button
                onClick={() => onResolveTicket(ticket.id)}
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold rounded-lg shadow-sm transition"
              >
                <CheckCircle className="w-3.5 h-3.5" />
                <span>Hoàn tất (Resolve)</span>
              </button>
            )}

            <button
              onClick={() => setShowRightPanel(!showRightPanel)}
              className={`p-1.5 rounded-lg border text-xs transition ${
                showRightPanel ? 'bg-slate-100 text-slate-700 border-slate-300' : 'text-slate-400 border-slate-200'
              }`}
              title="Ẩn/Hiện Panel trợ lý AI và thông tin"
            >
              <ChevronRight className={`w-4 h-4 transition-transform ${showRightPanel ? '' : 'rotate-180'}`} />
            </button>
          </div>
        </div>

        {/* Message Thread (Timeline) */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4 bg-slate-50/50">
          {messages.map((msg) => {
            if (msg.isInternal) {
              // INTERNAL NOTE: Spec Requirement - Yellow/Amber note box with Lock
              return (
                <div
                  key={msg.id}
                  className="bg-internal-bg border border-internal-border rounded-xl p-4 space-y-2 shadow-xs transition"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <div className="p-1 bg-amber-200 text-amber-800 rounded">
                        <Lock className="w-3 h-3" />
                      </div>
                      <span className="text-xs font-bold text-internal-text">
                        Ghi chú nội bộ (Chỉ Agent & Admin nhìn thấy)
                      </span>
                      <span className="text-[11px] text-amber-700/80">• {msg.sender.name}</span>
                    </div>
                    <span className="text-[10px] text-amber-700/80">
                      {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </span>
                  </div>
                  <p className="text-xs text-slate-800 leading-relaxed font-normal whitespace-pre-wrap">
                    {msg.content}
                  </p>
                </div>
              );
            }

            // PUBLIC MESSAGE (Customer or Agent Reply)
            const isCustomer = msg.sender.role === 'CUSTOMER';
            return (
              <div
                key={msg.id}
                className={`flex space-x-3 max-w-3xl ${isCustomer ? '' : 'ml-auto flex-row-reverse space-x-reverse'}`}
              >
                <img
                  src={msg.sender.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80'}
                  alt={msg.sender.name}
                  className="w-8 h-8 rounded-full ring-2 ring-white shadow-xs shrink-0"
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
                    className={`p-3.5 rounded-2xl text-xs leading-relaxed shadow-xs whitespace-pre-wrap ${
                      isCustomer
                        ? 'bg-white text-slate-800 border border-slate-200/80 rounded-tl-sm'
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

        {/* Reply Composer */}
        <div className="border-t border-slate-200 bg-white p-4">
          <form onSubmit={handleSend} className="space-y-3">
            {/* Tabs & AI Trigger Bar */}
            <div className="flex items-center justify-between">
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
                  Trả lời công khai (Khách thấy)
                </button>
                <button
                  type="button"
                  onClick={() => setReplyType('INTERNAL')}
                  className={`px-3 py-1 rounded-md font-medium transition flex items-center space-x-1 ${
                    replyType === 'INTERNAL'
                      ? 'bg-amber-100 text-amber-900 shadow-xs font-semibold'
                      : 'text-slate-600 hover:text-slate-900'
                  }`}
                >
                  <Lock className="w-3 h-3 text-amber-700" />
                  <span>Ghi chú nội bộ</span>
                </button>
              </div>

              {/* Instant AI Suggestion Action */}
              <button
                type="button"
                onClick={handleGenerateAI}
                disabled={isGeneratingAI}
                className="inline-flex items-center space-x-1.5 px-3 py-1 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white text-xs font-medium rounded-lg shadow-xs transition active:scale-95"
              >
                {isGeneratingAI ? (
                  <>
                    <Loader2 className="w-3.5 h-3.5 animate-spin" />
                    <span>RAG Đang sinh câu trả lời...</span>
                  </>
                ) : (
                  <>
                    <Sparkles className="w-3.5 h-3.5" />
                    <span>✨ AI Gợi ý phản hồi</span>
                  </>
                )}
              </button>
            </div>

            {/* Input Textarea with contextual coloring */}
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
                className={`w-full p-3 text-xs rounded-xl border focus:outline-none focus:ring-2 transition resize-none ${
                  replyType === 'INTERNAL'
                    ? 'bg-amber-50/60 border-amber-300 focus:ring-amber-400/30 text-amber-950 placeholder-amber-700/50'
                    : 'bg-white border-slate-200 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 text-slate-800'
                }`}
              />
            </div>

            {/* Bottom Actions */}
            <div className="flex items-center justify-between text-xs">
              <p className="text-[11px] text-slate-400">
                Nhấn <kbd className="px-1 py-0.5 bg-slate-100 border border-slate-200 rounded text-[10px]">Ctrl + Enter</kbd> để gửi
              </p>

              <button
                type="submit"
                disabled={!replyText.trim()}
                className={`inline-flex items-center space-x-1.5 px-4 py-2 text-xs font-semibold rounded-lg shadow-sm transition ${
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
      </div>

      {/* Right Column: AI Copilot & Customer Meta (Column 4) */}
      {showRightPanel && (
        <div className="w-80 lg:w-96 bg-white border-l border-slate-200 overflow-y-auto p-4 space-y-5 shrink-0 text-left">
          {/* AI Copilot Card */}
          <div className="bg-gradient-to-b from-purple-50/70 to-indigo-50/30 border border-purple-200 rounded-xl p-4 space-y-3">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-1.5 text-purple-900 font-bold text-xs">
                <Sparkles className="w-4 h-4 text-purple-600" />
                <span>Trợ lý AI Copilot</span>
              </div>
              <span className="text-[10px] bg-purple-100 text-purple-700 font-bold px-2 py-0.5 rounded-full">
                Độ chính xác: 95%
              </span>
            </div>

            {/* Mandatory UX Warning from SRS Section 13.3 */}
            <div className="bg-purple-100/70 border border-purple-200/80 rounded-lg p-2 flex items-center space-x-2 text-[11px] text-purple-900 font-medium">
              <ShieldCheck className="w-4 h-4 text-purple-600 shrink-0" />
              <span>Gợi ý tạo bởi AI — hãy duyệt trước khi gửi</span>
            </div>

            {/* Suggested Draft Content */}
            {aiSuggestion ? (
              <div className="space-y-3">
                <div className="bg-white border border-purple-100 rounded-lg p-3 text-xs text-slate-700 space-y-2 max-h-48 overflow-y-auto leading-relaxed whitespace-pre-wrap shadow-2xs">
                  {aiSuggestion.draftReply}
                </div>

                <button
                  onClick={handleApplyAISuggestion}
                  className="w-full py-1.5 bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold rounded-lg shadow-sm transition flex items-center justify-center space-x-1.5"
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Áp dụng vào khung trả lời (Apply Draft)</span>
                </button>

                {/* Citations / Sources */}
                <div className="space-y-1.5 pt-1">
                  <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">
                    Nguồn trích dẫn (Citations)
                  </span>
                  {aiSuggestion.citations.map((cite, idx) => (
                    <div
                      key={idx}
                      onClick={() => setSelectedCitation(cite)}
                      className="p-2 bg-white border border-slate-200 hover:border-purple-300 rounded-lg cursor-pointer transition text-left space-y-1"
                    >
                      <div className="flex items-center justify-between text-[11px]">
                        <span className="font-semibold text-purple-900 truncate max-w-[200px]">
                          {cite.documentTitle}
                        </span>
                        <span className="text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.2 rounded text-[10px]">
                          {Math.round(cite.score * 100)}% match
                        </span>
                      </div>
                      <p className="text-[10px] text-slate-500 line-clamp-2 italic">
                        "{cite.chunkSnippet}"
                      </p>
                      <div className="flex items-center space-x-1 text-[9px] text-purple-600 font-medium">
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
                <p className="text-xs">Bấm nút "AI Gợi ý" để lấy câu trả lời</p>
              </div>
            )}
          </div>

          {/* Customer Metadata Card */}
          <div className="border border-slate-200 rounded-xl p-4 space-y-3 bg-white">
            <h3 className="text-xs font-bold text-slate-800 uppercase tracking-wider">Thông tin khách hàng</h3>
            <div className="flex items-center space-x-3">
              <img
                src={ticket.customer.avatar || 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'}
                alt={ticket.customer.name}
                className="w-10 h-10 rounded-full object-cover ring-1 ring-slate-200"
              />
              <div>
                <p className="text-xs font-bold text-slate-900">{ticket.customer.name}</p>
                <div className="flex items-center space-x-1 text-[11px] text-slate-500">
                  <Mail className="w-3 h-3" />
                  <span>{ticket.customer.email}</span>
                </div>
              </div>
            </div>

            <div className="pt-2 border-t border-slate-100 space-y-1.5 text-xs">
              <div className="flex items-center justify-between text-slate-600">
                <span className="text-slate-400 flex items-center gap-1">
                  <Building className="w-3 h-3" /> Đơn vị:
                </span>
                <span className="font-semibold text-slate-800">{ticket.customer.organization || 'Khoa CNTT'}</span>
              </div>
              <div className="flex items-center justify-between text-slate-600">
                <span className="text-slate-400">Ngày tạo:</span>
                <span className="font-medium text-slate-700">
                  {new Date(ticket.createdAt).toLocaleDateString()}
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Citation Detail Modal */}
      {selectedCitation && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-lg w-full p-5 space-y-4 shadow-xl border border-slate-200 animate-in fade-in zoom-in-95 duration-150">
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
                <div className="p-3 bg-purple-50/70 border border-purple-200/80 rounded-lg text-slate-800 font-serif leading-relaxed italic">
                  "{selectedCitation.chunkSnippet}"
                </div>
              </div>
            </div>

            <button
              onClick={() => setSelectedCitation(null)}
              className="w-full py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-xs font-semibold"
            >
              Đóng xem trước
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
