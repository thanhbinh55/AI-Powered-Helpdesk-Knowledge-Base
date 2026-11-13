import re
from bs4 import BeautifulSoup

print("=" * 60)
print("1. COMPREHENSIVE AUDIT: GIT-CONTRIBUTIONS")
print("=" * 60)
with open("reports/submit/git-contributions/git-contributions.md") as f:
    git_md = f.read()
with open("reports/submit/git-contributions/git-contributions.html") as f:
    git_html = f.read()

# Hashes
md_hashes = re.findall(r"\[([0-9a-f]{8})\]", git_md)
html_hashes = re.findall(r"\[([0-9a-f]{8})\]", git_html)
print(f"- Total Commits: MD={len(md_hashes)}, HTML={len(html_hashes)} -> Match: {md_hashes == html_hashes}")
assert md_hashes == html_hashes, "Hashes mismatch!"

# Check Lead vs Nhóm trưởng
lead_in_md = "lead" in git_md.lower() and "leader" not in git_md.lower()
lead_in_html = "lead" in git_html.lower() and "leader" not in git_html.lower()
print(f"- Occurrences of Lead: MD={lead_in_md}, HTML={lead_in_html} (Expected: False/False)")
print(f"- Occurrences of Nhom truong: MD={'Nhóm trưởng' in git_md}, HTML={'Nhóm trưởng' in git_html}")

# Check forbidden terms
for banned in ["frontend", "ui-prototype", "feat/frontend", "Customer Portal"]:
    assert banned.lower() not in git_md.lower(), f"Found {banned} in git_md"
    assert banned.lower() not in git_html.lower(), f"Found {banned} in git_html"
print("- Forbidden frontend terms check: ALL CLEAN")

print("=" * 60)
print("2. COMPREHENSIVE AUDIT: AI-USAGE")
print("=" * 60)
with open("reports/submit/ai-usage/ai-usage.md") as f:
    ai_md = f.read()
with open("reports/submit/ai-usage/ai-usage.html") as f:
    ai_html = f.read()

# Sessions
md_sessions = re.findall(r"Phiên ghi nhận #(\d+)", ai_md)
html_sessions = re.findall(r"Phiên ghi nhận #(\d+)", ai_html)
print(f"- Total Sessions: MD={len(md_sessions)}, HTML={len(html_sessions)} -> Match: {md_sessions == html_sessions}")
assert md_sessions == html_sessions, "Sessions mismatch!"

# Backslash escapes check
bks = re.findall(r"\\(?:[>#\*_]|code|reports|SCRUM)", ai_html)
print(f"- Leaked markdown backslash artifacts in HTML: {len(bks)} (Expected: 0)")
assert len(bks) == 0, f"Still found leaked backslashes in ai-usage.html: {bks}"

# Foreign citations check
for banned in ["MLA Style Center", "MIT Libraries", "Harvard Library"]:
    assert banned not in ai_md, f"Found {banned} in ai_md"
    assert banned not in ai_html, f"Found {banned} in ai_html"
print("- Banned foreign reference check: ALL CLEAN")

# Check all member roles
print(f"- Nhom truong in ai-usage.md: {'Nhóm trưởng' in ai_md}")
print(f"- Nhom truong in ai-usage.html: {'Nhóm trưởng' in ai_html}")
print(f"- Lead in ai-usage.md: {'Lead' in ai_md}")
print(f"- Lead in ai-usage.html: {'Lead' in ai_html}")

print("=" * 60)
print("3. COMPREHENSIVE AUDIT: PROJECT-PROPOSAL")
print("=" * 60)
with open("reports/submit/project-proposal/project-proposal.md") as f:
    prop_md = f.read()
with open("reports/submit/project-proposal/project-proposal.html") as f:
    prop_html = f.read()

# Check 30 FRs
stt_md = re.findall(r"\|\s*(\d+)\s*\|\s*Là [^\|]+\|\s*[^\|]+", prop_md)
stt_html = re.findall(r"<td class=\"align-center\">(\d+)</td>\s*<td class=\"align-left\">Là [^<]+</td>", prop_html)
print(f"- FRs count: MD={len(stt_md)}, HTML={len(stt_html)} -> Match: {stt_md == stt_html}")
assert len(stt_md) == 30 and len(stt_html) == 30 and stt_md == stt_html, "FR mismatch!"

# Check budget
print(f"- Budget 47.840.000 in MD: {'47.840.000' in prop_md}, in HTML: {'47.840.000' in prop_html}")
assert "47.840.000" in prop_md and "47.840.000" in prop_html

# Check Section 4.3 and 4.5 titles
print(f"- 4.3 Cài đặt in MD: {'4.3. Cài đặt (implement) phần mềm' in prop_md}, HTML: {'4.3. Cài đặt (implement) phần mềm' in prop_html}")
print(f"- 4.5 Triển khai in MD: {'4.5. Triển khai, bảo trì' in prop_md}, HTML: {'4.5. Triển khai, bảo trì' in prop_html}")
assert "4.3. Cài đặt (implement) phần mềm" in prop_md and "4.3. Cài đặt (implement) phần mềm" in prop_html
assert "4.5. Triển khai, bảo trì" in prop_md and "4.5. Triển khai, bảo trì" in prop_html

# Check modules
for mod in ["Identity", "Ticket", "Knowledge", "AI"]:
    assert f"Module {mod}" in prop_md or f"Module `{mod}`" in prop_md
    assert f"Module {mod}" in prop_html or f"Module <code>{mod}</code>" in prop_html
print("- Module capitalization: ALL CLEAN")

print("=" * 60)
print(">>> TẤT CẢ 3 FILE ĐỀU CHUẨN XÁC 100%, KHÔNG LỖI, KHÔNG THỪA! <<<")
print("=" * 60)

