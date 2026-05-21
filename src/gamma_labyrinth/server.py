"""Minimal HTTP server for Gamma Labyrinth game controls.

This server is intentionally observation/control oriented. It does not call LMS
models and does not mutate Truth-plane state.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, Tuple
from urllib.parse import urlparse

from gamma_labyrinth.controls import GameController
from gamma_labyrinth.core.types import AgentProposal, SandboxResult
from gamma_labyrinth.judge import TrophyJudge


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: Dict[str, Any]) -> None:
    body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class GammaLabyrinthRequestHandler(BaseHTTPRequestHandler):
    controller = GameController(max_turns=100)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003 - stdlib hook
        return

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/health":
            _json_response(self, 200, {"ok": True, "service": "gamma-labyrinth", "truth_status": "truth_safe_unverified"})
            return
        if path == "/api/status":
            _json_response(self, 200, self.controller.status_payload())
            return
        if path == "/api/rules":
            _json_response(
                self,
                200,
                {
                    "ok": True,
                    "rules_source_repo": "gamma-protocol",
                    "truth_status": "truth_safe_unverified",
                    "rules": [
                        "LMS interface lives in gamma.",
                        "Game controls, judge, and server live in gamma-labyrinth.",
                        "Rules and contracts live in gamma-protocol Markdown.",
                        "No Truth-plane mutation without receipt-backed THETA validation.",
                    ],
                },
            )
            return
        if path == "/api/judge/dry-run":
            proposal = AgentProposal(agent_id="dry_run_agent", team_id="A", turn=0, proposed_patch="# none")
            result = SandboxResult(proposal=proposal, executed=False, dry_run=True)
            decision = TrophyJudge().evaluate(result)
            _json_response(self, 200, {"ok": True, "decision": decision.__dict__})
            return
        _json_response(self, 404, {"ok": False, "error": "not_found", "truth_status": "truth_safe_unverified"})

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/turn/dry-run":
            state = asyncio.run(self.controller.run_turn_dry_run())
            _json_response(self, 200, {"ok": True, "state": state.as_dict()})
            return
        _json_response(self, 404, {"ok": False, "error": "not_found", "truth_status": "truth_safe_unverified"})


def make_server(host: str = "127.0.0.1", port: int = 8765) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), GammaLabyrinthRequestHandler)


def smoke_payload() -> Dict[str, Any]:
    controller = GameController(max_turns=1)
    state = asyncio.run(controller.run_epoch_dry_run())
    return {"ok": True, "state": state.as_dict(), "truth_status": "truth_safe_unverified"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Gamma Labyrinth control server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--smoke", action="store_true", help="Run one dry-run epoch and exit")
    args = parser.parse_args()
    if args.smoke:
        print(json.dumps(smoke_payload(), indent=2, sort_keys=True))
        return 0
    server = make_server(args.host, args.port)
    print(f"Gamma Labyrinth server listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
