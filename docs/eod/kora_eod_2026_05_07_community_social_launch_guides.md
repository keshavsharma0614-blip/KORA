# KORA EOD - Community And Social Launch Guides

Date: 2026-05-07

Branch: `task206_community_manager_guide`

Branch head before this EOD update: `70a937d8b30e6e600d18de236e6cb422e3b6c34a`

Final branch head after this task is recorded in the Task 210 completion response after commit and push.

Current public HEAD baseline: `6a288e17b1b5dd454649508c5d44eb7b209ec9d6`

Release: `v0.3.0-alpha`

Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.3.0-alpha

## Summary

This branch adds community and social launch guidance for the `v0.3.0-alpha` prerelease.

Completed on this branch:

- Community Manager Guide exists.
- Social Media Announcement Guide exists.
- Social guide is revised around strong hooks and channel-specific launch messaging.
- Reusable image-generation prompt samples are included as Markdown prompt text only.
- Community Manager Guide now includes a social launch focus section.
- No runtime code was changed.
- No actual images were generated or committed.
- No image files were added.

## Files Changed

- `README.md`
- `docs/README.md`
- `docs/community/KORA_COMMUNITY_MANAGER_GUIDE.md`
- `docs/community/KORA_SOCIAL_MEDIA_ANNOUNCEMENT_GUIDE.md`
- `docs/eod/kora_eod_2026_05_07_community_social_launch_guides.md`
- `docs/context/KORA_NEXT_CHATGPT_SOD_PROMPT.md`
- `docs/context/KORA_NEXT_CODEX_SOD_PROMPT.md`

## Social Launch Guidance Added

The Social Media Announcement Guide now emphasizes:

- launch objective and attention strategy
- one-line KORA positioning
- strong short hooks for LinkedIn and X/Twitter
- core message pillars
- channel-specific launch strategy
- short post formulas
- LinkedIn short and long drafts
- X/Twitter single-post and thread drafts
- Telegram/Discord announcement draft
- GitHub Discussions announcement draft with commands and expected counters
- reusable image-generation prompt samples
- visual overlay text snippets
- positive comment reply templates
- Sumanta launch checklist
- compact boundary reminder

## Validation Summary

Validation passed on this branch:

- `python3 -m pytest`: 54 passed
- `python3 -m kora run direct_vs_kora -- --offline`: passed
- `python3 -m kora run runtime_integrated_benchmark -- --offline`: passed
- runtime JSON generation to `/tmp`: passed
- Markdown report generation to `/tmp`: passed
- telemetry JSON/Markdown generation to `/tmp`: passed

Expected runtime benchmark counters were confirmed:

- `total_tasks`: 100
- `deterministic_route_count`: 80
- `fallback_or_model_candidate_route_count`: 20
- `simulated_baseline_model_invocations`: 100
- `kora_controlled_model_invocations`: 20
- `avoided_simulated_model_invocations`: 80
- `avoided_simulated_model_invocation_rate`: 0.8
- `deterministic_outputs_checked`: 80
- `mismatch_count`: 0
- `runtime_path_execution_status`: ok
- `telemetry_event_count`: 100

Expected telemetry counters were confirmed:

- `total_llm_calls`: 20
- `events_ok`: 100
- `events_fail`: 0
- `events_skipped`: 0
- `stage_counts`: ADAPTER 20 / DETERMINISTIC 80

## Branch And PR Status

- Branch is pushed: `task206_community_manager_guide`
- Manual PR likely required because previous PR creation was permission-blocked.
- Compare URL: https://github.com/Krako-Labs/KORA/compare/main...task206_community_manager_guide?expand=1

## Next Steps

1. Manually open a PR from `task206_community_manager_guide` to `main`.
2. Merge if checks pass and the diff remains docs-only.
3. Refresh local ChatGPT context after merge.
4. Share the Social Media Announcement Guide with Sumanta.
5. Use the guide for LinkedIn-first launch messaging, then X/Twitter, Telegram/Discord, and GitHub Discussions.

## Boundaries Preserved

- No generated benchmark JSON/Markdown artifacts were committed.
- No local-only ChatGPT context files were modified or committed.
- No runtime code was changed.
- No actual images were generated or committed.
- No image files were added.
- No additional tag, GitHub Release, release asset, raw artifact, or package version change was created.
