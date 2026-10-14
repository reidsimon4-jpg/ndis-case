# usage: python3 add.py S01 events|people  (JSON objects one per line on stdin)
import sys,json,re,os
sl,kind=sys.argv[1],sys.argv[2]
out=os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_agents/{sl}_{kind}.jsonl')
REQ={'events':['date','date_precision','who','what','how','why','category','status','source_file','source_id','locator','confidence'],
     'people':['name','role','organisation','side','key_acts','sources']}
ok=bad=0
with open(out,'a',encoding='utf-8') as f:
    for ln,l in enumerate(sys.stdin,1):
        l=l.strip()
        if not l: continue
        try: o=json.loads(l)
        except Exception as e: print('BAD JSON line',ln,e,l[:80]); bad+=1; continue
        miss=[k for k in REQ[kind] if k not in o]
        if miss: print('MISSING',miss,'line',ln,l[:80]); bad+=1; continue
        if kind=='events' and not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',str(o['date'])): print('BAD DATE',o['date'],'line',ln); bad+=1; continue
        o['_slice']=sl; f.write(json.dumps(o,ensure_ascii=False)+'\n'); ok+=1
print(f'appended {ok}, rejected {bad} -> {out}')
