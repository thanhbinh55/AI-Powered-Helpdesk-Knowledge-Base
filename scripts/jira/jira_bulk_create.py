#!/usr/bin/env python3
"""
scripts/jira/jira_bulk_create.py
Kịch bản tự động tạo hàng loạt Jira issues từ file CSV (Jira Cloud REST API v3).
Hỗ trợ:
- Đọc biến môi trường từ .env hoặc os.environ (JIRA_BASE, JIRA_EMAIL, JIRA_TOKEN, JIRA_PROJECT)
- Đọc CSV cấu trúc: ref,type,summary,description,assignee_email,parent_ref,labels,duedate
- Ánh xạ parent_ref của Task vào mã Jira key của Epic vừa tạo
- Tra cứu accountId của người dùng qua email
- Chuyển đổi mô tả sang Atlassian Document Format (ADF)
- Chế độ chạy thử (--dry-run) không cần mạng hay gọi API thật
- Chống tạo trùng lặp bằng cache tasks_created.csv
- Tùy chọn --sprint-id để thêm các issue vừa tạo vào Sprint
"""

import os
import sys
import csv
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
    """Tự động nạp cấu hình từ .env nếu biến môi trường hệ thống chưa có."""
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


def text_to_adf(text):
    """Chuyển đổi chuỗi văn bản thường sang định dạng ADF (Atlassian Document Format) cho Jira API v3."""
    if not text:
        return {
            "version": 1,
            "type": "doc",
            "content": []
        }

    paragraphs = text.strip().split("\n")
    content = []
    for p in paragraphs:
        p_clean = p.strip()
        if p_clean:
            content.append({
                "type": "paragraph",
                "content": [{
                    "type": "text",
                    "text": p_clean
                }]
            })

    if not content:
        content.append({
            "type": "paragraph",
            "content": [{"type": "text", "text": ""}]
        })

    return {
        "version": 1,
        "type": "doc",
        "content": content
    }


def load_cached_created_tasks():
    """Nạp danh sách các ref đã tạo trước đó từ tasks_created.csv để tránh tạo trùng."""
    created_map = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    created_map[row[0].strip()] = row[1].strip()
    return created_map


def save_cached_task(ref, key):
    """Ghi thêm ref và Jira key vừa tạo vào tasks_created.csv."""
    with open(CACHE_FILE, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ref, key])


class JiraClient:
    def __init__(self, base_url, email, token, dry_run=False):
        self.base_url = base_url.rstrip("/")
        self.email = email
        self.token = token
        self.dry_run = dry_run
        self.user_cache = {}

        if not self.dry_run:
            self.auth_str = base64.b64encode(f"{self.email}:{self.token}".encode("utf-8")).decode("utf-8")

    def _request(self, method, endpoint, payload=None, params=None):
        url = f"{self.base_url}{endpoint}"

        if requests is not None:
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            try:
                res = requests.request(
                    method,
                    url,
                    auth=(self.email, self.token),
                    headers=headers,
                    json=payload,
                    params=params,
                    timeout=30
                )
                return res.status_code, res.text
            except Exception as e:
                return 0, str(e)
        else:
            # Fallback dùng thư viện chuẩn urllib nếu chưa cài requests
            if params:
                query_str = urllib.parse.urlencode(params)
                url = f"{url}?{query_str}"

            data_bytes = json.dumps(payload).encode("utf-8") if payload is not None else None
            req = urllib.request.Request(url, data=data_bytes, method=method)
            req.add_header("Authorization", f"Basic {self.auth_str}")
            req.add_header("Accept", "application/json")
            req.add_header("Content-Type", "application/json")

            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    return response.status, response.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                return e.code, e.read().decode("utf-8")
            except Exception as e:
                return 0, str(e)

    def find_account_id(self, email):
        """Tìm accountId của người dùng Jira theo địa chỉ email."""
        if not email or email.startswith("<"):
            return None

        if email in self.user_cache:
            return self.user_cache[email]

        if self.dry_run:
            simulated_id = f"acc-{abs(hash(email)) % 100000}"
            self.user_cache[email] = simulated_id
            return simulated_id

        status, body = self._request("GET", "/rest/api/3/user/search", params={"query": email})
        if status == 200:
            try:
                users = json.loads(body)
                if users and isinstance(users, list):
                    account_id = users[0].get("accountId")
                    self.user_cache[email] = account_id
                    return account_id
            except json.JSONDecodeError:
                pass

        print(f"  ⚠️ Không tìm thấy accountId cho email: {email} (HTTP {status})")
        return None

    def create_issue(self, project_key, issue_type, summary, description, parent_key=None, labels=None, duedate=None, assignee_id=None):
        """Tạo issue mới trên Jira Cloud API v3."""
        if self.dry_run:
            simulated_key = f"{project_key}-{100 + len(self.user_cache) + 1}"
            return True, simulated_key

        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": text_to_adf(description),
                "issuetype": {"name": issue_type}
            }
        }

        if parent_key:
            payload["fields"]["parent"] = {"key": parent_key}

        if labels:
            label_list = [l.strip() for l in labels.split(";") if l.strip()]
            if label_list:
                payload["fields"]["labels"] = label_list

        if duedate:
            payload["fields"]["duedate"] = duedate

        if assignee_id:
            payload["fields"]["assignee"] = {"accountId": assignee_id}

        status, body = self._request("POST", "/rest/api/3/issue", payload=payload)
        if status in (200, 201):
            try:
                data = json.loads(body)
                return True, data.get("key")
            except Exception:
                return True, "UNKNOWN-KEY"
        else:
            return False, f"HTTP {status}: {body}"

    def add_issues_to_sprint(self, sprint_id, issue_keys):
        """Gán danh sách issue vào Sprint theo Sprint ID."""
        if not issue_keys:
            return True, "No issues to add"

        if self.dry_run:
            print(f"  [DRY-RUN] Giả lập thêm các issues {issue_keys} vào Sprint ID {sprint_id}.")
            return True, "Dry-run sprint success"

        endpoint = f"/rest/agile/1.0/sprint/{sprint_id}/issue"
        payload = {"issues": issue_keys}
        status, body = self._request("POST", endpoint, payload=payload)
        if status in (200, 204):
            return True, "Sprint updated"
        else:
            return False, f"HTTP {status}: {body}"


def main():
    parser = argparse.ArgumentParser(description="Tạo hàng loạt task/epic trên Jira từ file CSV.")
    parser.add_argument("--csv", default=os.path.join(os.path.dirname(__file__), "tasks_template0.csv"),
                        help="Đường dẫn tới file CSV chứa danh sách task")
    parser.add_argument("--dry-run", action="store_true",
                        help="Chạy thử nghiệm mô phỏng, không gửi request thật lên Jira")
    parser.add_argument("--sprint-id", type=str, default=None,
                        help="ID của Sprint cần gán các issue sau khi tạo")
    args = parser.parse_args()

    load_env()

    jira_base = os.getenv("JIRA_BASE", "")
    jira_email = os.getenv("JIRA_EMAIL", "")
    jira_token = os.getenv("JIRA_TOKEN", "")
    jira_project = os.getenv("JIRA_PROJECT", "SCRUM")

    print("================================================================================")
    print("🚀 JIRA BULK ISSUE CREATOR (Jira Cloud REST API v3)")
    print("================================================================================")
    print(f"📄 File dữ liệu CSV: {args.csv}")
    print(f"🎯 Project Key:      {jira_project}")
    print(f"🌐 Jira Base URL:    {jira_base if jira_base else '(chưa cấu hình)'}")
    print(f"👤 Jira Account:     {jira_email if jira_email else '(chưa cấu hình)'}")
    print(f"🧪 Chế độ hoạt động: {'[DRY-RUN - Chạy thử mô phỏng]' if args.dry_run else '[LIVE - Tạo thực tế trên Jira]'}")
    print("================================================================================\n")

    if not args.dry_run:
        missing = []
        if not jira_base or "your-domain" in jira_base:
            missing.append("JIRA_BASE")
        if not jira_email or "your_email" in jira_email:
            missing.append("JIRA_EMAIL")
        if not jira_token or "your_atlassian" in jira_token:
            missing.append("JIRA_TOKEN")

        if missing:
            print(f"❌ LỖI CẤU HÌNH: Thiếu hoặc chưa điền thông tin hợp lệ cho các biến: {', '.join(missing)}")
            print("💡 Hãy cập nhật các biến này trong file .env hoặc sử dụng cờ --dry-run để chạy kiểm tra thử.")
            sys.exit(1)

    if not os.path.exists(args.csv):
        print(f"❌ Lỗi: Không tìm thấy file CSV tại {args.csv}")
        sys.exit(1)

    cached_tasks = load_cached_created_tasks()
    ref_to_key = dict(cached_tasks)

    client = JiraClient(jira_base, jira_email, jira_token, dry_run=args.dry_run)

    tasks_to_create = []
    with open(args.csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks_to_create.append(row)

    print(f"📋 Đã đọc {len(tasks_to_create)} dòng từ CSV.\n")

    created_in_this_run = []
    sim_counter = 1

    for row in tasks_to_create:
        ref = row.get("ref", "").strip()
        issue_type = row.get("type", "Task").strip()
        summary = row.get("summary", "").strip()
        description = row.get("description", "").strip()
        assignee_email = row.get("assignee_email", "").strip()
        parent_ref = row.get("parent_ref", "").strip()
        labels = row.get("labels", "").strip()
        duedate = row.get("duedate", "").strip()

        print(f"👉 Xử lý [{ref}] ({issue_type}): {summary}")

        if ref in ref_to_key:
            existing_key = ref_to_key[ref]
            print(f"  ⏭️ [BỎ QUA] Đã tồn tại trong cache với mã: {existing_key}")
            continue

        parent_key = None
        if parent_ref:
            if parent_ref in ref_to_key:
                parent_key = ref_to_key[parent_ref]
            else:
                print(f"  ⚠️ Cảnh báo: Không tìm thấy key của parent_ref [{parent_ref}]. Tạo issue không có parent.")

        account_id = None
        if assignee_email:
            account_id = client.find_account_id(assignee_email)

        if args.dry_run:
            sim_key = f"{jira_project}-{sim_counter}"
            sim_counter += 1
            ref_to_key[ref] = sim_key
            created_in_this_run.append(sim_key)
            parent_info = f" (Parent: {parent_key})" if parent_key else ""
            assignee_info = f" (Assignee: {assignee_email})" if assignee_email else ""
            print(f"  ✅ [DRY-RUN] {ref} -> {sim_key}{parent_info}{assignee_info}")
        else:
            success, result = client.create_issue(
                project_key=jira_project,
                issue_type=issue_type,
                summary=summary,
                description=description,
                parent_key=parent_key,
                labels=labels,
                duedate=duedate,
                assignee_id=account_id
            )

            if success:
                new_key = result
                print(f"  🎉 Thành công: {ref} -> {new_key}")
                ref_to_key[ref] = new_key
                save_cached_task(ref, new_key)
                created_in_this_run.append(new_key)
            else:
                print(f"  ❌ THẤT BẠI khi tạo [{ref}]: {result}")
                print("  ➡️ Tiếp tục xử lý các dòng tiếp theo...")

    print("\n--------------------------------------------------------------------------------")
    print(f"📊 Tổng kết: Đã tạo {len(created_in_this_run)} issue(s) trong lượt chạy này.")

    if args.sprint_id:
        print(f"\n🏃 Đang gán các issue vào Sprint ID: {args.sprint_id}...")
        s_ok, s_msg = client.add_issues_to_sprint(args.sprint_id, created_in_this_run)
        if s_ok:
            print("  ✅ Đã thêm thành công các issue vào Sprint!")
        else:
            print(f"  ❌ Lỗi khi thêm issue vào Sprint: {s_msg}")

    print("================================================================================")
    print("✨ Kết thúc quá trình xử lý Jira Bulk Create.")


if __name__ == "__main__":
    main()
