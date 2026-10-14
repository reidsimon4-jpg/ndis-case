# usage: python3 gr.py "regex" ID [ID...] [--ctx 200]  -> matches with char offsets (case-insens)
import sys,os,re
a=sys.argv[1:]; ctx=200
if '--ctx' in a: k=a.index('--ctx'); ctx=int(a[k+1]); a=a[:k]+a[k+2:]
pat=re.compile(a[0],re.I)
for x in a[1:]:
    t=open(os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_corpus/{int(x):05d}.txt'),encoding='utf-8',errors='ignore').read()
    for m in list(pat.finditer(t))[:60]:
        print(f'--{int(x):05d} @{m.start()}: '+t[max(0,m.start()-ctx):m.end()+ctx].replace('\n',' '))
