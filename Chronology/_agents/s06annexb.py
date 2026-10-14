import re,os,collections,datetime
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[l.rstrip('\n').split('\t') for l in open(base+'_build/slice_S06.tsv')]
for r in rows:
    if 'Annex_B_' not in r[4] or 'Summary' in r[4]: continue
    i=int(r[0]); t=open(base+f'_corpus/{i:05d}.txt',encoding='utf-8',errors='ignore').read()
    ds=[]
    pm=collections.Counter()
    for m in re.finditer(r'(?m)^\s*(\d{6,9})\s+(Payment Request[^\n]*?|Cancel Request[^\n]*?)\s{2,}(\d{2}/\d{2}/\d{4})\s+(\d+:\d+:\d+ [AP]M)\s+(\d+)\s+(.+?)\s{2,}',t):
        d=datetime.datetime.strptime(m.group(3),'%d/%m/%Y').date(); ds.append(d); pm[m.group(6).strip()]+=1
    tot=re.findall(r'Total alleged fraud amount[^\$\n]*?\s+(\$[\d,\.]+)',t)
    nm=re.search(r'participant\s+([A-Z][^\n]*?)\s{2,}',t)
    name=r[4].split('Annex_B_')[1].replace('.pdf','')
    print(i,name,len(ds),min(ds) if ds else None,max(ds) if ds else None,dict(pm.most_common(6)),tot)
