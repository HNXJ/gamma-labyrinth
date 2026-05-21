"""Team roster controls for Gamma Labyrinth."""

from __future__ import annotations

from typing import Iterator, List

from gamma_labyrinth.core.types import AgentSlot, Team

TEAM_IDS = ("A", "B", "C", "D")


def build_default_teams() -> List[Team]:
    teams: List[Team] = []
    for team_id in TEAM_IDS:
        agents: List[AgentSlot] = []
        for idx in range(1, 3):
            agents.append(
                AgentSlot(
                    agent_id=f"{team_id}_31b_{idx}",
                    team_id=team_id,
                    model_family="gemma_31b_core",
                    model_label="Gemma-31B-Core",
                    harness_id=f"harness_{team_id}_31b_{idx}",
                )
            )
            agents.append(
                AgentSlot(
                    agent_id=f"{team_id}_26b_{idx}",
                    team_id=team_id,
                    model_family="gemma_26b_agent",
                    model_label="Gemma-26B-Agent",
                    harness_id=f"harness_{team_id}_26b_{idx}",
                )
            )
        teams.append(Team(team_id=team_id, agents=agents))
    return teams


def iter_agent_slots(teams: List[Team]) -> Iterator[AgentSlot]:
    for team in teams:
        yield from team.agents


def validate_roster(teams: List[Team]) -> bool:
    if [team.team_id for team in teams] != list(TEAM_IDS):
        return False
    for team in teams:
        if len(team.agents) != 4:
            return False
        if sum(a.model_family == "gemma_31b_core" for a in team.agents) != 2:
            return False
        if sum(a.model_family == "gemma_26b_agent" for a in team.agents) != 2:
            return False
        if any(agent.route_ready for agent in team.agents):
            return False
        if any(agent.route_block_reason != "baseline_load_not_verified" for agent in team.agents):
            return False
    return True
