import React from 'react';
import { Sparkles, Bot, LifeBuoy, Bell, Menu, PanelLeftClose, PanelLeft } from 'lucide-react';
import { UserRole, User } from '../../types';

interface NavbarProps {
  currentRole: UserRole;
  onRoleChange: (role: UserRole) => void;
  currentUser: User;
  isSidebarOpen: boolean;
  onToggleSidebar: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ 
  currentRole, 
  onRoleChange, 
  currentUser,
  isSidebarOpen,
  onToggleSidebar
}) => {
  return (
    <header className="h-14 bg-white border-b border-slate-200 px-4 flex items-center justify-between select-none sticky top-0 z-30">
      {/* Brand Logo & Sidebar Toggle */}
      <div className="flex items-center space-x-3">
        {currentRole !== 'CUSTOMER' && (
          <button
            onClick={onToggleSidebar}
            title={isSidebarOpen ? "Thu gọn thanh chức năng" : "Mở rộng thanh chức năng"}
            className="p-1.5 text-slate-500 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition"
          >
            {isSidebarOpen ? <PanelLeftClose className="w-5 h-5" /> : <PanelLeft className="w-5 h-5 text-helpdesk-600" />}
          </button>
        )}

        <div className="flex items-center space-x-2.5">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-helpdesk-600 to-indigo-500 flex items-center justify-center text-white shadow-sm shadow-blue-500/20">
            <LifeBuoy className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="font-bold text-slate-900 text-sm tracking-tight">HelpDesk</span>
              <span className="text-xs bg-helpdesk-100 text-helpdesk-700 px-1.5 py-0.2 rounded font-semibold flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-helpdesk-600" /> AI-Ready
              </span>
            </div>
            <p className="text-[10px] text-slate-400 font-medium">HCMUS • Group 04</p>
          </div>
        </div>
      </div>

      {/* Role Switcher & Environment Indicator */}
      <div className="flex items-center space-x-3">
        <div className="hidden lg:flex items-center space-x-1.5 text-xs text-slate-500 bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-full">
          <Bot className="w-3.5 h-3.5 text-emerald-600 animate-pulse" />
          <span className="font-medium text-slate-600">RAG Engine:</span>
          <span className="text-emerald-700 font-semibold">pgvector Connected</span>
        </div>

        {/* Live Role Switcher (Dành cho việc chuyển đổi kiểm thử vai trò) */}
        <div className="bg-slate-100 p-0.5 rounded-lg border border-slate-200 flex items-center">
          <span className="text-[10px] font-bold text-slate-400 px-2 uppercase tracking-wider hidden sm:inline">Vai trò:</span>
          <button
            onClick={() => onRoleChange('CUSTOMER')}
            className={`px-2.5 py-1 text-xs font-medium rounded-md transition-all ${
              currentRole === 'CUSTOMER'
                ? 'bg-white text-emerald-700 shadow-xs font-semibold'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            Customer
          </button>
          <button
            onClick={() => onRoleChange('AGENT')}
            className={`px-2.5 py-1 text-xs font-medium rounded-md transition-all ${
              currentRole === 'AGENT'
                ? 'bg-white text-helpdesk-700 shadow-xs font-semibold'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            Support Agent
          </button>
          <button
            onClick={() => onRoleChange('ADMIN')}
            className={`px-2.5 py-1 text-xs font-medium rounded-md transition-all ${
              currentRole === 'ADMIN'
                ? 'bg-white text-purple-700 shadow-xs font-semibold'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            System Admin
          </button>
        </div>
      </div>

      {/* User Info & Actions */}
      <div className="flex items-center space-x-3">
        <button 
          title="Thông báo hệ thống"
          className="p-1.5 text-slate-400 hover:text-slate-600 hover:bg-slate-100 rounded-full transition relative"
        >
          <Bell className="w-4 h-4" />
          <span className="absolute top-1 right-1 w-2 h-2 bg-blue-500 rounded-full ring-2 ring-white"></span>
        </button>

        <div className="h-6 w-px bg-slate-200"></div>

        <div className="flex items-center space-x-2">
          <img
            src={currentUser.avatar}
            alt={currentUser.name}
            className="w-7 h-7 rounded-full object-cover ring-1 ring-slate-300"
          />
          <div className="hidden sm:block text-left">
            <p className="text-xs font-semibold text-slate-800 leading-tight">{currentUser.name}</p>
            <p className="text-[10px] text-slate-500">{currentUser.email}</p>
          </div>
        </div>
      </div>
    </header>
  );
};
