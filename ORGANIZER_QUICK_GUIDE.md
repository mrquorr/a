# Organizer Quick Guide - Running Experiments Smoothly

## Pre-Experiment Setup (Do Once)

1. **Validate exercises:**
   ```bash
   bin/validate
   ```

2. **Make repository accessible:**
   - **Public:** Already done
   - **Private:** Add participants as collaborators (Settings → Collaborators)

3. **Share with participants:**
   - Repository URL: https://github.com/libanmohamud-spec/a
   - Tell them: "Create a Codespace, then run `bin/start <id> <yes|no>`"
   - Share PARTICIPANT_INSTRUCTIONS.md

## On Experiment Day

### For Participants (Share This):

**Super Quick Start:**
1. Open: https://github.com/libanmohamud-spec/a
2. Click "Code" → "Codespaces" → "Create codespace on main"
3. Wait 2 minutes
4. Run: `bin/start <your_id> <yes|no>`
5. Work on Round 1 (no AI) → Submit
6. Run: `bin/round2 <your_id>` → Work on Round 2 (AI allowed) → Submit

**Total setup time: ~2 minutes**

### For Organizers:

**Monitor Progress:**
```bash
# Check who has submitted
ls results/

# Generate progress report
bin/report -o progress.csv

# Check specific participant
cat results/<participant_id>/assignment.json
```

**Common Issues:**

1. **"Can't see repository":**
   - Add them as collaborator
   - Or make repo public

2. **"No codespace on main":**
   - They need to CREATE it (click "Create codespace on main")
   - This is normal - each person creates their own

3. **"Confused about what to do":**
   - Point them to PARTICIPANT_INSTRUCTIONS.md
   - Or have them run `bin/start` - it guides them through

## Post-Experiment

```bash
# Generate final report
bin/report -o final_results.csv

# Analyze compliance (optional)
bin/analyze-compliance -o compliance_report.json
```

## Time-Saving Tips

- **Use `bin/start`** instead of separate `bin/init` + `bin/round1` commands
- **Pre-assign participant IDs** to avoid confusion
- **Have PARTICIPANT_INSTRUCTIONS.md open** to share quickly
- **Monitor `results/` directory** to see who's submitted

## Expected Timeline

- **Setup:** 2-3 minutes per participant
- **Round 1:** 15-30 minutes (depends on exercises)
- **Round 2:** 10-20 minutes (with AI assistance)
- **Total:** ~30-60 minutes per participant

