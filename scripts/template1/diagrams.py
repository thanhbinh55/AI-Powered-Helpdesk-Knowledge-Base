"""Vector UML diagrams derived from the existing drawio graphs and final UC tables."""
from pathlib import Path
import html
import shutil
import json
import math
import statistics
import re
import textwrap
import xml.etree.ElementTree as ET

STYLE = 'font-family:Arial,sans-serif;font-size:16px;fill:#111'
ACTORS = {
    'actor-guest': ['Guest / Unauthenticated User', '(Người dùng chưa xác thực)'],
    'actor-auth': ['Authenticated User', '(Người dùng đã xác thực)'],
    'actor-customer': ['Customer', '(Khách hàng)'],
    'actor-agent': ['Support Agent', '(Nhân viên hỗ trợ)'],
    'actor-admin': ['System Administrator', '(Quản trị viên hệ thống)'],
    'actor-mail': ['«system»', 'External Mail Service Provider'],
    'actor-llm': ['«system»', 'Embedding / LLM Provider'],
    'actor-embed': ['«system»', 'Embedding / LLM Provider'],
}
BASELINES = ['uc_overall_19_usecases', 'uc_module_d_identity', 'uc_module_c_ticketing',
             'uc_module_b_kb', 'uc_module_a_ai_analytics']
TITLES = ['Clarune — Tổng thể 19 Use Case', 'Clarune — Định danh và phân quyền',
          'Clarune — Quản lý ticket', 'Clarune — Cơ sở tri thức',
          'Clarune — Trợ lý AI']
ORDERS = [[1,16,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,17],
          [1,16,2,3,4], [5,6,7,8,9,10], [11,12,13], [14,15,18,19,17]]


def uc_names(source):
    names = {}
    for block in re.split(r'(?=^### \*\*4\.2\.)', source, flags=re.M)[1:]:
        match = re.search(r'^\| Use case ID \| UC-(\d+) \|', block, re.M)
        label = re.search(r'^\| \*\*Tên Use Case\*\* \| (.+?) \|', block, re.M)
        if match and label:
            names[int(match[1])] = label[1]
    assert len(names) == 19, names
    return names


def display_uc_name(name):
    return re.sub(r'\s*\(P1\)', '', name).strip()


class Diagram:
    def __init__(self, title, width, height):
        self.title, self.width, self.height = title, width, height
        self.nodes, self.edges = [], []

    def node(self, ident, kind, x, y, w, h, lines):
        self.nodes.append(dict(id=ident, kind=kind, x=x, y=y, w=w, h=h, lines=lines))

    def edge(self, source, target, points, generalization=False, arrow=False, label=''):
        self.edges.append(dict(source=source, target=target, points=points,
                               generalization=generalization, arrow=arrow, label=label))

    def write(self, folder, name):
        folder.mkdir(parents=True, exist_ok=True)
        esc = html.escape
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" role="img" aria-labelledby="title">',
               f'<title id="title">{esc(self.title)}</title>',
               '<defs><marker id="generalization" viewBox="0 0 14 14" markerWidth="14" markerHeight="14" refX="13" refY="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L13 7 L1 13 Z" fill="white" stroke="#111" stroke-width="1.5"/></marker><marker id="arrow" viewBox="0 0 10 10" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="#111" stroke-width="1.5"/></marker></defs>',
               '<rect width="100%" height="100%" fill="white"/>', f'<g style="{STYLE}">']
        # Boundaries first, associations second, nodes last: lines never obscure labels.
        for n in self.nodes:
            if n['kind'] == 'boundary':
                out += [f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" fill="white" stroke="#111" stroke-width="1.7"/>',
                        f'<text x="{n["x"]+n["w"]/2}" y="{n["y"]+28}" text-anchor="middle" font-weight="bold">{esc(n["lines"][0])}</text>']
        for e in self.edges:
            marker = ' marker-end="url(#generalization)"' if e['generalization'] else (' marker-end="url(#arrow)"' if e['arrow'] else '')
            points=' '.join(f'{x},{y}' for x,y in e['points'])
            out.append(f'<polyline data-source="{e["source"]}" data-target="{e["target"]}" points="{points}" fill="none" stroke="#111" stroke-width="1.45" stroke-linejoin="round"'+marker+'/>')
            if e['label']:
                p=e['points'][len(e['points'])//2]
                for j,line in enumerate(e['label'].split('\n')):
                    out.append(f'<text x="{p[0]}" y="{p[1]-10+j*20}" text-anchor="middle" font-size="15" paint-order="stroke" stroke="white" stroke-width="5" stroke-linejoin="round">{esc(line)}</text>')
        for n in self.nodes:
            x,y,w,h=n['x'],n['y'],n['w'],n['h'];cx=x+w/2
            if n['kind']=='boundary': continue
            if n['kind']=='actor':
                out += [f'<circle cx="{cx}" cy="{y+13}" r="11" fill="white" stroke="#111" stroke-width="1.7"/>',
                        f'<path d="M{cx} {y+24} V{y+57} M{cx-23} {y+36} H{cx+23} M{cx} {y+57} L{cx-22} {y+82} M{cx} {y+57} L{cx+22} {y+82}" fill="none" stroke="#111" stroke-width="1.7"/>']
                ty=y+108
                if n.get('label_above'):ty=y-40
            elif n['kind']=='uc':
                out.append(f'<ellipse cx="{cx}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="white" stroke="#111" stroke-width="1.7"/>')
                ty=y+h/2-(len(n['lines'])-1)*11+5
            elif n['kind']=='note':
                ty=y+h/2-(len(n['lines'])-1)*11+5
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#111" stroke-width="1.7"/>')
                ty=y+h/2-(len(n['lines'])-1)*11+5
            for i,line in enumerate(n['lines']):
                weight=' font-weight="bold"' if n['kind']=='uc' and i==0 else ''
                label_x=cx;anchor='middle'
                if n['kind']=='actor':
                    label_x=cx+12 if cx<self.width/2 else cx-12
                    anchor='end' if cx<self.width/2 else 'start'
                    if n.get('label_above'):label_x=cx;anchor='middle'
                out.append(f'<text x="{label_x}" y="{ty+i*22}" text-anchor="{anchor}"{weight}>{esc(line)}</text>')
        out += ['</g></svg>'];(folder/(name+'.svg')).write_text('\n'.join(out)+'\n')
        mx=ET.Element('mxfile',host='app.diagrams.net',type='device',version='24.0.0')
        di=ET.SubElement(mx,'diagram',id=name,name=self.title)
        model=ET.SubElement(di,'mxGraphModel',grid='1',gridSize='10',page='1',pageScale='1',pageWidth=str(self.width),pageHeight=str(self.height))
        root=ET.SubElement(model,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
        def bounds(node):
            if node['kind']=='actor':
                return node['x']+node['w']/2-23,node['y'],46,node['h']
            return node['x'],node['y'],node['w'],node['h']
        for n in self.nodes:
            styles={'boundary':'shape=rect;verticalAlign=top;spacingTop=12;fontStyle=1;', 'actor':'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;align=center;labelWidth=230;spacingTop=14;', 'uc':'ellipse;', 'box':'shape=rect;', 'note':'shape=text;align=center;verticalAlign=middle;'}
            if n['kind']=='actor':
                styles['actor']+=('labelPosition=left;align=right;spacingRight=-35;' if n['x']+n['w']/2<self.width/2 else 'labelPosition=right;align=left;spacingLeft=-35;')
                if n.get('label_above'):
                    styles['actor']='shape=umlActor;verticalLabelPosition=top;verticalAlign=bottom;labelPosition=center;align=center;labelWidth=230;spacingBottom=18;'
            c=ET.SubElement(root,'mxCell',id=n['id'],value='<br>'.join(esc(a) for a in n['lines']),style=styles[n['kind']]+'html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#111111;fontColor=#111111;strokeWidth=1.7;fontSize=16;fontFamily=Arial;',vertex='1',parent='1')
            if n['kind']=='note':c.set('style',c.get('style')+'fillColor=none;strokeColor=none;')
            x,y,w,h=bounds(n)
            ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),**{'as':'geometry'})
        for i,e in enumerate(self.edges):
            style='edgeStyle=none;html=1;strokeColor=#111111;strokeWidth=1.45;jumpStyle=none;'
            # Preserve the SVG ports instead of letting drawio reconnect through labels.
            source=next(n for n in self.nodes if n['id']==e['source'])
            target=next(n for n in self.nodes if n['id']==e['target'])
            for prefix,node,point in [('exit',source,e['points'][0]),('entry',target,e['points'][-1])]:
                x,y,w,h=bounds(node)
                style+=f'{prefix}X={(point[0]-x)/w};{prefix}Y={(point[1]-y)/h};{prefix}Perimeter=0;'
            style+=('endArrow=block;endFill=0;endSize=14;' if e['generalization'] else ('endArrow=open;' if e['arrow'] else 'endArrow=none;'))
            c=ET.SubElement(root,'mxCell',id='edge-'+str(i),value=e['label'],style=style,edge='1',parent='1',source=e['source'],target=e['target'])
            g=ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'});pts=ET.SubElement(g,'Array',**{'as':'points'})
            for x,y in e['points'][1:-1]: ET.SubElement(pts,'mxPoint',x=str(x),y=str(y))
        ET.indent(mx);ET.ElementTree(mx).write(folder/(name+'.drawio'),encoding='utf-8',xml_declaration=True)
        return {'name':name,'title':self.title,'nodes':self.nodes,'edges':self.edges}


def generate(repo, source):
    folder=repo/'reports/template1/report/assets/diagrams';names=uc_names(source);records=[]
    for index,baseline in enumerate(BASELINES):
        graph=ET.parse(repo/'reports/template1/assets/diagrams'/(baseline+'.drawio'))
        edges=[]
        for e in graph.iter('mxCell'):
            if e.get('edge')!='1':continue
            a,b=e.get('source'),e.get('target')
            general='endFill=0' in e.get('style','')
            if general and not b:b='actor-auth'
            if a and b:edges.append((a,b,general))
        if index==1:
            edges += [('actor-customer','actor-auth',True),('actor-agent','actor-auth',True)]
        order=ORDERS[index];overall=index==0
        # One semantic relation per actor/UC; user roles inherit only session/profile.
        actors=[a for a in ACTORS if any(a in (x,y) for x,y,g in edges)]
        left=[a for a in actors if a not in ['actor-admin','actor-mail','actor-llm','actor-embed']]
        if index==1:left.append('actor-admin')
        right=[a for a in actors if a not in left]
        width=1560 if overall else 1320; center=width/2;ux=center-240;uw=480
        if index==1:
            width=1800;center=1080;ux=center-240
        # Size the boundary to the UC stack, with identical top/bottom padding.
        # A fixed minimum height leaves short modules with a large empty footer.
        boundary_y=25; padding=65; uc_height=86; row_step=112
        first_y=boundary_y+padding
        boundary_height=2*padding+uc_height+(len(order)-1)*row_step
        height=boundary_y+boundary_height+25
        boundary_bottom=boundary_y+boundary_height
        inheritance_y=boundary_bottom+40
        has_outer_route=any(g and a in right for a,b,g in edges)
        canvas_height=max(height,inheritance_y+40 if has_outer_route else 0)
        d=Diagram(TITLES[index],width,canvas_height)
        d.node('system','boundary',center-280,boundary_y,560,boundary_height,[TITLES[index]])
        positions={}
        for row,n in enumerate(order):
            y=first_y+row*row_step
            d.node(f'uc-{n:02}','uc',ux,y,uw,uc_height,[f'UC-{n:02}'+(' (P1)' if n in [16,17,19] else '')]+textwrap.wrap(display_uc_name(names[n]),width=42,break_long_words=False))
            positions[f'uc-{n:02}']=(ux,y,uw,uc_height)
        # Align each actor with its related UCs, leaving space for actor labels.
        for side,aa in [('left',left),('right',right)]:
            if index==1:
                layout={'actor-guest':(670,65),'actor-auth':(410,250),
                        'actor-customer':(150,500),'actor-agent':(410,500),
                        'actor-admin':(670,500),'actor-mail':(1540,209)}
                for actor in aa:
                    cx,y=layout[actor];x=cx-115
                    d.node(actor,'actor',x,y,230,82,ACTORS[actor])
                    if actor=='actor-auth':d.nodes[-1]['label_above']=True
                    positions[actor]=(x,y,230,82)
                continue
            desired={}
            for actor in aa:
                related=[t if s==actor else s for s,t,g in edges if not g and actor in (s,t)]
                centers=[positions[uc][1]+positions[uc][3]/2 for uc in related]
                desired[actor]=statistics.median(centers)-36 if centers else height/2-80
            ordered=sorted(aa,key=lambda actor:desired[actor])
            spacing=min(300,(height-240)/max(1,len(ordered)-1))
            ys=[]
            for actor in ordered:
                ys.append(max(65,desired[actor],ys[-1]+spacing if ys else 65))
            for j in range(len(ys)-1,-1,-1):
                ys[j]=min(ys[j],height-175 if j==len(ys)-1 else ys[j+1]-spacing)
            for actor,y in zip(ordered,ys):
                x=145 if side=='left' else width-375
                d.node(actor,'actor',x,y,230,82,ACTORS[actor])
                positions[actor]=(x,y,230,82)
        # Each association has its own path; never merge them into a junction/bus.
        for a,b,general in edges:
            ax,ay,aw,ah=positions[a];bx,by,bw,bh=positions[b]
            if general:
                if index==1:
                    # Short upward inheritance tree, entirely beside the system.
                    points=[(ax+aw/2,ay+2),(ax+aw/2,420),(bx+bw/2,420),(bx+bw/2,by+82)]
                    p=[point for i,point in enumerate(points) if i==0 or point!=points[i-1]]
                    d.edge(a,b,p,generalization=True)
                    continue
                side='left' if a in left else 'right'
                lane=40
                approach=by-18
                outer=lane if side=='left' else width-40
                cx=bx+bw/2
                head_y=by+2
                if side=='right':
                    # Leave from above the head, separately from the UC association.
                    p=[(ax+aw/2,ay+2),(ax+aw/2,ay-22),(outer,ay-22),(outer,inheritance_y),(lane,inheritance_y),(lane,approach),(cx,approach),(cx,head_y)]
                else:
                    p=[(ax+aw/2-24,ay+36),(outer,ay+36),(outer,approach),(cx,approach),(cx,head_y)]
            else:
                actor=a if a.startswith('actor-') else b;uc=b if actor==a else a
                x,y,w,h=positions[actor];xx,yy,ww,hh=positions[uc]
                aa=left if actor in left else right
                peers=[candidate for candidate in aa if any(not g and {s,t}=={candidate,uc} for s,t,g in edges)]
                # Match port order to actor height to avoid crossings at the ellipse.
                peers.sort(key=lambda candidate:positions[candidate][1])
                offset=(peers.index(actor)-(len(peers)-1)/2)*18
                port_y=yy+hh/2+offset
                radius=ww/2*math.sqrt(1-(offset/(hh/2))**2)
                port_x=xx+ww/2+(-radius if actor in left else radius)
                direction=1 if actor in left else -1
                p=[(x+w/2+direction*24,y+36),(port_x,port_y)]
                if actor!=a:p=p[::-1]
            d.edge(a,b,p,generalization=general)
        records.append(d.write(folder,baseline))
    # Keep the submitted source intact; apply documented corrections to the report copy.
    source_folder=repo/'reports/template1/sources/diagrams'
    provenance=json.loads((source_folder/'context-diagram-source.json').read_text())
    for suffix in ['svg','drawio']:
        shutil.copy2(source_folder/('context_diagram_system.'+suffix),folder/('context_diagram_system.'+suffix))
    context=folder/'context_diagram_system.drawio'
    graph=ET.parse(context)
    values={'actor-guest':'Guest / Unauthenticated User','actor-agent':'Support Agent',
            'actor-admin':'System Administrator',
            'ext-llm':'«system»<br>Embedding / LLM<br>Provider',
            'e1':'Đăng ký, đăng nhập','e4':'Quản lý nhân viên, yêu cầu và tri thức'}
    for cell in graph.iter('mxCell'):
        if cell.get('id') in values:cell.set('value',values[cell.get('id')])
    ET.indent(graph);graph.write(context,encoding='utf-8',xml_declaration=True)
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    svg=ET.parse(folder/'context_diagram_system.svg')
    replacements={'Guest':'Guest / Unauthenticated User','Agent':'Support Agent',
                  'Admin':'System Administrator','Embedding hoặc LLM':'Embedding / LLM'}
    for parent in svg.iter():
        for child in list(parent):
            if child.text in ['Yêu cầu đặt lại mật khẩu','Xem thống kê']:
                parent.remove(child)
            elif child.text in replacements:child.text=replacements[child.text]
    svg.getroot().set('content',ET.tostring(graph.getroot(),encoding='unicode'))
    svg.write(folder/'context_diagram_system.svg',encoding='utf-8',xml_declaration=True)
    nodes=[];edges=[]
    for cell in graph.iter('mxCell'):
        if cell.get('vertex')=='1':
            label=re.sub('<[^>]+>',' ',html.unescape(cell.get('value',''))).strip()
            nodes.append({'id':cell.get('id'),'kind':'actor' if 'shape=umlActor' in cell.get('style','') else 'box','lines':[label]})
        elif cell.get('edge')=='1':
            edges.append({'source':cell.get('source'),'target':cell.get('target'),'generalization':False})
    records.insert(0,{'name':'context_diagram_system','title':'Clarune — Sơ đồ bối cảnh P0',
                     'provenance':provenance,'corrections':['Remove P1 labels UC-16/UC-17 to match the P0 caption',
                     'Normalize actor names; preserve original layout and relationships'], 'nodes':nodes,'edges':edges})
    return records
