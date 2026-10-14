import csv,io,re,json,os,collections,datetime
p=os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/01373.txt')
t=open(p,encoding='utf-8-sig').read()
i=t.index('First name,Last name')
rows=list(csv.reader(io.StringIO(t[i:])))
hdr=rows[0]; ix={h:k for k,h in enumerate(hdr)}
def pd(s):
    try: return datetime.datetime.strptime(s.strip(),'%d-%b-%y').date()
    except: return None
agg={}
n=0
for r in rows[1:]:
    if len(r)<20 or not r[ix['First name']].strip(): continue
    n+=1
    nm=(r[0].strip()+' '+r[1].strip()).strip()
    a=agg.setdefault(nm,{'name':nm,'term':r[ix['Terminated']],'termdate':r[ix['Termination date']],'type':r[ix['Employee type']],'teams':collections.Counter(),'dates':[],'status':collections.Counter(),'hrs':0.0,'email':r[2]})
    d=pd(r[ix['Start date']])
    if d: a['dates'].append(d)
    a['teams'][r[ix['Team(s)']]]+=1; a['status'][r[ix['Shift status']]]+=1
    try: a['hrs']+=float(r[ix['Total hours excluding breaks (decimal)']] or 0)
    except: pass
print('rows',n,'staff',len(agg))
out=[]
for nm,a in sorted(agg.items()):
    ds=sorted(a['dates'])
    out.append({'name':nm,'first':str(ds[0]) if ds else None,'last':str(ds[-1]) if ds else None,'shifts':len(ds),'hrs':round(a['hrs'],1),'term':a['term'],'termdate':a['termdate'],'type':a['type'],'team':a['teams'].most_common(1)[0][0],'status':dict(a['status'])})
json.dump(out,open('s04_roster_agg.json','w'),indent=0)
for o in out: print(o['name'],o['first'],o['last'],o['shifts'],o['hrs'],o['term'],o['termdate'],o['team'][:25])
