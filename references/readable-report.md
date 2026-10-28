# Readable reports and incremental revision

Read before writing or updating a reader-facing report. Preserve evidence history in ledgers and separate snapshots; synthesize one coherent current report. Never embed an old full report under a historical heading.

## Structure

Full project reports use six stable section IDs in order:

- overview / 项目概况: purpose, dated status and contribution boundary.
- timeline / 发展过程: chronological phases, goals, decisions and outcomes.
- problems / 关键问题与解决: selected problem chains and open items; link detailed P records.
- architecture / 当前架构: present entities and read/write flow; obsolete designs belong in the timeline.
- contribution / 成果与个人贡献: verified scoped results and supported user/AI contributions.
- next / 未解决事项与下一步: remaining risks, dependencies, acceptance criteria and source links.

Brief explanations use profile brief and selected sections; aim for 800–1600 Chinese characters or equivalent reading effort unless the user asks for completeness. Full reports have no forced word count. Group minor fixes and keep exhaustive evidence in ledgers. Explicit user structure takes precedence; diaries retain the legacy dated format.

## Formatting

One title, one current as-of date, H2 sections and H3 phase/problem names. No skipped levels or duplicated manual numbering. Use connected paragraphs, one idea each, usually 2–4 sentences; split at meaning boundaries, not mechanical character positions.

Use lists for parallel items/steps, without nested bullet walls. Tables are for short comparisons, usually four columns at most. Explain jargon once; paths, commit lists, tool access logs and full test outputs belong in the private index. Cite readable source links near claims. State limitations where relevant rather than repeating the same disclaimer throughout.

Markdown has blank lines around headings, lists and tables, without forced wrapping or ASCII grids. Word uses Title style, black headings, normal body prose, deliberate spacing and headings kept with following text; do not convert every paragraph to a bullet.

## Incremental update

1. Read report, ledgers and cutoff; identify new evidence, corrections and still-valid facts.
2. Update matching T/P records with stable IDs. Preserve supported historical status unless contradicted. Record Last-checked and Recheck separately; no rerun does not mean NOT_VERIFIED. Reopen only on evidence of recurrence or material contradiction.
3. Rewrite affected sections by stable ID and retain valid unaffected content. Keep superseded wording in snapshots and issue history, never a second current conclusion.
4. Reconcile dependent sections: capability changes may affect overview, architecture, results and next steps.
5. Keep canonical PROJECT_REPORT.md and PROJECT_REPORT.json. Archive prior content in snapshots without overwriting snapshots. Log a short dated increment. Dated exports are optional copies, not independent masters.
6. Run evidence preflight and readability lint, then read the complete output for flow, duplication, jargon and stale statements.

Use scripts/render_report.py INPUT.json ARCHIVE_DIRECTORY to render a complete supplied v2 state and snapshot prior text. It does not retrieve or semantically merge facts. The agent authors the reconciled sections first. The command never edits ledgers. Legacy concatenated reports must be preserved separately before a consolidated v2 rewrite.

Run python scripts/lint_report.py PROJECT_REPORT.md --strict. Mechanical checks cover title/heading structure, spacing, duplicates, wide tables and long prose; passing is not proof of truth or prose quality. Inspect rendered Markdown. DOCX layout requires rendered-page review where available; XML checks alone are structural, not visual acceptance.
