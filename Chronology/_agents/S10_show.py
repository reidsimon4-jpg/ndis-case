import json,sys
ids=set(int(x) for x in sys.argv[1:])
for l in open('/dev/stdin' if False else __import__('os').path.expanduser('~/mnt/NDIS Case/Chronology/_agents/S10_events.jsonl')):
    r=json.loads(l)
    if not ids or r['source_id'] in ids: print(r['date'],r['source_id'],r['category'],'|',r['what'][:130])
