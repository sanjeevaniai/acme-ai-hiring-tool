# Human Oversight

**Document Owner:** AI Governance Lead
**Last Updated:** 2026-01-25
**Review Cycle:** Quarterly

## Overview

This document describes the human oversight mechanisms for the Acme AI Hiring Tool, in compliance with Article 14 of the EU AI Act.

## Human-Machine Interface Design

### Recruiter Dashboard

The recruiter dashboard is designed to support informed human decision-making:

- **Score Display:** Suitability score shown with confidence interval (e.g., "72 [68-76]")
- **Explanation Panel:** Top 5 contributing factors with SHAP values, shown alongside each candidate
- **Comparison View:** Side-by-side candidate comparison with AI scores and raw application data
- **Override Button:** Prominent "Override AI Score" button on every candidate card
- **Flagging System:** Recruiters can flag candidates for additional review regardless of AI score

### Information Provided to Human Overseers

For each candidate, the human reviewer sees:
1. AI suitability score with confidence interval
2. Feature importance breakdown (SHAP values)
3. Full application data (resume, responses)
4. Any system flags (anomaly detection, low confidence)
5. Fairness monitoring alerts if applicable

## Intervention Mechanisms

### Override Capability

- Any recruiter can override the AI score for any candidate
- Overrides are logged with reason code and free-text justification
- No minimum or maximum score is enforced on human overrides
- Override decisions are not penalized or questioned by the system

### Escalation Procedure

1. **Recruiter flags concern** → Notification to hiring manager
2. **Hiring manager review** → Can escalate to AI Governance team
3. **AI Governance review** → Can pause system for affected role category
4. **Emergency stop** → AI Governance Lead can disable the system entirely within 15 minutes

### Human-in-the-Loop Requirements

| Decision Type | AI Role | Human Role | Policy |
|--------------|---------|------------|--------|
| Initial screening | Generate suitability score | Review and validate | AI score is advisory only |
| Shortlisting | Rank candidates | Select final shortlist | Human makes final selection |
| Rejection | Flag low scores | Confirm rejection decision | No automated rejection |
| Interview invitation | Recommend candidates | Send invitations | Human decides and sends |

## Monitoring of Human Oversight Effectiveness

### Metrics Tracked

- **Override Rate:** Percentage of AI scores overridden by recruiters (target: 5-15%)
- **Override Direction:** Whether overrides tend to increase or decrease scores
- **Time-to-Decision:** Average time recruiters spend reviewing each candidate
- **Automation Bias Detection:** Statistical comparison of decisions with and without AI scores

### Current Metrics (Q4 2025)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Override Rate | 8.2% | 5-15% | On target |
| Score Increase Overrides | 4.1% | N/A | Normal |
| Score Decrease Overrides | 4.1% | N/A | Normal |
| Avg Review Time | 3.2 min | > 2 min | On target |

### Automation Bias Mitigation

- Recruiters complete mandatory training on AI limitations before system access
- Quarterly refresher training on cognitive biases in AI-assisted decision-making
- Dashboard design deliberately avoids anchoring effects (shows application data before AI score)
- Random audit of decisions to check for rubber-stamping patterns

## Training Requirements

### Initial Training (Required)

All recruiters must complete before system access:
- Module 1: How the AI system works (2 hours)
- Module 2: Interpreting AI scores and explanations (1 hour)
- Module 3: When and how to override (1 hour)
- Module 4: Bias awareness and fair hiring practices (2 hours)
- Assessment: Must pass with 80% or higher

### Ongoing Training

- Quarterly refresher sessions (1 hour)
- Annual certification renewal
- Ad-hoc training when system updates are deployed

## Emergency Procedures

### System Pause

The AI Governance Lead can pause the system:
- **Trigger:** Fairness violation detected, system malfunction, or regulatory request
- **Process:** Single-click disable in admin panel
- **Fallback:** Recruiters continue with manual screening using existing application data
- **Communication:** Automated notification to all active users within 5 minutes

### Incident Response

1. System paused within 15 minutes of confirmed issue
2. Root cause analysis within 48 hours
3. Fix implemented and tested within 2 weeks
4. System re-enabled only after AI Governance Lead approval
5. Post-incident report filed within 30 days
