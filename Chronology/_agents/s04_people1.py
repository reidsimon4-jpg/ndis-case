import json,subprocess,os
W=[ # name, role, org, side, id, date, act
("Terri Susan Roberts","Former FFG support coordinator; witness (two statements)","FFG (former)","Applicant_staff",[545,546],"2022-10-11","Statements 11 and 18 Oct 2022 (bundle T10) re FFG support coordination"),
("Sarah-Jane Elizabeth Clulow","NDIS participant; witness","—","Participant",[543],"2022-10-11","Statement 11 Oct 2022 taken by Brenda Ryan"),
("Rhiannon Teague","Parent/nominee of participant Max Teague; witness","—","Participant_family",[542],"2022-10-11","Statement 11 Oct 2022 taken by Fiona Lane"),
("Pieter Nicolaas Rossouw","Witness (other)","—","Other",[541,545],"2022-10-11","Statement 11 Oct 2022"),
("Liz Odi","NDIS participant and nominee/guardian of Georgios Taraganis; witness","—","Participant_family",[534],"2022-10-11","Statement 11 Oct 2022 at Yanchep; disputes FFG invoice 0378 ($12,590.16) and others"),
("Leah Norman","Purchasing Officer; former FFG support coordinator; witness","FFG (former)","Applicant_staff",[532],"2022-10-11","Statement 11 Oct 2022 taken by Gerard Righetti"),
("Hayden Michael Trantham","NDIS participant; witness","—","Participant",[524],"2022-10-13","Statement 13 Oct 2022 taken by Tim Jarratt, Rockingham"),
("Barry Ross MacDonald","Retired; NDIS participant; witness","—","Participant",[518],"2022-10-11","Statement 11 Oct 2022 taken by Gerard Righetti"),
("Meghan Erica Goodwin","NDIS participant; witness","—","Participant",[537],"2022-10-12","Statement 12 Oct 2022 taken by Brenda Ryan with support person Tabatha Sadler"),
("Jonathan Charles Shapiera","NDIS participant; witness","—","Participant",[529,521],"2022-10-12","Statement 12 Oct 2022 (Project ARCHER heading); positive about FFG/HH; terminated Access services 1 Dec 2022 per Burke"),
("Janine Ruth Hall","Former FFG Service Manager/support coordinator; witness","FFG (former)","Applicant_staff",[526],"2022-10-15","Statement 15 Oct 2022 taken by James Lane"),
("Danica Rochelle Hall","FFG Accounts Officer Dec 2021 - 25 Jul 2022; witness","FFG (former)","Applicant_staff",[522],"2022-10-14","Statement 14 Oct 2022; alleges false/backdated invoicing under Rejaul Alam and Vida Reid"),
("Candice Yavarzadeh-Tehrani","Parent/nominee of participant Ziah O'Reilly; witness","—","Participant_family",[520],"2022-10-12","Statement 12 Oct 2022 taken by Fiona Lane"),
("Amber Wilson","Participant and nominee of her children; witness","—","Participant",[514],"2022-10-12","Statement 12 Oct 2022 taken by Christine Bruckner"),
("Alexsis Carla Bott","Practice manager; NDIS participant; witness","—","Participant",[513],"2022-10-12","Statement 12 Oct 2022 taken by Fiona Lane; says FFG never visited"),
("Paul Gilbert","NDIS participant; witness","—","Participant",[540],"2022-10-13","Statement 13 Oct 2022 taken by Amanda Laing"),
("Monbo Steven Jetoh","Nominee for son Levi Jetoh; witness","—","Participant_family",[539],"2022-10-13","Statement 13 Oct 2022 taken by Christine Bruckner"),
("Joy Valerie Pickering","Host family; nominee for Benjamin Dines; witness","—","Participant_family",[530],"2022-10-13","Statement 13 Oct 2022 taken by Gerard Righetti"),
("Jerusha Jetoh","Carer; nominee for son Levi Jetoh; witness","—","Participant_family",[527],"2022-10-13","Statement 13 Oct 2022 taken by Christine Bruckner"),
("Hrimnir Benediktsson","NDIS participant; witness","—","Participant",[525],"2022-10-12","Statement 12 Oct 2022 taken by Gerard Righetti"),
("Amy Janet Crane","NDIS participant; witness","—","Participant",[515],"2022-10-13","Statement 13 Oct 2022 taken by Brenda Ryan"),
("Merina Craig","Carer, mother and nominee of participant Janine Craig; witness","—","Participant_family",[538],"2022-10-14","Statement 14 Oct 2022 taken by Fiona Lane"),
("Marish Cimafranca","Carer; mother of participant Miah Williams; witness","—","Participant_family",[535],"2022-10-14","Statement 14 Oct 2022 taken by Christine Bruckner"),
("Jessica Rose Smith","Mother; plan nominee for Charlie Harrison; witness","—","Participant_family",[528],"2022-10-14","Statement 14 Oct 2022 taken by Amanda Laing, Jurien Bay"),
("Gina Regali","Carer; mother of participants Angelus and Indiana Regali-Park; witness","—","Participant_family",[523],"2022-10-11","Statement 11 Oct 2022 taken by James Lane"),
("Bassam Abau Haidar","Retiree; NDIS participant; witness","—","Participant",[519],"2022-10-14","Statement 14 Oct 2022 taken by Tim Jarratt"),
("Andrew David Hahn","Utility operator; NDIS participant (Safety Bay SIL); witness","—","Participant",[516],"2022-10-14","Statement 14 Oct 2022 taken by Gerard Righetti"),
("Lisa Mulock","Clinical nurse specialist; mother/nominee of participant Bekki Mulock; witness","—","Participant_family",[533],"2022-10-17","Statement 17 Oct 2022 taken by James Lane"),
("Karen Ruth Canalija Marasigan","Head of Compliance, Zettai Pty Ltd t/as Assist Plan Managers; witness","Assist Plan Managers","Plan_manager",[531],"2022-10-17","Statement 17 Oct 2022 taken by Sian Harsley"),
("Yvonne Charlotte-May Harrison","NDIS participant; witness","—","Participant",[547],"2022-10-18","Statement 18 Oct 2022 taken by Christine Bruckner; terminated FFG/Hive 29 Aug 2022"),
("Sarah-Jane Hammond","Tax consultant; NDIS participant; witness","—","Participant",[544],"2022-10-18","Statement 18 Oct 2022 taken by Christine Bruckner"),
("Angela Cutler","Participant; witness","—","Participant",[517],"2022-10-18","Statement 18 Oct 2022 taken by Fiona Lane"),
("Marisha Lombard","Medical receptionist; NDIS participant; witness","—","Participant",[536],"2022-10-20","Statement 20 Oct 2022 taken by Christine Bruckner"),
("Cassandra Lee Burke","Support Coordinator, Access Disability Services; former FFG support coordinator (Jun/Jul-Oct 2022); witness","Access Disability Services","Other",[521],"2023-02-16","Statement 16 Feb 2023 (bundle T60); alleges staff laptop recalls 30 Sep 2022, Vida editing staff emails, Dream Big approach 1 Dec 2022"),
]
INV=[
("Tim Jarratt","NDIS Fraud Investigator","NDIA","NDIA",[529,534,524,519],"Took statements of Shapiera (12 Oct), Odi (11 Oct), Trantham (13 Oct), Haidar (14 Oct) 2022"),
("Christine Bruckner","Fraud Investigator (Perth)","NDIA","NDIA",[514,527,535,536,539,544,547],"Took 7 statements 12-20 Oct 2022"),
("Gerard Righetti","Assistant Director, Fraud Investigations (Perth)","NDIA","NDIA",[516,518,522,525,530,532],"Took 6 statements 11-14 Oct 2022 incl. Danica Hall"),
("Fiona Lane","Senior Investigator (Perth)","NDIA","NDIA",[513,517,520,538,542,546],"Took 6 statements 11-18 Oct 2022; distinct from James Lane"),
("James Lane","NDIS Investigator (Cannington/Armadale/Golden Bay per OCR)","NDIA","NDIA",[523,526,533],"Took statements of Gina Regali, Janine Hall, Lisa Mulock"),
("Brenda Ryan","NDIS Fraud Investigator (Rockingham)","NDIA","NDIA",[515,537,543],"Took statements of Crane, Goodwin, Clulow"),
("Sian Harsley","NDIS Investigator (name per OCR)","NDIA","NDIA",[531,545],"Took statements of Marasigan and Roberts (11 Oct)"),
("Amanda Laing","NDIS Fraud Taskforce (Rockingham/Jurien Bay)","NDIA","NDIA",[528,540],"Took statements of Jessica Smith and Paul Gilbert"),
("Bruce Graydon","NDIS Fraud Investigator","NDIA","NDIA",[521],"Took Cassandra Burke statement 16 Feb 2023 at Jull Street, Perth"),
("Narelle Richardson","NDIA Investigator","NDIA","NDIA",[521],"Visited Access Disability Services with Graydon 16 Feb 2023"),
("Nathan Halls","NDIA officer contacted by Burke re Shapiera plan and Dream Big","NDIA","NDIA",[521],"Per Burke, spoke with her about Shapiera being agency-managed and received her report of Dream Big; also 'Andrew Halls' named by Vida at 4 Oct 2022 staff meeting (name per Burke)"),
]
OTH=[
("Vida Reid","Director/CEO of FFG and Hybrid Hive; accused (R v Vida Reid)","Forward Focused Group; Hybrid Hive","Applicant",[513,515,521,522,534,547],"Subject of all witness statements; alleged to direct invoicing, cruise promotion, laptop recall 30 Sep 2022 and Dream Big approach"),
("Simon Reid","Co-owner of FFG (per witnesses); recovery coach role alleged; Hive contact","Forward Focused Group; Hybrid Hive","Applicant",[515,518,522,529,547],"Named by witnesses as co-owner/contact; met Yvonne Harrison at cafe Nov 2021"),
("Rejaul Alam","FFG/Hive Accounts Manager (Oct 2021), financial partner Dec 2021, CFO Jan-Feb 2022; setting up Exact Financial Solutions","FFG/The Hive","Applicant_staff",[522,517,519],"Per Danica Hall, sent invoices without service evidence at Vida's direction"),
("Virginie Fanny-Dulloo","FFG then Hive Accounts Officer","FFG/The Hive","Applicant_staff",[522,521,531],"Trained Hall in invoicing; present at 1 Dec 2022 Vida approach to Burke"),
("Blake Sadler","FFG coordinator/staff; to run 'Dream Big' per Shapiera","FFG","Applicant_staff",[521,516,523,524,529],"Locked Burke out of Care View 25 Oct 2022"),
("Sally See","FFG counsellor/recovery coach; resigned 5 Apr 2022","FFG","Applicant_staff",[522,523,526,547],"Name appears on invoices after departure per witnesses"),
("Honey Nguyen","FFG staff","FFG","Applicant_staff",[514,519,524,533,547],"Sent 16 Feb 2022 'thank you for attending' cruise email per Harrison"),
("Chloe Osborne","Named across several statements","FFG","Applicant_staff",[515,520,527,528],"See individual statements"),
("Paul Ugwunali","Director, Access Disability Services","Access Disability Services","Other",[521],"Took on Burke and clients 25 Oct 2022"),
("Ahmad","Perth Health and Care Services; signed PHCS service agreement with Odi 25 Oct 2021","Perth Health and Care Services","Provider",[534],"Provided support workers for Georgios per Vida's arrangement"),
("Emily King","Plan manager contact, Provider Choice Management","Provider Choice Management","Plan_manager",[534],"Sent Odi FFG invoices"),
("Joshua Davidson","Advocate for Andrew Hahn","—","Other",[522],"Requested evidence of support worker services"),
]
rows=[]
for n,r,o,s,ids,d,a in W:
    rows.append(dict(name=n,role=r,organisation=o,side=s,key_acts=[f"{d} {a}"],first_seen=d,last_seen=d,sources=ids))
for n,r,o,s,ids,a in INV:
    rows.append(dict(name=n,role=r,organisation=o,side=s,key_acts=[a],first_seen="2022-10-11",last_seen="2023-02-16" if 521 in ids else "2022-10-20",sources=ids))
for n,r,o,s,ids,a in OTH:
    rows.append(dict(name=n,role=r,organisation=o,side=s,key_acts=[a],sources=ids))
p=subprocess.run(['python3',os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/add.py'),'S04','people'],input='\n'.join(json.dumps(x,ensure_ascii=False) for x in rows),text=True,capture_output=True)
print(p.stdout,p.stderr)
