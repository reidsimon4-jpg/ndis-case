import os,re,json,collections
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/')
rows=[]
for l in open(B+'_build/slice_S04.tsv',encoding='utf-8'):
    p=l.rstrip('\n').split('\t')
    if len(p)>=5 and p[0].isdigit() and 'CLIENTS/' in p[4]: rows.append((int(p[0]),p[4]))
KW={'nurseassist':r'nurse\s*-?assist|nurseassist|nurse assist 24','terri':r'\bterri\b|\broberts\b','commission':r'\bNDIS Commission|Quality and Safeguards|\bQSC\b|safeguards commission','fraud':r'\bfraud','investig':r'investigat','police':r'\bpolice\b|\bWAPOL\b','complaint':r'complain','cease':r'\bceas(e|ed|ing)\b|terminat|discontinu|\bexit(ed)? (the )?(service|ffg)|withdraw(n|ing)? from ffg|cancel(led)? (the |their |his |her )?service','transfer':r'transfer(red|ring)? to|moved? (over )?to (another|a different|new) provider|change(d)? provider|changing provider|new provider|other provider|leaving ffg|leave ffg|left ffg','freeze':r'\bfroz|freez|locked (the )?(funds|plan)|funds? (were )?(blocked|locked)|plan (was )?blocked','ndiaagent':r'\bNDIA\b.*(audit|review of provider)|provider audit|\baudit\b','hall':r'\bhalls?\b','lawyer':r'lawyer|solicitor|legal|court'}
hits=collections.defaultdict(list)
cnt=collections.Counter()
for i,rel in rows:
    c=rel.split('CLIENTS/')[1].split('/')[1]
    t=open(B+'_corpus/%05d.txt'%i,encoding='utf-8',errors='replace').read()
    for k,rx in KW.items():
        for m in re.finditer(rx,t,flags=re.I):
            cnt[k]+=1
            if k in ('nurseassist','commission','fraud','investig','police','freeze','cease','transfer','terri'):
                s=max(0,m.start()-160); e=min(len(t),m.end()+200)
                hits[k].append((c,i,m.start(),re.sub(r'\s+',' ',t[s:e])))
print(cnt)
json.dump(hits,open('s04kw.json','w'))
for k in ('nurseassist','commission','freeze'):
    print('=====',k,len(hits[k]))
    for h in hits[k][:25]: print(h[0],h[1],h[2],'|',h[3][:360])
