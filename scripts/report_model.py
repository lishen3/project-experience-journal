"""Structured readable report model; no evidence inference or historical merging."""
from datetime import date
import re

SECTION_IDS = ('overview', 'timeline', 'problems', 'architecture', 'contribution', 'next')


def text(value, label):
    if not isinstance(value, str) or not value.strip() or '\n' in value or '\r' in value:
        raise ValueError(f'{label} must be non-empty single-line text')
    return value.strip()


def validate_report(payload):
    if not isinstance(payload, dict):
        raise ValueError('report must be an object')
    if payload.get('schema_version') != 2:
        raise ValueError('schema_version must be 2')
    if 'entries' in payload or 'period_summary' in payload:
        raise ValueError('v2 sections cannot be mixed with legacy diary fields')
    text(payload.get('title'), 'title')
    as_of = payload.get('as_of')
    if not isinstance(as_of, str) or date.fromisoformat(as_of).isoformat() != as_of:
        raise ValueError('as_of must be an ISO calendar date')
    if payload.get('profile', 'full') not in ('full', 'brief'):
        raise ValueError('profile must be full or brief')
    sections = payload.get('sections')
    if not isinstance(sections, list) or not sections:
        raise ValueError('sections must be non-empty')
    ids = []
    for section in sections:
        if not isinstance(section, dict):
            raise ValueError('section must be an object')
        sid = text(section.get('id'), 'section id')
        if not re.fullmatch(r'[a-z][a-z0-9_-]*', sid) or sid in ids:
            raise ValueError('section IDs must be stable and unique')
        ids.append(sid)
        text(section.get('heading'), 'heading')
        blocks = section.get('blocks')
        if not isinstance(blocks, list) or not blocks:
            raise ValueError('section blocks must be non-empty')
        for block in blocks:
            if not isinstance(block, dict):
                raise ValueError('block must be an object')
            kind = block.get('type')
            if kind in ('paragraph', 'subheading'):
                text(block.get('text'), kind)
            elif kind == 'bullets':
                if not isinstance(block.get('items'), list) or not block['items']:
                    raise ValueError('bullet items must be non-empty')
                for item in block['items']:
                    text(item, 'bullet')
            else:
                raise ValueError('unsupported report block')
    if payload.get('profile', 'full') == 'full' and tuple(ids) != SECTION_IDS:
        raise ValueError('full report requires the six canonical section IDs in order')
    return payload


def iter_report_text(payload):
    yield 'title', payload['title']
    for section in payload['sections']:
        yield section['id'] + '.heading', section['heading']
        for index, block in enumerate(section['blocks']):
            for item in block.get('items', [block.get('text', '')]):
                yield f"{section['id']}.blocks[{index}]", item


def markdown(payload):
    validate_report(payload)
    lines = ['# ' + payload['title'].strip(), '', '更新日期：' + payload['as_of'], '']
    for section in payload['sections']:
        lines += ['## ' + section['heading'].strip(), '']
        for block in section['blocks']:
            if block['type'] == 'bullets':
                lines += ['- ' + item.strip() for item in block['items']]
            else:
                lines.append(('### ' if block['type'] == 'subheading' else '') + block['text'].strip())
            lines.append('')
    return '\n'.join(lines).rstrip() + '\n'
