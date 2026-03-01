# Acme AI Hiring Tool

**Version:** 2.1.0
**Last Updated:** 2026-02-15
**Risk Classification:** High-Risk AI System (EU AI Act, Annex III, Section 4(a))

## Overview

Acme AI Hiring Tool is a machine-learning-powered candidate screening system used by HR departments to rank and shortlist job applicants. The system processes structured application data (resume text, skills, experience years, education level) and outputs a suitability score from 0-100.

This system is classified as **high-risk** under the EU AI Act because it is used in employment, workers management, and access to self-employment (Article 6(2), Annex III, Area 4).

## Intended Use

- **Purpose:** Assist HR recruiters in screening large applicant pools by generating suitability scores
- **Users:** Trained HR professionals at Acme Corp and its clients
- **Scope:** Pre-screening stage only. Final hiring decisions are always made by human recruiters
- **Not intended for:** Automated rejection without human review, performance evaluation of existing employees, or any use outside of recruitment screening

## Architecture

```
Application Data (CSV/API)
        |
   Data Validation & Cleaning
        |
   Feature Extraction (NLP + structured)
        |
   XGBoost Ensemble Model
        |
   Suitability Score (0-100)
        |
   Human Reviewer Dashboard
```

## Key Components

| Component | Description | Location |
|-----------|-------------|----------|
| Data pipeline | Ingestion, validation, cleaning | `src/model.py` |
| Prediction engine | XGBoost inference with logging | `src/predict.py` |
| Monitoring | Drift detection, performance tracking | `src/monitoring.py` |
| Fairness tests | Demographic parity, disparate impact | `tests/test_fairness.py` |
| Robustness tests | Edge cases, distribution shift | `tests/test_robustness.py` |
| Security tests | Input validation, access control | `tests/test_security.py` |

## Regulatory Compliance

This system is subject to the EU AI Act (Regulation 2024/1689). Compliance documentation is maintained in the `docs/` directory:

- [Risk Assessment](docs/risk_assessment.md) - Risk classification and mitigation
- [Data Governance](docs/data_governance.md) - Training data quality and management
- [Fairness Analysis](docs/fairness_analysis.md) - Bias testing and non-discrimination
- [Transparency Notice](docs/transparency_notice.md) - User disclosures
- [Human Oversight](docs/human_oversight.md) - Override and intervention mechanisms
- [Security Policy](docs/security_policy.md) - Cybersecurity measures
- [Technical Documentation](docs/technical_documentation.md) - Annex IV documentation

## Model Performance

| Metric | Value |
|--------|-------|
| AUC-ROC | 0.87 |
| Precision@80 | 0.82 |
| Recall@80 | 0.79 |
| F1 Score | 0.80 |

See [MODEL_CARD.md](MODEL_CARD.md) for detailed performance breakdown by demographic group.

## Quick Start

```bash
pip install -r requirements.txt
python src/predict.py --input candidates.csv --output scores.csv
```

## Testing

```bash
pytest tests/ -v
```

## Contact

- **AI Governance Lead:** compliance@acmecorp.example.com
- **Technical Lead:** ai-team@acmecorp.example.com
- **Data Protection Officer:** dpo@acmecorp.example.com

## License

Proprietary. See [LICENSE](LICENSE) for terms.
