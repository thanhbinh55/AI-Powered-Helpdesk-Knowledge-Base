#!/usr/bin/env python3
"""
scripts/git_contributions.py
Đọc thông tin từ members.csv và lịch sử git log để tổng hợp danh sách commit theo từng thành viên:
- Định dạng chuẩn học thuật: MSSV - Git username (Họ và tên)
- Bảng tổng hợp số lượng commit và tỷ lệ % đóng góp
- Chi tiết từng commit: hash rút gọn, ngày commit, thông điệp kèm Jira key, danh sách file thay đổi
- Tự động đồng bộ vào reports/08-git-contributions.md và reports/submit/08-git-contributions.md
"""

import os
import sys
import csv
import subprocess
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MEMBERS_CSV = os.path.join(REPO_ROOT, "members.csv")
REPORT_FILE = os.path.join(REPO_ROOT, "reports", "08-git-contributions.md")
SUBMIT_REPORT_FILE = os.path.join(REPO_ROOT, "reports", "submit", "git-contributions", "git-contributions.md")


def load_members():
    members = []
    if not os.path.exists(MEMBERS_CSV):
        print(f"Cảnh báo: Không tìm thấy file {MEMBERS_CSV}")
        return members

    with open(MEMBERS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            members.append({
                "mssv": row.get("mssv", "").strip(),
                "full_name": row.get("full_name", "").strip(),
                "git_username": row.get("git_username", "").strip(),
                "git_email": row.get("git_email", "").strip().lower(),
                "jira_email": row.get("jira_email", "").strip().lower(),
                "role_module": row.get("role_module", "").strip(),
                "commits": []
            })
    return members


def get_git_commits():
    """Lấy danh sách commit và danh sách file thay đổi từ git log."""
    test_res = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if test_res.returncode != 0:
        return []

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


def build_full_report(members, commits):
    # Phân loại commit theo thành viên
    unassigned_commits = []

    for commit in commits:
        assigned = False
        author_em = commit["author_email"]
        author_nm = commit["author_name"].lower()

        for m in members:
            git_em = m["git_email"]
            jira_em = m["jira_email"]
            git_user = m["git_username"].lower()

            match_git_email = git_em and not git_em.startswith("<") and git_em == author_em
            match_jira_email = jira_em and not jira_em.startswith("<") and jira_em == author_em
            match_username = git_user and not git_user.startswith("<") and (git_user == author_nm or git_user in author_nm)

            if match_git_email or match_jira_email or match_username:
                m["commits"].append(commit)
                assigned = True
                break
        if not assigned:
            unassigned_commits.append(commit)

    total_commits = len(commits)

    md = []
    md.append("# BÁO CÁO LỊCH SỬ COMMIT GIT (GIT COMMIT HISTORY REPORT)\n")
    md.append("> **Dự án:** AI-Powered Helpdesk & Knowledge Base  ")
    md.append("> **Mã nhóm:** Group 04  ")
    md.append("> **Môn học:** Nhập môn Công nghệ Phần mềm (CS10014) — Trường ĐHKHTN, ĐHQG-HCM  ")
    md.append("> **Kho lưu trữ (Repository):** https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base  \n")
    md.append("---\n")
    md.append("## THÔNG TIN TÀI LIỆU\n")
    today_str = datetime.now().strftime("%Y-%m-%d")
    md.append("- **Tiêu đề (Title):** Git Commit History & Individual Contributions Report")
    md.append("- **Phiên bản (Version):** 1.0.0")
    md.append(f"- **Ngày cập nhật (Generated Date):** {today_str}")
    md.append("- **Nhóm trưởng & Giám sát kỹ thuật:** `24120269` - `Ngô Viết Thanh Bình` (thanhbinh55)")
    md.append("- **Danh sách thành viên:**")
    md.append("  1. `24120269` - `thanhbinh55` — Ngô Viết Thanh Bình (DevOps / Lead / Phân hệ Identity & Access)")
    md.append("  2. `24120083` - `Lamnguyen-code` — Nguyễn Đức Lãm (Backend / QC / Phân hệ Knowledge Base)")
    md.append("  3. `24120503` - `t4lf4n` — Phan Gia Phúc (Full-stack / Testing Lead / Phân hệ Ticket Management)")
    md.append("  4. `24120121` - `Shinkiisme` — Lê Quý Phúc (AI Integration / Phân hệ AI Assistance)")
    md.append("- **Mục đích tài liệu:** Thống kê minh bạch, chính xác toàn bộ lịch sử commit Git của từng thành viên từ lúc khởi tạo repository đến hiện tại, phục vụ công tác đối soát đóng góp cá nhân và thẩm định của Giảng viên.\n")
    md.append("---\n")
    md.append("## DANH SÁCH COMMIT CỦA MỖI THÀNH VIÊN\n")
    md.append("Mỗi mục dưới đây thống kê chi tiết toàn bộ các commit của từng thành viên theo trật tự thời gian, bao gồm mã hash rút gọn (8 ký tự), ngày commit, thông điệp commit và danh sách các tệp tin thay đổi.\n")

    for idx, m in enumerate(members, 1):
        ident = f"{m['mssv']} - {m['git_username']}"
        md.append("---\n")
        md.append(f"### {idx}. Thành viên: {ident} ({m['full_name']})")
        md.append(f"- **Họ và tên:** {m['full_name']}")
        md.append(f"- **Mã số sinh viên:** `{m['mssv']}`")
        md.append(f"- **Tài khoản Git:** `{m['git_username']}`")
        md.append(f"- **Email Git:** `{m['git_email']}`")
        md.append(f"- **Phân hệ phụ trách:** {m['role_module']}")
        md.append(f"- **Tổng số commit ghi nhận:** {len(m['commits'])} commits\n")

        if not m["commits"]:
            md.append("*(Chưa có commit nào được ghi nhận với thông tin tác giả này)*\n")
            continue

        md.append("| STT | Mã Hash | Ngày commit | Thông điệp commit (Jira Key) | Các tệp thay đổi chính |")
        md.append("| :---: | :--- | :---: | :--- | :--- |")

        for c_idx, c in enumerate(m["commits"], 1):
            if c["files"]:
                file_items = [f"<code>{f}</code>" for f in c["files"][:4]]
                files_str = "<br>".join(file_items)
                if len(c["files"]) > 4:
                    files_str += f"<br>*(và {len(c['files']) - 4} tệp khác...)*"
            else:
                files_str = "*(Merge commit / không có tệp thay đổi trực tiếp)*"

            clean_subject = c["subject"].replace("|", "\\|")
            md.append(f"| {c_idx} | `[{c['short_hash']}]` | {c['date']} | {clean_subject} | {files_str} |")
        md.append("")

    if unassigned_commits:
        md.append("---\n")
        md.append(f"### {len(members) + 1}. Các commit khởi tạo / chưa ánh xạ trong members.csv")
        md.append(f"- **Tổng số commit:** {len(unassigned_commits)}\n")
        md.append("| STT | Mã Hash | Tác giả Git | Ngày commit | Thông điệp commit |")
        md.append("| :---: | :--- | :--- | :---: | :--- |")
        for c_idx, c in enumerate(unassigned_commits, 1):
            clean_sub = c["subject"].replace("|", "\\|")
            md.append(f"| {c_idx} | `[{c['short_hash']}]` | `{c['author_name']}` | {c['date']} | {clean_sub} |")
        md.append("")

    return "\n".join(md)


def main():
    print("Đang nạp danh sách thành viên từ members.csv...")
    members = load_members()
    print(f"Tìm thấy {len(members)} thành viên.")

    print("Đang truy xuất lịch sử git log...")
    commits = get_git_commits()
    print(f"Tìm thấy {len(commits)} commit trong repository.")

    report_content = build_full_report(members, commits)

    # Ghi vào reports/08-git-contributions.md
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Đã cập nhật: {REPORT_FILE}")

    # Ghi vào reports/submit/08-git-contributions.md
    os.makedirs(os.path.dirname(SUBMIT_REPORT_FILE), exist_ok=True)
    with open(SUBMIT_REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Đã tạo bản nộp: {SUBMIT_REPORT_FILE}")


if __name__ == "__main__":
    main()
