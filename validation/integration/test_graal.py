import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from graal import registry, validate, load_record, rubedo_reference, lilium_synthetic_totals

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS = Path(sys.argv[1]) if len(sys.argv)>1 else None
if SNAPSHOTS is not None:
    sys.argv.pop(1)

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.catalog=(ROOT/"docs/graal-catalog.md").read_text(encoding="utf-8")
        self.sample={"schema":"graal.metric.v1","source":"lilium","source_schema":"1.0","data_kind":"synthetic","metrics":[{"id":"revenue","unit":"BRL_cent","value":100}]}
    def test_registry(self):
        r=registry(self.catalog)
        self.assertGreaterEqual(len(r["components"]),16)
        self.assertFalse(r["release_approved"])
    def test_hold(self):
        with self.assertRaises(ValueError):
            registry(self.catalog.replace("GEN-03 | Mini Extension | 0.1.0 | SUSPENDED","GEN-03 | Mini Extension | 0.1.0 | MANUAL"))
    def test_valid(self):
        self.assertEqual(validate(self.sample),self.sample)
    def test_wrong_unit(self):
        self.sample["metrics"][0]["unit"]="BRL"
        with self.assertRaises(ValueError): validate(self.sample)
    def test_real_data(self):
        self.sample["data_kind"]="personal"
        with self.assertRaises(ValueError): validate(self.sample)
    def test_unknown_field(self):
        self.sample["raw_text"]="not allowed"
        with self.assertRaises(ValueError): validate(self.sample)
    def test_bool(self):
        self.sample["metrics"][0]["value"]=True
        with self.assertRaises(ValueError): validate(self.sample)
    def test_duplicate_metric(self):
        self.sample["metrics"].append(copy.deepcopy(self.sample["metrics"][0]))
        with self.assertRaises(ValueError): validate(self.sample)
    def test_duplicate_json_key(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/"bad.json"
            p.write_text('{"schema":"x","schema":"y"}',encoding="utf-8")
            with self.assertRaises(ValueError): load_record(p)
    def test_reconciliation(self):
        with self.assertRaises(ValueError):
            lilium_synthetic_totals({"schema_version":"1.0","currency":"BRL","totals":{"revenue_cents":100,"cost_cents":50,"result_cents":99}})
    def test_rubedo_real_reference(self):
        self.assertIsNotNone(SNAPSHOTS)
        doc=json.loads((SNAPSHOTS/"rubedo/examples/reference-results.json").read_text())
        r=rubedo_reference(doc)
        self.assertEqual([(m["id"],m["unit"],m["value"]) for m in r["metrics"]],[("queue.wait","min","9"),("queue.total","min","15")])
        (SNAPSHOTS/"rubedo-metrics.json").write_text(json.dumps(r,indent=2)+"\n")
    def test_lilium_real_engine(self):
        self.assertIsNotNone(SNAPSHOTS)
        import runpy
        analyze=runpy.run_path(str(SNAPSHOTS/"lilium/core/metrics.py"))["analyze_csv"]
        result=analyze(b"date,revenue,cost\n2026-01-01,100.00,60.00\n2026-02-01,200.00,120.00\n")
        r=lilium_synthetic_totals(result)
        self.assertEqual([m["value"] for m in r["metrics"]],[30000,18000,12000])
        (SNAPSHOTS/"lilium-metrics.json").write_text(json.dumps(r,indent=2)+"\n")

if __name__=="__main__":
    unittest.main(verbosity=2)
