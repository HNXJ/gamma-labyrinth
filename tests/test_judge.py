import pytest

from gamma_labyrinth.core.types import AgentProposal, SandboxResult
from gamma_labyrinth.judge import JudgeInputError, TrophyJudge, euclidean_distance


def proposal():
    return AgentProposal(agent_id="agent", team_id="A", turn=1, proposed_patch="# none")


def test_dry_run_judge_no_score():
    decision = TrophyJudge().evaluate(SandboxResult(proposal=proposal(), executed=False, dry_run=True))
    assert decision.decision == "DRY_RUN_NO_SCORE"
    assert decision.score_delta == 0.0
    assert decision.truth_mutation_allowed is False


def test_vector_delta_accepts_candidate_without_truth_mutation():
    result = SandboxResult(
        proposal=proposal(),
        executed=True,
        dry_run=False,
        previous_vector=[2.0, 0.0],
        candidate_vector=[1.0, 0.0],
        target_vector=[0.0, 0.0],
    )
    decision = TrophyJudge().evaluate(result)
    assert decision.decision == "ACCEPT_CANDIDATE"
    assert decision.score_delta > 0
    assert decision.truth_status == "truth_safe_unverified"
    assert decision.truth_mutation_allowed is False


def test_non_finite_vector_rejected():
    with pytest.raises(JudgeInputError):
        euclidean_distance([float("nan")], [0.0])
