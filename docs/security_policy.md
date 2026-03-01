# Security Policy

**Document Owner:** Information Security Officer
**Last Updated:** 2026-02-01
**Review Cycle:** Semi-annual

## Overview

This document describes the cybersecurity measures for the Acme AI Hiring Tool, in compliance with Article 15 of the EU AI Act and ISO 27001.

## Threat Model

### Attack Surface Analysis

| Attack Vector | Description | Likelihood | Impact | Mitigation |
|--------------|-------------|-----------|--------|-----------|
| Data poisoning | Malicious training data injection | Low | Critical | Data provenance tracking, input validation |
| Model extraction | Unauthorized model copying via API | Low | High | Rate limiting, query logging, watermarking |
| Adversarial inputs | Crafted resumes to manipulate scores | Medium | Medium | Input validation, anomaly detection |
| Data exfiltration | Unauthorized access to candidate data | Low | Critical | Encryption, RBAC, DLP |
| API abuse | Excessive or unauthorized API calls | Medium | Medium | Authentication, rate limiting, monitoring |
| Supply chain | Compromised dependencies | Low | High | Dependency scanning, SBOM, pinned versions |

## Access Control

### Role-Based Access Control (RBAC)

| Role | Permissions | Authentication |
|------|------------|---------------|
| Recruiter | Read scores, view explanations, override scores | SSO + MFA |
| Hiring Manager | Recruiter permissions + team reports | SSO + MFA |
| ML Engineer | Model training, deployment | SSO + MFA + VPN |
| Data Engineer | Data pipeline management | SSO + MFA + VPN |
| Admin | User management, system configuration | SSO + MFA + hardware key |
| Auditor | Read-only audit logs | SSO + MFA, supervised |

### Authentication

- Single Sign-On (SSO) via SAML 2.0 with corporate identity provider
- Multi-factor authentication (MFA) required for all users
- Hardware security key required for admin access
- Session timeout: 30 minutes of inactivity
- Maximum concurrent sessions: 3 per user

## Encryption

### Data at Rest

- **Algorithm:** AES-256-GCM
- **Key Management:** AWS KMS with automatic key rotation (annual)
- **Scope:** All candidate data, model artifacts, and audit logs

### Data in Transit

- **Protocol:** TLS 1.3
- **Certificate:** Let's Encrypt with automatic renewal
- **HSTS:** Enabled with 1-year max-age
- **Certificate pinning:** Implemented for API clients

## Vulnerability Management

### Dependency Scanning

- Automated dependency vulnerability scanning via Dependabot (daily)
- Software Bill of Materials (SBOM) maintained for all components
- All dependencies pinned to specific versions (see `requirements.txt`)
- Critical vulnerabilities patched within 48 hours

### Penetration Testing

- Annual third-party penetration test (last completed: 2025-11-15)
- Quarterly internal vulnerability assessment
- Bug bounty program for responsible disclosure

### Security Testing

- Automated security tests in CI pipeline (see `tests/test_security.py`)
- Input validation testing for all API endpoints
- SQL injection and XSS prevention testing
- Adversarial input detection testing

## Monitoring and Logging

### Audit Logging

All security-relevant events are logged:
- Authentication attempts (success and failure)
- Data access events
- Score queries and overrides
- System configuration changes
- Model deployments

### Log Retention

- Security logs: 2 years
- Access logs: 1 year
- Audit trails: 5 years (regulatory requirement)

### Alerting

| Event | Alert Level | Response Time |
|-------|------------|---------------|
| Multiple failed auth attempts | Warning | 1 hour |
| Unauthorized data access attempt | Critical | 15 minutes |
| Anomalous API usage pattern | Warning | 4 hours |
| Dependency vulnerability (critical) | Critical | 48 hours |
| Model artifact modification | Critical | 15 minutes |

## Incident Response

1. **Detection:** Automated monitoring alerts or manual report
2. **Triage:** Security team assesses severity within 30 minutes
3. **Containment:** Isolate affected systems within 1 hour
4. **Eradication:** Remove threat and patch vulnerability
5. **Recovery:** Restore systems from verified backups
6. **Lessons Learned:** Post-incident review within 7 days

### Data Breach Notification

Per GDPR Article 33:
- Supervisory authority notified within 72 hours
- Affected data subjects notified without undue delay if high risk
- Documentation of breach, effects, and remedial actions
