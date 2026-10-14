#!/bin/bash
# usage: pg.sh id path first last
id=$1; src="$2"; f=$3; l=$4; d=$(mktemp -d)
pdftoppm -r 150 -gray -png -f $f -l $l "$src" $d/p
ls $d/p*.png | xargs -P 2 -I{} sh -c 'tesseract {} {} --psm 3 >/dev/null 2>&1'
out=$(printf "%05d" $id)_p$f-$l.txt
rm -f $out
for t in $(ls $d/p*.png.txt | sort -V); do echo "--- $(basename $t .png.txt) ---" >> $out; cat $t >> $out; done
rm -rf $d; echo done $out
