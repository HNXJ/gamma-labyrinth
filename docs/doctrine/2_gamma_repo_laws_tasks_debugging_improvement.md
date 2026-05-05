# Gamma Labyrinth Repository Laws, Runtime Tasks, Debugging Doctrine, and Improvement Plan

**Status:** generalized source markdown v1.1  
**Scope:** operational laws for Gamma-family repositories, code, runtime agents, tasks, debugging, repo hygiene, and improvement.  
**Plane:** Control/Execution boundary document.  
**Truth status:** Not a Truth-plane receipt. This document defines repo laws and tasks. It does not assert current runtime truth or accepted circuit state.

## 0. Purpose

This document tells agents how to work safely across the Gamma Labyrinth repository ecosystem. It is generalized: it may refer to relative workspace conventions, repo roles, and coordination rules, but it should not contain private personal context, absolute local paths, or individual thesis-specific goals. Local/personal deployment details belong in a separate local-context markdown.

## 1. Repository Plane Map

| Repo/surface | URL | Plane | Role | Laws |
|---|---|---|---|---|
| `gamma-labyrinth` | https://github.com/HNXJ/gamma-labyrinth | Control/world shell | top-level skeleton, world front door, repo map, onboarding, mission entrypoints | not runtime, not truth storage, not UI duplicate |
| `gamma-protocol` | https://github.com/HNXJ/gamma-protocol | Control/Doctrine | laws, contracts, templates, Markdown specs | Markdown-only; no runtime code/artifacts/live schemas |
| `gamma` | https://github.com/HNXJ/gamma | Execution + Truth storage | runtime, solver, adapters, persistence, receipts, harnesses | may execute; must gate truth; must write receipts |
| `gamma-arena` | https://github.com/HNXJ/gamma-arena | Observation | dashboard, UI, browser validation | no hardcoded scientific truth; visual validation required |
| `gamma-analysis` | https://github.com/HNXJ/gamma-analysis | Analysis/evidence | transcript/model-output analysis, benchmarks, reports | interpretation/recommendation only; no Truth mutation |
| `gamma-science` | https://github.com/HNXJ/gamma-science | Scientific source | science references, methods, empirical grounding | not runtime truth storage |
| `hnxj.github.io` | https://github.com/HNXJ/hnxj.github.io | Public observation | static public evidence surface | never source of scientific truth |
| GitHub Project `gamma` | HNXJ GitHub Project | Control ledger | issues, labels, comments, routing board | no secrets; no executable payloads |

Every repo operation must declare plane, repo, branch, scope, evidence, and stop conditions. Cross-plane work requires explicit routing.

## 2. Generalized Local Clone Roots

Use sibling clone roots rather than hardcoded absolute paths in generalized doctrine:

```text
Gemini/Antigravity: ../gemini-gamma-labyrinth/repos/
Claude/Cowork:     ../claude-gamma-labyrinth/repos/
```

These are relative workspace conventions. A local-context file may map them to absolute machine paths. There should be one canonical clone root per agent family. Do not create duplicate clone trees, alternate workspaces, or shadow repos without explicit approval.

Rules:

1. Gemini and Antigravity work from the Gemini/Antigravity clone root.
2. Claude and Cowork work from the Claude/Cowork clone root.
3. Agents must not write into another family’s clone root without explicit authorization.
4. If a repo is missing from the expected clone root, ask before cloning or moving.
5. If a repo exists both inside and outside the canonical root, route to DELTA before moving/deleting.
6. If local paths differ, the local-context markdown, not this generalized repo-law document, should record the exact paths.

## 3. Branch and Parallel-Agent Law

`main` is the preferred source-of-truth branch for repos unless a repo-specific verified exception exists. `gamma-protocol` may use `master`; verify before claiming. Branch-sensitive work must inspect current status before execution.

Parallel-agent rule:

- Assume Gemini, Antigravity, Claude, and Cowork may work concurrently.
- Check GitHub Project `gamma` or assigned issue ownership before work.
- Run `git status --short --branch` before edits.
- Fetch/pull only when safe and authorized.
- Use bounded commits.
- Use task branches such as `dev-gemini`, `dev-claude`, or issue-specific branches for conflict isolation.
- Pull/push synchronization is required before declaring work complete.
- If `git pull --ff-only` fails, route to DELTA; do not merge by guess.

Zero tolerance:

- no overwriting unowned changes;
- no force-push without explicit authorization;
- no branch doctrine from memory alone;
- no commit mixing unrelated task changes;
- no cross-agent conflict hidden in final report.

## 4. Non-Negotiable Game Laws in Code

Gamma Labyrinth never stops. It may checkpoint, restart, recover, or resume from the latest valid checkpoint, but the world model is continuous. Turns are asynchronous. Players, developer-agents, judges, backends, and observers may act independently, but every turn must preserve continuity, provenance, and state discipline.

The game remains about scientific analysis, simulation, reasoning, biological modeling, literature/data interpretation, and scientific idea generation. New ideas enter as patches, quests, missions, events, experiments, proposals, or receipts. Every player requires explicit harness/runtime identity. No harness means no valid player run.

Any prompt, code path, dashboard, issue, or runtime feature that violates these laws is drift and must be patched or routed to BETA/DELTA/GAMMA.

## 5. `gamma-protocol` Laws

`gamma-protocol` is the doctrine temple: orientation, laws, contracts, templates, validation playbooks, and Markdown specs. It is inert at runtime.

Allowed: `.md` normative content, `.gitignore`, CODEOWNERS, and GitHub workflows that enforce documentation policy. Forbidden: `.py`, `.js`, `.ts`, `.toml`, runtime `.json`/`.yaml` schemas, packages, generated artifacts, logs, transcripts, datasets, receipts, or runtime imports from `gamma`.

Doctrine sync pattern: canonical doctrine lives in `gamma-protocol`; runtime-loaded copies may live in `gamma` with source commit, sync timestamp, and sentinel. `gamma` must not import `gamma-protocol` as a runtime package.

## 6. `gamma` Runtime Laws

`gamma` owns execution and truth-bearing gates: orchestration, solver/adapter logic, persistence, receipts, player harnesses, model backends, runtime validation, and truth-state storage.

A run is not truth. A transcript is not truth. A player consensus is not truth. A dashboard is not truth. Truth requires approved adapter-mediated commit and receipt.

### Prompt injection law

Every player-facing prompt should receive the continuity/world-law banner at a central scheduler/prompt chokepoint. Required invariant: banner present exactly once; sentinel prevents duplication; missing banner fails closed; banner SHA256/word count recorded; no unverified neuron count or growth target in banner.

### Player harness law

A player harness must self-declare, assign/verify agent slot, create session manifest before Turn 1, write artifacts under `outputs/runs/<run_id>/`, flush transcript after each turn, write transcript plus `.sha256`, write session-end receipt, distinguish live vs mock, and stop on credential, persistence, redaction, branch, or truth-safety failure.

### Truth-state law

If no verified truth receipt exists, sessions needing active scientific state must use:

```text
truth_mode: truth_safe_unverified
```

Active neuron counts, circuit states, growth targets, accepted streaks, and model states are proposal values unless verified from receipts.

## 7. `gamma-arena` Observation Laws

`gamma-arena` is browser-facing Observation. It must not invent or hardcode active neuron count, layer, area, cell composition, accepted streak, or growth target. It must distinguish receipt-backed truth, live observation, stale state, fallback state, and bridge/API failure.

Front agents must perform browser visual validation and must not edit backend truth logic or other repos directly. If front work discovers backend needs, draft or route an issue instead of modifying backend code.

User-facing branding should treat **Gamma Labyrinth** as the top-level game/world identity. Gamma Arena may remain as the observation UI subsystem. User-facing “Protocol” pages/labels should generally be “Rules” unless referring to a literal repository or protocol file name.

## 8. `gamma-analysis` Laws

`gamma-analysis` stores derived analysis, reports, transcript audits, model-output reviews, benchmark summaries, figures, tables, and manuscript-facing evidence. It does not mutate Truth-plane state. Outputs are interpretation or recommendation until routed through Execution and Truth gates.

Required for analysis tasks: source/provenance references, reproducible scripts/notebooks where applicable, output hashes, claim typing, and explicit separation of interpretation, proposal, simulation result, and truth.

## 9. `gamma-labyrinth` Skeleton Laws

`gamma-labyrinth` is the world front door and skeleton repo. It may hold orientation, repo index, mission/quest entrypoints, source markdown aggregation, onboarding, templates, and a world map. It must not duplicate backend runtime from `gamma`, frontend UI from `gamma-arena`, analysis archives from `gamma-analysis`, or doctrine authority from `gamma-protocol`.

If staging copies of source markdowns exist outside the canonical repo clone, move/commit them only through an explicit DELTA-approved migration path with hashes and no silent deletion.

## 10. Repo Hygiene and Ignore Policy

All six canonical repos should ignore:

```gitignore
.DS_Store
*.npy
*.mat
```

All six canonical repos except `gamma-arena` should also ignore:

```gitignore
*.html
```

Rationale:

- `.DS_Store` is local OS noise.
- `.npy` and `.mat` are usually generated scientific artifacts and should enter evidence through manifests/receipts, not source clutter.
- `.html` is often rendered/generated output outside the UI repo. `gamma-arena` is the exception because HTML/front assets may be legitimate.

Tracked artifacts matching ignored patterns must not be deleted automatically. Report them as cleanup candidates.

Zero tolerance:

- no committed `.env` secrets;
- no credential-bearing context files;
- no generated binaries as source without explicit approval;
- no local-only path doctrine inside generalized source docs;
- no hidden artifact dependency in a scientific report.

## 11. GitHub Project / GAMMA-BUS Laws

Use GitHub Project `gamma` as task table, issues board, routing ledger, and cross-agent control plane. Issues are task envelopes; comments are agent logs; labels/project fields route by repo, plane, agent, risk, status, and evidence. PRs are execution artifacts. Receipts, reports, screenshots, hashes, transcripts, and validation notes are evidence.

Handoffs to Claude, Gemini, Antigravity, or other agents must state target agent/class, repo, plane, task type, allowed scope, forbidden scope, evidence required, stop conditions, and final report format. Reports require footer with agent/model variant. Issues must not carry secrets or arbitrary executable payloads.

## 12. Turn System Law

A turn is an action cycle, not merely a chat reply. Each turn should include continuity banner, mission/study question, truth mode, tools/inventory, prior-turn summary, player decision, code/action when appropriate, artifact capture, drift check, truth-claim typing, and next-turn note.

A multi-turn session is a behavioral experiment for drift, tool-use, mission comprehension, artifact persistence, and interaction patterns.

## 13. Biophysical Logic Laws

A neuron is not a counter; it is a modeled unit with class, parameters, connectivity, and validation status. A circuit is not accepted because it runs; it must satisfy model, numerical, and biological gates. Parameters must be extracted or specified honestly; no phantom extraction. LFP, spike, spectral, and gain claims must define observables. Omission modeling must distinguish bottom-up absence from top-down prediction.

## 14. Anti-Drift / Zero-Unpatched-Drift

Zero-tolerance drift means no drift may remain unpatched, unlogged, or normalized as acceptable behavior. It does not mean agents cannot be creative. Creativity is encouraged for hypotheses, model proposals, UI design, mission ideas, and analysis routes, as long as outputs are labeled by claim type and validated before truth.

Hard triggers:

- cryptocurrency proof-of-work in place of scientific evidence;
- truth mutation without receipt;
- accepted-state claim without gate evidence;
- placeholder-as-implementation;
- dashboard-as-truth;
- code-execution claim without artifact/log;
- stale memory used as active state;
- player without harness identity;
- secret leakage;
- cross-repo edits outside scope;
- branch conflict ignored.

Soft triggers use two-strike correction: generic coding detached from Gamma, role confusion, mission amnesia, passive refusal despite valid mission, or analogy not tied back to science. Ordinary drift is logged, corrected next turn, and patched. Stop only if drift contaminates truth, credentials, persistence, branch safety, or security.

## 15. Implementation Tasklist

Runtime and harness:

- verify continuity banner location and scheduler injection;
- add idempotency/missing-banner tests;
- add/verify player backends;
- add player harness with manifest, transcript, artifacts, receipt;
- enforce dry-run vs live separation;
- add truth-safe state loader or explicit fallback;
- add redaction scanner and branch/status preflight.

Truth and science:

- establish canonical truth-state receipt path;
- create claim ledger schema/spec;
- add parameter provenance for solver/model runs;
- add NaN/inf, range, unit, and plausibility gates;
- add perturbation tests for scientific hypotheses;
- separate voltage-target-hit, gate-accepted, and accepted-streak-closed.

Observation:

- remove hardcoded scientific truth from dashboards;
- add stale/fallback labels for bridge/API failure;
- verify public page sync and observation disclaimer;
- maintain browser validation checklist.

Repo hygiene:

- keep `.gitignore` rules synchronized;
- sanitize tracked `.env` risk;
- avoid committing generated artifacts;
- update READMEs with repo role, plane, truth-safe note, task-board note, and branch/status discipline.

## 16. Debugging Doctrine

Pre-run checks:

```bash
git status --short --branch
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

If a command requires missing dependencies, report honestly and do not install unless authorized.

## 17. Failure Triage

| Failure | Protocol | Action |
|---|---|---|
| unknown repo state | BETA | inspect only |
| branch/truth conflict | DELTA | reconcile, do not execute |
| syntax/test failure | GAMMA | bounded fix, rerun |
| runtime mismatch | THETA | post-execution autopsy |
| secret exposure | GAMMA-BURST | stop, sanitize, rotate if needed |
| science inconsistency | ALPHA -> BETA | plan, audit, then execute |
| duplicate clone/staging folder | DELTA | compare hashes, ask before move/delete |

Stop and report if branch is unsafe, uncommitted changes are not owned, active truth would need hardcoding, transcript/redaction/persistence fails, credentials would need repo/workspace storage, emergency flag is active, heartbeat/session race is detected, or task requires out-of-scope files.

## 18. Definition of Done

A repo task is complete only when scope/plane are declared, changed files listed, compile/type/lint checks pass where applicable, targeted tests pass or failures are reported, artifacts/receipts are written when applicable, no secrets are introduced, no unverified truth is asserted, final report includes evidence and risks, and agent identity footer is included.
