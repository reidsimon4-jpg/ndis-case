import re,os,csv
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[l.rstrip('\n').split('\t') for l in open(base+'_build/slice_S06.tsv')]
out=csv.writer(open(base+'_agents/S06_pma_headers.tsv','w',encoding='utf-8'),delimiter='\t')
out.writerow(['id','pm','ext','chars','from','to','cc','date','subject','attach','ndis_in_text','path'])
for r in rows:
    if 'Service_2/PMA' not in r[4] and 'Service_3/PMAs' not in r[4]: continue
    i=int(r[0]); t=open(base+f'_corpus/{i:05d}.txt',encoding='utf-8',errors='ignore').read()
    body=t.split('\n',3)[3] if t.startswith('###') else t
    m=re.search(r'(?:Service_2/PMA|Service_3/PMAs)/([^/]+)',r[4]); pm=m.group(1) if m else '?'
    ext=r[4].rsplit('.',1)[-1].lower()
    h={}
    for k in ('From','To','Cc','Date','Subject','Attachments'):
        mm=re.search(r'(?m)^'+k+r':\s*(.*)$',body[:3000])
        h[k]=mm.group(1).strip() if mm else ''
    nd=len(re.findall(r'ndis\.gov\.au|ndia',t,re.I))
    out.writerow([i,pm,ext,r[1],h['From'],h['To'],h['Cc'],h['Date'],h['Subject'],h['Attachments'],nd,r[4].split('/')[-1]])
