#!/usr/bin/env python3
"""Validate fidelity, assets, source provenance and (optionally) HTML layout.

python3 scripts/verify_template1.py [--browser] [--screenshots /tmp/template1-qa]
Browser QA requires playwright and a local Chrome/Chromium executable.
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parent))
import package_template1 as package
import markdown

ROOT=package.ROOT
T1=package.T1


def segment_hits_box(a,b,box):
    """Clip any segment, including diagonals, to the open actor/label rectangle."""
    left,top,right,bottom=box
    low,high=0.0,1.0
    for start,delta,minimum,maximum in [(a[0],b[0]-a[0],left,right),(a[1],b[1]-a[1],top,bottom)]:
        if abs(delta)<1e-9:
            if not minimum<start<maximum:return False
        else:
            enter,leave=sorted(((minimum-start)/delta,(maximum-start)/delta))
            low,high=max(low,enter),min(high,leave)
            if low>=high:return False
    return low<high


def check_static():
    raw=package.report_source_path().read_text()
    report=(T1/'report/report.md').read_text()
    assert package.content_fingerprint(raw)==package.content_fingerprint(report),'Report wording differs'
    baseline=json.loads((T1/'sources/report-baseline.json').read_text())
    assert package.sha((T1/baseline['authority']).read_bytes())==baseline['pdf_sha256'],'PDF baseline changed; review the new PDF first'
    assert package.sha(package.report_source_path().read_bytes())==baseline['markdown_sha256'],'Reviewed transcription changed'
    review_path=T1/'sources/pdf-sync-review.json'
    if review_path.exists():
        review=json.loads(review_path.read_text())
        assert review['pdf_sha256']==baseline['pdf_sha256'] and review['transcription_sha256']==baseline['markdown_sha256'], 'PDF synchronization review is stale'
        assert review['pages']==baseline['pages'] and len(review['figures'])==37
        assert review['ui_images_verified_against_pdf']==31
        assert not review['other_body_changes_after_documented_layout_normalization']
    from report_sync import working_documents
    for path, expected in working_documents(T1,report).items():
        assert path.read_text()==expected, f'Working document is stale: {path}'
    assert 'data:image' not in report and '[image' not in report
    assets=json.loads((T1/'report/assets/manifest.json').read_text())
    assert len(assets)==37 and len(set(x['asset'] for x in assets))==37
    for x in assets:
        p=T1/'report'/x['asset'];assert p.is_file(),p
        assert package.sha(p.read_bytes())==x['sha256'],p
        if x['source']:
            assert p.read_bytes()==(ROOT/x['source']).read_bytes(),p
    ui=list((T1/'report/assets/ui').glob('*.png'));assert len(ui)==31
    assert set('assets/ui/'+p.name for p in ui)=={x['asset'] for x in assets if x['source']}
    assert len(re.findall(r'^\| Use case ID \| UC-',report,re.M))==19
    # Every final UC table is retained literally, not just its normalized wording.
    for table in re.findall(r'\| Use case ID \| UC-\d+ \|\n(?:\|[^\n]*\n)+',raw):
        assert table in report
        assert len(table.rstrip().splitlines())==10
    from diagrams import uc_names, display_uc_name
    names=uc_names(raw)
    diagrams=json.loads((T1/'report/assets/diagrams/semantics.json').read_text())
    assert len(diagrams)==6
    for drawing in diagrams:
        folder=T1/'report/assets/diagrams'
        ET.parse(folder/(drawing['name']+'.svg'));ET.parse(folder/(drawing['name']+'.drawio'))
        if 'provenance' in drawing:
            for suffix,item in drawing['provenance']['files'].items():
                asset=folder/(drawing['name']+'.'+suffix)
                assert package.sha((ROOT/item['path']).read_bytes())==item['sha256'], 'Archived context source changed'
                assert asset.is_file()
            context=ET.parse(folder/(drawing['name']+'.svg'))
            visible=' '.join(n.text or '' for n in context.iter() if n.tag.endswith('text'))
            assert 'Yêu cầu đặt lại mật khẩu' not in visible and 'Xem thống kê' not in visible
            assert 'Support Agent' in visible and 'System Administrator' in visible
            assert ET.fromstring(context.getroot().get('content')).tag=='mxfile'
        ids={n['id'] for n in drawing['nodes']}
        for e in drawing['edges']:assert e['source'] in ids and e['target'] in ids
        for n in drawing['nodes']:
            if n['kind']=='uc':
                number=int(n['id'][3:]);assert ' '.join(n['lines'][1:])==display_uc_name(names[number])
                assert n['lines'][0]==f'UC-{number:02}'+(' (P1)' if number in [16,17,19] else '')
    overall=diagrams[1]
    assert len([n for n in overall['nodes'] if n['kind']=='uc'])==19
    def normalized_edges(drawing):
        edges=set()
        for e in drawing['edges']:
            if e['generalization']:continue
            a,b=e['source'],e['target']
            if a.startswith('uc-'):a,b=b,a
            edges.add((a.replace('actor-embed','actor-llm'),b))
        return edges
    assert normalized_edges(overall)==set.union(*(normalized_edges(d) for d in diagrams[2:]))
    for drawing in diagrams[1:3]:
        inheritance={(e['source'],e['target']) for e in drawing['edges'] if e['generalization']}
        assert inheritance=={(actor,'actor-auth') for actor in ['actor-customer','actor-agent','actor-admin']}
    for drawing in diagrams[1:]:
        boundary=next(n for n in drawing['nodes'] if n['kind']=='boundary')
        usecases=sorted((n for n in drawing['nodes'] if n['kind']=='uc'),key=lambda n:n['y'])
        top=usecases[0]['y']-boundary['y']
        bottom=boundary['y']+boundary['h']-usecases[-1]['y']-usecases[-1]['h']
        assert top==bottom==65, f"Uneven boundary padding: {drawing['name']}"
        assert all(b['y']-a['y']-a['h']==26 for a,b in zip(usecases,usecases[1:]))
        # Lines must clear unrelated actors, including the labels below their bodies.
        actors=[n for n in drawing['nodes'] if n['kind']=='actor']
        if drawing['name']=='uc_module_d_identity':
            parent=next(n for n in actors if n['id']=='actor-auth')
            children=[n for n in actors if n['id'] in ['actor-customer','actor-agent','actor-admin']]
            assert len({n['y'] for n in children})==1 and parent['y']<children[0]['y']
            for edge in drawing['edges']:
                if edge['generalization']:
                    assert all(x<boundary['x']-25 for x,y in edge['points']), 'Identity inheritance must stay beside the system'
                    assert edge['points'][-2][1]>edge['points'][-1][1], 'Inheritance arrow must point upward to parent'
        svg=ET.parse(T1/'report/assets/diagrams'/(drawing['name']+'.svg'))
        lines=svg.findall('.//{http://www.w3.org/2000/svg}polyline')
        assert len(lines)==len(drawing['edges']), 'Every relationship needs its own visible line'
        assert len(svg.findall('.//{http://www.w3.org/2000/svg}circle'))==len(actors), 'No association junction dots'
        drawio=ET.parse(T1/'report/assets/diagrams'/(drawing['name']+'.drawio'))
        cells={cell.get('id'):cell for cell in drawio.iter('mxCell')}
        for actor in actors:
            assert float(cells[actor['id']].find('mxGeometry').get('width'))==46, 'Actor body must not stretch to label width'
        for i,(edge,line) in enumerate(zip(drawing['edges'],lines)):
            assert (line.get('data-source'),line.get('data-target'))==(edge['source'],edge['target'])
            style=cells[f'edge-{i}'].get('style')
            if edge['generalization']:
                assert line.get('marker-end')=='url(#generalization)'
                assert 'endArrow=block;endFill=0;' in style
                clearance=(boundary['x']-25,boundary['y']-25,
                           boundary['x']+boundary['w']+25,boundary['y']+boundary['h']+25)
                for a,b in zip(edge['points'],edge['points'][1:]):
                    assert not segment_hits_box(a,b,clearance), f"Generalization too close to system boundary: {drawing['name']}"
                canvas_width=float(svg.getroot().get('width'))
                canvas_height=float(svg.getroot().get('height'))
                assert all(25<=x<=canvas_width-25 and 25<=y<=canvas_height-25 for x,y in edge['points']), 'Generalization needs canvas margins'
            else:
                assert line.get('marker-end') is None and 'endArrow=none;' in style
                assert len(edge['points'])==2, 'Actor–UC associations must be single straight segments'
                assert not cells[f'edge-{i}'].findall('.//mxPoint'), 'No drawio waypoints on associations'
        ports={}
        segments=[]
        uc_lines={}
        for edge in drawing['edges']:
            for actor in actors:
                cx=actor['x']+actor['w']/2
                canvas_width=float(svg.getroot().get('width'))
                label_left,label_right=(cx-218,cx+12) if cx<canvas_width/2 else (cx-12,cx+218)
                label_top,label_bottom=actor['y']+92,actor['y']+140
                if actor.get('label_above'):
                    label_left,label_right=cx-115,cx+115
                    label_top,label_bottom=actor['y']-55,actor['y']-10
                for a,b in zip(edge['points'],edge['points'][1:]):
                    assert not segment_hits_box(a,b,(label_left,label_top,label_right,label_bottom)), f"Line crosses label {actor['id']}: {drawing['name']}"
                if actor['id'] in (edge['source'],edge['target']):continue
                left,right=(cx-218,cx+23) if cx<canvas_width/2 else (cx-23,cx+218)
                top,bottom=actor['y'],actor['y']+140
                for (x1,y1),(x2,y2) in zip(edge['points'],edge['points'][1:]):
                    hits=segment_hits_box((x1,y1),(x2,y2),(left,top,right,bottom))
                    assert not hits, f"Line crosses {actor['id']}: {drawing['name']}"
            if not edge['generalization']:
                uc=edge['target'] if edge['target'].startswith('uc-') else edge['source']
                port=edge['points'][-1] if uc==edge['target'] else edge['points'][0]
                assert tuple(port) not in ports.setdefault(uc,set()), f'Shared UC port: {uc}'
                ports[uc].add(tuple(port))
                uc_lines.setdefault(uc,[]).append(edge['points'])
                segments.extend(zip(edge['points'],edge['points'][1:]))
        for uc,connections in uc_lines.items():
            def orientation(a,b,c):
                return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
            for i,(a,b) in enumerate(connections):
                for c,d in connections[i+1:]:
                    crossing=orientation(a,b,c)*orientation(a,b,d)<0 and orientation(c,d,a)*orientation(c,d,b)<0
                    assert not crossing, f"Crossing lines into {uc}: {drawing['name']}"
        # Distinct associations may intersect, but must not share a length of line.
        for i,(a,b) in enumerate(segments):
            dx,dy=b[0]-a[0],b[1]-a[1]
            for c,d in segments[i+1:]:
                cross=lambda p:dx*(p[1]-a[1])-dy*(p[0]-a[0])
                if abs(cross(c))>1e-6 or abs(cross(d))>1e-6:continue
                axis=0 if abs(dx)>abs(dy) else 1
                overlap=min(max(a[axis],b[axis]),max(c[axis],d[axis]))-max(min(a[axis],b[axis]),min(c[axis],d[axis]))
                assert overlap<1e-6, f"Overlapping association segments: {drawing['name']}"
        edges=normalized_edges(drawing)
        assert ('actor-admin','uc-19') not in edges
        assert ('actor-agent','uc-17') not in edges
        if drawing['name'] in ['uc_module_b_kb','uc_module_a_ai_analytics']:
            assert all(n['kind']!='note' for n in drawing['nodes']), 'No explanatory captions inside diagram images'
    ai=(T1/'ai-usage/ai-usage.md').read_text()
    index=json.loads((T1/'verification.json').read_text())['ai_sources']
    for item in index:
        source=(T1/item['source']).read_text()
        rows=[l for l in source.splitlines() if l.startswith('|') and item['mssv'] in l]
        blocks=[b for b in package.extract_sessions(source) if item['mssv'] in b]
        assert len(rows)==item['summary_rows'] and len(blocks)==item['detailed_sessions']
        key=Path(item['source']).stem.removeprefix('ai-usage-')
        block_by_id={re.match(r'### Phiên (T1-\d+):',b)[1]:b for b in blocks}
        for row in rows:
            old=re.match(r'\| \*\*(T1-\d+)\*\*',row)[1]
            expected=package.ai_submission_text(package.ai_summary_row(row,block_by_id[old]),key,item['report_ids'])
            assert expected in ai
        for block in blocks:
            assert package.ai_submission_text(block,key,item['report_ids']) in ai
    expected_ids=[f'T1-{i:02}' for i in range(1,24)]
    assert re.findall(r'^\| \*\*(T1-\d+)\*\*',ai,re.M)==expected_ids
    assert re.findall(r'^#### Phiên (T1-\d+):',ai,re.M)==expected_ids
    assert 'không ghi nhận' not in ai
    assert not re.search(r'\t\d+',report.split('# **1 Bảng đánh giá thành viên')[0])
    source_manifest=json.loads((T1/'sources/member-sources.json').read_text())
    for name,item in source_manifest.items():
        assert package.sha((T1/f'sources/ai-usage-{name}.md').read_bytes())==item['sha256']
    snapshot=json.loads((T1/'sources/git-snapshot.json').read_text());gitmd=(T1/'git-contributions/git-contributions.md').read_text()
    shas=[c['sha'] for c in snapshot['commits']];assert len(shas)==len(set(shas))
    for c in snapshot['commits']:
        assert package.git('show','-s','--format=%s',c['sha'])==c['subject']
        assert c['sha'] in gitmd
        assert c['subject'].replace('|','&#124;') in gitmd or c['subject'] in gitmd
        coverage=[]
        for path,count,is_folder in package.summarize_changed_paths(c['files']):
            covered=[f for f in c['files'] if f.startswith(path)] if is_folder else [path]
            assert len(covered)==count
            coverage.extend(covered)
        assert sorted(coverage)==sorted(c['files']), 'Grouping lost or duplicated paths'

    print('PASS: report wording, 19 literal UC tables, 37 mapped figures, 31 source-verified UI assets, 6 valid/consistent UML graphs, all AI source entries, unique Git metadata.')


async def check_browser(output):
    from playwright.async_api import async_playwright
    chrome=next((p for p in ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',shutil.which('google-chrome'),shutil.which('chromium')] if p and Path(p).exists()),None)
    if not chrome:raise RuntimeError('Chrome/Chromium not found')
    output.mkdir(parents=True,exist_ok=True)
    results={}
    async with async_playwright() as p:
        browser=await p.chromium.launch(executable_path=chrome,headless=True)
        page=await browser.new_page(viewport={'width':1280,'height':1500},device_scale_factor=1)
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        for kind in ['ai-usage','git-contributions']:
            await page.goto((T1/kind/(kind+'.html')).as_uri())
            await page.wait_for_function('document.documentElement.dataset.ready === "true"',timeout=60000)
            overflow=await page.locator('.page-body').evaluate_all('(xs)=>xs.map((x,i)=>({page:i+1,h:x.scrollHeight-x.clientHeight,w:x.scrollWidth-x.clientWidth})).filter(x=>x.h>1||x.w>1)')
            assert not overflow,(kind,overflow)
            content=' '.join(await page.locator('.page-body').all_text_contents())
            expected=markdown.markdown((T1/kind/(kind+'.md')).read_text(),extensions=['tables','fenced_code','sane_lists'],tab_length=2)
            # Browser-normalized text catches omitted source blocks; repeated table headers are allowed.
            def words(t):return re.findall(r'\S+',t)
            got=' '.join(words(content))
            # Compare every sentence-sized text node in its original order, ignoring repeated headers.
            nodes=await page.evaluate('(s)=>{let d=document.createElement("div");d.innerHTML=s;let w=document.createTreeWalker(d,NodeFilter.SHOW_TEXT),a=[];while(w.nextNode()){let t=w.currentNode.textContent.trim();if(t)a.push(t)}return a}',expected)
            cursor=0
            for text in nodes:
                needle=' '.join(words(text))
                # Splitting paragraphs can drop one joining whitespace; source text is otherwise exact.
                pos=got.find(needle,cursor)
                assert pos>=0,(kind,'Missing rendered text',needle[:120])
                cursor=pos+len(needle)
            pages=await page.locator('.page').count()
            for i in sorted(set([0,min(1,pages-1),pages//2,pages-1])):
                await page.locator('.page').nth(i).screenshot(path=str(output/f'{kind}-page-{i+1}.png'))
            await page.locator('.cover-page').screenshot(path=str(output/f'{kind}-cover.png'))
            results[kind]={'pages':pages,'overflow':overflow,'rendered_source_nodes':len(nodes)}
        # Preview report only for QA; the requested deliverable is report.md, PDF is supplied by the leader.
        md=(T1/'report/report.md').read_text()
        rendered=markdown.markdown(md,extensions=['tables','fenced_code','sane_lists'],tab_length=2)
        preview=output/'report-preview.html'
        preview.write_text('<!doctype html><html lang="vi"><head><meta charset="utf-8"><base href="'+(T1/'report').as_uri()+'/"><style>body{font:17px/1.55 "Times New Roman",serif;margin:40px auto;max-width:1100px;padding:20px}img{max-width:100%;height:auto;display:block;margin:20px auto}table{border-collapse:collapse;width:100%;font-size:15px;overflow-wrap:anywhere}td,th{border:1px solid #999;padding:7px;vertical-align:top}h1,h2,h3{color:#254b78}a{overflow-wrap:anywhere}</style></head><body>'+rendered+'</body></html>')
        await page.goto(preview.as_uri());await page.wait_for_function('Array.from(document.images).every(x=>x.complete)')
        bad=await page.locator('img').evaluate_all('(xs)=>xs.filter(x=>!x.naturalWidth).map(x=>x.src)');assert not bad,bad
        broken=await page.locator('a[href^="#"]').evaluate_all('(xs)=>xs.filter(x=>!document.getElementById(decodeURIComponent(x.hash.slice(1)))).map(x=>x.hash)')
        assert not broken,('Broken report anchors',broken)
        for i in [0,1,2,3,4,5,6,8,24,30,36]:
            await page.locator('img').nth(i).screenshot(path=str(output/f'report-image-{i+1}.png'))
        assert not errors,errors
        results['report']={'images':await page.locator('img').count(),'broken_images':bad,'broken_anchors':broken}
        await browser.close()
    (output/'browser-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    record=dict(results)
    record['command']='python scripts/verify_template1.py --browser'
    baseline=json.loads((T1/'sources/report-baseline.json').read_text())
    record['review_date']=baseline['review_date']
    record['pdf_sha256']=baseline['pdf_sha256']
    record['files_sha256']={path:package.sha((T1/path).read_bytes()) for path in [
        'report/report.md','ai-usage/ai-usage.md','ai-usage/ai-usage.html',
        'git-contributions/git-contributions.md','git-contributions/git-contributions.html']}
    (T1/'browser-validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print('PASS browser:',json.dumps(results,ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--browser',action='store_true');parser.add_argument('--screenshots',type=Path,default=Path('/tmp/clarune-template1-qa'));args=parser.parse_args()
    check_static()
    if args.browser:
        import asyncio
        asyncio.run(check_browser(args.screenshots))
