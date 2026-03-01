"""
Acme AI Hiring Tool - Post-Deployment Monitoring

Monitors model performance, data drift, and fairness metrics
in production. Generates alerts when thresholds are exceeded.
Supports post-market surveillance per EU AI Act Article 72.
"""

import logging
from dataclasses import dataclass

import numpy as np
from scipy import stats

logger = logging.getLogger(__name__)


@dataclass
class DriftAlert:
    """Alert generated when drift is detected."""
    metric_name: str
    current_value: float
    threshold: float
    severity: str  # "warning" or "critical"
    message: str


def population_stability_index(reference: np.ndarray, current: np.ndarray, bins: int = 10) -> float:
    """
    Calculate Population Stability Index (PSI) to detect feature drift.

    PSI < 0.1: No significant drift
    PSI 0.1-0.2: Moderate drift (warning)
    PSI > 0.2: Significant drift (critical)
    """
    breakpoints = np.linspace(
        min(reference.min(), current.min()),
        max(reference.max(), current.max()),
        bins + 1,
    )

    ref_counts = np.histogram(reference, bins=breakpoints)[0] / len(reference)
    cur_counts = np.histogram(current, bins=breakpoints)[0] / len(current)

    # Avoid division by zero
    ref_counts = np.clip(ref_counts, 1e-6, None)
    cur_counts = np.clip(cur_counts, 1e-6, None)

    psi = np.sum((cur_counts - ref_counts) * np.log(cur_counts / ref_counts))
    return float(psi)


def ks_test(reference: np.ndarray, current: np.ndarray) -> tuple[float, float]:
    """
    Kolmogorov-Smirnov test for distribution shift.

    Returns (statistic, p_value). Alert if p_value < 0.05.
    """
    stat, p_value = stats.ks_2samp(reference, current)
    return float(stat), float(p_value)


def check_drift(
    reference_scores: np.ndarray,
    current_scores: np.ndarray,
    psi_warning: float = 0.1,
    psi_critical: float = 0.2,
    ks_alpha: float = 0.05,
) -> list[DriftAlert]:
    """Check for score distribution drift using PSI and KS test."""
    alerts = []

    # PSI check
    psi = population_stability_index(reference_scores, current_scores)
    if psi > psi_critical:
        alerts.append(DriftAlert(
            metric_name="PSI",
            current_value=psi,
            threshold=psi_critical,
            severity="critical",
            message=f"Critical score drift detected (PSI={psi:.3f} > {psi_critical})",
        ))
    elif psi > psi_warning:
        alerts.append(DriftAlert(
            metric_name="PSI",
            current_value=psi,
            threshold=psi_warning,
            severity="warning",
            message=f"Moderate score drift detected (PSI={psi:.3f} > {psi_warning})",
        ))

    # KS test
    ks_stat, p_value = ks_test(reference_scores, current_scores)
    if p_value < ks_alpha:
        alerts.append(DriftAlert(
            metric_name="KS_test",
            current_value=p_value,
            threshold=ks_alpha,
            severity="warning",
            message=f"Distribution shift detected (KS p-value={p_value:.4f} < {ks_alpha})",
        ))

    for alert in alerts:
        logger.warning("DRIFT_ALERT | %s | %s", alert.severity.upper(), alert.message)

    return alerts


def check_fairness_drift(
    selection_rates: dict[str, float],
    reference_group: str = "male",
    threshold: float = 0.80,
) -> list[DriftAlert]:
    """
    Check if demographic parity ratios fall below the 4/5ths threshold.

    Args:
        selection_rates: Dict mapping group names to selection rates
        reference_group: Group to use as reference for ratio calculation
        threshold: Minimum acceptable ratio (0.80 = 4/5ths rule)
    """
    alerts = []
    ref_rate = selection_rates.get(reference_group)
    if ref_rate is None or ref_rate == 0:
        return alerts

    for group, rate in selection_rates.items():
        if group == reference_group:
            continue
        ratio = rate / ref_rate
        if ratio < threshold:
            alerts.append(DriftAlert(
                metric_name=f"disparate_impact_{group}",
                current_value=ratio,
                threshold=threshold,
                severity="critical",
                message=(
                    f"Fairness violation: {group} selection rate ratio "
                    f"({ratio:.3f}) below {threshold} threshold"
                ),
            ))

    for alert in alerts:
        logger.error("FAIRNESS_ALERT | %s | %s", alert.severity.upper(), alert.message)

    return alerts
