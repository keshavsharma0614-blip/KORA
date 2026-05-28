# KORA Studio v0.2 Visual QA Checklist

## Status and Boundary

This checklist is for manual review of the KORA Studio v0.2 local first-run preview.

KORA Studio v0.2 is a local preview/demo readiness milestone, not a production release. The preview must remain local-only and claim-safe. It must not execute models, download models, call providers, enable cloud sync, scan private model directories, or call runtime model list commands.

## Launch Checks

- Start the local preview with `python3 -m kora studio`.
- Confirm the terminal prints the local URL.
- Confirm the default URL is `http://127.0.0.1:8765/`.
- Confirm the browser auto-open behavior works during manual review.
- Start the preview with `python3 -m kora studio --no-browser`.
- Confirm `--no-browser` prints the local URL and does not attempt browser launch.
- Confirm the terminal copy states local-only mode.
- Confirm provider calls are disabled.
- Confirm cloud sync is disabled.
- Confirm no API key is required for the default local preview.

## Endpoint Checks

- Open `http://127.0.0.1:8765/health`.
- Confirm `/health` returns local health JSON.
- Open `http://127.0.0.1:8765/status`.
- Confirm `/status` returns preview status JSON.
- Confirm `/status` exposes provider calls as disabled.
- Confirm `/status` exposes cloud sync as disabled.
- Confirm `/status` includes system profile, model capability estimate, runtime status, installed model summary, model catalog status, recommended models, setup guidance status, execution viewer fixture, Standard Mode vs KORA Boost fixture, and report viewer placeholder fields.
- Open `http://127.0.0.1:8765/`.
- Confirm `/` renders the static first-run preview page.

## Section Order

Confirm the root page presents the first-run story in this order:

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

## First-Run Copy Checks

- Confirm KORA Studio is framed as a local-first AI Task Execution Router workspace.
- Confirm the page says KORA Studio routes local AI workflows, not just local models.
- Confirm the page does not frame KORA Studio as an LM Studio replacement.
- Confirm the page does not frame KORA Studio as a generic local chatbot.
- Confirm model recommendations are labelled as estimates until validated.
- Confirm catalog examples are clearly separated from installed models.
- Confirm runtime executable detection is not presented as model execution readiness.
- Confirm installed model detection is not connected by default.
- Confirm no private model directories are scanned.
- Confirm no runtime model list command is called by default.

## Disabled Action Checks

- Confirm download actions are disabled or labelled not connected.
- Confirm run actions are disabled or labelled not connected.
- Confirm no active `Download now`, `Run now`, or `Install now` action appears.
- Confirm disabled actions point to setup guidance, not to an active installer.
- Confirm setup guidance is informational only.
- Confirm no model is downloaded.
- Confirm no model is executed.
- Confirm provider/cloud routes remain disabled by default.

## Fixture and Report Checks

- Confirm Execution Viewer data is labelled fixture/mock only.
- Confirm Execution Viewer stages show request received, deterministic route check, structured lookup, validation pass, model fallback skipped, and final counters.
- Confirm Standard Mode vs KORA Boost comparison data is labelled fixture/mock only.
- Confirm comparison cards do not claim production cost reduction.
- Confirm comparison cards do not claim energy reduction.
- Confirm Report Viewer Placeholder uses fixture metadata only.
- Confirm report copy states no arbitrary local file scan is performed.
- Confirm report copy states no cloud upload is connected.
- Confirm report export remains a placeholder and is not active.

## Forbidden Claim Checks

The visible page and related status copy must not claim:

- KORA Studio is production-ready.
- KORA Studio is an LM Studio replacement.
- KORA physically removes RAM, VRAM, unified-memory, or model-loading requirements.
- KORA runs larger models locally on hardware that cannot load them.
- KORA proves GPT-4-level local performance.
- KORA guarantees cost reduction.
- KORA guarantees energy reduction.
- All open-source LLMs are supported.
- Provider, cloud, or distributed routes are enabled by default.
- Real API-cost reduction is proven.
- Real model execution is connected.
- Model download is connected.

## Responsive Layout Sanity

- Check a desktop-width viewport.
- Check a narrow mobile-width viewport.
- Confirm section headings remain readable.
- Confirm cards stack without overlapping text.
- Confirm badges and labels do not overflow their cards.
- Confirm the workflow steps remain readable on narrow screens.
- Confirm endpoint links remain local and do not point to remote URLs.

## Screenshot Review Notes

- Screenshots are optional manual review artifacts.
- Do not commit screenshot files as part of v0.2 readiness unless a future task explicitly asks for them.
- If screenshots are taken, verify they show the local URL and disabled action boundaries.
- Do not include raw benchmark artifacts or provider output in screenshots.

## Pass Criteria

The v0.2 visual QA pass is acceptable when the local preview clearly communicates a first-run local setup flow, keeps all model download/run/provider/cloud behavior disabled, labels execution and comparison data as fixture/mock only, and avoids unsupported product claims.
