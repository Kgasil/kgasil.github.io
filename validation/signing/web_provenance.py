"""Build a public site provenance manifest, not a malware or identity certification."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

root = Path.cwd()
files = ["index.html", "distribuicao.html", "portfolio/index.html", "portfolio/cases.html",
         "portfolio/lab.html", "portfolio/resume.html", "portfolio/shared.css"]
result = {"schema": "graal.web-provenance.v1", "repository": os.environ["GITHUB_REPOSITORY"],
          "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
          "workflow_run": os.environ["GITHUB_RUN_ID"],
          "scope": "Source file snapshot only; not Windows code signing or malware clearance.",
          "files": [{"path": p, "sha256": hashlib.sha256((root / p).read_bytes()).hexdigest(),
                     "bytes": (root / p).stat().st_size} for p in files]}
out = Path(os.environ["RUNNER_TEMP"]) / "graal-web-provenance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(out.read_text())
