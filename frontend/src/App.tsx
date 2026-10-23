import { useState } from 'react';
import { UserRole, Ticket, Message, KnowledgeDocument, User } from './types';
import { 
  currentUserMock, 
  mockTickets, 
  mockMessagesByTicketId, 
  mockKnowledgeDocuments, 
  mockAISuggestionsByTicketId, 
  mockUsers 
} from './mock/data';
import { Navbar } from './components/layout/Navbar';
import { Sidebar, NavTab } from './components/layout/Sidebar';
import { TicketQueue } from './features/ticket/TicketQueue';
import { TicketWorkspace } from './features/ticket/TicketWorkspace';
import { KnowledgeBaseView } from './features/knowledge/KnowledgeBaseView';
import { CustomerPortal } from './features/customer/CustomerPortal';
import { AdminUserView } from './features/admin/AdminUserView';
import { AIInsightsView } from './features/analytics/AIInsightsView';

export function App() {
  const [role, setRole] = useState<UserRole>('AGENT');
  const [activeTab, setActiveTab] = useState<NavTab>('QUEUE');
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isQueueCollapsed, setIsQueueCollapsed] = useState(false);
  
  // State management
  const [tickets, setTickets] = useState<Ticket[]>(mockTickets);
  // Default to first OPEN ticket when starting on QUEUE
  const [selectedTicketId, setSelectedTicketId] = useState<string>(
    mockTickets.find(t => t.status === 'OPEN')?.id || mockTickets[0]?.id || ''
  );
  const [messagesMap, setMessagesMap] = useState<Record<string, Message[]>>(mockMessagesByTicketId);
  const [documents, setDocuments] = useState<KnowledgeDocument[]>(mockKnowledgeDocuments);
  const [users, setUsers] = useState<User[]>(mockUsers);

  const handleSelectTab = (newTab: NavTab) => {
    // Nếu đang ở tab hiện tại mà hàng đợi bị thu gọn, click lại vào tab sẽ mở lại hàng đợi (chuẩn Slack/Notion)
    if (newTab === activeTab && isQueueCollapsed) {
      setIsQueueCollapsed(false);
      return;
    }
    setActiveTab(newTab);
    setIsQueueCollapsed(false);
    if (newTab === 'QUEUE') {
      const firstOpen = tickets.find(t => t.status === 'OPEN');
      if (firstOpen) setSelectedTicketId(firstOpen.id);
    } else if (newTab === 'MY_TICKETS') {
      const firstMy = tickets.find(t => t.assignee?.id === currentUserMock.id) || tickets.find(t => t.status === 'IN_PROGRESS');
      if (firstMy) setSelectedTicketId(firstMy.id);
    }
  };

  const openTickets = tickets.filter(t => t.status === 'OPEN');
  const myTickets = tickets.filter(t => t.assignee?.id === currentUserMock.id || t.status === 'IN_PROGRESS');

  const currentTabTickets = activeTab === 'QUEUE' ? openTickets : myTickets;
  const selectedTicket = currentTabTickets.find(t => t.id === selectedTicketId) 
    || currentTabTickets[0] 
    || tickets.find(t => t.id === selectedTicketId) 
    || tickets[0];
  const currentMessages = messagesMap[selectedTicket?.id] || [];
  const currentAISuggestion = mockAISuggestionsByTicketId[selectedTicket?.id] || null;

  // Handlers for Ticket Actions
  const handleSendMessage = (ticketId: string, content: string, isInternal: boolean = false) => {
    const newMsg: Message = {
      id: `msg-${Date.now()}`,
      ticketId,
      sender: {
        name: role === 'CUSTOMER' ? 'Nguyễn Văn An' : currentUserMock.name,
        email: role === 'CUSTOMER' ? 'an.nguyen@company.com' : currentUserMock.email,
        role: role,
        avatar: role === 'CUSTOMER' 
          ? 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80'
          : currentUserMock.avatar,
      },
      content,
      isInternal,
      createdAt: new Date().toISOString(),
    };

    setMessagesMap(prev => ({
      ...prev,
      [ticketId]: [...(prev[ticketId] || []), newMsg],
    }));
  };

  const handleClaimTicket = (ticketId: string) => {
    setTickets(prev =>
      prev.map(t =>
        t.id === ticketId
          ? {
              ...t,
              status: 'IN_PROGRESS',
              assignee: {
                id: currentUserMock.id,
                name: currentUserMock.name,
                avatar: currentUserMock.avatar,
              },
            }
          : t
      )
    );
    setActiveTab('MY_TICKETS');
    setSelectedTicketId(ticketId);
  };

  const handleResolveTicket = (ticketId: string) => {
    setTickets(prev =>
      prev.map(t =>
        t.id === ticketId
          ? { ...t, status: 'RESOLVED' }
          : t
      )
    );
  };

  const handleCloseTicket = (ticketId: string) => {
    setTickets(prev =>
      prev.map(t =>
        t.id === ticketId
          ? { ...t, status: 'CLOSED' }
          : t
      )
    );
  };

  const handleCreateTicket = (title: string, description: string, category: string) => {
    const newTicket: Ticket = {
      id: `tck-${Date.now()}`,
      ticketNumber: `TCK-${1032 + tickets.length}`,
      title,
      description,
      status: 'OPEN',
      priority: 'NORMAL',
      category,
      customer: {
        name: 'Nguyễn Văn An',
        email: 'an.nguyen@company.com',
        avatar: 'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=80',
        organization: 'K24 - Khoa CNTT',
      },
      assignee: null,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      slaDeadline: new Date(Date.now() + 8 * 3600 * 1000).toISOString(),
    };

    setTickets(prev => [newTicket, ...prev]);
    setSelectedTicketId(newTicket.id);

    // Initial message
    setMessagesMap(prev => ({
      ...prev,
      [newTicket.id]: [
        {
          id: `msg-${Date.now()}`,
          ticketId: newTicket.id,
          sender: {
            name: newTicket.customer.name,
            email: newTicket.customer.email,
            role: 'CUSTOMER',
            avatar: newTicket.customer.avatar,
          },
          content: description,
          isInternal: false,
          createdAt: newTicket.createdAt,
        }
      ]
    }));
  };

  // Handlers for Knowledge Base
  const handleUploadDocument = (title: string, category: string, filename: string) => {
    const newDoc: KnowledgeDocument = {
      id: `doc-${Date.now()}`,
      title,
      filename,
      fileSize: '1.2 MB',
      status: 'PROCESSING',
      chunkCount: 16,
      isPublished: false,
      uploadedAt: new Date().toISOString(),
      category,
      summary: 'Đang trích xuất chunks và tính toán vector embeddings...',
    };

    setDocuments(prev => [newDoc, ...prev]);

    // Simulate completion
    setTimeout(() => {
      setDocuments(prev =>
        prev.map(d => (d.id === newDoc.id ? { ...d, status: 'READY', isPublished: true } : d))
      );
    }, 2500);
  };

  const handleTogglePublish = (id: string) => {
    setDocuments(prev =>
      prev.map(d =>
        d.id === id ? { ...d, isPublished: !d.isPublished } : d
      )
    );
  };

  const handleArchiveDocument = (id: string) => {
    setDocuments(prev =>
      prev.map(d =>
        d.id === id ? { ...d, status: 'ARCHIVED', isPublished: false } : d
      )
    );
  };

  // Handlers for Users
  const handleToggleUserActive = (userId: string) => {
    setUsers(prev =>
      prev.map(u => (u.id === userId ? { ...u, active: !u.active } : u))
    );
  };

  const handleCreateAgent = (name: string, email: string, newRole: UserRole) => {
    const newUser: User = {
      id: `usr-${Date.now()}`,
      name,
      email,
      role: newRole,
      avatar: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100',
      active: true,
    };
    setUsers(prev => [...prev, newUser]);
  };

  const openTicketCount = tickets.filter(t => t.status === 'OPEN').length;
  const assignedTicketCount = tickets.filter(t => t.assignee?.id === currentUserMock.id).length;

  return (
    <div className="min-h-screen flex flex-col bg-slate-100 font-sans">
      {/* Top Navbar with Instant Role Switcher */}
      <Navbar
        currentRole={role}
        onRoleChange={(newRole) => {
          setRole(newRole);
          if (newRole === 'CUSTOMER') {
            handleSelectTab('MY_TICKETS');
          } else {
            handleSelectTab('QUEUE');
          }
        }}
        currentUser={currentUserMock}
        isSidebarOpen={isSidebarOpen}
        onToggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)}
      />

      {/* Main Content Area */}
      <div className="flex-1 flex overflow-hidden">
        {role === 'CUSTOMER' ? (
          // Phân hệ Customer Portal (Màn 3, 4, 5)
          <CustomerPortal
            tickets={tickets}
            messages={Object.values(messagesMap).flat()}
            onCreateTicket={handleCreateTicket}
            onSendMessage={(ticketId, content) => handleSendMessage(ticketId, content, false)}
            onCloseTicket={handleCloseTicket}
          />
        ) : (
          // Phân hệ Agent & Admin (HelpDesk Workspace)
          <>
            {/* Column 1: Sidebar Navigation (Collapsible) */}
            <Sidebar
              currentTab={activeTab}
              onSelectTab={handleSelectTab}
              role={role}
              openTicketCount={openTicketCount}
              assignedTicketCount={assignedTicketCount}
              isOpen={isSidebarOpen}
            />

            {/* View Switching based on active tab */}
            {activeTab === 'QUEUE' && (
              <>
                {/* Column 2: Ticket Queue (Collapsible) */}
                <TicketQueue
                  tickets={tickets.filter(t => t.status === 'OPEN')}
                  selectedTicketId={selectedTicket?.id}
                  onSelectTicket={(t) => setSelectedTicketId(t.id)}
                  title="Hàng đợi Ticket OPEN"
                  isCollapsed={isQueueCollapsed}
                  onToggleCollapse={() => setIsQueueCollapsed(!isQueueCollapsed)}
                />

                {/* Column 3: Redesigned Spacious Ticket Workspace */}
                {selectedTicket ? (
                  <TicketWorkspace
                    ticket={selectedTicket}
                    messages={currentMessages}
                    onSendMessage={handleSendMessage}
                    onClaimTicket={handleClaimTicket}
                    onResolveTicket={handleResolveTicket}
                    aiSuggestion={currentAISuggestion}
                    isQueueCollapsed={isQueueCollapsed}
                    onToggleQueue={() => setIsQueueCollapsed(!isQueueCollapsed)}
                    queueTicketCount={openTickets.length}
                  />
                ) : (
                  <div className="flex-1 flex flex-col items-center justify-center text-slate-400 text-xs space-y-3 bg-slate-50">
                    <p>Không có ticket nào trong hàng đợi</p>
                    {isQueueCollapsed && (
                      <button
                        onClick={() => setIsQueueCollapsed(false)}
                        className="px-3 py-1.5 bg-white border border-slate-200 text-helpdesk-600 font-semibold rounded-lg shadow-2xs hover:bg-helpdesk-50 transition"
                      >
                        Mở lại hàng đợi ({openTickets.length})
                      </button>
                    )}
                  </div>
                )}
              </>
            )}

            {activeTab === 'MY_TICKETS' && (
              <>
                {/* Column 2: Assigned Tickets (Collapsible) */}
                <TicketQueue
                  tickets={tickets.filter(t => t.assignee?.id === currentUserMock.id)}
                  selectedTicketId={selectedTicket?.id}
                  onSelectTicket={(t) => setSelectedTicketId(t.id)}
                  title="Ticket tôi đang xử lý"
                  isCollapsed={isQueueCollapsed}
                  onToggleCollapse={() => setIsQueueCollapsed(!isQueueCollapsed)}
                />

                {/* Column 3: Workspace */}
                {selectedTicket ? (
                  <TicketWorkspace
                    ticket={selectedTicket}
                    messages={currentMessages}
                    onSendMessage={handleSendMessage}
                    onClaimTicket={handleClaimTicket}
                    onResolveTicket={handleResolveTicket}
                    aiSuggestion={currentAISuggestion}
                    isQueueCollapsed={isQueueCollapsed}
                    onToggleQueue={() => setIsQueueCollapsed(!isQueueCollapsed)}
                    queueTicketCount={myTickets.length}
                  />
                ) : (
                  <div className="flex-1 flex flex-col items-center justify-center text-slate-400 text-xs space-y-3 bg-slate-50">
                    <p>Bạn chưa nhận ticket nào</p>
                    {isQueueCollapsed && (
                      <button
                        onClick={() => setIsQueueCollapsed(false)}
                        className="px-3 py-1.5 bg-white border border-slate-200 text-helpdesk-600 font-semibold rounded-lg shadow-2xs hover:bg-helpdesk-50 transition"
                      >
                        Mở lại hàng đợi ({myTickets.length})
                      </button>
                    )}
                  </div>
                )}
              </>
            )}

            {activeTab === 'KNOWLEDGE_BASE' && (
              // Module B: Knowledge Base Explorer (Màn 9, 10)
              <KnowledgeBaseView
                documents={documents}
                onUploadDocument={handleUploadDocument}
                onTogglePublish={handleTogglePublish}
                onArchiveDocument={handleArchiveDocument}
              />
            )}

            {activeTab === 'AI_INSIGHTS' && (
              // Module A: AI Assistance & Analytics (FR-AI-03 & SLA)
              <AIInsightsView />
            )}

            {activeTab === 'ADMIN_USERS' && (
              // Module D: Admin User & Agent Management (Màn 11)
              <AdminUserView
                users={users}
                onToggleUserActive={handleToggleUserActive}
                onCreateAgent={handleCreateAgent}
              />
            )}

            {activeTab === 'SETTINGS' && (
              <div className="flex-1 bg-white p-8 text-left space-y-4">
                <h1 className="text-lg font-bold text-slate-900">Cấu hình hệ thống Helpdesk & KB</h1>
                <p className="text-xs text-slate-500">
                  Cấu hình các tham số Spring AI, Flyway DB connection, pgvector similarity threshold (0.75), JWT expiration (86400s).
                </p>
                <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2 text-xs font-mono">
                  <p>SPRING_AI_GEMINI_MODEL=gemini-1.5-pro</p>
                  <p>PGVECTOR_INDEX_DIMENSIONS=1536</p>
                  <p>SECURITY_JWT_ACCESS_TOKEN_VALIDITY_SECONDS=900</p>
                  <p>SECURITY_JWT_REFRESH_TOKEN_VALIDITY_SECONDS=604800</p>
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
