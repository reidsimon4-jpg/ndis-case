#!/bin/bash
cd "$HOME/mnt/NDIS Case/ART_FOI_2026-1839"
OUT="$HOME/mnt/NDIS Case/Chronology/_agents/S11_ocr"
T=/tmp/s11o; mkdir -p $T
do_one(){ # tag file pages...
  tag="$1"; f="$2"; shift 2
  for p in "$@"; do
    [ -s "$OUT/${tag}_p$p.txt" ] && continue
    pdftoppm -r 200 -gray -png -f $p -l $p "$f" $T/x && img=$(ls $T/x*.png | head -1)
    tesseract "$img" - --psm 4 2>/dev/null > "$OUT/${tag}_p$p.txt"; rm -f $T/x*.png
  done
}
do_one d8 "8 - File notes and internal emails  - 2023.4494.pdf" 1 25 26 29
do_one d7 "7 - External emails to respondent - 2023.4494.pdf" 2 47 71 84 85
do_one d6 "6 - Received administrative documents - 2023.4494.pdf" 7 8 10 12 15 20 27
do_one d5 "5 - Respondent submissions - 2023.4494.pdf" 1 2
do_one d13 "13 - Constitution report.pdf" 3
do_one d15 "15 - Emails from national listings team.pdf" 1 2 3 13 14 15 16 17
do_one d12 "12 - T - documents for case 2023.4494.pdf" 4 5 7 8 26 43 45 46 47 49 $(seq 61 87) $(seq 91 103)
echo DONE > "$OUT/_done"
