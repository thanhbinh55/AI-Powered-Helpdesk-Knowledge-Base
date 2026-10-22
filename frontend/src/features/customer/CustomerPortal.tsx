import { useState } from 'react';
import { 
  Plus, 
  Send, 
  Sparkles, 
  BookOpen, 
  CheckCircle, 
} from 'lucide-react';
import { Ticket, Message } from '../../types';
import { Badge } from '../../components/common/Badge';

interface CustomerPortalProps {
  tickets: Ticket[];
  messages: Message[];
  onCreateTicket: (title: string, description: string, category: string) => void;
  onSendMessage: (ticketId: string, content: string) => void;
  onCloseTicket: (ticketId: string) => void;
}

export const CustomerPortal: React.FC<CustomerPortalProps> = ({
  tickets,
  messages,
  onCreateTicket,
  onSendMessage,
  onCloseTicket,
}) => {
  const [selectedTicketId, setSelectedTicketId] = useState<string>(tickets[0]?.id || '');
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [newTitle, setNewTitle] = useState('');
  const [newDesc, setNewDesc] = useState('');
  const [newCategory, setNewCategory] = useState('Identity & Access');
  const [replyText, setReplyText] = useState('');

  const selectedTicket = tickets.find(t => t.id === selectedTicketId) || tickets[0];
  const ticketMessages = messages.filter(m => m.ticketId === selectedTicket?.id && !m.isInternal); // Customer NEVER sees internal notes!

  // Instant AI recommendation when customer types title
  const hasAISuggestion = newTitle.toLowerCase().includes('kích hoạt') || newTitle.toLowerCase().includes('tài khoản');

  const handleCreateSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim() || !newDesc.trim()) return;
    onCreateTicket(newTitle, newDesc, newCategory);
    setShowCreateModal(false);
    setNewTitle('');
    setNewDesc('');
  };

  const handleReplySubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!replyText.trim() || !selectedTicket) return;
    onSendMessage(selectedTicket.id, replyText);
    setReplyText('');
  };

  return (
    <div className="flex-1 flex overflow-hidden h-[calc(100vh-3.5rem)] bg-white text-left">
      {/* Left List: My Tickets (Màn 3 SRS) */}
      <div className="w-80 border-r border-slate-200 flex flex-col shrink-0">
        <div className="p-4 border-b border-slate-200 flex items-center justify-between">
          <div>
            <h2 className="text-sm font-bold text-slate-900">Yêu cầu của tôi</h2>
            <p className="text-[11px] text-slate-400">Customer Support Portal</p>
          </div>
          <button
            onClick={() => setShowCreateModal(true)}
            className="inline-flex items-center space-x-1 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-semibold shadow-xs transition"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>Tạo mới</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto divide-y divide-slate-100">
          {tickets.map((ticket) => {
            const isSelected = ticket.id === selectedTicket?.id;
            return (
              <div
                key={ticket.id}
                onClick={() => setSelectedTicketId(ticket.id)}
                className={`p-3.5 cursor-pointer transition ${
                  isSelected ? 'bg-emerald-50/60 border-l-4 border-emerald-600' : 'hover:bg-slate-50'
                }`}
              >
                <div className="flex items-center justify-between mb-1">
                  <span className="text-[11px] font-bold text-slate-400">#{ticket.ticketNumber}</span>
                  <Badge variant="status" value={ticket.status} />
                </div>
                <h3 className={`text-xs font-semibold line-clamp-1 ${
                  isSelected ? 'text-emerald-950 font-bold' : 'text-slate-800'
                }`}>
                  {ticket.title}
                </h3>
                <p className="text-[11px] text-slate-500 line-clamp-2 mt-1">
                  {ticket.description}
                </p>
                <div className="flex items-center justify-between mt-2 text-[10px] text-slate-400">
                  <span>{ticket.category}</span>
                  <span>{new Date(ticket.createdAt).toLocaleDateString()}</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Right Area: Ticket Detail (Màn 5 SRS) */}
      {selectedTicket ? (
        <div className="flex-1 flex flex-col overflow-hidden bg-slate-50/40">
          {/* Header */}
          <div className="p-4 bg-white border-b border-slate-200 flex items-center justify-between">
            <div>
              <div className="flex items-center space-x-2">
                <span className="text-xs font-bold text-slate-400">#{selectedTicket.ticketNumber}</span>
                <Badge variant="status" value={selectedTicket.status} />
                <span className="text-xs text-slate-400">•</span>
                <span className="text-xs font-medium text-slate-600">{selectedTicket.category}</span>
              </div>
              <h1 className="text-base font-bold text-slate-900 mt-0.5">{selectedTicket.title}</h1>
            </div>

            {selectedTicket.status === 'RESOLVED' && (
              <button
                onClick={() => onCloseTicket(selectedTicket.id)}
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-900 text-white rounded-lg text-xs font-semibold shadow-xs transition"
              >
                <CheckCircle className="w-3.5 h-3.5 text-emerald-400" />
                <span>Xác nhận đóng Ticket (Close)</span>
              </button>
            )}
          </div>

          {/* Messages Stream (Public only) */}
          <div className="flex-1 overflow-y-auto p-5 space-y-4">
            {ticketMessages.map((msg) => {
              const isMe = msg.sender.role === 'CUSTOMER';
              return (
                <div
                  key={msg.id}
                  className={`flex space-x-3 max-w-2xl ${isMe ? 'ml-auto flex-row-reverse space-x-reverse' : ''}`}
                >
                  <img
                    src={msg.sender.avatar || 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'}
                    alt={msg.sender.name}
                    className="w-8 h-8 rounded-full ring-2 ring-white shadow-xs shrink-0"
                  />
                  <div className="space-y-1">
                    <div className={`flex items-center space-x-2 text-[11px] ${isMe ? 'justify-end' : ''}`}>
                      <span className="font-semibold text-slate-800">{msg.sender.name}</span>
                      <span className="text-slate-400">
                        {new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </span>
                    </div>

                    <div
                      className={`p-3.5 rounded-2xl text-xs leading-relaxed shadow-xs whitespace-pre-wrap ${
                        isMe
                          ? 'bg-emerald-600 text-white rounded-tr-sm'
                          : 'bg-white text-slate-800 border border-slate-200/80 rounded-tl-sm'
                      }`}
                    >
                      {msg.content}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Reply Box */}
          <div className="p-4 bg-white border-t border-slate-200">
            <form onSubmit={handleReplySubmit} className="flex items-center space-x-2">
              <input
                type="text"
                value={replyText}
                onChange={(e) => setReplyText(e.target.value)}
                placeholder="Nhập phản hồi của bạn..."
                className="flex-1 p-2.5 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500"
              />
              <button
                type="submit"
                disabled={!replyText.trim()}
                className="px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-100 disabled:text-slate-400 text-white rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Gửi</span>
              </button>
            </form>
          </div>
        </div>
      ) : (
        <div className="flex-1 flex items-center justify-center text-slate-400 text-xs">
          Chọn một ticket để xem chi tiết
        </div>
      )}

      {/* New Ticket Modal with Instant AI Knowledge Suggestion (Màn 4 SRS) */}
      {showCreateModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-lg w-full p-5 space-y-4 shadow-xl border border-slate-200">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-bold text-sm text-slate-900">Gửi yêu cầu hỗ trợ mới (New Ticket)</h3>
              <button
                onClick={() => setShowCreateModal(false)}
                className="text-slate-400 hover:text-slate-600 text-xs px-2 py-1 rounded"
              >
                ✕ Đóng
              </button>
            </div>

            <form onSubmit={handleCreateSubmit} className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-slate-700 mb-1">Tiêu đề yêu cầu</label>
                <input
                  type="text"
                  required
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  placeholder="Ví dụ: Không thể kích hoạt tài khoản sinh viên..."
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500"
                />
              </div>

              {/* Instant AI RAG Suggestion Box (SRS requirement FR-AI-01) */}
              {hasAISuggestion && (
                <div className="p-3 bg-gradient-to-r from-purple-50 to-indigo-50 border border-purple-200 rounded-xl space-y-1.5">
                  <div className="flex items-center space-x-1.5 text-purple-900 font-bold text-[11px]">
                    <Sparkles className="w-3.5 h-3.5 text-purple-600" />
                    <span>Bài viết có thể giải đáp ngay vấn đề của bạn:</span>
                  </div>
                  <div className="bg-white p-2 rounded-lg border border-purple-100 flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      <BookOpen className="w-3.5 h-3.5 text-purple-600" />
                      <span className="font-medium text-slate-800">Hướng dẫn khắc phục lỗi xác thực tài khoản & JWT Expired</span>
                    </div>
                    <span className="text-[10px] text-purple-700 font-bold cursor-pointer hover:underline">
                      Xem ngay
                    </span>
                  </div>
                </div>
              )}

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Phân loại danh mục</label>
                <select
                  value={newCategory}
                  onChange={(e) => setNewCategory(e.target.value)}
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500"
                >
                  <option value="Identity & Access">Identity & Access (Tài khoản, Mật khẩu)</option>
                  <option value="Chính sách & Học vụ">Chính sách & Học vụ (Bảo lưu, Học phí)</option>
                  <option value="Kỹ thuật Portal">Kỹ thuật Portal (Lỗi nộp bài, Upload)</option>
                  <option value="Cơ sở hạ tầng & VPN">Cơ sở hạ tầng & VPN</option>
                </select>
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Mô tả chi tiết</label>
                <textarea
                  required
                  rows={4}
                  value={newDesc}
                  onChange={(e) => setNewDesc(e.target.value)}
                  placeholder="Mô tả cụ thể sự cố, thông báo lỗi (nếu có) để nhân viên hỗ trợ nhanh nhất..."
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 resize-none"
                />
              </div>

              <div className="flex space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowCreateModal(false)}
                  className="w-1/2 py-2 border border-slate-200 hover:bg-slate-50 text-slate-600 rounded-lg font-semibold"
                >
                  Hủy
                </button>
                <button
                  type="submit"
                  className="w-1/2 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-semibold shadow-xs"
                >
                  Gửi yêu cầu
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
