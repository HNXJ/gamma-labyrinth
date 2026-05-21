import pytest

from gamma_labyrinth.controls import GameController
from gamma_labyrinth.teams import build_default_teams, validate_roster


def test_default_roster_route_blocked():
    teams = build_default_teams()
    assert validate_roster(teams) is True
    assert len(teams) == 4
    assert sum(len(team.agents) for team in teams) == 16
    for team in teams:
        assert sum(agent.model_family == "gemma_31b_core" for agent in team.agents) == 2
        assert sum(agent.model_family == "gemma_26b_agent" for agent in team.agents) == 2
        assert all(agent.route_ready is False for agent in team.agents)


@pytest.mark.asyncio
async def test_game_controller_dry_run_turn_is_truth_safe():
    controller = GameController(max_turns=1)
    state = await controller.run_turn_dry_run()
    assert state.current_turn == 1
    assert state.status == "epoch_complete"
    assert state.truth_status == "truth_safe_unverified"
    assert state.truth_bearing_run is False
    assert set(state.team_scores) == {"A", "B", "C", "D"}
