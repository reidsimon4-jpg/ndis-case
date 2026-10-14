import os,re,json,collections
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit() and 'CLIENTS/' in p[4]:
        rows.append((int(p[0]),p[4]))
print(len(rows))
KW=re.compile(r'complaint|NDIA|investigat|police|plan manager|cease|terminat|exit|invoice|freeze|Commission',re.I)
KW2=re.compile(r'complaint|investigat|police|cease|terminat|freeze|Commission|exit|fraud|dispute|cancel|discharg',re.I)
rec=collections.OrderedDict()
dre=re.compile(r'^(\d{2}/\d{2}/\d{4})\s{1,}(\S.*?)\s{2,}(\d.*)$')
for i,rel in rows:
    m=re.search(r'CLIENTS/(.)/([^/]+)/(.+)$',rel)
    if not m: print('nomatch',rel);continue
    cl=m.group(2); fn=m.group(3)
    t=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read()
    r=rec.setdefault(cl,dict(client=cl,files=[],dates=[],authors=collections.Counter(),kw=collections.Counter(),kwhits=[],hdr=[]))
    r['files'].append((i,fn,len(t)))
    h=re.search(r'(\d{1,2} \w+ \d{4}) - (\d{1,2} \w+ \d{4})',t[:1500])
    if h: r['hdr'].append(h.group(0))
    tot=re.search(r'Total Amount\s+\$([\d,\.]+)',t[:2000])
    lines=t.split('\n')
    for ln,line in enumerate(lines):
        mm=dre.match(line)
        if mm:
            d=mm.group(1); r['dates'].append((d[6:]+d[3:5]+d[:2],d))
            au=mm.group(2).strip()
            r['authors'][au]+=1
        for k in set(x.lower() for x in KW.findall(line)): r['kw'][k]+=1
        if KW2.search(line):
            r['kwhits'].append((i,ln,line.strip()[:200]))
out=[]
for cl,r in rec.items():
    ds=sorted(r['dates'])
    out.append(dict(client=cl,nfiles=len(r['files']),ids=[f[0] for f in r['files']],first=ds[0][1] if ds else None,last=ds[-1][1] if ds else None,nentries=len(ds),authors=r['authors'].most_common(),kw=dict(r['kw']),hdr=r['hdr'],nhits=len(r['kwhits']),hits=r['kwhits'][:40]))
json.dump(out,open('s04_clients.json','w'),indent=0)
print(len(out))
