from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_incidents import audit, load  # noqa: E402

def test_dataset_size():
    assert audit(load())["records"] == 12

def test_category_mismatches_detected():
    assert audit(load())["category_mismatches"] == 6

def test_priority_mismatches_detected():
    assert audit(load())["priority_mismatches"] == 4

def test_accuracy_is_bounded():
    result = audit(load())
    assert 0 <= result["category_accuracy_pct"] <= 100
    assert 0 <= result["priority_accuracy_pct"] <= 100
