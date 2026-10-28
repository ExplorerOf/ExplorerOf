import re
from xml.sax.saxutils import escape as e
CW=7.7; X=16; Y0=62; LH=21; W=800
PROMPT=r"C:\Users\Explorer_Of>"
G1="#39ff14"; G2="#21c421"  # verde claro (comandos) / verde (saída)
lines=[
 ("out","Microsoft Windows [versão 10.0.26200]",0.1),
 ("out","",0.1),
 ("cmd","whoami",0.5,0.5),
 ("out","Gustavo Kogien Caraski · dev @ Olimpo Esportes · estudante de ADS",1.2),
 ("out","",1.2),
 ("cmd","type stack.json",1.7,0.9),
 ("out","{",2.8),
 ("out",'  "linguagens": ["TypeScript", "Python"],',2.9),
 ("out",'  "web":        ["Next.js", "Node.js"],',3.0),
 ("out",'  "dados":      ["PostgreSQL", "Docker", "GitHub Actions"],',3.1),
 ("out",'  "ecommerce":  ["Shopify", "Mercado Livre", "Shopee", "Amazon", "Magalu", "TikTok Shop"]',3.2),
 ("out","}",3.3),
 ("out","",3.3),
 ("cmd","dir /b projetos",3.9,0.8),
 ("out","hermes-hub",4.9),("out","hefesto",5.0),("out","temis-etiquetas",5.1),
 ("out","",5.1),
 ("cmd","",5.6,0.01),
]
H=Y0+LH*len(lines)+4
body=[]; defs=[]
for i,l in enumerate(lines):
    y=Y0+LH*i; kind,txt=l[0],l[1]
    if kind=="cmd":
        t0,d=l[2],l[3]; pw=X+CW*len(PROMPT); w=pw+CW*len(txt)+8
        defs.append(f'<clipPath id="c{i}"><rect x="0" y="{y-16}" width="{pw:.0f}" height="{LH}"><animate attributeName="width" from="{pw:.0f}" to="{w:.0f}" begin="{t0}s" dur="{d}s" fill="freeze"/></rect></clipPath>')
        cur='' if txt else f'<tspan opacity="0">_<animate attributeName="opacity" values="1;1;0;0" dur="1s" begin="{t0}s" repeatCount="indefinite"/></tspan>'
        body.append(f'<text x="{X}" y="{y}" fill="{G1}" clip-path="url(#c{i})">{e(PROMPT)}{e(txt)}{cur}</text>')
    elif txt:
        body.append(f'<text x="{X}" y="{y}" fill="{G2}" opacity="0" xml:space="preserve">{e(txt)}<animate attributeName="opacity" to="1" begin="{l[2]}s" dur="0.05s" fill="freeze"/></text>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Consolas, 'Cascadia Mono', 'Lucida Console', ui-monospace, monospace" font-size="14">
<defs>{"".join(defs)}</defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="#0c0c0c" stroke="#3a3a3a"/>
<path d="M0.5 8 a8 8 0 0 1 8 -7.5 H{W-8.5} a8 8 0 0 1 8 7.5 V32 H0.5 Z" fill="#202020"/>
<rect x="12" y="9" width="16" height="14" rx="2" fill="#0c0c0c" stroke="#8a8a8a"/><text x="15" y="20" fill="{G1}" font-size="10" font-weight="bold">&gt;_</text>
<text x="38" y="21" fill="#d0d0d0" font-size="13">Explorer_Of / Gustavo Kogien Caraski</text>
<text x="{W-100}" y="21" fill="#d0d0d0" font-size="14" xml:space="preserve">─    ☐    ✕</text>
{chr(10).join(body)}
</svg>'''
open('terminal.svg','w',encoding='utf-8').write(svg)
import xml.dom.minidom as m; m.parse('terminal.svg'); print("ok",H)
