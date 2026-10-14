import json,subprocess,os,sys
B=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build')
F={}
for l in open(B+'/slice_S07.tsv'):
    p=l.rstrip('\n').split('\t'); F[int(p[0])]=p[4]
def ev(sid,rows):
    out=[]
    for r in rows:
        d=dict(date_precision='day',confidence='high',status='fact')
        d.update(r); d['source_id']=sid; d['source_file']=F[sid]
        d.setdefault('how','not stated'); d.setdefault('why','not stated in source')
        out.append(json.dumps(d,ensure_ascii=False))
    run('events',out)
def pe(rows):
    out=[]
    for r in rows:
        d=dict(); d.update(r); out.append(json.dumps(d,ensure_ascii=False))
    run('people',out)
def run(k,out):
    r=subprocess.run(['python3',B+'/add.py','S07',k],input='\n'.join(out)+'\n',capture_output=True,text=True,cwd=B)
    print(r.stdout,r.stderr)
