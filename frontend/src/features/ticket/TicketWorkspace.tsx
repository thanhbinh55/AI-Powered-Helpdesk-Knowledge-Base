import React, { useState, useRef, useEffect } from 'react';
import { Ticket, Message, AISuggestion, Citation } from '../../types';
import { TicketIssuePane } from './components/TicketIssuePane';
import { TicketChatPane } from './components/TicketChatPane';
import { CitationModal } from './components/CitationModal';

interface TicketWorkspaceProps {
  ticket: Ticket;
  messages: Message[];
  onSendMessage: (ticketId: string, content: string, isInternal: boolean) => void;
  onClaimTicket: (ticketId: string) => void;
  onResolveTicket: (ticketId: string) => void;
  aiSuggestion?: AISuggestion | null;
  isQueueCollapsed?: boolean;
  onToggleQueue?: () => void;
  queueTicketCount?: number;
}

export const TicketWorkspace: React.FC<TicketWorkspaceProps> = ({
  ticket,
  messages,
  onSendMessage,
  onClaimTicket,
  onResolveTicket,
  aiSuggestion,
  isQueueCollapsed = false,
  onToggleQueue,
  queueTicketCount,
}) => {
  const [replyText, setReplyText] = useState('');
  const [isAIDeclined, setIsAIDeclined] = useState(false);
  const [selectedCitation, setSelectedCitation] = useState<Citation | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Khi chuyển ticket khác: Đặt lại trạng thái AI Suggestion và xóa nháp
  useEffect(() => {
    setIsAIDeclined(false);
    setReplyText('');
  }, [ticket.id]);

  // Hành động với AI Suggestion
  const handleAcceptAI = (draft: string) => {
    setReplyText(draft);
    textareaRef.current?.focus();
  };

  const handleEditAI = (draft: string) => {
    setReplyText(draft);
    setTimeout(() => {
      if (textareaRef.current) {
        textareaRef.current.focus();
        textareaRef.current.setSelectionRange(draft.length, draft.length);
      }
    }, 50);
  };

  const handleDeclineAI = () => {
    setIsAIDeclined(true);
  };

  const handleRestoreAI = () => {
    setIsAIDeclined(false);
  };

  return (
    <div className="flex-1 flex overflow-hidden h-[calc(100vh-3.5rem)] bg-slate-100 select-none">
      {/* 1. Cột Trái: Ticket Detail & Issue Workspace (Spacious, uncompressed issue view) */}
      <TicketIssuePane
        ticket={ticket}
        aiSuggestion={aiSuggestion}
        isQueueCollapsed={isQueueCollapsed}
        onToggleQueue={onToggleQueue}
        queueTicketCount={queueTicketCount}
        onClaimTicket={onClaimTicket}
        onResolveTicket={onResolveTicket}
        onViewCitation={(cite) => setSelectedCitation(cite)}
      />

      {/* 2. Cột Phải: Chat Pane (Facebook Messenger style, AI auto-suggestion, composer) */}
      <TicketChatPane
        ticket={ticket}
        messages={messages}
        aiSuggestion={aiSuggestion}
        isAIDeclined={isAIDeclined}
        onAcceptAI={handleAcceptAI}
        onEditAI={handleEditAI}
        onDeclineAI={handleDeclineAI}
        onRestoreAI={handleRestoreAI}
        onViewCitation={(cite) => setSelectedCitation(cite)}
        onSendMessage={onSendMessage}
        replyText={replyText}
        setReplyText={setReplyText}
        textareaRef={textareaRef}
      />

      {/* 3. Modal xem chi tiết trích dẫn RAG Grounding */}
      <CitationModal
        citation={selectedCitation}
        onClose={() => setSelectedCitation(null)}
      />
    </div>
  );
};
