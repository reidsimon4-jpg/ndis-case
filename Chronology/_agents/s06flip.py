import sys,os
i=int(sys.argv[1])
t=open(os.path.expanduser(f'~/mnt/NDIS Case/Chronology/_corpus/{i:05d}.txt'),encoding='utf-8',errors='ignore').read()
a="abcdefghijklmnopqrstuvwxyz"
mp={'a':'ɐ','b':'q','c':'ɔ','d':'p','e':'ǝ','f':'ɟ','g':'ƃ','h':'ɥ','i':'ᴉ','j':'ɾ','k':'ʞ','l':'l','m':'ɯ','n':'u','o':'o','p':'d','q':'b','r':'ɹ','s':'s','t':'ʇ','u':'n','v':'ʌ','w':'ʍ','x':'x','y':'ʎ','z':'z'}
# Observed OCR: flipped letters appear as other letters: build simple flip: reverse string and map letters
fm={'a':'e','e':'a'}
# simple: rotate180 maps for ocr output chars
r={'A':'V','V':'A','M':'W','W':'M','N':'N','Z':'Z','S':'S','H':'H','I':'I','O':'O','X':'X','0':'0','b':'q','q':'b','d':'p','p':'d','n':'u','u':'n','u':'n','m':'w','w':'m','a':'e','e':'a','h':'y','y':'h','6':'9','9':'6','!':'i','i':'!','L':'L','7':'L','t':'t'}
lines=t.split('\n')
out=[]
for l in reversed(lines):
    out.append(''.join(r.get(c,c) for c in reversed(l)))
print('\n'.join(out))
