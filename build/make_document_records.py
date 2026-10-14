#!/usr/bin/env python3
"""Build records/documents.jsonl: one line per PDF and email in the case repo.

Deterministic fields only (no interpretation): path, checksum, size, dates
found in the filename or text, extracted-text location, and email headers.
Run from repo root:  python3 build/make_document_records.py
"""
import email, hashlib, json, os, re, datetime
from email import policy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "00_TEXT", "00_INDEX", "records", "build"}
MONTHS = {m: i for i, m in enumerate(
    ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"], 1)}
RE_ISO = re.compile(r"(?<!\d)(20\d{2})[-_.]?(0[1-9]|1[0-2])[-_.]?(0[1-9]|[12]\d|3[01])(?!\d)")
RE_DMY = re.compile(r"(?<!\d)(\d{1,2})\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?,?\s+(20\d{2})", re.I)
RE_MY = re.compile(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?,?\s+(20\d{2})\b", re.I)

def guess_date(s):
    m = RE_ISO.search(s)
    if m:
        y, mo, d = map(int, m.groups())
        try: return datetime.date(y, mo, d).isoformat()
        except ValueError: pass
    m = RE_DMY.search(s)
    if m:
        d, mon, y = m.groups()
        try: return datetime.date(int(y), MONTHS[mon[:3].lower()], int(d)).isoformat()
        except ValueError: pass
    m = RE_MY.search(s)
    if m:
        mon, y = m.groups()
        return f"{y}-{MONTHS[mon[:3].lower()]:02d}"
    return None

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def first_line(text):
    for line in text.splitlines():
        t = line.strip()
        if len(t) > 3:
            return t[:160]
    return None

def body_text(msg):
    part = msg.get_body(preferencelist=("plain", "html"))
    if part is None:
        return "", None
    content = part.get_content()
    if part.get_content_type() == "text/html":
        content = re.sub(r"<[^>]+>", " ", content)
        content = re.sub(r"\s+", " ", content)
        return content, "html-stripped"
    return content, "plain"

def walk():
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in SKIP and not (Path(dp) == ROOT and d.startswith("."))]
        for fn in fns:
            p = Path(dp) / fn
            if p.suffix.lower() in (".pdf", ".eml", ".msg"):
                yield p

def main():
    recs, sums = [], {}
    for p in sorted(walk(), key=lambda x: str(x).lower()):
        rel = p.relative_to(ROOT).as_posix()
        kind = p.suffix.lower()[1:]
        st = p.stat()
        digest = sha256(p)
        rec = {
            "path": rel,
            "kind": kind,
            "bytes": st.st_size,
            "sha256": digest,
            "file_modified_utc": datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "folder": rel.split("/")[0] if "/" in rel else "(root)",
        }
        if digest in sums:
            rec["duplicate_of"] = sums[digest]
        else:
            sums[digest] = rel

        if kind == "pdf":
            tp = ROOT / "00_TEXT" / (rel + ".txt")
            text = tp.read_text(errors="replace") if tp.exists() else ""
            rec.update({
                "text_path": f"00_TEXT/{rel}.txt" if tp.exists() else None,
                "text_chars": len(text.strip()),
                "text_status": ("ok" if len(text.strip()) > 50 else "empty_or_scanned") if tp.exists() else "not_extracted",
                "first_text_line": first_line(text),
            })
            d = guess_date(p.name)
            src = "filename" if d else None
            if not d:
                d = guess_date(text[:3000]); src = "text" if d else None
            rec["date_guess"], rec["date_source"] = d, src

        elif kind == "eml":
            try:
                msg = email.message_from_bytes(p.read_bytes(), policy=policy.default)
                body, fmt = body_text(msg)
                tp = ROOT / "00_TEXT" / (rel + ".txt")
                tp.parent.mkdir(parents=True, exist_ok=True)
                tp.write_text(body or "", encoding="utf-8")
                date_hdr = msg.get("date")
                try:
                    d = email.utils.parsedate_to_datetime(date_hdr).date().isoformat() if date_hdr else None
                except Exception:
                    d = None
                rec.update({
                    "from": str(msg.get("from") or "") or None,
                    "to": str(msg.get("to") or "") or None,
                    "cc": str(msg.get("cc") or "") or None,
                    "subject": str(msg.get("subject") or "") or None,
                    "date_header": date_hdr,
                    "date_guess": d or guess_date(p.name),
                    "date_source": "header" if d else ("filename" if guess_date(p.name) else None),
                    "body_format": fmt,
                    "text_path": f"00_TEXT/{rel}.txt",
                    "text_chars": len(body or ""),
                    "attachments": [a.get_filename() for a in msg.iter_attachments() if a.get_filename()],
                })
            except Exception as e:
                rec.update({"text_status": "parse_error", "error": str(e)[:200]})

        else:  # .msg: needs a parser; recorded so nothing is missed
            rec.update({"text_status": "not_parsed", "note": "Outlook .msg; parser not yet run"})

        recs.append(rec)

    out = ROOT / "records" / "documents.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {len(recs)} records to {out.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
