import sys,os,re
s=int(sys.argv[1]); n=int(sys.argv[2])
t=open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/00014.txt'),encoding='utf-8',errors='ignore').read()
c=t[s:s+n]
c=re.sub(r'[ \t]{2,}','  ',c); c=re.sub(r'\n\s*\n+','\n',c)
print(f'[{s}-{s+n}]');print(c)
