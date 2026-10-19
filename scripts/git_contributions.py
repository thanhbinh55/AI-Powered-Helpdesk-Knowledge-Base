#!/usr/bin/env python3
"""
scripts/git_contributions.py
Đọc thông tin từ members.csv và lịch sử git log để tổng hợp danh sách commit theo từng thành viên:
- Định dạng danh mục: MSSV - Git username
- Số lượng commit
- Chi tiết từng commit: hash rút gọn, ngày commit, message (kèm Jira key), danh sách file thay đổi
Chỉ ghi đè nội dung nằm giữa cặp marker <!-- GENERATED:START --> và <!-- GENERATED:END -->
trong file reports/08-git-contributions.md.
"""

import os
import sys
import csv
import subprocess
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MEMBERS_CSV = os.path.join(REPO_ROOT, "members.csv")
REPORT_FILE = os.path.join(REPO_ROOT, "reports", "08-git-contributions.md")

START_MARKER = "<!-- GENERATED:START -->"
END_MARKER = "<!-- GENERATED:END -->"


def load_members():
    members = []
    if not os.path.exists(MEMBERS_CSV):
        print(f"⚠️ Cảnh báo: Không tìm thấy file {MEMBERS_CSV}")
        return members

    with open(MEMBERS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            members.append({
                "mssv": row.get("mssv", "").strip(),
                "full_name": row.get("full_name", "").strip(),
                "git_username": row.get("git_username", "").strip(),
                "git_email": row.get("git_email", "").strip().lower(),
                "jira_email": row.get("jira_email", "").strip(),
                "role_module": row.get("role_module", "").strip(),
                "commits": []
            })
    return members


def get_git_commits():
    """Lấy danh sách commit và danh sách file thay đổi từ git log."""
    # Kiểm tra xem repo đã có commit nào chưa
    test_res = subprocess.run(["git", "rev-parse", "--verify", "HEAD"],
                              cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if test_res.returncode != 0:
        return []

    # Định dạng git log: hash, author_name, author_email, date, subject
    cmd = [
        "git", "log",
        "--pretty=format:COMMIT_SEP%n%H%n%an%n%ae%n%ad%n%s",
        "--date=short",
        "--name-only"
    ]
    res = subprocess.run(cmd, cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    raw_output = res.stdout.strip()
    if not raw_output:
        return []

    commit_blocks = raw_output.split("COMMIT_SEP\n")
    parsed_commits = []

    for block in commit_blocks:
        if not block.strip():
            continue
        lines = block.strip().splitlines()
        if len(lines) < 5:
            continue
        commit_hash = lines[0].strip()
        author_name = lines[1].strip()
        author_email = lines[2].strip().lower()
        commit_date = lines[3].strip()
        commit_subject = lines[4].strip()
        files = [line.strip() for line in lines[5:] if line.strip()]

        parsed_commits.append({
            "hash": commit_hash,
            "short_hash": commit_hash[:8],
            "author_name": author_name,
            "author_email": author_email,
            "date": commit_date,
            "subject": commit_subject,
            "files": files
        })

    return parsed_commits


def generate_markdown(members, commits):
    # Phân loại commit theo thành viên
    unassigned_commits = []

    for commit in commits:
        assigned = False
        for m in members:
            # Đối chiếu linh hoạt qua git_email, jira_email hoặc git_username
            git_em = m["git_email"]
            jira_em = m["jira_email"].lower()
            git_user = m["git_username"].lower()
            author_em = commit["author_email"]
            author_nm = commit["author_name"].lower()

            match_git_email = git_em and not git_em.startswith("<") and git_em == author_em
            match_jira_email = jira_em and not jira_em.startswith("<") and jira_em == author_em
            match_username = git_user and not git_user.startswith("<") and (git_user == author_nm or git_user in author_nm)

            if match_git_email or match_jira_email or match_username:
                m["commits"].append(commit)
                assigned = True
                break
        if not assigned:
            unassigned_commits.append(commit)

    md = []
    md.append("### 📊 Tổng Hợp Lịch Sử Commit Theo Thành Viên (Tự Động Sinh)\n")
    md.append(f"> **Tổng số commit ghi nhận trong repository:** {len(commits)}\n")

    # Bảng tóm tắt số lượng commit
    md.append("| MSSV - Git username | Họ và tên | Vai trò / Phân hệ | Số lượng commit |")
    md.append("| :--- | :--- | :--- | :---: |")
    for m in members:
        ident = f"{m['mssv']} - {m['git_username']}"
        md.append(f"| **{ident}** | {m['full_name']} | {m['role_module']} | {len(m['commits'])} |")

    if unassigned_commits:
        md.append(f"| *(Chưa liên kết trong members.csv / Setup)* | - | Khởi tạo cấu hình repo | {len(unassigned_commits)} |")

    md.append("\n---\n")

    # Chi tiết từng thành viên
    for m in members:
        ident = f"{m['mssv']} - {m['git_username']}"
        md.append(f"#### 👤 {ident} ({m['full_name']})")
        md.append(f"- **Phân hệ phụ trách:** {m['role_module']}")
        md.append(f"- **Tổng số commit:** {len(m['commits'])}")

        if not m["commits"]:
            md.append("*(Chưa có commit nào được ghi nhận với thông tin tác giả này)*\n")
            continue

        md.append("\n| Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi |")
        md.append("| :--- | :--- | :--- | :--- |")
        for c in m["commits"]:
            files_str = "<br>".join([f"<code>{f}</code>" for f in c["files"][:4]])
            if len(c["files"]) > 4:
                files_str += f"<br>*(và {len(c['files']) - 4} tệp khác...)*"
            if not files_str:
                files_str = "*(không có tệp thay đổi)*"
            clean_subject = c["subject"].replace("|", "\\|")
            md.append(f"| `[{c['short_hash']}]` | {c['date']} | {clean_subject} | {files_str} |")
        md.append("")

    if unassigned_commits:
        md.append("#### ⚙️ Các Commit Khởi Tạo / Chưa Ánh Xạ Trong `members.csv`")
        md.append(f"- **Tổng số commit:** {len(unassigned_commits)}\n")
        md.append("| Hash | Tác giả Git | Ngày | Thông điệp commit |")
        md.append("| :--- | :--- | :--- | :--- |")
        for c in unassigned_commits:
            clean_sub = c["subject"].replace("|", "\\|")
            md.append(f"| `[{c['short_hash']}]` | `{c['author_name']}` | {c['date']} | {clean_sub} |")
        md.append("")

    return "\n".join(md)


def update_report_file(generated_content):
    if not os.path.exists(REPORT_FILE):
        print(f"❌ Lỗi: Không tìm thấy file {REPORT_FILE}")
        sys.exit(1)

    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print(f"❌ Lỗi: Không tìm thấy cặp marker hợp lệ ({START_MARKER} ... {END_MARKER}) trong {REPORT_FILE}")
        sys.exit(1)

    new_content = (
        content[:start_idx + len(START_MARKER)]
        + "\n"
        + generated_content
        + "\n"
        + content[end_idx:]
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Đã cập nhật thành công khu vực marker trong: {REPORT_FILE}")


def main():
    print("🔍 Đang nạp danh sách thành viên từ members.csv...")
    members = load_members()
    print(f"   Tìm thấy {len(members)} thành viên.")

    print("📜 Đang truy xuất lịch sử git log...")
    commits = get_git_commits()
    print(f"   Tìm thấy {len(commits)} commit trong repository.")

    generated_md = generate_markdown(members, commits)
    update_report_file(generated_md)


if __name__ == "__main__":
    main()
