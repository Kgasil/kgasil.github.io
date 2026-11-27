"""Validate recorded partial BOMs against the official pinned CycloneDX 1.5 schema.
Schema compliance is not completeness, licensing clearance or release approval.
"""
import argparse
import hashlib
import json
from pathlib import Path
from importlib.metadata import version
from jsonschema import Draft7Validator, FormatChecker
from referencing import Registry, Resource

SCHEMA_COMMIT="c320fc0f0b46873864927d9d5684eea7ba439728"
SCHEMAS={
    "bom-1.5.schema.json":"c149728127117c39317b795032ed6e9a92e2f950",
    "spdx.schema.json":"f04d013c74c48de35726e93e367f0f738f51135d",
    "jsf-0.82.schema.json":"f46bfb1e52731ad1280123ff3e2bd29bd18d4bc2",
}
EXPECTED={"genesis-source","rubedo-source","argus-source","aeris-source","aeris-candidate-source","lilium-source","aeris-build-environment","lilium-review-environment","lilium-build-environment"}

def unique(pairs):
    result={}
    for key,value in pairs:
        if key in result: raise ValueError("duplicate JSON key")
        result[key]=value
    return result

def parse(raw):
    return json.loads(raw,object_pairs_hook=unique,parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite")))

def require(ok,msg):
    if not ok: raise ValueError(msg)

def make_validator(root):
    registry=Registry()
    schemas={}
    for name,expected in SCHEMAS.items():
        raw=(root/name).read_bytes()
        blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        require(blob==expected,"schema blob mismatch: "+name)
        obj=parse(raw)
        Draft7Validator.check_schema(obj)
        schemas[name]=obj
        registry=registry.with_resource(obj["$id"],Resource.from_contents(obj))
    return Draft7Validator(schemas["bom-1.5.schema.json"],registry=registry,format_checker=FormatChecker())

def validate_bom(raw,validator):
    obj=parse(raw)
    validator.validate(obj)
    require(obj["specVersion"]=="1.5","unexpected version")
    props=obj["metadata"]["properties"]
    values={p["name"]:p["value"] for p in props}
    require(len(values)==len(props),"duplicate properties")
    for k,v in {"graal:completeness":"incomplete","graal:dependency_graph":"NOT_ESTABLISHED","graal:license_clearance":"NOT_TESTED","graal:release_approved":"false"}.items():
        require(values.get(k)==v,"scope gate: "+k)
    require(all(c["aggregate"]=="incomplete" for c in obj["compositions"]),"composition gate")
    refs=[c["bom-ref"] for c in obj["components"]]
    require(len(refs)==len(set(refs)),"duplicate bom-ref")
    return {"sha256":hashlib.sha256(raw).hexdigest(),"commit":obj["metadata"]["component"]["version"],"components":len(refs),"schema_validation":"PASS","completeness":"incomplete","license_clearance":"NOT_TESTED","release_approved":False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("schema_dir",type=Path)
    p.add_argument("bom_dir",type=Path)
    p.add_argument("output",type=Path)
    a=p.parse_args()
    validator=make_validator(a.schema_dir)
    paths=sorted(a.bom_dir.glob("*.cdx.json"))
    require({p.name.removesuffix(".cdx.json") for p in paths}==EXPECTED,"unexpected inventory set")
    records={p.name:validate_bom(p.read_bytes(),validator) for p in paths}
    # Exercise real schema rejection and independent institutional policy rejection.
    sample=parse(paths[0].read_bytes())
    invalid=dict(sample);invalid["bomFormat"]="invalid"
    require(not validator.is_valid(invalid),"schema negative control failed")
    sample["metadata"]["properties"]=[{**p,"value":"true"} if p["name"]=="graal:release_approved" else p for p in sample["metadata"]["properties"]]
    try: validate_bom(json.dumps(sample).encode(),validator)
    except ValueError as e: require(str(e)=="scope gate: graal:release_approved","wrong rejection")
    else: raise ValueError("policy negative control failed")
    report={"schema":"graal.sbom-validation.v1","official_schema_commit":SCHEMA_COMMIT,"schema_blobs":SCHEMAS,"validator_version":version("jsonschema"),"records":records,"negative_controls":2,"release_approved":False}
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    for name,r in records.items(): print(name,r["schema_validation"],r["components"],r["sha256"])
    print("Official schema PASS:",len(records),"BOMs; 2 negative controls PASS; release_approved=false")
if __name__=="__main__": main()
