#!/usr/bin/env python3
"""Create the three-folder Template 1 submission without repository QA files."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
T1 = ROOT / 'reports/template1'
FOLDERS = ('ai-usage', 'git-contributions', 'report')
INTERNAL = {'report/assets/manifest.json', 'report/assets/diagrams/semantics.json'}


def main():
    files = []
    for folder in FOLDERS:
        for path in sorted((T1 / folder).rglob('*')):
            relative = path.relative_to(T1)
            if not path.is_file() or any(part.startswith('.') or part == '__pycache__' for part in relative.parts):
                continue
            if relative.as_posix() not in INTERNAL:
                files.append(path)
    names = {p.relative_to(T1).as_posix() for p in files}
    assert {'report/Report.pdf', 'report/report.md', 'ai-usage/ai-usage.md',
            'ai-usage/ai-usage.html', 'git-contributions/git-contributions.md',
            'git-contributions/git-contributions.html'} <= names
    for path in files:
        if path.suffix not in {'.md', '.html'}:
            continue
        text = path.read_text(encoding='utf-8')
        for phrase in ['../sources/git-snapshot.json', 'Metadata/đường dẫn đầy đủ',
                       'các commit phát sinh sau thời điểm này không nằm trong snapshot',
                       'Chưa có xác nhận review của tác giả/reviewer', 'TODO', 'FIXME']:
            assert phrase not in text, f'Internal note in {path}: {phrase}'
        images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text) if path.suffix == '.md' else re.findall(r'<img[^>]+src=["\']([^"\']+)', text)
        for src in images:
            if src.startswith(('data:', 'https:', 'http:')):
                continue
            target = (path.parent / src).resolve()
            assert target.is_file(), f'Missing image: {path}: {src}'
            assert target.relative_to(T1.resolve()).as_posix() in names, f'Image excluded from ZIP: {src}'
    target = T1 / '4.zip'
    temporary = target.with_suffix('.zip.tmp')
    with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for folder in FOLDERS:
            archive.writestr(folder + '/', b'')
        for path in files:
            archive.write(path, path.relative_to(T1).as_posix())
    with zipfile.ZipFile(temporary) as archive:
        assert archive.testzip() is None
        assert {name.split('/')[0] for name in archive.namelist()} == set(FOLDERS)
        for path in files:
            assert archive.read(path.relative_to(T1).as_posix()) == path.read_bytes()
    temporary.replace(target)
    print(f'{target}: {len(files)} files, {target.stat().st_size:,} bytes')
    print('SHA-256:', hashlib.sha256(target.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
