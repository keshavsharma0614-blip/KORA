# KORA Studio v0.4 Readiness Report

## Status

KORA Studio v0.4 is ready as a local deterministic harness preview/demo milestone. It adds local run trigger surfaces for approved deterministic sample requests and exposes generated harness events, counters, comparison metadata, and report metadata without connecting real model execution, provider calls, downloads, cloud sync, or file export.

v0.4 remains a local preview/demo readiness milestone, not a production release.

## Current HEAD

Validated before this report commit:

```text
01d8c7051b5f97051ce8729837ed455c1e79981e
```

## Validation Commands and Results

```bash
git diff --check
```

Result: passed.

```bash
python3 -m pytest
```

Result: 231 passed.

```bash
python3 -m pytest tests -k "studio or sse or execution or harness"
```

Result: 93 passed, 138 deselected.

## Live Smoke Check Results

The local preview server was started with:

```bash
python3 -m kora studio --no-browser
```

Then the smoke check was run:

```bash
python3 scripts/check_kora_studio_preview.py
```

Result: passed.

Covered:

- `/health`
- `/status`
- `/api/harness/run`
- `/api/harness/run/<run_id>`
- `/api/harness/events`
- `/api/harness/sse`
- `/`

## Endpoints Covered

- `GET /health`
- `GET /status`
- `GET /`
- `POST /api/harness/run`
- `GET /api/harness/run/{run_id}`
- `GET /api/harness/events?run_id=<id>`
- `GET /api/harness/sse?run_id=<id>`

## v0.4 Implemented Surface

- Approved local harness run trigger for deterministic sample request IDs only.
- In-memory run retrieval while the local server process is alive.
- Generated events endpoint for existing local run records.
- Generated SSE endpoint for existing local run records.
- Static Run Local Harness panel in the preview UI.
- Generated Event Timeline panel.
- Generated Counters section.
- Standard Mode vs KORA Boost local harness comparison.
- Local Harness Report and Report Metadata Preview panels.
- Disabled file export boundary.
- Model-needed `execution_not_connected` boundary.

## Claim Boundaries

- Local deterministic harness only.
- Generated events only.
- No arbitrary prompt execution.
- No model execution.
- No provider calls.
- No model downloads.
- No cloud sync.
- No private model directory scanning.
- No runtime model list commands.
- No external network behavior.
- No file export.
- No report file writing.
- No production cost reduction claim.
- No energy outcome claim.
- No unsupported larger-model execution claim.
- Not an LM Studio replacement.

## Known Limitations

- The preview UI is still static and non-JavaScript.
- Run records are in-memory only and disappear when the server process stops.
- The Run Local Harness panel lists approved requests and endpoint guidance, but it does not yet provide browser-side selected-run state.
- SSE streams precomputed generated harness events only.
- Report metadata is preview metadata only; export remains disabled.
- Model-needed boundaries do not execute models.

## Next Recommended v0.5 Direction

KORA Studio v0.5 should focus on a local interactive trigger UI / selected-run state:

- interactive approved request selector
- Run Local Harness button
- selected-run state
- rendered generated timeline/comparison/counters/report metadata for the selected run
- no arbitrary prompt execution
- no model execution
- no provider calls
- no downloads
