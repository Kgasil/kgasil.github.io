"""Read-only source declaration inventory; not a complete SBOM or license clearance."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

PROJECTS = ("genesis","rubedo","argus","aeris","lilium","aeris-candidate")
PIN = re.compile(r"([A-Za-z0-9][A-Za-z0-9_.-]*)==([A-Za-z0-9][A-Za-z0-9_.!+~-]*)")
LICENSE = re.compile(r"^(license|licence|copying|notice|third-party-notices)([._-].*)?$",re.I)
MANIFESTS = {"package.json","package-lock.json","pyproject.toml","poetry.lock","uv.lock","Pipfile","Pipfile.lock","Cargo.toml","Cargo.lock","go.mod","go.sum"}
def require(ok, message):
    if not ok:
        raise ValueError(message)

def parse_requirements(text):
    entries=[]
    for raw in text.splitlines():
        line=raw.split("#",1)[0].strip()
        if not line:
            continue
        if line.startswith("-r "):
            value=line[3:].strip()
            require(re.fullmatch(r"[A-Za-z0-9_.-]+",value) is not None and value not in {".",".."},"unsupported include")
            entries.append({"kind":"include","path":value})
        else:
            m=PIN.fullmatch(line)
            require(m is not None,"unsupported or unpinned requirement")
            entries.append({"kind":"pin","name":m[1],"version":m[2]})
    return entries

def git(root,*args):
    return subprocess.check_output(["git","-C",str(root),*args])

def inventory(root):
    paths=git(root,"ls-files","-z").decode("utf-8").split("\0")
    dependencies=[]
    notices=[]
    for name in paths:
        if not name:
            continue
        p=PurePosixPath(name)
        if p.parts[0] in {"backups","downloads"}:
            continue
        is_req=p.name.startswith("requirements") and p.suffix==".txt"
        is_manifest=p.name in MANIFESTS
        is_notice=bool(LICENSE.fullmatch(p.name)) or any(x.lower()=="third-party-notices" for x in p.parts[:-1])
        if not (is_req or is_manifest or is_notice):
            continue
        f=root/name
        require(f.is_file() and not f.is_symlink() and f.resolve().is_relative_to(root.resolve()),"nonregular declaration")
        require(f.stat().st_size<=2*1024*1024,"oversize declaration")
        data=f.read_bytes()
        record={"path":name,"sha256":hashlib.sha256(data).hexdigest()}
        if is_req:
            try:
                record["entries"]=parse_requirements(data.decode("utf-8-sig"))
                record["status"]="DIRECT_DECLARATIONS"
            except (ValueError,UnicodeError):
                record["status"]="REVIEW_REQUIRED"
            dependencies.append(record)
        elif is_manifest:
            record["status"]="REVIEW_REQUIRED"
            dependencies.append(record)
        if is_notice:
            notices.append(record)
    return {"commit":git(root,"rev-parse","HEAD").decode().strip(),"dependency_declarations":dependencies,
            "license_notice_files":notices,"root_license_notice_present":any("/" not in x["path"] for x in notices),
            "transitive_resolution":"NOT_TESTED","license_clearance":"NOT_TESTED","artifact_sbom":"NOT_TESTED"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("snapshots",type=Path)
    p.add_argument("output",type=Path)
    a=p.parse_args()
    projects={n:inventory(a.snapshots/n) for n in PROJECTS}
    report={"schema":"graal.source-inventory.v1","scope":"tracked source declarations only, not resolved dependency or binary inventory","projects":projects,"release_approved":False}
    a.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    for n,r in projects.items():
        print(n,r["commit"],"declarations",len(r["dependency_declarations"]),"notices",len(r["license_notice_files"]),"root license/notice",r["root_license_notice_present"])
        for d in r["dependency_declarations"]:
            print(" ",d["path"],d["status"],"pins",sum(e["kind"]=="pin" for e in d.get("entries",[])))
    print("Release approved: false")
if __name__=="__main__":
    main()
