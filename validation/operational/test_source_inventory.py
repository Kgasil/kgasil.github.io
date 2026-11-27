import tempfile
import unittest
from pathlib import Path
import subprocess
from source_inventory import parse_requirements, inventory

class InventoryTests(unittest.TestCase):
    def test_pins_and_include(self):
        self.assertEqual(parse_requirements("# test\n-r requirements.txt\nexample==1.2.3\n"),[{"kind":"include","path":"requirements.txt"},{"kind":"pin","name":"example","version":"1.2.3"}])
    def test_unpinned(self):
        with self.assertRaises(ValueError): parse_requirements("example>=1")
    def test_remote(self):
        with self.assertRaises(ValueError): parse_requirements("-r https://example.invalid/file")
    def test_escape(self):
        with self.assertRaises(ValueError): parse_requirements("-r ../requirements.txt")
    def test_tracked_only(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            subprocess.run(["git","init","-q",d],check=True)
            (root/"requirements.txt").write_text("example==1.0\n")
            (root/"NOTICE").write_text("synthetic notice")
            (root/"requirements-untracked.txt").write_text("ignored==2.0")
            subprocess.run(["git","-C",d,"add","requirements.txt","NOTICE"],check=True)
            subprocess.run(["git","-C",d,"-c","user.name=Test","-c","user.email=test@example.invalid","commit","-qm","fixture"],check=True)
            r=inventory(root)
            self.assertEqual(len(r["dependency_declarations"]),1)
            self.assertEqual(len(r["license_notice_files"]),1)
            self.assertTrue(r["root_license_notice_present"])
            self.assertEqual(r["license_clearance"],"NOT_TESTED")
if __name__=="__main__":
    unittest.main(verbosity=2)
