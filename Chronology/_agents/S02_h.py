# helper: reads JSONL on stdin w/ defaults, appends to S02_events.jsonl via same validation
import sys,json,re,os
D={'source_file':'NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf','source_id':14,'date_precision':'day','confidence':'high','status':'fact','how':'document','why':'not stated in source'}
kind=sys.argv[1]
out=os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_agents/S02_{kind}.jsonl')
REQ={'events':['date','date_precision','who','what','how','why','category','status','source_file','source_id','locator','confidence'],'people':['name','role','organisation','side','key_acts','sources']}
ok=bad=0
with open(out,'a',encoding='utf-8') as f:
    for ln,l in enumerate(sys.stdin,1):
        l=l.strip()
        if not l: continue
        try: o=json.loads(l)
        except Exception as e: print('BAD JSON',ln,e,l[:80]); bad+=1; continue
        if kind=='events':
            for k,v in D.items(): o.setdefault(k,v)
            if 'people' not in o: o['people']=[]
        else:
            o.setdefault('sources',[14])
        miss=[k for k in REQ[kind] if k not in o]
        if miss: print('MISSING',miss,ln,l[:80]); bad+=1; continue
        if kind=='events' and not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',str(o['date'])): print('BAD DATE',o['date'],ln); bad+=1; continue
        o['_slice']='S02'; f.write(json.dumps(o,ensure_ascii=False)+'\n'); ok+=1
print(f'appended {ok}, rejected {bad}')
