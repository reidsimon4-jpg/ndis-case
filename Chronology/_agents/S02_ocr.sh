#!/bin/bash
cd "$HOME/mnt/NDIS Case/Chronology/_agents/S02_ocr"
PDF="$HOME/mnt/NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
for p in $(seq 1343 1506); do
  b=$((p-34))
  [ -f "b$b.txt" ] && continue
  pdftoppm -r 200 -gray -png -f $p -l $p "$PDF" /tmp/s02p_$p 2>/dev/null
  f=$(ls /tmp/s02p_$p*.png | head -1)
  tesseract "$f" "b$b" --psm 4 >/dev/null 2>&1
  rm -f /tmp/s02p_$p*.png
done
echo DONE > ocr_finished.txt
