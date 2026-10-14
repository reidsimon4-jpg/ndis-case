# usage: python3 s09w.py SID  (compact JSONL on stdin) -> expands and appends via S09 events
import sys,json,os,re
sid=int(sys.argv[1])
sl={}
for l in open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/slice_S09.tsv'),encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); sl[int(p[0])]=p[4]
if sid==0: sf=None
else: sf=sl[sid]
out=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S09_events.jsonl')
ok=bad=0
with open(out,'a',encoding='utf-8') as f:
    for ln,l in enumerate(sys.stdin,1):
        l=l.strip()
        if not l: continue
        try: o=json.loads(l)
        except Exception as e: print('BAD JSON',ln,e,l[:90]); bad+=1; continue
        d=o.get('d') or o.get('date')
        if not d or not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',d): print('BAD DATE',ln,d); bad+=1; continue
        prec={4:'year',7:'month',10:'day'}[len(d)]
        if o.get('prec'): prec=o['prec']
        r={'date':d,'date_precision':prec,'who':o.get('who','?'),'what':o.get('what','?'),'how':o.get('how','email'),
           'why':o.get('why','not stated in source'),'category':o.get('cat','correspondence'),'status':o.get('st','fact'),
           'source_file':o.get('sf') or sf,'source_id':o.get('sid',sid),'locator':o.get('loc','?'),'confidence':o.get('conf','medium'),
           'people':o.get('ppl',[]),'_slice':'S09'}
        for k,kk in (('to','to_whom'),('det','detail'),('q','quote'),('notes','notes'),('time','time'),('de','date_end'),('ag','agencies')):
            if k in o: r[kk]=o[k]
        if 'de' in o: r['date_precision']='range'
        f.write(json.dumps(r,ensure_ascii=False)+'\n'); ok+=1
print(f'ok {ok} bad {bad}')
