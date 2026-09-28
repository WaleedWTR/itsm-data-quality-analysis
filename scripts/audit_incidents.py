#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "incidents.csv"

def load():
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def audit(rows):
    category_mismatch = [
        r for r in rows if r["original_category"] != r["validated_category"]
    ]
    priority_mismatch = [
        r for r in rows if r["priority"] != r["expected_priority"]
    ]
    other_category = [
        r for r in rows if r["original_category"].lower() == "other"
    ]
    return {
        "records": len(rows),
        "category_mismatches": len(category_mismatch),
        "category_accuracy_pct": round(
            (len(rows) - len(category_mismatch)) / len(rows) * 100, 1
        ),
        "priority_mismatches": len(priority_mismatch),
        "priority_accuracy_pct": round(
            (len(rows) - len(priority_mismatch)) / len(rows) * 100, 1
        ),
        "other_category_count": len(other_category),
        "mismatch_by_original_category": dict(
            Counter(r["original_category"] for r in category_mismatch)
        ),
    }

if __name__ == "__main__":
    for key, value in audit(load()).items():
        print(f"{key}: {value}")
