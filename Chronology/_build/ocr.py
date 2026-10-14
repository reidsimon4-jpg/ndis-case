import json,subprocess,os,tempfile,glob,time,sys
H=os.path.expanduser('~/mnt'); OUT=H+'/NDIS Case/Chronology/_corpus'
R=[json.loads(l) for l in open('manifest.jsonl',encoding='utf-8')]
skipkw=['Statement of','DUPLICATES','Rencana','service agreement signed']
todo=[r for r in R if r['status'].startswith('scanned') and not any(k in r['rel'] for k in skipkw)]
done=set(open('ocr_done.txt').read().split()) if os.path.exists('ocr_done.txt') else set()
for r in todo:
    if str(r['id']) in done: continue
    d=tempfile.mkdtemp()
    subprocess.run(['pdftoppm','-r','150','-gray','-png',r['path'],d+'/p'],timeout=900)
    txt=[]
    for i,img in enumerate(sorted(glob.glob(d+'/p*.png'))):
        o=subprocess.run(['tesseract',img,'-','--psm','3'],capture_output=True,timeout=300).stdout.decode('utf-8','ignore')
        txt.append(f'\n--- page {i+1} ---\n'+o); os.remove(img)
    open(f'{OUT}/{r["id"]:05d}.txt','w',encoding='utf-8').write(f'### SOURCE: {r["rel"]}\n### MTIME: {r["mtime"]}\n### OCR (tesseract 150dpi) - verify against original\n'+''.join(txt))
    open('ocr_done.txt','a').write(f'{r["id"]}\n'); print('done',r['id'],r['rel'][-60:],flush=True)
print('OCR COMPLETE',flush=True)
