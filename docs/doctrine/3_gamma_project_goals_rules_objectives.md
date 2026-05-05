# Gamma Labyrinth Project Doctrine: Goals, Rules, Objectives, and Scientific Validation

**Status:** generalized source markdown v1.1  
**Scope:** Gamma Labyrinth as a long-term scientific-discovery game, multi-agent scientific reasoning platform, and biophysical modeling world.  
**Plane:** Control doctrine synthesis.  
**Truth status:** Not a Truth-plane receipt. This document defines goals and rules. It does not assert current biological truth, current neuron count, accepted model state, active branch state, or runtime state.

## 0. Purpose

Gamma Labyrinth is a continuous open-world scientific-discovery game for agentic AI systems. Gamma Council is the reasoning/council layer. Gamma Arena is the live observation/game UI. Gamma Labyrinth exists to support autonomous scientific discovery: literature/data analysis, biophysical modeling, simulation, reasoning, hypothesis generation, scientific validation, and iterative improvement.

This generalized doctrine must remain portable. It may define the scientific game, repo architecture, validation standards, and mission mechanics. It should not contain private local paths, personal thesis commitments, or machine-specific state. Such details belong in a local-context markdown.

## 1. North Star

Gamma Labyrinth is not merely a dashboard or an agent chat. It is an operational scaffold for AI-assisted science. The game metaphor enforces persistent state, player identities, missions, quests, inventories, turn semantics, evidence artifacts, and world laws. The scientific standard is stricter: meaningful claims must be grounded in data, literature, simulation, validation gates, and receipts.

Long-term capabilities:

- read and operationalize scientific literature without unsupported claims;
- analyze structured and semi-structured datasets;
- propose mechanistic hypotheses and executable analyses;
- build, tune, and perturb biophysical models;
- compare model predictions against empirical data;
- coordinate multiple agents without losing provenance;
- generate transparent evidence artifacts, not just prose;
- patch missions and doctrine live without scientific drift;
- scale from local workflows to larger scientific infrastructure without breaking truth discipline.

## 2. Non-Negotiable Game Laws

1. The game never stops. It may restart/recover/resume from the latest valid checkpoint, but the world model is continuous.
2. Turns are asynchronous. Players, developer-agents, judges, backends, and observers may act independently, but every turn must preserve continuity, provenance, and state discipline.
3. The game is always about scientific analysis, simulation, reasoning, biological modeling, literature/data interpretation, and scientific idea generation.
4. New ideas enter as patches, quests, missions, events, experiments, proposals, or receipts.
5. Every player requires explicit harness/runtime identity: API key/API URL/model backend/harness/session identity or equivalent execution contract. No harness means no valid player run.
6. Violations in prompts, code, dashboards, issues, runtime paths, or behavior route to BETA, DELTA, or GAMMA depending on severity.

## 3. Zero-Tolerance Doctrine

Zero tolerance means violations must not be ignored, normalized, or carried forward unpatched. It does not suppress creativity. Creative hypotheses, model variants, UI designs, mission ideas, and analysis strategies are encouraged when they are labeled as proposals and tested before truth.

Zero tolerance applies to:

- unreceipted truth claims;
- hardcoded active scientific state;
- dashboard/transcript/README-as-truth;
- mock runs presented as live evidence;
- missing harness identity for a player;
- credential leakage;
- branch conflict execution without DELTA;
- cross-plane mutation outside scope;
- placeholder implementation accepted as complete;
- generated artifact used as evidence without manifest;
- silent overwriting of another agent’s work;
- local/private machine state embedded in generalized doctrine;
- scientific claims detached from the study question.

## 4. Four-Plane Ontology

| Plane | Canonical repo/surface | May do | Must not do |
|---|---|---|---|
| Control | `gamma-labyrinth`, `gamma-protocol`, GitHub Project/issues | doctrine, missions, rules, task envelopes, validation policy, world map | execute simulations or assert biological truth |
| Execution | `gamma` | run analyses, simulations, model searches, player turns | commit truth without gates/receipts |
| Truth | `gamma` receipt/state storage | store accepted state after validation | treat proposals, dashboards, transcripts as truth |
| Observation | `gamma-arena`, `hnxj.github.io` | display committed or labeled observation state | invent/hardcode active scientific truth |
| Analysis | `gamma-analysis` | derive reports, audits, figures, transcript/model-output analyses | mutate Truth-plane state |
| Science source | `gamma-science` | maintain references, model rationale, scientific grounding | become runtime truth storage |

The system must never confuse proposal, execution result, observation, analysis, and truth. If no verified receipt exists, use `truth_mode: truth_safe_unverified`; active scientific numbers are proposal values.

## 5. Canonical Repositories

- `gamma-labyrinth`: https://github.com/HNXJ/gamma-labyrinth - top-level skeleton/world front door; orientation, repo index, mission entrypoints, onboarding, templates, and source markdown aggregation; not runtime, truth storage, UI, or analysis archive.
- `gamma-protocol`: https://github.com/HNXJ/gamma-protocol - doctrine/spec/control; Markdown-only; default branch may be `master`.
- `gamma`: https://github.com/HNXJ/gamma - backend execution, orchestration, solver, adapters, persistence, receipts, player harnesses, truth storage.
- `gamma-arena`: https://github.com/HNXJ/gamma-arena - frontend observation, UI, dashboards, browser validation.
- `gamma-analysis`: https://github.com/HNXJ/gamma-analysis - analysis/evidence/reports, transcripts, benchmarks, figures/tables, manuscript-facing evidence; not truth storage.
- `gamma-science`: https://github.com/HNXJ/gamma-science - scientific source, references, model rationale, empirical grounding; not runtime truth storage.
- `hnxj.github.io`: https://github.com/HNXJ/hnxj.github.io - public observation only, never source of scientific truth.

Verify branch/status before branch-sensitive claims. Do not assume repos share a default branch. Branch doctrine conflicts route to DELTA before execution.

## 6. Agent Domains

Front agents (`gamma-arena`) handle UI, dashboards, public pages, browser validation, and observation hygiene. They must not invent or hardcode scientific state, and must provide browser-visible evidence.

Back agents (`gamma`) own execution gates, orchestration, solver/adapter logic, persistence, receipts, player harnesses, model backends, truth gates, and backend validation.

Analysis agents (`gamma-analysis`) analyze transcripts, model outputs, benchmarks, post-run evidence, figures, tables, and derived analyses. Their outputs are interpretation/recommendation until routed through Execution and Truth gates.

Science agents (`gamma-science`) curate references, methods, model rationale, and empirical grounding. They do not mutate runtime truth.

Doctrine/high-level agents produce prompts, audits, plans, DELTA reconciliations, issue plans, and THETA validation criteria. `gamma-protocol` remains Markdown-only Control/Doctrine and must not contain executable logic, runtime artifacts, package code, or live schemas except minimal repo-policy files.

## 7. GitHub Project / Issues Board

GitHub Project `gamma` is the durable task table, issues board, routing ledger, and cross-agent control plane. Issues are task envelopes. Comments are agent communication logs. Labels/project fields route by repo, plane, agent, risk, status, and evidence. PRs are execution artifacts. Receipts, reports, screenshots, hashes, transcripts, and validation notes are evidence artifacts.

Agents may work in parallel across separate clone roots. GitHub Project `gamma` coordinates task ownership and work status, but scientific truth still requires Truth-plane receipts.

Handoffs to Claude, Gemini, Antigravity, or other agents must state target agent/class, repo, plane, task type, allowed scope, forbidden scope, evidence required, stop conditions, and final report format. Reports require a footer naming agent/model variant or role label.

## 8. Hellenic Stack

- BETA: read-only audit, grounding, repo inspection, risk discovery.
- ALPHA: planning, design, task decomposition, supervised refinement.
- DELTA: reconciliation of conflicting truth claims, branches, reports, patches, task histories, or simulations.
- GAMMA: exact bounded execution against a validated manifest.
- THETA: post-execution validation, QA, receipt review, runtime/browser verification, autopsy.
- GAMMA-BURST: controlled one-time refactor, security cleanup, or repo-wide hygiene action.

## 9. Scientific Discovery Goals

Gamma Labyrinth supports AI-assisted scientific reasoning and hypothesis generation from multi-modal data. The target problem class is cross-modal translation: discovering latent mechanisms or biomarkers across scales such as cellular/organoid dynamics, spike/LFP dynamics, and macro-scale field or imaging signals.

Core mission gates:

1. **Classification/measurement rigor:** features or mechanisms must be measurable by predefined statistical or simulation criteria.
2. **Translatability:** candidate mechanisms should map across relevant biological levels when claimed.
3. **AI advantage:** multi-agent or scaled compute should improve speed, robustness, reproducibility, or hypothesis coverage without increasing false positives.
4. **Falsifiability:** outputs must be executable analyses, model comparisons, and reproducible artifacts, not unsupported biological narratives.

## 10. Scientific Growth Doctrine

Scientific expansion is incremental and falsifiable. Neuron-count expansion follows N -> N+1. Levels cannot be skipped. Large-scale targets may be planned, but truth-bearing state advances one verified increment at a time.

A mission may plan a larger model, but each accepted growth event must verify previous N, add exactly one neuron, validate the change, write artifacts, and produce a report/receipt.

## 11. Scientific Work Unit

A valid Gamma Labyrinth scientific work unit includes study question, biological system/modality, input data/literature, code/analysis/simulation/model operation, parameters/assumptions, validation metrics, artifacts in a run workspace, claim typing, and receipt/report. Prose-only execution work is incomplete unless artifacts are impossible and the reason is explicit.

Claim types:

| Type | Meaning | Evidence |
|---|---|---|
| `background_literature` | published context | citation/source note |
| `empirical_observation` | data-analysis result | data manifest, script, stats, figure/table |
| `simulation_result` | model execution result | run manifest, parameters, logs, hashes |
| `proposal_value` | hypothesis/unverified number/state | no truth wording |
| `truth_value` | committed accepted state | current Truth-plane receipt |
| `rejected_invalid` | failed/invalid result | reason, gate, reproduction path |

## 12. Validation Ladder

Question lock -> data/literature manifest -> baseline reproduction -> model/analysis proposal -> executable implementation -> numerical sanity gates -> statistical gates -> mechanistic gates -> receipt -> observation update.

Observation surfaces display only committed truth or clearly labeled unverified observations.

## 13. Mission Alignment

Every mission starts with:

```yaml
study_question:
  biological_domain: neuroscience / biophysics / cross-modal biomarker discovery
  target_phenomenon: <omission mismatch | biomarker | other>
  data_modalities: [spikes, LFP, MEG, organoid, literature, simulation]
  model_level: <single neuron | microcircuit | column | hierarchy | biomarker pipeline>
  claim_scope: <exploratory | empirical | simulation | truth-bearing candidate>
  required_validation: [manifest, code, statistics, perturbation, receipt]
  forbidden_shortcuts: [hardcoded truth, placeholder implementation, dashboard-as-truth]
```

No mission may optimize a metric detached from the biological question. Artifact leakage, implausible parameters, placeholder implementations, and transcript-only claims are invalid.

## 14. Continuous Game and Patches

Do not stop for every patch, bug, mission update, drift event, or doctrine refinement. Prefer live patching of missions, quests, inventories, player context, rules, hatch notes, and objectives while players remain active. If restart is unavoidable: checkpoint -> stop/restart -> resume from latest valid checkpoint. Never treat restart as a new world unless explicitly instructed.

Every player-facing turn should receive a compact `<=200` word continuity/world-law banner anchoring Gamma Labyrinth, neuroscience/biophysics, plane separation, truth-safe mode, harness identity, and continuous gameplay. The banner is continuity, not reset. Prompt injection should use the runtime chokepoint when possible and must be idempotent.

## 15. Player Harness Doctrine

All players must have a harness defining model identity, API URL/API key or secure auth path, runtime backend, allowed tools, turn protocol, artifact permissions, transcript behavior, and evidence requirements. Valid sessions distinguish live vs mock, proposal vs truth, model output vs execution artifact, transcript evidence vs committed state, and observation vs validation. Mock output must never be live evidence. Live runs require auth/model checks before Turn 1 on the execution host.

## 16. Anti-Drift Doctrine

Detect and correct non-scientific proof-of-work interpretations, generic coding detours, proposal-as-truth, observation/truth conflation, placeholder-as-implementation, stale-memory truth assertions, scientific overclaiming, hardcoded unverified biology, mission drift away from analysis/simulation/reasoning/scientific ideas, and player sessions without harness identity.

Drift is usually logged and patched, not an automatic stop. Hard stops include credential leakage, unsafe branch state, impossible mock/live distinction, failed evidence persistence, truth mutation without receipts, and requests to hardcode unverified scientific claims.

## 17. Project Objectives

A. Continuous scientific game runtime with persistent players, live missions, turn-based interactions, heartbeat, transcript capture, and safe patching.  
B. Autonomous analysis/modeling with code execution, data inspection, figures, artifacts, model tuning, parameter search, and reports.  
C. Multi-agent consensus and adversarial validation; consensus is proposal, not truth.  
D. Truth-safe scientific back that accepts updates only through receipts and gates.  
E. Cross-modal translation across biological scales.  
F. Incremental N -> N+1 biophysical modeling of scientific mechanisms.

## 18. Project-Level Tasklist

Immediate:

- Establish canonical truth-state receipt path in `gamma`.
- Sync continuity banner doctrine between `gamma-protocol` and runtime copy in `gamma`.
- Ensure all player prompts receive continuity header.
- Separate mock dry-runs from live evidence.
- Produce receipts for player sessions, even observation-only (`commit_decision: REVISE`).
- Maintain claim ledgers for biological statements.
- Populate `gamma-labyrinth` as the world front door and skeleton repo.

Near term:

- Convert transcript failures into missions/issues.
- Build council workflows for biomarker and mechanism evaluation.
- Add parameter plausibility gates and perturbation tests.
- Standardize manifests for scientific datasets and simulations.
- Enforce observation disclaimers on dashboards.
- Standardize `.gitignore` and README hygiene across repos.

Long term:

- Mature Gamma Arena into a reliable observation surface.
- Make Gamma Labyrinth reusable for multi-scale scientific domains.
- Preserve truth discipline while expanding agent creativity.

## 19. Definition of Project Success

Gamma Labyrinth succeeds when it can take a real scientific question, load relevant doctrine and data, assign harnessed agents to bounded roles, execute reproducible analyses/simulations, identify candidate mechanisms or biomarkers, reject invalids, commit only validated truth, and update observation surfaces without semantic drift or scientific overclaiming.
