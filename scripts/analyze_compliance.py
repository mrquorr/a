#!/usr/bin/env python3
"""
Analyze participant submissions for potential LLM policy violations.

This script provides heuristics to detect potential AI assistance in Round 1.
Note: These are indicators, not proof. Use with caution.
"""
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
EX_DIR = ROOT / "exercises"


def load_assignment(pid: str) -> dict:
    """Load assignment.json."""
    path = RESULTS_DIR / pid / "assignment.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def load_round_code(pid: str, round_num: str) -> dict:
    """Load code from submitted round."""
    code_dir = RESULTS_DIR / pid / f"round{round_num}" / "code"
    if not code_dir.exists():
        return {}
    
    code_files = {}
    for exercise_dir in code_dir.iterdir():
        if exercise_dir.is_dir():
            task_file = exercise_dir / "task.py"
            if task_file.exists():
                code_files[exercise_dir.name] = task_file.read_text(encoding="utf-8")
    return code_files


def analyze_code_quality(code: str) -> dict:
    """Analyze code for AI-like patterns."""
    indicators = {
        "has_docstrings": "'''" in code or '"""' in code,
        "has_type_hints": "->" in code or ":" in code.split("\n")[0] if code else False,
        "has_comments": "#" in code,
        "line_count": len(code.split("\n")),
        "complexity_indicators": sum([
            "def " in code,
            "class " in code,
            "import " in code,
            "try:" in code,
            "except" in code,
        ]),
    }
    return indicators


def compare_rounds(pid: str) -> dict:
    """Compare Round 1 vs Round 2 code quality."""
    assignment = load_assignment(pid)
    if not assignment:
        return {}
    
    round1_code = load_round_code(pid, "1")
    round2_code = load_round_code(pid, "2")
    
    if not round1_code or not round2_code:
        return {"error": "Missing submissions"}
    
    analysis = {
        "participant_id": pid,
        "round1_quality": {},
        "round2_quality": {},
        "differences": {},
    }
    
    # Analyze each exercise
    for ex_name in round1_code.keys():
        if ex_name in round2_code:
            r1_analysis = analyze_code_quality(round1_code[ex_name])
            r2_analysis = analyze_code_quality(round2_code[ex_name])
            
            analysis["round1_quality"][ex_name] = r1_analysis
            analysis["round2_quality"][ex_name] = r2_analysis
            
            # Calculate differences
            diff = {
                "docstring_diff": r2_analysis["has_docstrings"] - r1_analysis["has_docstrings"],
                "type_hints_diff": r2_analysis["has_type_hints"] - r1_analysis["has_type_hints"],
                "line_count_diff": r2_analysis["line_count"] - r1_analysis["line_count"],
            }
            analysis["differences"][ex_name] = diff
    
    return analysis


def check_timing_patterns(pid: str) -> dict:
    """Check timing patterns that might indicate AI use."""
    assignment = load_assignment(pid)
    if not assignment:
        return {}
    
    round1_meta = RESULTS_DIR / pid / "round1" / "meta.json"
    round2_meta = RESULTS_DIR / pid / "round2" / "meta.json"
    
    timing = {}
    
    if round1_meta.exists():
        r1_data = json.loads(round1_meta.read_text(encoding="utf-8"))
        timing["round1_submitted"] = r1_data.get("submitted_at")
    
    if round2_meta.exists():
        r2_data = json.loads(round2_meta.read_text(encoding="utf-8"))
        timing["round2_submitted"] = r2_data.get("submitted_at")
    
    if timing.get("round1_submitted") and timing.get("round2_submitted"):
        try:
            r1_time = datetime.fromisoformat(timing["round1_submitted"].replace("Z", "+00:00"))
            r2_time = datetime.fromisoformat(timing["round2_submitted"].replace("Z", "+00:00"))
            time_diff = (r2_time - r1_time).total_seconds() / 3600  # hours
            timing["time_between_rounds_hours"] = time_diff
            
            # Flag if Round 2 was completed suspiciously fast
            if time_diff < 0.5:  # Less than 30 minutes
                timing["warning"] = "Round 2 completed very quickly after Round 1"
        except Exception as e:
            timing["error"] = str(e)
    
    return timing


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Analyze participant compliance with LLM policy")
    ap.add_argument("participant_id", nargs="?", help="Specific participant ID (or analyze all)")
    ap.add_argument("--output", "-o", help="Output JSON file")
    args = ap.parse_args()
    
    if args.participant_id:
        participants = [args.participant_id]
    else:
        # Analyze all participants
        participants = []
        if RESULTS_DIR.exists():
            for pid_dir in RESULTS_DIR.iterdir():
                if pid_dir.is_dir() and (pid_dir / "assignment.json").exists():
                    participants.append(pid_dir.name)
    
    if not participants:
        print("No participants found.")
        return 1
    
    results = []
    
    for pid in sorted(participants):
        print(f"\nAnalyzing {pid}...")
        
        assignment = load_assignment(pid)
        if not assignment:
            continue
        
        analysis = {
            "participant_id": pid,
            "code_analysis": compare_rounds(pid),
            "timing_analysis": check_timing_patterns(pid),
            "policy": assignment.get("allow_llm", {}),
        }
        
        results.append(analysis)
        
        # Print summary
        code_analysis = analysis.get("code_analysis", {})
        if "differences" in code_analysis:
            print(f"  Code quality differences detected:")
            for ex, diff in code_analysis["differences"].items():
                if diff.get("docstring_diff", 0) > 0:
                    print(f"    {ex}: More docstrings in Round 2 (possible AI use)")
                if diff.get("type_hints_diff", 0) > 0:
                    print(f"    {ex}: More type hints in Round 2 (possible AI use)")
        
        timing = analysis.get("timing_analysis", {})
        if timing.get("warning"):
            print(f"  ⚠️  {timing['warning']}")
    
    # Output results
    if args.output:
        import json
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Results saved to {args.output}")
    else:
        print("\n" + "=" * 60)
        print("Summary:")
        print(f"Analyzed {len(results)} participants")
        print("\nNote: These are heuristics, not proof of violations.")
        print("Use this data to identify cases for manual review.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

