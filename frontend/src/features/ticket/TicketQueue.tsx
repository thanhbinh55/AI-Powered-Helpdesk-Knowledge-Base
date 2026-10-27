import React, { useState } from 'react';
import { Search, Clock, AlertCircle, PanelLeftClose } from 'lucide-react';
import { Ticket, TicketStatus } from '../../types';
import { Badge } from '../../components/common/Badge';

interface TicketQueueProps {
  tickets: Ticket[];
  selectedTicketId: string | null;
  onSelectTicket: (ticket: Ticket) => void;
  title?: string;
  isCollapsed?: boolean;
  onToggleCollapse?: () => void;
}

export const TicketQueue: React.FC<TicketQueueProps> = ({
  tickets,
  selectedTicketId,
  onSelectTicket,
  title = 'Danh sách Ticket',
  isCollapsed = false,
  onToggleCollapse,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [filterStatus, setFilterStatus] = useState<TicketStatus | 'ALL'>('ALL');

  const filteredTickets = tickets.filter(ticket => {
    const matchesSearch =
      ticket.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      ticket.ticketNumber.toLowerCase().includes(searchQuery.toLowerCase()) ||
      ticket.customer.name.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesStatus = filterStatus === 'ALL' || ticket.status === filterStatus;

    return matchesSearch && matchesStatus;
  });

  // Khi thu gọn: Ẩn hoàn toàn để tối đa hóa không gian đọc ticket & chat (chuẩn Linear/Notion/Zendesk)
  // Cơ chế mở lại được tích hợp trực tiếp tại:
  // 1. Nút "Mở hàng đợi" nổi bật tại Header Workspace
  // 2. Nút tab nổi (Floating dock pill) tại mép biên trái
  // 3. Nhấp vào mục Hàng đợi trên Sidebar chính
  if (isCollapsed) {
    return null;
  }

  return (
    <div className="w-80 sm:w-84 bg-white border-r border-slate-200 flex flex-col h-[calc(100vh-3.5rem)] shrink-0 transition-all select-none">
      {/* Header & Search */}
      <div className="p-3 border-b border-slate-200 space-y-2.5">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <h2 className="text-sm font-bold text-slate-900 tracking-tight">{title}</h2>
            <span className="text-[11px] bg-slate-100 text-slate-600 font-semibold px-2 py-0.5 rounded-full">
              {filteredTickets.length}
            </span>
          </div>

          {onToggleCollapse && (
            <button
              onClick={onToggleCollapse}
              title="Thu gọn danh sách để mở rộng không gian làm việc"
              className="p-1.5 text-slate-400 hover:text-slate-700 hover:bg-slate-100 rounded-lg transition"
            >
              <PanelLeftClose className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Search Bar */}
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-2.5 top-2.5" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Tìm số ticket, tiêu đề, tên khách..."
            className="w-full pl-8 pr-3 py-1.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 transition"
          />
        </div>

        {/* Filter Pills */}
        <div className="flex items-center space-x-1 overflow-x-auto pb-0.5 text-xs">
          {(['ALL', 'OPEN', 'IN_PROGRESS', 'RESOLVED'] as const).map((status) => (
            <button
              key={status}
              onClick={() => setFilterStatus(status)}
              className={`px-2 py-1 rounded-md text-[11px] font-medium transition whitespace-nowrap ${
                filterStatus === status
                  ? 'bg-slate-900 text-white font-semibold'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              {status === 'ALL' ? 'Tất cả' : status}
            </button>
          ))}
        </div>
      </div>

      {/* Ticket List */}
      <div className="flex-1 overflow-y-auto p-2 space-y-1.5">
        {filteredTickets.length === 0 ? (
          <div className="p-8 text-center text-slate-400 space-y-2">
            <AlertCircle className="w-8 h-8 mx-auto text-slate-300" />
            <p className="text-xs font-medium">Không tìm thấy ticket phù hợp</p>
          </div>
        ) : (
          filteredTickets.map((ticket) => {
            const isSelected = selectedTicketId === ticket.id;
            return (
              <div
                key={ticket.id}
                onClick={() => onSelectTicket(ticket)}
                className={`p-3 cursor-pointer transition rounded-xl text-left ${
                  isSelected
                    ? 'bg-blue-50/90 border border-blue-200/90 shadow-2xs'
                    : 'bg-white hover:bg-slate-50 border border-transparent hover:border-slate-200/60'
                }`}
              >
                {/* Top line: Number, Badges */}
                <div className="flex items-center justify-between mb-1.5">
                  <div className="flex items-center space-x-1.5">
                    <span className="text-[11px] font-bold text-slate-500">#{ticket.ticketNumber}</span>
                    <Badge variant="status" value={ticket.status} />
                  </div>
                  <Badge variant="priority" value={ticket.priority} />
                </div>

                {/* Title */}
                <h3 className={`text-xs mb-1 line-clamp-1 ${
                  isSelected ? 'text-helpdesk-900 font-bold' : 'text-slate-800 font-semibold'
                }`}>
                  {ticket.title}
                </h3>

                {/* Description Snippet */}
                <p className="text-[11px] text-slate-500 line-clamp-2 mb-2 leading-relaxed">
                  {ticket.description}
                </p>

                {/* Footer: Customer Info & SLA Timer */}
                <div className="flex items-center justify-between text-[10px] text-slate-400">
                  <div className="flex items-center space-x-1.5">
                    <span className="font-medium text-slate-600 truncate max-w-[100px]">{ticket.customer.name}</span>
                    <span>•</span>
                    <span className="truncate max-w-[80px]">{ticket.customer.organization || 'Khách'}</span>
                  </div>

                  <div className="flex items-center space-x-1 text-amber-700 bg-amber-50 px-1.5 py-0.5 rounded font-medium">
                    <Clock className="w-2.5 h-2.5" />
                    <span>SLA: 4h</span>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
