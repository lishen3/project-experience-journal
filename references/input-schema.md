# Input schema

## V2 full and brief reports

Use v2 for readable full-project reports, keeping the legacy diary below compatible:

```json
{
  "schema_version": 2,
  "profile": "brief",
  "title": "示例项目实践记录",
  "as_of": "2026-10-28",
  "verification": {
    "timeline_checked": true,
    "technology_stack_checked": true,
    "metrics_checked": true,
    "privacy_checked": true
  },
  "sections": [
    {
      "id": "overview",
      "heading": "项目概况",
      "blocks": [
        {"type": "paragraph", "text": "说明实际问题与当前结果。"},
        {"type": "subheading", "text": "当前范围"},
        {"type": "bullets", "items": ["有依据的能力", "待验证的边界"]}
      ]
    }
  ]
}
```

The default profile is full, requiring section IDs overview, timeline, problems, architecture, contribution, next in this exact order. Brief allows a non-empty subset or a user-requested structure with unique stable lowercase IDs. Text fields are single-line strings; use separate paragraph blocks rather than manual line wraps. Supported blocks are paragraph, subheading and bullets. Arbitrary Markdown tables/code are not a v2 block type; use the concise prose/list representation for portable Markdown/Word output.

Run `python scripts/render_report.py INPUT.json ARCHIVE_DIRECTORY` to validate evidence/readability and write canonical PROJECT_REPORT.md/PROJECT_REPORT.json. Changed prior files are preserved by content hash in snapshots; an identical rerun creates no snapshot. Ledgers are never touched. Current files are replaced atomically per file, not as a cross-file transaction; if interrupted, rerun the same input and compare the canonical pair. Concurrent writers to the same archive are not supported.

For Word use the same input with render_journal_docx.py. Prose stays Normal, lists stay List Bullet, section/subheadings map to Heading 1/2, and the document title uses Title. No old snapshot is appended. Strict preflight scans all v2 body text and legacy summaries. Legacy schema remains supported for daily logs.

## Legacy diary

The Word renderer accepts UTF-8 JSON with this structure:

```json
{
  "title": "项目实践与能力成长记录",
  "verification": {
    "timeline_checked": true,
    "technology_stack_checked": true,
    "metrics_checked": true,
    "privacy_checked": true
  },
  "period_summary": {
    "项目概述": "Optional summary text",
    "阶段成果": ["Optional bullet"]
  },
  "entries": [
    {
      "date": "2026-08-18",
      "project": "Example project",
      "stage": "Implementation",
      "sections": {
        "当日目标": ["One goal"],
        "我完成的工作": ["One supported action"],
        "AI辅助与团队协作": ["One accurately attributed action"],
        "使用的知识、技巧、方法与策略": ["One applied method"],
        "关键决策及依据": ["Decision and rationale"],
        "项目推进与可验证结果": ["Result and evidence"],
        "遇到的问题及解决方式": ["Problem and resolution"],
        "体现的能力": ["Evidence-based capability"],
        "下一步计划": ["Next action"]
      }
    }
  ]
}
```

Rules:

- `title` is optional and defaults to `项目实践与能力成长记录`.
- `verification` is optional for backward compatibility, but all four checks must be `true` for strict preflight validation.
- `period_summary` is optional. Values may be strings or arrays of strings.
- `entries` is required and must be a non-empty array.
- Each entry requires ISO date `YYYY-MM-DD`, project name, and non-empty `sections`.
- `stage` is optional.
- Section values may be strings or arrays of strings.
- Empty values are omitted from the Word document.
- The renderer does not infer or verify facts. Evidence validation belongs to the agent workflow.

Before formal, portfolio, interview, resume, or public delivery, run:

```bash
python scripts/validate_evidence.py evidence.json --strict
```

The preflight rejects invalid or unordered dates and likely sensitive data. It warns when numerical results or technology-stack claims need source confirmation. Review warnings against the evidence ledger; do not merely rewrite claims to evade detection.

## Long-term archive and full-project reports

The three Markdown records described in [long-term-records.md](long-term-records.md) are maintained before report rendering. Validate them with `python scripts/validate_archive.py ARCHIVE_DIRECTORY`.

The Word renderer remains backward compatible with legacy diaries. For full reports prefer v2 above and readable-report.md. Unknown or approximate event dates remain paragraph text, never fabricated ISO diary entries. Verification booleans record investigator checks, not automatic proof of source truth or completeness.

