import json,re,urllib.request,concurrent.futures as cf,os
d=json.load(open('rb.json'))
paths={t['path'].split('/')[-1].replace('.max.fbx',''):t['path'] for t in d['tree'] if t['path'].startswith('Assets/Animations') and t['path'].endswith('.fbx')}
want=[]
pat=re.compile(r'^(dancing_|cheer_|claphands_|wave_|gestic_laugh_|gestic_shrug_01|gestic_thoughtful|gestic_talk_(neutral_0[1-5]|excited_0[12]|cool|relaxed_0[12]|self.assured_01|angry_01|femalestressed_01)|gestic_listen_(accept_01|deny_01|excited_01)|gestic_presentation_(left|right)_01|idle_(look_around_01|stretch_arms_01|yawn_01|scratch_head_01|touch_hair_01|shake_arms_01|cough_01|neutral_0[1-3]|breathe_0[12])|crouch_idle|cell_phone_talk_01)')
for n in paths:
    m=re.match(r'^([fm])_(.*)$',n)
    if m and pat.match(m.group(2)): want.append(n)
print(len(want))
def g(n):
    o=f'anim2/{n}.fbx'
    if os.path.exists(o) and os.path.getsize(o)>1000: return n
    for _ in range(3):
        try: urllib.request.urlretrieve('https://raw.githubusercontent.com/microsoft/Microsoft-Rocketbox/master/'+paths[n].replace(' ','%20'),o); return n
        except Exception as e: err=e
    print('FAIL',n,err)
with cf.ThreadPoolExecutor(10) as ex: list(ex.map(g,want))
print('done',len(os.listdir('anim2')))
