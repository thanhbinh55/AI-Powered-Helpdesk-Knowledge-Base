import os
import re

submit_dir = "reports/submit"

print("=== 1. KIỂM TRA ĐƯỜNG DẪN CỤC BỘ FILE:/// VÀ LINK BỊ HỎNG ===")
for root, dirs, files in os.walk(submit_dir):
    for f in files:
        if f.endswith(('.md', '.html')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            if 'file://' in content:
                print(f"[CẢNH BÁO] Có file:// trong: {path}")
            if 'reports/' in content and not 'reports/assets/' in content:
                # check if there are lingering reports/ file links
                matches = re.findall(r'\[.*?\]\((reports/[^\)]+)\)', content)
                if matches:
                    print(f"[CẢNH BÁO] Có link relative reports/ trong {path}: {matches}")

print("-> Kiểm tra đường dẫn cục bộ: HOÀN TẤT.")

print("\n=== 2. KIỂM TRA ĐỐI SOÁT AI-USAGE (MD vs HTML) ===")
with open(f"{submit_dir}/ai-usage/ai-usage.md", "r") as f:
    ai_md = f.read()
with open(f"{submit_dir}/ai-usage/ai-usage.html", "r") as f:
    ai_html = f.read()

md_sessions = re.findall(r'Phiên ghi nhận #(\d+)', ai_md)
html_sessions = re.findall(r'Phiên ghi nhận #(\d+)', ai_html)
print(f"Số phiên ghi nhận trong MD: {len(md_sessions)} -> {md_sessions}")
print(f"Số phiên ghi nhận trong HTML: {len(html_sessions)} -> {html_sessions}")
assert md_sessions == html_sessions, "Lệch số phiên AI!"

# Check date session 11
md_s11_date = "19h30 ngày 28/10/2026" in ai_md
html_s11_date = "19h30 ngày 28/10/2026" in ai_html
print(f"Phiên #11 ngày 19h30 28/10/2026: MD={md_s11_date}, HTML={html_s11_date}")

# Check MLA/MIT references removed
for banned in ["MLA Style Center", "MIT Libraries", "Harvard Library"]:
    assert banned not in ai_md, f"Vẫn còn {banned} trong ai-usage.md"
    assert banned not in ai_html, f"Vẫn còn {banned} trong ai-usage.html"
print("Xác nhận đã loại bỏ triệt để tài liệu nước ngoài (MLA, MIT, Harvard).")

print("\n=== 3. KIỂM TRA ĐỐI SOÁT GIT-CONTRIBUTIONS (MD vs HTML) ===")
with open(f"{submit_dir}/git-contributions/git-contributions.md", "r") as f:
    git_md = f.read()
with open(f"{submit_dir}/git-contributions/git-contributions.html", "r") as f:
    git_html = f.read()

md_hashes = re.findall(r'\[([0-9a-f]{8})\]', git_md)
html_hashes = re.findall(r'\[([0-9a-f]{8})\]', git_html)
print(f"Số commit hash trong MD: {len(md_hashes)}")
print(f"Số commit hash trong HTML: {len(html_hashes)}")
assert len(md_hashes) == 39, f"Kỳ vọng 39 hashes trong MD, thấy {len(md_hashes)}"
assert len(html_hashes) >= 39, f"Kỳ vọng >= 39 hashes trong HTML, thấy {len(html_hashes)}"

# Check git log matching
import subprocess
git_log_8chars = [c[:8] for c in subprocess.check_output(['git', 'log', '--format=%H'], text=True).strip().split('\n')]
found = sum(1 for h in md_hashes if h in git_log_8chars)
print(f"Đối soát Git log: Tìm thấy {found}/{len(md_hashes)} commit hash chính xác 100% trong git log repo!")
assert found == len(md_hashes), "Có commit hash không khớp với git log!"

print("\n=== 4. KIỂM TRA ĐỐI SOÁT PROJECT-PROPOSAL (MD vs HTML) ===")
with open(f"{submit_dir}/project-proposal/project-proposal.md", "r") as f:
    prop_md = f.read()
with open(f"{submit_dir}/project-proposal/project-proposal.html", "r") as f:
    prop_html = f.read()

# Check 30 Functional Requirements
stt_md = re.findall(r'\|\s*(\d+)\s*\|\s*Là [^\|]+\|\s*[^\|]+', prop_md)
stt_html = re.findall(r'<td class="align-center">(\d+)</td>\s*<td class="align-left">Là [^<]+</td>', prop_html)
print(f"Số chức năng nghiệp vụ trong MD: {len(stt_md)} (STT: {stt_md[0]} -> {stt_md[-1]})")
print(f"Số chức năng nghiệp vụ trong HTML: {len(stt_html)} (STT: {stt_html[0]} -> {stt_html[-1]})")
assert len(stt_md) == 30, f"Kỳ vọng 30 chức năng trong MD, thấy {len(stt_md)}"
assert len(stt_html) == 30, f"Kỳ vọng 30 chức năng trong HTML, thấy {len(stt_html)}"

# Check modules in 3.1.2 capitalized
for mod in ["Identity", "Ticket", "Knowledge", "AI"]:
    assert f"Module `{mod}`" in prop_md or f"Module {mod}" in prop_md, f"Thiếu Module {mod} trong MD"
    assert f"Module <code>{mod}</code>" in prop_html or f"Module {mod}" in prop_html, f"Thiếu Module {mod} trong HTML"
print("Xác nhận Module Identity, Ticket, Knowledge, AI đã viết hoa đúng chuẩn.")

# Check Section 4.3 & 4.5 titles
assert "4.3. Cài đặt (implement) phần mềm" in prop_md
assert "4.3. Cài đặt (implement) phần mềm" in prop_html
assert "4.5. Triển khai, bảo trì" in prop_md
assert "4.5. Triển khai, bảo trì" in prop_html
print("Xác nhận tiêu đề mục 4.3 và 4.5 đúng 100% template.")

# Check Cost table: 47.840.000
assert "47.840.000" in prop_md
assert "47.840.000" in prop_html
print("Xác nhận bảng chi phí 47.840.000 VNĐ có mặt đầy đủ trong MD và HTML.")

print("\n=== 5. KIỂM TRA TYPOGRAPHY & CSS TRONG HTML ===")
for h_file in ["project-proposal/project-proposal.html", "ai-usage/ai-usage.html", "git-contributions/git-contributions.html"]:
    path = f"{submit_dir}/{h_file}"
    with open(path, "r") as f:
        html_code = f.read()
    assert "Times New Roman" in html_code, f"Thiếu Times New Roman trong {path}"
    # check no border-left blue on blockquote or cover-meta-box
    assert "border-left: 4px solid #548dd4" not in html_code, f"Vẫn còn viền xanh trái trong {path}"
    assert "border-left: 3px solid #548dd4" not in html_code, f"Vẫn còn viền xanh trái 3px trong {path}"
    print(f"File {h_file}: Typography Times New Roman đạt chuẩn, không có viền xanh cạnh trái.")

print("\n>>> TẤT CẢ CÁC BƯỚC KIỂM TRA ĐỀU PASS 100%! <<<")
