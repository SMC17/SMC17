"""Run: python3 -m unittest ops/test_smc17ops.py"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from smc17ops import parse_tests, ratchet_baseline  # noqa: E402

CASES = {
    "Build Summary: 3/3 steps succeeded; 47/47 tests passed": (47, 0, 0),
    "Build Summary: 15/15 steps succeeded; 166/195 tests passed (29 skipped)": (166, 0, 29),
    "Build Summary: 7/9 steps succeeded (1 failed); 594/613 tests passed (16 skipped, 3 failed)": (594, 3, 16),
    "Finished in 0.02 seconds\n5 tests, 0 failures": (5, 0, 0),
    "5 tests, 5 failures": (0, 5, 0),
    "Passed!  - Failed:     0, Passed:   392, Skipped:     0, Total:   392, Duration: 16 s": (392, 0, 0),
    "194 passed, 12 skipped in 10.71s": (194, 0, 12),
    "1 failed, 193 passed, 12 skipped in 25.74s": (193, 1, 12),
    "Ran 11 tests in 0.000s\n\nOK": (11, 0, 0),
    "Ran 3 tests in 0.001s\n\nFAILED (failures=1)": (2, 1, 0),
}


class ParseTests(unittest.TestCase):
    def test_toolchain_summaries(self):
        for text, want in CASES.items():
            r = parse_tests(text)
            self.assertEqual((r["passed"], r["failed"], r["skipped"]), want, text)


class Ratchet(unittest.TestCase):
    def test_baseline_only_moves_up(self):
        base = {"r": {"passed": 10, "formula_computed_pct": 70.0, "placeholders": 100}}
        worse = {"repos": {"r": {"gate": {"ok": True, "passed": 8}, "workbooks": {"formula_computed_pct": 60.0, "placeholders": 120}}}}
        self.assertEqual(ratchet_baseline(worse, base)["r"], base["r"])
        better = {"repos": {"r": {"gate": {"ok": True, "passed": 12}, "workbooks": {"formula_computed_pct": 80.0, "placeholders": 90}}}}
        self.assertEqual(ratchet_baseline(better, base)["r"], {"passed": 12, "formula_computed_pct": 80.0, "placeholders": 90})

    def test_failing_gate_does_not_raise_baseline(self):
        base = {"r": {"passed": 10}}
        failing = {"repos": {"r": {"gate": {"ok": False, "passed": 50}}}}
        self.assertEqual(ratchet_baseline(failing, base)["r"]["passed"], 10)


if __name__ == "__main__":
    unittest.main()
