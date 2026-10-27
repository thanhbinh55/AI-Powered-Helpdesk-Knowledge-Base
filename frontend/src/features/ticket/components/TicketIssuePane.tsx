import React from 'react';
import { 
  FileText, 
  Paperclip, 
  Clock, 
  Sparkles, 
  ExternalLink, 
  UserCheck, 
  CheckCircle, 
  Mail, 
  Building, 
  Inbox,
  PanelLeftOpen
} from 'lucide-react';
import { Ticket, AISuggestion, Citation } from '../../../types';
import { Badge } from '../../../components/common/Badge';

interface TicketIssuePaneProps {
  ticket: Ticket;
  aiSuggestion?: AISuggestion | null;
  isQueueCollapsed?: boolean;
  onToggleQueue?: () => void;
  queueTicketCount?: number;
  onClaimTicket: (ticketId: string) => void;
  onResolveTicket: (ticketId: string) => void;
  onViewCitation: (citation: Citation) => void;
}

export const TicketIssuePane: React.FC<TicketIssuePaneProps> = ({
  ticket,
  aiSuggestion,
  isQueueCollapsed,
  onToggleQueue,
  queueTicketCount,
  onClaimTicket,
  onResolveTicket,
  onViewCitation,
}) => {
  return (
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

        {/* Card Chi tiết sự cố & Yêu cầu của khách hàng */}
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

        {/* Card Tài liệu RAG đối chiếu */}
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
                  onClick={() => onViewCitation(cite)}
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

        {/* Card Lịch sử xử lý ticket (Audit Log) */}
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
  );
};
