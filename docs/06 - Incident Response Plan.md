# AI Incident Response Plan

**Document ID:** INC-AI-001
**Effective Date:** 2025-08-01
**Owner:** AI Governance Lead
**Classification:** Internal

---

## 1. Purpose

This plan defines the procedures for detecting, responding to, and recovering from incidents involving the AI Hiring Tool. It ensures compliance with Article 62 of the EU AI Act (serious incident reporting) and supports the broader risk management framework.

## 2. Incident Definition

An AI incident is any event where the AI Hiring Tool:
- Produces incorrect, biased, or harmful outputs
- Experiences a security breach or data exposure
- Fails to operate as intended
- Violates fairness thresholds or compliance requirements
- Causes harm or potential harm to data subjects

## 3. Severity Classification

| Level | Name | Definition | Example | Response Time |
|-------|------|-----------|---------|---------------|
| P1 | Critical | Immediate harm to individuals or fundamental rights violation | Systematic discrimination detected, data breach with PII exposure | 1 hour |
| P2 | High | Significant impact on fairness, safety, or compliance | Disparate impact ratio below threshold, model producing degenerate outputs | 4 hours |
| P3 | Medium | Moderate impact requiring correction | Performance degradation, drift above warning threshold | 24 hours |
| P4 | Low | Minor issue with no immediate impact | Documentation gap, minor process deviation | 1 week |

## 4. Response Procedures

### 4.1 Phase 1: Detection and Triage (0-1 hour)

**Detection Sources:**
- Automated monitoring alerts (drift, fairness, performance)
- User reports (recruiters, candidates, deployers)
- Internal audit findings
- External reports (researchers, authorities)

**Triage Steps:**
1. On-call engineer acknowledges alert
2. Initial severity assessment using classification matrix
3. Notify AI Governance Lead for P1/P2 incidents
4. Open incident ticket with timestamp and initial assessment

### 4.2 Phase 2: Containment (1-4 hours for P1/P2)

**Containment Options:**
| Action | When | Who Approves |
|--------|------|-------------|
| Monitor closely | P3/P4 incidents | On-call engineer |
| Disable affected feature | Specific functionality compromised | AI Governance Lead |
| Pause system for affected deployer | Deployer-specific issue | AI Governance Lead |
| Full system shutdown | Systemic issue affecting all users | AI Governance Board (emergency) |
| Revert to previous model version | Model-related issue | ML Team Lead |

### 4.3 Phase 3: Investigation (4-48 hours)

**Root Cause Analysis:**
- Data analysis: Review input data, model outputs, and logs
- Model analysis: Check for drift, bias, or degradation
- Security analysis: Review access logs, check for unauthorized activity
- Process analysis: Review deployment, configuration, and operational procedures

**Documentation:**
- Timeline of events
- Affected scope (users, data subjects, deployers)
- Root cause determination
- Contributing factors

### 4.4 Phase 4: Remediation (48 hours - 2 weeks)

- Implement fix for root cause
- Test fix thoroughly (including regression testing)
- Validate fairness metrics post-fix
- Deploy fix with enhanced monitoring
- Communicate resolution to affected parties

### 4.5 Phase 5: Recovery and Lessons Learned (2-4 weeks)

- Confirm system operating normally for sustained period
- Post-incident review meeting with all stakeholders
- Update risk register with new risk or revised assessment
- Update procedures if process gap identified
- Share anonymized lessons learned across organization

## 5. Serious Incident Reporting (Article 62)

### 5.1 What Constitutes a Serious Incident

Per Article 3(49) of the EU AI Act:
- Incident causing death or serious damage to health
- Serious and irreversible disruption of critical infrastructure management
- Breach of obligations under Union law intended to protect fundamental rights
- Serious damage to property or the environment

### 5.2 Reporting Timeline

- **Within 15 days:** Report to relevant market surveillance authority after becoming aware
- **Immediate:** If the incident involves imminent risk, notify authority immediately
- **72 hours:** Data breach notification to supervisory authority (GDPR Article 33)

### 5.3 Reporting Content

Report must include:
- AI system identification (name, version, registration number)
- Description of the incident
- Date and time of occurrence
- Affected parties
- Root cause (if known)
- Corrective measures taken
- Contact information for follow-up

## 6. Communication Plan

| Audience | Channel | Timing | Content |
|----------|---------|--------|---------|
| Internal teams | Slack #ai-incidents | Immediately | Technical details, action items |
| AI Governance Board | Email + emergency meeting | Within 4 hours (P1/P2) | Impact assessment, containment status |
| Affected deployers | Email + phone | Within 24 hours | Impact on their operations, recommended actions |
| Affected data subjects | Email | Within 72 hours (if required) | What happened, what we're doing, their rights |
| Regulatory authority | Official reporting channel | Per reporting timeline | Formal incident report |
| Public | Press release (if warranted) | After internal review | Factual statement, corrective actions |

## 7. Roles and Responsibilities

| Role | Responsibility During Incident |
|------|-------------------------------|
| On-Call Engineer | Detection, triage, initial containment |
| AI Governance Lead | Incident commander, authority reporting |
| ML Team Lead | Technical investigation, model remediation |
| CISO | Security investigation, data breach assessment |
| DPO | Data subject notification, GDPR compliance |
| Legal | Regulatory reporting, liability assessment |
| Communications | External communications, press inquiries |

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-08-01 | AI Governance Lead | Initial release |
| 1.1 | 2026-01-10 | AI Governance Lead | Updated serious incident reporting per final EU AI Act guidance |
