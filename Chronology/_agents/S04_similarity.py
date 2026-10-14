import re,os,glob,collections,itertools,json,sys
D=os.path.expanduser('~/mnt/NDIS Case/Hearing_Prep/OCR_witness_statements/')
OUT=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S04_statement_similarity.md')
K=8
files=sorted(glob.glob(D+'*.txt'))
def short(f):
    n=os.path.basename(f)[:-4]
    n=re.sub(r' \d{1,2}Oct$','',n)
    if 'Terri Roberts' in n: n='Terri Roberts '+re.search(r'(\d+)Oct',os.path.basename(f)).group(1)+'Oct'
    return n
TAKERS=[('Fiona Lane',r'F[il1]ona\s+LANE'),('James Lane',r'James\s+LANE'),('Brenda Ryan',r'Brenda\s+Ryan'),('Tim Jarratt',r'Tim\s+JAR|JARRATT|Jarratt'),
 ('Christine Bruckner',r'Bruckner'),('Gerard Righetti',r'Righetti'),('Sian Harsley',r'Sian\s+Hars'),('Amanda Laing',r'Amanda\s+La[il]'),('Bruce Graydon',r'GRAYDON|Graydon')]
MONTHS='January|February|March|April|May|June|July|August|September|October|November|December'
def split(t):
    m=re.search(r'(?i)witnessed\s+by\s+me',t)
    body=t[:m.start()] if m else t
    jur=t[m.start()-80:m.start()+500] if m else ''
    return body,jur
HDR=[r'Statement in the matter of R v Vida R[eE][iI]D\s+Page \d+ of \d+',r'Statement of [^\n]{3,60}continued\s*:?',r'^\s*Signature\s*$',r'^\s*Witness\s*$',r'^\s*Signature Witness\s*$']
def clean(b):
    for h in HDR: b=re.sub(h,' ',b,flags=re.M|re.I)
    return b
def words(b):
    b=b.replace('|',' I ').replace('’',"'")
    b=re.sub(r"[^A-Za-z0-9' ]+",' ',b).lower()
    b=b.replace("'",'')
    return b.split()
S={}
for f in files:
    t=open(f,encoding='utf-8',errors='replace').read()
    body,jur=split(t)
    n=short(f)
    S[n]=dict(file=os.path.basename(f),text=t,body=body,jur=jur,w=words(clean(body)))
names=sorted(S)
def shingles(w): return [tuple(w[i:i+K]) for i in range(len(w)-K+1)]
for n in names:
    S[n]['sh']=shingles(S[n]['w']); S[n]['shs']=set(S[n]['sh'])
df=collections.Counter()
for n in names:
    for s in S[n]['shs']: df[s]+=1
N=len(names)
BP=int(sys.argv[1]) if len(sys.argv)>1 else 12
boiler={s for s,c in df.items() if c>=BP}
def runs(w,idxs):
    idxs=sorted(idxs); out=[]; 
    if not idxs: return out
    a=b=idxs[0]
    for i in idxs[1:]:
        if i==b+1: b=i
        else: out.append((a,b)); a=b=i
    out.append((a,b))
    return [(' '.join(w[a:b+K]),b-a+K) for a,b in out]

BPN=10
boiler={x for x,c in df.items() if c>=BPN}
def runs_(w,idxs):
    idxs=sorted(idxs); out=[]
    if not idxs: return out
    a=b=idxs[0]
    for i in idxs[1:]:
        if i==b+1: b=i
        else: out.append((a,b)); a=b=i
    out.append((a,b))
    return [(' '.join(w[a:b+K]),b-a+K) for a,b in out]
bp_runs=collections.Counter()
for n in names:
    idx=[i for i,x in enumerate(S[n]['sh']) if x in boiler]
    for txt,l in runs_(S[n]['w'],idx): bp_runs[txt]+=1
# ---- metadata
def meta(n):
    d=S[n]; t=d['text']; jur=re.sub(r'\s+',' ',d['jur'])
    hd=re.search(r'Date\s+\W{0,3}(\d{1,2}\s*(?:th|st|nd|rd)?\s*(?:%s)\s+\d{4})'%MONTHS,re.sub(r'\s+',' ',t[:900]))
    hdate=hd.group(1) if hd else ''
    jm=re.search(r'about\s*(.{0,22}?)\s*on\s+(\d{1,2}\s+(?:%s)\s+\d{4})\s+at\s+(.{0,60}?)\s+in\s+(?:Western|Wes)'%MONTHS,jur) 
    tm=jm.group(1).strip() if jm else ''; jd=jm.group(2) if jm else ''; pl=jm.group(3).strip() if jm else ''
    tk=''
    after=jur[jur.lower().find('witnessed by me'):][:400] if 'witnessed by me' in jur.lower() else jur
    if 'Insert name of Investigator' in after: tk='[BLANK TEMPLATE: "Insert name of Investigator (insert location)"]'
    else:
        best=None
        for nm,rx in TAKERS:
            mm=re.search(rx,after[:330],re.I)
            if mm and (best is None or mm.start()<best[0]): best=(mm.start(),nm)
        if best: tk=best[1]
    paras=re.findall(r'(?m)^\s*(\d{1,2})\.\s+(.+?)(?=^\s*\d{1,2}\.\s|\Z)',clean(d['body']),flags=re.S)
    ann=bool(re.search(r'(?i)annexure|annex',t[len(d['body']):]))
    return dict(hdate=hdate,jdate=jd,time=tm,place=pl,taker=tk,paras=paras,ann=ann)
M={n:meta(n) for n in names}
# ---- pairs
nb={n:[(i,x) for i,x in enumerate(S[n]['sh']) if x not in boiler] for n in names}
nbset={n:{x for _,x in nb[n]} for n in names}
pairs=[]
for a,b in itertools.combinations(names,2):
    sh=nbset[a]&nbset[b]
    if not sh: pairs.append((a,b,0,0,0,[]));continue
    idxa=[i for i,x in nb[a] if x in sh]
    rs=runs_(S[a]['w'],idxa)
    cont=len(sh)/max(1,min(len(nbset[a]),len(nbset[b])))
    jac=len(sh)/len(nbset[a]|nbset[b])
    pairs.append((a,b,len(sh),cont,jac,sorted(rs,key=lambda r:-r[1])))
pairs.sort(key=lambda p:-p[2])
# ---- shared by >=3 statements (non boiler)
df2=collections.Counter()
for n in names:
    for x in nbset[n]: df2[x]+=1
multi={x for x,c in df2.items() if c>=3}
mruns=collections.defaultdict(set)
for n in names:
    idx=[i for i,x in nb[n] if x in multi]
    for txt,l in runs_(S[n]['w'],idx): mruns[txt].add(n)
# ---- structure
op=collections.defaultdict(set)
for n in names:
    for num,pt in M[n]['paras']:
        w=words(pt)[:6]
        if len(w)>=4: op[' '.join(w)].add(n)
# ---- output
L=[]
A=L.append
A('# S04 Part 1b - witness statement templating test\n')
A('Generated by `_agents/S04_similarity.py` (8-word shingles over statement body text only: from heading to the taker/jurat line; annexures, attached invoices/service agreements and the 11-Oct annexure copied into Terri Roberts 18Oct are excluded; page headers/footers stripped). Source files: `Hearing_Prep/OCR_witness_statements/*.txt` (35 files, OCR - names/spellings may be garbled; Janine Hall file omits some statement pages).\n')
A('## 1. Boilerplate identified (excluded from overlap scores)\nShingles present in >= %d of %d statements. These are the Commonwealth statement template (heading block, para 1, paras 2-3 identity/address lines, and the jurat/declaration):\n'%(BPN,N))
for t,c in bp_runs.most_common(12):
    if len(t.split())>=12: A('- (%dx) `%s`'%(c,t[:330]))
A('\nTemplate skeleton common to all statements: "Statement Sensitive / Statement in the matter of R v Vida Reid / Name / Occupation / Address Known to NDIS / Date / STATES: / 1. This statement made by me accurately sets out the evidence that I would be prepared, if necessary, to give in court as a witness. / 2. My full name is ... / 3. My residential address is known to the NDIS ... / [narrative] / This statement is true to the best of my knowledge and belief ... / Statement taken and signature witnessed by me about [time] on [date] at [place] in Western Australia."\nThis is the standard Commonwealth/NDIA form and is expected in every statement; it is NOT evidence of leading.\n')
A('## 2. Per-statement particulars (taker, date, time, place)\n')
A('| Statement (file) | Header date | Jurat date | Time | Place | Taker (per OCR jurat) | Words (body) | Numbered paras | Annexures in file |')
A('|---|---|---|---|---|---|---|---|---|')
for n in names:
    m=M[n]; A('| %s | %s | %s | %s | %s | %s | %d | %d | %s |'%(n,m['hdate'],m['jdate'],m['time'],m['place'],m['taker'],len(S[n]['w']),len(m['paras']),'yes' if m['ann'] else 'no'))
A('')
# per day
byday=collections.defaultdict(list)
for n in names: byday[M[n]['jdate'] or M[n]['hdate'] or '?'].append(n)
def dkey(d):
    mm=re.match(r'(\d+)\s+(\w+)\s+(\d{4})',d); 
    if not mm: return (9999,0,0)
    mo=MONTHS.split('|').index(mm.group(2))+1 if mm.group(2) in MONTHS else 0
    return (int(mm.group(3)),mo,int(mm.group(1)))
A('## 3. Statements per day\n')
A('| Date taken (jurat) | Count | Statements |'); A('|---|---|---|')
for d in sorted(byday,key=dkey): A('| %s | %d | %s |'%(d,len(byday[d]),'; '.join(byday[d])))
A('')
bt=collections.defaultdict(list)
for n in names: bt[M[n]['taker'] or '?'].append(n)
A('## 4. Statements per taker (investigator named in jurat)\n')
A('| Taker | Count | Statements (date/time/place) |'); A('|---|---|---|')
for k,v in sorted(bt.items(),key=lambda x:-len(x[1])): A('| %s | %d | %s |'%(k,len(v),'; '.join('%s (%s %s, %s)'%(x,M[x]['jdate'][:6].strip(),M[x]['time'],M[x]['place']) for x in sorted(v,key=lambda x:(dkey(M[x]['jdate']),M[x]['time'])))))
A('')
A('## 5. Pairs with highest verbatim overlap (non-boilerplate 8-word shingles)\n')
A('Containment = shared shingles / shingles in the shorter statement (non-boilerplate). Jaccard = shared / union.\n')
A('| Rank | Statement A | Statement B | Shared 8-grams | Containment | Jaccard | Same taker? | Longest shared passages (words) |'); A('|---|---|---|---|---|---|---|---|')
for r,(a,b,c,ct,jc,rs) in enumerate(pairs[:30],1):
    same='yes' if M[a]['taker'] and M[a]['taker']==M[b]['taker'] else 'no'
    ps=' || '.join('"%s" (%d)'%(t[:160],l) for t,l in rs[:3])
    A('| %d | %s | %s | %d | %.1f%% | %.1f%% | %s | %s |'%(r,a,b,c,ct*100,jc*100,same,ps))
A('')
# same vs different taker
same=[p for p in pairs if M[p[0]]['taker'] and M[p[0]]['taker']==M[p[1]]['taker'] and not M[p[0]]['taker'].startswith('[')]
diff=[p for p in pairs if not(M[p[0]]['taker'] and M[p[0]]['taker']==M[p[1]]['taker'])]
import statistics as st
A('## 6. Same-taker vs different-taker overlap\n')
A('- Pairs sharing a taker: %d; mean shared 8-grams %.1f; mean containment %.2f%%; pairs with zero shared non-boilerplate 8-grams: %d'%(len(same),st.mean(p[2] for p in same),100*st.mean(p[3] for p in same),sum(1 for p in same if p[2]==0)))
A('- Pairs with different takers: %d; mean shared 8-grams %.1f; mean containment %.2f%%; zero-overlap pairs: %d'%(len(diff),st.mean(p[2] for p in diff),100*st.mean(p[3] for p in diff),sum(1 for p in diff if p[2]==0)))
allp=[p for p in pairs]
A('- All %d pairs: %d have zero shared non-boilerplate 8-grams; %d have >=5; %d have >=20.\n'%(len(allp),sum(1 for p in allp if p[2]==0),sum(1 for p in allp if p[2]>=5),sum(1 for p in allp if p[2]>=20)))

# ---- within-taker table and per-statement templated fraction
A('## 6b. Overlap within each taker group (mean shared 8-grams over pairs; max)\n')
A('| Taker | Statements | Pairs | Mean shared 8-grams | Max | Notes |'); A('|---|---|---|---|---|---|')
pm={(p[0],p[1]):p for p in pairs}
for k,v in sorted(bt.items(),key=lambda x:-len(x[1])):
    if len(v)<2 or k.startswith('['): continue
    ps=[pm.get((a,b)) or pm.get((b,a)) for a,b in itertools.combinations(sorted(v),2)]
    A('| %s | %d | %d | %.1f | %d | |'%(k,len(v),len(ps),st.mean(p[2] for p in ps),max(p[2] for p in ps)))
A('')
A('## 6c. Per-statement share of body text that is verbatim-shared (8-grams in at least one other statement, boilerplate excluded)\n')
A('| Statement | Taker | Non-boilerplate 8-grams | Shared with >=1 other | % shared |'); A('|---|---|---|---|---|')
rows=[]
for n in names:
    tot=len(nbset[n]); sh=sum(1 for x in nbset[n] if df2[x]>=2)
    rows.append((100*sh/max(1,tot),n,tot,sh))
for pc,n,tot,sh in sorted(rows,reverse=True): A('| %s | %s | %d | %d | %.1f%% |'%(n,M[n]['taker'][:22],tot,sh,pc))
A('')
A('## 7. Passages shared (non-boilerplate) by 3 or more statements\n')
ml=sorted(mruns.items(),key=lambda x:(-len(x[1]),-len(x[0])))
for t,ns in ml[:40]:
    if len(t.split())>=K: A('- (%d stmts: %s) "%s"'%(len(ns),', '.join(sorted(ns)),t[:260]))
A('')
A('## 8. Paragraph-opening structure (first 6 words of numbered paragraphs recurring across statements)\n')
A('| Opening | # statements | Which |'); A('|---|---|---|')
for k,v in sorted(op.items(),key=lambda x:-len(x[1]))[:40]:
    if len(v)>=4: A('| %s | %d | %s |'%(k,len(v),', '.join(sorted(v))))
A('')
open(OUT,'w',encoding='utf-8').write('\n'.join(L))
print('written',len(L))
