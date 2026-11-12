"""Derive the working Template 1 documents from the reviewed final report."""
import os
import re


SECTION_FILES = {
    '01-danh-gia-thanh-vien.md': ('1',),
    '02-mo-ta-bai-toan.md': ('2',),
    '03-tong-quan-yeu-cau/03.1-stakeholders.md': ('3.1',),
    '03-tong-quan-yeu-cau/03.2.1-yeu-cau-chuc-nang.md': ('3.2.1',),
    '03-tong-quan-yeu-cau/03.2.2-yeu-cau-phi-chuc-nang.md': ('3.2.2',),
    '04-dac-ta-use-cases/04.1-so-do-tong-the.md': ('4.1',),
    '04-dac-ta-use-cases/04.2-module-D-identity.md': ('4.2.1', '4.2.2', '4.2.3', '4.2.4', '4.2.5'),
    '04-dac-ta-use-cases/04.2-module-C-ticket.md': ('4.2.6', '4.2.7', '4.2.8', '4.2.9', '4.2.10', '4.2.11'),
    '04-dac-ta-use-cases/04.2-module-B-knowledge.md': ('4.2.12', '4.2.13', '4.2.14'),
    '04-dac-ta-use-cases/04.2-module-A-ai.md': ('4.2.15', '4.2.16', '4.2.18', '4.2.19'),
    '04-dac-ta-use-cases/04.2-uc-17-analytics.md': ('4.2.17',),
    '05-prototype-mockup.md': ('5',),
}


def section(report, number):
    # Each heading's explicit anchor belongs to the heading, not its predecessor.
    blocks = list(re.finditer(r'<a id="[^"]+"></a>\n\n(#{1,6}) \*\*([0-9]+(?:\.[0-9]+)*) ', report))
    start = next(i for i, h in enumerate(blocks) if h[2] == number)
    depth = len(blocks[start][1])
    end = next((h.start() for h in blocks[start + 1:] if len(h[1]) <= depth), len(report))
    return report[blocks[start].start():end].strip() + '\n'


def relocate_images(text, target, report_dir):
    prefix = os.path.relpath(report_dir, target.parent)
    text = re.sub(r'!\[\]\((assets/[^)]+)\)', lambda m: f'![]({prefix}/{m[1]})', text)
    return '\n'.join(line.rstrip() for line in text.splitlines()) + '\n'


def working_documents(t1, report):
    documents = {}
    for relative, sections in SECTION_FILES.items():
        target = t1 / relative
        pdf = os.path.relpath(t1 / 'report/Report.pdf', target.parent)
        full = os.path.relpath(t1 / 'report/report.md', target.parent)
        notice = (f'> Đồng bộ theo [Report.pdf]({pdf}) ngày 12/11/2026. '
                  f'Nội dung trích từ [report.md]({full}); ảnh dùng chung với bản final.\n\n')
        content = '\n'.join(section(report, n) for n in sections)
        documents[target] = notice + relocate_images(content, target, t1 / 'report')
    target = t1 / 'TEMPLATE1_DRAFT_MASTER.md'
    documents[target] = ('> Bản master đồng bộ theo [Report.pdf](report/Report.pdf) ngày 12/11/2026. '
                         'Tên tệp được giữ để các liên kết hiện có tiếp tục hoạt động. '
                         'Bản nháp trước khi chốt được lưu tại '
                         '[sources/history/template1-master-before-final-pdf.md](sources/history/template1-master-before-final-pdf.md).\n\n'
                         + relocate_images(report, target, t1 / 'report'))
    return documents


def sync_working_documents(t1, report):
    for target, text in working_documents(t1, report).items():
        target.write_text(text, encoding='utf-8')
