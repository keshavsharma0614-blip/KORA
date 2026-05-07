# KORA Next Codex SOD Prompt

Copy and paste this prompt into Codex for the next KORA work session.

```text
Task ###

Continue KORA after the v0.3.0-alpha prerelease.

Repository and workspace rules:
- Official repo: https://github.com/Krako-Labs/KORA
- Public truth: origin/main on Krako-Labs/KORA
- Current public HEAD after post-release docs: f41d7a41acb1de4a466c8a478cd03477851aa6d1
- v0.3.0-alpha release/tag target HEAD: 078de0777178f8b233877f126a4ed844247da7d7
- Released tag: v0.3.0-alpha
- GitHub Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha
- Active clean repo path: /Users/albertkim/02_PROJECTS/05_KORA_Project/repo/KORA
- Worktree root: /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/
- Local ChatGPT context path: /Users/albertkim/02_PROJECTS/05_KORA_Project/local/chatgpt_context/
- Legacy/dirty old repo: /Users/albertkim/02_PROJECTS/05_KORA
- Do not use or modify the legacy/dirty old repo.
- Create fresh worktrees under /Users/albertkim/02_PROJECTS/05_KORA_Project/worktrees/ from latest origin/main / current public HEAD for public repo changes.
- Do not base new work on the v0.3.0-alpha release tag unless explicitly requested; release evidence remains tied to the tag target HEAD above.
- Do not create additional tags or GitHub Releases without explicit approval.
- Do not upload release assets or raw benchmark artifacts without explicit approval.
- Do not create GitHub issues, project boards, repo setting changes, package version changes, collaborator changes, or raw benchmark artifacts unless explicitly approved.
- Do not delete branches or worktrees unless explicitly approved.
- Keep generated benchmark JSON/Markdown outputs in /tmp unless a later approved task says otherwise.

Release state:
- v0.3.0-alpha is published as a GitHub prerelease.
- Draft: false.
- Prerelease: true.
- Release assets: none.
- Raw benchmark artifacts uploaded: none.
- Package version unchanged: pyproject.toml remains 0.1.0a0.

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
- Post-release EOD/SOD handoff exists if Task 189 has merged.

Current official validation commands:
- python3 -m pytest
- python3 -m kora run direct_vs_kora -- --offline
- python3 -m kora run runtime_integrated_benchmark -- --offline
- python3 -m kora run runtime_integrated_benchmark -- --offline --json-out /tmp/kora_runtime_integrated_benchmark.json
- python3 examples/runtime_integrated_benchmark/report.py --input /tmp/kora_runtime_integrated_benchmark.json --md-out /tmp/kora_runtime_integrated_benchmark.md
- python3 -m kora telemetry --input /tmp/kora_runtime_integrated_benchmark.json --json-out /tmp/kora_runtime_integrated_benchmark.telemetry.json --md-out /tmp/kora_runtime_integrated_benchmark.telemetry.md

Expected runtime benchmark counters:
- total_tasks: 100
- deterministic_route_count: 80
- fallback_or_model_candidate_route_count: 20
- simulated_baseline_model_invocations: 100
- kora_controlled_model_invocations: 20
- avoided_simulated_model_invocations: 80
- avoided_simulated_model_invocation_rate: 0.8
- deterministic_outputs_checked: 80
- mismatch_count: 0
- runtime_path_execution_status: ok
- telemetry_event_count: 100

Expected telemetry counters:
- total_llm_calls: 20
- events_ok: 100
- events_fail: 0
- events_skipped: 0
- stage_counts: ADAPTER 20 / DETERMINISTIC 80

Current safe benchmark claim:
"In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline."

Claim boundaries:
- Do not claim production cost reduction proof.
- Do not claim real API-cost reduction proof.
- Do not claim production benchmark proof.
- Do not claim full runtime-integrated benchmark evidence.
- Do not claim broad workload superiority proof.
- Do not claim energy reduction evidence.
- Do not claim formal government validation.
- Do not claim signed partner validation unless actually signed and documented.
- Do not claim guaranteed adoption or funding.

Recommended first next task:
- Create a post-release cleanup plan or v0.3.1-alpha planning document.
- Do not delete branches/worktrees unless explicitly approved.
- Do not create tags, releases, assets, or raw artifacts without explicit approval.

Completion output convention:
- Response must start exactly with: Task ###
- Response must end exactly with: Task ###
```
