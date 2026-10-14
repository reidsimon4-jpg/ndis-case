# usage: python3 rd.py ID [start] [length]   -> prints corpus text slice (default 0 25000)
import sys,os
a=sys.argv[1]; i=int(a) if a.isdigit() else a; s=int(sys.argv[2]) if len(sys.argv)>2 else 0; n=int(sys.argv[3]) if len(sys.argv)>3 else 25000
t=open(os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_corpus/{i:05d}.txt' if isinstance(i,int) else f'~/mnt/NDIS Case/Chronology/_corpus/{i}'),encoding='utf-8',errors='ignore').read()
print(f'[{i} chars {s}-{min(s+n,len(t))} of {len(t)}]'); print(t[s:s+n])
