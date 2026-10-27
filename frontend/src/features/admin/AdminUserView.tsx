import { useState } from 'react';
import { UserPlus, Sparkles } from 'lucide-react';
import { User, UserRole } from '../../types';
import { Badge } from '../../components/common/Badge';

interface AdminUserViewProps {
  users: User[];
  onToggleUserActive: (userId: string) => void;
  onCreateAgent: (name: string, email: string, role: UserRole) => void;
}

export const AdminUserView: React.FC<AdminUserViewProps> = ({
  users,
  onToggleUserActive,
  onCreateAgent,
}) => {
  const [showModal, setShowModal] = useState(false);
  const [newName, setNewName] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [newRole, setNewRole] = useState<UserRole>('AGENT');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newName.trim() || !newEmail.trim()) return;
    onCreateAgent(newName, newEmail, newRole);
    setShowModal(false);
    setNewName('');
    setNewEmail('');
  };

  return (
    <div className="flex-1 bg-white h-[calc(100vh-3.5rem)] overflow-y-auto p-6 space-y-6 text-left">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
        <div>
          <div className="flex items-center space-x-2">
            <h1 className="text-lg font-bold text-slate-900 tracking-tight">Quản trị nhân sự & Phân quyền</h1>
            <span className="text-xs bg-purple-100 text-purple-700 font-bold px-2 py-0.5 rounded-full flex items-center gap-1">
              <Sparkles className="w-3 h-3" /> Module D (Bình - Lead)
            </span>
          </div>
          <p className="text-xs text-slate-500 mt-1">
            Quản lý tài khoản Support Agent, kiểm soát phân quyền RBAC và chính sách kích hoạt bảo mật
          </p>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="inline-flex items-center space-x-1.5 px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold rounded-lg shadow-sm transition"
        >
          <UserPlus className="w-4 h-4" />
          <span>Thêm Agent mới</span>
        </button>
      </div>

      {/* Agents Table */}
      <div className="border border-slate-200 rounded-xl overflow-hidden bg-white shadow-2xs">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase text-[10px] tracking-wider font-semibold">
              <th className="py-3 px-4">Thành viên</th>
              <th className="py-3 px-4">Email xác thực</th>
              <th className="py-3 px-4">Vai trò (Role)</th>
              <th className="py-3 px-4">Trạng thái tài khoản</th>
              <th className="py-3 px-4 text-right">Thao tác</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {users.map((user) => (
              <tr key={user.id} className="hover:bg-slate-50/70 transition">
                <td className="py-3.5 px-4">
                  <div className="flex items-center space-x-3">
                    <img
                      src={user.avatar || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80'}
                      alt={user.name}
                      className="w-8 h-8 rounded-full ring-1 ring-slate-200 object-cover"
                    />
                    <div>
                      <p className="font-semibold text-slate-900">{user.name}</p>
                      <span className="text-[10px] text-slate-400 font-mono">{user.id}</span>
                    </div>
                  </div>
                </td>
                <td className="py-3.5 px-4 text-slate-600 font-mono text-[11px]">
                  {user.email}
                </td>
                <td className="py-3.5 px-4">
                  <Badge variant="role" value={user.role} />
                </td>
                <td className="py-3.5 px-4">
                  <span className={`inline-flex items-center space-x-1 text-xs font-medium px-2 py-0.5 rounded-full ${
                    user.active ? 'bg-emerald-50 text-emerald-700' : 'bg-red-50 text-red-700'
                  }`}>
                    {user.active ? (
                      <>
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                        <span>Đang hoạt động</span>
                      </>
                    ) : (
                      <>
                        <span className="w-1.5 h-1.5 rounded-full bg-red-500"></span>
                        <span>Đã vô hiệu hóa</span>
                      </>
                    )}
                  </span>
                </td>
                <td className="py-3.5 px-4 text-right">
                  <button
                    onClick={() => onToggleUserActive(user.id)}
                    className={`px-3 py-1 text-[11px] font-semibold rounded-lg transition ${
                      user.active
                        ? 'bg-red-50 text-red-700 hover:bg-red-100'
                        : 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100'
                    }`}
                  >
                    {user.active ? 'Vô hiệu hóa (Disable)' : 'Kích hoạt (Enable)'}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Create Agent Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-xs flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-md w-full p-5 space-y-4 shadow-xl border border-slate-200">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <div className="flex items-center space-x-2">
                <UserPlus className="w-4 h-4 text-purple-600" />
                <h3 className="font-bold text-sm text-slate-900">Tạo tài khoản Agent mới</h3>
              </div>
              <button
                onClick={() => setShowModal(false)}
                className="text-slate-400 hover:text-slate-600 text-xs px-2 py-1 rounded"
              >
                ✕ Đóng
              </button>
            </div>

            <form onSubmit={handleSubmit} className="space-y-3 text-xs">
              <div>
                <label className="block font-semibold text-slate-700 mb-1">Họ và tên</label>
                <input
                  type="text"
                  required
                  value={newName}
                  onChange={(e) => setNewName(e.target.value)}
                  placeholder="Ví dụ: Lê Quý Phúc"
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Email tổ chức</label>
                <input
                  type="email"
                  required
                  value={newEmail}
                  onChange={(e) => setNewEmail(e.target.value)}
                  placeholder="quyphuc@hcmus.edu.vn"
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">Vai trò hệ thống</label>
                <select
                  value={newRole}
                  onChange={(e) => setNewRole(e.target.value as UserRole)}
                  className="w-full p-2.5 border border-slate-200 rounded-lg focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500"
                >
                  <option value="AGENT">Support Agent (Nhân viên hỗ trợ)</option>
                  <option value="ADMIN">System Administrator (Quản trị viên)</option>
                </select>
              </div>

              <div className="flex space-x-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="w-1/2 py-2 border border-slate-200 hover:bg-slate-50 text-slate-600 rounded-lg font-semibold"
                >
                  Hủy
                </button>
                <button
                  type="submit"
                  className="w-1/2 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg font-semibold shadow-xs"
                >
                  Tạo tài khoản
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
