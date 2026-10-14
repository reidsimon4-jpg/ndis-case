import os,subprocess,time,sys,tempfile,glob,shutil
from concurrent.futures import ThreadPoolExecutor
H=os.path.expanduser('~/mnt')
PDF=H+'/NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf'
OUT=H+'/NDIS Case/Chronology/_agents/S01_ocr'
l1=[int(x) for x in open(OUT+'/list1.txt').read().split()]
l2=[int(x) for x in open(OUT+'/list2.txt').read().split()]
extra=[429]
order=extra+l1+l2
budget=float(sys.argv[1]) if len(sys.argv)>1 else 140
t0=time.time()
def todo(i):
    f=f'{OUT}/p{i:04d}.txt'
    return not (os.path.exists(f) and os.path.getsize(f)>40)
def one(i):
    if time.time()-t0>budget: return 0
    d=tempfile.mkdtemp()
    try:
        subprocess.run(['pdftoppm','-r','150','-gray','-png','-f',str(i+1),'-l',str(i+1),PDF,d+'/x'],timeout=60)
        img=glob.glob(d+'/x*.png')[0]
        o=subprocess.run(['tesseract',img,'-','--psm','4'],capture_output=True,timeout=90).stdout.decode('utf-8','ignore')
        open(f'{OUT}/p{i:04d}.txt','w',encoding='utf-8').write(o)
        return 1
    finally: shutil.rmtree(d,ignore_errors=True)
pend=[i for i in order if todo(i)]
with ThreadPoolExecutor(2) as ex: n=sum(ex.map(one,pend))
print('done',n,'remaining',len([i for i in order if todo(i)]))
