# Gamma Labyrinth Project Doctrine: Goals, Rules, Objectives, and Scientific Validation

**Status:** unified source markdown v1.0  
**Scope:** Gamma Labyrinth as a long-term scientific-discovery game, Gamma Council/Gamma Arena ecosystem, DOE Genesis-aligned AI reasoning platform, and thesis-aligned biophysical modeling world.  
**Plane:** Control doctrine synthesis.  
**Truth status:** Not a truth receipt. This document defines goals and rules. It does not assert current biological truth, current neuron count, accepted model state, or active runtime state.

## 0. Source Basis

This document consolidates Gamma continuity and player-harness doctrine; the DOE Genesis proposal for multi-agent cross-modal biomarker discovery; the omission roadmap for sparse spiking, field modulation, and post-omission gain; and the HNXJ repository context. It updates the project identity from Gamma/Gamma Arena to **Gamma Labyrinth** while preserving Gamma Council and Gamma Arena as named subsystems.

## 1. North Star

Gamma Labyrinth is a continuous open-world scientific-discovery game for agentic AI systems. Its purpose is not entertainment alone; it is an operational scaffold for AI-assisted neuroscience, biophysics, data analysis, model search, literature integration, hypothesis generation, simulation, and validation. The game metaphor enforces persistent state, player identities, missions, quests, inventories, turn semantics, evidence artifacts, and world laws. The scientific standard is stricter: every meaningful claim must be grounded in data, literature, simulation, validation gates, and receipts.

Long-term capabilities:

- read and operationalize literature without unsupported claims;
- analyze structured and semi-structured neuroscience datasets;
- propose mechanistic hypotheses and executable analyses;
- build, tune, and perturb biophysical models;
- compare model predictions against empirical data;
- coordinate multiple agents without losing provenance;
- generate transparent evidence artifacts, not just prose;
- patch missions and doctrine live without scientific drift.

Gamma Labyrinth must remain anchored to the question under study. DOE Genesis missions target cross-modal biomarker discovery and hypothesis generation across biological scales. Thesis missions target omission mismatch prediction error and circuit mechanisms. Generalization across domains is allowed only when it preserves study-question discipline.

## 2. Non-Negotiable Game Laws

1. The game never stops. It may restart/recover/resume from the latest valid checkpoint, but the world model is continuous.
2. Turns are asynchronous. Players, developer-agents, judges, backends, and observers may act independently, but every turn must preserve continuity, provenance, and state discipline.
3. The game is always about scientific analysis, simulation, reasoning, biological modeling, literature/data interpretation, and scientific idea generation.
4. New ideas enter as patches, quests, missions, events, experiments, proposals, or receipts.
5. Every player requires explicit harness/runtime identity: API key/API URL/model backend/harness/session identity or equivalent execution contract. No harness means no valid player run.
6. Violations in prompts, code, dashboards, issues, runtime paths, or behavior route to BETA, DELTA, or GAMMA depending on severity.

## 3. Four-Plane Ontology

| Plane | Canonical repo/surface | May do | Must not do |
|---|---|---|---|
| Control | `gamma-protocol`, GitHub Project/issues | doctrine, missions, rules, task envelopes, validation policy | execute simulations or assert biological truth |
| Execution | `gamma` | run analyses, simulations, model searches, player turns | commit truth without gates/receipts |
| Truth | `gamma` receipt/state storage | store accepted state after validation | treat proposals, dashboards, transcripts as truth |
| Observation | `gamma-arena`, `hnxj.github.io` | display committed or labeled observation state | invent/hardcode active scientific truth |
| Analysis | `gamma-analysis` | derive reports, audits, figures, transcript/model-output analyses | mutate Truth-plane state |

The system must never confuse proposal, execution result, observation, analysis, and truth. A player may propose; a solver may run; a transcript may record; an analysis may interpret. None becomes truth until a gate accepts it and a receipt commits it. If no verified receipt exists, use `truth_mode: truth_safe_unverified`; active scientific numbers are proposal values.

## 4. Canonical Repositories

- `gamma-protocol`: https://github.com/HNXJ/gamma-protocol - doctrine/spec/control; Markdown-only; default branch may be `master`.
- `gamma`: https://github.com/HNXJ/gamma - backend execution, orchestration, solver, adapters, persistence, receipts, player harnesses, truth storage.
- `gamma-arena`: https://github.com/HNXJ/gamma-arena - frontend observation, UI, dashboards, browser validation.
- `gamma-analysis`: https://github.com/HNXJ/gamma-analysis - analysis/evidence/reports, transcripts, benchmarks, figures/tables, manuscript-facing evidence; not truth storage.
- `gamma-science`: https://github.com/HNXJ/gamma-science and `jbiophysic`: https://github.com/HNXJ/jbiophysic - scientific source, neuroscience references, model rationale, empirical grounding; verify canonical status before edits.
- `hnxj.github.io`: https://github.com/HNXJ/hnxj.github.io - public observation only, never source of scientific truth.

Verify branch/status before branch-sensitive claims. Do not assume repos share a default branch. Branch doctrine conflicts route to DELTA before execution.

## 5. Agent Domains

Front agents (`gamma-arena`) handle UI, dashboards, public pages, browser validation, and observation hygiene. They must not invent or hardcode scientific state, and must provide browser-visible evidence.

Back agents (`gamma`) own execution gates, orchestration, solver/adapter logic, persistence, receipts, player harnesses, model backends, truth gates, and backend validation.

Analysis agents (`gamma-analysis`) analyze transcripts, model outputs, benchmarks, post-run evidence, figures, tables, and manuscript-facing derived analyses. Their outputs are interpretation/recommendation until routed through Execution and Truth gates.

Doctrine/high-level agents produce prompts, audits, plans, DELTA reconciliations, issue plans, and THETA validation criteria. `gamma-protocol` remains Markdown-only Control/Doctrine and must not contain executable logic, runtime artifacts, package code, or live schemas except minimal repo-policy files.

## 6. GitHub Project / Issues Board

GitHub Project `gamma` is the durable task table, issues board, routing ledger, and cross-agent control plane. Issues are task envelopes. Comments are agent communication logs. Labels/project fields route by repo, plane, agent, risk, status, and evidence. PRs are execution artifacts. Receipts, reports, screenshots, hashes, transcripts, and validation notes are evidence artifacts.

Handoffs to Claude, Gemini, Antigravity, or other agents must state target agent/class, repo, plane, task type, allowed scope, forbidden scope, evidence required, stop conditions, and final report format. Reports require a footer naming agent/model variant or role label.

## 7. Hellenic Stack

- BETA: read-only audit, grounding, repo inspection, risk discovery.
- ALPHA: planning, design, task decomposition, supervised refinement.
- DELTA: reconciliation of conflicting truth claims, branches, reports, patches, task histories, or simulations.
- GAMMA: exact bounded execution against a validated manifest.
- THETA: post-execution validation, QA, receipt review, runtime/browser verification, autopsy.
- GAMMA-BURST: controlled one-time refactor or repo-wide cleanup.

## 8. DOE Genesis Alignment

Gamma Labyrinth supports the Genesis goal of AI for scientific reasoning and hypothesis generation from multi-modal data. The target problem is cross-modal translation: discovering latent biomarkers across micro-scale cellular/organoid dynamics, meso-scale spike/LFP dynamics, and macro-scale clinical MEG oscillations.

Core data streams:

- Human MEG from healthy controls and schizophrenia patients.
- Non-human primate ketamine spike/LFP data.
- Human iPSC-derived cortical organoid spikes/LFP/network events.

Mission gates from the proposal:

1. **Classification rigor:** biomarkers separate healthy/control from dysfunction states within each modality by predefined statistical criteria.
2. **Translatability:** at least two biomarkers survive cross-modal mapping across organoid, primate, and human datasets.
3. **AI advantage:** scaling local compute and multi-agent councils improves speed, robustness, or consistency without increasing false positives.
4. **Falsifiability:** outputs must be executable analyses, model comparisons, and reproducible artifacts, not biological narratives.

## 9. Thesis Alignment

The omission campaign asks how sparse higher-order spiking can coexist with broad low-frequency field modulation and post-omission gain. Scientific growth is incremental and falsifiable: neuron-count expansion is N -> N+1, levels cannot be skipped, and truth-bearing state advances one verified increment at a time. Modeling must align with sparse higher-order spiking, broad alpha/beta field modulation, weak gamma, P4/P3 gain, laminar/area timing, and PV/SST/VIP candidate mechanisms.

## 10. Scientific Work Unit

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

## 11. Validation Ladder

Question lock -> data/literature manifest -> baseline reproduction -> model/analysis proposal -> executable implementation -> numerical sanity gates -> statistical gates -> mechanistic gates -> receipt -> observation update. Observation surfaces display only committed truth or clearly labeled unverified observations.

## 12. Mission Alignment

Every mission starts with:

```yaml
study_question:
  biological_domain: neuroscience / biophysics / cross-modal biomarker discovery
  target_phenomenon: <omission mismatch | schizophrenia biomarker | other>
  data_modalities: [spikes, LFP, MEG, organoid, literature, simulation]
  model_level: <single neuron | microcircuit | column | hierarchy | biomarker pipeline>
  claim_scope: <exploratory | empirical | simulation | truth-bearing candidate>
  required_validation: [manifest, code, statistics, perturbation, receipt]
  forbidden_shortcuts: [hardcoded truth, placeholder implementation, dashboard-as-truth]
```

No mission may optimize a metric detached from the biological question. Artifact leakage, implausible parameters, placeholder implementations, and transcript-only claims are invalid.

## 13. Continuous Game and Patches

Do not stop for every patch, bug, mission update, drift event, or doctrine refinement. Prefer live patching of missions, quests, inventories, player context, rules, hatch notes, and objectives while players remain active. If restart is unavoidable: checkpoint -> stop/restart -> resume from latest valid checkpoint. Never treat restart as a new world unless explicitly instructed.

Every player-facing turn should receive a compact `<=200` word continuity/world-law banner anchoring Gamma Labyrinth, neuroscience/biophysics, plane separation, truth-safe mode, harness identity, and continuous gameplay. The banner is continuity, not reset. Prompt injection should use the runtime chokepoint when possible and must be idempotent.

## 14. Player Harness Doctrine

All players must have a harness defining model identity, API URL/API key or secure auth path, runtime backend, allowed tools, turn protocol, artifact permissions, transcript behavior, and evidence requirements. Valid sessions distinguish live vs mock, proposal vs truth, model output vs execution artifact, transcript evidence vs committed state, and observation vs validation. Mock output must never be live evidence. Live runs require auth/model checks before Turn 1 on the execution host.

## 15. Anti-Drift Doctrine

Detect and correct non-scientific proof-of-work interpretations, generic coding detours, proposal-as-truth, observation/truth conflation, placeholder-as-implementation, stale-memory truth assertions, scientific overclaiming, hardcoded unverified biology, mission drift away from analysis/simulation/reasoning/scientific ideas, and player sessions without harness identity. Drift is usually logged and patched, not an automatic stop. Hard stops include credential leakage, unsafe branch state, impossible mock/live distinction, failed evidence persistence, truth mutation without receipts, and requests to hardcode unverified scientific claims.

## 16. Project Objectives

A. Continuous scientific game runtime with persistent players, live missions, turn-based interactions, heartbeat, transcript capture, and safe patching.  
B. Autonomous analysis/modeling with code execution, data inspection, figures, artifacts, model tuning, parameter search, and reports.  
C. Multi-agent consensus and adversarial validation; consensus is proposal, not truth.  
D. Truth-safe scientific back that accepts updates only through receipts and gates.  
E. Cross-modal translation across organoid, macaque, and human MEG data.  
F. Thesis-driven N -> N+1 biophysical modeling of omission mechanisms.

## 17. Project-Level Tasklist

Immediate:

- Establish canonical truth-state receipt path in `gamma`.
- Sync continuity banner doctrine between `gamma-protocol` and runtime copy in `gamma`.
- Ensure all player prompts receive continuity header.
- Separate mock dry-runs from live evidence.
- Produce receipts for player sessions, even observation-only (`commit_decision: REVISE`).
- Maintain claim ledgers for biological statements.

Near term:

- Convert transcript failures into missions/issues.
- Build council workflows for biomarkers and omission-model evaluation.
- Add parameter plausibility gates and perturbation tests.
- Standardize manifests for MEG, primate, organoid, and omission recordings.
- Enforce observation disclaimers on dashboards.

Long term:

- Port local MLX/Mac workflows to DOE/NNSA or American Science Cloud workflows.
- Mature Gamma Arena into reliable public observation surface.
- Make Gamma Labyrinth reusable for other multi-scale scientific domains.

## 18. Non-Negotiable Rules

No hardcoded active scientific truth. No truth claim without current verified receipt. No dashboard/transcript as truth. No mock run as live evidence. No credentials in repo/transcript. No runtime code in `gamma-protocol`. No mission without study question. No model scaling that skips validation. No placeholder accepted as implementation. No complete execution report without artifacts or explicit reason artifacts were impossible.

## 19. Definition of Project Success

Gamma Labyrinth succeeds when it can take a real scientific question, load relevant doctrine and data, assign harnessed agents to bounded roles, execute reproducible analyses/simulations, identify candidate mechanisms or biomarkers, reject invalids, commit only validated truth, and update observation surfaces without semantic drift or scientific overclaiming.
