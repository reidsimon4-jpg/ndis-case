import json,subprocess,os
SF="NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
def ev(date,who,what,how,why,cat,status,loc,people,conf="high",prec=None,**kw):
    d={"date":date,"date_precision":prec or ("day" if len(date)==10 else "month" if len(date)==7 else "year"),"who":who,"what":what,"how":how,"why":why,
       "category":cat,"status":status,"source_file":SF,"source_id":14,"locator":loc,"confidence":conf,"people":people}
    d.update(kw); return d
def push(lst,kind="events"):
    s="\n".join(json.dumps(x,ensure_ascii=False) for x in lst)
    r=subprocess.run(["python3",os.path.expanduser("~/mnt/NDIS Case/Chronology/_build/add.py"),"S01",kind],input=s.encode(),capture_output=True)
    print(r.stdout.decode(),r.stderr.decode()[:500])
