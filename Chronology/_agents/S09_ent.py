import re,os,sys
t=open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_corpus/00489.txt'),encoding='utf-8').read()
pos=[m.start() for m in re.finditer(r'^#### \d{4}-\d{2}-\d{2} ',t,re.M)]+[t.find('## Appendix A')]
want=sys.argv[1:]
for i,p in enumerate(pos[:-1]):
    h=t[p:p+30]
    if any(h[5:5+len(w)]==w for w in want):
        print(t[p:pos[i+1]][:int(os.environ.get('MAXC','3500'))]); print('-----')
