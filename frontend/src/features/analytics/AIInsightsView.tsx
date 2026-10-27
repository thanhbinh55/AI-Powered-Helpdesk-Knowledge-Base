import { useState } from 'react';
import { 
  Sparkles, 
  TrendingUp, 
  Clock, 
  CheckCircle, 
  Zap, 
  Database,
  ToggleLeft,
  ToggleRight
} from 'lucide-react';

export const AIInsightsView: React.FC = () => {
  const [mockAiEnabled, setMockAiEnabled] = useState(true);

  return (
    <div className="flex-1 bg-white h-[calc(100vh-3.5rem)] overflow-y-auto p-6 space-y-6 text-left">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
        <div>
          <div className="flex items-center space-x-2">
            <h1 className="text-lg font-bold text-slate-900 tracking-tight">Trợ lý AI & Thống kê SLA</h1>
            <span className="text-xs bg-purple-100 text-purple-700 font-bold px-2 py-0.5 rounded-full flex items-center gap-1">
              <Sparkles className="w-3 h-3" /> Module A (Quý Phúc)
            </span>
          </div>
          <p className="text-xs text-slate-500 mt-1">
            Hiệu suất phản hồi của mô hình RAG, tỷ lệ áp dụng gợi ý và chỉ số SLA hệ thống
          </p>
        </div>

        {/* Mock AI Toggle (NFR-AVAIL-01) */}
        <div className="flex items-center space-x-3 bg-purple-50 border border-purple-200 px-3.5 py-2 rounded-xl">
          <div className="text-left">
            <span className="text-xs font-bold text-purple-900 block">Chế độ Mock AI Offline</span>
            <span className="text-[10px] text-purple-600">NFR-AVAIL-01 Resilience</span>
          </div>
          <button
            onClick={() => setMockAiEnabled(!mockAiEnabled)}
            className="text-purple-700 hover:text-purple-900 transition"
          >
            {mockAiEnabled ? (
              <ToggleRight className="w-8 h-8 text-purple-600" />
            ) : (
              <ToggleLeft className="w-8 h-8 text-slate-400" />
            )}
          </button>
        </div>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
          <div className="flex items-center justify-between text-slate-400 mb-1">
            <span className="text-xs font-semibold">Tỷ lệ chấp nhận AI</span>
            <Sparkles className="w-4 h-4 text-purple-600" />
          </div>
          <p className="text-2xl font-bold text-purple-900">88.4%</p>
          <span className="text-[10px] text-emerald-600 font-semibold flex items-center gap-1 mt-1">
            <TrendingUp className="w-3 h-3" /> +12% so với tuần trước
          </span>
        </div>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
          <div className="flex items-center justify-between text-slate-400 mb-1">
            <span className="text-xs font-semibold">Thời gian phản hồi TB</span>
            <Clock className="w-4 h-4 text-blue-600" />
          </div>
          <p className="text-2xl font-bold text-slate-900">14 phút</p>
          <span className="text-[10px] text-emerald-600 font-semibold flex items-center gap-1 mt-1">
            <TrendingUp className="w-3 h-3" /> Đạt SLA 100%
          </span>
        </div>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
          <div className="flex items-center justify-between text-slate-400 mb-1">
            <span className="text-xs font-semibold">pgvector Latency</span>
            <Zap className="w-4 h-4 text-amber-600" />
          </div>
          <p className="text-2xl font-bold text-slate-900">42 ms</p>
          <span className="text-[10px] text-slate-500 font-medium block mt-1">
            Cosine similarity search
          </span>
        </div>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4">
          <div className="flex items-center justify-between text-slate-400 mb-1">
            <span className="text-xs font-semibold">Tỷ lệ giải quyết</span>
            <CheckCircle className="w-4 h-4 text-emerald-600" />
          </div>
          <p className="text-2xl font-bold text-emerald-700">96.2%</p>
          <span className="text-[10px] text-slate-500 font-medium block mt-1">
            Tổng số 240 tickets tháng 10
          </span>
        </div>
      </div>

      {/* RAG Top Citations */}
      <div className="border border-slate-200 rounded-xl p-5 bg-white space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Database className="w-4 h-4 text-purple-600" />
            <h2 className="text-sm font-bold text-slate-900">Tài liệu được AI trích dẫn nhiều nhất (Citations Leaderboard)</h2>
          </div>
          <span className="text-xs text-slate-400 font-medium">Cập nhật thời gian thực</span>
        </div>

        <div className="space-y-3">
          {[
            {
              title: 'Chính sách bảo lưu kết quả học tập & Quy định hoàn phí học vụ',
              category: 'Quy định đào tạo',
              citations: 86,
              confidence: '95%',
            },
            {
              title: 'Hướng dẫn khắc phục lỗi xác thực tài khoản & JWT Token Expired',
              category: 'Kỹ thuật & Tài khoản',
              citations: 64,
              confidence: '97%',
            },
            {
              title: 'Quy trình cấp phát tài khoản VPN & Máy chủ thực hành AI Lab',
              category: 'Cơ sở hạ tầng',
              citations: 39,
              confidence: '89%',
            },
          ].map((item, idx) => (
            <div key={idx} className="flex items-center justify-between p-3 bg-slate-50 border border-slate-100 rounded-xl">
              <div className="space-y-0.5">
                <p className="text-xs font-semibold text-slate-900">{item.title}</p>
                <span className="text-[10px] text-slate-400">{item.category}</span>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-xs font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded-full">
                  {item.citations} trích dẫn
                </span>
                <span className="text-xs font-semibold text-emerald-700">
                  {item.confidence} match
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
