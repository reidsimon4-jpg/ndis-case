#!/bin/bash
# usage: S11_ocr2.sh  (parallel, resumable)
cd "$HOME/mnt/NDIS Case/ART_FOI_2026-1839"
OUT="$HOME/mnt/NDIS Case/Chronology/_agents/S11_ocr"
T=/tmp/s11o; mkdir -p $T
job(){ tag="$1"; f="$2"; p="$3"
  [ -e "$OUT/${tag}_p$p.txt" ] && [ -s "$OUT/${tag}_p$p.txt" ] && exit 0
  [ -e "$OUT/${tag}_p$p.txt" ] && [ "$tag" = d7 ] && [ "$p" = 71 ] && exit 0
  pdftoppm -r 200 -gray -png -f $p -l $p "$f" $T/${tag}_$p && img=$(ls $T/${tag}_$p*.png | head -1)
  tesseract "$img" - --psm 4 2>/dev/null > "$OUT/${tag}_p$p.txt.tmp" && mv "$OUT/${tag}_p$p.txt.tmp" "$OUT/${tag}_p$p.txt"; rm -f $T/${tag}_$p*.png; }
export -f job; export OUT T
{
for p in 84 85; do echo "d7|7 - External emails to respondent - 2023.4494.pdf|$p"; done
for p in 7 8 10 12 15 20 27; do echo "d6|6 - Received administrative documents - 2023.4494.pdf|$p"; done
for p in 1 2; do echo "d5|5 - Respondent submissions - 2023.4494.pdf|$p"; done
echo "d13|13 - Constitution report.pdf|3"
for p in 1 2 3 13 14 15 16 17; do echo "d15|15 - Emails from national listings team.pdf|$p"; done
for p in 4 5 7 8 26 43 45 46 47 49 $(seq 61 87) $(seq 91 103); do echo "d12|12 - T - documents for case 2023.4494.pdf|$p"; done
} | xargs -P 6 -I{} bash -c 'IFS="|" read tag f p <<< "{}"; job "$tag" "$f" "$p"'
