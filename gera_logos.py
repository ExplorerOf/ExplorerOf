# Gera logos/<plataforma>.svg: tile branco com o logo oficial embutido.
# Fontes: Wikimedia Commons (domínio público) e Simple Icons (CC0), baixadas para a pasta SRC.
import re,os,sys
SRC=sys.argv[1] if len(sys.argv)>1 else os.environ['TEMP']+'/logos/'
H=48; PAD=12; LH=24
def tile(name,src,extra_w=0,extra=''):
    svg=open(os.path.join(SRC,src),encoding='utf-8').read()
    svg=re.sub(r'<\?xml[^>]*\?>|<!DOCTYPE[^>]*>','',svg,flags=re.S)
    m=re.search(r'<svg\b[^>]*>',svg,re.S); tag=m.group(0)
    ns=' '.join(sorted(set(re.findall(r'xmlns:[\w-]+="[^"]+"',tag))|{'xmlns:xlink="http://www.w3.org/1999/xlink"'}))
    vb=re.search(r'viewBox="([^"]+)"',tag)
    if vb: x,y,w,h=map(float,vb.group(1).replace(',',' ').split())
    else:
        w=float(re.search(r'\bwidth="([\d.]+)',tag).group(1)); h=float(re.search(r'\bheight="([\d.]+)',tag).group(1)); x=y=0
    inner=svg[m.end():svg.rindex('</svg>')]
    lw=w*LH/h; W=round(lw+2*PAD+extra_w)
    import xml.dom.minidom as mm
    for sub,bg,stroke,fg in (('', '#ffffff','#d0d7de','#000000'), ('dark/', '#161b22','#30363d','#ffffff')):
        body=inner if not sub else re.sub(r'#(2d3277|000000|000)',fg,inner)  # texto escuro vira branco no tema escuro
        out=f'''<svg xmlns="http://www.w3.org/2000/svg" {ns} width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" fill="{bg}" stroke="{stroke}"/>
<svg x="{PAD}" y="{PAD}" width="{lw:.1f}" height="{LH}" viewBox="{x} {y} {w} {h}" fill="{fg}">{body}</svg>{extra.replace('#000000',fg)}
</svg>'''
        open(f'logos/{sub}{name}.svg','w',encoding='utf-8').write(out)
        mm.parseString(out.encode('utf-8'))
    print(name,W,'ok')
os.makedirs('logos/dark',exist_ok=True)
tile('shopify','shopify.svg')
tile('mercado-livre','Mercado_Livre_wordmark_(Portuguese_version).svg')
tile('shopee','shopee2.svg')
tile('amazon','Amazon_logo.svg')
tile('magalu','Magalu_(2019).svg')
tile('tiktok-shop','tiktok_icon.svg',extra_w=100,extra=f'<text x="{PAD+LH+8}" y="{H/2+6}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="17" font-weight="700" fill="#000000">TikTok Shop</text>')
