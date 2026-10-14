# compact wrapper: python3 s04w.py events|people  (JSONL on stdin, short keys)
import sys,json,subprocess,os
kind=sys.argv[1]
SF={}
for l in open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/slice_S04.tsv'),encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit(): SF[int(p[0])]=p[4]
# ids not in slice (witness statements missing from corpus dir)
man={}
for l in open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/manifest.jsonl'),encoding='utf-8'):
    try: o=json.loads(l)
    except: continue
    if 513<=o['id']<=547: man[o['id']]=o['rel']
out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    try: o=json.loads(l)
    except Exception as e: print('BADJSON',l[:100]); continue
    if kind=='events':
        sid=o.get('id') or o.get('source_id')
        r={'date':o['d'],'date_precision':o.get('dp','day'),'who':o['who'],'what':o['what'],'how':o.get('how','not stated'),'why':o.get('why','not stated in source'),
           'category':o.get('cat','evidence'),'status':o.get('st','allegation'),'source_file':o.get('source_file') or SF.get(sid) or man.get(sid,''),'source_id':sid,'locator':o.get('loc',''),'confidence':o.get('conf','medium'),'people':o.get('ppl',[])}
        for k,kk in [('de','date_end'),('t','time'),('to','to_whom'),('detail','detail'),('quote','quote'),('ag','agencies'),('notes','notes')]:
            if k in o: r[kk]=o[k]
        out.append(r)
    else: out.append(o)
p=subprocess.run(['python3',os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/add.py'),'S04',kind],input='\n'.join(json.dumps(x,ensure_ascii=False) for x in out),text=True,capture_output=True)
print(p.stdout,p.stderr)
