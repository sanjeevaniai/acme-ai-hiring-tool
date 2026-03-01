# Technical Documentation

**Document Owner:** Technical Lead
**Last Updated:** 2026-02-10
**Review Cycle:** Per release
**EU AI Act Reference:** Annex IV

## 1. General Description

### 1.1 System Identity

- **Name:** Acme AI Hiring Tool
- **Version:** 2.1.0
- **Provider:** Acme Corp, 123 Innovation Street, Berlin, Germany
- **EU AI Act Registration:** Pending (to be submitted to EU database upon enforcement)

### 1.2 Intended Purpose

AI-assisted candidate screening system that generates suitability scores (0-100) to assist human recruiters in pre-screening job applicants. The system is intended as a decision-support tool and does not make autonomous hiring decisions.

### 1.3 System Boundaries

- **Input:** Structured application data (resume text, skills, experience, education)
- **Output:** Suitability score (0-100) with confidence interval and feature importance
- **Integration:** REST API consumed by Acme Corp's Applicant Tracking System (ATS)
- **Deployment:** Cloud-hosted (AWS eu-west-1), API-only (no direct candidate-facing interface)

## 2. System Architecture

### 2.1 Component Diagram

```
[Application Portal] → [API Gateway] → [Data Validation Service]
                                              ↓
                                     [Feature Extraction]
                                              ↓
                                     [XGBoost Model Service]
                                              ↓
                                     [Score + Explanation]
                                              ↓
                                     [Recruiter Dashboard]
```

### 2.2 Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Model | XGBoost | 2.0.3 |
| ML Framework | scikit-learn | 1.4.2 |
| Explainability | SHAP | 0.45.0 |
| Fairness | AIF360 | 0.6.1 |
| Monitoring | Evidently | 0.4.15 |
| API | FastAPI | 0.110.0 |
| Infrastructure | AWS (eu-west-1) | N/A |
| Database | PostgreSQL | 16.2 |

### 2.3 Model Architecture

- **Algorithm:** Gradient-boosted decision tree ensemble (XGBoost)
- **Number of trees:** 500
- **Max depth:** 6
- **Learning rate:** 0.05
- **Regularization:** L1=0.1, L2=1.0
- **Number of input features:** 47 (after NLP feature extraction)
- **Output:** Single scalar score (0-100), mapped from probability via calibration

## 3. Training Methodology

### 3.1 Data Preparation

1. Resume text tokenized and embedded using TF-IDF (top 5,000 terms)
2. Structured features normalized (StandardScaler)
3. Missing values imputed (median for numeric, mode for categorical)
4. Training/validation/test split: 80%/10%/10% (stratified by role category)

### 3.2 Training Process

- **Objective:** Binary classification (hired vs. not hired)
- **Optimization:** Bayesian hyperparameter optimization (50 trials)
- **Cross-validation:** 5-fold stratified CV
- **Early stopping:** 50 rounds patience on validation AUC
- **Fairness constraint:** Demographic parity ratio > 0.85 enforced during HPO

### 3.3 Evaluation Protocol

1. Performance metrics computed on held-out test set
2. Fairness metrics computed on demographic subset of test set
3. Calibration assessed via reliability diagram
4. Feature importance analyzed via SHAP
5. Results reviewed by AI Governance team before deployment

## 4. Computational Resources

- **Training:** AWS ml.m5.4xlarge (16 vCPU, 64 GB RAM), ~45 minutes per training run
- **Inference:** AWS ml.t3.large (2 vCPU, 8 GB RAM), < 200ms per prediction
- **Storage:** AWS S3 (encrypted), ~50 GB for all data and artifacts
- **Compute cost:** ~$500/month total

## 5. Instructions for Use

### 5.1 For Deployers

1. Integrate via REST API (OpenAPI spec provided separately)
2. Display AI scores alongside full candidate application data
3. Ensure human reviewer sees all flagged concerns
4. Implement the override mechanism in your ATS interface
5. Display the candidate notification text before application submission

### 5.2 API Specification

```
POST /api/v2/score
Content-Type: application/json
Authorization: Bearer <token>

{
  "resume_text": "string",
  "years_experience": number,
  "education_level": "high_school" | "bachelors" | "masters" | "phd",
  "skills": ["string"],
  "job_description_id": "string"
}

Response:
{
  "score": number (0-100),
  "confidence_interval": [number, number],
  "top_factors": [
    {"feature": "string", "impact": number, "direction": "positive" | "negative"}
  ],
  "flags": ["string"],
  "request_id": "uuid"
}
```

### 5.3 Known Limitations

- English-language resumes only
- Validated for: software engineering, data science, product management roles
- Minimum 50 words in resume text required
- Score accuracy degrades for roles with < 500 historical training examples

## 6. Changes Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 2.1.0 | 2026-01-10 | ML Team | Added age fairness monitoring, retrained with 2025 data |
| 2.0.0 | 2025-07-15 | ML Team | XGBoost migration, NLP features, SHAP explanations |
| 1.0.0 | 2024-11-01 | ML Team | Initial release |

## 7. Post-Market Monitoring

See `monitoring/config.yaml` for automated monitoring configuration and thresholds.

## 8. Record-Keeping

All model training runs, evaluation results, deployment decisions, and incident reports are maintained in the AI governance record-keeping system with audit trail functionality. Records are retained for the lifetime of the system plus 10 years per Article 12 requirements.

### Version Control

- All model code tracked in Git with signed commits
- Model artifacts versioned in MLflow registry
- Configuration changes tracked via Infrastructure-as-Code (Terraform)
- Documentation versioned alongside code in this repository
