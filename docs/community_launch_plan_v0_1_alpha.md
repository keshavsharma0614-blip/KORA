# KORA v0.1 Alpha Community Launch Plan

## Objective

Use the `v0.1.0-alpha` release to attract early GitHub stars, first contributors, students, and startup developers who care about deterministic-first AI execution.

The launch goal is not broad adoption yet. The goal is to make the project understandable, runnable, and contributor-friendly enough for the first community loop.

## Target audiences

- Students learning AI infrastructure, open source, or Python tooling
- Startup developers building AI products who need more control around model calls
- AI infrastructure builders interested in task graphs, routing, validation, and telemetry
- Open-source first-time contributors looking for small documentation, test, and example tasks

## Core message

KORA is an open-source execution control layer for AI systems.

It helps developers structure work before inference, run deterministic steps first, validate outputs, and inspect telemetry. The `v0.1.0-alpha` release is a small terminal-first baseline that can be cloned, installed, smoke-tested, and contributed to.

Short message:

> KORA makes AI execution explicit: structure first, inference second.

## Launch assets needed

- GitHub release page for `v0.1.0-alpha`
- README with first-run path and contributor links
- `CONTRIBUTING.md`
- `docs/good_first_issues.md`
- GitHub issue templates
- Pull request template
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- Short demo post showing:
  - clone
  - editable install
  - `./scripts/release_smoke.sh`
  - where to find good first issues
- Short technical post explaining deterministic-first execution
- Small set of GitHub issues converted from `docs/good_first_issues.md`

## 7-day launch plan

### Day 1: Prepare the repository surface

- Confirm README first-run path is current.
- Confirm `./scripts/release_smoke.sh` passes.
- Confirm `python3 -m pytest -q` passes.
- Convert 5 to 8 items from `docs/good_first_issues.md` into GitHub issues.
- Label first tasks with `good first issue` and `documentation`, `tests`, or `examples` as appropriate.

### Day 2: Publish the launch announcement

- Publish a concise launch post.
- Link to the GitHub repo, release tag, and good first issue backlog.
- Ask readers to star the repo if the deterministic-first direction is useful.
- Invite first-time contributors to start with docs, examples, small tests, telemetry docs, benchmark docs, or CLI help wording.

### Day 3: Student and first-time contributor outreach

- Share the project in student developer groups, university AI clubs, and beginner-friendly open-source communities.
- Point people to `CONTRIBUTING.md` and `docs/good_first_issues.md`.
- Offer simple starter tasks rather than large architecture work.

### Day 4: Startup developer outreach

- Share the project with startup developers building AI workflows.
- Emphasize first-run reproducibility, explicit routing, validation, and telemetry.
- Ask for feedback on what execution-control problems they face.

### Day 5: AI infrastructure builder outreach

- Share a technical note on task graphs, deterministic-first execution, telemetry, and bounded model calls.
- Ask for review of architecture docs and benchmark docs.
- Route feature ideas into `Feature discussion` issues before implementation.

### Day 6: Contributor follow-up

- Respond to all issues and comments within a clear time window.
- Help newcomers choose appropriately small tasks.
- Split oversized ideas into reviewable follow-up issues.
- Thank contributors for smoke-test feedback and issue reports.

### Day 7: Review and summarize

- Summarize stars, forks, issues, PRs, and smoke-test feedback.
- Identify which outreach channels produced useful contributors.
- Close stale or unclear launch issues.
- Choose the next 3 to 5 small community tasks.

## Contributor funnel

1. Star the repository.
2. Clone the repository.
3. Run `./scripts/release_smoke.sh`.
4. Read `CONTRIBUTING.md`.
5. Choose a task from `docs/good_first_issues.md`.
6. Open a focused first PR.
7. Get maintainer review.
8. Merge or revise with clear feedback.

## Role for the India-based team member

The India-based team member can own the first-response and contributor-support loop.

Primary responsibilities:

- Newcomer response: reply to first-time contributors, clarify setup, and point to the smoke script.
- Issue triage: label bugs, docs tasks, good first issues, and feature discussions.
- Good-first-issue conversion: turn backlog items into well-scoped GitHub issues.
- Weekly community summary: report stars, forks, issues, PRs, merged PRs, and common questions.
- Student outreach support: share beginner-friendly tasks with student communities and help them pick narrow issues.
- Startup outreach support: collect feedback from startup developers about AI execution-control pain points.

Suggested weekly output:

- 5 converted good first issues
- 1 short community summary
- 1 list of blocked contributors or unanswered questions
- 1 list of recurring feedback themes

## GitHub operations checklist

- Pin or highlight the `v0.1.0-alpha` release.
- Keep README contributor links visible.
- Keep 5 to 10 open `good first issue` tasks available.
- Use issue templates consistently.
- Ask PR authors to complete the PR template.
- Keep discussions about new CLI commands or public surface changes in feature discussion issues.
- Close issues that are too broad and replace them with smaller scoped tasks.
- Keep labels simple:
  - `good first issue`
  - `documentation`
  - `tests`
  - `examples`
  - `telemetry`
  - `benchmark`
  - `enhancement`
  - `bug`

## Metrics to track

- GitHub stars
- Forks
- First-time contributors
- Opened issues
- Opened PRs
- Merged PRs
- Release smoke script success feedback
- Number of good first issues opened
- Number of good first issues completed
- Time to first maintainer response
- Common setup failures

## What not to do

- Do not promise production readiness.
- Do not make broad performance claims.
- Do not market unsupported platforms as verified.
- Do not push newcomers toward runtime architecture changes first.
- Do not accept public surface expansion without prior discussion.
- Do not let large speculative feature ideas replace small reviewable tasks.
- Do not let issue quality collapse into vague requests.
- Do not mix contributor onboarding work with runtime feature development.
