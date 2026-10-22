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
}

export const Sidebar: React.FC<SidebarProps> = ({
  currentTab,
  onSelectTab,
  role,
  openTicketCount,
  assignedTicketCount,
}) => {
  return (
    <aside className="w-60 bg-white border-r border-slate-200 flex flex-col justify-between select-none h-[calc(100vh-3.5rem)] shrink-0">
      <div className="p-3 space-y-6">
        {/* Workspace Title */}
        <div className="px-2 pt-1 flex items-center justify-between">
          <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
            {role === 'CUSTOMER' ? 'Customer Workspace' : role === 'ADMIN' ? 'Admin Portal' : 'Agent Workspace'}
          </span>
        </div>

        {/* Navigation Links */}
        <nav className="space-y-1">
          {/* Module C: Tickets */}
          {role !== 'CUSTOMER' ? (
            <>
              <button
                onClick={() => onSelectTab('QUEUE')}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium transition ${
                  currentTab === 'QUEUE'
                    ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <div className="flex items-center space-x-2.5">
                  <Inbox className={`w-4 h-4 ${currentTab === 'QUEUE' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
                  <span>Hàng đợi OPEN</span>
                </div>
                {openTicketCount > 0 && (
                  <span className="bg-helpdesk-100 text-helpdesk-700 text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                    {openTicketCount}
                  </span>
                )}
              </button>

              <button
                onClick={() => onSelectTab('MY_TICKETS')}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium transition ${
                  currentTab === 'MY_TICKETS'
                    ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <div className="flex items-center space-x-2.5">
                  <CheckCircle2 className={`w-4 h-4 ${currentTab === 'MY_TICKETS' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
                  <span>Đang xử lý</span>
                </div>
                {assignedTicketCount > 0 && (
                  <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                    {assignedTicketCount}
                  </span>
                )}
              </button>
            </>
          ) : (
            <button
              onClick={() => onSelectTab('MY_TICKETS')}
              className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium transition ${
                currentTab === 'MY_TICKETS'
                  ? 'bg-emerald-50 text-emerald-800 font-semibold'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <div className="flex items-center space-x-2.5">
                <Inbox className="w-4 h-4 text-emerald-600" />
                <span>Ticket của tôi</span>
              </div>
              <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-1.5 py-0.5 rounded-full">
                2
              </span>
            </button>
          )}

          {/* Module B: Knowledge Base */}
          <div className="pt-3">
            <span className="px-3 text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
              Tri thức (KB)
            </span>
            <button
              onClick={() => onSelectTab('KNOWLEDGE_BASE')}
              className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-medium transition ${
                currentTab === 'KNOWLEDGE_BASE'
                  ? 'bg-helpdesk-50 text-helpdesk-700 font-semibold'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <BookOpen className={`w-4 h-4 ${currentTab === 'KNOWLEDGE_BASE' ? 'text-helpdesk-600' : 'text-slate-400'}`} />
              <span>Kho tài liệu RAG</span>
            </button>
          </div>

          {/* Module A: AI Assistance */}
          <div className="pt-3">
            <span className="px-3 text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
              Phân tích & AI
            </span>
            <button
              onClick={() => onSelectTab('AI_INSIGHTS')}
              className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-medium transition ${
                currentTab === 'AI_INSIGHTS'
                  ? 'bg-purple-50 text-purple-700 font-semibold'
                  : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
              }`}
            >
              <Bot className={`w-4 h-4 ${currentTab === 'AI_INSIGHTS' ? 'text-purple-600' : 'text-slate-400'}`} />
              <div className="flex items-center space-x-1.5">
                <span>Trợ lý & SLA Stats</span>
                <Sparkles className="w-3 h-3 text-purple-500" />
              </div>
            </button>
          </div>

          {/* Module D: Identity & Users (Visible to Admin or for inspection) */}
          {role === 'ADMIN' && (
            <div className="pt-3">
              <span className="px-3 text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">
                Quản trị (Module D)
              </span>
              <button
                onClick={() => onSelectTab('ADMIN_USERS')}
                className={`w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-medium transition ${
                  currentTab === 'ADMIN_USERS'
                    ? 'bg-purple-50 text-purple-700 font-semibold'
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                }`}
              >
                <Users className={`w-4 h-4 ${currentTab === 'ADMIN_USERS' ? 'text-purple-600' : 'text-slate-400'}`} />
                <span>Quản lý Agent & User</span>
              </button>
            </div>
          )}
        </nav>
      </div>

      {/* Footer Info */}
      <div className="p-3 border-t border-slate-100 space-y-1">
        <button
          onClick={() => onSelectTab('SETTINGS')}
          className={`w-full flex items-center space-x-2 px-3 py-2 rounded-lg text-xs font-medium transition ${
            currentTab === 'SETTINGS' ? 'bg-slate-100 text-slate-900' : 'text-slate-500 hover:bg-slate-50'
          }`}
        >
          <Settings className="w-4 h-4 text-slate-400" />
          <span>Cấu hình hệ thống</span>
        </button>
        <div className="px-3 py-1 flex items-center justify-between text-[11px] text-slate-400">
          <span>Spring AI v1.0</span>
          <span className="flex items-center gap-1 text-slate-400 hover:text-slate-600 cursor-pointer">
            <HelpCircle className="w-3 h-3" /> Trợ giúp
          </span>
        </div>
      </div>
    </aside>
  );
};
