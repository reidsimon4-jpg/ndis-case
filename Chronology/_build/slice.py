import json,collections
M=json.load(open('manifest_dedup.json',encoding='utf-8'))
ocr_ids={62,63,93,121,124,128,131,141,169,181,200,214,236,333,553,562,1236,570,571,572,1696,1698,1700,1701,1702,1706,1708,1710}
U=[r for r in M.values() if (r['status'] not in('duplicate_of','textdup_of','near_empty') and r.get('chars')) or r['id'] in ocr_ids]
EXCL={199,139,72,186,187,137,84}
root=lambda r: r['rel'].startswith('NDIS Case/') and r['rel'].count('/')==1
S={k:[] for k in ['S01','S02','S03','S04','S05','S06','S07','S08','S09','S10']}
S06r={11,12,17,18,28,29,30,55,65,207,35,205,216,62}
S07r={5,6,7,8,9,47,82,52,53,54,120,121,129,209,210,142,143,97,21,22,23,24,25,71,232,125,126,128,93,124,131,169,200,141,111,113,115,63}
S08r={3,4,10,13,15,16,31,32,33,44,45,46,48,56,59,61,95,85,96,103,104,164,165,168,174,184,178,19,20,34,181,333}
S09r={73,127,138,153,226,230,147,66,43,42,99}
S01r={14}; S02r={189,190,191,192,193,194,195,196,197,198}
S04r={74,75,76,77,78}
for r in U:
    i=r['id']; p=r['rel']
    if i in EXCL or 'DUPLICATES' in p: continue
    if p.endswith('.py') or r['ext'] in ('py','sh','ps1','js','ini','skill'): continue
    if i in S01r: S['S01'].append(i); continue
    if i in S02r: S['S02'].append(i); continue
    if root(r):
        for k,s in [('S06',S06r),('S07',S07r),('S08',S08r),('S09',S09r),('S04',S04r)]:
            if i in s: S[k].append(i); break
        else: S['S10'].append(i)
        continue
    if 'AGS_Disclosure_7_May_2026' in p: S['S03'].append(i); continue
    if 'OCR_witness_statements' in p or 'witness_extraction_all' in p: S['S04'].append(i); continue
    if 'TRansfer of files from Bennett' in p or 'Tom Monks- FFG/Roster' in p or 'Meghan Goodwin Rosters' in p or 'Tom Monks- FFG/bank' in p: S['S04'].append(i); continue
    if 'ART_FOI_2026-1839' in p: S['S05'].append(i); continue
    if '/CDPP/' in p or 'pma_emails.csv' in p: S['S06'].append(i); continue
    if 'FOI ATO 2026' in p or 'ART NDIS COMMISSION' in p or ('NDIS- ART' in p and 'Timeline and documents' not in p) or 'Received Emails/ART' in p or '_stage/severance' in p or '_stage/ags_minute' in p or 'Charles- weeks' in p or 'Tom Monks- FFG/AAT' in p: S['S08'].append(i); continue
    if 'Timeline and documents' in p or '/Chronology/' in p or 'review_workings' in p or '14_GMAIL_EVIDENCE_INDEX' in p or '29_post_sunflower' in p: S['S09'].append(i); continue
    if '_file_index.txt' in p or 'source_inventory' in p or 'source_extraction_errors' in p: continue
    S['S10'].append(i)
tot={}
for k,v in S.items():
    ch=sum(M[str(i)].get('chars',0) for i in v)
    print(k,len(v),ch//1000,'k')
    with open(f'slice_{k}.tsv','w',encoding='utf-8') as f:
        for i in sorted(v,key=lambda i:M[str(i)]['rel']):
            r=M[str(i)]; f.write(f"{i:05d}\t{r.get('chars',0)}\t{r['status']}\t{r['mtime']}\t{r['rel']}\n")
assigned=set(sum(S.values(),[]))
left=[r for r in U if r['id'] not in assigned and r['id'] not in EXCL and 'DUPLICATES' not in r['rel']]
print('unassigned',len(left)); [print(' ',r['id'],r['rel'][-90:]) for r in left[:40]]
