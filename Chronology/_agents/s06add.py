import sys,json,subprocess,os
kind=sys.argv[1]
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/')
m={}
for l in open(base+'slice_S06.tsv'):
    r=l.rstrip('\n').split('\t'); m[int(r[0])]=r[4]
out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    try: o=json.loads(l)
    except Exception as e: print('BADJSON',l[:80]); continue
    if kind=='events':
        o.setdefault('source_file',m.get(o.get('source_id'),'?'))
        o.setdefault('people',[])
    out.append(json.dumps(o,ensure_ascii=False))
p=subprocess.run(['python3',base+'add.py','S06',kind],input='\n'.join(out)+'\n',text=True,capture_output=True)
print(p.stdout,p.stderr)
