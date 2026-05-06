# KORA Codex Operating Context

## Purpose

This document provides stable operating context for Codex tasks on KORA.

## Repository

Official repo:

- https://github.com/Krako-Labs/KORA

Local path:

- `/Users/albertkim/02_PROJECTS/05_KORA`

Public truth:

- `origin/main` on `Krako-Labs/KORA`

## Core Development Rules

- Never modify dirty local `main`.
- Use fresh clean worktrees and branches from `origin/main`.
- Commit only intended files.
- Push the task branch.
- Do not open PRs unless explicitly requested.
- Do not create releases, tags, or assets unless explicitly requested.
- Do not upload raw benchmark artifacts unless explicitly requested.
- Completion must start with `Implemented Task ###`.

## Validation Baseline

Run relevant checks for the task scope:

- `git status -sb`
- `git log --oneline -5`
- `git diff --check`
- relevant smoke tests when code or docs require them

## Claim Scan Baseline

Scan changed or created files for these terms when claim safety matters:

- production cost
- real API
- energy reduction
- production benchmark
- broad workload superiority
- government validation
- formal partnership
- guaranteed
- proven cost reduction

Unsafe terms may appear only inside explicit do-not-claim, prohibited wording, limitation, or claim-boundary sections.

## Documentation Rules

- Distinguish official repo URL from migration history.
- Use `Krako-Labs/KORA` as the official repo.
- Keep internal-only artifacts clearly marked if needed.
- Keep public-facing docs free of unsupported claims.
- Preserve release evidence boundaries.

## EOD / SOD Artifact Rules

EOD reports and next-day prompts are internal operating artifacts.

Include:

- exact current state
- current public HEAD
- branch state
- release state
- tasks completed
- next tasks
- blockers
- claim boundaries
