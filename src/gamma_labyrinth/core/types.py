"""Shared Gamma Labyrinth game-control datatypes.

These types live in `gamma-labyrinth`, the game-control/server/judge repo.
They do not implement LMS transport and do not mutate Truth-plane state.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Optional

TRUTH_SAFE_UNVERIFIED = "truth_safe_unverified"


@dataclass(frozen=True)
class AgentSlot:
    agent_id: str
    team_id: str
    model_family: str
    model_label: str
    harness_id: str
    truth_mode: str = TRUTH_SAFE_UNVERIFIED
    route_ready: bool = False
    route_block_reason: str = "baseline_load_not_verified"


@dataclass(frozen=True)
class Team:
    team_id: str
    agents: List[AgentSlot]


@dataclass(frozen=True)
class AgentProposal:
    agent_id: str
    team_id: str
    turn: int
    proposed_patch: str
    claim_type: str = "proposal_value"
    truth_status: str = TRUTH_SAFE_UNVERIFIED
    receipt_required: bool = True
    truth_mutation_requested: bool = False


@dataclass(frozen=True)
class SandboxResult:
    proposal: AgentProposal
    executed: bool
    dry_run: bool
    stdout: str = ""
    stderr: str = ""
    previous_vector: Optional[List[float]] = None
    candidate_vector: Optional[List[float]] = None
    target_vector: Optional[List[float]] = None
    artifact_paths: List[str] = field(default_factory=list)
    truth_status: str = TRUTH_SAFE_UNVERIFIED


@dataclass(frozen=True)
class JudgeDecision:
    decision: str
    score_delta: float
    reason: str
    truth_status: str = TRUTH_SAFE_UNVERIFIED
    truth_mutation_allowed: bool = False
    receipt_required: bool = True


@dataclass
class GameControlState:
    epoch_id: str
    current_turn: int = 0
    max_turns: int = 100
    status: str = "initialized"
    truth_status: str = TRUTH_SAFE_UNVERIFIED
    truth_bearing_run: bool = False
    team_scores: Dict[str, float] = field(default_factory=dict)
    last_decision: Optional[JudgeDecision] = None

    def as_dict(self) -> Mapping[str, object]:
        return {
            "epoch_id": self.epoch_id,
            "current_turn": self.current_turn,
            "max_turns": self.max_turns,
            "status": self.status,
            "truth_status": self.truth_status,
            "truth_bearing_run": self.truth_bearing_run,
            "team_scores": dict(self.team_scores),
            "last_decision": None if self.last_decision is None else self.last_decision.__dict__,
        }
