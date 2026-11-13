#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Template 1 hand-in without editing the final report's wording.

Usage: python3 scripts/package_template1.py
Requires Python-Markdown. Uses pinned member snapshots in reports/template1/sources.
The PDF is exported by the team leader from Google Docs, outside this pipeline.
"""
import argparse
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
from report_sync import sync_working_documents
import render_ai_usage_template0 as template0

T1=ROOT/'reports/template1'
SOURCES=T1/'sources'
REPO='https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base'
DATE='13/11/2026'
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


def report_source_path():
    """The reviewed PDF transcription takes precedence over the archived export."""
    current = SOURCES/'template1-final-current.md'
    return current if current.is_file() else SOURCES/'template1-final-original.md'


def validate_report_baseline():
    baseline=json.loads((SOURCES/'report-baseline.json').read_text())
    assert sha((T1/baseline['authority']).read_bytes())==baseline['pdf_sha256'], 'PDF changed; review and update report-baseline.json before packaging'
    assert str(report_source_path().relative_to(T1))==baseline['markdown_source'], 'Reviewed transcription is missing'
    assert sha(report_source_path().read_bytes())==baseline['markdown_sha256'], 'Transcription changed; review against the PDF before packaging'


def report_body(text):
    return re.split(r'^\[image\d+\]:',text,flags=re.M)[0].rstrip()


def strip_toc_page_numbers(text):
    match=re.search(r'^# \*\*1 Bảng đánh giá thành viên',text,re.M)
    if not match:return text
    toc,rest=text[:match.start()],text[match.start():]
    toc=re.sub(r'\t\d+(?=\**\]\()', '',toc)
    toc=re.sub(r'\t\[\d+\]\([^\n]*\)', '',toc)
    return toc+rest


def content_fingerprint(text):
    """Formatting-insensitive comparison; keeps every prose/table word in order."""
    text=strip_toc_page_numbers(report_body(text))
    text=re.sub(r'!\[.*?\](?:\[image\d+\]|\([^\n]*?\))','',text)
    text=re.sub(r' \{#[^\n]+\}','',text)
    text=re.sub(r'<a id="[^"]*"></a>','',text)
    # Markdown markers and whitespace carry formatting, not report wording.
    return re.sub(r'[\s*#]+','',text)


def build_report():
    raw=report_source_path().read_text()
    body=strip_toc_page_numbers(report_body(raw))
    refs=['assets/diagrams/context_diagram_system.svg']+['assets/diagrams/'+a+'.svg' for a in BASELINES]
    refs += ['assets/ui/'+Path(a).name+'.png' for a in UI]
    assert len(refs)==37
    overrides={}
    override_path=SOURCES/'pdf-figure-overrides.json'
    if override_path.exists():
        override_data=json.loads(override_path.read_text())
        assert sha((ROOT/override_data['pdf']).read_bytes())==override_data['pdf_sha256'], 'PDF image overrides need review after PDF changes'
        overrides=override_data['files']
    manifest=[]
    for i,ref in enumerate(refs,1):
        match=re.search(r'!\[\]\[image'+str(i)+r'\]',body)
        assert match, f'Missing image{i}'
        caption=re.search(r'Hình [^\n]+',body[match.end():]).group(0).strip('* ')
        source_path=None
        if i>=7:
            source_path='docs/design/anh/'+UI[i-7]+'.png'
            override=overrides.get(Path(ref).name)
            if override:
                source_path=override['source']
                assert sha((ROOT/source_path).read_bytes())==override['sha256'], 'Reviewed PDF image changed'
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
    sync_working_documents(T1,body)
    write(T1/'report/assets/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest


def extract_sessions(text):
    start=text.index('## 6.3');end=text.index('## 6.4')
    blocks=re.split(r'(?=^### Phiên )',text[start:end],flags=re.M)[1:]
    return blocks


def ai_submission_text(text, author, id_map):
    """Apply only the numbering, dates and editorial cleanup confirmed by the owner."""
    text=re.sub(r'\bT1-\d+\b',lambda m:id_map.get(m[0],m[0]),text)
    if author=='lam':
        text=re.sub(r'\b(09|10|11)/10/2026\b',r'\1/11/2026',text)
    if author=='binh':
        text=text.replace(' (không ghi nhận model cụ thể)','')
        text=text.replace(' (không ghi nhận giờ cụ thể)','')
        text=text.replace('; không ghi nhận model cụ thể','')
        text=text.replace(' Chưa có xác nhận review của tác giả/reviewer trong phiên này.','')
        text=text.replace(' Các mô tả tự kiểm chứng của các phiên cũ là dữ liệu do tác giả đã ghi, chưa được phiên này xác minh độc lập. Tác giả/reviewer chưa xác nhận review nội dung trong phiên này; chưa kiểm thử phần mềm hay nghiệm thu học thuật.','')
    text=re.sub(r'^### Phiên ', '#### Phiên ',text,flags=re.M)
    return text


def ai_summary_row(row, block):
    # Lam's submitted rows have six cells; use the evidence already in the detail.
    cells=row.strip().strip('|').split('|')
    if len(cells)==6:
        match=re.search(r'^- \*\*Minh chứng:\*\* (.+)$',block,re.M)
        assert match,'Missing evidence in source detail'
        return row.rstrip()+' '+match[1]+' |'
    return row


def build_ai():
    owners=[('binh','Ngô Viết Thanh Bình','24120269'),('lam','Nguyễn Đức Lãm','24120083'),('quy-phuc','Lê Quý Phúc','24120121'),('gia-phuc','Phan Gia Phúc','24120503')]
    baseline=(SOURCES/'ai-usage-binh.md').read_text()
    prefix=baseline[:baseline.index('## 6.2')]
    prefix=re.sub(r'^# 6\.[^\n]*\n\n','',prefix)
    prefix=prefix.replace('## 6.1 ','## 1. ')
    out=['# BÁO CÁO SỬ DỤNG AI — TEMPLATE 1\n\n',prefix,
         '## 2. NHẬT KÝ SỬ DỤNG AI THEO THÀNH VIÊN\n\n']
    index=[];mapping=[];counter=0
    table_header='\n'.join(l for l in baseline.splitlines() if l.startswith('| STT |') or l.startswith('| :---: |'))
    for section,(key,name,mssv) in enumerate(owners,1):
        text=(SOURCES/f'ai-usage-{key}.md').read_text()
        rows=[l for l in text.splitlines() if l.startswith('|') and mssv in l]
        blocks=[b for b in extract_sessions(text) if mssv in b]
        block_by_id={re.match(r'### Phiên (T1-\d+):',b)[1]:b for b in blocks}
        id_map={}
        for row in rows:
            old=re.match(r'\| \*\*(T1-\d+)\*\*',row)[1]
            counter+=1;new=f'T1-{counter:02}'
            id_map[old]=new
            mapping.append({'author':name,'mssv':mssv,'source_id':old,'report_id':new,'source':f'sources/ai-usage-{key}.md'})
        assert set(id_map)==set(block_by_id),'Summary/detail mismatch in source'
        shown_rows=[]
        for row in rows:
            old=re.match(r'\| \*\*(T1-\d+)\*\*',row)[1]
            shown_rows.append(ai_submission_text(ai_summary_row(row,block_by_id[old]),key,id_map))
        shown_blocks=[ai_submission_text(b,key,id_map) for b in blocks]
        out += [f'### 2.{section} {name} — {mssv}\n\n',table_header+'\n'+'\n'.join(shown_rows)+'\n\n',''.join(shown_blocks)]
        index.append({'author':name,'mssv':mssv,'summary_rows':len(rows),'detailed_sessions':len(blocks),'source':f'sources/ai-usage-{key}.md','report_ids':id_map})
    counter+=1;pack_id=f'T1-{counter:02}'
    mapping.append({'author':'Ngô Viết Thanh Bình','mssv':'24120269','source_id':'T1-PACK-01','report_id':pack_id,'source':'Phiên đóng gói trong cuộc hội thoại'})
    out += ['### 2.5 Ngô Viết Thanh Bình — Đóng gói Template 1\n\n',table_header+'\n',
            f'| **{pack_id}** | 12/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Codex, OpenAI | Tổng hợp và chỉnh định dạng gói nộp Template 1 | Đóng gói report, assets, nhật ký AI và lịch sử Git; đối chiếu nội dung, hình ảnh và bố cục HTML bằng công cụ | `report/report.md`; `git-contributions/git-contributions.md`; nhánh `merge-template1` |\n\n',
            f'#### Phiên {pack_id}: Tổng hợp gói nộp Template 1\n\n',
            '- **Thời gian:** 12/11/2026.\n',
            '- **Tác giả chịu trách nhiệm:** Ngô Viết Thanh Bình — `24120269`.\n',
            '- **Công cụ / Nền tảng:** Codex, OpenAI.\n',
            '- **Prompt đã khử dữ liệu nhạy cảm:** Tổng hợp bản Markdown final, thay hình nhúng mờ bằng assets đúng mã, điều chỉnh sơ đồ theo bản final, tổng hợp Git contributions và AI usage như Template 0, giữ nguyên nội dung gốc và làm trên nhánh `merge-template1`.\n',
            '- **Nội dung AI tạo / áp dụng:** Công cụ đóng gói, ánh xạ 37 hình, 5 sơ đồ Use Case vector cùng nguồn drawio, tích hợp nguyên bản sơ đồ bối cảnh của Lãm, bản Markdown và HTML của nhật ký AI và đóng góp Git. Chuẩn hóa mã phiên và định dạng theo yêu cầu của trưởng nhóm.\n',
            '- **Kiểm chứng bằng công cụ:** Đối chiếu toàn bộ chữ của report và 19 bảng Use Case với nguồn; kiểm tra mã ảnh, SHA commit, đường dẫn assets, mã phiên trong bảng/chi tiết và bố cục HTML qua trình duyệt.\n',
            '- **Minh chứng:** `report/report.md`, `git-contributions/git-contributions.md`, nhánh `merge-template1`; task `T1-PUB-01` / `SCRUM-41` và `T1-SUBMIT-01` / `SCRUM-52`.\n\n---\n\n',
            baseline[baseline.index('## 6.4'):].replace('## 6.4 ','## 3. ').replace('ĐHKHTN:\n1.','ĐHKHTN:\n\n1.')]
    final_id=f'T1-{counter+1:02}'
    mapping.append({'author':'Ngô Viết Thanh Bình','mssv':'24120269','source_id':'T1-FINAL-01','report_id':final_id,'source':'Phiên hiệu chỉnh và hoàn thiện bản nộp trong cuộc hội thoại ngày 13/11/2026'})
    out.insert(-1, f'''### 2.6 Ngô Viết Thanh Bình — Hoàn thiện bản nộp

{table_header}
| **{final_id}** | 13/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Codex, OpenAI | Hiệu chỉnh sơ đồ UML, đồng bộ PDF và hoàn thiện gói nộp | AI chỉnh bố cục và đường nối; đối chiếu 19 UC, 37 hình và các thay đổi trong PDF; người dùng xem hình, góp ý và yêu cầu hiệu chỉnh | `report/Report.pdf`; `report/report.md`; `ai-usage/ai-usage.md`; `git-contributions/git-contributions.md` |

#### Phiên {final_id}: Hiệu chỉnh sơ đồ và hoàn thiện bản nộp

- **Thời gian:** 13/11/2026.
- **Tác giả chịu trách nhiệm:** Ngô Viết Thanh Bình — `24120269`.
- **Công cụ / Nền tảng:** Codex, OpenAI.
- **Prompt đã khử dữ liệu nhạy cảm:** Cân đối khung sơ đồ, dùng association thẳng riêng, sửa đường giao nhau và bố trí kế thừa actor; bỏ chú thích khỏi ảnh; đồng bộ Markdown với PDF mới; rà soát bản nộp, cập nhật lịch sử Git và tạo `4.zip` gồm ba thư mục ai-usage, git-contributions và report.
- **Nội dung AI tạo / áp dụng:** Hiệu chỉnh sáu sơ đồ SVG/drawio và ảnh PNG; đồng bộ nội dung Markdown, các mục trích và ảnh với PDF 70 trang; cập nhật nhật ký AI, lịch sử Git, HTML và công cụ đóng gói.
- **Kiểm chứng và hiệu chỉnh:** Người dùng xem các hình, chỉ ra khoảng trống, đường giao nhau, lỗi đường kế thừa đè khung và yêu cầu chỉnh lại bố cục. Công cụ đối chiếu toàn bộ thay đổi văn bản giữa hai PDF, kiểm tra 19 bảng UC và 37 hình, thử tải ảnh/liên kết mục lục và kiểm tra bố cục HTML bằng trình duyệt.
- **Minh chứng:** `report/Report.pdf`, `report/report.md`, các sơ đồ trong `report/assets/diagrams/` và lịch sử commit trên kho GitHub của nhóm.

---

''')
    combined=''.join(out)
    write(T1/'ai-usage/ai-usage.md',combined)
    write(T1/'sources/ai-session-index.json',json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
    return index


def capture_git_snapshot(refresh=False):
    path=SOURCES/'git-snapshot.json'
    if path.exists():
        if not refresh:return json.loads(path.read_text())
        previous=json.loads(path.read_text())
        stamp=re.sub(r'[^0-9]','',previous['captured_at'])
        archive=SOURCES/'history'/f'git-snapshot-{stamp}.json'
        if not archive.exists():shutil.copy2(path,archive)
    members=list(csv.DictReader((ROOT/'members.csv').open()))
    refs=['origin/main','origin/docs/t1-identity-binh','origin/docs/t1-knowledge-lam','origin/docs/t1-ai-quyphuc-markdown','origin/docs/t1-ticket-giaphuc','origin/merge-template1']
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


def summarize_changed_paths(files, threshold=5):
    """Partition paths into small file lists or whole directory subtrees."""
    tree={}
    for path in sorted(files):
        node=tree
        for part in Path(path).parts[:-1]:
            node=node.setdefault(part,{})
        node[Path(path).name]=path

    def walk(node, prefix):
        children=[v for v in node.values() if isinstance(v,str)]
        def leaves(n):
            return [p for v in n.values() for p in (leaves(v) if isinstance(v,dict) else [v])]
        paths=leaves(node)
        if prefix and len(paths)>=threshold and (len(prefix)>=2 or len(children)>=threshold):
            return [('/'.join(prefix)+'/',len(paths),True)]
        result=[]
        for name,value in sorted(node.items()):
            result.extend(walk(value,prefix+[name]) if isinstance(value,dict) else [(value,1,False)])
        return result
    return walk(tree,[])


def build_git(refresh=False):
    snapshot=capture_git_snapshot(refresh);commits=snapshot['commits'];members=snapshot['members']
    lines=['# BÁO CÁO LỊCH SỬ COMMIT GIT — TEMPLATE 1\n\n',
           f'> **Dự án:** Clarune — AI-Powered Helpdesk & Knowledge Base\n> **Nhóm:** Group 04\n> **Kho lưu trữ:** {REPO}\n> **Thời điểm chốt dữ liệu:** {snapshot["captured_at"]}\n\n',
           '## Phạm vi thống kê\n\n',
           'Báo cáo ghi nhận lịch sử Git của giai đoạn Template 1 từ 03/11/2026 đến thời điểm chốt dữ liệu, gồm phân tích yêu cầu, đặc tả Use Case, prototype và hoàn thiện bản nộp. Mỗi commit được tính một lần theo SHA; các commit lưu trữ Template 0 không thuộc phạm vi thống kê. Tác giả, thông điệp và thời gian được lấy từ lịch sử Git; thời gian hiển thị theo UTC+7.\n\n',
           '| Nhánh nguồn | SHA tại thời điểm chốt |\n| --- | --- |\n']
    for ref,h in snapshot['refs'].items():lines.append(f'| `{ref}` | [{h}]({REPO}/commit/{h}) |\n')
    lines += ['\nDanh sách thay đổi được nhóm theo thư mục khi có từ 5 tệp, kèm số lượng tệp. Commit được xác định theo tài khoản hoặc email của thành viên; tác giả Git `PC` với email `phgphuc0609@gmail.com` được ghi nhận cho Phan Gia Phúc.\n\n',
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
        lines.append('\n#### Tệp/thư mục thay đổi và nguồn nhánh\n\n')
        for c in own:
            lines += [f'**[{c["sha"][:8]}]({REPO}/commit/{c["sha"]})** — {c["subject"]}\n\n',
                      'Nguồn: '+', '.join('`'+r+'`' for r in c['refs'])+'.\n\n']
            if c['files']:
                groups=summarize_changed_paths(c['files'])
                lines.append('\n'.join('- `'+path+'`'+(' — '+str(count)+' tệp thay đổi' if is_folder else '') for path,count,is_folder in groups)+'\n\n')
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
                        'Ghi nhận '+('việc sử dụng AI' if kind=='ai-usage' else 'lịch sử Git và đóng góp cá nhân')+' trong giai đoạn Template 1 của dự án Clarune.')
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

- `report/Report.pdf`: bản final do trưởng nhóm xuất từ Google Docs, là nguồn chuẩn về nội dung.
- `report/report.md`: bản Markdown đã đối chiếu với PDF final; ảnh dùng đường dẫn tương đối vào `report/assets/`.
- Các file mục 01–05 và `TEMPLATE1_DRAFT_MASTER.md`: bản trích đồng bộ từ report hiện hành, không còn là khung chờ soạn.
- `report/assets/ui/`: chỉ 31 ảnh giao diện có trong report: 26 tệp nguồn Figma và 5 ảnh Knowledge Base trích nguyên từ PDF hiện hành; nguồn được ghi trong manifest.
- `report/assets/diagrams/`: 6 sơ đồ SVG sắc nét và mã nguồn drawio tương ứng; Hình 3.1 dựa trên bản Lãm nộp, đã hiệu chỉnh nhãn theo phạm vi P0; 5 sơ đồ Use Case chỉnh theo bản final.
- `ai-usage/ai-usage.md` và `.html`: tổng hợp theo tác giả, đánh số phiên thống nhất và áp dụng các hiệu chỉnh do trưởng nhóm xác nhận; giữ nguồn gốc để đối soát.
- `git-contributions/git-contributions.md` và `.html`: snapshot lịch sử Git Template 1, gồm cả nhánh nộp bài chưa merge. Nhóm nhiều tệp được gom thành thư mục kèm số lượng; danh sách đầy đủ giữ trong sources/git-snapshot.json.
- `sources/`: bản final gốc có ảnh nhúng, draft dùng tra mã ảnh, nguyên bản nhật ký theo người và snapshot metadata Git; dùng đối soát, không thay thế nội dung report. `pdf-assets/` chứa 5 ảnh Knowledge Base khớp PDF; `pdf-figure-overrides.json` ghi trang/xref/SHA-256 và khóa theo hash PDF; `pdf-sync-review.json` ghi kết quả đối chiếu PDF ngày 13/11/2026.

**PDF report:** dùng đúng tên `report/Report.pdf` (phân biệt chữ hoa/thường). Công cụ không tạo hoặc sửa PDF. Việc có PDF không phải bằng chứng đã nộp lên cổng trường.

## Nguồn và quy ước trình bày

- Nguồn chuẩn là `report/Report.pdf`. Bản chữ đã đối chiếu dùng để đóng gói là `sources/template1-final-current.md`; SHA-256 và các quyết định đồng bộ nằm tại `sources/report-baseline.json`.
- `sources/template1-final-original.md`, `sources/TEMPLATE1_DRAFT_MASTER.md`, các bản trong `sources/history/` và bản xuất Markdown `(1).md` là nguồn lưu trữ trước khi chốt; không dùng ghi đè nội dung hiện hành.
- AI usage đã thu thập của cả 4 thành viên. Gia Phúc đã nộp cả dòng tổng hợp T1-08 và phần chi tiết mục 6.3 tại commit 3eb4181; giữ nguyên nội dung tác giả đã nộp.
- Bản nộp dùng mã phiên duy nhất T1-01…T1-23 theo nhóm thành viên. Bảng và phần chi tiết khớp từng mã; bảng ánh xạ mã gốc nằm tại sources/ai-session-index.json. Nguồn lưu trữ giữ nguyên mã ban đầu.
- Trưởng nhóm xác nhận 8 phiên của Lãm diễn ra 09–11/11/2026; bản nộp đã sửa tháng 10 thành tháng 11, nguyên bản lưu trữ giữ nguyên. Hai phiên Codex ngày 12/11 chỉ ghi ngày và tên công cụ theo xác nhận của trưởng nhóm.
- Các PR nguồn chưa được tác vụ đóng gói này merge vào main; trạng thái ghi trong báo cáo Git là trạng thái tại snapshot. Nhánh docs/t1-ticket-giaphuc đã có 5 commit của Gia Phúc; tại lần thu thập chưa thấy PR tương ứng. Snapshot ban đầu được lưu ở sources/history/git-snapshot-initial.json.
- Mục lục Markdown đã bỏ số trang từ Google Docs theo yêu cầu trưởng nhóm; giữ nguyên tên mục và liên kết đến nội dung.
- Ảnh hồ sơ trong bản final là `62-8328.png`; draft nêu cả `62-8216` và `62-8328`, chỉ lấy ảnh thực sự xuất hiện trong final.
- Tệp `report/assets/manifest.json` ghi đủ 37 ánh xạ hình và SHA-256, trong đó 1 sơ đồ bối cảnh hiệu chỉnh nhãn từ bản gốc của Lãm, 5 sơ đồ Use Case được dựng lại và 31 hình UI sao chép nguyên tệp từ nguồn được chỉ định (26 Figma, 5 từ PDF).

## Quy tắc sơ đồ

Hình 3.1 dựa trên SVG/drawio của Lãm tại commit 979179b; giữ bố cục và quan hệ, thống nhất tên actor, bỏ nhãn đặt lại mật khẩu và thống kê thuộc P1 để khớp chú thích P0. Không thêm actor Mail Service. Sơ đồ thể hiện P0; đoạn giải thích bên dưới hình dẫn dịch vụ Email P1 tới UC-16 và sơ đồ Định danh và phân quyền. Nguồn được lưu tại sources/diagrams cùng SHA-256. Năm sơ đồ Use Case còn lại dựa vào graph của các tệp drawio hiện có; cập nhật tên Use Case theo 19 bảng đặc tả final. Người dùng là actor người que, Use Case là ellipse bên trong ranh giới hệ thống, actor/dịch vụ ngoài ranh giới. Association nét liền không mũi tên; generalization nét liền với tam giác rỗng hướng về actor cha. Mỗi association actor–Use Case được vẽ bằng một đoạn thẳng liền riêng, không có điểm bẻ, không gom trục hoặc thêm chấm phân nhánh; giao cắt không biểu thị quan hệ nối. Actor được đặt gần nhóm Use Case liên quan, đường nối tránh người que và nhãn. Khung hệ thống có khoảng đệm trên/dưới bằng nhau. Quy ước ký pháp tham chiếu OMG UML 2.5.1, mục 18 (https://www.omg.org/spec/UML/2.5.1/PDF). Không tự thêm include/extend. Worker, CSDL và storage là thành phần nội bộ, không vẽ thành actor. Các mô tả P1 và quyền hạn được đối chiếu với bản final. P1 được ghi thống nhất ở dòng mã UC; hình dùng tên nhà cung cấp chung, module tri thức chỉ sử dụng năng lực embedding. Module Định danh đặt Authenticated User phía trên ba vai trò Customer, Support Agent và System Administrator cùng hàng phía dưới, với cây kế thừa ngắn bên trái hệ thống, không có đường vòng quanh hình. Các đường kế thừa có thể dùng chung thân cây và đầu tam giác; quy tắc này không áp dụng cho association. Ở sơ đồ tổng thể, đường kế thừa vòng ngoài cách đáy khung 40 đơn vị; canvas được mở rộng để chừa lề dưới 40 đơn vị. Chi tiết phản biện và các điểm cần đối chiếu đặc tả nằm trong diagram-review.md.

Sơ đồ tổng thể và module dùng cùng nguồn tên UC và quan hệ; thay tên lỗi của graph tổng thể cũ (đặc biệt UC-07..10), sửa generalization Admin→Authenticated User bị thiếu target trong mã cũ, giữ UC-19 riêng cho Agent và UC-17 riêng cho Admin. Bản vẽ gốc vẫn còn nguyên ở thư mục assets/diagrams cũ; gói nộp trỏ tới bản đã chỉnh trong report/assets/diagrams.

## Tạo lại và kiểm tra

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/template1/requirements.txt
.venv/bin/python scripts/package_template1.py --report-only
.venv/bin/python scripts/verify_template1.py
```

Kiểm tra thêm bố cục bằng trình duyệt (tùy chọn): cài `playwright`, sau đó chạy `python scripts/verify_template1.py --browser`; cần Chrome/Chromium cục bộ.

Lệnh `--report-only` cập nhật report, các mục 01–05, master và metadata mà không tạo lại nhật ký AI hoặc lịch sử Git. Chạy không có cờ này chỉ khi cần tạo lại cả gói. Khi PDF thay đổi, đối chiếu và cập nhật `sources/template1-final-current.md` cùng `sources/report-baseline.json` trước khi chạy; không sửa nguồn tác giả lưu trữ. Snapshot Git được cố định để việc render lại không thay số liệu. Muốn chốt snapshot mới, lưu lại snapshot cũ trước khi cập nhật. HTML dùng kiểu bìa, Times New Roman, A4, header/footer của Template 0; nội dung được đọc đầy đủ từ Markdown, không dùng các trường hợp hard-code commit/phiên của Template 0.

Bản nguồn lưu trữ giữ nguyên cả khoảng trắng và Markdown hard-break của tác giả; không tự sửa các dòng này để làm sạch diff. Kết quả kiểm tra nội dung/ảnh nằm ở `verification.json`, kiểm tra HTML ở `browser-validation.json`.
'''
    write(T1/'README.md',text)
    audit={'report_wording_preserved':True,'source_sha256':sha(report_source_path().read_bytes()),
           'report_source':str(report_source_path().relative_to(T1)),
           'pdf_baseline':json.loads((SOURCES/'report-baseline.json').read_text()),
           'figures':len(manifest),'ui_assets':len(UI),'diagrams':6,'context_diagram_source':'sources/diagrams/context-diagram-source.json','ai_sources':ai_index,'git_commit_counts':counts}
    write(T1/'verification.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--report-only',action='store_true',help='Sync report and working sections without rebuilding AI/Git companions')
    parser.add_argument('--refresh-git',action='store_true',help='Capture the latest fetched Git refs and PR states')
    args=parser.parse_args()
    validate_report_baseline()
    raw=report_source_path().read_text()
    diagrams=generate(ROOT,raw)
    write(T1/'report/assets/diagrams/semantics.json',json.dumps(diagrams,ensure_ascii=False,indent=2)+'\n')
    manifest=build_report()
    if args.report_only:
        audit=json.loads((T1/'verification.json').read_text())
        build_readme(manifest,audit['ai_sources'],audit['git_commit_counts'])
        print('Synced report, 12 section documents, master, README and PDF provenance.')
        return
    ai=build_ai();counts=build_git(refresh=args.refresh_git)
    render_companion('ai-usage','AI Usage Report','Báo cáo Sử dụng AI — Giai đoạn Template 1')
    render_companion('git-contributions','Git Commit History Report','Báo cáo Lịch sử Commit &amp; Đóng góp cá nhân — Template 1')
    build_readme(manifest,ai,counts)
    print(json.dumps({'figures':len(manifest),'ai':ai,'git':counts},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
