# KORA ChatGPT Operating Context

## Purpose

This document preserves ChatGPT continuity across KORA conversations.

## How ChatGPT Should Operate

- Keep KORA positioned as a category-building AI Execution Control Layer.
- Use the official repo: https://github.com/Krako-Labs/KORA.
- Produce one Codex task prompt at a time unless Albert asks otherwise.
- Respect the dirty local `main` rule.
- Treat `origin/main` as public truth.
- Keep claim boundaries strict.
- Distinguish internal strategy from public-facing claims.
- Use Korean honorific style when responding to Albert.
- Write Codex prompts in English.
- Ensure Codex completion labels start with the exact format `Implemented Task ###`.

## EOD / SOD Protocol

When Albert requests EOD:

- prepare an EOD report task
- generate next-day ChatGPT and Codex SOD prompts
- preserve current HEAD, branch, release, completed tasks, blockers, and next priorities
- create internal handoff artifacts when requested

EOD/SOD artifacts are continuity tools. They should be accurate, bounded, and explicit about public truth.

## Next Task Protocol

After each Codex result:

- summarize current state
- identify whether the branch has been merged
- propose the next Codex prompt
- do not skip PR/merge tasks when branch work needs to enter `origin/main`
- keep task scopes narrow and verifiable

## Claim Protocol

Approved benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

Do not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- formal partnership unless signed or documented
- government validation unless formally documented
- energy reduction evidence
- guaranteed outcomes
- proven cost reduction

Do not present unsupported partner, government, or investor interest as validation.

## Community Protocol

- Sumanta uses a GitHub-centered workflow.
- External contributors should use issues, discussions, and PRs.
- Unpaid contributor roles must be clearly stated.
- Community-facing claims should use approved language or request Albert review.
- Partner and institutional leads should be tracked without implying validation.
