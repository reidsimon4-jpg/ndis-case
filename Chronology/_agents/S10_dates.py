import sys,re,os
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/')
pat=re.compile(r'(\b\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+20\d\d|\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d\d|\b\d{1,2}[./]\d{1,2}[./](20)?\d\d\b)')
for a in sys.argv[1:]:
    fn=[f for f in os.listdir(base) if f.startswith(a.zfill(5))][0]
    t=open(base+fn,encoding='utf-8',errors='ignore').read()
    lines=t.split('\n'); off=0
    print('#####',fn,len(t))
    for ln in lines:
        if pat.search(ln): print(off,ln[:int(os.environ.get('W','350'))])
        off+=len(ln)+1
