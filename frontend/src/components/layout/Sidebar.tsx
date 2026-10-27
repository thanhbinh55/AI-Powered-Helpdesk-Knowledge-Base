import React from 'react';
import { 
  Inbox, 
  CheckCircle2, 
  BookOpen, 
  Bot, 
  Users, 
  Settings,
  Sparkles,
  HelpCircle
} from 'lucide-react';
import { UserRole } from '../../types';

export type NavTab = 'QUEUE' | 'MY_TICKETS' | 'KNOWLEDGE_BASE' | 'AI_INSIGHTS' | 'ADMIN_USERS' | 'SETTINGS';

interface SidebarProps {
  currentTab: NavTab;
  onSelectTab: (tab: NavTab) => void;
  role: UserRole;
  openTicketCount: number;
  assignedTicketCount: number;
  isOpen: boolean;
}

export const Sidebar: React.FC<SidebarProps> = ({
  currentTab,
  onSelectTab,
  role,
  openTicketCount,
  assignedTicketCount,
  isOpen
}) => {
  return (
    <aside 
      className={`bg-white border-r border-slate-200 flex flex-col justify-between select-none h-[calc(100vh-3.5rem)] shrink-0 transition-all duration-200 ease-in-out z-20 ${
        isOpen ? 'w-56' : 'w-16'
      }`}
    >
      <div className="p-2 space-y-4">
        {/* Workspace Title (Only visible when expanded) */}
        {isOpen && (
          <div className="px-3 pt-2">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
              {role === 'ADMIN' ? 'Admin Portal' : 'Agent Workspace'}
            </span>
          </div>
        )}

        {/* Navigation Links */}
        <nav className="space-y-1">
          {/* Module C: Tickets */}
          {role !== 'CUSTOMER' && (
            <>
              <button
                onClick={() => onSelectTab('QUEUE')}
                title="Hàng đợi OPEN"
                className={`w-full flex items-center ${isOpen ? 'justify-between px-3' : 'justify-center px-2'} py-2.5 rounded-xl text-xs font-medium transition ${
                  currentTab === 'QUEUE'
                    ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold shadow-2xs'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <div className="flex items-center space-x-2.5">
                  <div className="relative">
                    <Inbox className={`w-4 h-4 ${currentTab === 'QUEUE' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
                    {!isOpen && openTicketCount > 0 && (
                      <span className="absolute -top-1 -right-1 w-2 h-2 bg-helpdesk-500 rounded-full ring-2 ring-white"></span>
                    )}
                  </div>
                  {isOpen && <span>Hàng đợi OPEN</span>}
                </div>
                {isOpen && openTicketCount > 0 && (
                  <span className="bg-helpdesk-100 text-helpdesk-700 text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                    {openTicketCount}
                  </span>
                )}
              </button>

              <button
                onClick={() => onSelectTab('MY_TICKETS')}
                title="Đang xử lý"
                className={`w-full flex items-center ${isOpen ? 'justify-between px-3' : 'justify-center px-2'} py-2.5 rounded-xl text-xs font-medium transition ${
                  currentTab === 'MY_TICKETS'
                    ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold shadow-2xs'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <div className="flex items-center space-x-2.5">
                  <div className="relative">
                    <CheckCircle2 className={`w-4 h-4 ${currentTab === 'MY_TICKETS' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
                    {!isOpen && assignedTicketCount > 0 && (
                      <span className="absolute -top-1 -right-1 w-2 h-2 bg-emerald-500 rounded-full ring-2 ring-white"></span>
                    )}
                  </div>
                  {isOpen && <span>Đang xử lý</span>}
                </div>
                {isOpen && assignedTicketCount > 0 && (
                  <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                    {assignedTicketCount}
                  </span>
                )}
              </button>
            </>
          )}

          {/* Module B: Knowledge Base */}
          <div className="pt-2">
            {isOpen && (
              <span className="px-3 text-[9px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                Tri thức
              </span>
            )}
            <button
              onClick={() => onSelectTab('KNOWLEDGE_BASE')}
              title="Kho tài liệu RAG"
              className={`w-full flex items-center ${isOpen ? 'space-x-2.5 px-3' : 'justify-center px-2'} py-2.5 rounded-xl text-xs font-medium transition ${
                currentTab === 'KNOWLEDGE_BASE'
                  ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <BookOpen className={`w-4 h-4 ${currentTab === 'KNOWLEDGE_BASE' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
              {isOpen && <span>Kho tài liệu RAG</span>}
            </button>
          </div>

          {/* Module A: AI Assistance */}
          <div className="pt-2">
            {isOpen && (
              <span className="px-3 text-[9px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                Phân tích & AI
              </span>
            )}
            <button
              onClick={() => onSelectTab('AI_INSIGHTS')}
              title="Trợ lý & SLA Stats"
              className={`w-full flex items-center ${isOpen ? 'space-x-2.5 px-3' : 'justify-center px-2'} py-2.5 rounded-xl text-xs font-medium transition ${
                currentTab === 'AI_INSIGHTS'
                  ? 'bg-purple-50 text-purple-700 font-semibold shadow-2xs'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <Bot className={`w-4 h-4 ${currentTab === 'AI_INSIGHTS' ? 'text-purple-600' : 'text-slate-400'}`} />
              {isOpen && (
                <div className="flex items-center space-x-1.5">
                  <span>Trợ lý & SLA Stats</span>
                  <Sparkles className="w-3 h-3 text-purple-500" />
                </div>
              )}
            </button>
          </div>

          {/* Module D: Identity & Users (Admin only) */}
          {role === 'ADMIN' && (
            <div className="pt-2">
              {isOpen && (
                <span className="px-3 text-[9px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                  Quản trị
                </span>
              )}
              <button
                onClick={() => onSelectTab('ADMIN_USERS')}
                title="Quản lý Agent & User"
                className={`w-full flex items-center ${isOpen ? 'space-x-2.5 px-3' : 'justify-center px-2'} py-2.5 rounded-xl text-xs font-medium transition ${
                  currentTab === 'ADMIN_USERS'
                    ? 'bg-purple-50 text-purple-700 font-semibold shadow-2xs'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <Users className={`w-4 h-4 ${currentTab === 'ADMIN_USERS' ? 'text-purple-600' : 'text-slate-400'}`} />
                {isOpen && <span>Quản lý Agent</span>}
              </button>
            </div>
          )}
        </nav>
      </div>

      {/* Footer Info */}
      <div className="p-2 border-t border-slate-100 space-y-1">
        <button
          onClick={() => onSelectTab('SETTINGS')}
          title="Cấu hình hệ thống"
          className={`w-full flex items-center ${isOpen ? 'space-x-2 px-3' : 'justify-center px-2'} py-2 rounded-xl text-xs font-medium transition ${
            currentTab === 'SETTINGS' ? 'bg-slate-100 text-slate-900' : 'text-slate-500 hover:bg-slate-50'
          }`}
        >
          <Settings className="w-4 h-4 text-slate-400" />
          {isOpen && <span>Cấu hình</span>}
        </button>
        {isOpen && (
          <div className="px-3 py-1 flex items-center justify-between text-[10px] text-slate-400">
            <span>Spring AI v1.0</span>
            <span className="flex items-center gap-1 text-slate-400 hover:text-slate-600 cursor-pointer">
              <HelpCircle className="w-3 h-3" /> Trợ giúp
            </span>
          </div>
        )}
      </div>
    </aside>
  );
};
