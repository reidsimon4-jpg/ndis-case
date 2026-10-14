import sys,json,subprocess,os
# usage: S11_w.py ID  (stdin JSONL with partial fields; fills defaults)
SF={336:"NDIS Case/ART_FOI_2026-1839/8 - File notes and internal emails  - 2023.4494.pdf",
335:"NDIS Case/ART_FOI_2026-1839/7 - External emails to respondent - 2023.4494.pdf",
334:"NDIS Case/ART_FOI_2026-1839/6 - Received administrative documents - 2023.4494.pdf",
333:"NDIS Case/ART_FOI_2026-1839/5 - Respondent submissions - 2023.4494.pdf",
326:"NDIS Case/ART_FOI_2026-1839/12 - T - documents for case 2023.4494.pdf",
327:"NDIS Case/ART_FOI_2026-1839/13 - Constitution report.pdf",
328:"NDIS Case/ART_FOI_2026-1839/14 - Listings report.pdf",
329:"NDIS Case/ART_FOI_2026-1839/15 - Emails from national listings team.pdf",
337:"NDIS Case/ART_FOI_2026-1839/ART FOI 2026 1839 — Breach Register & FIRA Analysis.pdf",
338:"NDIS Case/ART_FOI_2026-1839/Notice of Decision - FOI request no. 2026.1839.pdf",
339:"NDIS Case/ART_FOI_2026-1839/Schedule of documents - 2026.1839.pdf"}
sid=int(sys.argv[1]); out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    o=json.loads(l)
    o.setdefault('date_precision','day'); o.setdefault('status','fact'); o.setdefault('confidence','high')
    o.setdefault('category','tribunal'); o.setdefault('how','AAT/ART case system file note')
    o.setdefault('why','not stated in source')
    sid2=o.pop('sid',sid)
    o['source_id']=sid2; o['source_file']=SF[sid2]
    o.setdefault('people',[])
    out.append(json.dumps(o,ensure_ascii=False))
p=subprocess.run(['python3','add.py','S11','events'],input='\n'.join(out)+'\n',text=True,capture_output=True)
print(p.stdout,p.stderr)
