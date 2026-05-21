"""Game-control layer for Gamma Labyrinth epochs and turns."""

from __future__ import annotations

import asyncio
from dataclasses import asdict
from datetime import datetime, timezone
from typing import Dict, List

from gamma_labyrinth.context import RollingContextBuffer
from gamma_labyrinth.core.types import AgentProposal, GameControlState, SandboxResult
from gamma_labyrinth.judge import TrophyJudge
from gamma_labyrinth.teams import build_default_teams, iter_agent_slots, validate_roster


class GameControlError(RuntimeError):
    """Raised for invalid game-control actions."""


class GameController:
    """Owns turn/epoch control without LMS transport or Truth mutation."""

    def __init__(self, epoch_id: str | None = None, max_turns: int = 100):
        self.teams = build_default_teams()
        if not validate_roster(self.teams):
            raise GameControlError("default roster violates Gamma Labyrinth route-blocking constraints")
        self.state = GameControlState(
            epoch_id=epoch_id or datetime.now(timezone.utc).strftime("epoch_%Y%m%dT%H%M%SZ"),
            max_turns=max_turns,
            team_scores={team.team_id: 0.0 for team in self.teams},
        )
        self.context_buffers: Dict[str, RollingContextBuffer] = {
            team.team_id: RollingContextBuffer() for team in self.teams
        }
        self.judge = TrophyJudge()

    async def run_turn_dry_run(self) -> GameControlState:
        if self.state.current_turn >= self.state.max_turns:
            self.state.status = "epoch_complete"
            return self.state
        self.state.current_turn += 1
        self.state.status = "running_dry_run"
        tasks = [self._build_dry_run_result(agent.agent_id, agent.team_id) for agent in iter_agent_slots(self.teams)]
        results = await asyncio.gather(*tasks)
        for result in results:
            decision = self.judge.evaluate(result)
            self.state.last_decision = decision
            self.state.team_scores[result.proposal.team_id] += decision.score_delta
            self.context_buffers[result.proposal.team_id].append_execution_log(
                f"turn={self.state.current_turn}; agent={result.proposal.agent_id}; decision={decision.decision}"
            )
        if self.state.current_turn >= self.state.max_turns:
            self.state.status = "epoch_complete"
        return self.state

    async def _build_dry_run_result(self, agent_id: str, team_id: str) -> SandboxResult:
        self.context_buffers[team_id].build_prompt(self.state.current_turn, team_id)
        proposal = AgentProposal(
            agent_id=agent_id,
            team_id=team_id,
            turn=self.state.current_turn,
            proposed_patch="# dry-run proposal placeholder; no TFNE source mutation",
        )
        return SandboxResult(
            proposal=proposal,
            executed=False,
            dry_run=True,
            stdout="[DRY RUN] sandbox execution bypassed",
        )

    async def run_epoch_dry_run(self) -> GameControlState:
        while self.state.current_turn < self.state.max_turns:
            await self.run_turn_dry_run()
        return self.state

    def status_payload(self) -> Dict[str, object]:
        return {
            "ok": True,
            "controller": asdict(self.state),
            "truth_status": "truth_safe_unverified",
            "truth_bearing_run": False,
            "teams": [asdict(team) for team in self.teams],
        }
