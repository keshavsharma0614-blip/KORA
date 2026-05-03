# KORA Good First Issue Backlog

## Purpose

This document lists small, contributor-friendly tasks that maintainers can convert into GitHub issues.

The goal is to help new contributors make useful changes without expanding KORA's public surface or changing runtime behavior.

## How to use this list

Maintainers can copy one candidate into a GitHub issue using the `Good first issue` template.

Contributors should choose tasks that are narrow, easy to verify, and aligned with KORA's deterministic-first alpha scope.

Before opening a pull request, run:

```bash
./scripts/release_smoke.sh
python3 -m pytest -q
```

For docs-only tasks, explain why runtime tests were not needed if you skip them.

## Good first issue candidates

### 1. Clarify the release smoke script purpose

- Suggested title: `Docs: explain when to run the release smoke script`
- Type: docs improvement
- Likely files/area: `scripts/release_smoke.sh`, `CONTRIBUTING.md`, or docs
- Expected outcome: contributors understand that the smoke script verifies the current first-run path
- Verification command: `./scripts/release_smoke.sh`

### 2. Add short notes for `hello_kora`

- Suggested title: `Docs: explain the hello_kora example`
- Type: example explanation
- Likely files/area: `examples/hello_kora/`, README or docs
- Expected outcome: readers understand what the example demonstrates and what output to expect
- Verification command: `python3 -m kora run hello_kora`

### 3. Add short notes for `retry_demo`

- Suggested title: `Docs: explain the retry_demo example`
- Type: example explanation
- Likely files/area: `examples/retry_demo/`, README or docs
- Expected outcome: readers understand the retry/recovery behavior without reading the code first
- Verification command: `python3 -m kora run retry_demo`

### 4. Clarify offline mode for `direct_vs_kora`

- Suggested title: `Docs: clarify direct_vs_kora offline mode`
- Type: docs improvement
- Likely files/area: `examples/direct_vs_kora/`, README or docs
- Expected outcome: users understand that `--offline` is the reproducible no-credential path
- Verification command: `python3 -m kora run direct_vs_kora -- --offline`

### 5. Document telemetry sample input

- Suggested title: `Docs: describe sample telemetry input`
- Type: telemetry docs
- Likely files/area: `docs/reports/sample_telemetry_input.json`, telemetry docs
- Expected outcome: users understand why the sample exists and how to run telemetry against it
- Verification command: `python3 -m kora telemetry --input docs/reports/sample_telemetry_input.json`

### 6. Add a focused test for example discovery ordering

- Suggested title: `Test: cover examples list ordering`
- Type: small test
- Likely files/area: `tests/`, `kora/cli.py`
- Expected outcome: example listing stays stable and predictable
- Verification command: `python3 -m pytest -q`

## Small docs tasks

### 7. Tighten README first-run wording

- Suggested title: `Docs: tighten README first-run wording`
- Type: docs improvement
- Likely files/area: `README.md`
- Expected outcome: first-run commands remain clear and match the release smoke script
- Verification command: `./scripts/release_smoke.sh`

### 8. Add a note about alpha scope to contributor docs

- Suggested title: `Docs: clarify alpha scope for contributors`
- Type: docs improvement
- Likely files/area: `CONTRIBUTING.md`
- Expected outcome: contributors understand why public surface expansion needs discussion
- Verification command: not applicable for docs-only change

## Small test tasks

### 9. Add a test for unknown example names

- Suggested title: `Test: cover unknown example error path`
- Type: small test
- Likely files/area: `tests/`, `kora/cli.py`
- Expected outcome: `kora run <missing>` keeps returning a clear error and nonzero status
- Verification command: `python3 -m pytest -q`

### 10. Add a telemetry markdown smoke assertion

- Suggested title: `Test: cover telemetry markdown output basics`
- Type: small test
- Likely files/area: `tests/`, `kora/telemetry.py`
- Expected outcome: telemetry markdown output keeps core headings and counters
- Verification command: `python3 -m pytest -q`

## Example explanation tasks

### 11. Add expected output snippets for first-run examples

- Suggested title: `Docs: add expected output snippets for first-run examples`
- Type: example explanation
- Likely files/area: `README.md`, example docs, or `docs/`
- Expected outcome: users can compare their local output with the expected shape
- Verification command: `./scripts/release_smoke.sh`

### 12. Explain `real_workload_harness` as a next-step example

- Suggested title: `Docs: position real_workload_harness as a next step`
- Type: example explanation
- Likely files/area: `examples/real_workload_harness/`, `docs/benchmark-real-app.md`
- Expected outcome: users understand it is not required for the first-run path
- Verification command: not applicable for docs-only change

## Telemetry / benchmark docs tasks

### 13. Add a glossary for telemetry counters

- Suggested title: `Docs: define core telemetry counters`
- Type: telemetry docs
- Likely files/area: `docs/telemetry-and-observability.md`, `docs/glossary.md`
- Expected outcome: users understand counters such as `events_ok`, `events_fail`, and `budget_breaches`
- Verification command: not applicable for docs-only change

### 14. Clarify benchmark docs are exploratory

- Suggested title: `Docs: clarify benchmark docs are exploratory`
- Type: benchmark docs
- Likely files/area: `docs/benchmark.md`, `docs/benchmark-real-app.md`
- Expected outcome: benchmark docs avoid broad performance claims and stay alpha-scoped
- Verification command: not applicable for docs-only change

## CLI/help wording tasks

### 15. Review CLI help text for first-run clarity

- Suggested title: `CLI: review help wording for first-run commands`
- Type: CLI help wording
- Likely files/area: `kora/cli.py`, tests if wording is asserted
- Expected outcome: help text is clearer without adding commands or changing behavior
- Verification command: `python3 -m kora --help`

### 16. Add a small test around telemetry input requirement

- Suggested title: `Test: cover telemetry input requirement`
- Type: small test
- Likely files/area: `tests/`, `kora/cli.py`
- Expected outcome: missing telemetry input remains a clear CLI error
- Verification command: `python3 -m pytest -q`

## Out of scope for first-time contributors

The following are not good first issues:

- adding new public CLI commands
- changing task graph schema
- changing model-routing behavior
- adding new model providers
- changing release packaging metadata without maintainer direction
- broad performance claims or benchmark conclusions
- large refactors across runtime modules

If a task may expand KORA's public surface, discuss it before implementation.
