#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EX_DIR = ROOT / "exercises"
RESULTS_DIR = ROOT / "results"
WS_DIR = ROOT / "assignments"


def copytree(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main():
    ap = argparse.ArgumentParser(description="Prepare workspace for a specific round")
    ap.add_argument("participant_id")
    ap.add_argument("round", choices=["1", "2"])
    args = ap.parse_args()

    pid = args.participant_id
    round_key = f"round{args.round}"

    meta_path = RESULTS_DIR / pid / "assignment.json"
    if not meta_path.exists():
        raise SystemExit(f"Assignment plan not found at {meta_path}. Run scripts/setup_session.py first.")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    picks = meta["assignments"][round_key]
    target = WS_DIR / round_key
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    for item in picks:
        pool = item["pool"]
        name = item["exercise"]
        src = EX_DIR / pool / name
        dst = target / f"{pool}-{name}"
        copytree(src, dst)

    # Write round README
    llm_allowed = meta['allow_llm'][round_key]
    policy_note = ""
    if not llm_allowed:
        policy_note = """

⚠️  IMPORTANT: LLM assistance is NOT allowed in this round.
   - Do NOT use ChatGPT, Copilot, or other AI tools
   - Work independently
   - Violations may invalidate your results
"""
    else:
        policy_note = """

✅ LLM assistance is ALLOWED in this round.
   - You may use ChatGPT, Copilot, or other AI tools
   - Feel free to get AI help with your solutions
"""
    
    (target / "README.md").write_text(
        f"""
Round {args.round} Assignments
============================

Solve each exercise. To run tests from repo root:

  pytest -q assignments/{round_key} --json-report --json-report-file tmp_results.json

When ready, submit using:

  python scripts/submit.py {pid} {args.round}
{policy_note}
""".strip()
    )

    print(f"Prepared {target}")


if __name__ == "__main__":
    main()

