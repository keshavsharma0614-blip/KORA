# KORA Studio UI Composition

## Purpose

This doc describes the initial visual/UI composition for KORA Studio.

## Visual Direction

- dark technical UI
- local-first status indicators
- cyan for normal paths
- amber for KORA Boost or model escalation highlights
- green for local runtime ready / validation passed
- avoid cloud/SaaS visual language in v0.1

## Screens

### 1. Welcome / Setup

Purpose: Introduce KORA Studio as a future local-first workspace and guide the user into a local setup flow.

Key UI elements:

- local-only status strip
- Mac/Linux support note
- runtime readiness checklist
- Open Studio CTA
- no API key required note

Key copy:

- KORA Studio
- Local-first AI workspace
- Less waiting. Better answers. No hardware upgrade.

Claim-safety notes:

- State that Studio is a planned v0.1 experience until implementation exists.
- Do not imply hosted accounts, cloud sync, or production monitoring.
- Do not present validation counters as production evidence.

### 2. Model Selection

Purpose: Help users understand local machine capability, local runtime status, and the initial model path.

Key UI elements:

- detected machine panel
- Ollama runtime status
- supported model list
- recommended direct model card
- KORA Boost recommendation card
- model pull/download status

Key copy:

- Standard Mode
- Run the local model directly.
- KORA Boost handles simple work through fast paths and saves model power for the tasks that need it.

Claim-safety notes:

- Describe model recommendations as local setup guidance, not benchmark proof.
- Keep future runtime support explicit opt-in and fail-closed until implemented.
- Do not claim that larger models physically run on unsupported hardware.

### 3. Project Chat Workspace

Purpose: Provide a project-based chat surface where users can compare Standard Mode and KORA Boost behavior.

Key UI elements:

- project sidebar
- chat panel
- model selector
- Standard Mode / KORA Boost toggle
- local runtime status
- execution trace panel
- model-call counter cards

Key copy:

- KORA Boost
- Less waiting. Better answers. No hardware upgrade.
- Simple tasks take the fast path. Harder tasks use the model when it matters.

Claim-safety notes:

- Do not use the primary copy and optional stronger marketing line in the same UI block.
- Label counters as local project/session counters.
- Avoid cost, billing, energy, or production claims.

### 4. Reports / Validation Viewer

Purpose: Let users inspect local validation reports and aggregate counters without uploading artifacts.

Key UI elements:

- local report list
- Markdown report preview
- counter summary cards
- adapter/runtime metadata
- claim boundary note
- local file path indicator

Key copy:

- Local validation reports
- Aggregate counters only
- No cloud upload by default

Claim-safety notes:

- Reports should use claim-safe boundary language from existing validation docs.
- Do not show raw provider responses, secrets, private data, or proprietary datasets.
- Do not convert local/no-network counters into production claims.

## UI Composition Reference

A concept board was generated during planning showing four UI areas:

- Welcome / Setup
- Model Selection
- Project Chat Workspace
- Reports / Validation Viewer

Do not commit binary image assets in this task unless explicitly provided and approved. Do not reference local/private image paths.
