#!/usr/bin/env python3
"""Preflight a project journal JSON before prose or Word export."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from render_journal_docx import as_items, validate


SENSITIVE_PATTERNS = {
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "local absolute path": re.compile(r"(?:[A-Z]:\\Users\\[^\\\s]+|/Users/[^/\s]+|/home/[^/\s]+)", re.I),
    "private key": re.compile(r"BEGIN [A-Z ]*PRIVATE KEY", re.I),
    "credential-like value": re.compile(r"\b(?:api[_-]?key|password|secret)\s*[:=]\s*\S+", re.I),
}
NUMBER_PATTERN = re.compile(r"(?<![\w-])\d+(?:\.\d+)?\s*(?:%|倍|个|次|条|项|人|小时|天|ms|s|MB|GB)?", re.I)
TECH_PATTERN = re.compile(
    r"\b(?:Python|JavaScript|TypeScript|Java|Go|Rust|React|Vue|Angular|Django|Flask|FastAPI|Spring|Node\.js|SQL|Docker|Kubernetes)\b",
    re.I,
)


def iter_text(payload: dict):
    for entry_index, entry in enumerate(payload["entries"], start=1):
        for heading, value in entry["sections"].items():
            for item_index, item in enumerate(as_items(value), start=1):
                yield f"entries[{entry_index}].sections.{heading}[{item_index}]", item


def preflight(payload: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    dates = [entry["date"] for entry in payload["entries"]]
    if dates != sorted(dates):
        errors.append("entries must be ordered from earliest to latest date")

    verification = payload.get("verification")
    checks = ("timeline_checked", "technology_stack_checked", "metrics_checked", "privacy_checked")
    if not isinstance(verification, dict):
        warnings.append("verification checklist is missing")
    else:
        for check in checks:
            if verification.get(check) is not True:
                warnings.append(f"verification.{check} is not true")

    metrics_checked = isinstance(verification, dict) and verification.get("metrics_checked") is True
    technology_stack_checked = (
        isinstance(verification, dict) and verification.get("technology_stack_checked") is True
    )

    for location, text in iter_text(payload):
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{location}: possible {label}")
        if NUMBER_PATTERN.search(text) and not metrics_checked:
            warnings.append(f"{location}: numerical claim needs a traceable source")
        if TECH_PATTERN.search(text) and not technology_stack_checked:
            warnings.append(f"{location}: technology-stack claim needs confirmation")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    try:
        payload = validate(json.loads(args.input.read_text(encoding="utf-8")))
        errors, warnings = preflight(payload)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "fail", "errors": [str(exc)], "warnings": []}, ensure_ascii=False, indent=2))
        return 1

    status = "fail" if errors or (args.strict and warnings) else "pass"
    print(json.dumps({"status": status, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 1 if status == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
