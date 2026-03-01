# Model Card: Acme AI Hiring Tool v2.1

## Model Details

- **Model Name:** Acme Candidate Suitability Scorer
- **Version:** 2.1.0
- **Type:** XGBoost gradient-boosted ensemble classifier
- **Training Framework:** XGBoost 2.0, scikit-learn 1.4
- **Date Trained:** 2026-01-10
- **Developers:** Acme Corp AI Team
- **Contact:** ai-team@acmecorp.example.com

## Intended Use

**Primary Use:** Rank job applicants by suitability score (0-100) to assist human recruiters in pre-screening.

**Intended Users:** Trained HR professionals who use suitability scores as one input among many in hiring decisions.

**Out-of-Scope Uses:**
- Automated rejection without human review
- Performance evaluation of current employees
- Use in jurisdictions where automated employment screening is prohibited
- Screening for roles where the model has not been validated (currently validated for: software engineering, data science, product management)

## Training Data

- **Source:** 150,000 anonymized historical applications from 2020-2025
- **Geographic Coverage:** EU and UK applicants
- **Features Used:**
  - Resume text (NLP-extracted keywords and structure)
  - Years of experience (numeric)
  - Education level (categorical: high school, bachelors, masters, PhD)
  - Skills match score (computed against job description)
  - Prior role titles (NLP-extracted)
- **Features Excluded (by design):**
  - Name, gender, age, ethnicity, nationality
  - Photo or video data
  - Social media profiles
  - Address (beyond country-level for legal compliance)
- **Label:** Hiring outcome (hired = 1, not hired = 0), validated against 12-month retention

## Performance Metrics

### Overall Performance

| Metric | Value | 95% CI |
|--------|-------|--------|
| AUC-ROC | 0.87 | [0.85, 0.89] |
| Precision@80 | 0.82 | [0.79, 0.85] |
| Recall@80 | 0.79 | [0.76, 0.82] |
| F1 Score | 0.80 | [0.77, 0.83] |
| Accuracy | 0.83 | [0.81, 0.85] |

### Performance by Demographic Group

Evaluated on a held-out test set of 15,000 applications with voluntary demographic data.

| Group | AUC-ROC | Selection Rate | Disparate Impact Ratio |
|-------|---------|---------------|----------------------|
| Male | 0.87 | 32.1% | 1.00 (reference) |
| Female | 0.86 | 29.8% | 0.93 |
| Non-binary | 0.84 | 28.5% | 0.89 |
| Age 18-30 | 0.88 | 33.2% | 1.00 (reference) |
| Age 31-45 | 0.87 | 31.4% | 0.95 |
| Age 46-65 | 0.85 | 27.9% | 0.84 |

**Note:** The 46-65 age group shows a disparate impact ratio of 0.84, which is below the 4/5ths (0.80) threshold but warrants continued monitoring. Mitigation strategies are documented in `docs/fairness_analysis.md`.

### Performance by Role Category

| Role Category | AUC-ROC | N (test set) |
|--------------|---------|-------------|
| Software Engineering | 0.89 | 6,200 |
| Data Science | 0.88 | 4,100 |
| Product Management | 0.84 | 3,400 |
| Other | 0.81 | 1,300 |

## Limitations

- Model performance degrades for role categories with fewer than 500 training examples
- Resume parsing accuracy drops for non-English resumes (currently English-only)
- The model may encode historical biases present in past hiring decisions despite mitigation efforts
- Suitability scores should never be the sole basis for hiring decisions
- Model has not been validated for executive-level or C-suite positions
- Performance may degrade over time as job market conditions change (drift monitoring is active)

## Ethical Considerations

- **Bias Risk:** Employment AI systems can perpetuate historical discrimination. We conduct quarterly fairness audits and maintain demographic parity monitoring
- **Transparency:** All candidates are notified that AI-assisted screening is used in the process
- **Human Oversight:** Final hiring decisions are always made by human recruiters with full override capability
- **Right to Explanation:** Candidates can request an explanation of factors that influenced their score

## Monitoring & Updates

- **Drift Detection:** Weekly statistical tests (PSI, KS test) on input feature distributions
- **Performance Monitoring:** Monthly AUC-ROC recalculation on recent hiring outcomes
- **Fairness Monitoring:** Quarterly disparate impact analysis across all protected groups
- **Retraining Schedule:** Semi-annual retraining with most recent 24 months of data
- **Incident Reporting:** Any fairness violation triggers immediate review (see `docs/transparency_notice.md`)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-10 | Added age group fairness monitoring, updated training data |
| 2.0.0 | 2025-07-15 | Switched from logistic regression to XGBoost, added NLP features |
| 1.0.0 | 2024-11-01 | Initial release, logistic regression baseline |
