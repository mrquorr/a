#!/usr/bin/env python3
"""
Optional LLM policy enforcement script for Round 1.

This script can be run in Round 1 to block common LLM services.
Note: This is a best-effort approach and can be bypassed by determined users.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"


def block_llm_services():
    """Block access to common LLM service domains."""
    # Common LLM service domains
    blocked_domains = [
        "api.openai.com",
        "chat.openai.com",
        "openai.com",
        "api.anthropic.com",
        "claude.ai",
        "anthropic.com",
        "bard.google.com",
        "generativelanguage.googleapis.com",
        "copilot.github.com",
        "githubcopilot.com",
        "copilot.microsoft.com",
    ]
    
    print("⚠️  Round 1: LLM services are NOT allowed")
    print("Blocking access to common LLM services...")
    print("\nNote: This is a best-effort block and can be bypassed.")
    print("Please honor the policy and work independently for Round 1.\n")
    
    # Try to modify /etc/hosts (requires sudo)
    hosts_file = Path("/etc/hosts")
    if hosts_file.exists():
        try:
            # Read current hosts
            with open(hosts_file, "r") as f:
                hosts_content = f.read()
            
            # Check if already blocked
            if "127.0.0.1 api.openai.com" in hosts_content:
                print("LLM services already blocked in /etc/hosts")
                return
            
            # Add blocks (requires sudo)
            print("To block LLM services, run:")
            print("sudo bash -c 'echo \"\" >> /etc/hosts'")
            for domain in blocked_domains:
                print(f"sudo bash -c 'echo \"127.0.0.1 {domain}\" >> /etc/hosts'")
            print("\nOr manually edit /etc/hosts and add:")
            for domain in blocked_domains:
                print(f"127.0.0.1 {domain}")
        except PermissionError:
            print("⚠️  Cannot modify /etc/hosts without sudo privileges")
            print("Consider using Codespaces network policies instead.")
    else:
        print("⚠️  /etc/hosts not found (Windows?)")
        print("Use Windows hosts file or Codespaces network policies.")


def check_round_policy(participant_id: str, round_num: str):
    """Check if LLM is allowed for this round."""
    assignment_path = RESULTS_DIR / participant_id / "assignment.json"
    if not assignment_path.exists():
        print(f"Assignment not found for {participant_id}")
        return None
    
    import json
    assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
    round_key = f"round{round_num}"
    return assignment.get("allow_llm", {}).get(round_key, False)


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Enforce LLM policy for Round 1")
    ap.add_argument("participant_id", help="Participant ID")
    ap.add_argument("--round", choices=["1", "2"], default="1", help="Round number")
    args = ap.parse_args()
    
    allowed = check_round_policy(args.participant_id, args.round)
    
    if allowed:
        print(f"✅ Round {args.round}: LLM assistance is ALLOWED")
        print("You may use ChatGPT, Copilot, or other AI tools.")
    else:
        print(f"🚫 Round {args.round}: LLM assistance is NOT ALLOWED")
        print("Please work independently without AI assistance.")
        print("\nThis is enforced by honor code.")
        print("Violations may invalidate your results.")
        
        response = input("\nDo you want to block LLM services? (y/n): ")
        if response.lower() == 'y':
            block_llm_services()


if __name__ == "__main__":
    main()

