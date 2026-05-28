# KORA Studio v0.2 Readiness Report

## Status

KORA Studio v0.2 is ready as a local preview/demo readiness milestone for the first-run local setup experience.

It is not a production release. It does not execute models, download models, call providers, enable cloud sync, scan private model directories, call runtime model list commands, or prove production cost, billing, energy, or provider outcomes.

## Repository State

- branch: `main`
- public truth: `origin/main`
- readiness baseline HEAD before this report commit: `3a22cc9fce40b99f34305ae94b3210f5f13d09e1`
- previous milestone: Task 421 local preview smoke check
- v0.2 readiness status exposed by `/status`: `local_preview_demo_ready`

## Implemented v0.2 Surfaces

The local preview now presents the first-run setup flow in this order:

1. Launch / Local-only Status
2. Your Computer
3. Model Capability Estimate
4. Runtime Status
5. Catalog vs Installed
6. Setup Guidance
7. Disabled Download/Run Actions
8. KORA Boost Boundary
9. Execution Viewer
10. Standard Mode vs KORA Boost
11. Report Viewer Placeholder

The preview also includes:

- `python3 -m kora studio` localhost launch
- browser auto-open by default
- `python3 -m kora studio --no-browser`
- `python3 -m kora studio --status`
- `/health`
- `/status`
- `/`
- grouped v0.2 `/status` fields for Studio status, launch boundary, disabled action state, and claim boundaries
- system profile scaffold
- model capability estimate scaffold
- static curated model catalog scaffold
- runtime status scaffold
- installed model detection scaffold, disabled by default
- setup guidance scaffold
- disabled download/run action metadata
- fixture/mock Execution Viewer events
- fixture/mock Standard Mode vs KORA Boost comparison
- report viewer/export placeholder
- local smoke-check helper: `python3 scripts/check_kora_studio_preview.py`
- visual QA checklist: `docs/kora-studio/kora-studio-v0-2-visual-qa-checklist.md`

## Claim Boundaries

KORA Studio v0.2 remains claim-safe:

- KORA Studio is a local-first AI Task Execution Router workspace.
- Catalog examples are not installed models.
- Model recommendations are estimates until validated.
- Runtime executable detection is not model execution readiness.
- Installed model detection is not connected by default.
- KORA does not remove model memory requirements.
- Larger-model workflows may become more practical when deterministic work avoids the model path.
- Download and run actions remain disabled until explicitly connected.
- Provider calls and cloud sync are disabled by default.
- Execution data is fixture/mock only until live harness wiring is implemented.
- Report viewer data is fixture metadata only.

## Non-Scope

v0.2 does not add:

- real model download
- real model execution
- provider calls
- cloud sync
- remote catalog fetching
- Hugging Face or Ollama registry calls
- private model directory scans
- runtime model list commands
- active report file picker/export
- production monitoring
- billing dashboard
- cost-reduction dashboard
- energy dashboard
- LM Studio replacement behavior

## Validated Results

Task 422 readiness validation passed with:

- `git diff --check`
- `python3 -m pytest tests/test_kora_studio_cli.py`: 9 passed
- `python3 -m pytest tests/test_kora_studio_server.py`: 14 passed
- `python3 -m pytest tests/test_kora_studio_system_profile.py`: 5 passed
- `python3 -m pytest tests/test_kora_studio_model_catalog.py`: 8 passed
- `python3 -m pytest tests/test_kora_studio_runtime_status.py`: 8 passed
- `python3 -m pytest tests/test_kora_studio_execution_fixture.py`: 7 passed
- `python3 -m pytest tests/test_kora_studio_preview_smoke.py`: 4 passed
- `python3 -m pytest tests -k "studio or sse or execution or harness"`: 66 passed, 138 deselected
- `python3 -m pytest`: 204 passed
- live local smoke check with `python3 scripts/check_kora_studio_preview.py`: passed for `/health`, `/status`, and `/`

`tests/test_kora_studio_comparison_fixture.py` does not exist in the current tree; Standard Mode vs KORA Boost fixture coverage is included through existing Studio server, fixture, and selected Studio tests.

## Known Limitations

- v0.2 remains a local preview/demo readiness milestone, not a full product.
- The root page is still a static preview surface.
- The separate React demo remains a scaffold.
- Runtime service reachability is a scaffold and does not prove model execution readiness.
- Installed model detection is scaffold-only and disabled by default.
- Catalog entries are curated examples only.
- Download and run actions are disabled.
- Execution Viewer data is fixture/mock only.
- Standard Mode vs KORA Boost comparison data is fixture/mock only.
- Report Viewer data is fixture metadata only.
- Visual QA checklist is manual; screenshots are not committed.

## Next Recommended Milestone

Task 423 should start the next v0.x planning slice. A conservative next step is a UI/data contract cleanup pass that keeps the preview local-only while deciding whether the next implementation should focus on:

- a more product-like static frontend layout,
- safer runtime readiness UX,
- local installed-model detection design,
- or fixture-backed interaction polish.

Any future task that adds provider calls, model download, model execution, runtime model list commands, private directory scanning, or remote catalog fetching requires explicit approval and a separate claim-boundary review.
