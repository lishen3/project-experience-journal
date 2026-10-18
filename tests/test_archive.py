"""Synthetic regression cases; no actual project history is published."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_archive import validate_archive, STATUSES

META = '- Project: Synthetic project\n- Investigated-through: 2026-10-18\n- Updated: 2026-10-18\n'
ISSUE = '''## P001 Provider failure
- First-seen: unknown
- Status: UNRESOLVED
- Cause-confidence: UNKNOWN
- Symptom: Timeout
- Reproduction: Reported under complete payload
- Root-cause: unknown
- Attempts: Smaller payload; result inconclusive
- Fix: none
- Verification: Historical observation only
- Release: unknown
- Remaining-risk: Still times out
- History: 2026-10-04 reported; 2026-10-18 still unresolved
- Evidence: E001
'''
EVIDENCE = '''## E001 Observation
- Source-type: REPORT
- Locator: reports/provider.md section 2
- Source-date: 2026-10-04
- Observed-at: 2026-10-18
- Claim: Historical timeout reported
- Limits: Not rerun; cause unknown
'''
TIMELINE = '''## T001 Investigation
- Date: approximately early October; exact date unknown
- Date-basis: report timestamp, not project inception
- Workstream: Provider integration
- Goal: Obtain valid model output
- Decisions: Isolate format and timeout failures
- Outputs: Diagnostic report
- Problems: P001 remains open
- Validation: Historical report E001
- Next-impact: Restrict scope
- Outstanding: No verified release
- Evidence: E001

## Investigation 2026-10-18
- Coverage: requested interval checked; history tool unavailable; inception unknown
- Changes: baseline created; next step reproduce P001
'''


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.put('PROJECT_TIMELINE.md', TIMELINE)
        self.put('ISSUE_LEDGER.md', ISSUE)
        self.put('EVIDENCE_INDEX.md', EVIDENCE)

    def put(self, name, body):
        (self.root / name).write_text(META + body, encoding='utf-8')

    def test_a_agent_history_links_without_claiming_real_release(self):
        self.assertEqual(validate_archive(self.root), [])

    def test_b_python_modularization_and_git_are_not_user_authorship_proof(self):
        self.put('EVIDENCE_INDEX.md', EVIDENCE.replace('REPORT', 'GIT').replace('Historical timeout reported', 'Functions moved to modules; import corrected; commit exists; author contribution unknown'))
        self.put('PROJECT_TIMELINE.md', TIMELINE.replace('Provider integration', 'Functions / modules / import / Git initialization'))
        self.assertEqual(validate_archive(self.root), [])

    def test_c_unknown_start_and_inaccessible_history_allowed(self):
        self.put('EVIDENCE_INDEX.md', EVIDENCE.replace('Source-date: 2026-10-04', 'Source-date: unknown'))
        self.assertEqual(validate_archive(self.root), [])

    def test_d_open_states_preserved(self):
        for status in ('UNRESOLVED', 'BLOCKED', 'NOT_VERIFIED', 'PARTIALLY_RESOLVED'):
            with self.subTest(status=status):
                self.put('ISSUE_LEDGER.md', ISSUE.replace('Status: UNRESOLVED', f'Status: {status}'))
                self.assertEqual(validate_archive(self.root), [])
                self.assertIn(f'Status: {status}', (self.root / 'ISSUE_LEDGER.md').read_text())

    def test_statuses_all_supported(self):
        self.assertEqual(len(STATUSES), 11)

    def test_unit_evidence_cannot_prove_e2e_or_release(self):
        self.put('EVIDENCE_INDEX.md', EVIDENCE.replace('REPORT', 'TEST'))
        for status in ('E2E_VERIFIED', 'RELEASED'):
            self.put('ISSUE_LEDGER.md', ISSUE.replace('UNRESOLVED', status))
            self.assertTrue(validate_archive(self.root))

    def test_test_status_needs_test_evidence(self):
        self.put('ISSUE_LEDGER.md', ISSUE.replace('UNRESOLVED', 'TEST_VERIFIED'))
        self.assertTrue(validate_archive(self.root))
        self.put('EVIDENCE_INDEX.md', EVIDENCE.replace('REPORT', 'TEST'))
        self.assertEqual(validate_archive(self.root), [])

    def test_dangling_and_duplicate_ids(self):
        self.put('ISSUE_LEDGER.md', ISSUE.replace('Evidence: E001', 'Evidence: E099'))
        self.assertTrue(validate_archive(self.root))
        self.put('ISSUE_LEDGER.md', ISSUE + ISSUE)
        self.assertTrue(validate_archive(self.root))

    def test_incremental_reopen_retains_prior_history(self):
        history = '2026-10-10 TEST_VERIFIED E002; 2026-10-18 recurrence E001'
        self.put('ISSUE_LEDGER.md', ISSUE.replace('2026-10-04 reported; 2026-10-18 still unresolved', history))
        self.put('EVIDENCE_INDEX.md', EVIDENCE + EVIDENCE.replace('E001', 'E002').replace('REPORT', 'TEST'))
        self.assertEqual(validate_archive(self.root), [])
        self.assertIn(history, (self.root / 'ISSUE_LEDGER.md').read_text())

    def test_invalid_calendar_date(self):
        self.put('EVIDENCE_INDEX.md', EVIDENCE.replace('2026-10-04', '2026-02-30'))
        self.assertTrue(validate_archive(self.root))

    def test_confirmed_root_cause_required(self):
        self.put('ISSUE_LEDGER.md', ISSUE.replace('UNRESOLVED', 'ROOT_CAUSE_IDENTIFIED'))
        self.assertTrue(validate_archive(self.root))

    def test_unfilled_templates_rejected(self):
        self.put('EVIDENCE_INDEX.md', 'TO_FILL')
        self.assertTrue(validate_archive(self.root))


if __name__ == '__main__':
    unittest.main()
