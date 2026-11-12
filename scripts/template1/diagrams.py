"""Vector UML diagrams derived from the existing drawio graphs and final UC tables."""
from pathlib import Path
import html
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
    'actor-mail': ['«system»', 'Mail Service (P1)'],
    'actor-llm': ['«system»', 'Embedding / LLM Provider'],
    'actor-embed': ['«system»', 'Embedding Provider'],
}
BASELINES = ['uc_overall_19_usecases', 'uc_module_d_identity', 'uc_module_c_ticketing',
             'uc_module_b_kb', 'uc_module_a_ai_analytics']
TITLES = ['Clarune — Tổng thể 19 Use Case', 'Clarune — Định danh và phân quyền',
          'Clarune — Quản lý ticket', 'Clarune — Cơ sở tri thức',
          'Clarune — Trợ lý AI và thống kê']
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
            out.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in e['points'])+'" fill="none" stroke="#111" stroke-width="1.45" stroke-linejoin="round"'+marker+'/>')
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
            elif n['kind']=='uc':
                out.append(f'<ellipse cx="{cx}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="white" stroke="#111" stroke-width="1.7"/>')
                ty=y+h/2-(len(n['lines'])-1)*11+5
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#111" stroke-width="1.7"/>')
                ty=y+h/2-(len(n['lines'])-1)*11+5
            for i,line in enumerate(n['lines']):
                weight=' font-weight="bold"' if n['kind']=='uc' and i==0 else ''
                out.append(f'<text x="{cx}" y="{ty+i*22}" text-anchor="middle"{weight}>{esc(line)}</text>')
        out += ['</g></svg>'];(folder/(name+'.svg')).write_text('\n'.join(out)+'\n')
        mx=ET.Element('mxfile',host='app.diagrams.net',type='device',version='24.0.0')
        di=ET.SubElement(mx,'diagram',id=name,name=self.title)
        model=ET.SubElement(di,'mxGraphModel',grid='1',gridSize='10',page='1',pageScale='1',pageWidth=str(self.width),pageHeight=str(self.height))
        root=ET.SubElement(model,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
        for n in self.nodes:
            styles={'boundary':'shape=rect;verticalAlign=top;spacingTop=12;fontStyle=1;', 'actor':'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;', 'uc':'ellipse;', 'box':'shape=rect;'}
            c=ET.SubElement(root,'mxCell',id=n['id'],value='<br>'.join(esc(a) for a in n['lines']),style=styles[n['kind']]+'html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor=#111111;fontColor=#111111;strokeWidth=1.7;fontSize=16;fontFamily=Arial;',vertex='1',parent='1')
            ET.SubElement(c,'mxGeometry',x=str(n['x']),y=str(n['y']),width=str(n['w']),height=str(n['h']),**{'as':'geometry'})
        for i,e in enumerate(self.edges):
            style='edgeStyle=none;html=1;strokeColor=#111111;strokeWidth=1.45;'
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
        order=ORDERS[index];overall=index==0
        # One semantic relation per actor/UC; user roles inherit only session/profile.
        actors=[a for a in ACTORS if any(a in (x,y) for x,y,g in edges)]
        left=[a for a in actors if a not in ['actor-admin','actor-mail','actor-llm','actor-embed']]
        right=[a for a in actors if a not in left]
        width=1560 if overall else 1320; center=width/2;ux=center-240;uw=480
        height=max(700,200+len(order)*112)
        d=Diagram(TITLES[index],width,height)
        d.node('system','boundary',center-280,25,560,height-50,[TITLES[index]])
        positions={}
        for row,n in enumerate(order):
            y=90+row*112
            d.node(f'uc-{n:02}','uc',ux,y,uw,86,[f'UC-{n:02}'+(' (P1)' if n in [16,17,19] and '(P1)' not in names[n] else '')]+textwrap.wrap(names[n],width=42,break_long_words=False))
            positions[f'uc-{n:02}']=(ux,y,uw,86)
        for side,aa in [('left',left),('right',right)]:
            for j,a in enumerate(aa):
                x=55 if side=='left' else width-285
                y=95+j*(height-300)/max(1,len(aa)-1) if len(aa)>1 else height/2-80
                # Put association origins in gaps between UC rows, avoiding false junctions.
                y=153+112*round((y+36-189)/112)
                y=max(65,min(y,height-140))
                d.node(a,'actor',x,y,230,82,ACTORS[a]);positions[a]=(x,y,230,82)
        # Parallel orthogonal association routes, no direction arrow for UML associations.
        for a,b,general in edges:
            ax,ay,aw,ah=positions[a];bx,by,bw,bh=positions[b]
            if general:
                side='left' if a in left else 'right'
                outer=25 if side=='left' else width-25
                cx=bx+bw/2
                if side=='right':
                    p=[(ax+aw/2,ay+82),(outer,ay+82),(outer,height-12),(25,height-12),(25,by-22),(cx,by-22),(cx,by+2)]
                else:
                    p=[(ax+aw/2-24,ay+36),(outer,ay+36),(outer,by-22),(cx,by-22),(cx,by+2)]
            else:
                actor=a if a.startswith('actor-') else b;uc=b if actor==a else a
                x,y,w,h=positions[actor];xx,yy,ww,hh=positions[uc]
                aa=left if actor in left else right;k=aa.index(actor)
                rail=(ux-40-k*32) if actor in left else (ux+uw+40+k*32)
                p=[(x+w/2+(24 if actor in left else -24),y+36),(rail,y+36),(rail,yy+hh/2),(xx if actor in left else xx+ww,yy+hh/2)]
                if actor!=a:p=p[::-1]
            d.edge(a,b,p,generalization=general)
        records.append(d.write(folder,baseline))
    # The context drawing retains external actors only; infrastructure stays internal.
    d=Diagram('Clarune — Sơ đồ bối cảnh',1500,850)
    d.node('clarune','box',620,320,250,150,['Clarune'])
    for i,a in enumerate(['actor-guest','actor-customer','actor-agent','actor-admin']):
        y=35+i*190;d.node(a,'actor',40,y,240,82,ACTORS[a])
        labels=['Đăng ký, đăng nhập,','đặt lại mật khẩu (P1)'] if i==0 else (['Tạo/xem ticket, trao đổi,','xác nhận đóng hoặc mở lại'] if i==1 else (['Nhận và xử lý ticket,','tra cứu tri thức, duyệt gợi ý AI'] if i==2 else ['Quản lý Agent, phân công,','quản trị tri thức, thống kê']))
        # Label near the actor, connectors enter distinct points on the central boundary.
        d.edge(a,'clarune',[(184,y+36),(440,y+36),(620,350+i*28)],arrow=True,label='\n'.join(labels))
    for a,y,label in [('actor-llm',195,'Embedding và gợi ý AI'),('actor-mail',565,'Gửi liên kết đặt lại mật khẩu (P1)')]:
        d.node(a,'actor',1230,y,240,82,ACTORS[a]);d.edge('clarune',a,[(870,360 if y<300 else 430),(1030,y+36),(1326,y+36)],arrow=True,label=label)
    records.insert(0,d.write(folder,'context_diagram_system'))
    return records
