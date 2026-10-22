export type UserRole = 'CUSTOMER' | 'AGENT' | 'ADMIN';

export type TicketStatus = 'OPEN' | 'IN_PROGRESS' | 'RESOLVED' | 'CLOSED';
export type TicketPriority = 'LOW' | 'NORMAL' | 'HIGH' | 'URGENT';

export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  avatar?: string;
  active: boolean;
}

export interface Ticket {
  id: string;
  ticketNumber: string;
  title: string;
  description: string;
  status: TicketStatus;
  priority: TicketPriority;
  category: string;
  customer: {
    name: string;
    email: string;
    avatar?: string;
    organization?: string;
  };
  assignee?: {
    id: string;
    name: string;
    avatar?: string;
  } | null;
  createdAt: string;
  updatedAt: string;
  slaDeadline: string; // ISO String
  unreadCount?: number;
}

export interface Message {
  id: string;
  ticketId: string;
  sender: {
    name: string;
    email: string;
    avatar?: string;
    role: UserRole;
  };
  content: string;
  isInternal: boolean; // TRUE: Amber Yellow Internal Note; FALSE: Public Reply
  createdAt: string;
  attachments?: string[];
}

export type DocumentStatus = 'PENDING' | 'PROCESSING' | 'READY' | 'FAILED' | 'ARCHIVED';

export interface KnowledgeDocument {
  id: string;
  title: string;
  filename: string;
  fileSize: string;
  status: DocumentStatus;
  chunkCount: number;
  isPublished: boolean;
  uploadedAt: string;
  category: string;
  summary?: string;
}

export interface Citation {
  documentId: string;
  documentTitle: string;
  chunkSnippet: string;
  score: number;
  pageOrSection?: string;
}

export interface AISuggestion {
  ticketId: string;
  draftReply: string;
  citations: Citation[];
  confidence: number;
  generatedAt: string;
}
