# Gera fluxo.svg: diagrama animado do fluxo de dados (marketplaces -> Hermes Hub -> ERP / Hefesto / Temis).
W,H=800,300; G1="#39ff14"; G2="#21c421"; LINE="#1e5c25"
def node(x,y,w,h,title,sub=None,fs=14):
    t=f'<text x="{x+w/2}" y="{y+h/2+(5 if not sub else -1)}" text-anchor="middle" fill="{G1}" font-size="{fs}" font-weight="bold">{title}</text>'
    if sub: t+=f'<text x="{x+w/2}" y="{y+h/2+15}" text-anchor="middle" fill="{G2}" font-size="11">{sub}</text>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#0c0c0c" stroke="{G2}"/>{t}'
def edge(path,dur,begin,both=False):
    e=f'<path d="{path}" fill="none" stroke="{LINE}" stroke-width="1.5"/>'
    e+=f'<circle r="3" fill="{G1}"><animateMotion path="{path}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>'
    if both: e+=f'<circle r="3" fill="{G1}"><animateMotion path="{path}" dur="{dur}s" begin="{begin+dur/2}s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1" calcMode="linear"/></circle>'
    return e
mk=["Shopify","Mercado Livre","Shopee","Amazon","Magalu","TikTok Shop"]
b=[]
hub=(330,120,150,64); b.append(node(*hub,"Hermes Hub","pedidos · estoque · anúncios"))
for i,m in enumerate(mk):
    y=44+i*40; b.append(node(30,y,140,28,m,fs=13))
    b.append(edge(f"M170 {y+14} C 250 {y+14}, 250 152, 330 152",2.6,i*0.45))
right=[("ERP (TOTVS)","faturamento · fiscal",48,True),("Hefesto","expedição e produção",124,False),("Temis.etiquetas","etiquetas de envio",200,False)]
for i,(t,sub,y,both) in enumerate(right):
    b.append(node(620,y,160,52,t,sub)); yc=y+26
    if t.startswith("Temis"): b.append(edge("M700 176 L700 200",1.6,0.8))
    else: b.append(edge(f"M480 {152 if i else 140} C 550 {152 if i else 140}, 550 {yc}, 620 {yc}",2.2,0.3+i*0.7,both))
b.append(f'<text x="100" y="30" text-anchor="middle" fill="{G2}" font-size="11">marketplaces e loja</text>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Consolas, 'Cascadia Mono', 'Lucida Console', ui-monospace, monospace">
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="#0c0c0c" stroke="#3a3a3a"/>
<path d="M0.5 8 a8 8 0 0 1 8 -7.5 H{W-8.5} a8 8 0 0 1 8 7.5 V32 H0.5 Z" fill="#202020"/>
<rect x="12" y="9" width="16" height="14" rx="2" fill="#0c0c0c" stroke="#8a8a8a"/><text x="15" y="20" fill="{G1}" font-size="10" font-weight="bold">&gt;_</text>
<text x="38" y="21" fill="#d0d0d0" font-size="13">Explorer_Of / fluxo de dados</text>
<text x="{W-100}" y="21" fill="#d0d0d0" font-size="14" xml:space="preserve">─    ☐    ✕</text>
<g transform="translate(0,14)">{"".join(b)}</g>
</svg>'''
open('fluxo.svg','w',encoding='utf-8').write(svg)
import xml.dom.minidom as m; m.parse('fluxo.svg'); print("fluxo ok")
