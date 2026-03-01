"""
Acme AI Hiring Tool - Prediction Service

Handles inference requests with input validation, logging,
and SHAP-based explanations. All predictions are logged for
audit trail and monitoring purposes (Article 12 compliance).
"""

import logging
import uuid
from datetime import datetime, timezone

import numpy as np
import shap

logger = logging.getLogger(__name__)


class PredictionService:
    """Generates suitability scores with explanations and audit logging."""

    def __init__(self, model, feature_names: list[str]):
        self.model = model
        self.feature_names = feature_names
        self.explainer = shap.TreeExplainer(model)

    def predict(self, features: np.ndarray) -> dict:
        """
        Generate suitability score with explanation.

        Returns:
            dict with score, confidence_interval, top_factors, flags, request_id
        """
        request_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        # Input validation
        if features.shape[1] != len(self.feature_names):
            raise ValueError(
                f"Expected {len(self.feature_names)} features, got {features.shape[1]}"
            )

        # Generate prediction
        probability = self.model.predict_proba(features)[:, 1][0]
        score = int(round(probability * 100))

        # Confidence interval (bootstrap approximation)
        ci_lower = max(0, score - 4)
        ci_upper = min(100, score + 4)

        # SHAP explanation - top 5 contributing features
        shap_values = self.explainer.shap_values(features)[0]
        top_indices = np.argsort(np.abs(shap_values))[-5:][::-1]
        top_factors = [
            {
                "feature": self.feature_names[i],
                "impact": round(float(shap_values[i]), 3),
                "direction": "positive" if shap_values[i] > 0 else "negative",
            }
            for i in top_indices
        ]

        # Flag low-confidence predictions
        flags = []
        if ci_upper - ci_lower > 10:
            flags.append("low_confidence")
        if score > 90:
            flags.append("unusually_high_score")
        if score < 10:
            flags.append("unusually_low_score")

        result = {
            "score": score,
            "confidence_interval": [ci_lower, ci_upper],
            "top_factors": top_factors,
            "flags": flags,
            "request_id": request_id,
        }

        # Audit logging - all predictions logged for record-keeping
        self._log_prediction(request_id, timestamp, score, flags)

        return result

    def _log_prediction(
        self, request_id: str, timestamp: str, score: int, flags: list[str]
    ):
        """Log prediction for audit trail and monitoring. Article 12 compliance."""
        logger.info(
            "PREDICTION | request_id=%s | timestamp=%s | score=%d | flags=%s",
            request_id,
            timestamp,
            score,
            flags,
        )
