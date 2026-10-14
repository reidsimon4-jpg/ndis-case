#!/bin/bash
cd "$HOME/mnt/NDIS Case/Chronology/_agents/S02_ocr"
PDF="$HOME/mnt/NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
for b in $(seq $1 $2); do
  p=$((b+34))
  [ -s "b$b.txt" ] && continue
  pdftoppm -r 180 -gray -png -f $p -l $p "$PDF" /tmp/s02r_$p 2>/dev/null
  f=$(ls /tmp/s02r_$p*.png | head -1)
  tesseract "$f" "tmp_b$b" --psm 4 >/dev/null 2>&1 && mv "tmp_b$b.txt" "b$b.txt"
  rm -f /tmp/s02r_$p*.png
done
