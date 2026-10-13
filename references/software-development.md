# Software development profile

Capture the useful subset of:

- requirement or defect addressed;
- architecture or implementation decision;
- affected component and behavior;
- tests added or executed;
- failure reproduced and root cause;
- performance, security, accessibility, or compatibility consideration;
- version or commit evidence;
- review feedback and revision;
- deployment or release status;
- remaining technical debt or blocker.

Before writing a chronology, identify the software project's strongest engineering signals:

- a business or safety risk translated into an enforceable contract;
- a difficult failure narrowed through controlled diagnosis;
- a meaningful tradeoff between capability, reliability, cost, latency, or scope;
- a boundary that prevents one component from assuming another component's authority;
- a result verified at the correct layer rather than inferred from a weaker signal;
- a scope reduction that made an MVP safe or genuinely testable.

For each selected signal, prefer a problem-solving chain:

`symptom -> risk -> investigation -> decision -> implementation -> verification -> remaining risk`

Distinguish at least these verification layers when relevant:

- static or type checking;
- unit tests;
- mocked component or API integration;
- browser, device, database, or end-to-end execution;
- real external provider verification;
- production deployment and post-deployment check.

Do not treat HTTP success, valid JSON, schema validation, authorization, tool invocation, database persistence, and user-visible success as interchangeable. State which boundary was actually crossed.

Describe observable behavior rather than raw file activity. “Implemented duplicate-request protection and verified idempotency” is more useful than “edited three files.”

Do not claim a feature is complete merely because code was written. State the verification performed and any missing checks.
