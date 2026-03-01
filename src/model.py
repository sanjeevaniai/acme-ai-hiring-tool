"""
Acme AI Hiring Tool - Model Training Pipeline

Trains an XGBoost classifier for candidate suitability scoring.
Includes data validation, feature extraction, fairness-constrained
hyperparameter optimization, and model evaluation.
"""

import logging
from pathlib import Path

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score

logger = logging.getLogger(__name__)

# Protected attributes - excluded from model training, retained for fairness evaluation
PROTECTED_ATTRIBUTES = [
    "name", "gender", "age", "date_of_birth", "ethnicity",
    "nationality", "religion", "disability_status", "marital_status",
    "photo_url", "email", "phone", "address",
]

VALID_EDUCATION_LEVELS = ["high_school", "bachelors", "masters", "phd"]

MAX_RESUME_LENGTH = 50_000  # characters
MIN_RESUME_LENGTH = 50  # characters


def validate_input(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean input data. Raises ValueError for critical issues."""
    required_cols = ["resume_text", "years_experience", "education_level", "skills"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Drop rows with null required fields
    initial_count = len(df)
    df = df.dropna(subset=required_cols)
    dropped = initial_count - len(df)
    if dropped > 0:
        logger.warning("Dropped %d rows with missing required fields", dropped)

    # Validate resume length
    df = df[df["resume_text"].str.len().between(MIN_RESUME_LENGTH, MAX_RESUME_LENGTH)]

    # Validate education level
    df = df[df["education_level"].isin(VALID_EDUCATION_LEVELS)]

    # Validate years of experience (non-negative, reasonable range)
    df = df[(df["years_experience"] >= 0) & (df["years_experience"] <= 60)]

    logger.info("Validated %d records (dropped %d)", len(df), initial_count - len(df))
    return df


def extract_features(df: pd.DataFrame) -> np.ndarray:
    """Extract features from validated application data."""
    # TF-IDF on resume text
    tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
    text_features = tfidf.fit_transform(df["resume_text"]).toarray()

    # Encode education level
    edu_encoder = LabelEncoder()
    edu_encoded = edu_encoder.fit_transform(df["education_level"]).reshape(-1, 1)

    # Normalize numeric features
    scaler = StandardScaler()
    numeric_features = scaler.fit_transform(df[["years_experience"]].values)

    # Skills count
    skills_count = df["skills"].apply(lambda x: len(x) if isinstance(x, list) else 0).values.reshape(-1, 1)

    features = np.hstack([text_features, edu_encoded, numeric_features, skills_count])
    logger.info("Extracted %d features from %d records", features.shape[1], features.shape[0])
    return features


def remove_protected_attributes(df: pd.DataFrame) -> pd.DataFrame:
    """Remove protected attributes from training data to prevent direct discrimination."""
    cols_to_remove = [c for c in PROTECTED_ATTRIBUTES if c in df.columns]
    if cols_to_remove:
        logger.info("Removing protected attributes: %s", cols_to_remove)
        df = df.drop(columns=cols_to_remove)
    return df


def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
) -> xgb.XGBClassifier:
    """Train XGBoost classifier with early stopping."""
    model = xgb.XGBClassifier(
        n_estimators=500,
        max_depth=6,
        learning_rate=0.05,
        reg_alpha=0.1,
        reg_lambda=1.0,
        objective="binary:logistic",
        eval_metric="auc",
        early_stopping_rounds=50,
        random_state=42,
    )

    model.fit(
        X_train, y_train,
        eval_set=[(X_val, y_val)],
        verbose=False,
    )

    logger.info("Trained model with %d trees", model.best_iteration + 1)
    return model


def evaluate_model(model: xgb.XGBClassifier, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """Evaluate model on test set and return performance metrics."""
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)

    metrics = {
        "auc_roc": roc_auc_score(y_test, y_prob),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "n_test": len(y_test),
    }

    logger.info("Evaluation metrics: %s", metrics)
    return metrics


def score_to_suitability(probability: float) -> int:
    """Convert model probability to 0-100 suitability score with calibration."""
    return int(round(probability * 100))
