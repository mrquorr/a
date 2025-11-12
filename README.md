GitHub Codespaces Setup for Disposable Python Exercises
======================================================

This repo is configured to run your two‑round coding experiment inside a fresh GitHub Codespace per participant.

What you get
- Isolated, disposable environment per participant (Codespace).
- Deterministic exercise sampling per participant ID.
- Round 1 (LLM not allowed) and Round 2 (LLM allowed) workflow.
- One‑command submission that runs tests and archives results under `results/` (optional auto‑push).

Quick start (as organizer)
1) Validate exercise pools:
   ```bash
   bin/validate
   ```
   This checks you have sufficient exercises (minimum 2 per pool, recommended 5+).

2) Ensure repository is accessible:
   - **For public repo:** Already accessible to everyone
   - **For private repo:** Add participants as collaborators:
     - Go to: Settings → Collaborators → Add people
     - Add each participant's GitHub username
     - Give them "Read" access (or "Write" if they need to push results)

3) Share with participants:
   - Repository URL: https://github.com/libanmohamud-spec/a
   - Tell them: "Click Code → Codespaces → Create codespace on main"
   - Share QUICK_START.md for step-by-step instructions

4) See PRODUCTION_SETUP.md for detailed launch checklist.

Participant flow (Streamlined)

**Quick Start (One Command):**
```bash
bin/start <participant_id> <yes|no>
```
This does everything: initializes session, sets up Round 1, and shows next steps.

**Or Step-by-Step:**
1) Initialize: `bin/init <participant_id> <yes|no>`
2) Round 1: `bin/round1 <participant_id>` → work in `assignments/round1/` → `bin/submit1 <participant_id>`
3) Round 2: `bin/round2 <participant_id>` → work in `assignments/round2/` → `bin/submit2 <participant_id>`

**See PARTICIPANT_INSTRUCTIONS.md for the fastest path.**

Notes
- Exercise selection:
  - If participant answered “yes” to experience: Round1 = Medium+Hard, Round2 = Medium+Hard.
  - If “no”: Round1 = Easy+Medium, Round2 = Easy+Medium.
  - Selection is random but deterministic per participant ID; no replacement across rounds within a pool.
- LLM policy is encoded in `results/<id>/assignment.json` as `allow_llm` (round1=false, round2=true). You can enforce it by policy, honor code, or additional network restrictions if desired.
- To customize packages, edit `requirements.txt` and rebuild the codespace (or let `postCreateCommand` install).

Organizer utilities
- Validate exercise pools: `bin/validate` (checks sufficient exercises and structure)
- Generate results report: `bin/report` (creates CSV summary from all participants)
- Generate report to custom path: `bin/report -o path/to/report.csv`

Optional: GitHub Action for automatic aggregation
- A workflow file (`.github/workflows/aggregate-results.yml`) is provided for automatic CSV generation
- Add it manually via GitHub UI (Actions → New workflow) due to OAuth scope restrictions
- Or run `bin/report` manually to generate `reports/summary.csv`

Troubleshooting
- If `pytest` fails to discover tests, ensure each exercise folder contains a `tests/` subfolder with test files named `test_*.py`.
- If pushing results fails, the user may need to set up repo permissions in the codespace (run `gh auth login` or use the VS Code Source Control UI).
- Run `bin/validate` before starting experiments to ensure pools have enough exercises.

