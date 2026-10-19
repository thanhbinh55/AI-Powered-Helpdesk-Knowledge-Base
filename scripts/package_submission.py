#!/usr/bin/env python3
"""
scripts/package_submission.py
Đóng gói sản phẩm nộp bài đồ án thành file GroupID.zip (mặc định: Group04.zip).
Tuân thủ nghiêm ngặt các ràng buộc từ Giảng viên (HCMUS):
- Loại bỏ toàn bộ file nhạy cảm và file rác: .git, .env, node_modules, target, __pycache__, *.zip, .DS_Store...
- Ràng buộc 1: Tổng số file trong kho lưu trữ <= 20 files.
- Ràng buộc 2: Dung lượng mỗi file <= 20 MB.
- Không dùng link Google Drive.
- Hướng dẫn chia nhỏ (split-and-zip) khi vượt quá giới hạn.
"""

import os
import sys
import zipfile
import argparse

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MAX_FILES = 20
MAX_FILE_SIZE_BYTES = 20 * 1024 * 1024  # 20 MB

# Các thư mục và mẫu tên file bị loại trừ
EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    "target",
    "build",
    "dist",
    "out",
    "__pycache__",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    ".pytest_cache",
    ".gradle"
}

EXCLUDE_EXTENSIONS = {
    ".zip",
    ".tar.gz",
    ".rar",
    ".7z",
    ".pyc",
    ".class",
    ".swp"
}

EXCLUDE_FILENAMES = {
    ".env",
    ".env.local",
    ".DS_Store",
    "tasks_created.csv"
}


def is_excluded(rel_path):
    parts = rel_path.split(os.sep)
    for part in parts:
        if part in EXCLUDE_DIRS:
            return True
        if part.startswith(".env"):
            return True

    base_name = os.path.basename(rel_path)
    if base_name in EXCLUDE_FILENAMES:
        return True

    for ext in EXCLUDE_EXTENSIONS:
        if base_name.endswith(ext):
            return True

    return False


def collect_files(root_dir):
    collected = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Lọc dirnames tại chỗ để không đi sâu vào các thư mục bị loại trừ
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]

        for fname in filenames:
            abs_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(abs_path, root_dir)

            if not is_excluded(rel_path):
                file_size = os.path.getsize(abs_path)
                collected.append((abs_path, rel_path, file_size))

    return collected


def main():
    parser = argparse.ArgumentParser(description="Đóng gói nộp bài đồ án NMCNPM theo quy định giảng viên.")
    parser.add_argument("--group-id", default="Group04", help="Tên nhóm / Mã nộp bài (mặc định: Group04)")
    parser.add_argument("--output-dir", default=REPO_ROOT, help="Thư mục chứa file zip kết quả")
    parser.add_argument("--force", action="store_true", help="Bỏ qua cảnh báo số file/dung lượng để tiếp tục tạo zip")
    args = parser.parse_args()

    zip_filename = f"{args.group_id}.zip"
    zip_output_path = os.path.join(os.path.abspath(args.output_dir), zip_filename)

    print("================================================================================")
    print(f"📦 ĐÓNG GÓI NỘP BÀI: {zip_filename}")
    print("================================================================================")
    print(f"📂 Thư mục gốc: {REPO_ROOT}")
    print(f"🎯 File đầu ra dự kiến: {zip_output_path}")
    print(f"⚙️ Giới hạn quy định: Tối đa {MAX_FILES} file, mỗi file <= 20 MB, KHÔNG link Drive.\n")

    files_to_pack = collect_files(REPO_ROOT)
    total_count = len(files_to_pack)

    print(f"🔍 Đã quét và thu thập được: {total_count} file cần đóng gói.\n")
    print(f"{'STT':<4} | {'Dung lượng (KB)':<15} | {'Đường dẫn file':<50}")
    print("-" * 75)

    violations = []
    for idx, (abs_path, rel_path, size) in enumerate(files_to_pack, 1):
        size_kb = size / 1024.0
        print(f"{idx:<4} | {size_kb:>13.2f} KB | {rel_path}")

        if size > MAX_FILE_SIZE_BYTES:
            violations.append(f"❌ File vượt quá 20 MB ({size / (1024*1024):.2f} MB): {rel_path}")

    print("-" * 75)

    has_error = False

    # Kiểm tra ràng buộc số lượng file
    if total_count > MAX_FILES:
        print(f"\n⚠️ CẢNH BÁO QUY ĐỊNH: Số lượng file ({total_count}) VƯỢT QUÁ mức cho phép ({MAX_FILES} file)!")
        has_error = True

    # Kiểm tra ràng buộc dung lượng từng file
    if violations:
        print("\n⚠️ CẢNH BÁO DUNG LƯỢNG:")
        for v in violations:
            print(f"  {v}")
        has_error = True

    if has_error and not args.force:
        print("\n❌ QUÁ TRÌNH TẠO FILE ZIP BỊ TẠM DỪNG ĐỂ TRÁNH BỊ TRỪ ĐIỂM!")
        print("--------------------------------------------------------------------------------")
        print("💡 HƯỚNG DẪN XỬ LÝ (SPLIT-AND-ZIP HOẶC TINH CHỈNH):")
        print("   1. Nếu số file vượt quá 20:")
        print("      - Xóa các file build tạm thời, file cache.")
        print("      - Chỉ chọn nộp các file báo cáo cần thiết (.md và .html trong reports/rendered/).")
        print("   2. Nếu có file > 20 MB:")
        print("      - Nén ảnh trong reports/assets/ bằng công cụ tối ưu ảnh.")
        print("      - Dùng lệnh chia nhỏ file: split -b 19M <file_lon> <file_lon>.part_")
        print("   3. Nếu bạn vẫn muốn ép buộc đóng gói, hãy thêm tham số --force:")
        print(f"      python3 scripts/package_submission.py --group-id {args.group_id} --force")
        print("--------------------------------------------------------------------------------")
        sys.exit(1)

    print(f"\n🔨 Đang tiến hành nén vào {zip_output_path}...")
    with zipfile.ZipFile(zip_output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for abs_path, rel_path, _ in files_to_pack:
            zf.write(abs_path, rel_path)

    final_size_mb = os.path.getsize(zip_output_path) / (1024 * 1024)
    print(f"🎉 ĐÃ TẠO THÀNH CÔNG: {zip_output_path}")
    print(f"📊 Tổng số file trong gói: {total_count}")
    print(f"⚖️ Dung lượng gói nộp: {final_size_mb:.2f} MB")
    print("================================================================================")


if __name__ == "__main__":
    main()
