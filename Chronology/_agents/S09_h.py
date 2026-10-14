# usage: python3 S09_h.py SRCID [conf]  ; stdin lines: date | who | what | to | how | cat | st | people;; | locator | why | detail
import sys,json,re,os,subprocess
sid=int(sys.argv[1]); conf=sys.argv[2] if len(sys.argv)>2 else 'medium'
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/slice_S09.tsv')
path=None
for l in open(base,encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if int(p[0])==sid: path=p[4]
if sid==0: path=sys.argv[3]
ST={'f':'fact','a':'allegation','c':'contention','s':'simon_position','u':'unverified','p':'planned'}
CT={'corr':'correspondence','trib':'tribunal','reg':'regulatory_decision','inv':'investigation','crim':'criminal','foi':'foi','leg':'legal_representation','work':'work_product','dead':'deadline','ev':'evidence','fc':'federal_court','corp':'corporate','ops':'operations','ato':'ato_tax','ir':'internal_review','comp':'complaint','bord':'border_customs','oth':'other'}
out=[]
for ln,l in enumerate(sys.stdin,1):
    l=l.strip()
    if not l or l.startswith('#'): continue
    f=[x.strip() for x in l.split(' | ')]
    while len(f)<11: f.append('')
    d,who,what,to,how,cat,st,ppl,loc,why,det=f[:11]
    prec='day'; tm=None; dend=None
    if d.startswith('~'): prec='approx'; d=d[1:]
    if '@' in d: d,tm=d.split('@')
    if '..' in d: d,dend=d.split('..'); prec='range'
    if re.match(r'^\d{4}$',d): prec='year' if prec=='day' else prec
    elif re.match(r'^\d{4}-\d{2}$',d): prec='month' if prec=='day' else prec
    if not re.match(r'^\d{4}(-\d{2}(-\d{2})?)?$',d): print('BADDATE',ln,d); continue
    o=dict(date=d,date_precision=prec,who=who,what=what,how=how or 'not stated',why=why or 'not stated in source',category=CT.get(cat,cat or 'correspondence'),status=ST.get(st,st or 'fact'),people=[x.strip() for x in ppl.split(';') if x.strip()],source_file=path,source_id=sid,locator=loc,confidence=conf)
    if tm: o['time']=tm
    if dend: o['date_end']=dend
    if to: o['to_whom']=to
    if det: o['detail']=det
    out.append(o)
op=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S09_events.jsonl')
with open(op,'a',encoding='utf-8') as fh:
    for o in out: o['_slice']='S09'; fh.write(json.dumps(o,ensure_ascii=False)+'\n')
print('appended',len(out))
