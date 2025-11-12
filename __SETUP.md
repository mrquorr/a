# Production Setup Guide

This guide helps you prepare the repository for a live experiment with participants.

## Pre-Launch Checklist

### 1. Exercise Pool Validation

Run the validation script to ensure you have enough exercises:

```bash
bin/validate
```

**Requirements:**
- Minimum: 2 exercises per pool (for basic functionality)
- Recommended: 5+ exercises per pool (for variety)
- Each exercise must have:
  - `task.py` with function stubs
  - `tests/test_task.py` with pytest tests

### 2. Repository Access

**For Public Repository:**
- Repository is already accessible to everyone
- Share the repository URL: `https://github.com/libanmohamud-spec/a`

**For Private Repository:**
- Go to Settings → Collaborators
- Add participants as collaborators (Read access is sufficient)
- Or use GitHub Classroom for automated access

### 3. Test the Full Flow

Before launching, test with a sample participant:

```bash
# In a Codespace
bin/init test001 yes
bin/round1 test001
# ... work on exercises ...
bin/submit1 test001
bin/round2 test001
# ... work on exercises ...
bin/submit2 test001

# Verify results
ls results/test001/
cat results/test001/assignment.json
```

### 4. Documentation

Ensure participants have access to:
- `PARTICIPANT_INSTRUCTIONS.md` - **Quick reference (recommended for participants)**
- `QUICK_START.md` - Detailed step-by-step guide
- `README.md` - Full documentation
- `ORGANIZER_QUICK_GUIDE.md` - **Quick reference for organizers**

## Launch Steps

### Step 1: Final Validation

```bash
# Validate exercise pools
bin/validate

# Check repository is accessible
# (Test by creating a new Codespace)
```

### Step 2: Share Repository

Send participants:
1. Repository URL: `https://github.com/libanmohamud-spec/a`
2. **Quick instructions:** "Create Codespace → Run `bin/start <id> <yes|no>`"
3. Link to `PARTICIPANT_INSTRUCTIONS.md` for reference

### Step 3: Monitor Progress

- Check `results/` directory for participant submissions
- Run `bin/report` periodically to generate CSV summaries
- Monitor GitHub commits if participants use `--push`

### Step 4: Collect Results

After experiment completion:

```bash
# Generate final report
bin/report -o reports/final_results.csv

# Or aggregate manually
python scripts/aggregate_results.py -o reports/final_results.csv
```

## Post-Experiment

1. **Backup Results:**
   ```bash
   git add results/
   git commit -m "Experiment results"
   git push
   ```

2. **Generate Reports:**
   ```bash
   bin/report -o reports/experiment_summary.csv
   ```

3. **Archive Repository:**
   - Consider making repository read-only
   - Or archive it for future reference

## Troubleshooting

**Participants confused about setup:**
- Point them to `PARTICIPANT_INSTRUCTIONS.md`
- Use `bin/start` instead of separate commands (saves 5-10 minutes)
- See `ORGANIZER_QUICK_GUIDE.md` for common issues

**Participants can't access repository:**
- Check repository visibility settings
- Verify collaborator access (for private repos)
- Make sure they're signed in to GitHub

**Not enough exercises error:**
- Run `bin/validate` to see what's missing
- Add more exercises to the pools

**Results not saving:**
- Check `results/` directory permissions
- Ensure participants have write access

**Setup taking too long:**
- Use `bin/start` command (one command instead of multiple)
- Pre-assign participant IDs to avoid confusion
- Have `PARTICIPANT_INSTRUCTIONS.md` ready to share


## Support

For issues during the experiment:
- Check `README.md` troubleshooting section
- Review `PARTICIPANT_GUIDE.md` for common questions
- Check GitHub Issues (if enabled)

