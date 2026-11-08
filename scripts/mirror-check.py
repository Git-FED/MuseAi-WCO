#!/usr/bin/env python3
"""Safe local status placeholder. It never visits a site or follows a link."""
import argparse, csv

parser = argparse.ArgumentParser(description="Review domain/status rows without network access")
parser.add_argument("csv_file", nargs="?", default="data/sites-private.csv")
args = parser.parse_args()
with open(args.csv_file, newline="", encoding="utf-8") as f:
    rows = csv.DictReader(f)
    for row in rows:
        print(f"{row.get('name','')}: recorded status={row.get('status','UNKNOWN')} (not network-checked)")
