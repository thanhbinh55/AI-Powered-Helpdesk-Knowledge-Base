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


def check_static():
    raw=(T1/'sources/template1-final-original.md').read_text()
    report=(T1/'report/report.md').read_text()
    assert package.content_fingerprint(raw)==package.content_fingerprint(report),'Report wording differs'
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
    from diagrams import uc_names
    names=uc_names(raw)
    diagrams=json.loads((T1/'report/assets/diagrams/semantics.json').read_text())
    assert len(diagrams)==6
    for drawing in diagrams:
        folder=T1/'report/assets/diagrams'
        ET.parse(folder/(drawing['name']+'.svg'));ET.parse(folder/(drawing['name']+'.drawio'))
        ids={n['id'] for n in drawing['nodes']}
        for e in drawing['edges']:assert e['source'] in ids and e['target'] in ids
        for n in drawing['nodes']:
            if n['kind']=='uc':
                number=int(n['id'][3:]);assert ' '.join(n['lines'][1:])==names[number]
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
    for drawing in diagrams[1:]:
        edges=normalized_edges(drawing)
        assert ('actor-admin','uc-19') not in edges
        assert ('actor-agent','uc-17') not in edges
    ai=(T1/'ai-usage/ai-usage.md').read_text()
    index=json.loads((T1/'verification.json').read_text())['ai_sources']
    for item in index:
        source=(T1/item['source']).read_text()
        rows=[l for l in source.splitlines() if l.startswith('|') and item['mssv'] in l]
        blocks=[b for b in package.extract_sessions(source) if item['mssv'] in b]
        assert len(rows)==item['summary_rows'] and len(blocks)==item['detailed_sessions']
        for text in rows+blocks:assert text in ai
    source_manifest=json.loads((T1/'sources/member-sources.json').read_text())
    for name,item in source_manifest.items():
        assert package.sha((T1/f'sources/ai-usage-{name}.md').read_bytes())==item['sha256']
    snapshot=json.loads((T1/'sources/git-snapshot.json').read_text());gitmd=(T1/'git-contributions/git-contributions.md').read_text()
    shas=[c['sha'] for c in snapshot['commits']];assert len(shas)==len(set(shas))
    for c in snapshot['commits']:
        assert package.git('show','-s','--format=%s',c['sha'])==c['subject']
        assert c['sha'] in gitmd
        assert c['subject'].replace('|','&#124;') in gitmd or c['subject'] in gitmd
    print('PASS: report wording, 19 literal UC tables, 37 mapped figures, 31 original UI assets, 6 valid/consistent UML graphs, all AI source entries, unique Git metadata.')


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
    print('PASS browser:',json.dumps(results,ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--browser',action='store_true');parser.add_argument('--screenshots',type=Path,default=Path('/tmp/clarune-template1-qa'));args=parser.parse_args()
    check_static()
    if args.browser:
        import asyncio
        asyncio.run(check_browser(args.screenshots))
