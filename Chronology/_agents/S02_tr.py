import sys,os,re
s=int(sys.argv[1]); n=int(sys.argv[2])
t=open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/00014.txt'),encoding='utf-8',errors='ignore').read()
c=t[s:s+n]
out=[]
for l in c.split('\n'):
    l=l.strip()
    if not l: continue
    l=re.sub(r'^\d{1,2}\s+','',l)
    if re.match(r'^(T58|TRANSCRIPT-IN-CONFIDENCE|\[M Fanny-Dulloo\]|Transcript prepared by.*|09 March 2023\s+Page.*|\d{4})$',l): continue
    out.append(l)
txt=' '.join(out)
txt=re.sub(r'\s+',' ',txt)
# break at speaker labels
txt=re.sub(r' (READ:|FANNY-DULLOO:|HAYWOOD:)',r'\n\1',txt)
print(f'[{s}-{s+n}]');print(txt)
