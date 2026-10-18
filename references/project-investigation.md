# Project investigation

Run these steps in order before synthesis. Source retrieval is read-only; do not alter business code/data or incur new paid model requests to write a report. Tests are optional diagnostics: run only relevant safe checks when authorized; otherwise cite dated historical results as historical.

## 1. Identify scope and baseline

Identify project, purpose, repository, stack with source, requested interval, timezone, and existing journals/handoffs. Distinguish first mention, formal start, first commit, phase changes and last activity; the earliest commit does not prove the project's inception. Record recollected dates, conversation timestamps and Git/report dates separately. Use unknown or approximate ranges where necessary.

Read the three existing archive records and last investigation cutoff. Confirm repository identity using its root and remote before attributing code or Git evidence. When updating this Skill itself, verify the target is the Skill repository; never mix application code into it. User-authorized work in an explicitly named target repository may proceed even if the chat originally opened another workspace.

## 2. Retrieve available history

Inspect the tools actually exposed before choosing memory/history/connector calls. Search project names, repository, distinctive errors and stage names. Read relevant hits and follow pagination when required to cover the interval. Bound searches to the project; do not sweep unrelated private histories. Search accessible journals, HANDOFFs, logs and stage reports as well.

Extract original intent, requirements/constraints, user decisions/rejections, failures, attempts, implementations, reviews and last handoff. Link repeated occurrences while preserving dates. Record source access and exact coverage: unavailable tools, denied access and unvisited older pages remain gaps. Cached conversation previews are bounded evidence, not full history. Never convert an assistant's proposal or the user's brief approval into personal implementation claims.

## 3. Verify current state

Read current branch, HEAD, working tree, relevant history and tags, README/changelog/reports and affected implementation/tests/configuration. Check uncommitted/unreleased work and relevant TODOs. Query remote branches/releases only with available access. A clean tree proves neither push nor release; local tags prove neither remote tags nor GitHub Releases.

Reconcile old reports with current code without erasing either. Record observed-at date, revision and environment. Current code proves present implementation, not that it existed in a historical interval. Historical reports prove their recorded observations, not present health. Test counts are snapshots, never additive; distinguish focused/full, mocked/real-provider, browser/device, build and deployment. If not rerun, say so.

## 4. Reconstruct timeline

Cover every accessible phase in the requested interval, grouped by workstream. Record dates/confidence, goals, actual outputs, problems, decisions, failed attempts and causes, validation, next-phase influence and outstanding work. Check for missing initial failures before repairs, missing acceptance before releases and unexplained architecture changes. Preserve gaps rather than fabricate transitions.

For historical reports, separate interval-end status from current recheck date. For incremental runs, look beyond the prior cutoff AND recheck old open/closed issues for regressions or contradictory evidence.

## 5. Reconcile issues

Use stable P IDs. Match by symptom, affected component and confirmed cause; repeated symptoms with distinct causes need separate linked issues. Keep dated occurrences, hypotheses, attempts, changes, verification and release evidence. Record cause confidence as CONFIRMED, LIKELY or UNKNOWN. An issue can be test-verified while cause remains unknown; do not infer cause from passing tests.

Statuses: REPORTED, INVESTIGATING, ROOT_CAUSE_IDENTIFIED, FIX_IMPLEMENTED, TEST_VERIFIED, E2E_VERIFIED, RELEASED, PARTIALLY_RESOLVED, BLOCKED, UNRESOLVED, NOT_VERIFIED. These are evidence states, not a mandatory linear progression. Keep verified extent separately from current blocking/open state. A failed current check can reopen a released issue; append its history and retain prior release evidence. Not reproduced does not mean fixed. Partial resolution must name the remaining failure.

## 6. Index evidence and resolve conflicts

Give each source a stable E ID, a retrievable locator, source date (or unknown), observation date, revision/environment when relevant, supported claim and limits. Prefer direct implementation/runtime evidence for implementation/runtime claims; then commits/tests/releases, dated reports, history/handoffs/memory, user recollection, and inference. Evidence must match the claim: code does not prove user authorship, intention, actual deployment or historical performance.

Keep conflicting accounts, their E IDs and the reason for the adopted interpretation. Preserve failed experiments that affected decisions. Keep private locators in the private archive only; redact them in public-facing exports. The three records cite E IDs and each other instead of duplicating transcripts.

## Completeness gate

Before report generation, record checked/gap/not-applicable with evidence or explanation for each:

- available memory/history retrieval and pagination coverage;
- inception evidence or unknown start;
- all accessible phases in scope and independent workstreams;
- issues from errors, reports, tests, Git and conversations;
- failed attempts versus implemented/verified fixes;
- current status of every known issue, including unresolved/blocked/unverified;
- current implementation and Git state, unpublished work and validation limits;
- conflicts with older reports;
- gaps, unavailable sources and their impact;
- completed, partial and unresolved work shown separately.

On later runs append a dated investigation entry with interval, prior cutoff, source coverage, additions/corrections/reopened issues and next retrieval cursor. Rebuild the current full report from the records. Do not silently replace historical failures with latest successes. No automatic commits, pushes or public publication of project records without an explicit user request.
