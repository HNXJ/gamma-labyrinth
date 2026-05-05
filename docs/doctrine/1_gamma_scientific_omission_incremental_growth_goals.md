# Gamma Labyrinth Scientific Campaign Doctrine: Omission, Incremental Growth, and Biophysical Modeling

**Status:** generalized source markdown v1.1  
**Scope:** scientific campaign doctrine for omission/prediction-error modeling inside Gamma Labyrinth.  
**Plane:** Control doctrine for future Execution and Analysis tasks.  
**Truth status:** Not a Truth-plane receipt. This document defines scientific goals, constraints, task structure, and validation rules. It does not assert a current accepted circuit state, active neuron count, growth target, runtime state, or empirical result.

## 0. Purpose

This document defines a generalized Gamma Labyrinth scientific campaign around omission responses, prediction error, sparse spiking, field modulation, and stepwise biophysical modeling. It is written for agents, researchers, and scientific workflows. It must not depend on a single person's private workspace or personal goals. A local/personal thesis mapping may live in a separate local-context document, but this source document should remain portable.

Gamma Labyrinth turns scientific reasoning into a persistent, evidence-producing game. Empirical analyses become missions; simulations become executable quests; model growth occurs through receipt-backed events; hypotheses become perturbation tests; failures become evidence; and no biological claim becomes truth without gate validation and a receipt.

## 1. Scientific North Star

The central scientific question is how an omission response can arise when bottom-up sensory input is absent but temporal expectation remains. The target dissociation is:

- sparse omission-specific spiking, often expected to be strongest in higher-order or feedback-linked populations;
- broad low-frequency field modulation, especially alpha/beta-like state changes;
- weaker or more selective gamma modulation;
- post-omission gain/facilitation in the response to the next expected stimulus;
- laminar, area, and timing structure consistent with predictive routing rather than nonspecific arousal.

A valid mechanism must distinguish prediction without input from simple stimulus removal. It must explain both spike-level and field-level observables without collapsing them into one metric.

## 2. Omission Task Definition

The task must separate bottom-up sensory drive from top-down prediction.

| Condition | Bottom-up input | Top-down prediction | Purpose |
|---|---:|---:|---|
| Baseline/spontaneous | absent or baseline | absent or baseline | stable regime and background dynamics |
| Standard predictable stimulus | present | present | standard response, e.g. P1/P2/P3-like state |
| Mismatch/deviant | altered/unexpected | present or mismatched | optional contrast condition |
| Omission | absent | present | core prediction-without-input condition |
| Post-omission stimulus | present | post-omission state | gain/facilitation comparison against pre-omission standard |

A model that only removes input without representing expectation does not solve the omission problem.

## 3. Non-Negotiable N -> N+1 Growth Law

Scientific model growth must be incremental.

```text
Allowed:   N -> N+1
Forbidden: N -> N+k where k > 1
```

This applies at every scale. The rule enforces provenance, interpretability, debuggability, falsifiability, and auditability. A growth step cannot be accepted unless the previous N is verified from a current Truth-plane receipt. If no current receipt exists, the next task is truth-state recovery or seed validation, not growth.

### Zero-tolerance growth rules

- Zero tolerance for skipping levels by assertion.
- Zero tolerance for changing multiple cells while claiming a one-cell growth event.
- Zero tolerance for accepting a model because it merely runs.
- Zero tolerance for replacing failed steps with silent parameter drift.
- Zero tolerance for calling an unverified proposal a truth state.

Creativity is allowed in hypotheses, perturbations, candidate mechanisms, and model-search proposals. Creativity is not allowed to bypass validation, provenance, or N -> N+1.

## 4. Growth Event Template

```yaml
growth_event:
  previous_N: <verified from receipt>
  proposed_N: <previous_N + 1>
  truth_mode: <receipt_backed | truth_safe_unverified>
  new_cell:
    id: <unique>
    class: <E | PV | SST | VIP | other>
    area_or_column: <lower | higher | column_id>
    layer_or_compartment: <if modeled>
    biological_reason: <why this cell is needed for the omission question>
  connectivity:
    incoming: <list>
    outgoing: <list>
    sign_and_receptor: <AMPA | NMDA | GABA_A | GABA_B | proxy>
  parameters:
    source: <default | literature | search | inherited>
    bounds: <biologically plausible range>
    units: <explicit>
  validation:
    compile_check: required
    no_nan_inf: required
    baseline_response: required
    omission_task_response: required when task-ready
    artifact_manifest: required
    receipt_or_report: required
  decision: <REVISE | ACCEPT_CANDIDATE | REJECT_INVALID>
```

## 5. Mechanistic Hypotheses

| Hypothesis | Manipulation | Success signal | Rejection pattern |
|---|---|---|---|
| PV-like gain control | feedback modulates perisomatic inhibition | post-omission gain without destroying sparse omission spiking | nonspecific silencing or suppressed sensory response |
| SST-like dendritic gating | feedback modulates dendritic inhibition | field-state/alpha-beta similarity improves while sparse spiking remains | rate fits without field dynamics |
| VIP-like disinhibition | VIP-like disinhibition reduces SST-like suppression | P4/post-omission facilitation improves over PV/SST-only models | nonspecific gain or no P4 > pre-omission standard |
| Combined PV/SST/VIP | asymmetric feedback through multiple interneuron classes | best joint fit across spikes, fields, timing, spectra, perturbations | no improvement over simpler model or implausible parameters |
| Nonspecific reset | global excitability/noise reset | may increase post-omission firing | rejected if it fails laminar/area/spectral/representational structure |

## 6. Simulation Modes

| Mode | Purpose | Validity level |
|---|---|---|
| `toy_linear_or_rate` | sign/timing/gain sanity checks | exploratory only |
| `numpy_hh_like` | fast fallback if external APIs fail | candidate simulation, honestly labeled fallback |
| `single_cell_hh` | validate E/PV/SST/VIP dynamics | component validation |
| `microcircuit_ei` | validate local E/I stability and gain | pre-column candidate |
| `two_column_omission` | lower/higher-order omission model | model-lite target |
| `hierarchical_omission` | multi-column or multi-area mechanism generalization | model-base target |
| `data_assimilation_model_search` | fit baseline, standard, omission, post-omission dynamics | model-search evidence |

Fallbacks are valid only if honestly labeled. Do not call a fallback a full biophysical or Jaxley implementation unless it actually is one.

## 7. Required Metrics and Gates

Required numerical gates:

- compile/syntax pass;
- no NaN/inf;
- stable voltage/current ranges with explicit units;
- reproducible seeds;
- parameter bounds and provenance;
- run manifest;
- artifact hashes;
- receipt/report.

Required neurophysiology metrics when applicable:

- spike count/rate;
- response latency;
- LFP proxy or population current;
- alpha/beta power;
- gamma power;
- post-omission gain index;
- spike-field coupling;
- synchrony/coherence;
- representational similarity or condition separability;
- perturbation effect size.

A step may be marked `ACCEPT_CANDIDATE` only when previous N is verified, new-neuron metadata is complete, baseline stability passes, task execution produces artifacts, omission/post-omission metrics are computed or explicitly deferred, parameters are plausible or labeled exploratory, claims are not overstated, and a report/receipt is written. Truth-plane acceptance requires a separate THETA gate.

## 8. Empirical Claim Ledger

Every empirical figure or claim should map to:

- source sessions or datasets;
- inclusion/exclusion criteria;
- analysis script;
- time window;
- response variable;
- statistic and effect size;
- null/shuffle result;
- figure/table hash;
- exact claim wording;
- claim type: `background_literature`, `empirical_observation`, `simulation_result`, `proposal_value`, `truth_value`, or `rejected_invalid`.

## 9. Artifact Hygiene

Scientific artifacts such as `.npy`, `.mat`, `.csv`, figures, and model traces may be valid evidence only when they are saved under a run/artifact directory with manifests, hashes, and provenance. Repository `.gitignore` rules may ignore `.npy` and `.mat` by default to prevent accidental source pollution. Ignored artifacts can still be evidence when referenced by receipts, manifests, external artifact storage, or a deliberate promotion path.

Zero tolerance:

- no orphaned artifact as evidence;
- no hidden artifact required for reproduction;
- no artifact without manifest when used in a claim;
- no generated binary committed to source repos unless explicitly authorized.

## 10. Debugging and Failure Rules

A failed growth step is data. Do not hide failures by skipping N, changing multiple variables at once, or overwriting artifacts.

| Failure | Likely cause | Required response |
|---|---|---|
| voltage instability | bad parameters/weights | reject or revise last neuron only |
| no baseline firing | input/gain regime wrong | bounded parameter search |
| all neurons fire during omission | nonspecific excitation | test inhibition and reject reset if needed |
| post-omission gain absent | no state-change mechanism | test PV/SST/VIP alternatives |
| alpha/beta absent | slow field proxy/timescale missing | inspect synaptic/time constants |
| gamma dominates incorrectly | E/I timing mismatch | tune or reject mechanism |
| rate fits only | overfit/nonspecific reset | require spectral/perturbation gates |
| agent asserts accepted truth | plane drift | route to truth-safe correction |

Stop the growth chain if previous N cannot be verified, the proposed step adds more than one neuron, artifacts cannot be saved, NaN/inf cannot be localized, parameter bounds are violated without an exploratory label, claims overstate biological truth, or branch/repo state is unsafe.

## 11. Mission Pack

Recommended portable mission names:

- `omission_trial_taxonomy_lock`
- `omission_post_event_gain_analysis`
- `omission_spike_field_dissociation`
- `omission_two_column_seed_validation`
- `omission_growth_N_to_N_plus_1`
- `omission_pv_sst_vip_perturbation_suite`
- `omission_model_lite_report`
- `omission_hierarchical_scaling_report`

These are missions, not truth. Mission success requires artifacts, validation, and claim typing.

## 12. Definition of Scientific Success

The campaign succeeds when Gamma Labyrinth can start from a verified seed, add neurons one at a time, preserve biophysical interpretability, reproduce or reject the dissociation between sparse spiking and broad field modulation, test inhibitory mechanisms for post-omission gain, and feed model predictions back into empirical analyses without overclaiming.
