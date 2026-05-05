# Gamma Labyrinth Windows Runtime Shell

## Purpose
This directory contains the manifest and documentation for the Windows-based runtime shell of Gamma Labyrinth. It establishes the boundary between the current verified world state and future development work.

## Repo Role Map
- **gamma-labyrinth**: World shell, control plane, and front door.
- **gamma-protocol**: Markdown-only doctrine and protocols.
- **gamma**: Execution engine, truth storage, and adversarial harnesses.
- **gamma-arena**: Observation UI and frontend browser validation.
- **gamma-analysis**: Derived analysis, reports, and benchmarks.
- **gamma-science**: Scientific grounding and reference methods.
- **hnxj.github.io**: Public observation surface.

## Freeze Rule
No repo is considered "frozen" until a formal `runtime/windows-stable` branch or `windows-runtime-v0.1` tag is created. This directory tracks "freeze candidates" only.

## No-Secrets Rule
This directory and all manifest files MUST NOT contain secrets, tokens, credentials, or private host information.

## Office Mac LMS Dependency
Live model-integrated runtime is PENDING resolution of the Office Mac LM Studio endpoint over Tailscale.

## Pass Sequence
1. **Pass 1**: Windows repo/runtime shell setup (CURRENT).
2. **Pass 2**: Office Mac LMS-only endpoint setup.
3. **Pass 3**: Windows front visual validation.
4. **Pass 4**: Full integration smoke test.

## Truth-Safe Warning
`truth_mode: truth_safe_unverified`. This shell does not assert active scientific truth.
