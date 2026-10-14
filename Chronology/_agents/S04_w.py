# usage: python3 S04_w.py events|people <<EOF ; first line "#D {json defaults}" (may be repeated to change defaults)
import sys,json,subprocess,os
kind=sys.argv[1]; D={}; out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    if l.startswith('#D '): D.update(json.loads(l[3:])); continue
    try: o=json.loads(l)
    except Exception as e: print('BAD JSON',e,l[:100]); continue
    r=dict(D); r.update(o)
    if kind=='events':
        r.setdefault('date_precision','day'); r.setdefault('confidence','high'); r.setdefault('status','allegation'); r.setdefault('why','not stated in source')
    out.append(json.dumps(r,ensure_ascii=False))
p=subprocess.run(['python3',os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/add.py'),'S04',kind],input='\n'.join(out),text=True,capture_output=True)
print(p.stdout,p.stderr)
