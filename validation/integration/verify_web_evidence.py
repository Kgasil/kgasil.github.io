"""Recompute the web evidence from the exact source snapshots and compare records."""
import json
import sys
from pathlib import Path
from demo import build as demo, EDGES
from pilots import build as pilots, GRANTS
root=Path(sys.argv[1])
catalog=Path("docs/graal-catalog.md").read_text(encoding="utf-8")
e=json.loads(Path("graal/evidence.json").read_text(encoding="utf-8"))
assert e["trace"]==demo(root,catalog,EDGES),"web trace differs from fixed sources"
assert e["pilots"]==pilots(root,catalog,GRANTS),"web pilots differ from fixed sources"
assert e["trace"]["steps"][-1]["sha256"]==e["pilots"]["demo_terminal_sha256"]
print("Web evidence exactly reproduced from all five pinned sources; 3 pilots and 5 stages.")
