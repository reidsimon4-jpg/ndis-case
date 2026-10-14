import os,re,json,collections
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit() and 'CLIENTS/' in p[4]: rows.append((int(p[0]),p[4]))
dl=re.compile(r'^(\d{2}/\d{2}/\d{4})\s+(.*)$')
dur=re.compile(r'\s{2,}(\d+\s*(?:hrs?|hours?)(?:\s+\d+\s*minutes?)?|\d+\s*minutes?|\d+(?:\.\d+)?\s*KMs?)\s')
tot=0;lines=0;nomatch=[]
out={}
for i,rel in rows:
    t=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read()
    cl=rel.split('CLIENTS/')[1].split('/')[1]
    ent=[]
    for ln in t.split('\n'):
        m=dl.match(ln)
        if not m: continue
        lines+=1
        rest=m.group(2)
        md=dur.search('  '+rest+' ')
        if md:
            au=rest[:md.start()-0].strip() if md.start()>0 else ''
            au=re.sub(r'\s{2,}.*','',rest.strip())
            ent.append((m.group(1),au))
        else: nomatch.append((i,ln[:100]))
    out[i]=dict(client=cl,ent=ent,hdr=re.search(r'Case Note Report\s+(\d{1,2} \w+ \d{4}) - (\d{1,2} \w+ \d{4})',t[:3000]),tot=re.search(r'Total Hours\s+([^\n]+)',t[:3000]))
    tot+=len(ent)
print('files',len(rows),'date lines',lines,'entries parsed',tot,'nomatch',len(nomatch))
print(nomatch[:15])
