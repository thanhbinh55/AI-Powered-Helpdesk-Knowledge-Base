#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Template 2 hand-in package (ai-usage, report, git-contributions, 4.zip)
strictly preserving the final report wording and authentic member AI usage & Git commits.

Usage:
  python3 scripts/package_template2.py [--refresh-git]
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
import zipfile
import zlib
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import render_ai_usage_template0 as template0
import render_reports

T2 = ROOT / 'reports/template2'
RELEASE = ROOT / 'docs/template2/release'
SOURCES = T2 / 'sources'
REPO = 'https://github.com/thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base'
DATE = '26/11/2026'

DOWNLOAD_MD = Path('/Users/ngovietthanhbinh/Downloads/[SE - Nhóm 4] Template2-ThietKe-Clarune-04 (1).md')
DOWNLOAD_PDF = Path('/Users/ngovietthanhbinh/Downloads/[SE - Nhóm 4] Template2-ThietKe-Clarune-04 (2).pdf')


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def report_body(text: str) -> str:
    return re.split(r'^\[image\d+\]:', text, flags=re.M)[0].rstrip()


def strip_toc_page_numbers(text: str) -> str:
    match = re.search(r'^# 1\*\*\. Đánh giá đóng góp các thành viên', text, re.M)
    if not match:
        return text
    toc, rest = text[:match.start()], text[match.start():]
    toc = re.sub(r'\t\d+(?=\**\]\()', '', toc)
    toc = re.sub(r'\t\[\d+\]\([^\n]*\)', '', toc)
    return toc + rest


def content_fingerprint(text: str) -> str:
    """Formatting-insensitive comparison; keeps every prose/table word in order."""
    text = strip_toc_page_numbers(report_body(text))
    text = re.sub(r'!\[.*?\](?:\[image\d+\]|\([^\n]*?\))', '', text)
    text = re.sub(r' \{#[^\n]+\}', '', text)
    text = re.sub(r'<a id="[^"]*"></a>', '', text)
    return re.sub(r'[\s*#]+', '', text)


def extract_pdf_class_diagrams(pdf_path: Path, out_dir: Path) -> dict:
    """Extract the 5 crisp 2000px Class Diagrams (3.3a..3.3e) directly from Report.pdf objects 102..112."""
    pdf_bytes = pdf_path.read_bytes()
    obj_map = {
        102: 'class-diagram-3.3a-workflow-ports.png',
        105: 'class-diagram-3.3b-identity.png',
        108: 'class-diagram-3.3c-ticket.png',
        109: 'class-diagram-3.3d-knowledge.png',
        112: 'class-diagram-3.3e-ai-data.png',
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    extracted = {}
    for obj_id, filename in obj_map.items():
        m = re.search(
            rf'\b{obj_id}\s+0\s+obj\s*<<(.*?)>>\s*stream\r?\n(.*?)\r?\nendstream'.encode(),
            pdf_bytes,
            re.S,
        )
        assert m, f'Missing PDF object {obj_id}'
        header = m.group(1)
        w = int(re.search(rb'/Width\s+(\d+)', header).group(1))
        h = int(re.search(rb'/Height\s+(\d+)', header).group(1))
        raw = zlib.decompress(m.group(2))
        assert len(raw) == w * h * 3, f'Unexpected raw RGB size for obj {obj_id}'
        dest = out_dir / filename
        Image.frombytes('RGB', (w, h), raw).save(dest)
        extracted[obj_id] = dest
    return extracted


def stage_sources() -> None:
    """Copy authoritative downloaded PDF/MD and member AI usage snapshots into reports/template2/sources/."""
    SOURCES.mkdir(parents=True, exist_ok=True)
    if DOWNLOAD_MD.is_file():
        shutil.copy2(DOWNLOAD_MD, SOURCES / 'template2-final-current.md')
    if DOWNLOAD_PDF.is_file():
        (T2 / 'report').mkdir(parents=True, exist_ok=True)
        shutil.copy2(DOWNLOAD_PDF, T2 / 'report/Report.pdf')
    for member in ('binh', 'lam', 'gia-phuc', 'quy-phuc'):
        src = ROOT / f'ai-usage/template2/{member}.md'
        assert src.is_file(), f'Missing member AI usage: {src}'
        shutil.copy2(src, SOURCES / f'ai-usage-{member}.md')
    pdf_bytes = (T2 / 'report/Report.pdf').read_bytes()
    md_bytes = (SOURCES / 'template2-final-current.md').read_bytes()
    page_count = len(re.findall(rb'/Type\s*/Page\b', pdf_bytes))
    baseline = {
        'authority': 'report/Report.pdf',
        'pdf_sha256': sha(pdf_bytes),
        'pages': page_count,
        'markdown_source': 'sources/template2-final-current.md',
        'markdown_sha256': sha(md_bytes),
        'review_date': '2026-11-26',
    }
    write(SOURCES / 'report-baseline.json', json.dumps(baseline, ensure_ascii=False, indent=2) + '\n')


def build_report() -> list:
    raw_path = SOURCES / 'template2-final-current.md'
    raw = raw_path.read_text(encoding='utf-8')
    body = strip_toc_page_numbers(report_body(raw))

    pdf_diagrams_dir = SOURCES / 'pdf-assets'
    extract_pdf_class_diagrams(T2 / 'report/Report.pdf', pdf_diagrams_dir)

    # Collapse the two-slice Google Docs image exports (`![][image4]![][image5]` and `![][image6]![][image7]`)
    # into single clean image tags before mapping, preserving every single word of text.
    body = body.replace('![][image4]![][image5]', '![][image4]')
    body = body.replace('![][image6]![][image7]', '![][image6]')
    body = re.sub(r'^\*+(!\[\]\[image\d+\])\*+$', r'\1', body, flags=re.M)

    # Copy draw.io & SVG sources for diagrams where available
    diag_dest_dir = T2 / 'report/assets/diagrams'
    diag_dest_dir.mkdir(parents=True, exist_ok=True)
    for stem, folder in [
        ('conceptual-model', ROOT / 'docs/template2/assets/diagrams'),
        ('system-decomposition-tree', ROOT / 'docs/template2/assets/diagrams'),
        ('system-architecture', ROOT / 'docs/template2/assets/diagrams'),
        ('physical-erd', ROOT / 'docs/template2/assets/diagrams'),
    ]:
        for ext in ('.drawio', '.svg'):
            candidate = folder / (stem + ext)
            if candidate.is_file():
                shutil.copy2(candidate, diag_dest_dir / (stem + ext))
    for qp_src, qp_dst in [
        ('screen-flow.drawio', 'screen-flow-template2.drawio'),
        ('screen-flow-figma.svg', 'screen-flow-template2.svg'),
    ]:
        candidate = ROOT / 'docs/template2/members/quy-phuc/diagrams' / qp_src
        if candidate.is_file():
            shutil.copy2(candidate, diag_dest_dir / qp_dst)

    image_plan = [
        ('image1', 'assets/diagrams/conceptual-model.png', 'docs/template2/assets/diagrams/conceptual-model.png', None),
        ('image2', 'assets/diagrams/system-decomposition-tree.png', 'docs/template2/assets/diagrams/system-decomposition-tree.png', None),
        ('image3', 'assets/diagrams/system-architecture.png', 'docs/template2/assets/diagrams/system-architecture.png', None),
        ('image4', 'assets/diagrams/class-diagram-3.3a-workflow-ports.png', 'reports/template2/sources/pdf-assets/class-diagram-3.3a-workflow-ports.png', 'image4+image5 (PDF obj 102)'),
        ('image6', 'assets/diagrams/class-diagram-3.3b-identity.png', 'reports/template2/sources/pdf-assets/class-diagram-3.3b-identity.png', 'image6+image7 (PDF obj 105)'),
        ('image8', 'assets/diagrams/class-diagram-3.3c-ticket.png', 'reports/template2/sources/pdf-assets/class-diagram-3.3c-ticket.png', 'PDF obj 108'),
        ('image9', 'assets/diagrams/class-diagram-3.3d-knowledge.png', 'reports/template2/sources/pdf-assets/class-diagram-3.3d-knowledge.png', 'PDF obj 109'),
        ('image10', 'assets/diagrams/class-diagram-3.3e-ai-data.png', 'reports/template2/sources/pdf-assets/class-diagram-3.3e-ai-data.png', 'PDF obj 112'),
        ('image11', 'assets/diagrams/physical-erd.png', 'docs/template2/assets/diagrams/physical-erd.png', None),
        ('image12', 'assets/diagrams/screen-flow-template2.png', 'docs/template2/members/quy-phuc/diagrams/screen-flow-template2.png', None),
        ('image13', 'assets/ui/113-4387.png', 'docs/design/anh/v3/113-4387.png', 'I01'),
        ('image14', 'assets/ui/114-4766.png', 'docs/design/anh/v3/114-4766.png', 'I02'),
        ('image15', 'assets/ui/113-3580.png', 'docs/design/anh/v3/113-3580.png', 'I03'),
        ('image16', 'assets/ui/111-2664.png', 'docs/design/anh/v3/111-2664.png', 'C01'),
        ('image17', 'assets/ui/132-6237.png', 'docs/design/anh/v3/132-6237.png', 'C02'),
        ('image18', 'assets/ui/111-2763.png', 'docs/design/anh/v3/111-2763.png', 'C03'),
        ('image19', 'assets/ui/132-5524.png', 'docs/design/anh/v3/132-5524.png', 'A01'),
        ('image20', 'assets/ui/132-5676.png', 'docs/design/anh/v3/132-5676.png', 'A02'),
        ('image21', 'assets/ui/111-1700.png', 'docs/design/anh/v3/111-1700.png', 'A03'),
        ('image22', 'assets/ui/118-8823.png', 'docs/design/anh/v3/118-8823.png', 'A-DiscardConfirm'),
        ('image23', 'assets/ui/118-6210.png', 'docs/design/anh/v3/118-6210.png', 'A11'),
        ('image24', 'assets/ui/111-3691.png', 'docs/design/anh/v3/111-3691.png', 'K01'),
        ('image25', 'assets/ui/111-4066.png', 'docs/design/anh/v3/111-4066.png', 'K04'),
        ('image26', 'assets/ui/133-7972.png', 'docs/design/anh/v3/133-7972.png', 'D01-PhanCong'),
        ('image27', 'assets/ui/112-2142.png', 'docs/design/anh/v3/112-2142.png', 'D02'),
        ('image28', 'assets/ui/112-2268.png', 'docs/design/anh/v3/112-2268.png', 'D03'),
    ]

    manifest = []
    for ref_key, asset_rel, source_rel, note in image_plan:
        match = re.search(r'!\[\]\[' + re.escape(ref_key) + r'\]', body)
        assert match, f'Missing {ref_key} in report body'
        cap_match = re.search(r'Hình [^\n]+', body[match.end():])
        caption = cap_match.group(0).strip('* ') if cap_match else ''
        src = ROOT / source_rel
        dest = T2 / 'report' / asset_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        body = body.replace(f'![][{ref_key}]', f'![]({asset_rel})')
        item = {
            'reference': ref_key,
            'caption': caption,
            'asset': asset_rel,
            'source': source_rel,
            'sha256': sha(dest.read_bytes()),
        }
        if note:
            item['note'] = note
        manifest.append(item)

    body = re.sub(r'^#+\s*$', '', body, flags=re.M)

    def heading(m):
        ident = re.sub(r'\\([()\[\]])', r'\1', m[2])
        return '<a id="' + html.escape(ident, quote=True) + '"></a>\n\n' + m[1]

    body = re.sub(r'^(#{1,6} [^\n]+?) \{#([^\n]+)\}$', heading, body, flags=re.M)
    body = re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'

    assert content_fingerprint(raw) == content_fingerprint(body), 'Report wording changed!'
    assert '[image' not in body and 'data:image' not in body, 'Unresolved image reference remains!'

    write(T2 / 'report/report.md', body)
    write(T2 / 'report/assets/manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

    # Sync TEMPLATE2_DRAFT_MASTER.md with final report wording
    relocated_t2 = re.sub(r'!\[\]\((assets/[^)]+)\)', r'![](report/\1)', body)
    write(
        T2 / 'TEMPLATE2_DRAFT_MASTER.md',
        f'> Bản master đồng bộ theo [Report.pdf](report/Report.pdf) ngày {DATE}. '
        'Nội dung trích từ [report.md](report/report.md); ảnh dùng chung với bản final.\n\n'
        + relocated_t2,
    )
    relocated_docs = re.sub(r'!\[\]\((assets/[^)]+)\)', r'![](release/report/\1)', body)
    write(
        ROOT / 'docs/template2/TEMPLATE2_DRAFT_MASTER.md',
        f'> Bản master đồng bộ theo [Report.pdf](release/report/Report.pdf) ngày {DATE}. '
        'Nội dung trích từ [report.md](release/report/report.md); ảnh dùng chung với bản final.\n\n'
        + relocated_docs,
    )
    return manifest


def build_ai() -> list:
    """Synthesize all 4 members' authentic AI usage logs into reports/template2/ai-usage/ai-usage.md."""
    table_header = (
        '| STT | Thời gian | Thành viên (MSSV) | Công cụ & Model | Nội dung công việc trong Template 2 | '
        'Nội dung AI tạo & Con người tự kiểm chứng | Minh chứng / Commit |\n'
        '| :---: | :---: | :--- | :--- | :--- | :--- | :--- |'
    )

    out = [
        '# BÁO CÁO SỬ DỤNG AI — TEMPLATE 2\n\n',
        '> **Dự án:** AI-Powered Helpdesk & Knowledge Base (Clarune)  \n'
        '> **Nhóm thực hiện:** Nhóm 04 — Lớp Nhập môn Công nghệ Phần mềm (CS10014), Trường ĐHKHTN, ĐHQG-HCM  \n'
        f'> **Kho lưu trữ:** {REPO}  \n'
        '> **Chuẩn quy định:** Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS  \n'
        '> **Phạm vi tài liệu:** Nhật ký ghi nhận các phiên sử dụng công cụ AI phục vụ trực tiếp cho Báo cáo Thiết kế Phần mềm Template 2 (kế thừa và tiếp nối độc lập sau khi đã nộp hoàn tất Template 0 và Template 1).  \n\n'
        '---\n\n'
        '## 1. NGUYÊN TẮC MINH BẠCH & KIỂM CHỨNG TRONG TEMPLATE 2\n\n'
        '1. **Minh bạch câu lệnh (Prompts):** Toàn bộ các câu prompt đưa vào AI đều được ghi nhận trung thực từ nhật ký của từng thành viên, tóm tắt rõ mục đích và đã khử các thông tin nhạy cảm (secrets/credentials/PII).\n'
        '2. **Không sao chép máy móc:** Mọi sơ đồ EER, sơ đồ kiến trúc, sơ đồ lớp (Class Diagram), sơ đồ cơ sở dữ liệu vật lý (Physical ERD), đặc tả dữ liệu Flyway V1–V5 và thiết kế giao diện Figma ver3 do AI hỗ trợ đều được thành viên phụ trách đối chiếu chéo với `SRS-master.md`, `MVP_CONTRACTS.md`, mã nguồn kho lưu trữ và tài liệu nhóm trên Google Docs (`[SE - Nhóm 4] Template2-ThietKe-Clarune-04`) trước khi chốt.\n'
        '3. **Phân định trách nhiệm cá nhân:** Tác giả từng mục chịu trách nhiệm trực tiếp về phần nội dung con người đã kiểm chứng; báo cáo tổng hợp này giữ nguyên trung thực 100% nội dung các phiên AI mà 4 thành viên đã ghi nhận trên nhánh cá nhân.\n\n'
        '---\n\n'
        '## 2. NHẬT KÝ SỬ DỤNG AI THEO THÀNH VIÊN\n\n',
    ]

    mapping = []
    index = []
    counter = 0

    # --- 2.1 Ngô Viết Thanh Bình (24120269) ---
    binh_text = (SOURCES / 'ai-usage-binh.md').read_text(encoding='utf-8')
    binh_rows = [l for l in binh_text.splitlines() if l.startswith('| **T2-')]
    binh_blocks = re.split(r'(?=^### Phiên T2-)', binh_text[binh_text.index('## 2.'):], flags=re.M)[1:]
    binh_id_map = {}
    for row in binh_rows:
        old_id = re.match(r'\|\s*\*\*(T2-\d+)\*\*', row)[1]
        counter += 1
        new_id = f'T2-{counter:02d}'
        binh_id_map[old_id] = new_id
        mapping.append({
            'author': 'Ngô Viết Thanh Bình',
            'mssv': '24120269',
            'source_id': old_id,
            'report_id': new_id,
            'source': 'ai-usage/template2/binh.md',
        })
    shown_binh_rows = [re.sub(r'\bT2-\d+\b', lambda m: binh_id_map.get(m[0], m[0]), r) for r in binh_rows]
    shown_binh_blocks = []
    for b in binh_blocks:
        b2 = re.sub(r'\bT2-\d+\b', lambda m: binh_id_map.get(m[0], m[0]), b)
        b2 = re.sub(r'^### Phiên (T2-\d+) — ', r'#### Phiên \1: ', b2, flags=re.M)
        shown_binh_blocks.append(b2.strip() + '\n\n')
    out.append('### 2.1 Ngô Viết Thanh Bình — 24120269\n\n')
    out.append(table_header + '\n' + '\n'.join(shown_binh_rows) + '\n\n')
    out.append(''.join(shown_binh_blocks))
    index.append({
        'author': 'Ngô Viết Thanh Bình',
        'mssv': '24120269',
        'summary_rows': len(binh_rows),
        'detailed_sessions': len(binh_blocks),
        'source': 'ai-usage/template2/binh.md',
        'report_ids': binh_id_map,
    })

    # --- 2.2 Nguyễn Đức Lãm (24120083) ---
    lam_text = (SOURCES / 'ai-usage-lam.md').read_text(encoding='utf-8')
    lam_rows = [l for l in lam_text.splitlines() if l.startswith('| **T2-')]
    lam_blocks = re.split(r'(?=^### Phiên T2-)', lam_text[lam_text.index('## 2.'):], flags=re.M)[1:]
    lam_id_map = {}
    for row in lam_rows:
        old_id = re.match(r'\|\s*\*\*(T2-\d+)\*\*', row)[1]
        counter += 1
        new_id = f'T2-{counter:02d}'
        lam_id_map[old_id] = new_id
        mapping.append({
            'author': 'Nguyễn Đức Lãm',
            'mssv': '24120083',
            'source_id': old_id,
            'report_id': new_id,
            'source': 'ai-usage/template2/lam.md',
        })
    shown_lam_rows = [re.sub(r'\bT2-\d+\b', lambda m: lam_id_map.get(m[0], m[0]), r) for r in lam_rows]
    shown_lam_blocks = []
    for b in lam_blocks:
        b2 = re.sub(r'\bT2-\d+\b', lambda m: lam_id_map.get(m[0], m[0]), b)
        b2 = re.sub(r'^### Phiên (T2-\d+) — ', r'#### Phiên \1: ', b2, flags=re.M)
        shown_lam_blocks.append(b2.strip() + '\n\n---\n\n')
    out.append('### 2.2 Nguyễn Đức Lãm — 24120083\n\n')
    out.append(table_header + '\n' + '\n'.join(shown_lam_rows) + '\n\n')
    out.append(''.join(shown_lam_blocks))
    index.append({
        'author': 'Nguyễn Đức Lãm',
        'mssv': '24120083',
        'summary_rows': len(lam_rows),
        'detailed_sessions': len(lam_blocks),
        'source': 'ai-usage/template2/lam.md',
        'report_ids': lam_id_map,
    })

    # --- 2.3 Phan Gia Phúc (24120503) ---
    gp_text = (SOURCES / 'ai-usage-gia-phuc.md').read_text(encoding='utf-8')
    gp_blocks = re.split(r'(?=^### )', gp_text, flags=re.M)[1:]
    gp_id_map = {}
    gp_rows = []
    shown_gp_blocks = []
    for idx_gp, b in enumerate(gp_blocks, 1):
        m_title = re.match(r'^### ([^\n]+)', b)
        raw_heading = m_title.group(1).strip()
        date_part, title_part = [p.strip() for p in raw_heading.split('—', 1)]
        old_id = f'GP-{idx_gp:02d}'
        counter += 1
        new_id = f'T2-{counter:02d}'
        gp_id_map[old_id] = new_id
        mapping.append({
            'author': 'Phan Gia Phúc',
            'mssv': '24120503',
            'source_id': raw_heading,
            'report_id': new_id,
            'source': 'ai-usage/template2/gia-phuc.md',
        })
        fields = {}
        for line in b.splitlines()[1:]:
            m_f = re.match(r'^- \*\*([^*]+)\*\*\s+(.+)$', line.strip())
            if m_f:
                fields[m_f.group(1).strip()] = m_f.group(2).strip()
        row = (
            f'| **{new_id}** | {fields["Thời gian"]} | {fields["Tác giả"]} | {fields["Công cụ/Model"]} | '
            f'{title_part} | **AI tạo:** {fields["Nội dung AI tạo"]} **Kiểm chứng:** {fields["Nội dung tự kiểm chứng & hiệu chỉnh"]} | '
            f'{fields["Minh chứng/Commit"]} |'
        )
        gp_rows.append(row)
        b_body = '\n'.join(b.splitlines()[1:]).strip()
        shown_gp_blocks.append(f'#### Phiên {new_id}: {raw_heading}\n\n{b_body}\n\n---\n\n')
    out.append('### 2.3 Phan Gia Phúc — 24120503\n\n')
    out.append(table_header + '\n' + '\n'.join(gp_rows) + '\n\n')
    out.append(''.join(shown_gp_blocks))
    index.append({
        'author': 'Phan Gia Phúc',
        'mssv': '24120503',
        'summary_rows': len(gp_rows),
        'detailed_sessions': len(gp_blocks),
        'source': 'ai-usage/template2/gia-phuc.md',
        'report_ids': gp_id_map,
    })

    # --- 2.4 Lê Quý Phúc (24120121) ---
    qp_text = (SOURCES / 'ai-usage-quy-phuc.md').read_text(encoding='utf-8')
    qp_table_rows = [l for l in qp_text.splitlines() if l.startswith('| 2')]
    qp_id_map = {}
    qp_rows = []
    shown_qp_blocks = []
    for idx_qp, r in enumerate(qp_table_rows, 1):
        cells = [c.strip() for c in r.strip().strip('|').split('|')]
        when, author, tool, prompt, ai_gen, verify, evidence = cells
        old_id = f'QP-{idx_qp:02d}'
        counter += 1
        new_id = f'T2-{counter:02d}'
        qp_id_map[old_id] = new_id
        mapping.append({
            'author': 'Lê Quý Phúc',
            'mssv': '24120121',
            'source_id': when,
            'report_id': new_id,
            'source': 'ai-usage/template2/quy-phuc.md',
        })
        qp_rows.append(
            f'| **{new_id}** | {when} | {author} | {tool} | {prompt} | '
            f'**AI tạo:** {ai_gen} **Kiểm chứng:** {verify} | {evidence} |'
        )
        shown_qp_blocks.append(
            f'#### Phiên {new_id}: {prompt}\n\n'
            f'- **Thời gian:** {when}\n'
            f'- **Tác giả:** {author}\n'
            f'- **Công cụ/Model:** {tool}\n'
            f'- **Prompt đã khử dữ liệu nhạy cảm:** {prompt}\n'
            f'- **Nội dung AI tạo:** {ai_gen}\n'
            f'- **Nội dung tự kiểm chứng & hiệu chỉnh:** {verify}\n'
            f'- **Minh chứng/Commit:** {evidence}\n\n---\n\n'
        )
    out.append('### 2.4 Lê Quý Phúc — 24120121\n\n')
    out.append(table_header + '\n' + '\n'.join(qp_rows) + '\n\n')
    out.append(''.join(shown_qp_blocks))
    index.append({
        'author': 'Lê Quý Phúc',
        'mssv': '24120121',
        'summary_rows': len(qp_rows),
        'detailed_sessions': len(qp_table_rows),
        'source': 'ai-usage/template2/quy-phuc.md',
        'report_ids': qp_id_map,
    })

    # --- 2.5 Ngô Viết Thanh Bình — Đóng gói Template 2 ---
    counter += 1
    pack_id = f'T2-{counter:02d}'
    mapping.append({
        'author': 'Ngô Viết Thanh Bình',
        'mssv': '24120269',
        'source_id': 'T2-PACK-01',
        'report_id': pack_id,
        'source': 'Phiên đóng gói bản nộp Template 2 trên nhánh merge-template2 ngày 26/11/2026',
    })
    out.append(
        f'### 2.5 Ngô Viết Thanh Bình — Đóng gói Template 2\n\n'
        f'{table_header}\n'
        f'| **{pack_id}** | 26/11/2026 | Ngô Viết Thanh Bình<br>`24120269` | Antigravity AI (Gemini 4 Argon Medium) | '
        f'Hợp nhất 4 nhánh thành viên và đóng gói bộ nộp Template 2 (`ai-usage`, `report`, `git-contributions`, `4.zip`) | '
        f'AI hỗ trợ merge 4 nhánh thành viên vào `merge-template2`, tổng hợp nguyên văn nhật ký AI của 4 thành viên, ánh xạ 26 hình từ `Report.pdf` & kho ảnh Figma ver3/draw.io vào `report/report.md` (giữ nguyên 100% câu chữ bản chốt), cập nhật lịch sử Git và xuất HTML chuẩn Template 1; sinh viên kiểm chứng SHA-256, đường dẫn ảnh và bố cục HTML | '
        f'`report/Report.pdf`; `report/report.md`; `ai-usage/ai-usage.md`; `git-contributions/git-contributions.md`; nhánh `merge-template2` (`SCRUM-55`) |\n\n'
        f'#### Phiên {pack_id}: Hợp nhất nhánh và đóng gói bộ nộp Template 2\n\n'
        '- **1. Thời gian:** 26/11/2026.\n'
        '- **2. Tác giả:** Ngô Viết Thanh Bình (MSSV: `24120269` — Trưởng nhóm).\n'
        '- **3. Công cụ / Model:** Antigravity AI (Gemini 4 Argon Medium) via Antigravity IDE.\n'
        '- **4. Prompt đã khử dữ liệu nhạy cảm:** Tạo nhánh `merge-template2` hợp nhất bài làm của tất cả thành viên; tổng hợp file `ai-usage` (`.md` và `.html`) dựa theo chính xác nội dung các thành viên đã thực hiện theo chuẩn định dạng Template 1; đưa hai bản tải về từ Google Docs (`Report.pdf` và `report.md`) vào phần nộp bài kèm đầy đủ hình ảnh trong `assets/` mà tuyệt đối không sửa nội dung chữ; cập nhật `git-contributions` (`.md` và `.html`) mới nhất từ repo.\n'
        '- **5. Nội dung AI tạo:** Script đóng gói `scripts/package_template2.py`, bộ báo cáo `ai-usage/ai-usage.md` & `.html`, `report/Report.pdf`, `report/report.md` kèm 26 tệp hình ảnh sắc nét trong `report/assets/{diagrams,ui}/`, `git-contributions/git-contributions.md` & `.html` và tệp nén `4.zip`.\n'
        '- **6. Nội dung tự kiểm chứng & hiệu chỉnh:** Đối chiếu fingerprint văn bản giữa file Markdown tải từ Google Docs và `report/report.md` đạt khớp 100% từng từ; kiểm tra 5 sơ đồ lớp trích nguyên gốc từ đối tượng ảnh 2000px trong `Report.pdf`, 5 sơ đồ kiến trúc/EER/ERD/Screen Flow và 16 ảnh giao diện Figma ver3; xác minh toàn bộ 18 phiên AI cá nhân và toàn bộ lịch sử commit Git không sai lệch.\n'
        '- **7. Minh chứng / Commit:** `reports/template2/`, `docs/template2/release/`, nhánh `merge-template2` (`SCRUM-55`).\n\n---\n\n'
        '## 3. CAM KẾT ĐẠO ĐỨC HỌC THUẬT\n\n'
        'Nhóm cam kết thực hiện đúng Quy định về việc sử dụng AI của Khoa CNTT - Trường ĐHKHTN:\n\n'
        '1. Mọi công cụ AI chỉ đóng vai trò hỗ trợ gợi ý cấu trúc, định dạng và tăng tốc quy trình làm việc; sinh viên tự thực hiện việc kiểm chứng, chỉnh sửa chuyên môn và chịu hoàn toàn trách nhiệm về nội dung báo cáo.\n'
        '2. Tuyệt đối không sao chép máy móc, không làm sai lệch số liệu thực nghiệm và không đưa thông tin nhạy cảm/khóa bảo mật lên các dịch vụ AI công cộng.\n'
    )

    combined = ''.join(out)
    write(T2 / 'ai-usage/ai-usage.md', combined)
    write(SOURCES / 'ai-session-index.json', json.dumps(mapping, ensure_ascii=False, indent=2) + '\n')
    return index


def capture_git_snapshot(refresh: bool = False) -> dict:
    path = SOURCES / 'git-snapshot.json'
    if path.exists() and not refresh:
        return json.loads(path.read_text(encoding='utf-8'))
    members = list(csv.DictReader((ROOT / 'members.csv').open(encoding='utf-8')))
    refs = [
        'origin/main',
        'docs/t2-binh',
        'origin/docs/t2-giaphuc',
        'origin/docs/t2-lam',
        'origin/docs/t2-quy-phuc',
        'merge-template2',
    ]
    pinned = {}
    for ref in refs:
        try:
            pinned[ref] = git('rev-parse', ref)
        except Exception:
            pass
    # Capture all commits in the repository (or since Template 2 phase started on 2026-11-14)
    # Note: Also capture full repo counts so both Template 2 phase commits and cumulative context are clear.
    hashes = git('log', '--since=2026-11-14T00:00:00+07:00', '--format=%H', *pinned.values()).splitlines()
    records = []
    for h in hashes:
        fields = git('show', '-s', '--format=%H%x00%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI%x00%s%x00%P', h).split('\0')
        files = git('diff-tree', '--root', '--no-commit-id', '--name-only', '-r', h).splitlines()
        if len(fields[8].split()) > 1:
            files = git('diff', '--name-only', fields[8].split()[0], h).splitlines()
        records.append(
            dict(
                zip(
                    ['sha', 'author', 'author_email', 'authored_at', 'committer', 'committer_email', 'committed_at', 'subject', 'parents'],
                    fields,
                ),
                files=files,
                refs=[
                    ref
                    for ref, tip in pinned.items()
                    if subprocess.run(['git', 'merge-base', '--is-ancestor', h, tip], cwd=ROOT).returncode == 0
                ],
            )
        )
    prs = json.loads(
        subprocess.check_output(
            [
                'gh',
                'pr',
                'list',
                '--repo',
                'thanhbinh55/AI-Powered-Helpdesk-Knowledge-Base',
                '--state',
                'all',
                '--limit',
                '50',
                '--json',
                'number,title,headRefName,state,author,url,mergedAt',
            ],
            text=True,
        )
    )
    snapshot = {
        'captured_at': datetime.now(ZoneInfo('Asia/Ho_Chi_Minh')).isoformat(timespec='seconds'),
        'period_start': '2026-11-14T00:00:00+07:00',
        'refs': pinned,
        'members': members,
        'commits': records,
        'pull_requests': prs,
    }
    write(path, json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    return snapshot


def summarize_changed_paths(files: list, threshold: int = 5) -> list:
    """Partition paths into small file lists or whole directory subtrees."""
    tree = {}
    for path in sorted(files):
        node = tree
        for part in Path(path).parts[:-1]:
            node = node.setdefault(part, {})
        node[Path(path).name] = path

    def walk(node, prefix):
        children = [v for v in node.values() if isinstance(v, str)]

        def leaves(n):
            return [p for v in n.values() for p in (leaves(v) if isinstance(v, dict) else [v])]

        paths = leaves(node)
        if prefix and len(paths) >= threshold and (len(prefix) >= 2 or len(children) >= threshold):
            return [('/'.join(prefix) + '/', len(paths), True)]
        result = []
        for name, value in sorted(node.items()):
            result.extend(walk(value, prefix + [name]) if isinstance(value, dict) else [(value, 1, False)])
        return result

    return walk(tree, [])


def build_git(refresh: bool = False) -> dict:
    snapshot = capture_git_snapshot(refresh)
    commits = snapshot['commits']
    members = snapshot['members']
    lines = [
        '# BÁO CÁO LỊCH SỬ COMMIT GIT — TEMPLATE 2\n\n',
        f'> **Dự án:** Clarune — AI-Powered Helpdesk & Knowledge Base\n'
        f'> **Nhóm:** Group 04\n'
        f'> **Kho lưu trữ:** {REPO}\n'
        f'> **Thời điểm chốt dữ liệu:** {snapshot["captured_at"]}\n\n',
        '## Phạm vi thống kê\n\n',
        'Báo cáo ghi nhận lịch sử Git của giai đoạn Template 2 từ 14/11/2026 đến thời điểm chốt dữ liệu, gồm tái cấu trúc kho mã nguồn Giai đoạn 2, khởi tạo khung nền tảng Backend/CI, thiết kế giao diện Clarune Redesign v3 (Figma ver3), mô hình quan niệm EER, thiết kế kiến trúc, sơ đồ lớp, lược đồ cơ sở dữ liệu vật lý (Physical ERD & Flyway V1–V5) và hợp nhất bản nộp Template 2. Mỗi commit được tính một lần theo SHA. Tác giả, thông điệp và thời gian được lấy trực tiếp từ lịch sử Git; thời gian hiển thị theo UTC+7.\n\n',
        '| Nhánh nguồn | SHA tại thời điểm chốt |\n| --- | --- |\n',
    ]
    for ref, h in snapshot['refs'].items():
        lines.append(f'| `{ref}` | [{h}]({REPO}/commit/{h}) |\n')
    lines += [
        '\nDanh sách thay đổi được nhóm theo thư mục khi có từ 5 tệp, kèm số lượng tệp. Commit được xác định theo tài khoản hoặc email của thành viên; tác giả Git `PC` với email `phgphuc0609@gmail.com` được ghi nhận cho Phan Gia Phúc.\n\n',
        '## Bảng tổng hợp\n\n| MSSV | Thành viên | GitHub | Commit |\n| --- | --- | --- | ---: |\n',
    ]
    grouped = {}
    for m in members:
        own = [
            c
            for c in commits
            if c['author_email'].lower() in {m['git_email'].lower(), m['jira_email'].lower()}
            or c['author'].lower() == m['git_username'].lower()
        ]
        own.sort(key=lambda c: (c['authored_at'], c['sha']), reverse=True)
        grouped[m['mssv']] = own
        lines.append(f'| {m["mssv"]} | {m["full_name"]} | {m["git_username"]} | {len(own)} |\n')
    assigned = {c['sha'] for v in grouped.values() for c in v}
    assert assigned == {c['sha'] for c in commits}, 'Unmapped or omitted author'
    lines += ['\n## DANH SÁCH COMMIT CỦA MỖI THÀNH VIÊN\n\n']
    for i, m in enumerate(members, 1):
        own = grouped[m['mssv']]
        lines += [
            f'### {i}. Thành viên: {m["mssv"]} - {m["git_username"]} ({m["full_name"]})\n\n',
            f'- **Họ và tên:** {m["full_name"]}\n'
            f'- **Mã số sinh viên:** `{m["mssv"]}`\n'
            f'- **Tài khoản Git:** `{m["git_username"]}`\n'
            f'- **Email Git:** `{m["git_email"]}`\n'
            f'- **Module phụ trách:** {m["role_module"]}\n'
            f'- **Tổng số commit ghi nhận:** {len(own)}\n\n',
        ]
        if not own:
            lines.append(
                'Chưa tìm thấy commit của thành viên trong phạm vi Template 2 trên các nhánh nguồn đã kiểm tra.\n\n'
            )
            continue
        lines.append('| STT | Mã Hash | Ngày commit (UTC+7) | Thông điệp commit (Jira Key) | Số tệp |\n| ---: | --- | --- | --- | ---: |\n')
        for j, c in enumerate(own, 1):
            when = datetime.fromisoformat(c['authored_at']).astimezone(ZoneInfo('Asia/Ho_Chi_Minh')).strftime('%d/%m/%Y %H:%M')
            subject = c['subject'].replace('|', '&#124;')
            lines.append(f'| {j} | [{c["sha"][:8]}]({REPO}/commit/{c["sha"]}) | {when} | {subject} | {len(c["files"])} |\n')
        lines.append('\n#### Tệp/thư mục thay đổi và nguồn nhánh\n\n')
        for c in own:
            lines += [
                f'**[{c["sha"][:8]}]({REPO}/commit/{c["sha"]})** — {c["subject"]}\n\n',
                'Nguồn: ' + ', '.join('`' + r + '`' for r in c['refs']) + '.\n\n',
            ]
            if c['files']:
                groups = summarize_changed_paths(c['files'])
                lines.append(
                    '\n'.join(
                        '- `' + path + '`' + (' — ' + str(count) + ' tệp thay đổi' if is_folder else '')
                        for path, count, is_folder in groups
                    )
                    + '\n\n'
                )
            else:
                lines.append('Merge commit / không có tệp thay đổi trực tiếp.\n\n')
    lines.append('## Pull Request liên quan\n\n| PR | Nội dung | Nhánh | Trạng thái tại thời điểm chốt |\n| --- | --- | --- | --- |\n')
    for p in snapshot['pull_requests']:
        if (
            p['headRefName'].startswith('docs/t2-')
            or p['headRefName'] in {'merge-template2', 'docs/scrum-61-clarune-v3', 'feat/ci-scrum43'}
            or p['number'] >= 14
        ):
            lines.append(f'| [#{p["number"]}]({p["url"]}) | {p["title"]} | `{p["headRefName"]}` | {p["state"]} |\n')
    write(T2 / 'git-contributions/git-contributions.md', ''.join(lines))
    return {m['full_name']: len(grouped[m['mssv']]) for m in members}


def render_companion(kind: str, title: str, subtitle: str) -> None:
    folder = T2 / kind
    md = (folder / (kind + '.md')).read_text(encoding='utf-8')
    logo = ROOT / 'reports/template1' / kind / 'hcmus_logo.png'
    shutil.copy2(logo, folder / 'hcmus_logo.png')
    template0.LOGO_PNG = str(folder / 'hcmus_logo.png')
    cover = template0.render_cover_page()
    cover = cover.replace('AI Usage Report', title).replace(
        'Báo cáo Sử dụng Trí tuệ Nhân tạo (AI Usage Transparency &amp; Accountability Report)', subtitle
    )
    cover = cover.replace('28/10/2026', DATE).replace('Đề tài đề xuất:', 'Đề tài:')
    cover = cover.replace(
        'Ghi nhận minh bạch toàn bộ quá trình sử dụng các công cụ Trí tuệ nhân tạo (LLM, AI Coding Assistant, Prompt-based generators) trong đồ án theo đúng quy chuẩn bắt buộc của Khoa CNTT - HCMUS.',
        'Ghi nhận ' + ('việc sử dụng AI' if kind == 'ai-usage' else 'lịch sử Git và đóng góp cá nhân') + ' trong giai đoạn Template 2 của dự án Clarune.',
    )
    cover = cover.replace(
        'Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS',
        'Mục 5 Quy định về việc sử dụng AI trong học phần — Khoa Công nghệ Thông tin, HCMUS'
        if kind == 'ai-usage'
        else 'Đối soát lịch sử Git và truy vết đóng góp cá nhân',
    )
    cover = cover.replace(
        'NMCNPM - AI-Powered Helpdesk &amp; Knowledge Base - Group 04', 'NMCNPM - Clarune - Group 04 | Template 2'
    )
    body = render_reports.simple_markdown_to_html(md)
    # Add thead/tbody structure to tables for paginator header repeating
    def wrap_thead_tbody(match):
        t = match.group(0)
        rows = re.findall(r'<tr>.*?</tr>', t, flags=re.S)
        if not rows:
            return t
        head_row = rows[0]
        body_rows = '\n'.join(rows[1:])
        count = head_row.count('<th>')
        if count == 7:
            widths = [8, 13, 12, 13, 18, 25, 11]
        elif 'Mã Hash' in head_row:
            widths = [7, 15, 20, 50, 8]
        elif count == 2:
            widths = [35, 65]
        elif 'Trạng thái' in head_row:
            widths = [8, 48, 30, 14]
        elif count == 4:
            widths = [16, 34, 34, 16]
        else:
            widths = []
        colgroup = '<colgroup>' + ''.join(f'<col style="width:{x}%">' for x in widths) + '</colgroup>' if widths else ''
        return f'<table>{colgroup}<thead>{head_row}</thead><tbody>{body_rows}</tbody></table>'

    body = re.sub(r'<table>.*?</table>', wrap_thead_tbody, body, flags=re.S)
    extra = '''
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
    script = template0.PAGINATOR_SCRIPT.replace(
        'var c = el.cloneNode(false); if (th) c.appendChild(th.cloneNode(true));',
        'var c = el.cloneNode(false); var cols=el.querySelector("colgroup"); if(cols) c.appendChild(cols.cloneNode(true)); if (th) c.appendChild(th.cloneNode(true));',
    ).replace(
        'newPage(); place([].slice.call(src.children)); src.remove(); toc();',
        'newPage(); place([].slice.call(src.children)); src.remove(); toc(); document.documentElement.dataset.ready="true";',
    )
    header_label = 'Sử dụng AI' if kind == 'ai-usage' else 'Lịch sử Git'
    doc = f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Template 2 — {html.escape(title)}</title><style>{template0.PAGE_CSS}\n{extra}</style></head><body>
{cover}<div id="pages"></div><div id="source">{body}</div>
<template id="tpl-header"><div class="template-header-bar"><div class="header-tab">Nhập môn công nghệ phần mềm</div><div class="header-title">Template 2 — {header_label}</div></div></template>
<template id="tpl-footer"><div class="template-footer-bar"><div class="footer-left">ĐH Khoa học tự nhiên TP HCM | Bộ môn Công nghệ phần mềm</div><div class="footer-tab">Trang <span class="pn"></span></div></div></template>
<a href="#trang-bia" class="back-to-top">▲ Lên đầu trang</a>{script}</body></html>'''
    write(folder / (kind + '.html'), doc)


def build_zip_and_sync_release() -> dict:
    folders = ('ai-usage', 'git-contributions', 'report')
    internal = {'report/assets/manifest.json'}
    files = []
    for folder in folders:
        for path in sorted((T2 / folder).rglob('*')):
            relative = path.relative_to(T2)
            if not path.is_file() or any(part.startswith('.') or part == '__pycache__' for part in relative.parts):
                continue
            if relative.as_posix() not in internal:
                files.append(path)
    names = {p.relative_to(T2).as_posix() for p in files}
    assert {
        'report/Report.pdf',
        'report/report.md',
        'ai-usage/ai-usage.md',
        'ai-usage/ai-usage.html',
        'git-contributions/git-contributions.md',
        'git-contributions/git-contributions.html',
    } <= names

    for path in files:
        if path.suffix not in {'.md', '.html'}:
            continue
        text = path.read_text(encoding='utf-8')
        images = (
            re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
            if path.suffix == '.md'
            else re.findall(r'<img[^>]+src=["\']([^"\']+)', text)
        )
        for src in images:
            if src.startswith(('data:', 'https:', 'http:')):
                continue
            target = (path.parent / src).resolve()
            assert target.is_file(), f'Missing image: {path}: {src}'
            assert target.relative_to(T2.resolve()).as_posix() in names, f'Image excluded from ZIP: {src}'

    target_zip = T2 / '4.zip'
    temp_zip = target_zip.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for folder in folders:
            archive.writestr(folder + '/', b'')
        for path in files:
            archive.write(path, path.relative_to(T2).as_posix())
    with zipfile.ZipFile(temp_zip) as archive:
        assert archive.testzip() is None
        assert {name.split('/')[0] for name in archive.namelist()} == set(folders)
        for path in files:
            assert archive.read(path.relative_to(T2).as_posix()) == path.read_bytes()
    temp_zip.replace(target_zip)

    # Also mirror the 3 submission folders and 4.zip into docs/template2/release/
    RELEASE.mkdir(parents=True, exist_ok=True)
    for folder in folders:
        dst_folder = RELEASE / folder
        if dst_folder.exists():
            shutil.rmtree(dst_folder)
        shutil.copytree(T2 / folder, dst_folder)
    shutil.copy2(target_zip, RELEASE / '4.zip')

    return {
        'zip_path': str(target_zip.relative_to(ROOT)),
        'zip_files': len(files),
        'zip_bytes': target_zip.stat().st_size,
        'zip_sha256': sha(target_zip.read_bytes()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--refresh-git', action='store_true', help='Capture the latest Git refs and PR states')
    args = parser.parse_args()

    stage_sources()
    manifest = build_report()
    ai_index = build_ai()
    git_counts = build_git(refresh=args.refresh_git)
    render_companion('ai-usage', 'AI Usage Report', 'Báo cáo Sử dụng AI — Giai đoạn Template 2')
    render_companion('git-contributions', 'Git Commit History Report', 'Báo cáo Lịch sử Commit &amp; Đóng góp cá nhân — Template 2')
    zip_info = build_zip_and_sync_release()

    verification = {
        'report_wording_preserved': True,
        'pdf_baseline': json.loads((SOURCES / 'report-baseline.json').read_text(encoding='utf-8')),
        'figures_mapped': len(manifest),
        'ai_sources': ai_index,
        'git_commit_counts': git_counts,
        'package': zip_info,
    }
    write(T2 / 'verification.json', json.dumps(verification, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(verification, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
