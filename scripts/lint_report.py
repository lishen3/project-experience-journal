"""Mechanical readability checks for reader-facing Markdown, not source ledgers."""
import argparse
import json
from pathlib import Path
import re


def lint_report(content):
    errors, warnings, headings, paragraphs = [], [], set(), set()
    lines = content.splitlines()
    title_count, previous_level, fenced = 0, 0, False
    paragraph = []

    def flush():
        value = ' '.join(paragraph).strip()
        paragraph.clear()
        if len(value) > 500:
            warnings.append('Overlong paragraph: split by meaning')
        if len(value) >= 60:
            if value in paragraphs:
                errors.append('Duplicate long paragraph')
            paragraphs.add(value)

    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^\s*(`{3,}|~{3,})', line):
            flush()
            fenced = not fenced
            continue
        if fenced:
            continue
        if not stripped:
            flush()
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading:
            flush()
            level, label = len(heading[1]), heading[2].strip()
            if level == 1:
                title_count += 1
            if level > 3 or level > previous_level + 1:
                errors.append(f'Line {i+1}: heading level jump or excessive depth')
            previous_level = level
            if label in headings:
                errors.append(f'Line {i+1}: duplicate heading')
            headings.add(label)
            if i+1 < len(lines) and lines[i+1].strip():
                errors.append(f'Line {i+1}: blank line required after heading')
            if i and lines[i-1].strip():
                errors.append(f'Line {i+1}: blank line required before heading')
        elif re.match(r'^\s*(?:[-*+] |\d+[.)] )', line):
            flush()
            if i and lines[i-1].strip() and not re.match(r'^\s*(?:[-*+] |\d+[.)] )', lines[i-1]):
                errors.append(f'Line {i+1}: blank line required before list')
            if i+1 < len(lines) and lines[i+1].strip() and not re.match(r'^\s*(?:[-*+] |\d+[.)] )', lines[i+1]):
                errors.append(f'Line {i+1}: blank line required after list')
            if len(line) - len(line.lstrip()) >= 4:
                warnings.append(f'Line {i+1}: nested list adds reading complexity')
        elif stripped.startswith('|'):
            flush()
            if len(re.split(r'(?<!\\)\|', stripped.strip('|'))) > 4:
                warnings.append(f'Line {i+1}: wide table')
        else:
            paragraph.append(stripped)
    flush()
    if title_count != 1:
        errors.append('Report must have exactly one document title')
    if fenced:
        errors.append('Unclosed code fence')
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    try:
        errors, warnings = lint_report(args.input.read_text(encoding='utf-8'))
    except (OSError, UnicodeError) as exc:
        errors, warnings = [str(exc)], []
    failed = bool(errors or (args.strict and warnings))
    print(json.dumps({'status': 'fail' if failed else 'pass', 'errors': errors, 'warnings': warnings}, ensure_ascii=False, indent=2))
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
