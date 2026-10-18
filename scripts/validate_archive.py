"""Check linked project archive records without writing or inferring facts."""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re

FILES = {'PROJECT_TIMELINE.md': 'T', 'ISSUE_LEDGER.md': 'P', 'EVIDENCE_INDEX.md': 'E'}
STATUSES = set('REPORTED INVESTIGATING ROOT_CAUSE_IDENTIFIED FIX_IMPLEMENTED TEST_VERIFIED E2E_VERIFIED RELEASED PARTIALLY_RESOLVED BLOCKED UNRESOLVED NOT_VERIFIED'.split())
TYPES = set('CODE RUN GIT TEST RELEASE REPORT CONVERSATION MEMORY USER INFERENCE'.split())


def fields(text):
    return dict(re.findall(r'^- ([\w-]+):\s*(.*)$', text, re.M))


def valid_date(value):
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_archive(root: Path):
    errors, records, projects, cutoffs = [], {}, set(), set()
    for filename, prefix in FILES.items():
        path = root / filename
        if not path.is_file():
            errors.append(f'Missing {filename}')
            continue
        text = path.read_text(encoding='utf-8')
        if 'TO_FILL' in text:
            errors.append(f'{filename}: unfinished template')
        chunks = re.split(r'^## ([TPE]\d{3,})\b[^\n]*\n', text, flags=re.M)
        meta = fields(chunks[0])
        if not meta.get('Project'):
            errors.append(f'{filename}: missing Project')
        projects.add(meta.get('Project'))
        cutoffs.add(meta.get('Investigated-through'))
        for key in ('Investigated-through', 'Updated'):
            if not valid_date(meta.get(key, '')):
                errors.append(f'{filename}: invalid {key}')
        if prefix == 'T' and not re.search(r'^## Investigation \d{4}-\d{2}-\d{2}\b', text, re.M):
            errors.append(f'{filename}: missing investigation log')
        for index in range(1, len(chunks), 2):
            rid, body = chunks[index:index + 2]
            if rid in records:
                errors.append(f'Duplicate ID {rid}')
            if not rid.startswith(prefix):
                errors.append(f'{rid}: wrong file')
            records[rid] = (fields(body), body)
    if len(projects) > 1 or len(cutoffs) > 1:
        errors.append('Archive project/cutoff metadata disagree')
    if not any(rid.startswith('E') for rid in records):
        errors.append('No indexed evidence')
    required = {'T': ('Date', 'Date-basis', 'Workstream', 'Goal', 'Decisions', 'Outputs', 'Problems', 'Validation', 'Next-impact', 'Outstanding', 'Evidence'),
                'P': ('First-seen', 'Status', 'Cause-confidence', 'Symptom', 'Reproduction', 'Root-cause', 'Attempts', 'Fix', 'Verification', 'Release', 'Remaining-risk', 'History', 'Evidence'),
                'E': ('Source-type', 'Locator', 'Source-date', 'Observed-at', 'Claim', 'Limits')}
    for rid, (data, body) in records.items():
        for key in required[rid[0]]:
            if not data.get(key):
                errors.append(f'{rid}: missing {key}')
        refs = set(re.findall(r'\b[TPE]\d{3,}\b', body))
        for ref in refs:
            if ref not in records:
                errors.append(f'{rid}: dangling reference {ref}')
        evidence = set(re.findall(r'\bE\d{3,}\b', data.get('Evidence', '')))
        if rid[0] in 'TP' and not evidence:
            errors.append(f'{rid}: missing evidence references')
        if rid.startswith('E'):
            if data.get('Source-type') not in TYPES:
                errors.append(f'{rid}: invalid source type')
            if data.get('Source-date') != 'unknown' and not valid_date(data.get('Source-date', '')):
                errors.append(f'{rid}: invalid source date')
            if not valid_date(data.get('Observed-at', '')):
                errors.append(f'{rid}: invalid observation date')
        if rid.startswith('P'):
            status = data.get('Status')
            if status not in STATUSES:
                errors.append(f'{rid}: invalid status')
            if data.get('Cause-confidence') not in ('CONFIRMED', 'LIKELY', 'UNKNOWN'):
                errors.append(f'{rid}: invalid cause confidence')
            if status == 'ROOT_CAUSE_IDENTIFIED' and data.get('Cause-confidence') != 'CONFIRMED':
                errors.append(f'{rid}: root cause not confirmed')
            types = {records[ref][0].get('Source-type') for ref in evidence if ref in records}
            needed = {'TEST_VERIFIED': {'TEST', 'RUN'}, 'E2E_VERIFIED': {'RUN'}, 'RELEASED': {'RELEASE'}}.get(status)
            if needed and not types.intersection(needed):
                errors.append(f'{rid}: status lacks supporting evidence type')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    try:
        errors = validate_archive(args.directory)
    except (OSError, UnicodeError) as exc:
        errors = [str(exc)]
    print(json.dumps({'status': 'fail' if errors else 'pass', 'errors': errors}, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
