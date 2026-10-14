#!/bin/bash
# usage: S02_ocr2.sh START END (bundle pages)
cd "$HOME/mnt/NDIS Case/Chronology/_agents/S02_ocr"
PDF="$HOME/mnt/NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
for b in $(seq $1 $2); do
  p=$((b+34))
  [ -s "b$b.txt" ] && continue
  pdftoppm -r 200 -gray -png -f $p -l $p "$PDF" /tmp/s02q_$p 2>/dev/null
  f=$(ls /tmp/s02q_$p*.png | head -1)
  tesseract "$f" "b$b" --psm 4 >/dev/null 2>&1
  rm -f /tmp/s02q_$p*.png
done
echo DONE > "done_$1_$2.txt"
