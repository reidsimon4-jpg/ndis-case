#!/bin/bash
# OCR every page that has no text layer, for the FOI PDFs
cd "$(dirname "$0")"
LOG=text_ocr/_progress.log
: > "$LOG"
ocr_page() {
  pdf="$1"; n="$2"; base="$3"
  out="text_ocr/${base}__p$(printf '%04d' "$n").txt"
  [ -s "$out" ] && return
  tmp=$(mktemp -d)
  pdftoppm -r 170 -gray -f "$n" -l "$n" -png "$pdf" "$tmp/pg" 2>/dev/null
  img=$(ls "$tmp"/pg*.png 2>/dev/null | head -1)
  if [ -n "$img" ]; then tesseract "$img" "${out%.txt}" -l eng --psm 6 >/dev/null 2>&1; fi
  rm -rf "$tmp"
  echo "$base p$n" >> text_ocr/_progress.log
}
export -f ocr_page
for pdf in "11 - T-documents for case 2023.3361.pdf" "4 - File notes and internal emails – 2023.3361.pdf" "2 - Received administrative documents – 2023.3361.pdf" "3 - External emails to respondent – 2023.3361.pdf" "15 - Emails from national listings team.pdf" "12 - T - documents for case 2023.4494.pdf" "8 - File notes and internal emails  - 2023.4494.pdf" "6 - Received administrative documents - 2023.4494.pdf" "7 - External emails to respondent - 2023.4494.pdf"; do
  base=$(echo "$pdf" | sed 's/\.pdf$//' | tr ' ' '_' | tr -cd 'A-Za-z0-9_.-')
  txt="text/${pdf%.pdf}.txt"
  # list pages whose text layer is nearly empty
  python3 - "$txt" > "text_ocr/_${base}_pages.lst" <<'PY'
import sys
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read().split('\f')
for i,p in enumerate(t,1):
    if len(p.strip())<80 and i<=len(t)-1: print(i)
PY
  cat "text_ocr/_${base}_pages.lst" | xargs -P 4 -I{} bash -c 'ocr_page "$@"' _ "$pdf" {} "$base"
done
echo DONE >> "$LOG"
