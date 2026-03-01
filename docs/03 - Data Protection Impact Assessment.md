# Data Protection Impact Assessment (DPIA)

**Document ID:** DPIA-2025-HR-AI-003
**Assessment Date:** 2025-09-15
**Assessor:** Data Protection Officer
**System:** Acme AI Hiring Tool v2.x
**Classification:** Confidential

---

## 1. Processing Description

### 1.1 Nature of Processing

The AI Hiring Tool processes personal data of job applicants to generate suitability scores that assist human recruiters in pre-screening candidates.

### 1.2 Data Processed

| Data Category | Examples | Legal Basis |
|--------------|---------|-------------|
| Application data | Resume text, skills, education, experience | Legitimate interest (Article 6(1)(f) GDPR) |
| Contact data | Email, name (for communication only) | Contract performance (Article 6(1)(b) GDPR) |
| Special category data | Not intentionally processed; excluded by design | N/A |
| Derived data | Suitability score, feature importance | Legitimate interest |

### 1.3 Purpose

- Primary: Assist recruitment screening process
- Secondary: Model performance monitoring and improvement
- Not used for: Marketing, profiling beyond recruitment, or any automated final decisions

### 1.4 Data Subjects

- Job applicants to Acme Corp and its clients
- Estimated volume: 50,000-100,000 applications per year
- Geographic scope: EU/EEA and UK

## 2. Necessity and Proportionality

### 2.1 Necessity Assessment

| Question | Assessment |
|----------|-----------|
| Is AI processing necessary for the stated purpose? | Yes - manual screening of 100K+ applications per year is impractical |
| Could the purpose be achieved with less data? | Partially - minimum viable features identified and used |
| Is the processing proportionate to the purpose? | Yes - AI scoring is advisory only, not deterministic |

### 2.2 Data Minimization

- Only job-relevant data is processed (resume, experience, education, skills)
- Protected attributes explicitly excluded from model features
- Contact information is not processed by the AI model
- Data retained only for documented retention periods

### 2.3 Lawful Basis

**Primary basis:** Legitimate interest (Article 6(1)(f) GDPR)

**Balancing test:**
- Acme Corp's legitimate interest: Efficient, fair candidate screening at scale
- Data subjects' rights and expectations: Applicants expect their data to be used for application evaluation
- Safeguards: Human oversight, transparency, appeal rights, bias monitoring
- Conclusion: Processing is proportionate given the safeguards in place

## 3. Risk Assessment

### 3.1 Risks to Data Subjects

| Risk | Likelihood | Severity | Overall Risk |
|------|-----------|----------|-------------|
| Unfair scoring due to algorithmic bias | Medium | High | High |
| Unauthorized access to application data | Low | High | Medium |
| Re-identification from anonymized data | Low | Medium | Low |
| Lack of transparency about AI use | Low | Medium | Low (mitigated) |
| Inability to contest AI-assisted decisions | Low | High | Medium (mitigated) |

### 3.2 Mitigation Measures

| Risk | Mitigation | Residual Risk |
|------|-----------|---------------|
| Algorithmic bias | Fairness testing (quarterly), protected attribute exclusion, demographic parity monitoring | Medium - ongoing monitoring required |
| Unauthorized access | Encryption (AES-256), RBAC, MFA, audit logging | Low |
| Re-identification | k-anonymity applied to training data, access controls on raw data | Low |
| Lack of transparency | Application portal notification, privacy notice update, right to explanation | Low |
| Inability to contest | Human review guaranteed, appeal process established, explanation available on request | Low |

## 4. Data Subject Rights

### 4.1 Rights Implementation

| GDPR Right | Implementation |
|-----------|---------------|
| Right to be informed (Art. 13-14) | Privacy notice updated, AI screening notification displayed |
| Right of access (Art. 15) | Data subject access requests processed within 30 days |
| Right to rectification (Art. 16) | Applicants can update their application data |
| Right to erasure (Art. 17) | Data deleted upon request (except legal retention requirements) |
| Right to restrict processing (Art. 18) | AI scoring can be bypassed for individual applicants |
| Right to data portability (Art. 20) | Application data exportable in structured format |
| Right to object (Art. 21) | Applicants can opt out of AI screening |
| Automated decision-making (Art. 22) | No solely automated decisions; human review always involved |

### 4.2 Response Times

- Standard requests: 30 calendar days
- Complex requests: 60 calendar days (with notification to data subject)
- Emergency requests (e.g., discrimination concern): 5 business days

## 5. Consultation

### 5.1 Internal Consultation

| Stakeholder | Date | Outcome |
|------------|------|---------|
| Legal Team | 2025-08-01 | Approved legitimate interest basis |
| HR Department | 2025-08-10 | Confirmed human oversight procedures |
| IT Security | 2025-08-15 | Validated technical security measures |
| Works Council | 2025-09-01 | Acknowledged with conditions on monitoring |

### 5.2 Supervisory Authority Consultation

Prior consultation with the supervisory authority (Article 36 GDPR) was considered but determined not required because:
- The high risks identified have been adequately mitigated
- No solely automated decisions are made
- Robust safeguards and human oversight are in place

This determination will be reassessed if risk profile changes.

## 6. Conclusion

The processing is **approved** subject to the following conditions:
1. All mitigation measures must be implemented before deployment
2. Quarterly fairness audits must be conducted and reported to the AI Governance Board
3. The DPIA must be reviewed annually or upon significant system changes
4. Any serious incident must trigger immediate DPIA reassessment

---

**Approved by:**
- Data Protection Officer: [Signed] - 2025-09-15
- AI Governance Lead: [Signed] - 2025-09-15
- CTO: [Signed] - 2025-09-18
