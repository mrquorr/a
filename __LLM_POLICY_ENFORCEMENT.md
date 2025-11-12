# LLM Policy Enforcement Guide

This document explains how to regulate and enforce the LLM policy (Round 1: no AI, Round 2: AI allowed).

## Current Approach

### 1. Policy Communication (Current)

The system currently uses **honor code** with clear communication:

- **Assignment JSON**: Policy encoded in `results/<id>/assignment.json`
- **Round READMEs**: Each round's README clearly states the policy
- **Documentation**: README.md and PARTICIPANT_GUIDE.md explain the policy
- **Terminal reminders**: Scripts print policy reminders

### 2. Enforcement Options

#### Option A: Honor Code (Current - Recommended for most cases)

**Pros:**
- Simple and non-intrusive
- Trusts participants
- No technical barriers

**Cons:**
- Relies on participant honesty
- Cannot technically prevent violations

**Implementation:**
- Clear communication in all documentation
- Reminders in terminal output
- Policy encoded in assignment.json for auditing

#### Option B: Network Restrictions (Technical Enforcement)

**For Round 1, you can block LLM services:**

1. **Using Codespaces Network Policies:**
   - Go to repository Settings → Codespaces → Network policies
   - Block domains: `api.openai.com`, `chat.openai.com`, `api.anthropic.com`, etc.
   - Apply only to Round 1 Codespaces

2. **Using /etc/hosts blocking:**
   ```bash
   # Run in Round 1 Codespace
   bin/check-policy <participant_id> --round 1
   ```
   This will attempt to block common LLM domains.

**Limitations:**
- Can be bypassed (VPN, mobile hotspot, etc.)
- May block legitimate resources
- Requires technical setup

#### Option C: Post-Hoc Analysis (Detection)

**Analyze submissions for patterns:**

```bash
# Analyze all participants
bin/analyze-compliance

# Analyze specific participant
bin/analyze-compliance p001

# Save results to file
bin/analyze-compliance -o compliance_report.json
```

**What it detects:**
- Code quality differences between rounds
- Timing patterns (suspiciously fast Round 2)
- Style differences (docstrings, type hints, etc.)

**Note:** These are **heuristics**, not proof. Use for flagging cases for manual review.

## Recommended Approach

### For Academic/Research Experiments:

1. **Pre-Experiment:**
   - Clear written policy in consent form
   - Verbal reminder at start
   - Explain consequences of violations

2. **During Experiment:**
   - Honor code approach (current)
   - Optional: Network restrictions for Round 1
   - Monitor timing patterns

3. **Post-Experiment:**
   - Run compliance analysis: `bin/analyze-compliance`
   - Review flagged cases manually
   - Compare Round 1 vs Round 2 code quality
   - Check timing patterns

### Detection Heuristics

The `analyze_compliance.py` script checks for:

1. **Code Quality Differences:**
   - Round 2 has significantly more docstrings
   - Round 2 has type hints, Round 1 doesn't
   - Round 2 code is more "polished"

2. **Timing Patterns:**
   - Round 2 completed suspiciously fast
   - Very short time between rounds

3. **Style Consistency:**
   - Round 1 and Round 2 code styles are very different
   - Round 2 code matches common AI patterns

## Implementation Steps

### Step 1: Set Up Network Restrictions (Optional)

If you want technical enforcement for Round 1:

1. **In Codespaces Settings:**
   - Repository → Settings → Codespaces
   - Configure network policies
   - Block LLM service domains

2. **Or use the enforcement script:**
   ```bash
   # Participants run this in Round 1
   bin/check-policy <participant_id> --round 1
   ```

### Step 2: Monitor During Experiment

- Check submission timestamps
- Review code quality differences
- Flag suspicious patterns

### Step 3: Post-Experiment Analysis

```bash
# Generate compliance report
bin/analyze-compliance -o compliance_report.json

# Review flagged cases
cat compliance_report.json | grep -A 5 "warning"
```

## Best Practices

1. **Clear Communication:**
   - State policy clearly in all materials
   - Remind participants at start of Round 1
   - Explain why Round 1 is no-AI

2. **Reasonable Expectations:**
   - Some participants may still use AI despite restrictions
   - Focus on aggregate patterns, not individual cases
   - Use analysis to identify outliers, not punish

3. **Data Collection:**
   - Save all submission timestamps
   - Archive code for both rounds
   - Compare patterns statistically

4. **Transparency:**
   - Tell participants you'll analyze patterns
   - Explain detection methods
   - This can act as a deterrent

## Example Analysis Workflow

```bash
# After experiment completes
cd /workspaces/a

# Generate compliance report
bin/analyze-compliance -o reports/compliance.json

# Review summary
python -c "
import json
data = json.load(open('reports/compliance.json'))
for p in data:
    pid = p['participant_id']
    timing = p.get('timing_analysis', {})
    if timing.get('warning'):
        print(f'{pid}: {timing[\"warning\"]}')
"

# Manual review of flagged cases
# Compare Round 1 vs Round 2 code quality
```

## Limitations

- **No perfect enforcement:** Determined users can bypass restrictions
- **False positives:** Analysis heuristics may flag legitimate work
- **Privacy concerns:** Network monitoring may be intrusive
- **Technical complexity:** Network restrictions require setup

## Recommendation

For most experiments, use **Option A (Honor Code)** with **Option C (Post-Hoc Analysis)**:

1. Clear policy communication
2. Trust participants
3. Analyze patterns after the fact
4. Flag outliers for manual review
5. Focus on aggregate results, not individual compliance

This balances experiment integrity with participant trust and technical feasibility.

