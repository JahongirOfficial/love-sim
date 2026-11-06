import json,re,urllib.request,os
d=json.load(open('rb.json'))
paths={t['path'].split('/')[-1].replace('.max.fbx',''):t['path'] for t in d['tree'] if t['path'].startswith('Assets/Animations') and t['path'].endswith('.fbx')}
for n in ['f_sit_chair_idle_neutral_01','f_sit_chair_idle_relaxed_01','m_sit_chair_idle_neutral_01','m_sit_chair_idle_relaxed_01']:
    o=f'anim2/{n}.fbx'
    if not os.path.exists(o): urllib.request.urlretrieve('https://raw.githubusercontent.com/microsoft/Microsoft-Rocketbox/master/'+paths[n],o)
    print(n,os.path.getsize(o))
