# Linked long-term project records

Reader-facing reports follow readable-report.md and the v2 input schema. Keep one canonical report; old full texts live in snapshots, not the current body. Preserve historical issue status unless contradicted by new evidence; record Last-checked and Recheck separately. Not rerunning does not mean NOT_VERIFIED. Unknown fields need specific gaps, not generic repeated filler. Existing legacy Word mapping below is for diaries only; use v2 blocks for full narratives.

Keep one private archive per project. Copy the three templates only for first initialization; never overwrite populated files with templates. IDs are local to the archive: T001 phases, P001 issues, E001 evidence. Allocate the next unused number; never renumber, recycle or delete cited IDs. Multiple workstreams share the same namespace and have explicit labels.

Each file has Project, Investigated-through and Updated metadata. Dates use ISO calendar dates; unknown historical event/source dates are written `unknown` and explained. The cutoff and update dates are actual dates. Headers `## T001 ...`, `## P001 ...`, `## E001 ...` define records. Fields use `- Field: value`. Literal E/P/T IDs in record bodies are cross references; do not use nonexistent example IDs in real records.

`PROJECT_TIMELINE.md`: append phase records with Date, Date-basis, Workstream, Goal, Decisions, Outputs, Problems/attempts, Validation, Next-impact, Outstanding and Evidence. Add `## Investigation YYYY-MM-DD` for each investigation, including requested interval, status-recheck date, previous cutoff, source-access log/cursors, completeness checklist, gaps/conflicts, incremental changes and handoff/acceptance criteria.

`ISSUE_LEDGER.md`: one record per issue with First-seen, Status, Cause-confidence, Symptom/impact, Reproduction, Root-cause, Attempts, Fix/affected modules, Verification, Release, Remaining-risk, Related and Evidence. Append dated History entries for each occurrence, repair, failed/passing check, publication and reopening. Update current fields without deleting the history. Do not auto-promote status based on newer dates or file existence.

`EVIDENCE_INDEX.md`: one entry per source/observation with Source-type, Locator, Source-date, Observed-at, Claim, Limits and relevant revision/environment. Types: CODE, RUN, GIT, TEST, RELEASE, REPORT, CONVERSATION, MEMORY, USER, INFERENCE. A new test run or revision is a new observation, even if its path is unchanged. Claims cite exact test scope/result and whether observed this run or reported historically. Changing a locator requires a dated correction note; keep enough old locator information to resolve earlier citations.

Status support rules checked by the validator:

- TEST_VERIFIED requires a cited TEST or RUN observation;
- E2E_VERIFIED requires a cited RUN observation describing real integration scope;
- RELEASED requires a cited RELEASE observation;
- ROOT_CAUSE_IDENTIFIED requires CONFIRMED cause confidence.

Every phase and issue needs Evidence references; each E record states both Claim and Limits. Other status evidence is assessed by the investigator. A source-type label alone cannot establish truth or adequacy. The validator checks links/shape and the minimal support rules above; the agent must still inspect the underlying sources and apply the completeness gate.

Run `python scripts/validate_archive.py <archive-directory>` before rendering. Use the v2 section/block schema for full reader-facing reports. The legacy Word JSON format stays compatible for dated diaries: map summaries to `period_summary` and dated milestones to `entries`. Keep uncertain-date events in summary/Markdown rather than invent an ISO date to satisfy the diary renderer. Run strict evidence preflight for formal output. Regenerate Word as a view; the Markdown archive remains the durable record.
