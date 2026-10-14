# wrapper: short keys -> add.py S10 events
import sys,json,subprocess,os
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build')
paths={}
for l in open(base+'/slice_S10.tsv'):
    r=l.rstrip('\n').split('\t'); paths[int(r[0])]=r[4]
M={'d':'date','dp':'date_precision','de':'date_end','tm':'time','w':'who','t':'what','to':'to_whom','h':'how','y':'why','det':'detail','q':'quote','c':'category','s':'status','ag':'agencies','p':'people','i':'source_id','l':'locator','cf':'confidence','n':'notes'}
out=[]
for ln in sys.stdin:
    ln=ln.strip()
    if not ln: continue
    try: o=json.loads(ln)
    except Exception as e: print('BADJSON',e,ln[:100]); continue
    r={M.get(k,k):v for k,v in o.items()}
    r.setdefault('date_precision','day'); r.setdefault('confidence','high'); r.setdefault('how','not stated'); r.setdefault('why','not stated in source')
    r.setdefault('people',[]); r.setdefault('category','work_product')
    sid=int(r['source_id']); r['source_id']=sid; r['source_file']=paths.get(sid,'?')
    out.append(json.dumps(r,ensure_ascii=False))
p=subprocess.run(['python3','add.py','S10',sys.argv[1]],input='\n'.join(out),text=True,cwd=base,capture_output=True)
print(p.stdout,p.stderr)
