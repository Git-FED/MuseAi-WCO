#!/usr/bin/env python3
"""Append a dated rename observation supplied by the operator; no browsing."""
import argparse, csv, datetime

parser = argparse.ArgumentParser()
parser.add_argument("history_csv")
parser.add_argument("old_name")
parser.add_argument("new_name")
parser.add_argument("source")
parser.add_argument("--confidence", default="UNVERIFIED")
a = parser.parse_args()
with open(a.history_csv, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([a.old_name, a.new_name, datetime.date.today().isoformat(), a.source, a.confidence])
print("Appended observation; no site was visited.")
