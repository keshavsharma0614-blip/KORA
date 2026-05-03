# KORA v0.1 Alpha Release Note Draft

## Release summary

KORA v0.1 alpha is the first public alpha snapshot of KORA's terminal-first execution control surface.

This release focuses on a small, runnable developer path for listing examples, running example task graphs, and summarizing telemetry from a committed sample input. It is intended as an alpha baseline for public verification, not as a production release.

## Included in this alpha

- `python3 -m kora --help`
- `python3 -m kora examples list`
- `python3 -m kora run <example>`
- `python3 -m kora telemetry`
- Runnable examples:
  - `hello_kora`
  - `retry_demo`
  - `direct_vs_kora`
  - `real_workload_harness`
  - `stress_test`
- Editable local development install with `python3 -m pip install -e ".[dev]"`
- Release smoke script: `scripts/release_smoke.sh`

## First-run path

```bash
python3 -m kora --help
python3 -m kora examples list
python3 -m kora run hello_kora
python3 -m kora run retry_demo
python3 -m kora run direct_vs_kora -- --offline
python3 -m kora telemetry --input docs/reports/sample_telemetry_input.json
```

The same sequence can be run with:

```bash
./scripts/release_smoke.sh
```

## Not included / not claimed yet

- This is not a production release.
- This release does not make broad performance claims.
- This release does not claim broad cross-platform validation beyond the verified local release-smoke path.
- KORA Studio is not part of the main v0.1 alpha release surface.
- The alpha surface is intentionally limited to the current terminal-first CLI, examples, telemetry summary, and release smoke path.

## Suggested release tag name

`v0.1.0-alpha`
