import React from 'react';
import { Sparkles, Check, X, ExternalLink, RotateCcw } from 'lucide-react';
import { AISuggestion, Citation } from '../../../types';

interface AISuggestionCardProps {
  suggestion?: AISuggestion | null;
  isDeclined: boolean;
  onAccept: () => void;
  onEdit: () => void;
  onDecline: () => void;
  onRestore: () => void;
  onViewCitation: (citation: Citation) => void;
}

export const AISuggestionCard: React.FC<AISuggestionCardProps> = ({
  suggestion,
  isDeclined,
  onAccept,
  onEdit,
  onDecline,
  onRestore,
  onViewCitation,
}) => {
  if (!suggestion) return null;

  if (isDeclined) {
    return (
      <div className="px-3 py-1 flex justify-end">
        <button
          type="button"
          onClick={onRestore}
          className="inline-flex items-center space-x-1 text-[11px] text-purple-600 hover:text-purple-800 font-medium py-1 px-2 hover:bg-purple-50 rounded-lg transition"
        >
          <RotateCcw className="w-3 h-3" />
          <span>Hiện lại gợi ý AI</span>
        </button>
      </div>
    );
  }

  return (
    <div className="mx-2.5 mb-2 p-3 bg-gradient-to-br from-purple-50 via-indigo-50/70 to-purple-50/50 border border-purple-200 rounded-2xl shadow-xs text-left space-y-2 animate-in fade-in slide-in-from-bottom-2 duration-150">
      {/* Header gợi ý */}
      <div className="flex items-center justify-between text-xs">
        <div className="flex items-center space-x-1.5">
          <div className="p-1 bg-purple-600 text-white rounded-md shadow-2xs">
            <Sparkles className="w-3.5 h-3.5" />
          </div>
          <h4 className="font-bold text-purple-950 text-xs">✨ AI Đề xuất câu trả lời</h4>
          <span className="text-[10px] bg-purple-200 text-purple-900 font-bold px-1.5 py-0.2 rounded-full">
            {Math.round((suggestion.confidence || 0.95) * 100)}% khớp
          </span>
        </div>
        <button
          onClick={onDecline}
          title="Bỏ qua gợi ý này"
          className="text-slate-400 hover:text-slate-600 p-0.5 rounded transition"
        >
          <X className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Nội dung câu trả lời nháp */}
      <div className="p-2.5 bg-white/95 border border-purple-100 rounded-xl text-xs text-slate-700 leading-relaxed max-h-32 overflow-y-auto whitespace-pre-wrap shadow-2xs font-normal">
        {suggestion.draftReply}
      </div>

      {/* Trích dẫn nguồn click xem */}
      {suggestion.citations && suggestion.citations[0] && (
        <div
          onClick={() => onViewCitation(suggestion.citations[0])}
          className="flex items-center justify-between p-1.5 bg-white/80 hover:bg-white border border-purple-100 hover:border-purple-300 rounded-lg text-[11px] text-purple-900 cursor-pointer transition shadow-2xs"
        >
          <span className="truncate max-w-[240px] font-medium text-[10px]">
            📚 {suggestion.citations[0].documentTitle}
          </span>
          <span className="text-purple-600 font-bold text-[10px] shrink-0 flex items-center gap-0.5">
            Xem nguồn <ExternalLink className="w-2.5 h-2.5" />
          </span>
        </div>
      )}

      {/* 3 Nút hành động nổi bật: Accept (ac), Edit, Decline */}
      <div className="flex items-center space-x-1.5 pt-0.5">
        <button
          type="button"
          onClick={onAccept}
          title="Chấp nhận bản nháp và đưa vào ô trả lời"
          className="flex-1 py-1.5 px-2 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white rounded-xl text-xs font-semibold shadow-xs transition active:scale-95 flex items-center justify-center space-x-1"
        >
          <Check className="w-3 h-3" />
          <span>Áp dụng (Accept)</span>
        </button>

        <button
          type="button"
          onClick={onEdit}
          title="Chỉnh sửa nội dung bản nháp trước khi gửi"
          className="py-1.5 px-3 bg-white hover:bg-purple-50 text-purple-800 border border-purple-200 rounded-xl text-xs font-semibold shadow-xs transition active:scale-95 flex items-center justify-center space-x-1"
        >
          <span>Sửa (Edit)</span>
        </button>

        <button
          type="button"
          onClick={onDecline}
          title="Từ chối gợi ý này"
          className="py-1.5 px-2.5 text-slate-500 hover:text-rose-600 hover:bg-rose-50 rounded-xl text-xs transition font-medium"
        >
          <span>Từ chối</span>
        </button>
      </div>
    </div>
  );
};
