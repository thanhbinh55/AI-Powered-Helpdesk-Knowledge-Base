#!/bin/bash
# ==============================================================================
# Script chuyển đổi báo cáo Markdown (.md) sang HTML tự chứa và PDF
# Dự án: AI-Powered Helpdesk & Knowledge Base - Group 4 (HCMUS)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPORTS_DIR="$REPO_ROOT/reports"
RENDERED_DIR="$REPORTS_DIR/rendered"

mkdir -p "$RENDERED_DIR"

echo "================================================================================"
echo "🚀 TIẾN HÀNH RENDER BÁO CÁO MARKDOWN SANG HTML / PDF"
echo "================================================================================"
echo "📁 Thư mục báo cáo: $REPORTS_DIR"
echo "📁 Thư mục xuất file: $RENDERED_DIR"
echo ""

# Chạy trình render thông minh
python3 "$SCRIPT_DIR/render_reports.py"

echo "================================================================================"
echo "✅ Hoàn tất render tài liệu!"
echo "📌 Vị trí các tệp đã tạo: reports/rendered/"
echo "================================================================================"
