import React from 'react';
import { TicketStatus, TicketPriority, DocumentStatus, UserRole } from '../../types';

interface BadgeProps {
  children?: React.ReactNode;
  variant?: 'status' | 'priority' | 'docStatus' | 'role' | 'default';
  value?: TicketStatus | TicketPriority | DocumentStatus | UserRole | string;
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({ variant = 'default', value, children, className = '' }) => {
  const content = children || value;

  let colorClasses = 'bg-slate-100 text-slate-700 border-slate-200';

  if (variant === 'status') {
    switch (value) {
      case 'OPEN':
        colorClasses = 'bg-blue-50 text-blue-700 border-blue-200';
        break;
      case 'IN_PROGRESS':
        colorClasses = 'bg-amber-50 text-amber-700 border-amber-200';
        break;
      case 'RESOLVED':
        colorClasses = 'bg-emerald-50 text-emerald-700 border-emerald-200';
        break;
      case 'CLOSED':
        colorClasses = 'bg-slate-100 text-slate-600 border-slate-300';
        break;
    }
  } else if (variant === 'priority') {
    switch (value) {
      case 'URGENT':
        colorClasses = 'bg-red-50 text-red-700 border-red-200 font-semibold';
        break;
      case 'HIGH':
        colorClasses = 'bg-orange-50 text-orange-700 border-orange-200 font-medium';
        break;
      case 'NORMAL':
        colorClasses = 'bg-blue-50 text-blue-700 border-blue-200';
        break;
      case 'LOW':
        colorClasses = 'bg-slate-100 text-slate-600 border-slate-200';
        break;
    }
  } else if (variant === 'docStatus') {
    switch (value) {
      case 'READY':
        colorClasses = 'bg-emerald-50 text-emerald-700 border-emerald-200';
        break;
      case 'PROCESSING':
        colorClasses = 'bg-purple-50 text-purple-700 border-purple-200 animate-pulse';
        break;
      case 'PENDING':
        colorClasses = 'bg-amber-50 text-amber-700 border-amber-200';
        break;
      case 'FAILED':
        colorClasses = 'bg-red-50 text-red-700 border-red-200';
        break;
      case 'ARCHIVED':
        colorClasses = 'bg-slate-100 text-slate-500 border-slate-200';
        break;
    }
  } else if (variant === 'role') {
    switch (value) {
      case 'ADMIN':
        colorClasses = 'bg-purple-50 text-purple-700 border-purple-200';
        break;
      case 'AGENT':
        colorClasses = 'bg-blue-50 text-blue-700 border-blue-200';
        break;
      case 'CUSTOMER':
        colorClasses = 'bg-emerald-50 text-emerald-700 border-emerald-200';
        break;
    }
  }

  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium border ${colorClasses} ${className}`}>
      {content}
    </span>
  );
};
