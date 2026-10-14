import json,re
ev=[json.loads(l) for l in open('S01_events.bak.jsonl')]
drop=set()
def note(i,t):
    e=ev[i]; n=e.get('notes','')
    if t not in n: e['notes']=(n+' | ' if n else '')+t
# --- fixes to prior records
e=ev[85]; e['who']='Tanya Gukwa (Support Coordinator/Recovery Coach, FFG) - identified from T9.16 pp.417-419'; e['date']='2022-07-01'; e['people']=['Tanya Gukwa','Vida Reid','Janine Hall']; e['confidence']='high'
e['what']='Resignation letter (8:44 AM, 1 Jul 2022) emailed to Vida Reid, cc Jess Goile and Janine H, citing lack of honesty, integrity and structure; one week notice. The Briefing Note T9.4 p.181 refers to it via Janine Hall; the letter itself is at T9.16 p.418 (copy forwarded by Janine to herself).'
note(85,'backstory_link: Vida wrote at 3:08 PM that day that Jan (Nuttall) had been messaging staff to get them to quit (T9.16 p.417-418).')
e=ev[155]; e['date']='2022-06-24'; note(155,'Date corrected from 26 Jun to Fri 24 Jun 2022 4:43 PM per OCR of T9.51. backstory_link (HIGH): Jan Nuttal still at FFG as operations lead on 24 Jun 2022; Vida described her as "previous Operations Manager" on 1 Jul 2022 (T9.52); Danica Hall gives 29 Jun 2022 as Jan departure date (T9.11).')
note(154,'Clulow thanks FFG for support coordination "since November" (2021). Clulow lodged Commission complaint 6 Jul 2022.')
e=ev[162]; e['date']='2022-06-13'; e['time']='17:08'; note(162,'Date corrected from 23 Jun to Mon 13 Jun 2022 17:08 per quoted header "On Mon, 13 Jun 2022 at 17:08, Tori Fitton wrote" (T9.55 p.507).')
e=ev[164]; e['time']='10:11'; e['what']=e['what'].replace('plan expiring 7/8/22','plan expired 7/4/22'); note(164,'Corrected: plan expired 7/4/22 per OCR. Same email also forwarded by Janine to janinehall09@gmail.com at 10:12 AM (T9.14 p.286).')
e=ev[169]; e['what']=e['what'].replace('8:33am','8:39am')
# --- merge my duplicates into granular events
note(160,'Davidson cites NDIA fraud case no. "1A 000 00 31749" [OCR 1A0000031749] for Hahn; Janine Hall quotes 1A0000031700RE on 30 Mar and 18 Apr 2022 - near-consecutive numbers; verify at image level. backstory_link: Davidson is Hahn\'s advocate, not ex-staff.')
note(166,'Predates Janine Hall first NDIA fraud email (30 Mar 2022) by 3 days; Davidson is Hahn\'s advocate, not ex-FFG staff.')
note(168,'Lawyer firm email domain reads dfelegal.com.au (OCR). Janine alleges Vida used lawyers\' letters to threaten Hahn with eviction.')
note(169,'Danica Hall raised the missing service agreement internally on 31 Mar 2022 (supports her T9.11 account); Janine H on cc. Blake Sadler shares surname with Tabatha Sadler (T9.20) - relationship not stated.')
note(165,'backstory_link: records Janine Hall told on 9 May 2022 to stop accessing portals; she later forwarded FFG emails to her Gmail (3 May, 13 Jun, 20 Jun, 1 Jul, 13-14 Jul 2022).')
note(158,'backstory_link (client transfers): "all others have now transferred due to conflict of interest" - reason for conflict not stated.')
note(150,'Simon Reid and Jan Nuttal received this participant complaint on 15 Jun 2022.')
note(153,'Threat to report to NDIS in same email as demand for payment is the document wording.')
note(149,'Footer shows AGS ID "Attachment 41 - FFG $(48789709.1).pdf" print stamp 8/08/2023 - 2023 litigation copy; HelloSign audit date format MM/DD/YYYY (06/07/2022 = 7 June 2022).')
note(250,'')
drop|={254,255,256,257,258,259,260,261,262,263}
# --- fix speculative notes
ev[253]['notes']='Danica Hall appears as the Xero sender on FFG invoice NDIS-1919-1 on 30 Jun 2022 (still employed; her departure per T9.4 is 19 Jul 2022). Eve Adam: "Assist" = Assist Plan Managers (not NurseAssist).'
ev[250]['notes']=ev[250]['notes'].replace('Tanya Gukwa then appears as Janine\'s colleague and co-author? (check Tanya complaint). ','')
# --- 239: merge T9.18 info, drop 130
note(239,'T9.18 (Att 9E, bundle p.420) is another copy of this email; its header shows it was sent from Janine\'s personal Gmail address (OCR "janinehall09@gmail.com") at 3:58 pm AWST on 18 Apr 2022 (a Monday during working hours), subject "FW: Case number 1A0000031700RE", i.e. forwarded from an earlier message. Briefing note labels Att 9E "Sally See FFG Counsellor Screenshot" (mismatch).')
drop|={130}
# --- 143, 146, 144, 145 replaced
drop|={143,144,145,146}
note(70,'Duplicate event 146 merged; see also event for T9.40.')
ev[108]['what']='Commission emailed AFP on 23 Aug 2022 requesting criminal/traffic history extracts for Simon Reid (Att 37) and Vida Reid (Att 40); WA Police Force records compiled 25 Aug 2022 and supplied via AFP (T9.45, T9.48). Content not summarised.'
ev[108]['notes']='Sensitive: records marked not to be disseminated to a third party. Offence details deliberately omitted (brief rule).'
# --- dedupe 176-220
merge={176:6,178:1,179:2,180:4,181:9,182:10,183:11,185:0,186:13,187:15,189:16,190:18,193:21,197:46,199:23,200:24,203:29,204:30,206:31,207:34,210:42,212:43,213:36,214:32,215:33,217:41}
for j,i in merge.items():
    a,b=ev[i],ev[j]
    if len(b['what'])>len(a['what']): a['what']=b['what']
    a['people']=sorted(set(a.get('people',[]))|set(b.get('people',[])))
    for k in ('how','why','to_whom'):
        if (not a.get(k) or a.get(k)=='not stated in source') and b.get(k): a[k]=b[k]
    if b.get('notes'): note(i,b['notes'])
    if b['locator'] not in a['locator']: a['locator']+=' ; '+b['locator']
    drop.add(j)
out=[e for k,e in enumerate(ev) if k not in drop]
open('S01_events.jsonl','w',encoding='utf-8').write('\n'.join(json.dumps(e,ensure_ascii=False) for e in out)+'\n')
print(len(ev),'->',len(out))
