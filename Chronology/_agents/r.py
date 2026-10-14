import sys,os,re
s=int(sys.argv[1]); n=int(sys.argv[2])
t=open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/00014.txt'),encoding='utf-8',errors='ignore').read()
seg=t[s:s+n]
seg=re.sub(r'[ \t]{3,}','  ',seg); seg=re.sub(r'\n\s*\n+','\n',seg)
print(f'[{s}-{s+n}]'); print(seg)
