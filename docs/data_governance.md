# Data Governance

**Document Owner:** Data Governance Lead
**Last Updated:** 2026-01-20
**Review Cycle:** Quarterly

## Data Governance Framework

This document describes the data governance practices for the Acme AI Hiring Tool, in compliance with Article 10 of the EU AI Act.

## Training Data

### Source Description

- **Dataset:** 150,000 anonymized historical job applications from Acme Corp's ATS (Applicant Tracking System)
- **Time Period:** January 2020 to December 2025
- **Geographic Coverage:** EU and UK applicants
- **Language:** English-language applications only
- **Label:** Binary hiring outcome (hired/not hired), validated against 12-month retention

### Data Quality Criteria

| Criterion | Measure | Threshold | Current Status |
|-----------|---------|-----------|---------------|
| Completeness | % fields with non-null values | > 95% | 97.2% |
| Consistency | Cross-field validation pass rate | > 99% | 99.6% |
| Timeliness | Data freshness (months since last update) | < 6 months | 2 months |
| Accuracy | Sample audit accuracy rate | > 98% | 98.4% |
| Uniqueness | Duplicate detection rate | < 0.5% | 0.3% |

### Data Collection Process

1. Applications submitted through Acme Corp's online portal
2. Structured data extracted automatically from application forms
3. Resume text parsed using NLP pipeline (spaCy + custom rules)
4. Manual quality review on 5% random sample quarterly
5. Data anonymized before model training (names, emails, addresses removed)

### Protected Attributes

The following attributes are **excluded from model training** to prevent direct discrimination:

- Name, gender, age, date of birth
- Ethnicity, race, national origin
- Religion, sexual orientation
- Disability status
- Marital status, pregnancy status
- Photo or video data

**Note:** These attributes are retained in a separate, access-controlled fairness evaluation dataset used solely for bias auditing purposes.

## Validation Data

- **Size:** 15,000 applications (10% stratified holdout)
- **Stratification:** By role category, geography, and time period
- **Representativeness:** Demographic distribution mirrors training data within 2% tolerance
- **Refresh:** Updated with each retraining cycle

## Testing Data

- **Size:** 15,000 applications (separate 10% holdout, never seen during training or validation)
- **Purpose:** Final performance evaluation and fairness testing
- **Independence:** Strict temporal split (most recent applications)

## Data Bias Assessment

### Known Biases in Historical Data

1. **Gender imbalance in tech roles:** Historical data reflects 70/30 male/female ratio in software engineering applications
2. **Age distribution skew:** 65% of applications from candidates aged 25-35
3. **Geographic concentration:** 40% of applications from 3 major EU cities

### Bias Mitigation Strategies

- Reweighting: Training samples weighted to equalize demographic representation
- Feature exclusion: All protected attributes removed from model inputs
- Regular audit: Quarterly fairness evaluation using AIF360 metrics
- Threshold adjustment: Score thresholds calibrated per role category to maintain fairness

## Data Retention and Deletion

- **Training data retention:** 36 months from collection date
- **Model artifacts:** Retained for model lifetime plus 24 months
- **Candidate personal data:** Deleted per GDPR Article 17 upon request
- **Audit logs:** Retained for 5 years per regulatory requirements

## Data Access Controls

| Role | Access Level | Justification |
|------|-------------|---------------|
| Data Engineers | Read/Write training pipeline | Data preparation |
| ML Engineers | Read-only processed data | Model training |
| Fairness Auditors | Read-only demographic data | Bias evaluation |
| Compliance Team | Read-only audit logs | Regulatory review |
| External Auditors | Restricted, supervised access | Annual audit |

## Data Processing Records

All data processing activities are recorded in the data processing register, including:
- Purpose of processing
- Categories of data subjects
- Data transfers (none outside EU/EEA)
- Technical and organizational security measures
- Data Protection Impact Assessment reference (DPIA-2025-HR-AI-003)
