# Gamma Labyrinth Repository Laws, Runtime Tasks, Debugging Doctrine, and Improvement Plan

**Status:** unified source markdown v1.0  
**Scope:** operational laws for Gamma-family repositories, code, runtime agents, tasks, debugging, and improvement.  
**Plane:** Control/Execution boundary document.  
**Truth status:** Not a truth receipt. This document defines repo laws and tasks. It does not assert current runtime truth or accepted circuit state.

## 0. Source Basis

This document consolidates Gamma Labyrinth continuity/player-harness doctrine, repo-plane separation, truth-safe mode, GitHub Project/Issues coordination, and final project instructions. It is meant to be useful to Claude, Gemini, Antigravity, and future CLI/browser agents.

## 1. Repository Plane Map

| Repo/surface | URL | Plane | Role | Laws |
|---|---|---|---|---|
| `gamma-protocol` | https://github.com/HNXJ/gamma-protocol | Control/Doctrine | laws, contracts, templates, Markdown specs | Markdown-only; no runtime code/artifacts/live schemas |
| `gamma` | https://github.com/HNXJ/gamma | Execution + Truth storage | runtime, solver, adapters, persistence, receipts, harnesses | may execute; must gate truth; must write receipts |
| `gamma-arena` | https://github.com/HNXJ/gamma-arena | Observation | dashboard, UI, browser validation | no hardcoded scientific truth; visual validation required |
| `gamma-analysis` | https://github.com/HNXJ/gamma-analysis | Analysis/evidence | transcript/model-output analysis, benchmarks, reports | interpretation/recommendation only; no Truth mutation |
| `gamma-science` | https://github.com/HNXJ/gamma-science | Scientific source | science references, methods, empirical grounding | verify canonical status before edits |
| `jbiophysic` | https://github.com/HNXJ/jbiophysic | Scientific source/prototype | model rationale, empirical/method code | verify relation to `gamma-science` |
| `hnxj.github.io` | https://github.com/HNXJ/hnxj.github.io | Public observation | static public evidence surface | never source of scientific truth |
| GitHub Project `gamma` | HNXJ GitHub Project | Control ledger | issues, labels, comments, routing board | no secrets; no executable payloads |

Every repo operation must declare plane, repo, branch, scope, evidence, and stop conditions. Cross-plane work requires explicit routing.

## 2. Branch and Status Law

Never assume canonical branch from memory. Before branch-sensitive work, inspect target repo branch/status. Known audit context: `gamma-protocol` default branch may be `master`; `gamma` reports have conflicted historically but recent audit described `main` as stable and `office-dev` as development; `gamma-arena` must be verified before edits. Conflicting branch doctrine routes to DELTA before execution.

Rules:

1. Do not merge to stable branches in routine worker tasks.
2. Use task branch or verified development branch.
3. Promotion to stable requires THETA validation.
4. Unknown repo state is BETA-only until grounded.

## 3. Non-Negotiable Game Laws in Code

Gamma Labyrinth never stops. It may checkpoint, restart, recover, or resume from the latest valid checkpoint, but the world model is continuous. Turns are asynchronous: players, developer-agents, judges, backends, and observers may act independently, but every turn must preserve continuity, provenance, and state discipline. The game is always about scientific analysis, simulation, reasoning, biological modeling, literature/data interpretation, and scientific idea generation. New ideas enter as patches, quests, missions, events, experiments, proposals, or receipts. Every player requires explicit harness/runtime identity. No harness means no valid player run.

Any prompt, code path, dashboard, issue, or runtime feature that violates these laws is drift and must be patched or routed to BETA/DELTA/GAMMA.

## 4. `gamma-protocol` Laws

`gamma-protocol` is the temple: doctrine, orientation, contracts, templates, validation playbooks, and Markdown specs. It is inert at runtime.

Allowed: `.md` normative content, `.gitignore`, CODEOWNERS, and GitHub workflows that enforce documentation policy. Forbidden: `.py`, `.js`, `.ts`, `.toml`, runtime `.json`/`.yaml` schemas, packages, generated artifacts, logs, transcripts, datasets, receipts, or runtime imports from `gamma`.

Required doctrine families: four-plane architecture, Hellenic stack, repo boundaries, neuroscience claim discipline, player harness contract, continuity banner doctrine, receipt/patch/quest/audit/THETA templates, glossary, and reading order.

Doctrine sync pattern: canonical doctrine lives in `gamma-protocol`; runtime-loaded copies live in `gamma`. Example: `gamma-protocol/doctrine/continuity_banner.md` -> `gamma/context/protocols/continuity_banner.md` with source commit, sync timestamp, and sentinel. `gamma` must not import `gamma-protocol` as a package.

## 5. `gamma` Runtime Laws

`gamma` owns execution and truth-bearing gates: orchestration, solver/adapter logic, persistence, receipts, player harnesses, model backends, runtime validation, and truth-state storage.

A run is not truth. A transcript is not truth. A player consensus is not truth. A dashboard is not truth. Truth requires approved adapter-mediated commit and receipt.

### Prompt injection law

Every player-facing prompt must begin with the continuity banner at a central scheduler/prompt chokepoint. Required invariant: banner present exactly once; sentinel prevents duplication; missing banner fails closed; banner SHA256/word count recorded; no unverified neuron count or growth target in banner.

### Player harness law

A player harness must self-declare (`HARNESS_SPEC` or equivalent), assign/verify agent slot, create session manifest before Turn 1, write artifacts under `outputs/runs/<run_id>/`, flush transcript after every turn, write transcript plus `.sha256`, write session-end receipt, distinguish live vs mock, and stop on credential, persistence, redaction, branch, or truth-safety failure.

### Truth-state law

If no verified truth receipt exists, sessions needing active scientific state must use:

```text
truth_mode: truth_safe_unverified
```

Active neuron counts, circuit states, growth targets, accepted streaks, and model states are proposal values unless verified from receipts.

## 6. `gamma-arena` Observation Laws

`gamma-arena` is browser-facing Observation. It must not invent or hardcode active neuron count, layer, area, cell composition, accepted streak, or growth target. It must distinguish receipt-backed truth, live observation, stale state, fallback state, and bridge/API failure. Front agents must perform browser visual validation and must not edit backend truth logic or other repos directly; instead, draft/routable issues.

## 7. `gamma-analysis` Laws

`gamma-analysis` stores derived analysis, reports, transcript audits, model-output reviews, benchmark summaries, figures, tables, and manuscript-facing evidence. It does not mutate Truth-plane state. Its outputs are interpretation or recommendation until routed through Execution and Truth gates.

Required for analysis tasks: source/provenance references, reproducible scripts/notebooks where applicable, output hashes, claim typing, and explicit separation of interpretation, proposal, simulation result, and truth.

## 8. GitHub Project / GAMMA-BUS Laws

Use GitHub Project `gamma` as task table, issues board, routing ledger, and cross-agent control plane. Issues are task envelopes; comments are agent logs; labels/project fields route by repo, plane, agent, risk, status, and evidence. PRs are execution artifacts. Receipts, reports, screenshots, hashes, transcripts, and validation notes are evidence.

Handoffs to Claude, Gemini, Antigravity, or other agents must state target agent/class, repo, plane, task type, allowed scope, forbidden scope, evidence required, stop conditions, and final report format. Reports require footer with agent/model variant. Issues must not carry secrets or arbitrary executable payloads.

## 9. Turn System Law

A turn is an action cycle, not merely a chat reply. Each turn should include continuity banner, mission/study question, truth mode, tools/inventory, prior-turn summary, player decision, code/action when appropriate, artifact capture, drift check, truth-claim typing, and next-turn note. A 20-turn session is a behavioral experiment for drift, tool-use, mission comprehension, artifact persistence, and interaction patterns.

## 10. Continuity Banner Law

All player-facing turns require a compact `<=200` word world-law banner unless superseded by newer canonical `gamma-protocol` doctrine. It must say the agent is already inside the ongoing Gamma Labyrinth world; anchor neuroscience/biophysics/science; define proof-of-work as scientific evidence; enforce plane separation and truth-safe mode; require code/artifacts where appropriate; state that patches/missions/rules may update live; and forbid unverified current neuron counts, secrets, or local paths.

## 11. Biophysical Logic Laws

A neuron is not a counter; it is a modeled unit with class, parameters, connectivity, and validation status. A circuit is not accepted because it runs; it must satisfy model, numerical, and biological gates. Parameters must be extracted or specified honestly; no phantom extraction. LFP, spike, spectral, and gain claims must define observables. Omission modeling must distinguish bottom-up absence from top-down prediction. Post-omission gain requires P4-vs-P3 or equivalent model observable.

## 12. Anti-Drift / Zero-Unpatched-Drift

Hard triggers: cryptocurrency proof-of-work, Ethereum, blockchain, proof-of-stake, ICO, wallet; truth mutation without receipt; accepted-state claim without gate evidence; placeholder-as-implementation; dashboard-as-truth; code-execution claim without artifact/log; stale memory used as active state; player without harness identity.

Soft triggers use two-strike rule: generic coding detached from Gamma, role confusion, mission amnesia, passive refusal despite valid mission, or analogy not tied back to science. Ordinary drift is logged, corrected next turn, and patched. Stop only if drift contaminates truth, credentials, persistence, branch safety, or security.

## 13. Implementation Tasklist

### Runtime and harness

- Verify continuity banner location and scheduler injection.
- Add idempotency/missing-banner tests.
- Add/verify Gemini CLI or equivalent player backend.
- Add player harness with manifest, transcript, artifacts, receipt.
- Enforce `_DRYRUN` segregation and live-vs-mock distinction.
- Add truth-safe state loader or explicit fallback.
- Add redaction scanner and branch/status preflight.

### Truth and science

- Establish canonical truth-state receipt path.
- Create claim ledger schema/spec.
- Add parameter provenance for solver/model runs.
- Add NaN/inf, range, unit, and plausibility gates.
- Add perturbation tests for omission hypotheses.
- Separate voltage-target-hit, gate-accepted, and accepted-streak-closed.

### Observation

- Remove hardcoded scientific truth from dashboards.
- Add stale/fallback labels for bridge/API failure.
- Verify public page sync and observation disclaimer.
- Maintain browser validation checklist.

### GAMMA-BUS

- Use issues as durable request envelopes.
- Enforce routing labels and footer conventions.
- Reject malformed agent messages into receipts/reports.

## 14. Debugging Doctrine

Pre-run checks:

```bash
git status --short
git branch --show-current
python -m py_compile <changed_python_files>
pytest <targeted_tests>
```

Front checks:

```bash
npm run build
npm run typecheck
# plus browser visual validation
```

Harness dry-run:

```bash
python -m src.gamma_runtime.player_harness --dry-run --turns 2 --mock-player
```

Gemini live check:

```bash
gemini auth status
```

or closest equivalent on the execution host.

## 15. Failure Triage

| Failure | Protocol | Action |
|---|---|---|
| unknown repo state | BETA | inspect only |
| branch/truth conflict | DELTA | reconcile, do not execute |
| syntax/test failure | GAMMA | bounded fix, rerun |
| runtime mismatch | THETA | post-execution autopsy |
| secret exposure | GAMMA-BURST | stop, sanitize, rotate if needed |
| science inconsistency | ALPHA -> BETA | plan, audit, then execute |

Stop and report if branch is unsafe, uncommitted changes are not owned, active truth would need hardcoding, transcript/redaction/persistence fails, credentials would need repo/workspace storage, emergency flag is active, heartbeat/session race is detected, or task requires out-of-scope solver/dashboard/credential files.

## 16. Improvement Plan

Phase 0: stabilize doctrine/evidence, keep `gamma-protocol` Markdown-only, normalize continuity banner, require session receipts.  
Phase 1: stabilize player harness, 20-turn sessions, run workspaces, drift detector, live-vs-mock enforcement.  
Phase 2: stabilize truth pipeline, canonical truth loader, receipt-backed state, parameter provenance, perturbation evidence.  
Phase 3: expand scientific missions: DOE Genesis biomarkers, thesis N -> N+1 omission models, multi-agent councils.  
Phase 4: public/DOE-scale translation: reliable public observation, portable local MLX to DOE-scale workflows, reusable templates.

## 17. Definition of Done

A repo task is complete only when scope/plane are declared, changed files listed, compile/type/lint checks pass where applicable, targeted tests pass or failures are reported, artifacts/receipts are written, no secrets introduced, no unverified truth asserted, final report includes evidence and risks, and agent identity footer is included.

