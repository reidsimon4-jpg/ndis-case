#!/usr/bin/env python3
"""Export the chronology database into a code layer for AI birds-eye review.

Reads:  Chronology/NDIS_Case_Database.sqlite  (events, records, people, meta)
Writes: records/events.jsonl, records/people.jsonl,
        records/case_overview.md, records/conflicts.md, records/verification.md

Event status is preserved everywhere. 'allegation' and 'simon_position' are
NOT established facts. Run from repo root: python3 build/build_overview.py
"""
import json, sqlite3, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "Chronology" / "NDIS_Case_Database.sqlite"
OUT = ROOT / "records"
OUT.mkdir(exist_ok=True)

STATUS_KEY = {
    "fact": "Stated in a source document; not contested in that source",
    "allegation": "Alleged by one party; not established",
    "simon_position": "Applicant (Simon Reid) position; not neutral",
    "contention": "Disputed between parties",
    "unverified": "Not yet checked against source",
    "planned": "Future or intended action",
}

def rows(c, q):
    c.row_factory = sqlite3.Row
    return [dict(r) for r in c.execute(q)]

def main():
    c = sqlite3.connect(DB)
    events = rows(c, "select * from events order by date, id")
    people = rows(c, "select * from people order by n_pivotal desc")
    meta = {r["k"]: r["v"] for r in rows(c, "select k,v from meta")}
    ev_by_id = {e["id"]: e for e in events}

    # --- events.jsonl (one line per event, all fields kept) ---
    with open(OUT / "events.jsonl", "w", encoding="utf-8") as f:
        for e in events:
            f.write(json.dumps({k: v for k, v in e.items() if v not in (None, "")}, ensure_ascii=False) + "\n")

    # --- people.jsonl ---
    with open(OUT / "people.jsonl", "w", encoding="utf-8") as f:
        for p in people:
            f.write(json.dumps({k: v for k, v in p.items() if v not in (None, "")}, ensure_ascii=False) + "\n")

    # --- case_overview.md ---
    year = lambda e: (e["date"] or "????")[:4]
    by_year = collections.Counter(year(e) for e in events)
    by_year_sig3 = collections.Counter(year(e) for e in events if str(e["significance"]) == "3")
    by_cat = collections.Counter(e.get("category") or "?" for e in events)
    by_status = collections.Counter(e.get("status") or "?" for e in events)
    verified = collections.Counter(e.get("verified") or "not_checked" for e in events)
    key_events = [e for e in events if str(e["significance"]) == "3"]

    L = []
    L += ["# NDIS case: birds-eye overview", "",
          f"Generated from the chronology database (built {meta.get('built','?')}). "
          f"Regenerate with `python3 build/build_overview.py`.", "",
          "**Read this first.** Every event has a `status`. Only `fact` is a stated fact in its source, "
          "and even `fact` is not verified unless `verified` says so. Do not treat `allegation` or "
          "`simon_position` as established.", ""]
    L += ["## Totals",
          f"- Events: {len(events)} (significance 3 = key: {len(key_events)})",
          f"- People: {len(people)}",
          f"- Source records: {c.execute('select count(*) from records').fetchone()[0]}",
          f"- Date range: {min(e['date'] for e in events if e['date'])} to {max(e['date'] for e in events if e['date'])}",
          ""]
    L += ["## Status key"] + [f"- `{k}`: {v} ({by_status.get(k,0)} events)" for k, v in STATUS_KEY.items()] + [""]
    L += ["## Verification"]
    L += [f"- `{k}`: {v}" for k, v in verified.most_common()] + [""]
    L += ["## Events by category"] + [f"- {k}: {v}" for k, v in by_cat.most_common()] + [""]
    L += ["## Events by year (all / key)"]
    L += ["| Year | All | Key (sig 3) |", "|---|---|---|"]
    L += [f"| {y} | {by_year[y]} | {by_year_sig3.get(y,0)} |" for y in sorted(by_year)] + [""]
    L += ["## Key events (significance 3), chronological",
          "Format: id | date | status | title | sources (primary)"]
    for e in key_events:
        src = (e.get("primary_source") or "").replace("NDIS Case/", "")
        L.append(f"- {e['id']} | {e['date']} | {e.get('status')} | {e['title']} | {src}")
    L += [""]
    L += ["## Top people (by pivotal events)", "| Name | Side | Pivotal | Events | Role |", "|---|---|---|---|---|"]
    for p in people[:25]:
        role = (p.get("role") or "")[:90].replace("|", "/")
        L.append(f"| {p['name']} | {p.get('side') or ''} | {p.get('n_pivotal') or 0} | {p.get('n_events') or 0} | {role} |")
    L += [""]
    (OUT / "case_overview.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # --- conflicts.md ---
    conf = [e for e in events if e.get("conflicts")]
    C = ["# Source conflicts", "",
         f"{len(conf)} events record a conflict between sources. Resolve against the originals before relying on them.", ""]
    for e in conf:
        C.append(f"- **{e['id']}** ({e['date']}, {e.get('status')}): {e['title']}")
        C.append(f"  - {e['conflicts']}")
    (OUT / "conflicts.md").write_text("\n".join(C) + "\n", encoding="utf-8")

    # --- verification.md (errors and minor corrections) ---
    V = ["# Verification findings", "",
         "Events where the source check found an error or a minor correction. Fix before any use.", ""]
    for label in ("error", "minor", "unverifiable"):
        group = [e for e in events if e.get("verified") == label]
        V.append(f"## {label} ({len(group)})")
        for e in group:
            V.append(f"- **{e['id']}** ({e['date']}): {e['title']}")
            if e.get("verifier_note"):
                V.append(f"  - {e['verifier_note']}")
        V.append("")
    (OUT / "verification.md").write_text("\n".join(V) + "\n", encoding="utf-8")

    print(f"events={len(events)} people={len(people)} key={len(key_events)} conflicts={len(conf)}")

if __name__ == "__main__":
    main()
