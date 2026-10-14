import sys,os
d=os.path.expanduser('~/mnt/NDIS Case/Hearing_Prep/OCR_witness_statements/')
f=[x for x in os.listdir(d) if x.startswith(sys.argv[1])][0]
s=open(d+f,encoding='utf-8',errors='replace').read()
a=int(sys.argv[2]) if len(sys.argv)>2 else 0
n=int(sys.argv[3]) if len(sys.argv)>3 else 30000
full = len(sys.argv)>4 and sys.argv[4]=='full'
if not full and a==0:
    i=s.find('witnessed by me')
    if i>0: s=s[:i+700]+'\n[...ANNEXURES TRUNCATED; use offset to read...]'
print(f'[{f} {a}-{a+n} of {len(s)}]'); print(s[a:a+n])
