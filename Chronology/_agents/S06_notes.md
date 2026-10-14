# S06 notes - criminal / investigative strand

## Counts
Events: 111; people: 41 (see S06_events.jsonl / S06_people.jsonl). Helper scripts and header table in _agents (s06*.py, S06_pma_headers.tsv, S06_ocr/).

## Coverage
| ids | what | depth |
|---|---|---|
| 11, 35 | WA Magistrates Court transcript 23 Feb 2024; our analysis memo | read fully |
| 12, 17, 18, 207 | Gmail inbox screenshots (Tom Monks ABF seizure / proceedings stayed) | read; subject lines only, bodies not captured |
| 55, 65 | Vida ABF-stop supplementary affidavit | read: UNSWORN TEMPLATE with placeholders |
| 28, 29, 30 | Property Seizure Record 96 Amethyst Crescent | OCR is upside-down; decoded partly by 180-degree flip; low confidence |
| 205, 216 | Dulloo timeline (7 Jan 2025); audio call transcript 11 Feb 2026 | read fully |
| 62 | ANZ investment statement | corpus empty; p1 OCR'd by S06 only |
| 1205, 1229 | Beckett Annex A, Annex B summary | read fully |
| 1206-1228 | Annex B.1-B.26 | scripted: claim date range, row counts, plan managers, totals only |
| 1230-1235 | Annex C/D/E and C.1/D.1/E.1 | summaries read; C/D/E bank reconstructions only date-range scanned |
| 1236 | Beckett main statement 20 Jun 2023 | corpus text was empty; S06 OCR'd the 42 pages (tesseract 130dpi) to _agents/S06_ocr/r1236.txt and read fully. Corpus 01236.txt should be refreshed from that file |
| Service_2/PMA (all) + 1782 csv | header pass over 511 emails; read ~30 non-invoice emails; keyword scan on all | scripted + targeted reads |
| Service_3/PMAs ProviderChoice (105 REM), PlanPartners (17) | remittance totals by script; PlanPartners case notes read | skimmed |
| 570-572 | Access Foundation invoice PDFs (image-only, near empty) | skipped, no OCR |
| 1237-1241, ManageMode/NDSP/Genesis REMs, Assist REM (36) | remittances | headline dates only |

## Key findings
- NDIA contact with plan managers in this corpus is thin: only the 32 forwards of 16 Dec 2022 (Karen Ruth, Assist -> Sian Harsley, NDIA -> Sean Crampton, NDIA; all Marisha Lombard invoices). Aug 2022 Karen Ruth relays NDIA payment-inquiry outcomes (declined counselling invoices, evidence demanded).
- Nathan Halls (Nathan.Halls2@ndis.gov.au) appears in Vida's 29 Jul 2022 email; the 11 Feb 2026 call transcript spells him 'Holtz' (transcription error likely). 'Karen' on the 2026 call may be Karen Ruth (Assist) - inference only.
- Beckett statement: compliance lock on FFG 3 May 2022; investigator Raymond Holder requested her review; review period 4 Feb 2021 - 3 Oct 2022; she is NDIA Fraud Intelligence and Investigations Branch (Brisbane).
- Property seizure record date reads 19/10/2025 (not 24 Dec 2025 as filename) - verify against image.
- Dulloo timeline: John Maloney named as NDIS investigator (7 Jan 2025) - allegation only, second-hand.
- Annex B charlie harrison subtotal in B.7 file ($68,858.20 incl. $14,989.99 cancelled Hybrid Hive claims) vs summary $53,868.21: summary nets the cancelled claims (Beckett's footnote).
- Beckett Annex A lists Widlake statement 12 Jan 2023 and 23 participant/nominee statements dated 11 Oct 2022 - 16 Feb 2023 (takers not named in Annex A).
- ABF: only a draft/unsworn affidavit template and Gmail screenshots; no ABF document, no seizure notice, no officer name.
- No search warrant, charge sheet date, or return-of-property demand found in slice.

## Gaps
Charge date; police/CDPP officer names beyond Rosaji and Stynes; ABF officers; body text of 28 Sep 2024 Tom Monks email; OCR of 570-572 and ANZ pages 2-16; per-line Annex B/C/D/E data (deliberately not itemised).
