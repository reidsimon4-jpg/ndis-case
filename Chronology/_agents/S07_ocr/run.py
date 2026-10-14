import json,subprocess,os,tempfile,glob,sys
H=os.path.expanduser('~/mnt'); 
R={}
for l in open(os.path.expanduser('~/mnt/NDIS Case/Chronology/_build/manifest.jsonl'),encoding='utf-8'):
    r=json.loads(l); R[r['id']]=r
ids=[int(x) for x in sys.argv[1:]]
for i in ids:
    r=R[i]; src=H+'/'+r['rel']
    out=os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_agents/S07_ocr/{i:05d}.txt')
    if os.path.exists(out): continue
    d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-r','150','-gray','-png',src,d+'/p'],timeout=900)
    txt=[]
    for n,img in enumerate(sorted(glob.glob(d+'/p*.png'))):
        o=subprocess.run(['tesseract',img,'-','--psm','3'],capture_output=True,timeout=300).stdout.decode('utf-8','ignore')
        txt.append(f'\n--- page {n+1} ---\n'+o); os.remove(img)
    open(out+'.tmp','w',encoding='utf-8').write(''.join(txt)); os.rename(out+'.tmp',out)
    print('done',i,flush=True)
