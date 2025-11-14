#!/usr/bin/env python3
"""
Aggregate results from all participants into a CSV report.

Reads results/<participant_id>/roundN/results.json files and produces
a consolidated CSV with participant ID, round, test results, etc.
"""
import argparse
import csv
import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def load_assignment(pid: str) -> dict:
    """Load assignment.json for a participant."""
    assignment_path = RESULTS_DIR / pid / "assignment.json"
    if not assignment_path.exists():
        return {}
    return json.loads(assignment_path.read_text(encoding="utf-8"))


def load_round_results(pid: str, round_num: str) -> dict:
    """Load results.json for a round."""
    results_path = RESULTS_DIR / pid / f"round{round_num}" / "results.json"
    if not results_path.exists():
        return {}
    return json.loads(results_path.read_text(encoding="utf-8"))


def load_round_meta(pid: str, round_num: str) -> dict:
    """Load meta.json for a round."""
    meta_path = RESULTS_DIR / pid / f"round{round_num}" / "meta.json"
    if not meta_path.exists():
        return {}
    return json.loads(meta_path.read_text(encoding="utf-8"))


def extract_test_summary(results_json: dict) -> dict:
    """Extract test summary from pytest JSON report."""
    if not results_json:
        return {
            "total_tests": 0,
            "confidence_score": 0,
            "passed": 0,
            "failed": 0,
            "errors": 0,
            "skipped": 0,
        }
    
    summary = results_json.get("summary", {})
    return {
        "total_tests": summary.get("total", 0),
        "passed": summary.get("passed", 0),
        "failed": summary.get("failed", 0),
        "errors": summary.get("error", 0),
        "skipped": summary.get("skipped", 0),
    }


def get_exercises_for_round(assignment: dict, round_num: str) -> str:
    """Get exercise names for a round as a comma-separated string."""
    if not assignment:
        return ""
    round_key = f"round{round_num}"
    exercises = assignment.get("assignments", {}).get(round_key, [])
    return ", ".join([f"{e['pool']}-{e['exercise']}" for e in exercises])


def main():
    ap = argparse.ArgumentParser(description="Aggregate participant results into CSV")
    ap.add_argument(
        "-o", "--output",
        default="reports/summary.csv",
        help="Output CSV file path (default: reports/summary.csv)"
    )
    args = ap.parse_args()
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Find all participants
    participants = []
    if RESULTS_DIR.exists():
        for pid_dir in RESULTS_DIR.iterdir():
            if pid_dir.is_dir() and (pid_dir / "assignment.json").exists():
                participants.append(pid_dir.name)
    
    participants.sort()
    
    if not participants:
        print("No participant results found.", file=sys.stderr)
        return 1
    
    # Collect data
    rows = []
    for pid in participants:
        assignment = load_assignment(pid)
        experienced = assignment.get("experienced", False)
        
        for round_num in ["1", "2"]:
            results_json = load_round_results(pid, round_num)
            meta = load_round_meta(pid, round_num)
            test_summary = extract_test_summary(results_json)
            print(meta)
            exercises = get_exercises_for_round(assignment, round_num)
            
            row = {
                "participant_id": pid,
                "experienced": "yes" if experienced else "no",
                "round": round_num,
                "round_confidence": meta["confidence_score"],
                "exercises": exercises,
                "total_tests": test_summary["total_tests"],
                "passed": test_summary["passed"],
                "failed": test_summary["failed"],
                "errors": test_summary["errors"],
                "skipped": test_summary["skipped"],
                "exit_code": meta.get("exit_code", ""),
                "submitted_at": meta.get("submitted_at", ""),
            }
            rows.append(row)
    
    # Write CSV
    if not rows:
        print("No results to aggregate.", file=sys.stderr)
        return 1
    
    fieldnames = [
        "participant_id",
        "experienced",
        "round",
        "round_confidence",
        "exercises",
        "total_tests",
        "passed",
        "failed",
        "errors",
        "skipped",
        "exit_code",
        "submitted_at",
    ]
    
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✅ Aggregated {len(rows)} result rows from {len(participants)} participants")
    print(f"   Output: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

