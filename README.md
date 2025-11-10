GitHub Codespaces Setup for Disposable Python Exercises
======================================================

This repo is configured to run your two‑round coding experiment inside a fresh GitHub Codespace per participant.

What you get
- Isolated, disposable environment per participant (Codespace).
- Deterministic exercise sampling per participant ID.
- Round 1 (LLM not allowed) and Round 2 (LLM allowed) workflow.
- One‑command submission that runs tests and archives results under `results/` (optional auto‑push).

Quick start (as organizer)
1) Ensure there are at least 5 exercises per pool under:
   - `exercises/easy/*`
   - `exercises/medium/*`
   - `exercises/hard/*`
   Each exercise should be a folder with:
   - `task.py` (starter or solution stub)
   - `tests/test_task.py` (pytest tests, can include hidden tests)

2) Commit and push to GitHub.

3) Click “Code” → “Create codespace on main”.

Participant flow
1) Initialize session (once per participant):
   - `bin/init <participant_id> <yes|no>`
     - Example: `bin/init p001 yes`
     - Writes the exercise plan to `results/<participant_id>/assignment.json`.

2) Round 1 setup:
   - `bin/round1 <participant_id>`
   - Work in `assignments/round1/*`.

3) Round 1 submit:
   - `bin/submit1 <participant_id> [--push]`
   - Saves results to `results/<participant_id>/round1/` (and commits/pushes if `--push`).

4) Round 2 setup (LLM allowed):
   - `bin/round2 <participant_id>`
   - Work in `assignments/round2/*`.

5) Round 2 submit:
   - `bin/submit2 <participant_id> [--push]`

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

