# KORA Studio v0.3 Readiness Report

## Status

KORA Studio v0.3 is ready as a local preview/demo readiness milestone for the live local harness track.

KORA Studio remains a local-first AI Task Execution Router workspace. v0.3 is not a production release, hosted service, provider billing dashboard, cost-reduction dashboard, energy dashboard, generic local chatbot, or LM Studio replacement.

## Repository State

- Repository: `https://github.com/Krako-Labs/KORA`
- Branch: `main`
- Public truth: `origin/main`
- Implementation HEAD before this report commit: `2fa0a310aa66dc1c698b6f612a49ffd52ca55170`
- v0.3 base public HEAD: `7f9bf50e8e396535363f955f76113c1ca43bd583`

## Implemented Surfaces

- v0.3 live harness plan
- local deterministic harness request set
- local harness event builder
- `/status` local harness surface
- static preview Local Harness Preview panel
- local harness-generated Standard Mode vs KORA Boost comparison
- report viewer placeholder connected to local harness summary metadata
- v0.3 smoke-check coverage for local harness surfaces

## Status Endpoint Coverage

`/status` now exposes:

- `local_harness_status`
- `local_harness_request_summary`
- `local_harness_requests`
- `local_harness_sample_run`
- `local_harness_counters`
- `local_harness_claim_boundary`
- `local_harness_comparison`
- `comparison_counters`
- `comparison_claim_boundary`
- `report_viewer_placeholder` with `report_source: local_harness_summary`

Backward-compatible fixture fields remain available where existing preview consumers still use them.

## Preview UI Coverage

The local preview page includes:

- launch/local-only status
- Your Computer
- Model Capability Estimate
- Runtime Status
- Catalog vs Installed
- Setup Guidance
- Disabled Download/Run Actions
- KORA Boost Boundary
- Local Harness Preview
- Execution Viewer
- Standard Mode vs KORA Boost
- Report Viewer Placeholder

The Local Harness Preview panel shows the harness status, event source state, run trigger boundary, sample request, expected route, event stages, counters, and local-only claim boundary.

## Smoke Check Coverage

`scripts/check_kora_studio_preview.py` checks an already-running localhost preview for:

- `/health`
- `/status`
- `/`
- local-only server state
- provider/cloud disabled state
- disabled download/run/model execution state
- local harness status
- local harness sample run
- local harness comparison source
- comparison counters
- report source as local harness summary
- required UI markers

The smoke check does not start external services, call providers, download models, execute models, scan private model directories, or run runtime model list commands.

## Validation

Validated commands:

- `git diff --check`: passed
- `python3 -m pytest`: `223 passed`
- `python3 -m pytest tests -k "studio or sse or execution or harness"`: `85 passed, 138 deselected`
- `python3 scripts/check_kora_studio_preview.py` against a live local preview: passed for `/health`, `/status`, and `/`

The live smoke check was run against `python3 -m kora studio --no-browser` on `http://127.0.0.1:8765/`.

## Claim Boundaries

- v0.3 is a local preview/demo readiness milestone, not a production release.
- Execution data is local deterministic harness data or fixture/mock data until live runtime wiring is implemented.
- Model-needed boundaries do not execute models in this milestone.
- Provider calls are disabled by default.
- Cloud sync is disabled by default.
- Download and run actions remain disabled.
- No model is downloaded.
- No model is executed.
- No private model directories are scanned.
- No runtime model list commands are called.
- Report viewer data is local summary metadata only.
- Export remains disabled.
- No production cost reduction is claimed.
- No energy outcome is claimed.
- No unsupported larger-model execution is claimed.
- KORA Studio is not an LM Studio replacement.

## Known Limitations

- No POST run endpoint is connected yet.
- No SSE event stream is connected yet.
- Runtime service reachability remains scaffolded and does not prove model execution readiness.
- Installed model detection remains disabled/not connected by default.
- Model catalog examples are curated local candidates, not installed models.
- Report export is a placeholder and does not write files.
- Standard Mode vs KORA Boost comparison is local deterministic harness output, not production evidence.

## Next Recommended Milestone

KORA Studio v0.4 should add a safe local run trigger or event-stream milestone:

- local-only run trigger for approved sample requests
- no model execution
- no provider calls
- no model downloads
- optional SSE stream for generated harness events
- mocked tests for run trigger and stream behavior
- clear model-needed boundary when a request cannot be completed deterministically
