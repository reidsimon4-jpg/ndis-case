# build entry-level index: for each client file, list entries (start,end,date,author,text)
import os,re,json,collections,datetime,pickle
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit() and 'CLIENTS/' in p[4]: rows.append((int(p[0]),p[4]))
rx=re.compile(r'(?m)^(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(\d+\s*(?:hrs?|minutes?|mins?)(?:\s+\d+\s*(?:minutes?|mins?))?|\d+(?:\.\d+)?\s*KMs?)(?=\s{2,}|\s*$)')
E=[]
for i,rel in rows:
    t=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read()
    c=rel.split('CLIENTS/')[1].split('/')[1]
    ms=list(rx.finditer(t))
    for k,m in enumerate(ms):
        end=ms[k+1].start() if k+1<len(ms) else len(t)
        d=m.group(1)
        E.append((c,i,d[6:]+'-'+d[3:5]+'-'+d[:2],re.sub(r'\s+',' ',m.group(2)).strip().lower(),re.sub(r'\s+',' ',t[m.start():end])))
pickle.dump(E,open('s04_entries.pkl','wb'))
print(len(E))
