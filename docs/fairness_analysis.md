# Fairness Analysis

**Document Owner:** AI Ethics & Fairness Lead
**Last Updated:** 2026-02-01
**Review Cycle:** Quarterly

## Overview

This document details the fairness evaluation methodology and results for the Acme AI Hiring Tool, in compliance with the EU AI Act's requirements for non-discrimination and fundamental rights protection.

## Fairness Metrics Framework

We evaluate fairness using the following metrics, aligned with AIF360 library implementations:

### Group Fairness Metrics

| Metric | Definition | Threshold | Rationale |
|--------|-----------|-----------|-----------|
| Demographic Parity | P(Y=1\|A=a) = P(Y=1\|A=b) for all groups a,b | Ratio > 0.80 | 4/5ths rule (EEOC guidelines) |
| Equal Opportunity | P(Y=1\|Y*=1,A=a) = P(Y=1\|Y*=1,A=b) | Difference < 0.10 | Equal true positive rates |
| Equalized Odds | TPR and FPR equal across groups | Difference < 0.10 | Balanced error rates |
| Calibration | P(Y*=1\|S=s,A=a) = P(Y*=1\|S=s,A=b) | Difference < 0.05 | Score means the same for all groups |

### Individual Fairness

- Similar candidates (by qualification profile) should receive similar scores
- Measured using consistency score: average score variance within k-nearest neighbors in feature space

## Evaluation Results (Q4 2025)

### Gender

| Metric | Male | Female | Non-binary | Compliant? |
|--------|------|--------|------------|-----------|
| Selection Rate | 32.1% | 29.8% | 28.5% | Yes (ratios: 0.93, 0.89) |
| True Positive Rate | 0.81 | 0.78 | 0.76 | Yes (diff < 0.10) |
| False Positive Rate | 0.18 | 0.20 | 0.21 | Yes (diff < 0.10) |
| Mean Score | 62.3 | 60.1 | 59.4 | Monitor |

### Age Group

| Metric | 18-30 | 31-45 | 46-65 | Compliant? |
|--------|-------|-------|-------|-----------|
| Selection Rate | 33.2% | 31.4% | 27.9% | Monitor (0.84 ratio) |
| True Positive Rate | 0.82 | 0.80 | 0.75 | Yes (diff < 0.10) |
| False Positive Rate | 0.17 | 0.19 | 0.22 | Yes (diff < 0.10) |
| Mean Score | 63.1 | 61.7 | 57.8 | Action needed |

**Action Item:** The 46-65 age group shows a 5.3-point mean score gap. Investigation underway to determine if this reflects genuine qualification differences or age bias in historical data. Targeted reweighting being tested for next model version.

### Education Level

| Metric | High School | Bachelors | Masters | PhD | Compliant? |
|--------|------------|-----------|---------|-----|-----------|
| Selection Rate | 18.2% | 30.5% | 35.8% | 41.2% | N/A (legitimate factor) |

**Note:** Education level is a legitimate, non-protected factor in hiring decisions and is intentionally used as a model feature.

## Bias Mitigation Techniques Applied

1. **Pre-processing:** Protected attribute removal from feature set
2. **Pre-processing:** Training data reweighting to balance demographic representation
3. **In-processing:** Fairness constraints during hyperparameter tuning (optimizing for AUC subject to demographic parity > 0.85)
4. **Post-processing:** Score calibration reviewed per demographic group

## Known Limitations

- Intersectional fairness analysis (e.g., age x gender) not yet implemented due to small subgroup sizes
- Fairness evaluation limited to candidates who voluntarily provided demographic data (~60% of test set)
- Current analysis covers gender, age, and education; ethnicity data not collected due to EU data minimization requirements
- Individual fairness metric (consistency score) sensitive to distance metric choice

## Remediation Process

When a fairness violation is detected:

1. **Immediate:** Flag metric in monitoring dashboard, notify AI Governance Lead
2. **Within 48 hours:** Root cause analysis (data bias vs. model bias vs. sampling)
3. **Within 2 weeks:** Implement targeted mitigation (reweighting, threshold adjustment, or data augmentation)
4. **Within 4 weeks:** Validate fix on holdout data, deploy updated model if metrics improve
5. **Ongoing:** Continue monitoring for 3 consecutive quarters to confirm resolution

## Candidate Rights

- Candidates are informed that AI-assisted screening is used (see `transparency_notice.md`)
- Candidates may request a human-only review of their application
- Candidates may request an explanation of factors influencing their score
- Candidates may challenge the outcome through Acme Corp's appeals process
