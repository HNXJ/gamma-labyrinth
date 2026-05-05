# Gamma Labyrinth Thesis Doctrine: Omission Neurophysiology, N -> N+1 Growth, and Biophysical Modeling Goals

**Status:** unified source markdown v1.0  
**Intended repo:** `gamma-science` or `jbiophysic` for science doctrine, with task envelopes routed through GitHub Project `gamma`.  
**Plane:** Control doctrine for thesis-aligned Execution and Analysis tasks.  
**Truth status:** Not a truth receipt. This document defines goals, constraints, task structure, and validation rules. It does not assert the current accepted Gamma circuit state.

## 0. Source Basis

This document consolidates the omission roadmap, Gamma Labyrinth continuity doctrine, player-harness doctrine, DOE Genesis scientific validation aims, and repository-plane discipline. It converts the dissertation question into executable Gamma Labyrinth missions without weakening the biology.

## 1. Thesis North Star

The thesis goal is to explain omission mismatch prediction error and its underlying neurophysiology using empirical laminar electrophysiology and stepwise biophysical modeling. The core empirical observation is a dissociation: robust omission-specific single-unit spiking is sparse and concentrated in higher-order cortex such as FEF/PFC, while LFP and time-frequency responses show broad low-frequency alpha/beta modulation across the hierarchy with weaker gamma modulation. Chapter 3 asks how sparse higher-order spiking can coexist with widespread field-state changes and post-omission gain.

Gamma Labyrinth turns this into a disciplined scientific-discovery game: empirical analyses become evidence-producing missions; models grow through receipt-backed N -> N+1 events; hypotheses become perturbation tests; artifacts and claim ledgers become audit trails; and no biological or model-state claim becomes truth without receipt-backed validation.

## 2. Biological Question

**Question:** During an omission, when bottom-up sensory input is absent but temporal expectation remains, what circuit mechanism generates the omission response and the post-omission state change?

The target phenomena are:

1. **Omission response:** internally generated response to the absence of an expected stimulus.
2. **Sparse spiking:** robust omission-specific single units are rare and mainly higher-order.
3. **Widespread field modulation:** alpha/beta LFP/TFR effects appear broadly across the hierarchy, with weaker gamma.
4. **Post-omission facilitation:** P4 response is enhanced relative to P3 even though the visual stimulus is identical.

Working mechanism: sparse higher-order omission activity produces top-down predictive gain control over lower-order laminar E/I circuits through PV-like, SST-like, VIP-like, or combined inhibitory pathways.

## 3. Dissertation-to-Gamma Map

| Dissertation component | Gamma Labyrinth translation | Required evidence |
|---|---|---|
| Chapter 1 methods | GSDR/AGSDR, model-search primitives, HH/EI validation | scripts, configs, validation reports |
| Chapter 2 empirical omission physiology | trial taxonomy, response windows, area/layer manifests, spike/LFP/TFR analysis | empirical claim ledger, figures, statistics |
| Chapter 3 model-lite | two-column lower/higher-order E/I omission model, endpoint around N=100 | N -> N+1 receipts, perturbation tests |
| Chapter 3 model-base | six-column hierarchy, endpoint around N=300 | scaling receipts, generalization tests |
| Model-informed physiology | spike-field coupling, gain, timing, laminar signatures | predictions tested back against data |

Endpoint labels such as N around 100 or N around 300 are campaign destinations, not allowed jumps.

## 4. Non-Negotiable N -> N+1 Law

The thesis modeling game must grow one neuron at a time.

```text
Allowed:   N -> N+1
Forbidden: N -> N+k where k > 1
```

This applies even if N is 1,000,000 and the target is 1,000,001. The rule enforces causality, debuggability, interpretability, anti-drift discipline, and receipt-backed provenance. A growth step cannot be accepted unless previous N is verified from a current Truth-plane receipt. If no receipt exists, the next task is truth-state recovery, not growth.

## 5. Growth Event Template

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

## 6. Omission Task Definition

The model must separate bottom-up sensory input from top-down prediction.

| Condition | Bottom-up input | Top-down prediction | Purpose |
|---|---:|---:|---|
| Baseline/spontaneous | absent or baseline | absent or baseline | tune stable regime |
| Standard predictable stimulus | present | present | P1/P2/P3-like standard response |
| Mismatch/deviant variant | altered/unexpected | present/mismatched | optional contrast |
| Omission | absent | present | prediction without input; core condition |
| Post-omission P4 | present | post-omission state | test gain change vs P3 |

A model that only removes input without modeling expectation does not capture the thesis mechanism.

## 7. Empirical and Model Targets

### Chapter 2 empirical lock

Lock trial taxonomy, session inclusion, area/layer manifest, response windows, single-unit response classes, LFP/TFR windows, P3-vs-P4 analysis, shuffle/null controls, effect-size thresholds, window-stability checks, and figure-level claim ledger.

### Chapter 3 model targets

A useful candidate model should reproduce or explain sparse higher-order omission spiking; broad alpha/beta field modulation; weak/modest gamma; P4 > P3 post-omission facilitation; biologically plausible parameters; preserved distinction between spikes, fields, and gain; and perturbation-specific predictions for PV/SST/VIP pathways.

## 8. Mechanistic Hypotheses

| Hypothesis | Manipulation | Success signal | Rejection pattern |
|---|---|---|---|
| H1 PV-only | higher-order feedback changes PV-like gain | post-omission gain without destroying sparse omission spiking | suppresses all sensory responses or nonspecific silencing |
| H2 SST-only | feedback changes SST-like dendritic inhibition | improves alpha/beta field similarity while preserving sparse spiking | fits rate but fails field dynamics |
| H3 VIP disinhibition | VIP-like cells reduce SST-like inhibition | explains P4 facilitation better than PV/SST-only | nonspecific gain or no P4 > P3 |
| H4 combined PV/SST/VIP | asymmetric feedback across interneuron classes | best across RSA, spectra, synchrony, spike stats, perturbations | no improvement over simpler mechanisms or implausible parameters |
| H5 nonspecific reset | global excitability/noise reset | may increase P4 firing | rejected if it fails area/layer/spectral/representational structure |

## 9. Simulation Modes

| Mode | Purpose | Validity level |
|---|---|---|
| `toy_linear_or_rate` | sign/timing/gain sanity checks | exploratory only |
| `numpy_hh_like` | fast HH-like fallback if external APIs fail | candidate simulation, clearly labeled fallback |
| `single_cell_hh` | validate E/PV/SST/VIP dynamics | component validation |
| `microcircuit_ei` | validate local E/I stability and gain | pre-column candidate |
| `two_column_omission` | lower/higher-order omission model | model-lite target |
| `six_column_hierarchy` | mechanism generalization | model-base target |
| `data_assimilation_model_search` | fit baseline, standard, omission, P4 | model-search evidence |

Fallbacks are useful only if honestly labeled. Do not call a fallback a full HH/Jaxley implementation unless it actually is one.

## 10. Metrics and Gates

Required numerical gates: compile/syntax pass, no NaN/inf, stable voltage ranges, explicit units, reproducible seeds, parameter bounds, run manifest, artifact hashes, and receipt/report.

Required neurophysiology metrics: spike count/rate, response latency, LFP proxy or population current, alpha/beta power, gamma power, P4/P3 gain index, spike-field coupling, synchrony/coherence, RSA/representational similarity, and perturbation effect size.

A candidate step may be marked `ACCEPT_CANDIDATE` only if previous N is verified; new neuron metadata is complete; baseline stability passes; task execution produces artifacts; omission/post-omission metrics are computed or explicitly deferred; parameter values are plausible or labeled exploratory; no empirical claim is overstated; and receipt/report is written. Truth-plane acceptance requires a separate THETA gate.

## 11. Thesis Campaign Roadmap

### May-July 2026: empirical analysis lock

Freeze Chapter 2 trial taxonomy, area/layer manifest, session inclusion, unit classes, LFP/TFR windows, P3/P4 comparison, null/shuffle checks, effect sizes, and claim ledger. Target: first empirical omission manuscript if results survive stability checks.

### July-October 2026: model-lite

Implement the four-condition matrix, stabilize HH/EI primitives, and grow the two-column lower/higher-order omission model toward N around 100 by N -> N+1 events. Test sparse higher-order spiking, low-frequency modulation, weak gamma, and post-omission gain.

### October-December 2026: model-base

Use GSDR/AGSDR to search models fitting baseline, standard, omission, and post-omission dynamics. Scale toward a six-column N around 300 hierarchy only by one-neuron growth events. Compare H1-H5.

### January-March 2027: model-informed physiology

Use model predictions to guide the second empirical paper: spike-field coupling, alpha/beta phase, P4 gain, area timing, and laminar signatures.

## 12. Mission Pack Tasklist

Create or maintain missions for:

- `omission_trial_taxonomy_lock`
- `omission_p3_p4_gain_analysis`
- `omission_spike_lfp_dissociation`
- `omission_two_column_seed_validation`
- `omission_growth_N_to_N_plus_1`
- `omission_pv_sst_vip_perturbation_suite`
- `omission_model_lite_report`
- `omission_model_base_scaling_report`

## 13. Growth Harness Requirements

The growth harness must read previous N only from receipt; add exactly one neuron; write pre/post state hashes; run baseline and task checks; save voltage traces, spike table, LFP proxy, spectra, and P4/P3 metrics when applicable; produce `growth_event_<N>_to_<N+1>.md`; and block the next step until the current step passes or is explicitly revised.

## 14. Empirical Claim Ledger

Every empirical figure must map to source sessions, inclusion/exclusion criteria, analysis script, time window, response variable, statistic, effect size, null/shuffle result, figure hash, and exact claim wording.

## 15. Debugging and Failure Rules

A failed growth step is data. Do not hide failures by skipping N, changing multiple variables at once, or overwriting artifacts.

| Failure | Likely cause | Required response |
|---|---|---|
| voltage instability | bad parameters/weights | reject or revise last neuron only |
| no baseline firing | input/gain regime wrong | bounded parameter search |
| all neurons fire during omission | nonspecific excitation | test inhibition, reject reset if needed |
| P4 not greater than P3 | no post-omission gain state | test VIP/SST/PV alternatives |
| alpha/beta absent | field proxy/slow timescale missing | inspect synaptic/time constants |
| gamma dominates incorrectly | E/I timing mismatch | tune or reject mechanism |
| fits rate only | overfit/nonspecific reset | require spectral/RSA/perturbation gates |
| agent asserts accepted truth | plane drift | route to truth-safe correction |

Stop the growth chain if previous N cannot be verified, proposed step adds more than one neuron, artifacts cannot be saved, NaN/inf cannot be localized, parameter bounds are violated without exploratory label, model claims biological truth without support, or branch/repo state is unsafe.

## 16. Required Thesis Artifacts

```text
outputs/runs/<run_id>/
  session_manifest.json
  growth/growth_event_<N>_to_<N+1>.md
  growth/state_pre.json
  growth/state_post.json
  growth/validation.json
  traces/voltage_traces.npy_or_csv
  traces/spike_table.csv
  traces/lfp_proxy.csv
  spectra/alpha_beta_gamma_metrics.csv
  figures/p3_p4_gain.png
  figures/omission_response_summary.png
  figures/perturbation_comparison.png
  logs/run.log
  receipt.md
```

For manuscript use, artifacts are promoted into a figure/claim ledger only after THETA validation.

## 17. Integration With DOE Genesis

The omission project is not schizophrenia drug discovery, but it is a proof case for the broader Genesis platform: multi-agent scientific reasoning, semi-automated analysis/model search, cross-scale mapping from spikes to fields, falsifiable mechanism comparison, reproducible local compute, and separation of model output from biological truth.

## 18. Definition of Thesis Success

The thesis-Gamma integration succeeds when Gamma Labyrinth can start from a verified seed, add neurons one at a time, preserve biophysical interpretability, reproduce the empirical dissociation between sparse higher-order spiking and broad alpha/beta field modulation, explain or reject PV/SST/VIP mechanisms for post-omission gain, and feed model predictions back into empirical analyses without overclaiming.
