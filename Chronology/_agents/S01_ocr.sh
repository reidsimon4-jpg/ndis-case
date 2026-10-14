#!/bin/bash
PDF="$HOME/mnt/NDIS Case/20240613 Tender Bundle [Finalised] 23004627.pdf"
OUT="$HOME/mnt/NDIS Case/Chronology/_agents/S01_ocr"
do1(){ i=$1; pn=$((i+1)); f="$OUT/p$(printf %04d $i).txt"; [ -s "$f" ] && return; d=$(mktemp -d); pdftoppm -r 170 -gray -png -f $pn -l $pn "$PDF" $d/x; tesseract $d/x*.png - --psm 4 > "$f" 2>/dev/null; rm -rf $d; }
export -f do1; export PDF OUT
# order: garbled/other small first, then T9.14-17
for i in 173 175 177 431 443 444 445 447 448 449 450 465 466 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 490 491 492 493 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 519 520 521 522 523 524 525; do echo $i; done > "$OUT/list1.txt"
seq 254 428 > "$OUT/list2.txt"
cat "$OUT/list1.txt" "$OUT/list2.txt" | xargs -P 3 -I{} bash -c 'do1 {}'
echo ALLDONE > "$OUT/DONE"
