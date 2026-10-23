import React from 'react';
import { Sparkles } from 'lucide-react';
import { Citation } from '../../../types';

interface CitationModalProps {
  citation: Citation | null;
  onClose: () => void;
}

export const CitationModal: React.FC<CitationModalProps> = ({ citation, onClose }) => {
  if (!citation) return null;

  return (
    <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl max-w-lg w-full p-5 space-y-4 shadow-xl border border-slate-200 text-left animate-in fade-in zoom-in-95">
        <div className="flex items-center justify-between border-b border-slate-100 pb-3">
          <div className="flex items-center space-x-2">
            <Sparkles className="w-4 h-4 text-purple-600" />
            <h3 className="font-bold text-sm text-slate-900">Chi tiết nguồn trích dẫn RAG</h3>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-slate-600 text-xs px-2 py-1 rounded transition"
          >
            ✕ Đóng
          </button>
        </div>

        <div className="space-y-3 text-xs">
          <div>
            <span className="text-slate-400 block text-[10px] uppercase font-bold">Tài liệu</span>
            <p className="font-semibold text-purple-950 text-sm">{citation.documentTitle}</p>
          </div>

          <div>
            <span className="text-slate-400 block text-[10px] uppercase font-bold">Vị trí</span>
            <p className="font-medium text-slate-700">{citation.pageOrSection}</p>
          </div>

          <div>
            <span className="text-slate-400 block text-[10px] uppercase font-bold">Đoạn trích Vector Chunk</span>
            <div className="p-3 bg-purple-50/70 border border-purple-200 rounded-xl text-slate-800 font-serif leading-relaxed italic">
              "{citation.chunkSnippet}"
            </div>
          </div>
        </div>

        <button
          onClick={onClose}
          className="w-full py-2 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-semibold transition"
        >
          Đóng cửa sổ
        </button>
      </div>
    </div>
  );
};
