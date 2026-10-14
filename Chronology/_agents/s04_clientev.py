import pickle,json,re,collections,os
E=pickle.load(open('s04_entries.pkl','rb'))
J=json.load(open('s04_clients2.json'))
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
SF={}
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit(): SF[int(p[0])]=p[4]
W={'Amber Wilson':'Amber Wilson (statement 12 Oct 2022, Bruckner)','Jamie Wilson':'child of witness Amber Wilson (statement 12 Oct 2022)','Amy Crane':'Amy Crane (statement 13 Oct 2022, Ryan)','Andrew Hahn':'Andrew David Hahn (statement 14 Oct 2022, Righetti)','Angela Cutler':'Angela Cutler (statement 18 Oct 2022, Lane)','Barry Macdonald':'Barry MacDonald (statement 11 Oct 2022, Righetti)','Bassam Haidar':'Bassam Abau Haidar (statement 14 Oct 2022, Jarratt)','Hayden Tranthem':'Hayden Trantham (statement 13 Oct 2022, Jarratt)','Hrmnir Benediktsson':'Hrimnir Benediktsson (statement 12 Oct 2022, Righetti)','Jonathan Shapiera':'Jonathan Shapiera (statement 12 Oct 2022, Jarratt)','Levi Jetoh':'son of witnesses Monbo and Jerusha Jetoh (statements 13 Oct 2022, Bruckner)','Benjamin Dines':'son of witness Joy Pickering (statement 13 Oct 2022, Righetti)','Charlie Harrison':'daughter of witness Jessica Smith (statement 14 Oct 2022, Laing)','Miah Williams':'daughter of witness Marish Cimafranca (statement 14 Oct 2022, Bruckner)','Janine Craig':'daughter of witness Merina Craig (statement 14 Oct 2022, Lane)','Georgios Taraganis':'son of witness Liz Odi (statement 11 Oct 2022, Jarratt)','Angelus Regali-Park':'son of witness Gina Regali (statement 11 Oct 2022, J. Lane)','Indiana Regali-Park':'son of witness Gina Regali (statement 11 Oct 2022, J. Lane)','Max Teague':'son of witness Rhiannon Teague (statement 11 Oct 2022, F. Lane)','Meghan Goodwin':'Meghan Goodwin (statement 12 Oct 2022, Ryan)','Marisha Lombard':'Marisha Lombard (statement 20 Oct 2022, Bruckner)','Paul Gilbert':'Paul Gilbert (statement 13 Oct 2022, Laing)','Sarah-Jane Clulow':'Sarah-Jane Clulow (statement 11 Oct 2022, Ryan)','Sarah-Jane Hammond':'Sarah-Jane Hammond (statement 18 Oct 2022, Bruckner)','Bekki Mulock':'possibly related to witness Lisa Mulock (statement 17 Oct 2022, J. Lane) - relationship not verified','Alexander Boyd':'file name in some PDFs reads AlexanderReid (surname Reid); Roberts and Danica Hall describe Vida Reid\'s son Alexander Reid - identity not verified'}
by=collections.defaultdict(list)
for e in E: by[e[0]].append(e)
out=[]
for c in J:
    cl=c['client']; es=sorted(by[cl],key=lambda e:e[2])
    if not es: continue
    au=collections.Counter(e[3] for e in es)
    top=', '.join('%s (%d)'%(a.title().strip(),n) for a,n in au.most_common(4))
    terri=[e for e in es if e[3]=='terri roberts']
    na=sum(1 for e in es if re.search(r'nurse\s*assist',e[4],re.I))
    first,last=es[0][2],es[-1][2]
    notes=[]
    if cl in W: notes.append('Participant/relative is a witness: '+W[cl]+'.')
    if terri: notes.append('Terri Roberts authored %d entries (%s to %s).'%(len(terri),terri[0][2],terri[-1][2]))
    if na: notes.append('Nurse Assist 24/7 mentioned in %d entries.'%na)
    first_id=c['ids'][0]
    hdr=c['hdr']
    o=dict(d=first,dp='day',de=last,who='Forward Focused Group (FFG) staff - main note authors: '+top,what='FFG case-note record for participant %s spans %s to %s: %d dated entries across %d Case Note Report file(s) in the Bennett & Co transferred client folder.'%(cl,first,last,len(es),len(c['ids'])),how='Careview Case Note Reports (PDF) transferred from Bennett & Co legal',why='not stated in source',cat='operations',st='fact',id=first_id,loc='client folder %s; corpus ids %s'%(cl,','.join(map(str,c['ids']))),conf='medium',ppl=[cl]+[a.title() for a,n in au.most_common(4)])
    o['detail']='Interval = first and last dated entry parsed by script (approximate; entries without a parsable header line are not counted). Report header ranges: %s.'%'; '.join('%s - %s'%(h[0],h[1]) for h in hdr[:6])
    if notes: o['notes']=' '.join(notes)
    out.append(o)
with open('/tmp/s04_clientev.jsonl','w',encoding='utf-8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
print(len(out))
