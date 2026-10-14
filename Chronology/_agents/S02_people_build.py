import json,os,re,subprocess
ev=[json.loads(l) for l in open('S02_events.jsonl',encoding='utf-8')]
ALIAS={"Alexsis Bott":"Alexis Bott","Barry McDonald":"Barry MacDonald","Bassam Haidar":"Bassam Haider","Cassandra Burke":"Cassandra Lee Burke",
"Elanor Smith":"Elanor Smith","Eleanor Smith":"Elanor Smith","Elanore Smith":"Elanor Smith","Giuseppe Circelli":"Giuseppe Cricelli","Graeme Ogden":"Graham Ogden","Mr Ogden":"Graham Ogden",
"Jessica Rose Smith":"Jessica Smith","Jonathan Shapeira":"Jonathon Shapiera","Jonathan Shapiera":"Jonathon Shapiera","MD Rejaul Alam":"Rejaul Alam","Pieter Rossouw":"Pieter Rousouw",
"Pamela":"Pamela Cricelli","Teri (Terri Roberts)":"Terri Roberts","Virginie Sharon Fanny-Dulloo":"Virginie Fanny-Dulloo","Ms Sutcliffe":"Carrie Sutcliffe","Danica H":"Danica Hall",
"Troy":"Troy (support worker)","Alex":"Alex (unspecified)","Luke":"Luke (behaviour therapist)","Tanya":"Tanya (FFG-linked)","Torri":"Torri (FFG staff 2022)","Evie":"Evie (support coordinator)","Ozzie":"Ozzie (FFG worker)",
"SL (initials only)":"SL (initials only)"}
def canon(n): return ALIAS.get(n,n)
Cm,P,PF,PM,APS,AL='Commission','Participant','Participant_family','Plan_manager','Applicant_staff','Applicant_lawyer'
# name:(role,org,side,aliases)
C={
"Philip Halton":("Branch Head, Operations - North Central West; delegate and original decision-maker (suspension, NOIs, revocation, banning orders of 19 Oct/20-21 Dec 2022; s 56 notice 20 Jan 2023)","NDIS Quality and Safeguards Commission",Cm,[]),
"Sian Leathem":("Complaints Commissioner Executive; internal review delegate (s 100) for Vida, Simon and FFG banning orders (Apr-Jun 2023)","NDIS Quality and Safeguards Commission",Cm,["SL"]),
"Pascal Moussa":("Lawyer; wrote internal review acknowledgement/process letters (Feb-Jun 2023)","NDIS Quality and Safeguards Commission",Cm,[]),
"Kristen Walker":("Assistant Director, Integrated Compliance Operations; co-author of Executive Brief EC22-002581 (T56)","NDIS Quality and Safeguards Commission",Cm,["Ms Walker"]),
"Katja Zerafa":("Senior Compliance Officer; co-author of Executive Brief EC22-002581","NDIS Quality and Safeguards Commission",Cm,[]),
"Carrie Sutcliffe":("Acting State Director (WA); PDMS cc on Brief EC22-002581; joined 7 Feb 2023 call with Fanny-Dulloo","NDIS Quality and Safeguards Commission",Cm,["Ms Sutcliffe"]),
"Natalie O'Neill":("Compliance, Western Australia; telephoned/emailed Fanny-Dulloo 7 Feb 2023","NDIS Quality and Safeguards Commission",Cm,[]),
"Matt Read":("Assistant Director (Perth); contact officer on s 56 notice; interviewed Fanny-Dulloo 9 Mar 2023","NDIS Quality and Safeguards Commission",Cm,[]),
"Keren Haywood":("Commission officer present at the 9 Mar 2023 s 56 interview; recipient of Ugwunali email 9 Feb 2023","NDIS Quality and Safeguards Commission",Cm,["Keren Haywood"]),
"Ms Awwad":("PDMS cc recipient of Executive Brief EC22-002581 (role not stated)","NDIS Quality and Safeguards Commission",Cm,[]),
"Mr Barr":("PDMS cc recipient of Executive Brief EC22-002581 (role not stated)","NDIS Quality and Safeguards Commission",Cm,[]),
"Corina Abraham":("Participant/guardian-side correspondent named in T55 (FFG/Hybrid correspondence 15-19 Jun 2022 incl $4,000 exit fee request)","—",P,[]),
"Christine Bruckner":("NDIA Investigator; took Sarah-Jane Hammond statement 18 Oct 2022","NDIA",'NDIA',[]),
"Bruce Graydon":("NDIS Fraud Investigator; took Cassandra Burke statement 16 Feb 2023","NDIA",'NDIA',[]),
"Narelle Richardson":("NDIA investigator; attended Access Disability Services 16 Feb 2023","NDIA",'NDIA',[]),
"Nathan Halls":("NDIA officer; Burke says she reported FFG/Dream Big to him by email and phone and that he told her Shapiera was agency managed","NDIA",'NDIA',["Andrew Halls (as named by Vida per Burke)"]),
"Andrew Halls":("Named by Burke as person from NDIS whom Vida allegedly blamed for 'malicious claims' (4 Oct 2022) - possibly same as Nathan Halls; unverified","NDIA",'NDIA',[]),
"Marek Svarc":("Named prosecutor in R v Vida Reid Magistrates Court caption on SoMF","WA DPP / prosecution",'CDPP',[]),
"Michael Periera":("Senior Head of Service Delivery; submitted 11 fraud reports to NDIA 26 Aug-21 Sep 2022","Assist Plan Managers / Zettai Pty Ltd",PM,[]),
"Karen Marasigan":("Head of Compliance, Zettai P/L; statement 17 Oct 2022","Zettai Pty Ltd",PM,[]),
"Sally Hansen":("Plan manager; complainant 5 Nov 2021 (confidential)","Provider Choice",PM,[]),
"Tilly Walker":("PlanCare staff; complaint 30 Nov 2021","PlanCare",PM,[]),
"Marc (Manage Mode)":("Manage Mode plan manager contact named in T55","Manage Mode",PM,[]),
"Simon Reid":("Applicant 2023/3363; FFG shareholder/former director; Director and Secretary of The Hive Pty Ltd; banned person","FFG / The Hive / Hybrid Hive group",'Applicant',[]),
"Vida Reid":("Applicant 2023/3361; FFG sole director and shareholder; Hybrid Hive sole Director; banned person; charged 19 Oct 2022 (R v Vida Reid)","FFG / Hybrid Hive",'Applicant',[]),
"Veronica Reid":("Registered member (100 ordinary shares, held non-beneficially) of Dream Big Employment Pty Ltd; 'our trustee' per Fanny-Dulloo","Dream Big Employment Pty Ltd",'Applicant',[]),
"Virginie Fanny-Dulloo":("Director/Secretary of Dream Big Employment Pty Ltd (reg. 29 Oct-31 Oct 2022); formerly FFG/Hybrid Hive accounts officer (per Danica Hall)","Dream Big Employment Pty Ltd",APS,["Marie Sharon Virginie Fanny-Dulloo","Virginie Sharon Fanny-Dulloo"]),
"Tom Monks":("Principal Director; lawyer for Vida, Simon and FFG (31 Oct 2022 onwards)","Tom & Co Legal Pty Ltd",AL,[]),
"Michelle Frost":("Paralegal","Tom & Co Legal Pty Ltd",AL,[]),
"Tori Fitton":("Director of Finance, Dream Big; telephoned Graham Ogden re rent/service agreement on Vida's request (per statements)","Dream Big Employment Pty Ltd",APS,[]),
"Tori Vince":("Name appearing in ASIC extract package T63 (role unverified)","—",'Other',[]),
"Blake Sadler":("Support Coordinator and Recovery Coach FFG; Director of Operations, Dream Big (per draft response); signatory of Sarah Gilbert agreement 7 Jun 2022","FFG / Dream Big",APS,[]),
"Alex Bowers":("FFG support coordinator/authorised person; Dream Big support worker; alleged to have charged cancellation fee to Hammond","FFG / Dream Big",APS,["Alex Fowler [Bowers] (as in Haywood's put-to)"]),
"Honey Nguyen":("FFG staff; photographed participant, cruise invitations/payment requests (per participant statements)","FFG / Hybrid Hive",APS,[]),
"Sally See":("FFG counsellor; subject of qualification allegation (Allegation 6)","FFG",APS,[]),
"Rejaul Alam":("Md Rejaul Alam - PRODA account holder per SoMF; alleged to approve invoices on participants' behalf; shown as Employment Operations Manager on FFG website","FFG / Hybrid Hive",APS,["Md Rejaul Alam"]),
"Ally Oleksiuk":("Client Intake Office, FFG (sender as 'FFG Admin' 28 Mar 2022)","FFG",APS,[]),
"Ozzie (FFG worker)":("FFG worker named by Burke and in complaint of 12 May 2022 (surname not given)","FFG",APS,["Ozzie"]),
"Torri (FFG staff 2022)":("FFG staff named by Burke as remaining in office after 30 Sep 2022 (may be Terri/Tori; unverified)","FFG",APS,["Torri"]),
"Terri Roberts":("Former FFG support coordinator; witness 11 Oct 2022; alleged by Simon to have been an Infinity Living Options director","FFG (former)",APS,["Teri","Terri Susan Roberts"]),
"Danica Hall":("Former FFG Accounts Manager; staff witness 14 Oct 2022 (cc 'Danica H' on 31 Mar 2022 email, unverified)","FFG (former)",APS,["Danica H"]),
"Janine Hall":("FFG support coordinator; staff witness 15 Oct 2022 (T44 date)","FFG (former)",APS,[]),
"Leah Norman":("FFG support coordinator; staff witness 11 Oct 2022 ('invoice bombing')","FFG (former)",APS,[]),
"Pieter Rousouw":("Staff witness 11 Oct 2022; said to have been a director of Infinity Living Options","Infinity Living Options / FFG",APS,["Pieter Rossouw"]),
"Elanor Smith":("Former FFG worker; per Hammond referred her to FFG (Dec 2021); named in T71.1 reasons (internal review of FFG ban) and Hammond's statement","FFG (former)",APS,["Elanore Smith","Eleanor Smith","Elanor Smith"]),
"Cassandra Lee Burke":("Support Coordinator, Access Disability Services (since Oct 2022); formerly FFG Jun/Jul-Oct 2022; witness 16 Feb 2023","Access Disability Services WA",'Provider',["Cassie Burke","Cassandra Burke"]),
"Paul Ugwunali":("Principal, Access Disability Services WA; took on FFG clients/staff Oct-Nov 2022","Access Disability Services WA",'Provider',["Paul Ndubueze Ugwunali"]),
"Graham Ogden":("Participant family; Dream Big service agreement signatory 6 Dec 2022 (Annette Ogden)","—",PF,["Graeme Ogden","Mr Ogden"]),
"Annette Ogden":("Participant; Dream Big service agreement 6 Dec 2022","—",P,[]),
"Tanya Faulkner":("Mable; recipient of alleged 29 Nov 2022 call from Vida","Mable",'Other',[]),
"Joshua Davidson":("Social worker (BSW), Joshua Davidson Therapy; support person for Andrew Hahn","Joshua Davidson Therapy",'Other',[]),
"Dr George Adnrawis":("Witness on complaint 4-35021929094 (11 May 2021)","—",'Other',[]),
"Tegan Bonham":("Nominee/foster mother of Tiffany Rose per T55; emailed FFG accounts 26 Nov 2021","—",PF,[]),
"Mark McGowan":("Then WA Premier named in Clulow statement as person Vida threatened to go to","WA Government",'Other',[]),
}
PART={"Alexis Bott","Bassam Haider","Amber Wilson","Amy Crane","Andrew Hahn","Angela Cutler","Barry MacDonald","Hayden Trantham","Hrimnir Benediktsson","Jonathon Shapiera","Marisha Lombard","Meghan Goodwin","Paul Gilbert","Sarah-Jane Clulow","Sarah-Jane Hammond","Yvonne Harrison","Liz Odi","Sarah Gilbert","Tiffany Rose","Nicole Kelleher","Dee Lilpop","James Harwood","Suzanne Hall","David Germon","Alana Campbell","Gregory Clark","Giuseppe Cricelli","Levi Kenyon","Levi Jetoh","Ziah O'Reilly","Max Teague","Georgios Taraganis","Bejamin Davies","Bekki Mulock","Charlie Harrison","Janine Craig","Miah Williams","Angelus Regali-Park","Jessica Harrison","Ethan Bonham"}
FAM={"Candice Yavarzadeh-Tehrani","Gina Regali","Jerusha Jetoh","Joy Pickering","Lisa Mulock","Marish Cimafranca","Merina Craig","Monbo Jetoh","Rhiannon Teague","Pamela Cricelli","Tracey Kenyon","Paul Totten"}
OTHER_WITNESS={"Rebecca Redick":"LAC (witness on complaint 13 Apr 2021)","Natalia McGregor":"Advocate (complaint 26 Apr 2021)","Namita Sharma":"Complainant (27 Apr 2021)","Natalie Smith":"Participant (complaint 27 Apr 2021)","Evie (support coordinator)":"Support coordinator named in complaint 27 Apr 2021","Liana Diacicov":"Witness (complaint 7 Jun 2021)","Dean Tingey":"Named in complaint 4-35234319303","Sukhi Tear":"Support coordinator (complaint 29 Nov 2021)","Kerryn Wood":"Disability worker; complainant 1 Jan 2022","Rizzie Nel":"COS contact; complaint 11 Mar 2022","Donna Sampson":"Worker; complaint 12 May 2022","Tammy Mogg":"Next of kin of S-J Clulow; complaint 20 May 2022","Ashlee Suckling":"Support worker; complaint 23 Jun 2022","Dianne Andreeva":"Complainant 5 Sep 2022","Janeece Ferreira":"Named in T55 Allegation 7 (non-compete 16 Jun 2022)","Usman Camara":"Worker moved to Access Disability Services (per Haywood)","Alex Reid":"Name as printed in T58 Haywood put-to (unverified)","Ousman Kamara":"Dream Big staff (draft Schedule 1)","Paula Stanford":"Dream Big staff (draft Schedule 1)","Samza Serry":"Dream Big staff (draft Schedule 1)","Troy (support worker)":"Support worker named in complaint 26 Oct 2021","Alex (unspecified)":"Alex named by Clulow (unspecified)","Luke (behaviour therapist)":"Behaviour therapist referred by FFG (per Yavarzadeh-Tehrani)","Tanya (FFG-linked)":"Tanya present at lunch with Vida/Blake (Trantham)","Pamela":"", }
FAM.add("Jessica Smith")
people={}
for e in ev:
    for n in e.get('people',[]):
        people.setdefault(canon(n),[]).append(e)
recs=[]
def norm_date(d): return d if len(d)==10 else (d+'-01' if len(d)==7 else d+'-01-01')
for n,evs in sorted(people.items()):
    evs=sorted(evs,key=lambda e:e['date'])
    acts=[]
    pref=[e for e in evs if n.split()[0] in e['who'] and n.split()[-1] in e['who']] or evs
    for e in pref[:6]:
        acts.append(f"{e['date']}: {e['what'][:130]}")
    if n in C: role,org,side,al=C[n]
    elif n in PART: role,org,side,al="NDIS participant (witness/complainant/named)","—",P,[]
    elif n in FAM: role,org,side,al="Guardian / nominee / family of participant (witness)","—",PF,[]
    elif n in OTHER_WITNESS: role,org,side,al=OTHER_WITNESS[n] or "Named person","—",'Other',[]
    elif n=="SL (initials only)": role,org,side,al="Initials 'SL' on comment bubbles in tracked-changes draft letter T49 (11 Nov 2022); identity not established in the bundle","NDIS Quality and Safeguards Commission",Cm,[]
    else: role,org,side,al="Named person (role not stated)","—",'Other',[]
    srcs=[14]
    recs.append({"name":n,"aliases":al,"role":role,"organisation":org,"side":side,"key_acts":acts,"first_seen":norm_date(evs[0]['date']),"last_seen":norm_date(evs[-1]['date']),"sources":srcs})
with open('S02_people.jsonl','w',encoding='utf-8') as f:
    for r in recs:
        r['_slice']='S02'; f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(recs))
