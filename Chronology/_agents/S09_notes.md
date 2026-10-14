# S09 notes - correspondence digests and compiled chronologies

Output: S09_events.jsonl (889 events, dates 2020-08-28 to 2027-12-22), S09_people.jsonl (181 people).
Status mix: fact 606, unverified 151, simon_position 72, planned 30, allegation 25, contention 5.
Events citing the digests: id 489 = 316, id 127 = 74, id 66 = 58, id 445 = 51, id 230 = 47. Project docs and memory files (source_id 0, cited project:/memory:) = 130.

## Coverage table (slice ids)
| id | what | coverage |
|---|---|---|
| 489 | Gmail AGS/ART digest, 365 entries | DONE. 316 events; the remaining entries are duplicates/auto-acks/out-of-office. Digest times are UTC, so some events fall a day earlier/later than local (Perth/Sydney) date |
| 127 | Key Gmail excerpts | DONE for the main parts; excerpts 19, 23, 41, 49, 64 only lightly mined (SKIMMED) |
| 66, 42, 43, 99, 1718, 1759, 445 | schedules and compiled chronologies | DONE (66: 58 events; 43: 23; 445: 51; 42 is the earlier v1 of the schedule in 43, covered via 43) |
| 230, 1715, 226, 153, 138, 73, 147 | correspondence / chronologies | DONE in an earlier run; depth for 138, 153, 73, 147 not re-spot-checked (SKIMMED on review) |
| 443 | SQL create-table schema | SKIPPED (no events) |
| 444 | SQL insert of the 65-event chronology | DONE; compared by date with S09 events, one row (2022-03-24 Harrison invoices) was missing and has been added |
| 486, 487, 488, 490 | review_workings analyses | DONE as dated work-product milestones/external events only (24, 20, 17 events from 487/488/486); 490 is a prior-review summary, no events beyond the work-product milestone |
| project docs (7) | claude.ai Project | READ: direction_2_oct timetable, foi_2026_1839 review, research duty-to-state, filing v4/v5/v6, defence_theme_admin_errors; the redactions tender-bundle check was also read. All read-only |
| memory files | /projects/01a0a467.../ | READ: all except reference_email_stores/supabase/index (read, locations only), memory-notes, user_simon_reid (background). 130 events from project/memory sources, all status fact (work-product milestone) or unverified (external events they report) |

## SFIC lodgement (specific ask)
- Simon's Statement of Facts, Issues and Contentions was filed by Tom & Co on 15 Jul 2024 (digest id 489; also id 230 and id 445 'Simon's SFIC filed'). Same day Tom sent Simon draft SFIC Rev4 for urgent comment and Simon disputed draft para 64 and asked to quote the Commission's 'Where there is smoke there is fire' line.
- Due date was 10 Jul 2024 (17 Jun 2024 amended direction), so 5 days late. AGS 16 Jul acknowledged it; 23 Jul and 31 Jul 2024 AGS told the Tribunal Simon's SFIC was filed late and that nothing was filed for Vida (3361) or FFG (4494).
- The Respondent's SFIC in Simon's matter was moved from 17 Jul to 6 Aug 2024 (not opposed); no Respondent SFIC was ever filed (AGS 31 Jul 2024 said it had not prepared SFICs for Vida/FFG).
- 'Dated 15 Jul 2024' and lodgement date agree; no source suggests a different lodgement date.

## backstory_link items (34 events flagged; see note field)
- Terri Roberts: FFG daily report 11 Aug 2021 (id 127); Simon says she was director of Infinity Living Options and a friend of Vida; Simon says she, Elanor Smith and Jan Nuttall were fired before the investigation and that Roberts and Smith orchestrated the complaints (simon-case-positions memory, Oct 2026). Roberts later appears as Commission witness / Nurse Assist 24/7 adviser (role list). Unverified HR dates.
- Jan Nuttall: fired 29 Jun 2022 per Danica Hall statement (T9.11), complaint to NDIA 11 Aug 2022 (T9.22), 43 days later; Halls to Mangion email 12 Aug 2022 on the Nuttall follow-up. Source is a Hall-family statement, not an HR record.
- Elanor Smith: Tabatha Sadler's 17 Jul 2022 email to Commission officer Cade Brown (Meghan Goodwin) says Smith asked her to provide information (T9.20, Att 10; redactions in the 13 Jun 2024 tender bundle).
- Hall family: Janine Hall info of 18 Jul 2022 (T9.14-T9.17); Danica Hall statement (T9.11); Brodie Hall resigned 6 May 2022 (corpus ids 14/189, outside slice). Redacted T-docs T9.04, 9.09, 9.11, 9.14, 9.20, 9.23, T44 cited in AGS 17 Sep 2025.
- NurseAssist: Amanda Damon / Terri Roberts, Nurse Assist 24/7; Diversitas WA (Sukhi Tear) installed 16 Aug 2022 'at the request of the agency'; Tear call to Shapiera 30 Sep 2022 saying she knew Nathan Halls.
- Nathan Halls: 38 events, from the 2021 cooperative emails (Simon to Halls 26 Aug 2021) through Feb 2022 fraud framing, 11-12 Aug 2022 tip-off call and Mangion email, 29 Sep 2022 'coordinated provider exit', 4 Oct 2022 payment stop.

## Key conflicts and discrepancies
1. Vitality: id 66 contains a correction on Vitality WA that differs from earlier characterisation; memory: Vitality WA reg 29 Oct 2022 (same day as Dream Big per source) with domains 8 Feb 2023. Treat as unresolved.
2. Tori Fitton / Tori Vince: same person under both names (FFG director resigned ~June 2023); ATO memo uses 'Tori Vince'.
3. ABF stop date Sep 2024: 25 Sep vs 26/27 Sep depending on source (digest times UTC).
4. Stay application date: 11 Oct 2023 vs about 31 Oct 2023.
5. Compliance Lock: applied 3 May 2022, notified 5 May 2022 (plead both).
6. Rejaul Alam removed from PRODA: 6 Oct 2022 vs 1 Nov 2022 vs 'removed ~7 May 2022'; SMF paras 19-20 show re-nomination 30 May to 4 Oct 2022.
7. FFG internal review decision: 8 Jun vs 9 Jun 2023; FFG ban expiry 20 vs 21 Dec 2025; original FFG order 20 vs 21 Dec 2022; AGS reference 23001627 vs 23004627.
8. Vida's varied order: Apr 2023 (variation effective 22 Apr 2023) vs file named 'Internal Review Vida 2025-03-06'.
9. ART bundle: redactions in tender bundle versus Craig Land's 'unredacted' claim (id 66 / redactions check doc).
10. 'Counter-minute filed' note (filing set 17 Aug) versus 'nothing filed since 14 Aug 2026' (filing_set_v2); treated as NOT filed.
11. 'Dec'21 FFG SGC unpaid' etc. are Claude-memory figures; ATO numbers are unverified secondary.
12. Entity bans: five entity PDFs are 17 Nov 2022 PROPOSED-order notices, not final orders. Earlier memory 'entity orders to Dec 2032' is an unverified inference and has been recorded only as proposed.
13. Dream Big / Burke statement: statement dated 16 Feb 2023 omitted from tender bundle (id 66) vs taken by Graydon/Richardson 16 Feb 2023.
14. Germon email: memory text dated 26 Aug 2021 (corrected from a typo during extraction).

## Gaps / suggestions
- ids 138, 153, 73, 147 and Key Gmail excerpts 19, 23, 41, 49, 64 were read in an earlier run and not re-verified.
- All project/memory-derived events are secondary: Federal s 39B lodgement status unconfirmed; ATO items unverified; KC strategy and GPT/Grok reviews are work product.
- Planned 2026 deadlines captured: 2 Oct 2026 directions; 23 Oct 2026 Respondent supplementary tender bundle; listing after 6 Nov 2026; ATO IR 30 Sep; Jun'22 SGC amendment window to ~27 Feb 2027; bans expire Dec 2027.
