"""tpl6.html + yuklab olingan fayllar -> web/ (Vercel'ga tayyor statik sayt)."""
import json, shutil
from pathlib import Path

root = Path(__file__).parent
web = root / 'web'
a = web / 'assets'
(a / 'anim').mkdir(parents=True, exist_ok=True)

chars = {'girl': ('Female_Adult_01', 'f001'), 'boy': ('Male_Adult_08', 'm014')}
assets = {}
for key, (fbx, pre) in chars.items():
    (a / key).mkdir(exist_ok=True)
    shutil.copy(root / 'src' / f'{fbx}.fbx', a / f'{key}.fbx')
    tex = {}
    for part in ('body_color', 'body_normal', 'head_color', 'head_normal'):
        shutil.copy(root / 'tex' / f'{pre}_{part}.jpg', a / key / f'{part}.jpg')
        tex[part] = f'assets/{key}/{part}.jpg'
    shutil.copy(root / 'tex' / f'{pre}_opacity_color.png', a / key / 'opacity_color.png')
    tex['opacity_color'] = f'assets/{key}/opacity_color.png'
    assets[key] = {'fbx': f'assets/{key}.fbx', 'tex': tex}

anims = json.loads((root / 'anims.json').read_text(encoding='utf8'))
for k, v in anims.items():
    (a / 'anim' / f'{k}.json').write_text(json.dumps(v, separators=(',', ':')), encoding='utf8')
(a / 'anim' / 'index.json').write_text(json.dumps(sorted(anims)), encoding='utf8')

html = (root / 'tpl6.html').read_text(encoding='utf8').replace('__ASSETS__', json.dumps(assets))
(web / 'index.html').write_text(html, encoding='utf8')
(web / 'vercel.json').write_text(json.dumps({
    'cleanUrls': True,
    'headers': [
        {'source': '/(.*)', 'headers': [
            {'key': 'Permissions-Policy', 'value': 'display-capture=(self), microphone=(self)'}]},
        {'source': '/assets/(.*)', 'headers': [
            {'key': 'Cache-Control', 'value': 'public, max-age=86400'}]},
    ]}, indent=2), encoding='utf8')
print('web/ tayyor:', len(html) // 1024, 'KB index.html,', len(anims), 'ta animatsiya')
