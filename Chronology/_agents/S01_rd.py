import sys,os,re
t=open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/00014.txt'),encoding='utf-8',errors='ignore').read()
pg=t.split('\f')
a=int(sys.argv[1]); b=int(sys.argv[2])  # pdf page idx range inclusive-exclusive
off=0;offs=[]
for p in pg: offs.append(off); off+=len(p)+1
for i in range(a,b):
    s=re.sub(r'[ \t]{3,}','  ',pg[i]); s=re.sub(r'\n\s*\n+','\n',s)
    if len(s.strip())<40: print(f'--[idx{i} @{offs[i]}] (blank/image)'); continue
    print(f'=====[idx{i} @{offs[i]}]'); print(s)
