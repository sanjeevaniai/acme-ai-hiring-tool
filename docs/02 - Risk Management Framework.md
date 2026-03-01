# Acme Corp - AI Risk Management Framework

**Document ID:** RISK-AI-001
**Effective Date:** 2025-06-01
**Review Date:** 2026-06-01
**Approved By:** AI Governance Board
**Classification:** Internal

---

## 1. Purpose

This framework establishes the risk management process for AI systems at Acme Corp, in compliance with Article 9 of the EU AI Act. It defines how risks are identified, assessed, mitigated, and monitored throughout the AI system lifecycle.

## 2. Risk Management Process

### 2.1 Risk Identification

Risk identification is conducted:
- During initial system design (design-phase risk assessment)
- Before deployment (pre-deployment risk review)
- Post-deployment (continuous monitoring)
- When significant changes are made to the system
- Following incidents or near-misses

### 2.2 Risk Assessment Methodology

Each identified risk is assessed on two dimensions:

**Likelihood Scale:**
| Level | Description | Probability |
|-------|-------------|------------|
| 1 - Rare | Unlikely to occur | < 5% |
| 2 - Unlikely | Could occur in exceptional circumstances | 5-20% |
| 3 - Possible | Could occur at some time | 20-50% |
| 4 - Likely | Will probably occur | 50-80% |
| 5 - Almost Certain | Expected to occur | > 80% |

**Impact Scale:**
| Level | Description | Consequences |
|-------|-------------|-------------|
| 1 - Negligible | Minimal impact | Minor inconvenience |
| 2 - Minor | Limited impact | Short-term disruption |
| 3 - Moderate | Significant impact | Material harm to individuals |
| 4 - Major | Serious impact | Significant harm, regulatory action |
| 5 - Catastrophic | Severe impact | Fundamental rights violations, systemic harm |

**Risk Matrix:**

| | Negligible | Minor | Moderate | Major | Catastrophic |
|---|---|---|---|---|---|
| **Almost Certain** | Medium | High | Critical | Critical | Critical |
| **Likely** | Low | Medium | High | Critical | Critical |
| **Possible** | Low | Medium | Medium | High | Critical |
| **Unlikely** | Low | Low | Medium | Medium | High |
| **Rare** | Low | Low | Low | Medium | Medium |

### 2.3 Risk Treatment

| Risk Level | Treatment | Timeline |
|-----------|-----------|----------|
| Critical | Immediate mitigation required; system may be paused | 24 hours |
| High | Mitigation plan required; enhanced monitoring | 2 weeks |
| Medium | Mitigation planned for next release cycle | 1 quarter |
| Low | Accept and monitor | Review at next assessment |

## 3. Fundamental Rights Impact Assessment

### 3.1 Scope

A fundamental rights impact assessment (FRIA) is conducted for all high-risk AI systems before deployment, evaluating impact on:

- Non-discrimination and equality (Article 21, EU Charter)
- Freedom of expression (Article 11, EU Charter)
- Right to privacy and data protection (Articles 7-8, EU Charter)
- Right to an effective remedy (Article 47, EU Charter)
- Rights of the child (Article 24, EU Charter)
- Workers' rights (Articles 27-31, EU Charter)

### 3.2 Assessment for AI Hiring Tool

| Right | Potential Impact | Mitigation | Residual Risk |
|-------|-----------------|------------|---------------|
| Non-discrimination | Model may encode historical bias | Fairness testing, protected attribute exclusion | Medium |
| Privacy | Processing of personal data | GDPR compliance, data minimization, encryption | Low |
| Effective remedy | Candidates may be unfairly scored | Appeal process, human override, explanation rights | Low |
| Workers' rights | Impact on employment access | Human-in-the-loop, transparency notice | Low |

## 4. Continuous Risk Monitoring

### 4.1 Monitoring Activities

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Performance metrics review | Monthly | ML Team |
| Fairness audit | Quarterly | AI Ethics Committee |
| Security vulnerability scan | Weekly | CISO |
| Incident review | Per occurrence | AI Governance Lead |
| Full risk reassessment | Annual | AI Governance Board |
| Regulatory compliance check | Quarterly | Legal |

### 4.2 Key Risk Indicators (KRIs)

| KRI | Threshold | Alert Level |
|-----|-----------|-------------|
| Model accuracy (AUC) | < 0.82 | Warning |
| Disparate impact ratio | < 0.80 | Critical |
| Data drift (PSI) | > 0.2 | Critical |
| Override rate | < 2% or > 25% | Warning |
| Incident count (monthly) | > 3 | Warning |

## 5. Incident Management

### 5.1 Incident Classification

| Severity | Definition | Response Time |
|----------|-----------|---------------|
| P1 - Critical | Fundamental rights impact, system malfunction causing harm | 1 hour |
| P2 - High | Significant fairness violation, data breach | 4 hours |
| P3 - Medium | Performance degradation, minor compliance gap | 24 hours |
| P4 - Low | Documentation issue, minor process deviation | 1 week |

### 5.2 Serious Incident Reporting

Per Article 62 of the EU AI Act, serious incidents are reported to the relevant market surveillance authority without undue delay, and no later than 15 days after the provider becomes aware of the incident.

A serious incident includes:
- Death or serious damage to health
- Serious and irreversible disruption of critical infrastructure
- Breach of fundamental rights obligations

## 6. Documentation Requirements

All risk management activities must be documented, including:
- Risk register (maintained and version-controlled)
- Assessment reports (signed by assessor)
- Mitigation plans (with deadlines and owners)
- Monitoring reports (with trend analysis)
- Incident reports (with root cause analysis)
- Board decisions (minutes recorded)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-06-01 | AI Governance Lead | Initial release |
| 1.1 | 2025-12-01 | AI Governance Lead | Added FRIA section, updated KRIs |
