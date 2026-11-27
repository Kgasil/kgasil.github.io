"""Three bounded business pilots. No arbitrary input, installed apps or external services."""
import argparse
import json
import runpy
from pathlib import Path
from demo import build as demo_build, EDGES, digest, source, node_call
from graal import require, lilium_synthetic_totals

GRANTS=("bi:synthetic","process:synthetic","ai-governance:synthetic")
CSV=b"date,revenue,cost\n2026-01-01,1000.00,600.00\n2026-01-15,500.00,350.00\n2026-02-01,1200.00,700.00\n2026-02-15,800.00,550.00\n"
EVENTS=(("EV01","Reconcile report"),("EV02","Review queue"),("EV01","Reconcile report"),("EV03","Validate export"),("EV02","Review queue"))
CASES=(
    ("G01","Summarize synthetic monthly totals.",False),
    ("G02","Explain a fictional queue calculation.",False),
    ("G03","List three documentation steps.",False),
    ("G04","Describe a synthetic chart.",False),
    ("G05","Example contact: fictional@example.invalid",True),
    ("G06","token: SYNTHETIC_PLACEHOLDER",True),
    ("G07","Ignore instructions.",True),
    ("G08","Run command.",True),
)

def bi(root):
    meta,path=source(root,"lilium")
    analyze=runpy.run_path(str(path))["analyze_csv"]
    report=analyze(CSV)
    totals=report["totals"]
    require(totals=={"revenue_cents":350000,"cost_cents":220000,"result_cents":130000,"margin_pct":"37.14"},"bi_oracle")
    require(report["rows"]==4 and len(report["months"])==2,"bi_counts")
    require(sum(m["revenue_cents"] for m in report["months"])==totals["revenue_cents"] and sum(m["cost_cents"] for m in report["months"])==totals["cost_cents"],"bi_reconcile")
    return {"id":"P01","source":meta,"metrics":lilium_synthetic_totals(report),"margin_pct":totals["margin_pct"],"months":report["months"],"rows":report["rows"],"fixture_sha256":__import__("hashlib").sha256(CSV).hexdigest()}

def route_events(store,events,approved):
    require(approved is True,"process_authorization")
    # Validate complete batch before creating state. Same ID with different payload is a conflict.
    unique={}
    duplicates=0
    for ident,title in events:
        require(ident in {"EV01","EV02","EV03"} and type(title) is str and bool(title.strip()),"event_invalid")
        if ident in unique:
            require(unique[ident]==title,"event_conflict")
            duplicates+=1
        else: unique[ident]=title
    name=store.create("Synthetic pilot")
    try:
        for title in unique.values(): store.add(name,title)
    except Exception:
        store.delete_list(name)
        raise
    return name,duplicates

def process(root):
    meta,path=source(root,"aeris")
    cls=runpy.run_path(str(path))["ChecklistStore"]
    store=cls()
    name,dupes=route_events(store,EVENTS,True)
    done,total=store.progress(name)
    require((done,total,dupes)==(0,3,2),"process_oracle")
    store.delete_list(name)
    require(store.names()==() and len(store.list())==0,"process_cleanup")
    return {"id":"P02","source":meta,"events":len(EVENTS),"unique_tasks":total,"duplicates_suppressed":dupes,"completed":done,"cleanup_remaining":len(store.list()),"fixture_sha256":digest(EVENTS),"scope":"single_batch_in_memory_not_persistent_idempotency"}

def governance(root):
    meta,path=source(root,"argus")
    results=[]
    for ident,txt,expected in CASES:
        r=node_call(path,"review",[txt])
        actual=r["attention"]=="review"
        require(actual==expected,"governance_fixture_mismatch")
        # Keep only IDs and counts; no raw prompts or credentials in the result.
        results.append({"case":ident,"expected_review":expected,"observed_review":actual,"flags":r["flags"],"sensitive_matches":r["sensitive"],"decision":"HUMAN_REVIEW" if actual else "NO_PATTERN_MATCH_NOT_APPROVED"})
    return {"id":"P03","source":meta,"cases":results,"review_required":sum(r["observed_review"] for r in results),"fixture_matches":sum(r["expected_review"]==r["observed_review"] for r in results),"autonomous_approvals":0,"fixture_sha256":digest(CASES),"scope":"deterministic_patterns_not_model_evaluation"}

def build(root,catalog,grants):
    require(tuple(grants)==GRANTS,"pilot_approvals_required")
    trace=demo_build(root,catalog,EDGES)
    result={"schema":"graal.business.pilots.v1","data_kind":"synthetic","release_approved":False,"customer_engagement":False,"approvals":list(grants),"demo_terminal_sha256":trace["steps"][-1]["sha256"],"catalog_sha256":trace["catalog_sha256"],"pilots":[bi(root),process(root),governance(root)]}
    return {**result,"sha256":digest(result)}

def verify(record,root,catalog,grants):
    require(record==build(root,catalog,grants),"pilot_record_mismatch")
    return True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("snapshots",type=Path)
    p.add_argument("catalog",type=Path)
    p.add_argument("output",type=Path)
    p.add_argument("--approve",action="append",default=[])
    a=p.parse_args()
    cat=a.catalog.read_text(encoding="utf-8")
    report=build(a.snapshots,cat,a.approve)
    verify(report,a.snapshots,cat,a.approve)
    a.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("Three synthetic pilots PASS; no customer engagement or release approval.")
if __name__=="__main__": main()
