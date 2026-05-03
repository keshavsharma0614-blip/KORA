# Contributing to KORA

## Project status

KORA is currently at `v0.1.0-alpha`.

This is an alpha release with a small terminal-first public surface. The current focus is keeping the CLI, examples, telemetry path, and release smoke checks reliable while the project matures.

KORA is not a production release yet. Contributions should be conservative, well-scoped, and easy to verify.

## Who this project is for

KORA is for developers and researchers building AI systems that need stronger execution control.

Good contributors are interested in:

- deterministic-first execution
- explicit task graphs
- bounded model invocation
- schema validation
- telemetry and repeatable verification
- clear examples and documentation

## Local setup

Start from a clean checkout of the repository.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

The editable install should install KORA and its development dependencies into the virtual environment.

## First verification commands

Before making changes, run the release smoke check:

```bash
./scripts/release_smoke.sh
```

Then run the test suite:

```bash
python3 -m pytest -q
```

Both commands should pass before you open a pull request.

## How to choose a first issue

For a first contribution, choose a task that is small and easy to review.

Good first issues usually:

- touch one or two files
- improve clarity without changing behavior
- add or tighten a narrow test
- explain an existing example or telemetry artifact
- preserve the current public CLI surface

Avoid starting with large runtime changes, new public commands, broad refactors, or changes that alter model-routing semantics.

## Good first contribution types

Good first contribution types include:

- docs improvements
- example explanations
- small tests
- telemetry docs
- benchmark docs
- CLI help wording

If you are unsure whether a change expands the public surface, open an issue or discussion before implementing it.

## Branch and PR workflow

Use a short topic branch name:

```bash
git switch -c your-name/small-description
```

Keep pull requests focused. A good PR should explain:

- what problem it solves
- what files changed
- how behavior is affected, if at all
- what verification commands were run

Prefer one logical change per PR. Do not bundle documentation cleanup, runtime edits, and unrelated formatting in the same pull request.

## Testing expectations

At minimum, run:

```bash
./scripts/release_smoke.sh
python3 -m pytest -q
```

If your change touches a specific module, also run the relevant focused test file when possible.

Examples:

```bash
python3 -m pytest tests/test_executor.py -q
python3 -m pytest tests/test_task_ir.py -q
```

Include the commands and results in your PR description.

## Contribution rules

- Keep PRs small.
- Do not include unrelated refactors.
- Run tests before opening a PR.
- Do not expand the public CLI or public task surface without prior discussion.
- Keep KORA deterministic-first: deterministic work should run before model inference when possible.
- Do not introduce hidden model calls.
- Keep retries, budgets, and validation explicit.
- Preserve schema validation around model outputs.
- Avoid broad claims in docs unless they are backed by committed verification artifacts.

## Community expectations

Be direct, practical, and respectful.

Good project communication is specific:

- describe the concrete issue
- explain the tradeoff
- show the verification result
- ask for review when scope is uncertain

KORA values careful, measurable changes over large speculative additions.
