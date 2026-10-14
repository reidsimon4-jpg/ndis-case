import json,subprocess,os,sys
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build')
SRC={336:'NDIS Case/ART_FOI_2026-1839/8 - File notes and internal emails  - 2023.4494.pdf',
335:'NDIS Case/ART_FOI_2026-1839/7 - External emails to respondent - 2023.4494.pdf',
334:'NDIS Case/ART_FOI_2026-1839/6 - Received administrative documents - 2023.4494.pdf',
326:'NDIS Case/ART_FOI_2026-1839/12 - T - documents for case 2023.4494.pdf',
327:'NDIS Case/ART_FOI_2026-1839/13 - Constitution report.pdf',
328:'NDIS Case/ART_FOI_2026-1839/14 - Listings report.pdf',
329:'NDIS Case/ART_FOI_2026-1839/15 - Emails from national listings team.pdf',
337:'NDIS Case/ART_FOI_2026-1839/ART FOI 2026 1839 — Breach Register & FIRA Analysis.pdf',
338:'NDIS Case/ART_FOI_2026-1839/Notice of Decision - FOI request no. 2026.1839.pdf',
339:'NDIS Case/ART_FOI_2026-1839/Schedule of documents - 2026.1839.pdf'}
def ev(sid,date,who,what,how,why,cat,loc,prec='day',status='fact',conf='high',**kw):
    d=dict(date=date,date_precision=prec,who=who,what=what,how=how,why=why,category=cat,status=status,source_file=SRC[sid],source_id=sid,locator=loc,confidence=conf)
    d.update(kw); return d
def push(kind,recs):
    p=subprocess.run(['python3',B+'/add.py','S11',kind],input='\n'.join(json.dumps(r,ensure_ascii=False) for r in recs),text=True,capture_output=True)
    print(p.stdout,p.stderr)
