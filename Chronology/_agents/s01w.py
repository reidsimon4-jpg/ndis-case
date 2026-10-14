import sys,json,subprocess,os
kind=sys.argv[1]
SF="NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    try: o=json.loads(l)
    except Exception as e: print("BADJSON",l[:80]); continue
    if kind=='events':
        o.setdefault('date_precision','day' if len(o['date'])==10 else ('month' if len(o['date'])==7 else 'year'))
        o.setdefault('source_file',SF); o.setdefault('source_id',14)
        o.setdefault('confidence','high'); o.setdefault('status','fact')
        o.setdefault('how','not stated'); o.setdefault('why','not stated in source')
        o.setdefault('category','other'); o.setdefault('people',[])
    else:
        o.setdefault('sources',[14]); o.setdefault('key_acts',[])
    out.append(json.dumps(o,ensure_ascii=False))
p=subprocess.run(['python3','add.py','S01',kind],input="\n".join(out),text=True,capture_output=True,cwd=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build'))
print(p.stdout,p.stderr)
