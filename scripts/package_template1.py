#!/usr/bin/env python3
"""Build the Template 1 hand-in without editing the final report's wording.

Usage: python3 scripts/package_template1.py
Requires Python-Markdown. Uses pinned member snapshots in reports/template1/sources.
The PDF is exported by the team leader from Google Docs, outside this pipeline.
"""
import csv
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import markdown

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
sys.path.insert(0,str(ROOT/'scripts/template1'))
from diagrams import generate, BASELINES
import render_ai_usage_template0 as template0

T1=ROOT/'reports/template1'
SOURCES=T1/'sources'
REPO='https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base'
DATE='12/11/2026'
UI=['62-8214','62-8215','62-8328','62-10225','62-10226','62-13238',
    '58-6763','58-6764','58-6765','62-6953','62-6954','55-1992','55-2537','56-3104',
    '62-9092','62-9094','62-9240','62-9241','62-9783','55-1994','56-3578','62-9943',
    '62-9944','62-9945','81-7585','81-8707','thanh-phan/81-7560','82-10422',
    '91-15641','91-15904','91-19910']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8')


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()


def report_body(text):
    return re.split(r'^\[image\d+\]:',text,flags=re.M)[0].rstrip()


def content_fingerprint(text):
    """Formatting-insensitive comparison; keeps every prose/table word in order."""
    text=report_body(text)
    text=re.sub(r'!\[.*?\](?:\[image\d+\]|\([^\n]*?\))','',text)
    text=re.sub(r' \{#[^\n]+\}','',text)
    text=re.sub(r'<a id="[^"]*"></a>','',text)
    # Markdown markers and whitespace carry formatting, not report wording.
    return re.sub(r'[\s*#]+','',text)


def build_report():
    raw=(SOURCES/'template1-final-original.md').read_text()
    body=report_body(raw)
    refs=['assets/diagrams/context_diagram_system.svg']+['assets/diagrams/'+a+'.svg' for a in BASELINES]
    refs += ['assets/ui/'+Path(a).name+'.png' for a in UI]
    assert len(refs)==37
    manifest=[]
    for i,ref in enumerate(refs,1):
        match=re.search(r'!\[\]\[image'+str(i)+r'\]',body)
        assert match, f'Missing image{i}'
        caption=re.search(r'Hình [^\n]+',body[match.end():]).group(0).strip('* ')
        source_path=None
        if i>=7:
            source_path='docs/design/anh/'+UI[i-7]+'.png'
            src=ROOT/source_path;dest=T1/'report'/ref
            dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
        manifest.append({'reference':f'image{i}','caption':caption,'asset':ref,'source':source_path,
                         'sha256':sha((T1/'report'/ref).read_bytes())})
    # Correct an export layout artifact: the ticket diagram was embedded in its heading.
    body=re.sub(r'^(### [^\n]*?)!\[\]\[image4\](\*\*[^\n]*)$',r'\1\2\n\n![][image4]',body,flags=re.M)
    # Remove emphasis around image-only lines, which otherwise wraps HTML paragraphs.
    body=re.sub(r'^\*+(!\[\]\[image\d+\])\*+$',r'\1',body,flags=re.M)
    for i,ref in enumerate(refs,1):
        body=body.replace(f'![][image{i}]',f'![]({ref})')
    body=re.sub(r'^#+\s*$', '',body,flags=re.M)
    # Standard HTML anchors work in Markdown viewers; exported {#...} syntax does not.
    def heading(m):
        ident=re.sub(r'\\([()\[\]])',r'\1',m[2])
        return '<a id="'+html.escape(ident,quote=True)+'"></a>\n\n'+m[1]
    body=re.sub(r'^(#{1,6} [^\n]+?) \{#([^\n]+)\}$',heading,body,flags=re.M)
    body=re.sub(r'\n{3,}','\n\n',body).strip()+'\n'
    assert content_fingerprint(raw)==content_fingerprint(body), 'Report wording changed'
    write(T1/'report/report.md',body)
    write(T1/'report/assets/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest


def extract_sessions(text):
    start=text.index('## 6.3');end=text.index('## 6.4')
    blocks=re.split(r'(?=^### Phiên )',text[start:end],flags=re.M)[1:]
    return blocks


def build_ai():
    owners=[('binh','Ngô Viết Thanh Bình','24120269'),('lam','Nguyễn Đức Lãm','24120083'),('quy-phuc','Lê Quý Phúc','24120121'),('gia-phuc','Phan Gia Phúc','24120503')]
    baseline=(SOURCES/'ai-usage-binh.md').read_text()
    # Preserve the common rules and every owner-specific row/session verbatim.
    prefix=baseline[:baseline.index('## 6.2')]
    out=['# BÁO CÁO SỬ DỤNG AI — TEMPLATE 1\n\n',prefix,
         '## Hồ sơ sử dụng AI theo thành viên\n\n']
    index=[]
    table_header='\n'.join(l for l in baseline.splitlines() if l.startswith('| STT |') or l.startswith('| :---: |'))
    for key,name,mssv in owners:
        text=(SOURCES/f'ai-usage-{key}.md').read_text()
        rows=[l for l in text.splitlines() if l.startswith('|') and mssv in l]
        blocks=[b for b in extract_sessions(text) if mssv in b]
        out += [f'## {name} — {mssv}\n\n',table_header+'\n'+'\n'.join(rows)+'\n\n', ''.join(blocks)]
        if not blocks:
            out.append('**Tình trạng hồ sơ:** Đã có dòng tổng hợp do tác giả nộp; chưa có phần chi tiết phiên ở mục 6.3 trong nguồn. Giữ nguyên nội dung đã nộp, không bổ sung prompt hoặc xác nhận kiểm chứng thay tác giả.\n\n')
        index.append({'author':name,'mssv':mssv,'summary_rows':len(rows),'detailed_sessions':len(blocks),'source':f'sources/ai-usage-{key}.md'})
        for block in blocks:
            assert block in ''.join(out)
    out += ['## Ngô Viết Thanh Bình — Phiên đóng gói Template 1\n\n',
            '### Phiên T1-PACK-01: Tổng hợp gói nộp Template 1\n\n',
            '- **Thời gian:** 12/11/2026; không ghi nhận giờ bắt đầu cụ thể.\n',
            '- **Tác giả chịu trách nhiệm:** Ngô Viết Thanh Bình — `24120269`.\n',
            '- **Công cụ / Model:** Codex, OpenAI; không ghi nhận model cụ thể.\n',
            '- **Prompt đã khử dữ liệu nhạy cảm:** Tổng hợp bản Markdown final, thay hình nhúng mờ bằng assets đúng mã, điều chỉnh sơ đồ theo bản final, tổng hợp Git contributions và AI usage như Template 0, giữ nguyên nội dung gốc và làm trên nhánh `merge-template1`.\n',
            '- **Nội dung AI tạo / áp dụng:** Công cụ đóng gói, ánh xạ 37 hình, 6 sơ đồ vector cùng nguồn drawio, bản Markdown và HTML của nhật ký AI và đóng góp Git.\n',
            '- **Kiểm chứng:** Đối chiếu tự động toàn bộ chữ của report với nguồn; so sánh ảnh theo mã và ảnh thu nhỏ; kiểm tra nguồn và số phiên theo từng tác giả, SHA commit, đường dẫn assets, HTML và bố cục qua trình duyệt. Chưa có xác nhận review của tác giả/reviewer; không xác nhận nghiệm thu thay thành viên. Nội dung tự kiểm chứng ở các phiên cũ được giữ theo nguồn, chưa được xác minh độc lập.\n',
            '- **Minh chứng:** `report/report.md`, `report/assets/manifest.json`, `git-contributions/git-contributions.md`, `sources/`, nhánh `merge-template1`; task `T1-PUB-01` / `SCRUM-41` và `T1-SUBMIT-01` / `SCRUM-52` (đối chiếu bảng ánh xạ task cục bộ).\n\n---\n\n',
            baseline[baseline.index('## 6.4'):].replace('ĐHKHTN:\n1.', 'ĐHKHTN:\n\n1.')]
    combined=''.join(out)
    for key,name,mssv in owners:
        t=(SOURCES/f'ai-usage-{key}.md').read_text()
        for row in [l for l in t.splitlines() if l.startswith('|') and mssv in l]:assert row in combined
        for block in [b for b in extract_sessions(t) if mssv in b]:assert block in combined
    write(T1/'ai-usage/ai-usage.md',combined)
    return index


def capture_git_snapshot():
    path=SOURCES/'git-snapshot.json'
    if path.exists():return json.loads(path.read_text())
    members=list(csv.DictReader((ROOT/'members.csv').open()))
    refs=['origin/main','origin/docs/t1-identity-binh','origin/docs/t1-knowledge-lam','origin/docs/t1-ai-quyphuc-markdown','origin/docs/t1-ticket-giaphuc']
    pinned={ref:git('rev-parse',ref) for ref in refs}
    hashes=git('log','--since=2026-11-03T00:00:00+07:00','--format=%H',*pinned.values()).splitlines()
    records=[]
    for h in hashes:
        fields=git('show','-s','--format=%H%x00%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI%x00%s%x00%P',h).split('\0')
        if 'template0' in fields[7].lower():continue
        files=git('diff-tree','--root','--no-commit-id','--name-only','-r',h).splitlines()
        if len(fields[8].split())>1:
            files=git('diff','--name-only',fields[8].split()[0],h).splitlines()
        records.append(dict(zip(['sha','author','author_email','authored_at','committer','committer_email','committed_at','subject','parents'],fields),files=files,
                            refs=[ref for ref,tip in pinned.items() if subprocess.run(['git','merge-base','--is-ancestor',h,tip],cwd=ROOT).returncode==0]))
    prs=json.loads(subprocess.check_output(['gh','pr','list','--repo','thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base','--state','all','--limit','50','--json','number,title,headRefName,state,author,url,mergedAt'],text=True))
    snapshot={'captured_at':datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds'),
              'period_start':'2026-11-03T00:00:00+07:00','refs':pinned,'members':members,'commits':records,'pull_requests':prs}
    write(path,json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
    return snapshot


def build_git():
    snapshot=capture_git_snapshot();commits=snapshot['commits'];members=snapshot['members']
    lines=['# BÁO CÁO LỊCH SỬ COMMIT GIT — TEMPLATE 1\n\n',
           f'> **Dự án:** Clarune — AI-Powered Helpdesk & Knowledge Base\n> **Nhóm:** Group 04\n> **Kho lưu trữ:** {REPO}\n> **Thời điểm chốt dữ liệu:** {snapshot["captured_at"]}\n\n',
           '## Phạm vi và nguồn đối chiếu\n\n',
           'Thống kê lịch sử của giai đoạn Template 1 từ 03/11/2026 đến thời điểm chốt dữ liệu, gồm chuẩn bị yêu cầu, prototype và bản Markdown đã đẩy lên remote. Hợp các commit từ những nhánh dưới đây theo SHA, mỗi commit chỉ tính một lần. Loại commit lưu trữ Template 0; không đưa commit đóng gói sau snapshot vào số liệu này. Giữ nguyên tên tác giả, thông điệp và thời gian đã ghi trong Git.\n\n',
           '| Nhánh nguồn | SHA tại thời điểm chốt |\n| --- | --- |\n']
    for ref,h in snapshot['refs'].items():lines.append(f'| `{ref}` | [{h}]({REPO}/commit/{h}) |\n')
    lines += ['\nChỉ số commit phản ánh lịch sử Git, không tương đương phần trăm công sức hay xác nhận đã hoàn thành nhiệm vụ. Commit trên nhánh chưa merge vẫn được ghi nhận và đánh dấu nguồn. Metadata/đường dẫn đầy đủ được giữ tại `../sources/git-snapshot.json`. Đối chiếu tác giả bằng tên GitHub hoặc email Git/Jira đã khai báo trong members.csv; Gia Phúc dùng tác giả PC với email phgphuc0609@gmail.com, trùng email Jira đã khai báo.\n\n',
              '## Bảng tổng hợp\n\n| MSSV | Thành viên | GitHub | Commit |\n| --- | --- | --- | ---: |\n']
    grouped={}
    for m in members:
        own=[c for c in commits if c['author_email'].lower() in {m['git_email'].lower(), m['jira_email'].lower()} or c['author'].lower()==m['git_username'].lower()]
        own.sort(key=lambda c:(c['authored_at'],c['sha']),reverse=True)
        grouped[m['mssv']]=own
        lines.append(f'| {m["mssv"]} | {m["full_name"]} | {m["git_username"]} | {len(own)} |\n')
    assigned={c['sha'] for v in grouped.values() for c in v};assert assigned=={c['sha'] for c in commits},'Unmapped or omitted author'
    lines += ['\n## DANH SÁCH COMMIT CỦA MỖI THÀNH VIÊN\n\n']
    for i,m in enumerate(members,1):
        own=grouped[m['mssv']]
        lines += [f'### {i}. Thành viên: {m["mssv"]} - {m["git_username"]} ({m["full_name"]})\n\n',
                  f'- **Họ và tên:** {m["full_name"]}\n- **Mã số sinh viên:** `{m["mssv"]}`\n- **Tài khoản Git:** `{m["git_username"]}`\n- **Email Git:** `{m["git_email"]}`\n- **Module phụ trách:** {m["role_module"]}\n- **Tổng số commit ghi nhận:** {len(own)}\n\n']
        if not own:
            lines.append('Chưa tìm thấy commit của thành viên trong phạm vi Template 1 trên các nhánh nguồn đã kiểm tra. Không suy diễn về phần làm ngoài Git hoặc trên Google Docs.\n\n');continue
        lines.append('| STT | Mã Hash | Ngày commit (UTC+7) | Thông điệp commit (Jira Key) | Số tệp |\n| ---: | --- | --- | --- | ---: |\n')
        for j,c in enumerate(own,1):
            when=datetime.fromisoformat(c['authored_at']).astimezone(ZoneInfo('Asia/Ho_Chi_Minh')).strftime('%d/%m/%Y %H:%M')
            subject=c['subject'].replace('|','&#124;')
            lines.append(f'| {j} | [{c["sha"][:8]}]({REPO}/commit/{c["sha"]}) | {when} | {subject} | {len(c["files"])} |\n')
        lines.append('\n#### Tệp thay đổi và nguồn nhánh\n\n')
        for c in own:
            lines += [f'**[{c["sha"][:8]}]({REPO}/commit/{c["sha"]})** — {c["subject"]}\n\n',
                      'Nguồn: '+', '.join('`'+r+'`' for r in c['refs'])+'.\n\n']
            if c['files']:lines.append('\n'.join('- `'+f+'`' for f in c['files'])+'\n\n')
            else:lines.append('Merge commit / không có tệp thay đổi trực tiếp.\n\n')
    lines.append('## Pull Request liên quan\n\n| PR | Nội dung | Nhánh | Trạng thái tại thời điểm chốt |\n| --- | --- | --- | --- |\n')
    for p in snapshot['pull_requests']:
        if p['headRefName'].startswith('docs/t1-') or p['number']==8:
            lines.append(f'| [#{p["number"]}]({p["url"]}) | {p["title"]} | `{p["headRefName"]}` | {p["state"]} |\n')
    write(T1/'git-contributions/git-contributions.md',''.join(lines))
    return {m['full_name']:len(grouped[m['mssv']]) for m in members}


# Reuse Template 0 cover, typography, A4 headers/footers and continuous paginator.
# Parse the full input using a standard Markdown implementation; the old renderers
# contained specific Template 0 session and commit hashes and cannot be reused as-is.
def render_companion(kind,title,subtitle):
    folder=T1/kind;md=(folder/(kind+'.md')).read_text()
    logo=ROOT/'reports/template0'/kind/'hcmus_logo.png'
    shutil.copy2(logo,folder/'hcmus_logo.png')
    template0.LOGO_PNG=str(folder/'hcmus_logo.png')
    cover=template0.render_cover_page()
    cover=cover.replace('AI Usage Report',title).replace('Báo cáo Sử dụng Trí tuệ Nhân tạo (AI Usage Transparency &amp; Accountability Report)',subtitle)
    cover=cover.replace('28/10/2026',DATE).replace('Đề tài đề xuất:','Đề tài:')
    cover=cover.replace('Ghi nhận minh bạch toàn bộ quá trình sử dụng các công cụ Trí tuệ nhân tạo (LLM, AI Coding Assistant, Prompt-based generators) trong đồ án theo đúng quy chuẩn bắt buộc của Khoa CNTT - HCMUS.',
                        'Ghi nhận '+('việc sử dụng AI' if kind=='ai-usage' else 'lịch sử Git và bằng chứng đóng góp cá nhân')+' trong giai đoạn Template 1. Nguồn và giới hạn đối chiếu được trình bày đầy đủ trong nội dung báo cáo.')
    cover=cover.replace('Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS',
                        'Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS' if kind=='ai-usage' else 'Đối soát lịch sử Git và truy vết đóng góp cá nhân')
    cover=cover.replace('NMCNPM - AI-Powered Helpdesk &amp; Knowledge Base - Group 04','NMCNPM - Clarune - Group 04 | Template 1')
    body=markdown.markdown(md,extensions=['tables','fenced_code','sane_lists'],output_format='html5',tab_length=2)
    # Resolve links to archived source snapshots so the deliverable works offline.
    body=body.replace('`../sources/git-snapshot.json`','../sources/git-snapshot.json')
    def columns(match):
        table=match[0];head=table.split('</thead>')[0];count=head.count('<th')-head.count('<thead')
        if count==7: widths=[8,13,12,13,18,25,11]
        elif 'Mã Hash' in head: widths=[7,15,20,50,8]
        elif count==2: widths=[35,65]
        elif 'Trạng thái' in head: widths=[8,48,30,14]
        elif count==4: widths=[16,34,34,16]
        else:return table
        return table.replace('<table>','<table><colgroup>'+''.join('<col style="width:'+str(x)+'%">' for x in widths)+'</colgroup>',1)
    body=re.sub(r'<table>.*?</table>',columns,body,flags=re.S)
    extra='''
.page-body { overflow-wrap: anywhere; }
.page-body table { table-layout: fixed; width: 100%; font-size: 9pt; line-height: 1.3; }
.page-body td, .page-body th { overflow-wrap: anywhere; word-break: normal; }
.page-body pre { white-space: pre-wrap; }
.page-body table code { font-size: inherit; padding: 0 1px; }
.page .header-title { max-width: 57%; font-size: 10pt !important; white-space: normal; text-align: right; }
.page-body li { font-size: 11pt; }
.page-body h1 { font-size: 18pt; }
.page-body blockquote { margin-left: 0; margin-right: 0; }
.cover-meta-box { font-size: 10pt; }
#source { width: 160mm; }
'''
    script=template0.PAGINATOR_SCRIPT.replace('var c = el.cloneNode(false); if (th) c.appendChild(th.cloneNode(true));', 'var c = el.cloneNode(false); var cols=el.querySelector("colgroup"); if(cols) c.appendChild(cols.cloneNode(true)); if (th) c.appendChild(th.cloneNode(true));').replace('newPage(); place([].slice.call(src.children)); src.remove(); toc();',
        'newPage(); place([].slice.call(src.children)); src.remove(); toc(); document.documentElement.dataset.ready="true";')
    # Keep a retained hidden copy to verify rendered content without pagination duplicates.
    header_label='Sử dụng AI' if kind=='ai-usage' else 'Lịch sử Git'
    doc=f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Template 1 — {html.escape(title)}</title><style>{template0.PAGE_CSS}\n{extra}</style></head><body>
{cover}<div id="pages"></div><div id="source">{body}</div>
<template id="tpl-header"><div class="template-header-bar"><div class="header-tab">Nhập môn công nghệ phần mềm</div><div class="header-title">Template 1 — {header_label}</div></div></template>
<template id="tpl-footer"><div class="template-footer-bar"><div class="footer-left">ĐH Khoa học tự nhiên TP HCM | Bộ môn Công nghệ phần mềm</div><div class="footer-tab">Trang <span class="pn"></span></div></div></template>
<a href="#trang-bia" class="back-to-top">▲ Lên đầu trang</a>{script}</body></html>'''
    write(folder/(kind+'.html'),doc)


def build_readme(manifest,ai_index,counts):
    text='''# Gói nộp Template 1 — Clarune — Nhóm 04

- `report/report.md`: toàn bộ bản final xuất từ Google Docs, giữ nguyên câu chữ; ảnh dùng đường dẫn tương đối vào `report/assets/`.
- `report/assets/ui/`: chỉ 31 ảnh giao diện có trong report, giữ nguyên tệp ảnh nguồn theo mã Figma.
- `report/assets/diagrams/`: 6 sơ đồ SVG sắc nét và mã nguồn drawio tương ứng; Hình 3.1 giữ nguyên bản Lãm nộp, 5 sơ đồ Use Case chỉnh theo bản final.
- `ai-usage/ai-usage.md` và `.html`: tổng hợp theo tác giả, giữ nguyên nội dung các phiên đã nộp.
- `git-contributions/git-contributions.md` và `.html`: snapshot lịch sử Git Template 1, gồm cả nhánh nộp bài chưa merge.
- `sources/`: bản final gốc có ảnh nhúng, draft dùng tra mã ảnh, nguyên bản nhật ký theo người và snapshot metadata Git; dùng đối soát, không thay thế nội dung report.

**PDF report:** trưởng nhóm tự xuất từ Google Docs và đặt tại `report/report.pdf`. Công cụ này không tạo hoặc giả lập PDF đã nộp.

## Nguồn và các điểm cần xác nhận

- Bản chữ duy nhất dùng đóng report là `sources/template1-final-original.md`; không lấy draft hoặc nội dung PR ghi đè bản final.
- AI usage đã thu thập của cả 4 thành viên. Gia Phúc đã nộp 1 dòng tổng hợp T1-08, chưa có phần chi tiết mục 6.3; giữ nguyên cả lỗi gõ trong nguồn, không tự viết thay tác giả.
- Các mã phiên T1-08… bị trùng giữa tác giả được giữ nguyên, đặt dưới tên tác giả để không đổi dữ liệu nguồn.
- Ngày 09–11/10/2026 trong nhật ký Lãm được giữ nguyên theo bản đã nộp, chưa có xác nhận đổi sang tháng 11.
- Các PR nguồn chưa được tác vụ đóng gói này merge vào main; trạng thái ghi trong báo cáo Git là trạng thái tại snapshot. Nhánh docs/t1-ticket-giaphuc đã có 4 commit của Gia Phúc; tại lần thu thập chưa thấy PR tương ứng. Snapshot ban đầu được lưu ở sources/history/git-snapshot-initial.json.
- Markdown gốc có mục lục kèm số trang từ Google Docs. Giữ nguyên các nhãn/số trang theo yêu cầu bảo toàn nội dung; đây không phải số trang do Markdown tự tính.
- Ảnh hồ sơ trong bản final là `62-8328.png`; draft nêu cả `62-8216` và `62-8328`, chỉ lấy ảnh thực sự xuất hiện trong final.
- Tệp `report/assets/manifest.json` ghi đủ 37 ánh xạ hình và SHA-256, trong đó 1 sơ đồ bối cảnh lấy nguyên tệp của Lãm, 5 sơ đồ Use Case được dựng lại và 31 hình UI sao chép nguyên tệp.

## Quy tắc sơ đồ

Hình 3.1 dùng nguyên văn SVG/drawio của Lãm tại commit 979179b, theo lựa chọn của trưởng nhóm; không vẽ lại hoặc thêm actor Mail Service. Nguồn được lưu tại sources/diagrams cùng SHA-256. Năm sơ đồ Use Case còn lại dựa vào graph của các tệp drawio hiện có; cập nhật tên Use Case theo 19 bảng đặc tả final. Người dùng là actor người que, Use Case là ellipse bên trong ranh giới hệ thống, actor/dịch vụ ngoài ranh giới. Association nét liền không mũi tên; generalization nét liền với tam giác rỗng hướng về actor cha. Không tự thêm include/extend. Worker, CSDL và storage là thành phần nội bộ, không vẽ thành actor. Các mô tả P1 và quyền hạn được đối chiếu với bản final.

Sơ đồ tổng thể và module dùng cùng nguồn tên UC và quan hệ; thay tên lỗi của graph tổng thể cũ (đặc biệt UC-07..10), sửa generalization Admin→Authenticated User bị thiếu target trong mã cũ, giữ UC-19 riêng cho Agent và UC-17 riêng cho Admin. Bản vẽ gốc vẫn còn nguyên ở thư mục assets/diagrams cũ; gói nộp trỏ tới bản đã chỉnh trong report/assets/diagrams.

## Tạo lại và kiểm tra

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/template1/requirements.txt
.venv/bin/python scripts/package_template1.py
.venv/bin/python scripts/verify_template1.py
```

Kiểm tra thêm bố cục bằng trình duyệt (tùy chọn): cài `playwright`, sau đó chạy `python scripts/verify_template1.py --browser`; cần Chrome/Chromium cục bộ.

Không sửa thủ công nguồn trong `sources/` nếu chưa có bản nộp mới của tác giả. Snapshot Git được cố định để việc render lại không thay số liệu. Muốn chốt snapshot mới, lưu lại snapshot cũ trước khi cập nhật. HTML dùng kiểu bìa, Times New Roman, A4, header/footer của Template 0; nội dung được đọc đầy đủ từ Markdown, không dùng các trường hợp hard-code commit/phiên của Template 0.

Bản nguồn lưu trữ giữ nguyên cả khoảng trắng và Markdown hard-break của tác giả; không tự sửa các dòng này để làm sạch diff. Kết quả kiểm tra nội dung/ảnh nằm ở `verification.json`, kiểm tra HTML ở `browser-validation.json`.
'''
    write(T1/'README.md',text)
    audit={'report_wording_preserved':True,'source_sha256':sha((SOURCES/'template1-final-original.md').read_bytes()),
           'figures':len(manifest),'ui_assets':len(UI),'diagrams':6,'context_diagram_source':'sources/diagrams/context-diagram-source.json','ai_sources':ai_index,'git_commit_counts':counts}
    write(T1/'verification.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')


def main():
    raw=(SOURCES/'template1-final-original.md').read_text()
    diagrams=generate(ROOT,raw)
    write(T1/'report/assets/diagrams/semantics.json',json.dumps(diagrams,ensure_ascii=False,indent=2)+'\n')
    manifest=build_report();ai=build_ai();counts=build_git()
    render_companion('ai-usage','AI Usage Report','Báo cáo Sử dụng AI — Giai đoạn Template 1')
    render_companion('git-contributions','Git Commit History Report','Báo cáo Lịch sử Commit &amp; Đóng góp cá nhân — Template 1')
    build_readme(manifest,ai,counts)
    print(json.dumps({'figures':len(manifest),'ai':ai,'git':counts},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
