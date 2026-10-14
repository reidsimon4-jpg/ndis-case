import os,re,json,collections,datetime
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit() and 'CLIENTS/' in p[4]: rows.append((int(p[0]),p[4]))
rx=re.compile(r'^(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(\d+\s*(?:hrs?|minutes?|mins?)(?:\s+\d+\s*(?:minutes?|mins?))?|\d+(?:\.\d+)?\s*KMs?)(?=\s{2,}|\s*$)')
def dt(s):
    try: return datetime.date(int(s[6:]),int(s[3:5]),int(s[:2]))
    except: return None
cl=collections.OrderedDict()
tot=0
for i,rel in rows:
    t=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read()
    c=rel.split('CLIENTS/')[1].split('/')[1]
    r=cl.setdefault(c,dict(client=c,ids=[],ent=[],hdr=[]))
    r['ids'].append(i)
    h=re.search(r'Case Note Report\s+(\d{1,2} \w+ \d{4})\s*-\s*(\d{1,2} \w+ \d{4})',t[:3000])
    if h: r['hdr'].append((h.group(1),h.group(2)))
    for ln in t.split('\n'):
        m=rx.match(ln)
        if m:
            d=dt(m.group(1))
            au=re.sub(r'\s+',' ',m.group(2)).strip().lower()
            if d and 2019<=d.year<=2023: r['ent'].append((d,au,i)); tot+=1
print('entries',tot)
J=[]
for c,r in cl.items():
    ds=sorted(r['ent'])
    au=collections.Counter(a for _,a,_ in ds)
    J.append(dict(client=c,ids=r['ids'],n=len(ds),first=str(ds[0][0]) if ds else None,last=str(ds[-1][0]) if ds else None,authors=au.most_common(),hdr=r['hdr']))
json.dump(J,open('s04_clients2.json','w'))
# people
pe=collections.defaultdict(lambda:dict(n=0,first=None,last=None,clients=set()))
for c,r in cl.items():
    for d,a,i in r['ent']:
        p=pe[a]; p['n']+=1; p['clients'].add(c)
        if not p['first'] or d<p['first']: p['first']=d
        if not p['last'] or d>p['last']: p['last']=d
for a,p in sorted(pe.items(),key=lambda x:-x[1]['n'])[:70]: print(a,p['n'],p['first'],p['last'],len(p['clients']))
