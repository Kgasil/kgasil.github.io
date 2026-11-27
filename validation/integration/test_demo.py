import copy
import sys
import unittest
from pathlib import Path
from demo import build,verify,permissions,EDGES,ORDER,digest

ROOT=Path(__file__).resolve().parents[2]
SNAP=Path(sys.argv.pop(1))
CAT=(ROOT/"docs/graal-catalog.md").read_text(encoding="utf-8")
class DemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trace=build(SNAP,CAT,EDGES)
    def test_end_to_end(self):
        self.assertTrue(verify(self.trace,SNAP,CAT,EDGES))
        self.assertEqual([s["stage"] for s in self.trace["steps"]],list(ORDER))
    def test_explicit_approval(self):
        for grants in ([],EDGES[:-1],tuple(reversed(EDGES)),EDGES+("extra",)):
            with self.subTest(grants=grants),self.assertRaises(ValueError):
                build(SNAP,CAT,grants)
    def test_hash_chain(self):
        prior=None
        for step in self.trace["steps"]:
            self.assertEqual(step["previous_sha256"],prior)
            self.assertEqual(step["sha256"],digest({k:v for k,v in step.items() if k!="sha256"}))
            prior=step["sha256"]
    def test_tamper(self):
        t=copy.deepcopy(self.trace);t["steps"][1]["payload"]["metrics"][0]["value"]="99"
        with self.assertRaises(ValueError): verify(t,SNAP,CAT,EDGES)
    def test_rehashed_tamper(self):
        t=copy.deepcopy(self.trace);t["steps"][2]["payload"]["review"]["sensitive"]=1
        prior=None
        for s in t["steps"]:
            s["previous_sha256"]=prior;s["sha256"]=digest({k:v for k,v in s.items() if k!="sha256"});prior=s["sha256"]
        with self.assertRaises(ValueError): verify(t,SNAP,CAT,EDGES)
    def test_release(self):
        t=copy.deepcopy(self.trace);t["release_approved"]=True
        with self.assertRaises(ValueError): verify(t,SNAP,CAT,EDGES)
    def test_distribution_hold(self):
        altered=CAT.replace("GEN-03 | Mini Extension | 0.1.0 | SUSPENDED","GEN-03 | Mini Extension | 0.1.0 | MANUAL")
        self.assertNotEqual(altered,CAT)
        with self.assertRaises(ValueError): build(SNAP,altered,EDGES)
    def test_fixture_only(self):
        t=copy.deepcopy(self.trace);t["data_kind"]="personal"
        with self.assertRaises(ValueError): verify(t,SNAP,CAT,EDGES)
    def test_source_trace(self):
        for step in self.trace["steps"]:
            self.assertEqual(len(step["source"]["commit"]),40)
            self.assertEqual(len(step["source"]["sha256"]),64)
    def test_reconciliation(self):
        l=self.trace["steps"][-1]["payload"]
        self.assertEqual([m["value"] for m in l["metrics"]["metrics"]],[30000,18000,12000])
        self.assertEqual(l["pending_review"],1)
    def test_no_task_completion_claim(self):
        self.assertIs(self.trace["steps"][3]["payload"]["done"],False)
    def test_repeatable(self):
        self.assertEqual(self.trace,build(SNAP,CAT,EDGES))
if __name__=="__main__": unittest.main(verbosity=2)
