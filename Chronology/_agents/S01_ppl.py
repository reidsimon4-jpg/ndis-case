import json,re
ev=[json.loads(l) for l in open('S01_events.jsonl')]
P=[json.loads(l) for l in open('S01_people.bak.jsonl')]
byn={x['name']:x for x in P}
# renames
byn['Lea W']['name']='Lea Warner'; byn['Lea W'].setdefault('aliases',[]).append('Lea W')
byn['Richard P']['name']='Richard Paul'; byn['Richard P'].setdefault('aliases',[]).append('Richard P')
def al(n,*a):
    x=[q for q in P if q['name']==n][0]; x['aliases']=sorted(set(x.get('aliases',[])+list(a)))
al('Tori Fitton','Tory Fitton'); al('Jan Nuttall','Jan Nuttal'); al('Jonathon Shapiera','Johnathon Shapiera')
al('Jess Goile','Jessica Goile'); al('Alex Bowers','Alex Bowler'); al('Rejaul Alam','MD Rejaul Alam','RJ')
al('Ally Olesiuk','Ally Oleksiuk'); al('Ashleigh Oleksiuk','Ashleigh Olesiuk')
def upd(n,role=None,org=None,side=None):
    x=[q for q in P if q['name']==n][0]
    if role: x['role']=role
    if org: x['organisation']=org
    if side: x['side']=side
upd('Janine Hall','Support Coordinator / Service Manager, FFG (started 1 Dec 2021 per her own 30 Mar 2022 email); anonymous NDIA fraud-line reporter from 30 Mar 2022 while employed (case 1A0000031700RE); supplied the 18.07.2022 Information Parts 1-5 to the Commission; forwarded FFG emails to her personal Gmail from 3 May 2022; gave Jan Nuttall NDIA officer Nathan Halls\' number (which she had from Elanor Smith); still employed 20 Jul 2022 per Danica Hall',org='FFG (former employee by Oct 2022)')
upd('Elanor Smith','Former FFG staff member (resigned 29 Mar 2022 per Danica Hall list); per T9.20 prompted Tabatha Sadler to write to the Commission on 17 Jul 2022; per Nathan Halls (T9.22) gave Janine Hall his phone number',org='FFG (former)')
upd('Tanya Gukwa','Support Coordinator/Recovery Coach, FFG; emailed resignation letter 1 Jul 2022 8:44 AM (honesty, integrity, structure); Danica Hall list gives 5 Jul 2022; Vida linked her resignation to Jan Nuttall (1 Jul 2022)',org='FFG')
upd('Jan Nuttall','Operations Manager, FFG (joined 2022 per Vida 31 May 2022 email; active at FFG 13-27 Jun 2022; Danica Hall dates departure 29 Jun 2022; Vida on 1 Jul 2022 calls her "previous Operations Manager" and says she was messaging staff to quit); contacted NDIA officer Nathan Halls 11 Aug 2022 (number via Janine Hall) and complained against Vida/FFG',org='FFG (former by 1 Jul 2022)')
upd('Danica Hall','Accounts Officer then Accounts Manager (promoted 28 Mar 2022) at FFG; per Janine Hall was emailing NDIA about the alleged fraud by 18 Apr 2022; resigned 19 Jul 2022 per T9.4; statement (Att 7, T9.11) to Commission July 2022',org='FFG (former)')
new=[
("Hayden Trantham","Participant (SIL, Bunbury/Rockingham) named in Janine Hall's NDIA fraud report and Information Part 1","Participant"),
("Yvonne Harrison","Participant named in Janine Hall 30 Mar 2022 NDIA report and Danica Hall statement (plan manager queried Hive invoices)","Participant"),
("Daniel Clark","Participant named in Janine Hall 18 Apr 2022 email (SIL application 1:1 vs 2:1)","Participant"),
("Sarah King","Hybrid Hive (The Hive) staff member (sarah.k@hybridhive.com.au); recipient of Ousman Kamara's 23 Jun 2022 'Immediate effect' email; phoned Janine Hall 23 and 27 Jun 2022; Danica Hall list gives departure 15 Jul 2022","Provider"),
("Isabella Wise","Hybrid Hive staff member cc'd on 23 Jun 2022 'Immediate effect' email","Provider"),
("Tammy Doidge","Hybrid Hive staff member cc'd on 23 Jun 2022 'Immediate effect' email","Provider"),
("Melissa Byfield","Local Area Coordinator (APM, NDIS partner) for Angela Cutler's plan review; Mar 2022 emails with Vida Reid","Other"),
("Angela Cutler","Participant; bathroom/ensuite modification quotes (Modplex PP220712, $85,800)","Participant"),
("Francesco","Modplex Construction builder ('Frank') producing Cutler home-modification quotes","Other"),
("Tarilee","Modplex Construction accounts (Tarilee/Tari Lee); emails to Vida 22 and 31 Mar 2022","Other"),
("Khaiah Thomson","NDIS Specialised Support/Support Coordinator, Huntington's WA; emails with Tori Fitton re Suzanne Shepard 1-12 Jul 2022","Other"),
("Paddy","Assist Plan Managers staff; emailed Tanya Gukwa 1 Jul 2022 re Eve Adam funds","Plan_manager"),
("Edilyn","Assist Plan Managers queries team; emailed 1 Jul 2022 re invoice NDIS-1919-1","Plan_manager"),
("Assist Plan Managers","Plan manager organisation (Eve Adam, Marisha Lombard, others) - not NurseAssist","Plan_manager"),
("Eve Adam","Participant; Coordination of Supports funds $16.38 left on 1 Jul 2022","Participant"),
("Brodie Hall","FFG/Hive staff member; resigned 6 May 2022 per Danica Hall list; OCR of Ousman Kamara's signature block shows brodie.h@hybridhive.com.au (low confidence)","Provider"),
("Hassan Zia","FFG staff; departure 16 Mar 2022 per Danica Hall list","Provider"),
("Nakita Toia","FFG Support Worker/cook; departure 28 Mar 2022 per Danica Hall list","Provider"),
("Jaimi Lee Smith","FFG staff; fired 6 Apr 2022 per Danica Hall list","Provider"),
("Blesson Varghese","FFG staff; departure 23 Jun 2022 per Danica Hall list; recipient of 31 May 2022 all-staff email","Provider"),
("Emma Imani","FFG staff; resigned (no date) per Danica Hall list","Provider"),
("Rachael Thomas","FFG staff; resigned (no date) per Danica Hall list","Provider"),
("Shadi Norouzi","FFG staff; resigned (no date) per Danica Hall list","Provider"),
("Janine Craig","Person invoiced by The Hive since Aug 2021 though allegedly never a Hive participant (Danica Hall statement)","Participant"),
("Angelus Regali-Park","Participant removed from FFG by nominee Gina Regali after Manage Mode queried invoice (Danica Hall statement)","Participant"),
("Gina Regali","Nominee (mother) of Angelus Regali-Park","Participant_family"),
("Maria Staltari","Participant (Bunbury); draft counselling invoices deleted (Danica Hall statement); Modplex quote also sent","Participant"),
("Hazel Carbungco","FFG Support Coordinator whose name appeared on counselling invoices (alleged not AHPRA registered, per Danica Hall)","Provider"),
("Linda Bill","Named by Danica Hall as Simon Reid's father's partner supported/employed by The Hive (allegation)","Other"),
("Graeme Ogden","Named in Ugwunali statement (T5) re Annette Ogden profit-share discussion","Other"),
("Heather Ankor","Ex-FFG client who moved to ACCESS (per Ugwunali)","Participant"),
("Jacob Bonasera","Ex-FFG client who moved to ACCESS (per Ugwunali)","Participant"),
("Jonah Bonasera","Ex-FFG client who moved to ACCESS (per Ugwunali)","Participant"),
("Jasiah Bonasera","Ex-FFG client who moved to ACCESS (per Ugwunali)","Participant"),
("King Tin (Aaron) Chan","Ex-FFG client who moved to ACCESS (per Ugwunali)","Participant"),
("Jenny (FFG staff, surname not given)","FFG front-office staff who greeted Paul Ugwunali June 2022 (per T5)","Provider"),
]
for n,r,s in new:
    if n in [q['name'] for q in P]: continue
    P.append({"name":n,"aliases":[],"role":r,"organisation":"FFG/Hybrid Hive" if s=="Provider" else ("Assist Plan Managers" if n.startswith(("Paddy","Edilyn","Assist")) else "n/a"),"side":s,"key_acts":[],"first_seen":"","last_seen":"","sources":[14],"_slice":"S01"})
# recompute key_acts / dates
def nm(s): return re.sub(r'[^a-z0-9]','',s.lower())
for x in P:
    keys={nm(x['name'])}|{nm(a) for a in x.get('aliases',[])}
    acts=[];dates=[]
    for e in sorted(ev,key=lambda e:e['date']):
        if any(nm(p) in keys for p in e.get('people',[])):
            acts.append(f"{e['date']}: {e['what'][:150].strip()} [{e['locator'][:40]}]"); dates.append(e['date'])
    if acts:
        x['key_acts']=acts[:14]
        d0=dates[0]; d1=dates[-1]
        pad=lambda d: d+'-01'*(3-len(d.split('-')))
        x['first_seen']=pad(d0); x['last_seen']=pad(d1)
    else:
        x.setdefault('first_seen',x.get('first_seen','')); 
    x['sources']=sorted(set(x.get('sources',[14])))
    if not x.get('key_acts'): x['key_acts']=[x['role']]
    if not x.get('first_seen'): x['first_seen']='2022-01-01'; x['last_seen']='2022-12-31'; x['_note']='dates unspecified'
open('S01_people.jsonl','w',encoding='utf-8').write('\n'.join(json.dumps(x,ensure_ascii=False) for x in P)+'\n')
print(len(P))
