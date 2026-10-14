
# usage: python3 S09_w.py SRCID  (stdin: compact JSON per line; keys d,t,w,x,to,h,y,dt,q,c,s,ag,p,l,cf,n,pr,de)
import sys,json,os,re
sid=int(sys.argv[1])
tsv=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/slice_S09.tsv')
paths={}
for l in open(tsv,encoding='utf-8'):
    a=l.rstrip('\n').split('\t')
    if len(a)>=5: paths[int(a[0])]=a[4]
sf=paths.get(sid,'project:unknown') if sid else sys.argv[2]
out=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S09_events.jsonl')
ok=bad=0
with open(out,'a',encoding='utf-8') as f:
  for ln,l in enumerate(sys.stdin,1):
    l=l.strip()
    if not l: continue
    try: o=json.loads(l)
    except Exception as e: print('BADJSON',ln,e,l[:90]); bad+=1; continue
    d=o['d']
    if not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',d): print('BADDATE',ln,d); bad+=1; continue
    prec=o.get('pr') or ('day' if len(d)==10 else 'month' if len(d)==7 else 'year')
    r={'date':d,'date_precision':prec,'who':o.get('w','not stated'),'what':o['x'],'how':o.get('h','email'),'why':o.get('y','not stated in source'),
       'category':o.get('c','correspondence'),'status':o.get('s','fact'),'source_file':sf,'source_id':sid,'locator':o.get('l',''),'confidence':o.get('cf','medium'),
       'people':o.get('p',[])}
    for k,kk in (('de','date_end'),('t','time'),('to','to_whom'),('dt','detail'),('q','quote'),('ag','agencies'),('n','notes')):
        if k in o: r[kk]=o[k]
    r['_slice']='S09'
    f.write(json.dumps(r,ensure_ascii=False)+'\n'); ok+=1
print('appended',ok,'bad',bad)
