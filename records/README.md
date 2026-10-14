# records/

`documents.jsonl`: one JSON line per PDF, email (.eml) and Outlook message (.msg) in the repo. Rebuild with `python3 build/make_document_records.py`.

## Fields
- `path`: location in the repo (the original file is at this path, unchanged).
- `sha256`, `bytes`: identify the exact file. `duplicate_of` is set when the same bytes appear at another path.
- `file_modified_utc`: filesystem timestamp. Not reliable as a document date.
- `text_path`, `text_chars`, `text_status`: where the extracted text is (`00_TEXT/`). `ok` = has a text layer; `empty_or_scanned` = needs OCR; `not_extracted` = PDF could not be read; `not_parsed` = .msg (no parser run yet).
- `first_text_line`: first non-trivial line of extracted text. A hint only, not a title.
- `date_guess` + `date_source`: a date found in the filename (`filename`), in the email header (`header`), or in the text (`text`). A text date is a date that *appears* in the document, not necessarily its date. Check before relying on it.
- Emails: `from`, `to`, `cc`, `subject`, `date_header`, `attachments` (names only; attachments are not extracted yet).

## Hand check (8 random records, before scaling)
- Email headers and dates: correct on every sample.
- PDF `first_text_line`: often noise (screen prints, "ANNEXURE B.2"). Treated as a hint, not a title.
- PDF `date_guess` from text: one sample was a date inside the document, so the field is unreliable for documents without a date in the filename.
- 69 PDFs have no text layer and need OCR. 2 PDFs could not be read at all.
- 96 records are byte-identical duplicates of another file.
- All 108 .msg files still need a parser.

## Not yet done
- Summaries, document types, parties and case references: these need reading and are the next step, in batches with a hand check.
- OCR for the 69 scanned PDFs.
- Parsing the 108 .msg files.
