#!/bin/bash
cd "$HOME/mnt/NDIS Case/Chronology/_agents/S06_ocr"
name=$1; pdf=$2
mkdir -p $name; pdftoppm -r 150 -gray -png "$pdf" $name/p
for f in $name/p*.png; do tesseract "$f" "${f%.png}" --psm 3 >/dev/null 2>&1; done
cat $(ls $name/p*.txt | sort -V) > $name.txt
echo done >> $name.done
