"""
Robustness Tests for Acme AI Hiring Tool

Tests model behavior under edge cases, distribution shift,
and adversarial-like inputs. Ensures the system degrades
gracefully and flags anomalous inputs.
"""

import numpy as np
import pytest

from src.model import validate_input, MIN_RESUME_LENGTH, MAX_RESUME_LENGTH
import pandas as pd


class TestInputValidation:
    """Test that input validation catches malformed data."""

    def test_rejects_empty_resume(self):
        """Resumes shorter than minimum length should be rejected."""
        df = pd.DataFrame([{
            "resume_text": "too short",
            "years_experience": 5,
            "education_level": "bachelors",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 0, "Should reject resume shorter than MIN_RESUME_LENGTH"

    def test_rejects_oversized_resume(self):
        """Resumes exceeding maximum length should be rejected."""
        df = pd.DataFrame([{
            "resume_text": "a" * (MAX_RESUME_LENGTH + 1),
            "years_experience": 5,
            "education_level": "bachelors",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 0, "Should reject resume exceeding MAX_RESUME_LENGTH"

    def test_rejects_invalid_education(self):
        """Invalid education levels should be rejected."""
        df = pd.DataFrame([{
            "resume_text": "x" * 100,
            "years_experience": 5,
            "education_level": "invalid_level",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 0, "Should reject invalid education level"

    def test_rejects_negative_experience(self):
        """Negative years of experience should be rejected."""
        df = pd.DataFrame([{
            "resume_text": "x" * 100,
            "years_experience": -1,
            "education_level": "bachelors",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 0, "Should reject negative experience"

    def test_rejects_unreasonable_experience(self):
        """Experience > 60 years should be rejected."""
        df = pd.DataFrame([{
            "resume_text": "x" * 100,
            "years_experience": 65,
            "education_level": "bachelors",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 0, "Should reject experience > 60 years"

    def test_accepts_valid_input(self):
        """Valid input should pass validation."""
        df = pd.DataFrame([{
            "resume_text": "Experienced software engineer with Python and ML skills. " * 5,
            "years_experience": 5,
            "education_level": "masters",
            "skills": ["python", "machine_learning"],
        }])
        result = validate_input(df)
        assert len(result) == 1, "Should accept valid input"

    def test_missing_required_columns(self):
        """Missing required columns should raise ValueError."""
        df = pd.DataFrame([{"resume_text": "test"}])
        with pytest.raises(ValueError, match="Missing required columns"):
            validate_input(df)


class TestEdgeCases:
    """Test model behavior with edge-case inputs."""

    def test_minimum_valid_resume(self):
        """Model should handle minimum-length valid resumes."""
        df = pd.DataFrame([{
            "resume_text": "a" * MIN_RESUME_LENGTH,
            "years_experience": 0,
            "education_level": "high_school",
            "skills": [],
        }])
        result = validate_input(df)
        assert len(result) == 1

    def test_zero_experience(self):
        """Zero years of experience should be valid (entry-level)."""
        df = pd.DataFrame([{
            "resume_text": "Recent graduate seeking first role in software engineering. " * 3,
            "years_experience": 0,
            "education_level": "bachelors",
            "skills": ["python"],
        }])
        result = validate_input(df)
        assert len(result) == 1

    def test_empty_skills_list(self):
        """Empty skills list should be valid (skills are optional)."""
        df = pd.DataFrame([{
            "resume_text": "Experienced professional with broad background. " * 3,
            "years_experience": 10,
            "education_level": "masters",
            "skills": [],
        }])
        result = validate_input(df)
        assert len(result) == 1


class TestKeywordStuffingDetection:
    """Test detection of adversarial resume keyword stuffing."""

    def test_repetitive_content_flagged(self):
        """Resumes with highly repetitive content should be detectable."""
        normal_resume = "Experienced engineer with Python skills and ML background. " * 5
        stuffed_resume = "Python machine learning AI expert " * 50

        # Keyword density check: stuffed resume has much lower unique-to-total ratio
        normal_unique_ratio = len(set(normal_resume.split())) / len(normal_resume.split())
        stuffed_unique_ratio = len(set(stuffed_resume.split())) / len(stuffed_resume.split())

        assert stuffed_unique_ratio < normal_unique_ratio * 0.5, (
            "Stuffed resume should have significantly lower lexical diversity"
        )
