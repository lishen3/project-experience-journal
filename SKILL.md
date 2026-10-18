---
name: project-experience-journal
description: Investigate project history and current state using available conversations, memory, files and Git; maintain linked timelines, issue histories and evidence indexes; generate evidence-based project journals, portfolio narratives, interview stories, resume bullets and Word-ready reports. Use for complete or incremental project experience reviews. Do not invent missing history or attribute AI-only actions to the user.
metadata:
  short-description: Extract valuable, evidence-based project experience
  version: 0.2.1
---

# Project Experience Journal

Create a clear record of what the user did, learned, decided, and advanced in a project. Identify why the work matters before polishing it. Prefer a few strong problem-decision-evidence chains over a complete chronology of low-value activity.

## Evidence boundary

Use only evidence that is available in the current task:

1. Current visible conversation and user-provided notes.
2. Files the user explicitly places in scope.
3. Read-only Git history when the user permits repository inspection.
4. Build, test, analysis, and validation outputs produced during the task.

Actively discover available memory, history-search, conversation-reading, handoff, file-search and Git capabilities. Search only project-relevant sources within their access boundaries. Record each source as searched (with coverage/cursor), unavailable, denied, or not applicable. Never imply that an unavailable search ran, or that missing evidence proves an event never happened. Ask for an export only when accessible alternatives cannot resolve a material gap.

Separate contribution types and preserve the strongest distinction supported by the evidence:

- `User-decided`: the user chose a requirement, boundary, tradeoff, acceptance criterion, or next step.
- `User-implemented`: evidence shows the user personally performed the implementation or analysis.
- `AI-proposed, user-adopted`: an assistant proposed an idea and the user demonstrably accepted or incorporated it.
- `AI-implemented, user-verified`: an assistant produced code, analysis, or artifacts that the user reviewed or accepted using stated evidence.
- `Team contribution`: work attributed to named or described collaborators.
- `Unknown`: evidence does not identify the contributor.

Do not infer personal implementation from approval alone. Never convert an AI action into a user capability claim. Capability statements must be grounded in a user decision, explanation, correction, implementation, or verified adoption. When authorship remains uncertain, describe the project outcome separately from the user's contribution.

## Workflow

### Investigation gate — before synthesis

Unless the user explicitly requests a local edit, first read and follow [references/project-investigation.md](references/project-investigation.md) in order. This gate applies to daily, resume and Word requests too; limit retrieval to their scope. Read existing archives before assigning IDs. Complete the source-access log, timeline, issue-state reconciliation and completeness check before writing polished prose. Missing sources limit claims, not the ability to deliver supported findings.

Maintain `PROJECT_TIMELINE.md`, `ISSUE_LEDGER.md`, and `EVIDENCE_INDEX.md` in the project's private experience archive using [references/long-term-records.md](references/long-term-records.md) and the bundled `templates/`. These are linked working records, not disposable exports. Reuse the existing archive location; otherwise use `project-experience/` inside the scoped project. A user-specified experience repository takes precedence. Never save real project evidence in this reusable Skill's source repository. For read-only/chat-only requests, return proposed record updates and disclose that files were not saved.

The report is a view of those records: include project overview/contribution boundary, complete scoped timeline, issue ledger, technical decisions/architecture evolution, verified development results, unresolved risks, personal/AI contributions, experience/resume wording, next handoff and evidence index. Keep independent workstreams identifiable. A short resume or journal may condense the view; it must not erase unresolved records from the archive.

### 1. Establish scope

Determine:

- project name;
- date or date range and timezone;
- intended audience: personal review, course record, portfolio, interview, resume, or formal report;
- available evidence sources;
- output format: chat, Markdown, or Word.

Default to the current local date when no date is specified. Use the project's own dates when the evidence clearly describes earlier work.

### 2. Build an evidence ledger

Before writing prose, extract factual entries with:

- date;
- source;
- action;
- purpose;
- result or current status;
- knowledge, technique, method, or strategy;
- decision and rationale;
- validation performed;
- blocker or unresolved risk;
- contributor type.

Deduplicate repeated conversational statements and repeated Git descriptions. Preserve meaningful revisions: explain what changed and why rather than listing every file touch.

For each result, record the highest maturity level directly supported by evidence:

- `CONCEPT`: discussed but not designed;
- `DESIGNED`: contract or architecture documented, not implemented;
- `IMPLEMENTED`: code or artifact exists, verification absent or incomplete;
- `UNIT_VERIFIED`: focused automated checks pass;
- `INTEGRATION_VERIFIED`: connected components pass together in a controlled environment;
- `REAL_ENV_VERIFIED`: the actual provider, device, browser, dataset, or operating environment was exercised successfully;
- `DEPLOYED`: the result is available in its intended environment and deployment was verified.

Use the highest proven level, not the intended next level. A successful process exit, HTTP 200, parseable JSON, compiled build, or approved proposal proves only its corresponding layer.

### 3. Perform a value audit

Before choosing headings or writing chronology, identify:

- the real user or engineering problem;
- the central tension or constraint;
- the hardest uncertainty or failure;
- the key decision or tradeoff;
- the strongest validation evidence;
- the important rejected alternative or scope reduction;
- the current maturity level and unresolved risk.

Rank candidate experiences by decision difficulty, consequence, evidence strength, and relevance to the intended audience. Prefer three to five strong themes. Do not force significance: if the evidence shows routine execution only, say so plainly.

### 4. Build problem-solving chains

For each high-value theme, reconstruct the supported subset of:

`observed problem -> risk -> hypothesis -> investigation or experiment -> evidence -> decision -> result -> remaining uncertainty`

Keep unknown causes unknown. Preserve failed attempts when they changed the diagnosis or decision. Highlight a scope reduction when it produced a safer or more verifiable result; do not present reduced scope as failure by default.

### 5. Select the domain profile

Use the general profile unless a domain profile is clearly applicable.

- For mathematical modeling, read [references/math-modeling.md](references/math-modeling.md).
- For software development, read [references/software-development.md](references/software-development.md).
- For research or coursework, read [references/research-coursework.md](references/research-coursework.md).

If a project spans domains, combine only the relevant fields. Do not force every heading into every entry.

### 6. Choose the narrative structure

- Daily log or course record: organize primarily by date.
- Weekly or monthly review: lead with milestones and value themes, then add a concise chronology.
- Portfolio, interview, or full-project summary: organize by problems, decisions, and evidence; use dates as supporting context rather than the main structure.
- Resume mode: select only the strongest two to four evidence-backed outcomes and decisions.

Do not default every request to a diary. Match structure to the user's audience.

### 7. Write the report

Use the title:

`# 项目实践与能力成长记录`

For each date, include the useful subset of:

- 项目名称与阶段；
- 当日目标；
- 我完成的工作；
- AI辅助与团队协作；
- 使用的知识、技巧、方法与策略；
- 关键决策及依据；
- 项目推进与可验证结果；
- 遇到的问题及解决方式；
- 体现的能力；
- 下一步计划。

Write in the user's first-person voice when the evidence supports it. Prefer concrete verbs and outcomes. Avoid inflated phrases such as “精通”“显著提升”“独立完成” unless explicitly supported.

For multi-day reports, add a short period summary covering the core problem, valuable decisions, milestones, capability growth, unresolved risks, and next priorities. For resume mode, convert the strongest evidence into 2-4 concise bullets without inventing metrics.

For portfolio and interview outputs, make the project's value legible without requiring the reader to know the repository. Explain why a decision mattered and what weaker alternative it avoided. Prefer “restricted the action space to date-only updates after semantic and policy failures” over a list of edited files.

When evidence contains several kinds of verification, state them separately. Do not collapse unit tests, mocked integration, browser checks, real-provider experiments, database execution, and deployment into a single claim of “fully verified.”

### 8. Validate

Before delivery, check:

- every claimed action is supported by evidence;
- dates and project stages are consistent;
- user, AI, and team contributions are not conflated;
- methods are connected to an actual decision or result;
- numerical claims have a source;
- unresolved work is not described as completed;
- each major result has an explicit maturity level or wording that makes its maturity unambiguous;
- the report foregrounds the highest-value problem-decision-evidence chains rather than raw activity volume;
- failed experiments and rejected alternatives that materially changed the project are preserved;
- secrets, personal data, private URLs, local absolute paths, and proprietary content are excluded unless explicitly requested for a private artifact;
- the report can be understood without reading the entire conversation.

Check the investigation completeness checklist in `references/project-investigation.md`. Run `python scripts/validate_archive.py <archive-directory>` after editing the three records. This checks record structure, IDs, references and status support, not whether the evidence is true. Resolve errors against sources; do not invent evidence to satisfy the validator. Report inaccessible sources, timeline gaps, uncertain dates, stale checks and unsaved updates explicitly.

For formal, portfolio, interview, resume, or public output, record the four checks in the input JSON and run the strict preflight described in [references/input-schema.md](references/input-schema.md). Treat a technology name as confirmed only when it appears in scoped project evidence. Trace every numerical result to a test, measurement, Git evidence, or explicit user statement. If the source is missing, label the claim as unverified or omit it.

Before reading or quoting project documents, minimize the material placed in scope. Redact credentials, personal identifiers, private URLs, customer data, local absolute paths, and proprietary content from generated artifacts. Describing a source as “project documentation” is usually enough; do not reproduce sensitive passages merely to prove they were consulted.

### 9. Export to Word when requested

Create an evidence JSON file matching [references/input-schema.md](references/input-schema.md), then run:

```bash
python scripts/render_journal_docx.py evidence.json output.docx
```

If `python-docx` is unavailable, install dependencies from `requirements.txt` or return Markdown and clearly state that Word export was not completed. Reopen the generated file and verify title, dates, headings, bullet lists, and page readability before delivery.

## Privacy and publishing

Treat project evidence as private by default. A request to publish this Skill does not authorize publishing source projects, transcripts, attachments, generated reports, or local paths.

Before publishing the Skill repository, run:

```powershell
pwsh -NoProfile -File scripts/check_public_safety.ps1 -Root .
```

Review every reported match. Do not publish if secrets, personal data, real project evidence, local absolute paths, or temporary files remain.
