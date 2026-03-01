# Conformity Assessment Roadmap

**Document ID:** CONF-AI-001
**Effective Date:** 2026-01-15
**Owner:** AI Governance Lead
**Classification:** Internal

---

## 1. Overview

This document outlines Acme Corp's plan for completing conformity assessment of the AI Hiring Tool per Articles 43 and 49 of the EU AI Act. As a high-risk AI system under Annex III, the system must undergo conformity assessment before being placed on the market or put into service.

## 2. Conformity Assessment Procedure

### 2.1 Applicable Procedure

Per Article 43(1), the AI Hiring Tool will undergo conformity assessment based on **internal control** (Annex VI), as:
- The system is not biometric identification
- No harmonised standard requires third-party assessment
- The provider (Acme Corp) maintains a quality management system

### 2.2 Alternative: Third-Party Assessment

Acme Corp will engage a notified body for optional third-party validation if:
- Client contracts require it
- Harmonised standards are published requiring it
- The AI Governance Board determines additional assurance is needed

## 3. Compliance Checklist

### 3.1 Quality Management System (Article 17)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Written QMS policy | Complete | GOV-AI-001 |
| Risk management process | Complete | RISK-AI-001 |
| Data governance procedures | Complete | docs/data_governance.md |
| Technical documentation | Complete | docs/technical_documentation.md |
| Record-keeping system | Complete | Audit log system + monitoring/config.yaml |
| Corrective action procedures | Complete | Incident management process |
| Post-market monitoring | Complete | monitoring/config.yaml |
| Resource management | In progress | Roles defined, budget allocation pending |
| Accountability framework | Complete | GOV-AI-001, Section 6 |

### 3.2 Risk Management (Article 9)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Risk identification | Complete | docs/risk_assessment.md |
| Risk assessment methodology | Complete | RISK-AI-001 |
| Risk mitigation measures | Complete | docs/risk_assessment.md |
| Residual risk evaluation | Complete | docs/risk_assessment.md |
| Continuous monitoring | Active | monitoring/config.yaml |
| Testing for risk mitigation | Active | tests/ directory |

### 3.3 Data Governance (Article 10)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Training data quality criteria | Complete | docs/data_governance.md |
| Validation data governance | Complete | docs/data_governance.md |
| Testing data independence | Complete | docs/data_governance.md |
| Bias examination | Complete | docs/fairness_analysis.md |
| Data gap identification | Partial | Known gap: ethnicity data not collected |

### 3.4 Technical Documentation (Article 11, Annex IV)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| General system description | Complete | README.md, docs/technical_documentation.md |
| System architecture | Complete | docs/technical_documentation.md |
| Training methodology | Complete | docs/technical_documentation.md |
| Performance metrics | Complete | MODEL_CARD.md |
| Computational resources | Complete | docs/technical_documentation.md |
| Instructions for use | Complete | docs/technical_documentation.md |
| Changes log | Complete | docs/technical_documentation.md |

### 3.5 Transparency (Article 13)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| User notification | Complete | docs/transparency_notice.md |
| Instructions for deployers | Complete | docs/technical_documentation.md |
| Explainability mechanism | Complete | SHAP-based explanations |
| Limitations disclosure | Complete | MODEL_CARD.md |

### 3.6 Human Oversight (Article 14)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Override mechanism | Complete | docs/human_oversight.md |
| Human-machine interface | Complete | Recruiter dashboard |
| Training for overseers | Complete | docs/human_oversight.md |
| Emergency stop procedure | Complete | docs/human_oversight.md |

### 3.7 Accuracy, Robustness, Cybersecurity (Article 15)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Accuracy metrics | Complete | MODEL_CARD.md |
| Robustness testing | Complete | tests/test_robustness.py |
| Cybersecurity measures | Complete | docs/security_policy.md |
| Resilience mechanisms | Partial | Drift monitoring active, adversarial robustness testing planned |

## 4. EU Declaration of Conformity

### 4.1 Timeline

| Milestone | Target Date | Status |
|-----------|------------|--------|
| Complete all compliance documentation | 2026-03-01 | In progress |
| Internal audit of QMS | 2026-04-01 | Planned |
| Gap remediation | 2026-05-01 | Planned |
| Draw up EU Declaration of Conformity | 2026-06-01 | Planned |
| Affix CE marking | 2026-06-15 | Planned |
| Register in EU database (Article 49) | 2026-07-01 | Planned |
| Full compliance before enforcement | 2026-08-02 | Target |

### 4.2 Declaration Contents (Annex V)

The EU Declaration of Conformity will include:
- AI system name and identification
- Provider name and address
- Statement of sole responsibility
- Reference to applicable harmonised standards (when available)
- Reference to other technical specifications
- Date and place of issue
- Signature of authorised representative

## 5. Post-Conformity Obligations

After conformity assessment is complete:
- Maintain all technical documentation for 10 years (Article 18)
- Keep QMS operational and updated
- Continue post-market monitoring (Article 72)
- Report serious incidents to market surveillance authorities (Article 62)
- Update conformity assessment if substantial modifications are made (Article 43(4))

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-15 | AI Governance Lead | Initial roadmap |
