# usage: python3 S08_w.py events|people  < jsonl ; fills source_file from source_id
import sys,json,csv,os,subprocess
b=os.path.expanduser('~/mnt/NDIS Case/Chronology/_build')
m={}
for r in csv.reader(open(b+'/slice_S08.tsv',encoding='utf-8'),delimiter='\t'):
    m[int(r[0])]=r[4]
out=[]
for l in sys.stdin:
    l=l.strip()
    if not l: continue
    try: o=json.loads(l)
    except Exception as e:
        print('BAD JSON',e,l[:100]); continue
    if sys.argv[1]=='events':
        sid=int(o.get('source_id',0)); o.setdefault('source_file',m.get(sid,'?'))
        if o['source_file']=='?' : o['source_file']=m.get(sid,'?')
        o.setdefault('confidence','high')
    out.append(json.dumps(o,ensure_ascii=False))
p=subprocess.run(['python3',b+'/add.py','S08',sys.argv[1]],input='\n'.join(out)+'\n',text=True,capture_output=True,cwd=b)
print(p.stdout,p.stderr)
