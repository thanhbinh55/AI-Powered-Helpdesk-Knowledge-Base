import { useState } from 'react';
import { 
  BookOpen, 
  Upload, 
  Search, 
  FileText, 
  Layers, 
  Archive, 
  RotateCcw,
  Sparkles,
} from 'lucide-react';
import { KnowledgeDocument } from '../../types';
import { Badge } from '../../components/common/Badge';

interface KnowledgeBaseViewProps {
  documents: KnowledgeDocument[];
  onUploadDocument: (title: string, category: string, filename: string) => void;
  onTogglePublish: (id: string) => void;
  onArchiveDocument: (id: string) => void;
}

export const KnowledgeBaseView: React.FC<KnowledgeBaseViewProps> = ({
  documents,
  onUploadDocument,
  onTogglePublish,
  onArchiveDocument,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [showUploadModal, setShowUploadModal] = useState(false);
  const [newTitle, setNewTitle] = useState('');
  const [newCategory, setNewCategory] = useState('Chính sách chung');
  const [newFilename, setNewFilename] = useState('huong-dan-moi.pdf');

  const filteredDocs = documents.filter(doc =>
    doc.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    doc.category.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const totalChunks = documents.reduce((sum, doc) => sum + doc.chunkCount, 0);
  const readyDocs = documents.filter(doc => doc.status === 'READY').length;

  const handleUploadSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;
    onUploadDocument(newTitle, newCategory, newFilename);
    setShowUploadModal(false);
    setNewTitle('');
  };

  return (
    <div className="flex-1 bg-white h-[calc(100vh-3.5rem)] overflow-y-auto p-6 space-y-6 text-left">
      {/* Header & Metrics */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
        <div>
          <div className="flex items-center space-x-2">
            <h1 className="text-lg font-bold text-slate-900 tracking-tight">Kho tri thức & Vector Database</h1>
            <span className="text-xs bg-purple-100 text-purple-700 font-bold px-2 py-0.5 rounded-full flex items-center gap-1">
              <Sparkles className="w-3 h-3" /> Module B (Lãm)
            </span>
          </div>
          <p className="text-xs text-slate-500 mt-1">
            Quản lý tài liệu nguồn, trích xuất chunking và vector hóa embeddings phục vụ tìm kiếm RAG
          </p>
        </div>

        <button
          onClick={() => setShowUploadModal(true)}
          className="inline-flex items-center space-x-1.5 px-4 py-2 bg-helpdesk-600 hover:bg-helpdesk-700 text-white text-xs font-semibold rounded-lg shadow-sm transition"
        >
          <Upload className="w-4 h-4" />
          <span>Upload tài liệu mới</span>
        </button>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between">
          <div>
            <span className="text-xs font-semibold text-slate-400">Tài liệu đã Publish</span>
            <p className="text-xl font-bold text-slate-900 mt-1">{readyDocs} / {documents.length}</p>
          </div>
          <div className="w-10 h-10 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center">
            <BookOpen className="w-5 h-5" />
          </div>
        </div>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between">
          <div>
            <span className="text-xs font-semibold text-slate-400">pgvector Chunks</span>
            <p className="text-xl font-bold text-purple-900 mt-1">{totalChunks} chunks</p>
          </div>
          <div className="w-10 h-10 rounded-lg bg-purple-100 text-purple-600 flex items-center justify-center">
            <Layers className="w-5 h-5" />
          </div>
        </div>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between">
          <div>
            <span className="text-xs font-semibold text-slate-400">Hàng đợi xử lý</span>
            <p className="text-xl font-bold text-amber-900 mt-1">1 đang xử lý</p>
          </div>
          <div className="w-10 h-10 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center">
            <RotateCcw className="w-5 h-5 animate-spin" />
          </div>
        </div>
      </div>

      {/* Search & Filter Bar */}
      <div className="relative">
        <Search className="w-4 h-4 text-slate-400 absolute left-3 top-3" />
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Tìm kiếm tài liệu tri thức theo tiêu đề hoặc danh mục..."
          className="w-full pl-9 pr-4 py-2.5 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-helpdesk-500/20 focus:border-helpdesk-500 transition"
        />
      </div>

      {/* Documents Table */}
      <div className="border border-slate-200 rounded-xl overflow-hidden bg-white shadow-2xs">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase text-[10px] tracking-wider font-semibold">
              <th className="py-3 px-4">Tài liệu / File</th>
              <th className="py-3 px-4">Chuyên mục</th>
              <th className="py-3 px-4">Trạng thái</th>
              <th className="py-3 px-4">Vector Chunks</th>
              <th className="py-3 px-4">Ngày cập nhật</th>
              <th className="py-3 px-4 text-right">Thao tác</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {filteredDocs.map((doc) => (
              <tr key={doc.id} className="hover:bg-slate-50/70 transition">
                <td className="py-3.5 px-4">
                  <div className="flex items-center space-x-3">
                    <div className="p-2 bg-blue-50 text-helpdesk-600 rounded-lg shrink-0">
                      <FileText className="w-4 h-4" />
                    </div>
                    <div>
                      <p className="font-semibold text-slate-900">{doc.title}</p>
                      <span className="text-[11px] text-slate-400">{doc.filename} ({doc.fileSize})</span>
                    </div>
                  </div>
                </td>
                <td className="py-3.5 px-4 font-medium text-slate-600">
                  {doc.category}
                </td>
                <td className="py-3.5 px-4">
                  <Badge variant="docStatus" value={doc.status} />
                </td>
                <td className="py-3.5 px-4">
                  <span className="font-semibold text-purple-700 bg-purple-50 px-2 py-0.5 rounded-full text-[11px]">
                    {doc.chunkCount} embeddings
                  </span>
                </td>
                <td className="py-3.5 px-4 text-slate-400 text-[11px]">
                  {new Date(doc.uploadedAt).toLocaleDateString()}
                </td>
                <td className="py-3.5 px-4 text-right space-x-2">
                  <button
                    onClick={() => onTogglePublish(doc.id)}
                    className={`px-2.5 py-1 rounded text-[11px] font-semibold transition ${
                      doc.isPublished
                        ? 'bg-amber-50 text-amber-700 hover:bg-amber-100'
                        : 'bg-emerald-600 text-white hover:bg-emerald-700'
                    }`}
                  >
                    {doc.isPublished ? 'Hủy Publish' : 'Publish'}
                  </button>
                  <button
                    onClick={() => onArchiveDocument(doc.id)}
                    className="p-1 text-slate-400 hover:text-red-600 rounded transition"
                    title="Lưu trữ (Archive)"
                  >
                    <Archive className="w-4 h-4" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Upload Document Modal */}
      {showUploadModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-md w-full p-5 space-y-4 shadow-xl border border-slate-200">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div className="flex items-center space-x-2">
                <Upload className="w-4 h-4 text-helpdesk-600" />
                <h3 className="font-bold text-sm text-slate-900">Upload tài liệu Knowledge Base</h3>
              </div>
              <button
                onClick={() => setShowUploadModal(false)}
                className="text-slate-400 hover:text-slate-600 text-xs px-2 py-1 rounded"
              >
                ✕ Đóng
              </button>
            </div>

            <form onSubmit={handleUploadSubmit} className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-slate-700 mb-1">Tiêu đề tài liệu</label>
                <input
                  type="text"
                  required
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  placeholder="Ví dụ: Quy định đăng ký môn học và đóng học phí..."
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-helpdesk-500/20 focus:border-helpdesk-500"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Chuyên mục</label>
                <select
                  value={newCategory}
                  onChange={(e) => setNewCategory(e.target.value)}
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-helpdesk-500/20 focus:border-helpdesk-500"
                >
                  <option value="Chính sách chung">Chính sách chung</option>
                  <option value="Quy định đào tạo">Quy định đào tạo</option>
                  <option value="Kỹ thuật & Tài khoản">Kỹ thuật & Tài khoản</option>
                  <option value="Cơ sở hạ tầng">Cơ sở hạ tầng</option>
                </select>
              </div>

              <div className="border-2 border-dashed border-slate-200 rounded-xl p-5 text-center space-y-1">
                <FileText className="w-8 h-8 text-slate-300 mx-auto" />
                <p className="font-semibold text-slate-700">Kéo thả tệp PDF, TXT hoặc Markdown vào đây</p>
                <p className="text-[10px] text-slate-400">Hỗ trợ tối đa 20MB. Chunk size tự động 500 tokens.</p>
              </div>

              <div className="flex space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowUploadModal(false)}
                  className="w-1/2 py-2 border border-slate-200 hover:bg-slate-50 text-slate-600 rounded-lg font-semibold"
                >
                  Hủy
                </button>
                <button
                  type="submit"
                  className="w-1/2 py-2 bg-helpdesk-600 hover:bg-helpdesk-700 text-white rounded-lg font-semibold shadow-xs"
                >
                  Bắt đầu Vector hóa
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
