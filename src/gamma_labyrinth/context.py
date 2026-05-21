"""Rolling prompt context for Gamma Labyrinth turns."""

from __future__ import annotations

from typing import Any, List

TRUTH_SAFE_BANNER = (
    "Gamma Labyrinth continuity: scientific game, plane separation, "
    "truth_mode=truth_safe_unverified, no Truth-plane mutation without receipt."
)


class RollingContextBuffer:
    def __init__(self, max_tokens: int = 131072, max_logs: int = 5):
        self.max_tokens = max_tokens
        self.max_logs = max_logs
        self.tfne_state = "{}"
        self.logs: List[str] = []
        self.score_delta = "{}"
        self.truth_mode = "truth_safe_unverified"

    def append_execution_log(self, log: str) -> None:
        self.logs.append(log)
        if len(self.logs) > self.max_logs:
            self.logs = self.logs[-self.max_logs :]

    def set_tfne_state(self, state: Any) -> None:
        self.tfne_state = str(state)

    def set_score_delta(self, delta: Any) -> None:
        self.score_delta = str(delta)

    def build_prompt(self, turn: int, team_id: str) -> str:
        prompt = (
            f"[WORLD LAW BANNER] {TRUTH_SAFE_BANNER}\n"
            f"Team: {team_id}\n"
            f"Turn: {turn}\n"
            f"Truth Mode: {self.truth_mode}\n"
            f"Score Delta: {self.score_delta}\n"
            f"TFNE State: {self.tfne_state}\n"
            "Recent Logs:\n"
            + "\n".join(self.logs)
        )
        max_chars = self.max_tokens * 4
        if len(prompt) > max_chars:
            prompt = prompt[-max_chars:]
        return prompt
