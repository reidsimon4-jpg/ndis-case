import json,re,collections
L=[json.loads(l) for l in open('S09_events.jsonl')]
rows=[l.rstrip('\n').split('|') for l in open('S09_roles.tsv') if l.strip()]
ppl=collections.OrderedDict()
ren={'Jan Nuttal':'Jan Nuttall','McMillan':'Kathryn McMillan','Karen (service provider)':'Karen (service provider)','Virginie':'Virginie Fanny-Dulloo','Virginie Dulloo':'Virginie Fanny-Dulloo','Tori':'Tori Fitton','Mischin':'DP Mischin','Lazanas':'DP Lazanas','Bec Hayward':'Bec Hayward','Hayley Bird':'Hayley Bird','B Payne':'Brendan Payne'}
for n,r,o,s in rows:
    n=ren.get(n,n)
    if n in ppl:
        if len(r)>len(ppl[n]['role']) and 'allegedly' not in r: pass
        continue
    ppl[n]=dict(name=n,role=r,organisation=o,side=s.lower())
extras=[
('Elanor Smith','Former FFG staff; per Simon fired just before the 2022 investigation and alleged (Simon position) to have orchestrated the complaints with Terri Roberts; named by Tabatha Sadler as having asked her to provide information to the Commission','FFG (former)','third_party'),
('Janine Hall','FFG Support Coordinator / Service Manager; compiled "Janine Hall Information 18.07.22" supplied to Commission/NDIA (T9.14-T9.17)','FFG (former)','third_party'),
('Brodie Hall','FFG staff member recorded as resigned 6 May 2022 (appears in resignations list in corpus ids 14/189, outside slice S09)','FFG (former)','third_party'),
('Tabatha Sadler','Recovery Support Worker, St Barts Medina; emailed Commission officer Cade Brown 17 Jul 2022 re Meghan Goodwin (T9.20, Att 10)','St Barts Medina','third_party'),
('Cade Brown','Commission officer who received Sadler complaint email 17 Jul 2022','NDIS Commission','commission'),
('Kristen Walker','Commission officer; 1 Dec 2022 counsellor-register search inside briefing note dated 19 Oct 2022 (T9.19, Att 9F)','NDIS Commission','commission'),
('Jason Mangion','NDIA officer (Halls recipient 11-12 Aug 2022 re Nuttall follow-up, T9.22)','NDIA','ndia'),
('Karen Haywood','Commission investigator attending 6 Jun 2025 directions hearing','NDIS Commission','commission'),
('Matt Barr','Commission officer; prepared NOI brief EC22-002103 (per memory)','NDIS Commission','commission'),
('Deepika Thimapuram','Assistant Director - FOI, NDIS Commission; s 24AB notice on 3 Jul 2026 FOI request','NDIS Commission','commission'),
('Seyi Akosile','CDPP FOI decision-maker; s 25 FOI Act neither confirm nor deny decision (17 Aug 2026)','CDPP','cdpp'),
('Ayesha Charan','Lawyer, ATO Office of General Counsel; FOI-2026-00901/00902 decisions (31 Aug 2026)','ATO','other'),
('Jake Langdon','AGS lawyer; emailed refreshed minute 28 Sep 2026','AGS','ags'),
('Sally Davis','AGS signatory (for Karlie Dickinson) of 14 Aug 2026 Proposed Minute of Order','AGS','ags'),
('Rosaji','CDPP prosecutor at 23 Feb 2024 discontinuance hearing','CDPP','cdpp'),
('M.L. Buchanan','Counsel at 23 Feb 2024 hearing (certified transcript PE 45655-45658/2022)','Counsel','unknown'),
('G. Randazzo','Magistrate, 23 Feb 2024 discontinuance','Magistrates Court WA','court'),
('Emilios Kyrou','ART President (timeliness complaint / mandamus sequence in 2026 plan)','ART','tribunal'),
('Huong Nguyen','Director of Infinity Living Options per proposed-ban NOI (Nov 2022)','Infinity Living Options','other'),
('Katherine Karunarathna','Director of Sunflower Care Services; applicant in Sunflower (No 2) [2025] FCA 1442','Sunflower Care Services','other'),
('Feutrill J','Federal Court judge, Sunflower (No 2) [2025] FCA 1442 (21 Nov 2025)','Federal Court','court'),
('P Spender','ART Senior Member, Abdullah [2026] ARTA 743 (6 May 2026)','ART','tribunal'),
('D Katter','AAT Senior Member, Johnston [2024] AATA 3438','AAT','tribunal'),
('Kerryn Wood','Witness; statement 0185 WOODKerryn_PPT_220223 (on Box/OneDrive per memory)','unknown','third_party'),
('Merina Craig','Mother of participant Janine Craig','participant family','third_party'),
('Jason Mangion','NDIA officer','NDIA','ndia'),
]
for n,r,o,s in extras:
    if n not in ppl: ppl[n]=dict(name=n,role=r,organisation=o,side=s)
    elif n in('Jan Nuttall',): pass
ppl['Jan Nuttall']['role']='Ex-FFG Operations Manager; fired 29 Jun 2022 per Danica Hall statement; complaint to NDIA 11 Aug 2022 (T9.22)'
ppl['Jan Nuttall']['note']='backstory_link'
for n in ['Terri Roberts','Elanor Smith','Janine Hall','Danica Hall','Brodie Hall','Nathan Halls']: ppl.get(n,{}).__setitem__('note','backstory_link')
# NurseAssist: Amanda Damon, Terri Roberts
ppl['Amanda Damon']['note']='backstory_link'
def txt(e): return (e['who']+' '+e['what']).lower()
short=set(['Jasmin','Julian','Liam','Crystal','Kim','Bali','Tori Fitton','Mark (ATO)','Reg (applicant side)','Karen (service provider)','Rosaji','Daniel K','Christie O','Rachel S','Jessica P','Leah N','Dylan T','Brylee G','Madeleine S','Pierce S','Damian M','Kathy L','Tracy L','Willem W','Bennett'])
out=[]
for n,p in ppl.items():
    nl=n.lower(); last=nl.split()[-1]
    hits=[]
    for e in L:
        pl=[x.lower() for x in (e.get('people') or [])]
        if nl in pl or any(x==nl for x in pl) or e['who'].lower().startswith(nl):
            hits.append(e); continue
        if n not in short and len(n.split())>=2 and nl in txt(e): hits.append(e)
    hits.sort(key=lambda e:e['date'])
    ka=[f"{e['date']}: {e['what'][:130]}" for e in hits[:5]]
    if len(hits)>5: ka.append(f"... {len(hits)} events in S09 (to {hits[-1]['date']})")
    if not ka: ka=['named in role listing / source; no dedicated event in S09']
    srcs=sorted(set(str(e['source_id']) if e['source_id'] else e['locator'].split(';')[0][:60] for e in hits)) or ['489']
    q=dict(name=n,role=p['role'],organisation=p['organisation'],side=p['side'],key_acts=ka,sources=srcs[:12],n_events=len(hits))
    if 'note' in p: q['note']=p['note']
    out.append(q)
with open('/tmp/S09_people_stage.jsonl','w') as f:
    for q in out: f.write(json.dumps(q,ensure_ascii=False)+'\n')
print(len(out), sum(1 for q in out if q['n_events']==0))
