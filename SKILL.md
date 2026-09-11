---
name: project-experience-journal
description: Summarize project work from the current conversation, user notes, project files, and optional Git evidence into dated, evidence-based experience records and Word-ready reports. Use for daily project journals, modeling competition logs, weekly or monthly reviews, portfolio narratives, and resume-oriented project summaries. Do not invent work or attribute AI-only actions to the user.
metadata:
  short-description: Create dated, evidence-based project experience reports
  version: 0.1.0
---

# Project Experience Journal

Create a clear record of what the user did, learned, decided, and advanced in a project. Prefer evidence over polished but unsupported claims.

## Evidence boundary

Use only evidence that is available in the current task:

1. Current visible conversation and user-provided notes.
2. Files the user explicitly places in scope.
3. Read-only Git history when the user permits repository inspection.
4. Build, test, analysis, and validation outputs produced during the task.

Do not claim access to earlier conversations that are not visible. Ask for an exported transcript or notes only when missing history materially affects the requested period.

Separate contribution types:

- `User contribution`: choices, reasoning, implementation, review, research, communication, and learning demonstrably performed by the user.
- `AI-assisted work`: analysis, drafts, code, or checks produced by an assistant and reviewed or adopted by the user.
- `Team contribution`: work attributed to named or described collaborators.
- `Unknown`: evidence does not identify the contributor.

Never convert an AI action into a user capability claim. Capability statements must be grounded in a user decision, explanation, correction, implementation, or verified adoption.

## Workflow

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

### 3. Select the domain profile

Use the general profile unless a domain profile is clearly applicable.

- For mathematical modeling, read [references/math-modeling.md](references/math-modeling.md).
- For software development, read [references/software-development.md](references/software-development.md).
- For research or coursework, read [references/research-coursework.md](references/research-coursework.md).

If a project spans domains, combine only the relevant fields. Do not force every heading into every entry.

### 4. Write the report

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

For multi-day reports, add a short period summary covering milestones, capability growth, unresolved risks, and next priorities. For resume mode, convert the evidence into 2-4 concise bullets without inventing metrics.

### 5. Validate

Before delivery, check:

- every claimed action is supported by evidence;
- dates and project stages are consistent;
- user, AI, and team contributions are not conflated;
- methods are connected to an actual decision or result;
- numerical claims have a source;
- unresolved work is not described as completed;
- secrets, personal data, private URLs, local absolute paths, and proprietary content are excluded unless explicitly requested for a private artifact;
- the report can be understood without reading the entire conversation.

### 6. Export to Word when requested

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
