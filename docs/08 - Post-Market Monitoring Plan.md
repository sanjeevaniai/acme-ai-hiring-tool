# Post-Market Monitoring Plan

**Document ID:** PMM-AI-001
**Effective Date:** 2025-10-01
**Owner:** AI Governance Lead
**Classification:** Internal
**EU AI Act Reference:** Article 72

---

## 1. Purpose

This post-market monitoring plan ensures continuous oversight of the AI Hiring Tool after deployment, detecting emerging risks, performance degradation, and compliance issues in a timely manner.

## 2. Monitoring Framework

### 2.1 Performance Monitoring

| Metric | Method | Frequency | Threshold | Action |
|--------|--------|-----------|-----------|--------|
| AUC-ROC | Computed on recent outcomes | Monthly | < 0.82 | Trigger retraining evaluation |
| Precision@80 | Computed on recent outcomes | Monthly | < 0.75 | Investigate feature drift |
| Score distribution | PSI against reference | Weekly | > 0.2 | Critical drift alert |
| Feature distributions | KS test per feature | Weekly | p < 0.05 | Warning alert |
| Prediction latency | P99 response time | Daily | > 500ms | Scale infrastructure |
| Error rate | API error count | Daily | > 1% | Investigate immediately |

### 2.2 Fairness Monitoring

| Metric | Groups | Frequency | Threshold | Action |
|--------|--------|-----------|-----------|--------|
| Demographic parity ratio | Gender, Age | Quarterly | < 0.80 | Critical: immediate investigation |
| Equal opportunity gap | Gender, Age | Quarterly | > 0.10 | High: investigation within 2 weeks |
| Mean score gap | Gender, Age | Monthly | > 10 points | Warning: trend analysis |
| Override rate by group | Gender, Age | Quarterly | Significant difference | Warning: investigate recruiter behavior |

### 2.3 Security Monitoring

| Metric | Frequency | Threshold | Action |
|--------|-----------|-----------|--------|
| Failed authentication attempts | Real-time | > 10/hour per account | Account lockout + alert |
| Anomalous API patterns | Daily | Statistical outlier | Investigation |
| Dependency vulnerabilities | Daily (automated) | Critical CVE | Patch within 48 hours |
| Data access anomalies | Real-time | Unusual access pattern | Alert + investigation |

## 3. Data Collection

### 3.1 What We Collect

- All prediction requests and responses (anonymized)
- Input feature distributions (aggregated, not individual)
- Model performance metrics against ground truth (when available)
- System health metrics (latency, errors, availability)
- User interaction data (overrides, explanations viewed)
- Incident reports and resolution data

### 3.2 Ground Truth Collection

Model accuracy requires ground truth (actual hiring outcomes):
- Hiring decisions collected from deployers monthly
- 12-month retention outcomes collected annually
- Used only for model evaluation, not for individual scoring

### 3.3 Data Retention

| Data Type | Retention Period | Justification |
|-----------|-----------------|---------------|
| Prediction logs | 5 years | Regulatory audit trail |
| Performance metrics | 10 years | System lifetime documentation |
| Fairness reports | 10 years | Compliance evidence |
| Incident reports | 10 years | Regulatory requirement |
| Raw input data | 36 months | Retraining and drift analysis |

## 4. Reporting

### 4.1 Internal Reports

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| Weekly monitoring digest | ML Team | Weekly | Drift metrics, alerts, system health |
| Monthly performance report | AI Governance Lead | Monthly | Full performance dashboard, trends |
| Quarterly fairness report | AI Governance Board | Quarterly | Fairness metrics, mitigation actions, audit results |
| Annual compliance review | Executive leadership | Annual | Full compliance posture, risk assessment update |

### 4.2 External Reports

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| Deployer performance report | Client organizations | Monthly | System performance, uptime, key metrics |
| Regulatory report | Market surveillance authority | Upon request | Full documentation package |
| Serious incident report | Market surveillance authority | Per occurrence | Incident details per Article 62 |

## 5. Continuous Improvement

### 5.1 Feedback Loop

```
Monitoring Data → Analysis → Findings → Action Items
       ↑                                      ↓
    Deploy Fix ← Testing ← Implementation ← Planning
```

### 5.2 Retraining Triggers

The model is retrained when any of the following occur:
1. Scheduled semi-annual retraining
2. AUC-ROC drops below 0.82 for two consecutive months
3. PSI exceeds 0.2 (critical drift)
4. Fairness violation detected and confirmed
5. Significant change in deployer population or use case

### 5.3 System Updates

All system updates follow:
1. Change request documentation
2. Impact assessment (does this require new conformity assessment?)
3. Testing in staging environment
4. Staged rollout with enhanced monitoring
5. Post-deployment validation (7-day monitoring period)
6. Update technical documentation

## 6. Authority Cooperation

Acme Corp will:
- Provide full documentation to competent authorities upon request
- Facilitate inspections and audits
- Implement corrective actions as directed
- Participate in regulatory sandboxes if invited
- Share anonymized incident data for sector-wide learning

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-01 | AI Governance Lead | Initial release |
| 1.1 | 2026-02-01 | AI Governance Lead | Updated monitoring thresholds based on 6-month operational data |
