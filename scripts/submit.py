#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
WS_DIR = ROOT / "assignments"


def run_pytest(target: Path, out_json: Path) -> tuple[int, str]:
    cmd = [
        "pytest",
        "-q",
        str(target),
        "--import-mode=importlib",
        "--json-report",
        f"--json-report-file={out_json}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout + "\n" + proc.stderr


def git_commit_and_push(paths):
    def run(cmd):
        subprocess.run(cmd, check=True)

    run(["git", "add", "--"] + [str(p) for p in paths])
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    run(["git", "commit", "-m", f"experiment: results {ts}"])
    try:
        run(["git", "push", "-u", "origin", "HEAD"])
    except Exception:
        print("Push failed. You may need to set up credentials.")


def main():
    ap = argparse.ArgumentParser(description="Run tests for a round and archive results")
    ap.add_argument("participant_id")
    ap.add_argument("confidence", choices=["0", "1", "2", "3", "4", "5"])
    ap.add_argument("round", choices=["1", "2"])
    ap.add_argument("--push", action="store_true", help="Commit and push results to repository")
    args = ap.parse_args()

    pid = args.participant_id
    round_key = f"round{args.round}"
    confidence_score = args.confidence
    target = WS_DIR / round_key
    if not target.exists():
        raise SystemExit(f"Assignments for {round_key} not found at {target}.")

    out_dir = RESULTS_DIR / pid / round_key
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "results.json"
    code_dir = out_dir / "code"
    if code_dir.exists():
        shutil.rmtree(code_dir)

    # Run tests
    rc, logs = run_pytest(target, out_json)

    # Archive code and logs
    shutil.copytree(target, code_dir)
    (out_dir / "logs.txt").write_text(logs, encoding="utf-8")
    meta = {
        "participant_id": pid,
        "round": round_key,
        "exit_code": rc,
        "confidence_score": confidence_score,
        "submitted_at": datetime.utcnow().isoformat() + "Z",
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print(f"Saved results to {out_dir}")

    if args.push:
        git_commit_and_push([out_dir])


if __name__ == "__main__":
    main()

