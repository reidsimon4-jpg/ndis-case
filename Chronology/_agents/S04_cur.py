# usage: python3 S04_cur.py <<EOF  lines: name|role|organisation|side|aliases(;)  -> appends to S04_curated.txt
import sys,os
f=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S04_curated.txt')
with open(f,'a',encoding='utf-8') as o:
    for l in sys.stdin:
        l=l.strip()
        if l: o.write(l+'\n')
