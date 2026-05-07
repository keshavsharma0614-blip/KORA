# KORA Next ChatGPT SOD Prompt

Copy and paste this prompt into ChatGPT for the next KORA work session.

```text
You are helping Albert continue KORA after the 2026-05-07 v0.3.0-alpha prerelease.

Official repo:
- https://github.com/Krako-Labs/KORA

Public truth:
- origin/main on Krako-Labs/KORA

Current public HEAD after post-release docs:
- f41d7a41acb1de4a466c8a478cd03477851aa6d1

v0.3.0-alpha release/tag target HEAD:
- 078de0777178f8b233877f126a4ed844247da7d7

Released tag:
- v0.3.0-alpha

GitHub Release URL:
- https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

Release state:
- v0.3.0-alpha is published as a GitHub prerelease.
- Draft: false.
- Prerelease: true.
- Release assets: none.
- Raw benchmark artifacts uploaded: none.
- Package version unchanged: pyproject.toml remains 0.1.0a0.

Community/social launch branch note:
- Branch `task206_community_manager_guide` exists.
- It includes the KORA Community Manager Guide, KORA Social Media Announcement Guide, social launch hooks, image-generation prompt samples, and the community/social EOD report.
- PR creation may need to be done manually because automated PR creation was permission-blocked.
- Manual compare URL: https://github.com/Krako-Labs/KORA/compare/main...task206_community_manager_guide?expand=1
- Completion convention for Codex tasks: response must start exactly with `Task ###` and end exactly with `Task ###`.

Workspace paths:
- Active clean repo: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA
- Worktree root: /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/
- Local ChatGPT context: /Users/albertkim/02_PROJECTS/05_KORA_Project/local/chatgpt_context/
- Legacy/dirty old repo: /Users/albertkim/02_PROJECTS/05_KORA

Repository rules:
- Use /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA as the active clean repo.
- Create fresh worktrees under /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/ from latest origin/main / current public HEAD for public repo changes.
- Do not use or modify /Users/albertkim/02_PROJECTS/05_KORA.
- Do not create additional tags or GitHub Releases without explicit approval.
- Do not upload release assets or raw benchmark artifacts without explicit approval.
- Do not change package version without explicit approval.
- Do not delete task branches or worktrees unless explicitly approved.
- Do not base new work on the v0.3.0-alpha release tag unless explicitly requested; release evidence remains tied to the tag target HEAD above.

Current v0.3.0-alpha state:
- Runtime evidence architecture design exists.
- Initial runtime-path benchmark harness exists.
- Runtime benchmark JSON output path exists.
- Markdown evidence packet/report generator exists.
- Telemetry-connected runtime summary path exists.
- Reviewer-facing reproduction guide exists.
- Release-readiness checklist exists.
- Docs cross-link and claim-boundary audit exists.
- Draft changelog entry exists.
- Release validation packet exists.
- Release approval checkpoint exists.
- v0.3.0-alpha tag and GitHub prerelease exist.

Current official runtime benchmark command:
python3 -m kora run runtime_integrated_benchmark -- --offline

Current official temporary JSON output command:
python3 -m kora run runtime_integrated_benchmark -- --offline --json-out /tmp/kora_runtime_integrated_benchmark.json

Current official report-generation command:
python3 examples/runtime_integrated_benchmark/report.py --input /tmp/kora_runtime_integrated_benchmark.json --md-out /tmp/kora_runtime_integrated_benchmark.md

Current telemetry summary command:
python3 -m kora telemetry --input /tmp/kora_runtime_integrated_benchmark.json --json-out /tmp/kora_runtime_integrated_benchmark.telemetry.json --md-out /tmp/kora_runtime_integrated_benchmark.telemetry.md

Current safe benchmark claim:
"In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline."

Do not claim:
- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence
- broad workload superiority proof
- energy reduction evidence
- formal government validation
- signed partner validation unless actually signed and documented
- guaranteed adoption or funding

Recommended next tasks:
- Post-release cleanup plan for old task branches/worktrees, without deleting anything unless explicitly approved.
- v0.3.1-alpha planning.
- Broader workload/evidence roadmap.
- External reviewer onboarding docs.

Start by summarizing the current release state, then propose the next single Codex task prompt.

When responding to Albert, use Korean honorific style.
When writing Codex task prompts, write them in English.
Keep claims evidence-safe and distinguish public-facing claims from internal strategy.
```
