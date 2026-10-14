import re,os,collections,json,sys
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/')
rx=re.compile(r'\|\s*(SC-\d+)?\s*\|\s*(\d{2}/\d{2}/\d{4})\s*\|\s*([^|]*?)\s*\|\s*(\d{2}/\d{2}/\d{4})?\s*\|\s*([^|]*?)\s*\|\s*([\d:]+)\s*\|\s*([^|]*?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*$')
res={}
for i in (74,75,76):
    t=open(B+'%05d.txt'%i,encoding='utf-8',errors='replace').read()
    recs=[]; cur=[]
    for line in t.split('\n'):
        cur.append(line)
        m=rx.search(line)
        if m:
            body='\n'.join(cur); cur=[]
            first=body.split('|')[0].strip()
            recs.append((first,m.groups(),body))
    res[i]=recs
    print(i,len(recs))
    cl=collections.defaultdict(list)
    for first,g,body in recs:
        d=g[1]; cl[first].append((d[6:]+d[3:5]+d[:2],g[2],g[4]))
    for c,v in cl.items():
        v.sort()
        au=collections.Counter(x[1] for x in v)
        print('  ',c,len(v),v[0][0],v[-1][0],au.most_common(6))

print('=========')
def mins(s):
    return int(s.split(":")[0])*60+int(s.split(":")[1]) if ":" in s else 0
for i,recs in res.items():
    print('##',i)
    st=collections.defaultdict(lambda:[0,0,0.0,[]])
    for first,g,body in recs:
        sc,dc,au,dd,ct,du,stt,rate,tot=g
        au=re.sub(r'\s+',' ',au)
        s=st[au]; s[0]+=1; s[1]+=mins(du); s[2]+=float(tot); s[3].append(dc[6:]+dc[3:5]+dc[:2])
    for a,s in sorted(st.items(),key=lambda x:-x[1][0]):
        print(' ',a,s[0],'entries',round(s[1]/60,1),'h $',round(s[2],2),min(s[3]),max(s[3]))
    sts=collections.Counter(g[6] for _,g,_ in recs); print(sts)
    print(collections.Counter(g[4].strip() for _,g,_ in recs).most_common(8), set(g[0] for _,g,_ in recs))
