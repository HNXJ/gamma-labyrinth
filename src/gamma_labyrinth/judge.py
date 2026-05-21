"""Trophy Judge controls for Gamma Labyrinth.

The judge may score sandbox outputs, but it never mutates Truth-plane state.
Acceptance here means a candidate control decision, not accepted scientific truth.
"""

from __future__ import annotations

import math
from typing import Iterable, List

from gamma_labyrinth.core.types import JudgeDecision, SandboxResult


class JudgeInputError(ValueError):
    """Raised when a sandbox result cannot be judged numerically."""


def _as_float_vector(values: Iterable[float], name: str) -> List[float]:
    vector = [float(v) for v in values]
    if not vector:
        raise JudgeInputError(f"{name} is empty")
    if any(not math.isfinite(v) for v in vector):
        raise JudgeInputError(f"{name} contains non-finite values")
    return vector


def euclidean_distance(a: Iterable[float], b: Iterable[float]) -> float:
    av = _as_float_vector(a, "a")
    bv = _as_float_vector(b, "b")
    if len(av) != len(bv):
        raise JudgeInputError("vector length mismatch")
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(av, bv)))


class TrophyJudge:
    """Immutable-style evaluator for directional TFNE vector capture."""

    def evaluate(self, result: SandboxResult) -> JudgeDecision:
        if result.truth_status != "truth_safe_unverified":
            return JudgeDecision(
                decision="REJECT_INVALID",
                score_delta=0.0,
                reason="sandbox_result_attempted_non_safe_truth_status",
            )
        if not result.executed:
            return JudgeDecision(
                decision="DRY_RUN_NO_SCORE",
                score_delta=0.0,
                reason="sandbox_not_executed",
            )
        if result.previous_vector is None or result.candidate_vector is None or result.target_vector is None:
            return JudgeDecision(
                decision="REVISE_PROVENANCE_GAP",
                score_delta=0.0,
                reason="missing_previous_candidate_or_target_vector",
            )
        previous_distance = euclidean_distance(result.previous_vector, result.target_vector)
        candidate_distance = euclidean_distance(result.candidate_vector, result.target_vector)
        delta = previous_distance - candidate_distance
        if delta > 0:
            return JudgeDecision(
                decision="ACCEPT_CANDIDATE",
                score_delta=delta,
                reason="candidate_moved_toward_target_vector",
            )
        if delta == 0:
            return JudgeDecision(
                decision="NO_CHANGE",
                score_delta=0.0,
                reason="candidate_did_not_change_target_distance",
            )
        return JudgeDecision(
            decision="REJECT_CANDIDATE",
            score_delta=delta,
            reason="candidate_moved_away_from_target_vector",
        )
