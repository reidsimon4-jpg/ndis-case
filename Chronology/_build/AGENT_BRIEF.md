# NDIS case master timeline — extraction brief (all agents)

## The matter (orientation only — verify everything from the documents)
Applicants: Simon Reid; Vida Reid (his partner); Forward Focused Group Pty Ltd (FFG, NDIS provider);
related companies Hybrid Hive Pty Ltd, The Hive Pty Ltd, Infinity Living Options Pty Ltd, Malibuhouse Pty Ltd,
Sahar & Simon Pty Ltd. Agencies: NDIA (National Disability Insurance Agency, incl. its fraud/investigations
branch), NDIS Quality and Safeguards Commission ("the Commission"), AGS (Australian Government Solicitor,
acting for the Commission), CDPP, WA Police / WA Magistrates Court, Australian Border Force (ABF), ATO, DEWR,
AAT -> ART (Administrative Review Tribunal) matters 2023/3361 (Vida), 2023/3363 (Simon), 2023/4494 (FFG).
Lawyers for applicants over time: Tom & Co Legal (Tom Monks), DFG Legal, Bennett & Co / Weeks & Co, Charles Weeks,
Hammond Legal. Plan managers, support coordinators, workers, participants and their families appear as witnesses.
Today is 11 Oct 2026.

## Tools
Use ONLY `mcp__remote-devices__device_bash` (it runs on Simon's PC). Corpus = plain-text copy of every file:
  `$HOME/mnt/NDIS Case/Chronology/_corpus/NNNNN.txt` (first line `### SOURCE: <path>`).
Your file list: `$HOME/mnt/NDIS Case/Chronology/_build/slice_SXX.tsv` (cols: id, chars, extract_status, file_mtime_utc, path).
Helpers (run from `$HOME/mnt/NDIS Case/Chronology/_build`):
  - `python3 rd.py ID START LEN` — read text (keep LEN <= 30000 per call)
  - `python3 gr.py "regex" ID [ID ...] --ctx 200` — find matches with char offsets
  - `python3 add.py SXX events` / `python3 add.py SXX people` — append records (one JSON object per line on stdin,
    use a quoted heredoc: `python3 add.py S03 events <<'JSONL'` ... `JSONL`). It validates and rejects bad lines — fix and resend rejects.
  You may write your own short python for bulk/scripted passes (e.g. listing email headers), but never edit or delete
  files outside `_agents/` and never touch the original case files.
Each device_bash call has a 180 s limit — keep commands small.

## What to extract — EVENTS (`add.py SXX events`)
Every dated act or occurrence relevant to the matter: who did what, to/with whom, when, how, why. Go deep — minor
actors matter (investigators, case officers, delegates, AGS lawyers, Commission/NDIA staff, registry staff, Border
Force officers, police, CDPP officers, plan managers, coordinators, workers, participants/family as witnesses,
accountants, lawyers). Include: meetings, phone calls, emails, letters, statements taken, searches/seizures, notices,
decisions, delegations, briefings, internal recommendations, complaints, payments/freezes, filings, hearings,
directions, FOI steps, deadlines (future ones too: status "planned").
Fields (all required unless marked optional):
  date            "YYYY-MM-DD" (or "YYYY-MM" / "YYYY" if that is all the source gives)
  date_precision  day | month | year | approx | range   (use "range" + date_end for periods)
  date_end        optional "YYYY-MM-DD"
  time            optional "HH:MM" (+ timezone if stated)
  who             actor(s): "Full Name (role, organisation)" — as precise as the source allows
  what            the act, concrete and specific (1–2 sentences)
  to_whom         optional recipient/target/affected person
  how             channel/instrument/power: e.g. "email", "letter", "s 73ZN NDIS Act banning order",
                  "s 56 notice", "witness statement taken by phone", "search warrant", "ABF border alert"
  why             stated reason/purpose, ATTRIBUTED ("per briefing note: ...", "Simon contends ...").
                  If not stated: "not stated in source".
  detail          optional, 1–4 sentences: key particulars, numbers, $ amounts, reference numbers (EC22-…, D23-…, INV…)
  quote           optional, <= 40 words verbatim from the source
  category        corporate | operations | complaint | investigation | criminal | border_customs | regulatory_decision |
                  internal_review | tribunal | federal_court | correspondence | foi | ato_tax | evidence |
                  legal_representation | work_product | deadline | other
  status          fact (document itself records it happening) | allegation (someone alleges it) |
                  contention (a party's argument) | simon_position | unverified | planned
  agencies        optional list, e.g. ["NDIA","Commission"]
  people          list of every named person involved in this event
  source_file     path from the slice file
  source_id       corpus id (integer)
  locator         page / para / T-number / email header date — enough to find it fast
  confidence      high | medium | low   (low for OCR-garbled or inferred dates)
  notes           optional: conflicts with other sources, OCR doubts, redactions ("XXXXX")

## PEOPLE (`add.py SXX people`)
One record per distinct person (or unnamed role like "NDIA investigator (redacted)") you encounter:
  name, aliases (optional list), role, organisation,
  side: NDIA | Commission | AGS | CDPP | Police | ABF | ATO | Tribunal | Court | Applicant | Applicant_lawyer |
        Applicant_staff | Participant | Participant_family | Provider | Plan_manager | Accountant | Other
  key_acts (list of short strings with dates), first_seen ("YYYY-MM-DD"), last_seen, sources (list of ids)

## Rules
1. NO FABRICATION. Every record must come from a document in your slice; cite it. If unsure, mark confidence low
   or status unverified. Never invent dates, names, numbers. Redacted names stay redacted.
2. Separate fact from allegation from contention — a witness statement asserting misconduct is "allegation";
   a decision recording a finding is "fact" that the finding was made (put the finding in `what`).
3. Our own work-product (Claude drafts, memos, strategy notes) is NOT evidence: record only (a) the dated work-product
   milestone itself (category work_product, note whether it was ever sent/filed) and (b) external events it reports,
   with status "unverified" unless you can see the primary document in your slice.
4. Privacy: participants' health/disability details — record only what is needed for the event (e.g. "participant
   gave statement re FFG services"), no diagnoses.
5. Write as you go: append after every 1–3 documents. Do not hold findings in memory — your context may be compacted.
6. Quality over speed, but cover your WHOLE slice. If you must triage, say what you skipped and why.
7. When done, write `_agents/SXX_notes.md` via python (coverage table: ids done / skimmed / skipped; key conflicts;
   gaps) and reply to the orchestrator in <= 250 words: counts of events/people, coverage, top 10 most significant
   events, conflicts found.

## Added 11 Oct 2026
- Corpus id 14 (13 Jun 2024 finalised tender bundle) has ~795 image-only pages with no text layer. OCR of the image-only pages
  OUTSIDE T10–T43 is being produced at `_corpus/00014_imagepages_OCR.txt` (read with `python3 rd.py 00014_imagepages_OCR.txt START LEN`;
  pages are headed "=== PDF page N (Tx) [OCR] ==="). If it is not there yet, do your text pages first and check again at the end.
- Redaction finding: the 13 Jun 2024 bundle shows UNREDACTED material that was blacked out in the 2023 T-docs: T9.11 = Danica Hall
  statement; T9.14–T9.17 = Janine Hall information 18.07.22; T9.20 = Tabatha Sadler email 17.07.22 to Cade Brown (Commission);
  T9.21 = Sarah-Jane Clulow complaint 06.07.22; T9.22 = Jan Nuttall complaint 11.08.22. Record who supplied what to whom and when.
- Agents S03, S06, S07 have already finished (AGS disclosure; criminal/CDPP; 2020–23 regulatory record). Don't duplicate their
  slices; if you see their documents cited, a short cross-reference event is fine.

## Simon's stated backstory (11 Oct 2026) — record as status "simon_position" only; look for documentary evidence FOR or AGAINST it
- Janine Hall, Danica Hall (and a third Hall — possibly Brodie Hall, FFG staff, resigned 6 May 2022) are family members.
- Terri Roberts, Elanor Smith and Jan Nuttall left/were fired shortly before the complaints. Terri was a director of Infinity Living
  Options Pty Ltd (Simon and Vida shareholders); she and Vida were friends, it ended in lawsuits; Simon says she was offered money by
  competitor NurseAssist 24/7 and took FFG clients there. FFG and NurseAssist had a joint company and fell out over a support worker.
- Simon says Nathan Halls (NDIA) and Vida had prior history; Terri and Elanor orchestrated the complaints; investigators led witnesses.
FLAG with notes "backstory_link": dates people left FFG vs dates of their complaints/statements; who referred whom (e.g. Tabatha Sadler
says Elanor Smith asked her to provide information); NurseAssist / Nurse Assist 24/7 mentions; client transfers to NurseAssist;
Terri Roberts' roles; repeated or templated wording across witness statements; any lawsuits between Roberts/Vida/FFG/ILO.
