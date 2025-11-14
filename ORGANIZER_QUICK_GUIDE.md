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
   - Repository URL: https://github.com/mrquorr/a
   - Tell them: "Create a Codespace, then run `bin/start <id> <yes|no>`"
   - Share PARTICIPANT_INSTRUCTIONS.md

## On Experiment Day

### Generate and share participant ID (3 digit starting in 001)

### For Participants (Share This):

**Participants test on their laptop**
1. Go to the repository: https://github.com/mrquorr/a
2. Click the green **"Code"** button
3. Select **"Create codespace on main"**
4. Wait 2-3 minutes for setup to complete
5. Run: `bin/start <your_id> <yes|no>` in the console ex.: `bin/start 999 yes`
6. Work on Round 1 (don't use AI for this round)
7. You can test your solution with `pytest assignments/round1/<assignment_to_test>` ex.: `pytest assignments/round1/medium-word_frequency`
8. When you finish Round 1 run `bin/submit1 <your_id> <your_confidence> --push` ex.: `bin/submit1 999 3 --push`
9. Run: `bin/round2 <your_id>` ex.: `bin/round2 999`
10. Work on Round 2 (you can use whatever AI youw ant for support here)
11. You can test your solution with `pytest assignments/round1/<assignment_to_test>` ex.: `pytest assignments/round1/medium-word_frequency`
12. When you finish Round 1 run `bin/submit2 <your_id> <your_confidence> --push`

**Participants test on tester laptop**
1. Run: `bin/start <your_id> <yes|no>` in the console ex.: `bin/start 999 yes`
2. Work on Round 1 (don't use AI for this round)
3. You can test your solution with `pytest assignments/round1/<assignment_to_test>` ex.: `pytest assignments/round1/medium-word_frequency`
4. When you finish Round 1 run `bin/submit1 <your_id> <your_confidence> --push` ex.: `bin/submit1 999 3 --push`
5. Run: `bin/round2 <your_id>` ex.: `bin/round2 999`
6. Work on Round 2 (you can use whatever AI youw ant for support here)
7. You can test your solution with `pytest assignments/round1/<assignment_to_test>` ex.: `pytest assignments/round1/medium-word_frequency`
8. When you finish Round 1 run `bin/submit2 <your_id> <your_confidence> --push`

Detailed instructions can be found in `PARTICIPANT_GUIDE.MD`

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

