#!/bin/bash
# usage: par.sh id "path"
id=$1; src="$2"; d=$(mktemp -d)
pdftoppm -r 150 -gray -png "$src" $d/p
ls $d/p*.png | xargs -P 6 -I{} sh -c 'tesseract {} {} --psm 3 >/dev/null 2>&1'
out=$(printf "%05d" $id)
rm -f $out.txt
for t in $(ls $d/p*.png.txt | sort -V); do echo "--- page $(basename $t .png.txt) ---" >> $out.txt; cat $t >> $out.txt; done
rm -rf $d
echo done $id
