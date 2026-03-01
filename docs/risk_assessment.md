# Risk Assessment

**Document Owner:** AI Governance Lead
**Last Updated:** 2026-02-01
**Review Cycle:** Quarterly

## Risk Classification

This AI system is classified as **High-Risk** under the EU AI Act, Regulation (EU) 2024/1689.

### Classification Basis

- **Article 6(2):** AI systems referred to in Annex III
- **Annex III, Area 4(a):** AI systems intended to be used for recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates
- **Risk Tier:** High-Risk (Tier 2)

### Prohibited Practices Confirmation

This system does NOT engage in any prohibited AI practices under Article 5:
- No subliminal manipulation techniques
- No exploitation of vulnerable groups
- No social scoring by public authorities
- No real-time remote biometric identification
- No emotion recognition in workplace (system uses text data only)

## Risk Identification

### Risk Register

| Risk ID | Description | Category | Likelihood | Impact | Severity | Mitigation |
|---------|-------------|----------|-----------|--------|----------|-----------|
| R-001 | Historical bias in training data leads to discriminatory scoring | Fairness | Medium | High | Critical | Bias audit, demographic parity testing, protected attribute exclusion |
| R-002 | Model drift causes accuracy degradation over time | Safety | Medium | Medium | High | Weekly drift monitoring, semi-annual retraining |
| R-003 | Unauthorized access to candidate data | Security | Low | High | High | Encryption at rest/transit, RBAC, audit logging |
| R-004 | Over-reliance on AI scores by recruiters | Oversight | Medium | High | High | Mandatory human review policy, training program |
| R-005 | Adversarial input manipulation (resume keyword stuffing) | Robustness | Medium | Medium | Medium | Input validation, anomaly detection |
| R-006 | Lack of candidate awareness of AI involvement | Transparency | Low | Medium | Medium | Notification in application portal, privacy notice update |
| R-007 | Model underperformance for underrepresented role categories | Accuracy | Medium | Medium | Medium | Minimum sample threshold, confidence intervals |
| R-008 | Non-compliance with evolving regulatory requirements | Compliance | Medium | High | High | Quarterly compliance review, regulatory monitoring |

## Risk Mitigation Measures

### R-001: Historical Bias
- Excluded protected attributes (name, gender, age, ethnicity) from feature set
- Quarterly fairness audit using AIF360 library
- Demographic parity monitoring with automated alerts
- Disparate impact ratio tracked against 4/5ths rule threshold
- Bias mitigation through reweighting when disparate impact detected

### R-002: Model Drift
- Population Stability Index (PSI) calculated weekly on input features
- Kolmogorov-Smirnov test on score distributions
- Automated alert when PSI > 0.2 or KS p-value < 0.05
- Semi-annual retraining with latest 24 months of data

### R-003: Data Security
- AES-256 encryption for data at rest
- TLS 1.3 for data in transit
- Role-based access control (RBAC) with principle of least privilege
- Audit logging of all data access events
- Annual penetration testing

### R-004: Over-reliance
- Mandatory recruiter training on AI limitations
- Dashboard shows confidence intervals, not just scores
- Policy requires interview for all candidates above score threshold
- Quarterly review of human override rates

### R-005: Adversarial Inputs
- Input length and format validation
- Statistical anomaly detection on feature vectors
- Keyword density analysis to detect resume stuffing
- Manual review flag for statistical outliers

## Residual Risk Assessment

After mitigation measures, the following residual risks remain:

| Risk ID | Residual Severity | Acceptable? | Justification |
|---------|-------------------|-------------|---------------|
| R-001 | Medium | Yes | Continuous monitoring catches emerging bias; human review provides final safeguard |
| R-002 | Low | Yes | Automated drift detection provides early warning |
| R-003 | Low | Yes | Industry-standard security controls in place |
| R-004 | Medium | Yes | Training program and mandatory review policy active |
| R-005 | Low | Yes | Input validation catches most adversarial attempts |

## Review Schedule

- **Quarterly:** Full risk register review
- **Monthly:** Monitoring dashboard review
- **Ad-hoc:** Triggered by incidents, regulatory updates, or significant model changes
