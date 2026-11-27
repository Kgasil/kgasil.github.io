"""GRAAL v1 interoperability reference, offline and synthetic only."""
import argparse
import json
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path

PROJECTS = {"GEN":"genesis","RUB":"rubedo","ARG":"argus","AER":"aeris","LIL":"lilium"}
STATES = {"WEB","MANUAL","PREVIEW","CONTROLLED","SUSPENDED"}
REQUIRED = {"GEN-03":"SUSPENDED","ARG-03":"SUSPENDED","AER-03":"PREVIEW","LIL-03":"CONTROLLED"}
SCHEMA = "graal.metric.v1"
MAX_BYTES = 16384
METRICS = {
    ("rubedo","queue.wait"): ("min","decimal"),
    ("rubedo","queue.total"): ("min","decimal"),
    ("lilium","revenue"): ("BRL_cent","integer"),
    ("lilium","cost"): ("BRL_cent","integer"),
    ("lilium","result"): ("BRL_cent","integer"),
}
def require(ok, code):
    if not ok:
        raise ValueError(code)

def registry(markdown):
    rows = []
    for line in markdown.splitlines():
        if not re.match(r"^\| (GEN|RUB|ARG|AER|LIL)-[0-9]{2} \|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        require(len(cells)==6,"catalog_row")
        ident,name,version,state,link,limit = cells
        match = re.fullmatch(r"\[[^\]]+\]\((https://[^ )]+)\)",link)
        require(match is not None and state in STATES,"catalog_state_or_link")
        url = match.group(1)
        require(url.startswith(("https://kgasil.github.io/","https://github.com/Kgasil/")),"catalog_origin")
        rows.append({"id":ident,"project":PROJECTS[ident[:3]],"name":name,"version":version,"distribution":state,"reference":url,"limitations":limit})
    ids = {r["id"]:r for r in rows}
    require(len(ids)==len(rows) and len(rows)>=15,"catalog_ids")
    require(set(r["project"] for r in rows)==set(PROJECTS.values()),"catalog_projects")
    for ident,state in REQUIRED.items():
        require(ident in ids and ids[ident]["distribution"]==state,"distribution_gate_changed")
    return {"schema":"graal.catalog.v1","source":"docs/graal-catalog.md","release_approved":False,"components":rows}

def validate(record):
    require(type(record) is dict and set(record)=={"schema","source","source_schema","data_kind","metrics"},"record_fields")
    require(record["schema"]==SCHEMA and record["data_kind"]=="synthetic","record_schema_or_data")
    source=record["source"]
    require(type(source) is str and source in {"rubedo","lilium"},"source")
    require(record["source_schema"]=={"rubedo":"rubedo.reference.results.v1","lilium":"1.0"}[source],"source_schema")
    values=record["metrics"]
    require(type(values) is list and 1<=len(values)<=5,"metric_count")
    seen=set()
    for item in values:
        require(type(item) is dict and set(item)=={"id","unit","value"},"metric_fields")
        ident=item["id"]
        require(type(ident) is str and (source,ident) in METRICS and ident not in seen,"metric_id")
        seen.add(ident)
        unit,kind=METRICS[(source,ident)]
        require(item["unit"]==unit,"metric_unit")
        value=item["value"]
        if kind=="integer":
            require(type(value) is int and abs(value)<=10**16,"metric_integer")
            require(ident=="result" or value>=0,"metric_negative")
        else:
            require(type(value) is str and re.fullmatch(r"[0-9]{1,12}(\.[0-9]{1,12})?",value) is not None,"metric_decimal")
            require(Decimal(value).is_finite(),"metric_finite")
    return record

def make(source,source_schema,metrics):
    return validate({"schema":SCHEMA,"source":source,"source_schema":source_schema,"data_kind":"synthetic","metrics":[{"id":i,"unit":u,"value":v} for i,u,v in metrics]})

def rubedo_reference(document):
    require(document.get("schema")=="rubedo.reference.results.v1" and document.get("data")=="synthetic","rubedo_schema")
    cases=[c for c in document["cases"] if c.get("id")=="queue"]
    require(len(cases)==1 and cases[0]["result"]["stable"] is True,"rubedo_case")
    result=cases[0]["result"]
    # This pinned reference case expresses W/Wq in minutes; do not infer units for other cases.
    require(cases[0]["inputs"]==[6,10],"rubedo_case_inputs")
    return make("rubedo",document["schema"],[("queue.wait","min",str(result["Wq"])),("queue.total","min",str(result["W"]))])

def lilium_synthetic_totals(document):
    # Caller must supply the result of the fixed synthetic fixture, not an arbitrary user export.
    require(document.get("schema_version")=="1.0" and document.get("currency")=="BRL","lilium_schema")
    t=document["totals"]
    require(all(type(t[k]) is int for k in ("revenue_cents","cost_cents","result_cents")),"lilium_cents")
    require(t["result_cents"]==t["revenue_cents"]-t["cost_cents"],"lilium_reconciliation")
    return make("lilium","1.0",[(k,"BRL_cent",t[k+"_cents"]) for k in ("revenue","cost","result")])

def load_record(path):
    raw=Path(path).read_bytes()
    require(len(raw)<=MAX_BYTES,"record_size")
    def unique(pairs):
        out={}
        for k,v in pairs:
            require(k not in out,"duplicate_key")
            out[k]=v
        return out
    return validate(json.loads(raw,object_pairs_hook=unique,parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite"))))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    cat=sub.add_parser("registry")
    cat.add_argument("catalog",type=Path)
    cat.add_argument("output",type=Path)
    val=sub.add_parser("validate")
    val.add_argument("record",type=Path)
    args=parser.parse_args()
    if args.command=="registry":
        args.output.write_text(json.dumps(registry(args.catalog.read_text(encoding="utf-8")),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    else:
        load_record(args.record)
        print("Contract PASS; synthetic-only metadata, not security or release approval.")
if __name__=="__main__":
    main()
