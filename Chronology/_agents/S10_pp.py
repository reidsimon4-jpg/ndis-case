import json,collections,subprocess,os
ev=collections.defaultdict(list)
for l in open('S10_events.jsonl'):
    o=json.loads(l)
    for p in o.get('people',[]): ev[p].append(o)
# canonical: (aliases) , role, org, side
R={
'Vida Reid':([],'Applicant (ART 2023/3361); FFG director/CEO; Hall-era complainants target','FFG / Applicant','Applicant'),
'Simon Reid':([],'Applicant (ART 2023/3363) in person; former/current FFG director (periods conflict); Hybrid Hive director','FFG / Applicant','Applicant'),
'Nathan Halls':([],'NDIA officer (WA) alleged central actor in provider exit / Project Archer referrals; subject of improper-purpose contention','NDIA','NDIA'),
'Karlie Dickinson':([],'Senior Lawyer, AGS for the Commission','AGS','AGS'),
'Philip Halton':([],'NDIS Commissioner; signed EC22-002000 recommendations / decision-maker on banning orders','NDIS Quality and Safeguards Commission','Commission'),
'Sukhi Tear':([],'Diversitas WA support coordinator; alleged recipient of Halls referrals (backstory_link)','Diversitas WA / Nurse Assist 24/7','Provider'),
'Tom Monks':([],'Principal, Tom & Co Legal; Applicants\' solicitor (banning orders, internal review)','Tom & Co Legal','Applicant_lawyer'),
'Virginie Fanny-Dulloo':([],'Dream Big / FFG-related staff; recorded interviewee 9 Mar 2023; records produced in Vida matter','Dream Big (FFG-linked)','Applicant_staff'),
'Jonathan Shapiera':([],'Participant / complainant (father of Nikolaus Shapiera); source of Tear/Halls allegations','Participant','Participant'),
'John Maloney':([],'Investigator (alleged witness coercion Jan 2025 per draft s 73ZO application)','Commission (per draft)','Commission'),
'Sian Leathem':([],'Internal review delegate; IR(6) 22/23 and IR(7) 22/23 decisions 21 Apr 2023','NDIS Commission','Commission'),
'Gina Nofal':([],'Bennett Law solicitor acting for Vida/FFG 2022 (cease and desist to Diversitas)','Bennett Law','Applicant_lawyer'),
'Karen Ruth':([],'Plan manager; audio re Halls instruction not to pay FFG invoices (Oct 2022)','Plan manager','Plan_manager'),
'Amanda Damon':([],'Nurse Assist / Diversitas-linked individual in 17 Aug 2022 assault allegation (backstory_link)','Nurse Assist 24/7','Provider'),
'Jan Nuttall':([],'Interviewee whose interview Simon seeks produced (backstory_link); NDIA/Commission witness','NDIA (per directions)','Other'),
'Cassandra Burke':([],'Commission witness (statement 16 Feb 2023 with annexures)','Commission','Commission'),
'Tim Jarratt':(['Jarratt'],'NDIA officer; canvassed participants 7-11 Oct 2022; Package 2 summons target','NDIA','NDIA'),
'Charles Dallimore':([],'Lawyer who wrote to Vida 9 Jan 2025 re ongoing investigation','Applicant counsel (firm not stated)','Applicant_lawyer'),
'Meghan Goodwin':([],'Participant allegedly removed from FFG-supported living Aug 2022','Participant','Participant'),
'Rachel Robson':([],'Diversitas/agency-side author of 16 Aug 2022 email to DFG Legal (role per event text)','Diversitas / DFG Legal correspondence','Other'),
'Barbie Lundgren':(['Barbara Lundgren','Lundgren'],'NDIA A/State Manager WA; recipient of Oct 2022 complaint; Package 2 summons target','NDIA','NDIA'),
'Kirsty Stynes':(['K. Stynes'],'CDPP prosecutor; appeared 23 Feb 2024 dismissal; complaint recipient 29 Sep 2024','CDPP','CDPP'),
'Terri Roberts':([],'Complainant/witness; relayed Shapiera report to Bennett Law (backstory_link)','Participant side','Participant_family'),
'Kathryn McMillan':([],'ART Deputy President (KC); case-management directions 8 Sep 2025','ART','Tribunal'),
'Chloe Osborne':([],'Named in Nurse Assist/Diversitas connection map and 17 Aug 2022 event','Nurse Assist 24/7','Provider'),
'Amanda Manni':([],'Diversitas staff; Teams meeting remark per Dawson statement','Diversitas WA','Provider'),
'Charles Weeks':([],'Weeks & Co solicitor drafting Vida affidavit Jan 2025','Weeks & Co','Applicant_lawyer'),
'Bruce Graydon':([],'NDIA officer; Package 2 summons target','NDIA','NDIA'),
'Rejaul Alam':([],'FFG CFO named in Tactical Intelligence Report as likely participant in fraud','FFG','Applicant_staff'),
'Pieter Rossouw':([],'Nurse Assist connection-map person (June 2026 discovery plan)','Nurse Assist 24/7','Provider'),
'Mischin':(['DP Mischin','Deputy President Mischin'],'ART Deputy President; made 26 Jul 2024 non-disclosure orders','ART','Tribunal'),
'Candice Jonker':([],'Solicitor/representative in Goodwin removal correspondence (role not stated)','not stated','Other'),
'Madeline Dawson':(['Madeleine Dawson'],'FFG support worker; alleged assault victim 17 Aug 2022; statement 19 Mar 2024','FFG','Applicant_staff'),
'Nikolaus Shapiera':([],'Participant (son of Jonathan Shapiera)','Participant','Participant'),
'Maddison Millan':([],'NDIA record author 5 Oct 2022 (consent removed for FFG)','NDIA','NDIA'),
'Daniel Rice':([],'Hammond Legal lawyer; costs agreement for malicious prosecution matter 19 Sep 2024','Hammond Legal','Applicant_lawyer'),
'Isobelle Saville':([],'CDPP officer; complaint recipient 29 Sep 2024','CDPP','CDPP'),
'Hayley Bird':([],'ART registry officer (Dec 2025 hearing lapse email)','ART','Tribunal'),
'G. Randazzo':([],'Magistrate; dismissed four charges 23 Feb 2024','Magistrates Court WA','Court'),
'Brenda Ryan':([],'NDIA/participant-side meeting attendee 7-10 Oct 2022','NDIA (per event)','NDIA'),
'Sarah-Jane Clulow':(['SJ Clulow'],'Participant; complaint to Commission about 6 Jul 2022','Participant','Participant'),
'Ousman Kamara':([],'Person who appears to have signed for registered-post notices of intention 7 Dec 2022 (unverified)','not stated','Other'),
'Craig Land':([],'AGS lawyer cc\'d in draft verification letter','AGS','AGS'),
'Shadi Norouzi':([],'NDIA planner/officer; 2 Feb 2022 email to FFG re over-utilisation','NDIA','NDIA'),
'Nadav Strum':([],'Yaran Property Group recipient of Halls 29 Sep 2022 provider-exit email','Yaran Property Group','Other'),
'Christine Arthur':([],'Bennett Law lawyer','Bennett Law','Applicant_lawyer'),
'Martin Bennett':([],'Bennett Law principal','Bennett Law','Applicant_lawyer'),
'Linda Bill':([],'Participant allegedly phoned by Halls 5 Oct 2022','Participant','Participant'),
'Frank (Modplex)':([],'Former FFG business contact allegedly phoned by NDIA investigators Mar 2024','Modplex Construction','Other'),
'Deepak Bhandari':(['Bhandari'],'NDIA officer; 17 Oct 2022 email cancelling FFG support coordination, naming Diversitas','NDIA','NDIA'),
'Tori Fitton':(['Fitton'],'Dream Big director/compliance subject of s 56 notice 20 Jan 2023; Fitton sole director per ASIC claim','Dream Big','Applicant_staff'),
'Monaz Kasad':([],'WA Consumer Protection conciliation officer file 271714','WA Consumer Protection','Other'),
'Kristen Walker':([],'Commission officer named in EC22-002000 (role in brief)','Commission','Commission'),
'Katja Zerafa':([],'Commission officer named in EC22-002000 (role in brief)','Commission','Commission'),
'Danica Hall':([],'Former FFG employee; resigned 19 Jul 2022; Evidence Package to Commission (backstory_link Hall family)','FFG (former)','Participant_family'),
'Cade Brown':([],'Former Acting AD Compliance (WA), Commission; took Danica Hall statement','NDIS Commission','Commission'),
'Janine Hall':([],'Former FFG employee/complainant; Evidence Package ~18 Jul 2022 (backstory_link Hall family)','FFG (former)','Participant_family'),
'Matt Read':([],'Assistant Director, Commission; contact on s 56 notice 20 Jan 2023','NDIS Commission','Commission'),
'Julian (ABF officer)':([],'ABF officer at Perth Airport stop 25 Sep 2024','ABF','ABF'),
'Mark (ATO)':([],'ATO officer on phone call (21 Aug 2023 / 7 Jan 2026 transcript)','ATO','ATO'),
'Tori Vince':([],'Named as sole FFG director in FFG statement; possibly same person as Tori Fitton (unverified)','FFG','Applicant_staff'),
'Isabelle Macdonald':([],'AGS lawyer cc\'d in draft verification letter','AGS','AGS'),
'DP Lazanas':([],'ART Deputy President; Oct-Nov 2024 stay orders','ART','Tribunal'),
'Sally Davis':([],'Respondent/AGS-side sender of proposed minute 14 Aug 2026','AGS (per event)','AGS'),
'Feutrill J':([],'Federal Court judge; Sunflower Care (No 2) [2025] FCA 1442','Federal Court','Court'),
'Gerard Righetti':([],'NDIA fraud investigator taking witness statements Oct 2022','NDIA','NDIA'),
'Sian Harsley':([],'NDIA fraud investigator taking witness statements Oct 2022','NDIA','NDIA'),
'Fiona Lane':([],'NDIA fraud investigator taking witness statements Oct 2022','NDIA','NDIA'),
'Christine Bruckner':([],'NDIA fraud investigator (Investigator Bruckner)','NDIA','NDIA'),
'Matt Barr':([],'Commission officer; EC22-002103 signature 17 Nov 2022','NDIS Commission','Commission'),
'Andrew Hahn':([],'Participant allegedly threatened with eviction (Hall evidence)','Participant','Participant'),
'Tabatha Sadler':([],'Complainant emailed Commission 17 Jul 2022 re Goodwin welfare','Complainant','Other'),
'Steven Norman':([],'Former sole director Hybrid Hive (17 Jun-1 Dec 2021) and The Hive (to 7 Nov 2021)','Hybrid Hive / The Hive','Applicant_staff'),
'Annette Ogden':([],'Participant named in s 56 notice (Dream Big supports Dec 2022)','Participant','Participant'),
'Blake Sadler':([],'Dream Big decision-maker per Fanny-Dulloo interview 9 Mar 2023','Dream Big','Applicant_staff'),
'Pascal Moussa':([],'Commission internal reviewer; 22 Mar 2023 new-information letter','NDIS Commission','Commission'),
'Bill Shorten':([],'Minister; joint media release 23 Dec 2022','Government','Other'),
'Tracy Mackey':([],'NDIS Commissioner named in 23 Dec 2022 media release (per event)','NDIS Commission','Commission'),
'Jason Moore':([],'NDIA/investigator; called Modplex Mar 2024 (per memo)','NDIA','NDIA'),
'Bec Hayward':([],'Reported home visit by investigators late 2024','Other','Other'),
'Alex Bowers':([],'Reported home visit by investigators late 2024','Other','Other'),
'Marie Ross':([],'NDIS officer cc\'d on 16 Aug 2022 reply','NDIA','NDIA'),
'Brooke Andrews':([],'Nurse Assist connection-map person','Nurse Assist 24/7','Provider'),
'Faryar Gorjy':([],'Forwarded Halls 29 Sep 2022 provider-exit email to Vida 7 Oct 2022','Yaran Property Group (per event)','Other'),
'William Cocks':([],'AHRC complaint officer Aug-Oct 2025','AHRC','Other'),
'Elanor Smith':([],'Resigned from FFG 29 Mar 2022; complaint to NDIA (backstory_link)','FFG (former)','Participant_family'),
'Emilios Kyrou':([],'ART President (Justice AO); addressee of draft Guidance and Appeals Panel request','ART','Tribunal'),
'Rasha Rushdy':([],'Insurer IDR decision-maker 13 Feb 2023 (FFG PI claim)','Swiss Re','Other'),
'L. Cooper':([],'Insurer decision-maker 27 Feb 2024 (Hybrid Hive claim)','Insurer','Other'),
'Robyn Shannon':([],'Commission officer named on 22 Mar 2023 Show Cause Notice','NDIS Commission','Commission'),
'Andrew Wong':([],'Commission officer named on 22 Mar 2023 Show Cause Notice','NDIS Commission','Commission'),
}
alias={}
for k,(al,_,_,_) in R.items():
    for a in al: alias[a]=k
agg=collections.defaultdict(list)
for n,v in ev.items():
    agg[alias.get(n,n)] += v
out=[]
miss=[n for n in agg if n not in R]
print('MISSING',miss)
for n,(al,role,org,side) in R.items():
    v=agg.get(n,[])
    seen=set(); acts=[]
    for o in sorted(v,key=lambda o:o['date']):
        key=(o['date'],o['what'][:40])
        if key in seen: continue
        seen.add(key)
        acts.append(f"{o['date']}: {o['what'][:150]}")
    d=sorted(o['date'] for o in v)
    r={'name':n,'role':role,'organisation':org,'side':side,'key_acts':acts[:6],'sources':sorted({str(o['source_id']) for o in v})[:12],'first_seen':d[0] if d else None,'last_seen':d[-1] if d else None,'n_events':len(v)}
    if al: r['aliases']=al
    out.append(json.dumps(r,ensure_ascii=False))
base=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build')
p=subprocess.run(['python3','add.py','S10','people'],input='\n'.join(out),text=True,cwd=base,capture_output=True)
print(p.stdout,p.stderr)
