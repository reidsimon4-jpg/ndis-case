import sys,os,re
for a in sys.argv[2:]:
    i=int(a); t=open(os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_corpus/{i:05d}.txt'),encoding='utf-8',errors='ignore').read()
    t=t.split('\n',3)[3] if t.startswith('###') else t
    t=re.sub(r'<https?://[^>]*>','',t); t=re.sub(r'<mailto:[^>]*>','',t); t=re.sub(r'https?://\S+','',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    n=int(sys.argv[1])
    print(f'##### {i}'); print(t[:n])
