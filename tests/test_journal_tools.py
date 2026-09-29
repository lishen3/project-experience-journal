from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from render_journal_docx import render, validate  # noqa: E402
from validate_evidence import preflight  # noqa: E402


def payload(date: str = "2026-08-18") -> dict:
    return {
        "verification": {
            "timeline_checked": True,
            "technology_stack_checked": True,
            "metrics_checked": True,
            "privacy_checked": True,
        },
        "entries": [
            {
                "date": date,
                "project": "示例项目",
                "sections": {"我完成的工作": ["完成输入校验并通过测试"]},
            }
        ],
    }


class ValidationTests(unittest.TestCase):
    def test_rejects_impossible_calendar_date(self):
        with self.assertRaisesRegex(ValueError, "valid calendar date"):
            validate(payload("2026-02-30"))

    def test_clean_verified_payload_passes(self):
        data = payload()
        data["entries"][0]["sections"]["结果"] = ["使用 Python 完成 3 项校验"]
        checked = validate(data)
        self.assertEqual(preflight(checked), ([], []))

    def test_detects_privacy_and_unverified_claims(self):
        data = payload()
        data.pop("verification")
        data["entries"][0]["sections"]["结果"] = [
            "使用 Python 提升 30%，联系 student@example.com"
        ]
        errors, warnings = preflight(validate(data))
        self.assertTrue(any("email address" in error for error in errors))
        self.assertTrue(any("numerical claim" in warning for warning in warnings))
        self.assertTrue(any("technology-stack" in warning for warning in warnings))

    def test_example_renders_to_docx(self):
        output = ROOT / "tests" / ".test-journal.docx"
        try:
            source = json.loads((ROOT / "examples" / "example-input.json").read_text(encoding="utf-8"))
            render(validate(source), output)
            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 0)
        finally:
            output.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
