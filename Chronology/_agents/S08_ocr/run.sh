cd "/sessions/rcw-01r7fbyjdsnajd97xgjdgfht/mnt/NDIS Case/Chronology/_agents/S08_ocr"
D="/sessions/rcw-01r7fbyjdsnajd97xgjdgfht/mnt/NDIS Case/LEGAL_TEAM_SP/EVIDENCE AND DOCUMENTS - Legal Professional Privilege (LPP)/NDIS- ART/Responses from ME"
for f in "4- EMAIL TO DICKINSON" "6- EMAIL FROM DICKINSON" "8- EMAIL TO DICKINSON" "11- email to dickinson and art" "13- email from ART and dickinson" "14- email reply to art" "15- email re orders of ART" "1"; do
  n=$(echo "$f" | cut -d- -f1 | tr -d ' ')
  pdftoppm -r 250 -png "$D/$f.pdf" "p$n" 
  for p in p$n-*.png; do tesseract "$p" "${p%.png}" >/dev/null 2>&1; done
  cat p$n-*.txt > "ocr_$n.txt"
done
echo done > finished.flag
