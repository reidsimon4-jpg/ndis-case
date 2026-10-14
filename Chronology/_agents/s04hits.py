import os,re,json
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
K=re.compile(r'complain|investigat|police|\bcease|terminat|freez|Commission|fraud|\bexit|cancel|discharge|no longer (want|wish)|end (of )?(our |the )?(service|agreement)|withdraw|reported to|\bsolicitor|lawyer|\bNDIA\b.{0,40}(review|plan)|changed? (plan )?manag|switch',re.I)
dre=re.compile(r'^(\d{2}/\d{2}/\d{4})\s+(\S.*?)\s{2,}')
out=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)<5 or not p[0].isdigit() or 'CLIENTS/' not in p[4]: continue
    i=int(p[0]); m=re.search(r'CLIENTS/./([^/]+)/',p[4]); cl=m.group(1)
    lines=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read().split('\n')
    cur=None;au=None
    for n,line in enumerate(lines):
        mm=dre.match(line)
        if mm: cur=mm.group(1);au=mm.group(2)
        if K.search(line):
            out.append((cl,i,n,cur,au,line.strip()[:260]))
with open('s04hits.tsv','w',encoding='utf-8') as f:
    for o in out: f.write('\t'.join(str(x) for x in o)+'\n')
print(len(out))
