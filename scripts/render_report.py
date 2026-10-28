"""Publish one supplied current report and preserve prior text/JSON snapshots."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

from lint_report import lint_report
from report_model import markdown, validate_report
from validate_evidence import preflight


def publish_report(payload, destination):
    validate_report(payload)
    content = markdown(payload)
    errors, warnings = lint_report(content)
    evidence_errors, evidence_warnings = preflight(payload)
    if errors or warnings or evidence_errors or evidence_warnings:
        raise ValueError('; '.join(errors + warnings + evidence_errors + evidence_warnings))
    destination = Path(destination)
    if not destination.is_dir():
        destination.mkdir(parents=True)
    outputs = {'PROJECT_REPORT.md': content.encode('utf-8'),
               'PROJECT_REPORT.json': (json.dumps(payload, ensure_ascii=False, indent=2) + '\n').encode('utf-8')}
    # Snapshot every changed old representation before replacing either current file.
    # Replacements are atomic per file, not a cross-file database transaction.
    for filename, data in outputs.items():
        target = destination / filename
        if target.exists() and target.read_bytes() != data:
            old = target.read_bytes()
            snapshots = destination / 'snapshots'
            snapshots.mkdir(exist_ok=True)
            saved = snapshots / (target.stem + '-' + hashlib.sha256(old).hexdigest() + target.suffix)
            if saved.exists():
                if saved.read_bytes() != old:
                    raise ValueError('Snapshot checksum conflict')
            else:
                with saved.open('xb') as handle:
                    handle.write(old)
    for filename, data in outputs.items():
        target = destination / filename
        if target.exists() and target.read_bytes() == data:
            continue
        fd, temporary = tempfile.mkstemp(prefix='.report-', dir=destination)
        try:
            with os.fdopen(fd, 'wb') as handle:
                handle.write(data)
            os.replace(temporary, target)
        finally:
            Path(temporary).unlink(missing_ok=True)
    return destination / 'PROJECT_REPORT.md'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    try:
        result = publish_report(json.loads(args.input.read_text(encoding='utf-8')), args.directory)
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(str(exc))
        return 1
    print(result)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
