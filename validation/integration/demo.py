"""GRAAL synthetic demonstration v1. Fixed fixture; no real data or app installation."""
import argparse
import hashlib
import json
import runpy
import subprocess
from pathlib import Path
from graal import registry, rubedo_reference, lilium_synthetic_totals, require

ORDER=("genesis","rubedo","argus","aeris","lilium")
EDGES=tuple(f"{a}:{b}" for a,b in zip(ORDER,ORDER[1:]))
FIXTURE="queue-and-finance-demo-v1"
AERIS_COMMIT="d6e03bc428fa3506fe5ec06d243e14438722432e"
TEXT="Estudo fictício de filas: seis chegadas e dez atendimentos por hora."
CSV=b"date,revenue,cost\n2026-01-01,100.00,60.00\n2026-02-01,200.00,120.00\n"
FILES={"genesis":"extension/core.js","rubedo":"examples/reference-results.json","argus":"extension/core.js","aeris":"desktop/aeris/checklist.py","lilium":"core/metrics.py"}
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
def digest(x):
    return hashlib.sha256(canonical(x)).hexdigest()
def source(root,name):
    p=root/name/FILES[name]
    require(p.is_file() and not p.is_symlink(),"source_missing")
    commit=subprocess.check_output(["git","-C",str(root/name),"rev-parse","HEAD"],text=True).strip()
    require(len(commit)==40 and all(c in "0123456789abcdef" for c in commit),"invalid_commit")
    require(name!="aeris" or commit==AERIS_COMMIT,"aeris_commit")
    # Refuse modified source files; bind path and actual byte hash to checked out commit.
    expected=subprocess.check_output(["git","-C",str(root/name),"show",f"HEAD:{FILES[name]}"])
    actual=p.read_bytes()
    require(expected==actual,"source_modified")
    return {"project":name,"commit":commit,"path":FILES[name],"sha256":hashlib.sha256(actual).hexdigest()},p
def node_call(p, method, args):
    # Fixed methods only. JSON sent through stdin, never interpolated into JS source.
    require(method in {"reading","review"},"method")
    js="const fs=require('fs');const m=require(process.argv[1]);const args=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(m[process.argv[2]](...args)));"
    return json.loads(subprocess.check_output(["node","-e",js,str(p.resolve()),method],input=canonical(args),timeout=10))
def permissions(grants):
    require(type(grants) in (list,tuple) and tuple(grants)==EDGES,"explicit_ordered_approvals_required")
def build(root,catalog,grants):
    permissions(grants)
    states=registry(catalog)
    sources={n:source(root,n) for n in ORDER}
    steps=[]
    def append(name,payload):
        index=len(steps)
        require(ORDER[index]==name,"step_order")
        record={"stage":name,"fixture":FIXTURE,"data_kind":"synthetic","source":sources[name][0],"previous_sha256":steps[-1]["sha256"] if steps else None,"approved_transfer":EDGES[index-1] if index else None,"payload":payload}
        steps.append({**record,"sha256":digest(record)})
    g=node_call(sources["genesis"][1],"reading",[TEXT,180])
    require(type(g.get("count")) is int and g["count"]>0 and g.get("minutes")==1,"genesis_reading")
    append("genesis",{"reading_words":g["count"],"reading_minutes":g["minutes"],"queue_inputs":[6,10],"objective":"queue_wait_review"})
    ref=json.loads(sources["rubedo"][1].read_text(encoding="utf-8"))
    r=rubedo_reference(ref)
    require(steps[-1]["payload"]["queue_inputs"]==[6,10],"fixture_inputs")
    append("rubedo",r)
    a=node_call(sources["argus"][1],"review",[canonical(r).decode()])
    require(a=={"flags":[],"sensitive":0,"attention":"none"},"argus_review_required")
    append("argus",{"review":a,"reviewed_record_sha256":steps[-1]["sha256"]})
    require(steps[-1]["payload"]["review"]["attention"]=="none","review_block")
    wait=next(m["value"] for m in r["metrics"] if m["id"]=="queue.wait")
    require(wait=="9","unexpected_reference")
    store=runpy.run_path(str(sources["aeris"][1]))["ChecklistStore"]()
    name=store.create("Synthetic GRAAL")
    task=store.add(name,"Review queue waiting time")
    require(task.done is False and store.progress(name)==(0,1),"checklist_pending")
    append("aeris",{"task_id":task.id,"task_code":"review_queue_wait","done":task.done,"pending":1,"wait_min":wait})
    require(steps[-1]["payload"]["pending"]==1,"action_required")
    analyze=runpy.run_path(str(sources["lilium"][1]))["analyze_csv"]
    l=lilium_synthetic_totals(analyze(CSV))
    append("lilium",{"metrics":l,"fixture_relation":"independent_finance_example_not_queue_forecast","pending_review":1})
    return {"schema":"graal.demo.trace.v1","fixture":FIXTURE,"data_kind":"synthetic","release_approved":False,"grants":list(grants),"catalog_sha256":digest(states),"steps":steps}
def verify(trace,root,catalog,grants):
    # Recompute from fixed sources; a hash chain alone is not authentication.
    require(trace==build(root,catalog,grants),"trace_mismatch")
    return True
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("snapshots",type=Path)
    p.add_argument("catalog",type=Path)
    p.add_argument("output",type=Path)
    p.add_argument("--approve",action="append",default=[])
    a=p.parse_args()
    cat=a.catalog.read_text(encoding="utf-8")
    trace=build(a.snapshots,cat,a.approve)
    verify(trace,a.snapshots,cat,a.approve)
    a.output.write_text(json.dumps(trace,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("GRAAL trace PASS: 5 source stages, 4 explicit synthetic grants, no release approval.")
if __name__=="__main__":
    main()
