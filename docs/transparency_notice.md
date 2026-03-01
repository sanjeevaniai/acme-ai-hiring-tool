# Transparency Notice

**Document Owner:** Compliance & Legal
**Last Updated:** 2026-01-15
**Review Cycle:** Semi-annual

## Purpose

This document describes the transparency and information provisions for the Acme AI Hiring Tool, in compliance with Article 13 of the EU AI Act and GDPR Articles 13-14.

## Notification to Candidates

### Pre-Application Disclosure

All candidates are informed about AI involvement **before** submitting their application through:

1. **Application Portal Notice:** A visible banner on the application page stating:
   > "Acme Corp uses AI-assisted screening to help evaluate applications. Your application will be reviewed by our AI system to generate a preliminary suitability score. This score is used by our human recruiters as one factor among many in the screening process. You have the right to request a human-only review."

2. **Privacy Notice Update:** The recruitment privacy notice (linked from the application form) includes a dedicated section on automated decision-making per GDPR Article 22.

3. **FAQ Page:** A publicly accessible FAQ explaining how the AI system works, what data it uses, and candidate rights.

### Post-Screening Disclosure

Candidates who proceed to interview stage may request:
- Confirmation that AI screening was used
- The main factors that influenced their suitability score (feature importance via SHAP values)
- Whether any automated rejection was involved (our policy prohibits this)

## Information for Deployers

Organizations using the Acme AI Hiring Tool receive:

### Technical Documentation Package

- Model card with performance metrics and limitations
- Data governance documentation
- Fairness analysis results
- Integration guide with human oversight requirements
- Incident reporting procedures

### Deployment Requirements

Deployers must:
1. Display the AI screening notification to all candidates
2. Ensure human review of all AI-generated scores before making hiring decisions
3. Maintain an appeals process for candidates
4. Report any suspected bias or malfunction within 24 hours
5. Complete the deployer training program before system activation

## Explainability

### Score Explanation Method

- **Technique:** SHAP (SHapley Additive exPlanations) values
- **Scope:** Top 5 contributing features per prediction
- **Format:** Natural language summary generated from SHAP output
- **Example:** "Your suitability score was primarily influenced by: relevant skills match (high positive), years of experience (moderate positive), education alignment (moderate positive)"

### Limitations of Explanations

- SHAP values are approximations and may not capture all model dynamics
- Feature interactions are simplified in natural language summaries
- Explanations cover the model's reasoning, not the final hiring decision (which includes human judgment)

## AI-Generated Content Labeling

This system does not generate content presented as human-created. All AI outputs are clearly labeled:
- Suitability scores are displayed with "AI-Generated" label
- Explanations are prefixed with "AI-Generated Explanation:"
- No deepfake, synthetic media, or AI-generated text is produced by this system

## Record Keeping

All transparency-related activities are logged:
- Candidate notification timestamps
- Explanation requests and responses
- Appeals filed and outcomes
- Deployer training completion records

Logs are retained for 5 years per regulatory requirements.

## Contact

For transparency-related inquiries:
- **Candidates:** transparency@acmecorp.example.com
- **Deployers:** compliance@acmecorp.example.com
- **Regulators:** regulatory@acmecorp.example.com
