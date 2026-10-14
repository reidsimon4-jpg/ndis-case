# S07 notes - primary regulatory record 2020-2023

Events: 150; people: 44. (see S07_events.jsonl / S07_people.jsonl)

## Coverage
| ids | status |
|---|---|
| 5 (Simon banning order + SoR, ref EC22-002521 / D23 41713) | done fully |
| 54 (briefing note D23 41712 / EC22-002521) | done fully |
| 6 (EC22-002103 Project Archer brief) | done fully |
| 52 (EC22-002429 correspondence brief) | done fully |
| 53 (ART directions 8 Sep 2025) | done |
| 7 (NDIA Notice of Compliance Lock 5 May 2022, plus Claude analysis header) | done; header = work product |
| 8 (Swiss Re Stage 2 IDR 13 Feb 2023) | done |
| 9 (Tom & Co FFG s100 submission 20 Mar 2023) | done |
| 142 (FFG s100 decision 8 Jun 2023, D-number n/a) ; 97 text duplicate | done; 97 = duplicate (99.9% word overlap) |
| 143 (Simon s100 decision D23 56430, 21 Apr 2023) | done |
| 125 (Vida s100 decision 21 Apr 2023); 126 text duplicate | done; 126 = duplicate |
| 129 (Vida banning order notice 20 Dec 2022); 209 text duplicate; 210 garbage PDF-structure text (no content) | done; 209 dup, 210 unreadable |
| 120 (Hybrid Hive banning order 21 Dec 2022, EC22-002431) | done fully |
| 47 (DEWR letter 30 Jun 2023); 82 text duplicate | done; 82 dup |
| 71 (Brief for Hammond Legal) | done (applicant narrative, status contention/allegation) |
| 232 (Shapiera email 14 Oct 2022) | done |
| 111, 113, 115 (FFG invoice statements to 14 Dec 2021: Trinca, Brown, Germon) | done |
| 21-25 ("Notice of Banning Order Simon Reid" OCR versions) | done: ALL are The Hive Pty Ltd order (s 73ZN(2A), 5 y), NOT Simon's personal order; id 24 = full; 21,22,23,25 = partial page ranges |
| 141 ("Notice of Banning Order- Simon Reid.pdf", scanned) | OCR'd by S07 into _agents/S07_ocr/00141.txt: same content as id 24 (The Hive order) |
| 93, 124, 131, 169, 200, 121 ("Full Document" ASIC-named PDFs; 121 "Hybrid banning orders") | OCR'd by S07 (pages 1-2 + last page; 93 whole): they are NOT ASIC extracts; they are the Commission 17 Nov 2022 notices of intention to EFS, Infinity, Malibuhouse, Sahar & Simon, The Hive, Hybrid Hive (ref EC22-002103). Corporate facts (ACN, registration date, officeholders) taken from them |
| 128 (letter to Nathan Halls 11 Oct 2022) | OCR'd by S07 (corpus file was near-empty; _agents/S07_ocr/00128.txt) - it is a Bennett (litigation law firm) letter, not Tom & Co |
| 63 (Simon affidavit) | OCR'd by S07 (_agents/S07_ocr/00063_p1-3.txt): affidavit in AAI Limited v FFG (insurance premium), WA Magistrates Court; not an NDIS-case affidavit; date illegible |

Note: corpus files for ids 63,93,121,124,128,131,141,169,200 were still ~empty when checked (central OCR had not produced output); S07 OCR'd them itself with tesseract 150dpi into _agents/S07_ocr/ (corpus untouched). Lower confidence for those.

## Key conflicts / discrepancies
1. Date of Tom & Co last letter to Commission: 7 Dec 2022 (SoR id 5, Leathem id 143) vs 8 Dec 2022 (briefing note id 54 para 10.4).
2. Simon's directorship of Hybrid Hive: Commission notices/SoR/briefs (ids 5,6,54,120,121,200) say sole director and shareholder, Hybrid registered 17 Jun 2021, Simon director "since 17 Feb 2022" (co-director with Vida to 22/23 Aug 2022). Leathem id 143 says co-director 17 Feb-21 Aug 2022, sole from 22 Aug 2022; id 125 says Vida was sole director 1 Dec 2021-16 Feb 2022 then co-director to 21 Aug 2022 - implies Simon not a director before 17 Feb 2022 despite statement he is "sole director and shareholder". Check ASIC.
3. Simon/Vida FFG directorships: Vida co-director 28 Aug 2020-3 Jan 2021, sole director 4 Jan 2021-20 Oct 2022, co-director 21 Oct-1 Nov 2022 (id 142, 125); Simon co-director 28 Aug 2020-3 Jan 2021 and again from 1 Nov 2022 (id 142,143). Id 129 SoR: Vida director "until November 2022". Id 124 notice: Vida "sole director of FFG since 28 Aug 2020". Simon's own 30 Jun 2023 letter to DEWR (id 47) calls him "sole Director" of FFG.
4. Decision/ref numbers: Simon's order notice refs EC22-002521 (briefing note PDR) though filename says D23 41713; Hybrid Hive order and The Hive order notices both bear ref EC22-002431.
5. Civil penalty amounts: $220,000 (21 Dec 2022 notices), $222,000 (Vida 20 Dec 2022 notice), $275,000 (Apr 2023 decisions), $1,375,000 for corporation (FFG Jun 2023).
6. Submission period: briefing EC22-002429 says notice gave 13 days then 14 days; Simon notice deadline 30 Nov 2022 (13 days from 17 Nov); Leathem records Monks complaint of 12 days; extension of 14 days from original due date to 14 Dec 2022 granted 2 Dec 2022 after submissions already lodged.
7. EFS: brief id 6 says sole director Vida Reid; notice id 93 says director Rejaul Alam, secretary Vida Reid. Sahar & Simon: brief says Simon secretary; notice says Simon director/shareholder. Malibuhouse: brief says Alam shareholder only; notice says Alam director too.
8. Leathem's reviews narrowed/removed several matters (Simon not FFG director during Clulow period; SoFM Hybrid portion $78,491.06 of Goodwin sum not attributed to FFG decision; $1,485,527 expired-plan figure given minimal weight per NDIA Tactical Intelligence Report 18 Aug 2022). Vida's order basis changed to suitability (s 73ZN(2)(a)(iii)); Simon's scope broadened due to Dream Big Employment Pty Ltd (ASIC application 29 Oct 2022) and Vitality WA Pty Ltd (email 9 Feb 2023), Burke statement 16 Feb 2023.
9. Original briefing note recorded Vida's bail conditions; SoR for Simon removed bail references.
10. Compliance lock: notice only says "manual assessment"; later total non-payment per plan manager 4 Oct 2022 and Bennett letter 11 Oct 2022; NDIA (Lundgren, 6 Oct 2022) denied directing Assist to cease all payments (quoted in id 128; and id 7 analysis).
11. Hammond brief (id 71): Vida's charges "dropped 28 Feb 2024, dismissed for want of prosecution" - applicant narrative, unverified here.

## Gaps
- Primary documents referred to but not in slice: 17 Nov 2022 notice of intention to Simon (Attachment H), 2 Dec 2022 letter, Tom & Co 22/30 Nov and 7 Dec 2022 letters, FFG 19 Oct 2022 notices, EC22-002000/002581 briefs, FFG revocation decision 20 Dec 2022, statements of Regali, Benediktsson, Smith, Clulow, Goodwin, Burke, NDIA SoFM 19 Oct 2022, NDIA Tactical Intelligence Report 18 Aug 2022.
- Date of Simon's AAI affidavit (id 63) not legible.
- No actual ASIC extracts in this slice (the "Full Document" PDFs are Commission notices).
- Pages 3-12 of ids 124,131,169,200,121 not OCR'd (they repeat the same allegations as id 93).
