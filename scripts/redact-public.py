#!/usr/bin/env python3
"""Generate the public tier from the private tier; drops notes and all operational fields."""
import argparse, csv
parser = argparse.ArgumentParser()
parser.add_argument("private_csv", nargs="?", default="data/sites-private.csv")
parser.add_argument("public_csv", nargs="?", default="data/sites-public.csv")
a = parser.parse_args()
with open(a.private_csv, newline="", encoding="utf-8") as f:
    rows = csv.DictReader(f)
    with open(a.public_csv, "w", newline="", encoding="utf-8") as out:
        w = csv.DictWriter(out, fieldnames=["name", "status", "category"])
        w.writeheader()
        for r in rows:
            w.writerow({"name": r.get("name", ""), "status": r.get("status", "UNKNOWN"), "category": r.get("category", "")})
print(f"Wrote redacted public tier to {a.public_csv}")
