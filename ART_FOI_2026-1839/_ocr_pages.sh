#!/bin/bash
# usage: _ocr_pages.sh "<pdf>" base page...
cd "$(dirname "$0")"
pdf="$1"; base="$2"; shift 2
mkdir -p text_ocr
for n in "$@"; do
  out="text_ocr/${base}__p$(printf '%04d' "$n").txt"
  [ -s "$out" ] && continue
  tmp=$(mktemp -d)
  pdftoppm -r 150 -gray -f "$n" -l "$n" -png "$pdf" "$tmp/pg" 2>/dev/null
  img=$(ls "$tmp"/pg*.png 2>/dev/null | head -1)
  [ -n "$img" ] && tesseract "$img" "${out%.txt}" -l eng --psm 6 >/dev/null 2>&1
  rm -rf "$tmp"
done
