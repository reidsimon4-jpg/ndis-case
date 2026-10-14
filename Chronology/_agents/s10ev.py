import sys,json,re,os
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
paths={}
for l in open(base+'_build/slice_S10.tsv'):
    p=l.rstrip('\n').split('\t'); paths[int(p[0])]=p[4]
kind=sys.argv[1]
out=base+f'_agents/S10_{kind}.jsonl'
D={'events':{'date_precision':'day','how':'not stated','why':'not stated in source','category':'work_product','status':'unverified','confidence':'medium','people':[]}}
ok=bad=0
with open(out,'a',encoding='utf-8') as f:
  for ln,l in enumerate(sys.stdin,1):
    l=l.strip()
    if not l: continue
    try:o=json.loads(l)
    except Exception as e: print('BADJSON',ln,e,l[:80]);bad+=1;continue
    if kind=='events':
        sid=o.get('source_id')
        if sid is None: print('nosid',ln);bad+=1;continue
        o['source_file']=paths.get(int(sid),'?')
        for k,v in D['events'].items(): o.setdefault(k,v)
        if not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',str(o.get('date'))): print('BADDATE',ln,o.get('date'));bad+=1;continue
        for k in ['who','what','locator']:
            if k not in o: print('MISSING',k,ln);bad+=1;break
        else:
            o['_slice']='S10';f.write(json.dumps(o,ensure_ascii=False)+'\n');ok+=1
    else:
        for k in ['name','role','organisation','side','key_acts','sources']:
            if k not in o: print('MISSING',k,ln);bad+=1;break
        else:
            o['_slice']='S10';f.write(json.dumps(o,ensure_ascii=False)+'\n');ok+=1
print('ok',ok,'bad',bad)
