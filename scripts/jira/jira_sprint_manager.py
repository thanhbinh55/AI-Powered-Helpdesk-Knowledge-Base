#!/usr/bin/env python3
"""
scripts/jira/jira_sprint_manager.py
Công cụ quản lý và tự động tạo Sprint trên Jira Cloud (Agile REST API v1.0).
Hỗ trợ:
- Xem danh sách Sprint hiện có trên Board (--list)
- Tự động tạo Sprint mới với Tên, Ngày bắt đầu, Ngày kết thúc, Mục tiêu (--create)
- Cập nhật thông tin Sprint hiện có (--update --sprint-id <ID>)
- Tự động thêm các issues (Tasks) vào Sprint (--add-issues hoặc --from-cache)
- Chế độ chạy thử mô phỏng (--dry-run) an toàn
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
import base64

try:
    import requests
except ImportError:
    requests = None


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ENV_FILE = os.path.join(REPO_ROOT, ".env")
CACHE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "tasks_created.csv"))


def load_env():
    """Tự động nạp cấu hình từ .env."""
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key not in os.environ:
                        os.environ[key] = val


class JiraSprintClient:
    def __init__(self, base_url, email, token, dry_run=False):
        self.base_url = base_url.rstrip("/")
        self.email = email
        self.token = token
        self.dry_run = dry_run
        auth_str = f"{email}:{token}"
        self.auth_header = "Basic " + base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    def _request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": self.auth_header,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data_bytes = json.dumps(payload).encode("utf-8") if payload else None

        if requests is not None:
            try:
                resp = requests.request(method, url, headers=headers, json=payload, timeout=30)
                return resp.status_code, resp.text
            except Exception as e:
                return 0, str(e)

        req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.status, response.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8")
        except Exception as e:
            return 0, str(e)

    def get_scrum_board(self, project_key):
        """Lấy board ID cho dự án."""
        status, body = self._request("GET", f"/rest/agile/1.0/board?projectKeyOrId={project_key}")
        if status == 200:
            try:
                data = json.loads(body)
                values = data.get("values", [])
                if values:
                    return values[0]
            except Exception:
                pass
        return None

    def list_sprints(self, board_id):
        """Liệt kê các Sprint trên board."""
        status, body = self._request("GET", f"/rest/agile/1.0/board/{board_id}/sprint")
        if status == 200:
            try:
                return json.loads(body).get("values", [])
            except Exception:
                return []
        return []

    def create_sprint(self, name, board_id, start_date=None, end_date=None, goal=None):
        """Tạo Sprint mới trên Board."""
        if self.dry_run:
            print(f"  [DRY-RUN] Giả lập tạo Sprint '{name}' trên Board ID {board_id}.")
            return True, {"id": 9999, "name": name, "state": "future"}

        payload = {
            "name": name,
            "originBoardId": board_id
        }
        if start_date:
            payload["startDate"] = start_date
        if end_date:
            payload["endDate"] = end_date
        if goal:
            payload["goal"] = goal

        status, body = self._request("POST", "/rest/agile/1.0/sprint", payload=payload)
        if status in (200, 201):
            try:
                data = json.loads(body)
                return True, data
            except Exception:
                return True, {"id": "UNKNOWN", "name": name}
        else:
            return False, f"HTTP {status}: {body}"

    def update_sprint(self, sprint_id, name=None, start_date=None, end_date=None, goal=None):
        """Cập nhật Sprint đã có."""
        if self.dry_run:
            print(f"  [DRY-RUN] Giả lập cập nhật Sprint ID {sprint_id}.")
            return True, {"id": sprint_id, "name": name}

        payload = {}
        if name:
            payload["name"] = name
        if start_date:
            payload["startDate"] = start_date
        if end_date:
            payload["endDate"] = end_date
        if goal:
            payload["goal"] = goal

        status, body = self._request("PUT", f"/rest/agile/1.0/sprint/{sprint_id}", payload=payload)
        if status in (200, 201):
            try:
                data = json.loads(body)
                return True, data
            except Exception:
                return True, {"id": sprint_id}
        else:
            return False, f"HTTP {status}: {body}"

    def add_issues_to_sprint(self, sprint_id, issue_keys):
        """Gán các issues vào Sprint."""
        if not issue_keys:
            return True, "No issues to add"

        if self.dry_run:
            print(f"  [DRY-RUN] Giả lập gán {len(issue_keys)} issues vào Sprint ID {sprint_id}.")
            return True, "Dry-run success"

        status, body = self._request("POST", f"/rest/agile/1.0/sprint/{sprint_id}/issue", payload={"issues": issue_keys})
        if status in (200, 204):
            return True, "Success"
        else:
            return False, f"HTTP {status}: {body}"


def main():
    parser = argparse.ArgumentParser(description="Công cụ quản lý và tạo Sprint tự động trên Jira Cloud.")
    parser.add_argument("--list", action="store_true", help="Liệt kê danh sách các Sprint hiện có trên board")
    parser.add_argument("--create", action="store_true", help="Tạo Sprint mới tự động")
    parser.add_argument("--update", action="store_true", help="Cập nhật Sprint đã có (cần kèm --sprint-id)")
    parser.add_argument("--name", type=str, default="Sprint 2 - Template 1 & MVP P0", help="Tên của Sprint")
    parser.add_argument("--start", type=str, default="2026-11-03T00:00:00.000+07:00", help="Ngày bắt đầu (ISO 8601)")
    parser.add_argument("--end", type=str, default="2026-11-24T23:59:00.000+07:00", help="Ngày kết thúc (ISO 8601)")
    parser.add_argument("--goal", type=str,
                        default="Hoàn thiện tài liệu Template 1 (41 FRs, 30 US, 17 UCs, 151 frames Figma), khởi động Template 2 và phát triển mã nguồn MVP P0",
                        help="Mục tiêu của Sprint")
    parser.add_argument("--add-issues", nargs="+", help="Danh sách mã issue (ví dụ: SCRUM-5 SCRUM-6) cần gán vào Sprint")
    parser.add_argument("--sprint-id", type=str, help="Sprint ID chỉ định")
    parser.add_argument("--from-cache", action="store_true", help="Lấy danh sách issue từ file cache tasks_created.csv")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử nghiệm mô phỏng, không gửi request thật")

    args = parser.parse_args()
    load_env()

    jira_base = os.getenv("JIRA_BASE", "")
    jira_email = os.getenv("JIRA_EMAIL", "")
    jira_token = os.getenv("JIRA_TOKEN", "")
    jira_project = os.getenv("JIRA_PROJECT", "SCRUM")

    if not all([jira_base, jira_email, jira_token]):
        print("❌ Lỗi: Chưa cấu hình đầy đủ JIRA_BASE, JIRA_EMAIL, JIRA_TOKEN trong .env!")
        sys.exit(1)

    client = JiraSprintClient(jira_base, jira_email, jira_token, dry_run=args.dry_run)

    print("================================================================================")
    print("🏃 JIRA SPRINT AUTOMATION TOOL")
    print("================================================================================")
    print(f"🎯 Project Key:   {jira_project}")
    print(f"🌐 Jira Base URL: {jira_base}")
    if args.dry_run:
        print("🧪 Chế độ:       [DRY-RUN - Mô phỏng an toàn]")
    print("================================================================================\n")

    # 1. Tìm Scrum Board
    board = client.get_scrum_board(jira_project)
    if not board:
        print(f"❌ Không tìm thấy Scrum Board nào thuộc Project '{jira_project}'!")
        sys.exit(1)

    board_id = board.get("id")
    board_name = board.get("name")
    print(f"📋 Board: [ID: {board_id}] '{board_name}'\n")

    # 2. Xử lý liệt kê (--list)
    if args.list:
        print(f"🔍 Danh sách các Sprint trên Board ID {board_id}:")
        sprints = client.list_sprints(board_id)
        if not sprints:
            print("  (Chưa có Sprint nào)")
        for s in sprints:
            s_id = s.get("id")
            s_name = s.get("name")
            s_state = s.get("state")
            s_start = s.get("startDate", "N/A")
            s_end = s.get("endDate", "N/A")
            s_goal = s.get("goal", "")
            print(f"  👉 [ID: {s_id:2d}] {s_name} | Trạng thái: {s_state.upper()} | Bắt đầu: {s_start[:10]} | Kết thúc: {s_end[:10]}")
            if s_goal:
                print(f"     Mục tiêu: {s_goal}")
        print()

    # 3. Xử lý tạo Sprint mới (--create)
    target_sprint_id = args.sprint_id
    if args.create:
        print(f"🚀 Đang tạo Sprint mới: '{args.name}'...")
        print(f"   - Ngày bắt đầu:  {args.start}")
        print(f"   - Ngày kết thúc: {args.end}")
        print(f"   - Mục tiêu:      {args.goal}")

        ok, result = client.create_sprint(
            name=args.name,
            board_id=board_id,
            start_date=args.start,
            end_date=args.end,
            goal=args.goal
        )
        if ok:
            target_sprint_id = result.get("id")
            print(f"  ✅ ĐÃ TẠO SPRINT THÀNH CÔNG! Mã Sprint ID: {target_sprint_id}\n")
        else:
            print(f"  ❌ Lỗi khi tạo Sprint: {result}")
            sys.exit(1)

    # 4. Xử lý cập nhật Sprint (--update)
    if args.update:
        if not args.sprint_id:
            print("❌ Lỗi: Cần truyền --sprint-id <ID> để cập nhật Sprint!")
            sys.exit(1)
        print(f"🔄 Đang cập nhật Sprint ID {args.sprint_id}...")
        ok, result = client.update_sprint(
            sprint_id=args.sprint_id,
            name=args.name,
            start_date=args.start,
            end_date=args.end,
            goal=args.goal
        )
        if ok:
            print(f"  ✅ ĐÃ CẬP NHẬT SPRINT {args.sprint_id} THÀNH CÔNG!\n")
            target_sprint_id = args.sprint_id
        else:
            print(f"  ❌ Lỗi khi cập nhật Sprint: {result}")
            sys.exit(1)

    # 5. Xử lý gán issues vào Sprint
    issues_to_add = []
    if args.add_issues:
        issues_to_add.extend(args.add_issues)

    if args.from_cache:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        ref, key = parts[0].strip(), parts[1].strip()
                        # Chỉ gán các Task, không gán Epic
                        if ref not in ("T1", "QA1", "T2", "T3", "T0"):
                            issues_to_add.append(key)
            print(f"📂 Đã đọc {len(issues_to_add)} issue keys từ cache {CACHE_FILE}.")

    if target_sprint_id and issues_to_add:
        print(f"🏃 Đang gán {len(issues_to_add)} issues vào Sprint ID {target_sprint_id}...")
        ok, msg = client.add_issues_to_sprint(target_sprint_id, issues_to_add)
        if ok:
            print(f"  ✅ Đã gán thành công {len(issues_to_add)} issues vào Sprint ID {target_sprint_id}!")
        else:
            print(f"  ❌ Lỗi khi gán issues: {msg}")

    print("\n✨ Xử lý hoàn tất.")


if __name__ == "__main__":
    main()
