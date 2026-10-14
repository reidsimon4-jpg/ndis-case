import sys,os,re
a=int(sys.argv[1]); b=int(sys.argv[2])
D=os.path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S01_ocr')
for i in range(a,b):
    f=f'{D}/p{i:04d}.txt'
    if not os.path.exists(f): print(f'--[idx{i}] none'); continue
    s=open(f,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'[ \t]{2,}',' ',s); s=re.sub(r'\n\s*\n+','\n',s).strip()
    print(f'=====[idx{i} bundle p{i-9}]'); print(s)
