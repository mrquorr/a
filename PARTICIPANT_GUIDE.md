# Participant Guide

Welcome! This guide will help you complete the coding experiment.

## Getting Started

### Step 0: Participant ID

**Make sure you know your Participant ID, ask the organizer for one if you don't know it**

### Step 1: Open Your Codespace

1. Go to the repository: https://github.com/libanmohamud-spec/a
2. Click the green **"Code"** button
3. Select **"Create codespace on main"**
4. Wait 2-3 minutes for setup to complete

### Step 2: Initialize Your Session

Once your Codespace is ready, open the terminal and run:

```bash
bin/init <your_participant_id> <yes|no>
```

**Parameters:**
- `<your_participant_id>`: Your unique participant ID (e.g., `001`, `002`) ALL PARTICIPANT IDs ARE ONLY 3 NUMBERS
- `<yes|no>`: 
  - `yes` if you have programming experience
  - `no` if you're a beginner

**Example ID is 002 and candidate has programming experience:**
```bash
bin/init 002 yes
```

This will:
- Create your exercise assignment plan
- Show you which exercises you'll work on in each round

### Step 3: Round 1 - No LLM Assistance

**Setup Round 1:**
```bash
bin/round1 <your_participant_id>
```

**Work on exercises:**
- Your exercises are built and placed in `assignments/round1/`
- Each exercise folder contains:
  - `task.py` - Your code goes here
  - `tests/` - Test files (don't modify these) to verify solutions

**Test your solutions:**
```bash
pytest assignments/round1/ -v
```

**Submit Round 1:**
```bash
bin/submit1 <your_participant_id>
```

Or to automatically save and push results:
```bash
bin/submit1 <your_participant_id> --push
```

### Step 4: Round 2 - LLM Assistance Allowed

**Setup Round 2:**
```bash
bin/round2 <your_participant_id>
```

**Work on exercises:**
- Your exercises are in `assignments/round2/`
- **You may use LLM assistance** (ChatGPT, Copilot, etc.) for this round

**Test your solutions:**
```bash
pytest assignments/round2/ -v
```

**Submit Round 2:**
```bash
bin/submit2 <your_participant_id>
```

Or with auto-push:
```bash
bin/submit2 <your_participant_id> --push
```

## Important Notes

- **Round 1**: LLM assistance is **NOT allowed**. Please work independently.
- **Round 2**: LLM assistance **IS allowed**. Feel free to use AI tools.
- Your participant ID is given by the experiment organizers
- Your participant ID determines which exercises you get (same ID = same exercises)
- You have 10 minutes per exercise
- Results are automatically saved to `results/<your_participant_id>/`, but without --push they won't be uploaded

## Troubleshooting

**Tests won't run?**
- Make sure you're in the repository root directory
- Check that `task.py` files exist in your exercise folders

**Can't push results?**
- Run `gh auth login` in the terminal
- Or use the VS Code Source Control panel to commit/push

**Need help?**
- Check the main README.md for more details
- Contact the experiment organizer

## Quick Reference

```bash
# Initialize
bin/init <id> <yes|no>

# Round 1
bin/round1 <id>
# ... work on assignments/round1/ ...
bin/submit1 <id> [--push]

# Round 2  
bin/round2 <id>
# ... work on assignments/round2/ ...
bin/submit2 <id> [--push]
```

Good luck!

