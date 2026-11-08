# Local test checklist

- [ ] Open `map/index.html` offline.
- [ ] Confirm the dark animated background renders without external requests.
- [ ] Confirm search/filter only uses embedded public rows.
- [ ] Confirm no card has an `<a href>` to a tracked service.
- [ ] Confirm the private CSV is not referenced by the map source.
- [ ] Run `python3 scripts/redact-public.py` and compare the public schema.
- [ ] Confirm `UNVERIFIED` remains visible where supplied.
