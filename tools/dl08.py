import json,urllib.request,concurrent.futures as cf,os
from PIL import Image
d=json.load(open('rb.json'))
fs=[t['path'] for t in d['tree'] if t['path'].startswith('Assets/Avatars/Adults/Male_Adult_08/') and t.get('size') and ((t['path'].endswith('.tga') and 'specular' not in t['path']) or t['path'].endswith('Export/Male_Adult_08.fbx'))]
def g(p):
    n=p.split('/')[-1]
    urllib.request.urlretrieve('https://raw.githubusercontent.com/microsoft/Microsoft-Rocketbox/master/'+p,'src/'+n)
    if n.endswith('.tga'):
        im=Image.open('src/'+n).resize((1024,1024),Image.LANCZOS); b=n[:-4]
        if 'opacity' in b: im.convert('RGBA').save(f'tex/{b}.png',optimize=True)
        else: im.convert('RGB').save(f'tex/{b}.jpg',quality=88)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(g,fs))
print('done',fs)
