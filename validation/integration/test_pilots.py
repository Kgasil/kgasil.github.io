import copy
import runpy
import sys
import unittest
from pathlib import Path
from demo import source
from pilots import build,verify,GRANTS,route_events,EVENTS

SNAP=Path(sys.argv.pop(1))
CAT=(Path(__file__).resolve().parents[2]/"docs/graal-catalog.md").read_text(encoding="utf-8")
class PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=build(SNAP,CAT,GRANTS)
        cls.store=runpy.run_path(str(source(SNAP,"aeris")[1]))["ChecklistStore"]
    def test_reproduce(self):
        self.assertTrue(verify(self.report,SNAP,CAT,GRANTS))
    def test_approval(self):
        for grant in ([],GRANTS[:-1],tuple(reversed(GRANTS))):
            with self.assertRaises(ValueError): build(SNAP,CAT,grant)
    def test_bi_totals(self):
        p=self.report["pilots"][0]
        self.assertEqual([m["value"] for m in p["metrics"]["metrics"]],[350000,220000,130000])
        self.assertEqual(p["margin_pct"],"37.14")
    def test_bi_months(self):
        self.assertEqual([m["result_cents"] for m in self.report["pilots"][0]["months"]],[55000,75000])
    def test_process(self):
        p=self.report["pilots"][1]
        self.assertEqual((p["events"],p["unique_tasks"],p["duplicates_suppressed"],p["completed"],p["cleanup_remaining"]),(5,3,2,0,0))
    def test_process_denied(self):
        s=self.store()
        with self.assertRaises(ValueError): route_events(s,EVENTS,False)
        self.assertEqual(s.names(),())
    def test_process_conflict(self):
        s=self.store()
        with self.assertRaises(ValueError): route_events(s,(("EV01","A"),("EV01","B")),True)
        self.assertEqual(s.names(),())
    def test_process_rollback(self):
        s=self.store()
        with self.assertRaises(ValueError): route_events(s,(("EV01","A"),("EV02","x"*201)),True)
        self.assertEqual(s.names(),())
    def test_governance(self):
        p=self.report["pilots"][2]
        self.assertEqual((p["review_required"],p["fixture_matches"],p["autonomous_approvals"]),(4,8,0))
        self.assertEqual([c["case"] for c in p["cases"] if c["observed_review"]],["G05","G06","G07","G08"])
    def test_no_raw_governance_input(self):
        import json
        s=json.dumps(self.report)
        self.assertNotIn("fictional@example.invalid",s)
        self.assertNotIn("SYNTHETIC_PLACEHOLDER",s)
    def test_tamper(self):
        p=copy.deepcopy(self.report);p["pilots"][0]["margin_pct"]="99"
        with self.assertRaises(ValueError): verify(p,SNAP,CAT,GRANTS)
    def test_no_release_or_customer(self):
        self.assertIs(self.report["release_approved"],False)
        self.assertIs(self.report["customer_engagement"],False)
    def test_hold(self):
        changed=CAT.replace("GEN-03 | Mini Extension | 0.1.0 | SUSPENDED","GEN-03 | Mini Extension | 0.1.0 | MANUAL")
        self.assertNotEqual(changed,CAT)
        with self.assertRaises(ValueError): build(SNAP,changed,GRANTS)
if __name__=="__main__": unittest.main(verbosity=2)
