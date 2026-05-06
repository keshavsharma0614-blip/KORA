# KORA Next Codex SOD Prompt

Copy and paste this prompt into Codex for the next KORA work session.

```text
Task ###

Continue KORA from the 2026-05-06 EOD handoff.

Repository:
- Official repo: https://github.com/Krako-Labs/KORA
- Local path: /Users/albertkim/02_PROJECTS/05_KORA
- Public truth: origin/main on Krako-Labs/KORA
- Current origin/main HEAD: 83bd8d5e013701c0d3aca6703e2a14a5d5189021
- Published release: v0.2.0-alpha
- Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha

Operating rules:
- Do not modify dirty local main.
- Use a fresh clean worktree and branch from origin/main.
- Work one task at a time.
- Do not create a release unless explicitly requested.
- Do not create a tag unless explicitly requested.
- Do not upload release assets unless explicitly requested.
- Do not upload raw benchmark artifacts unless explicitly requested.
- Do not change repository settings unless explicitly requested.
- Do not create actual GitHub issues or project boards unless explicitly requested.
- Do not add collaborators unless explicitly requested.
- Completion output must start with the exact label: Implemented Task ###

Current strategic position:
- KORA is a category-building open-source infrastructure project.
- Official category: AI Execution Control Layer.
- Vision phrase: Inference OS for AI systems.
- Official repo: Krako-Labs/KORA.
- GitHub is the OSS operating HQ.

Current safe benchmark claim:
“In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.”

Claim boundaries:
- Do not claim production cost reduction proof.
- Do not claim real API-cost reduction proof.
- Do not claim production benchmark proof.
- Do not claim full runtime-integrated benchmark evidence.
- Do not claim broad workload superiority proof.
- Do not claim energy reduction evidence.
- Do not claim formal government validation.
- Do not claim signed cloud/data center/telco partnership unless actually signed.
- Do not claim guaranteed adoption or funding.

Recommended first task:
- Verify whether Task 126 branch is merged; if not, open/merge it.
- If Task 126 is already merged, start safe docs cross-link cleanup using docs/README.md and docs/ops/2026-05-06-kora-docs-navigation-map.md.

Expected validation baseline:
- git status -sb
- git log --oneline -5
- git diff --check
- relevant ripgrep scans for old repository URLs and unsafe claim language when documentation changes.
```
