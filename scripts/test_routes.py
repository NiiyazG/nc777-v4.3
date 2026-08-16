#!/usr/bin/env python3
"""Regression checks for NC777 routing fixtures. Uses stdlib only.
router-cases.yaml intentionally contains JSON, which is valid YAML 1.2.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "tests" / "router-cases.yaml").read_text(encoding="utf-8"))
errors=[]

def check(cond, msg):
    if not cond: errors.append(msg)

check(data.get("version") == "4.3", "fixture version must be 4.3")
cases={c["id"]: c for c in data.get("cases", [])}
required_ids={"docs_typo","small_bug","expected_tdd_red","implementation_gap","oauth_feature","failing_test","prod_incident","refactor","security_audit","agent_security","deploy_verified"}
check(required_ids <= set(cases), f"missing cases: {sorted(required_ids-set(cases))}")

for cid,c in cases.items():
    req=set(c.get("required", [])); forb=set(c.get("forbidden", []))
    check(not (req & forb), f"{cid}: role both required and forbidden: {req&forb}")

check(cases["expected_tdd_red"].get("failure_class")=="EXPECTED_RED", "expected_tdd_red class")
check("Pitbull" in cases["expected_tdd_red"].get("forbidden", []), "EXPECTED_RED must not route Pitbull")
check(cases["implementation_gap"].get("entry")=="Developer", "implementation gap routes Developer")
check("Pitbull" in cases["implementation_gap"].get("forbidden", []), "implementation gap must not require Pitbull")
check(cases["failing_test"].get("entry")=="Pitbull", "regression must enter Pitbull")
check(cases["prod_incident"].get("entry")=="Pitbull", "incident must enter Pitbull")
check(cases["docs_typo"].get("qa_fallback_without_architect") is True, "GREEN QA fallback required")
check(cases["agent_security"].get("playbook")=="llm-agent-security", "agent security playbook expected")

print(f"NC777 route tests: {len(errors)} error(s), {len(cases)} case(s)")
for e in errors: print("ERROR:", e)
raise SystemExit(1 if errors else 0)
