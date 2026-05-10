# KORA Studio v0.1 Product Spec

## Product Definition

KORA Studio v0.1 is a local-first AI workspace for Mac and Linux that launches from the KORA CLI, opens a local browser UI, helps users choose local models, and lets them use Standard Mode or KORA Boost for project-based AI chat and validation visibility.

## Target Users

- local AI users
- developers testing local LLM workflows
- AI app builders
- technical reviewers
- contributors exploring KORA validation

## User Problem

Local model users often do not know which model their machine can run, how to compare direct model usage with KORA-controlled execution, or how much model work is being avoided.

## Core Promise

Less waiting. Better answers. No hardware upgrade.

## KORA Boost Explanation

KORA Boost handles simple work through fast paths and saves model power for the tasks that need it.

## Standard Mode

Standard Mode runs the selected local model directly.

## KORA Boost

KORA Boost routes simple or structured work through fast local paths first, then uses the model when deeper reasoning is needed.

## MVP Features

- CLI launch: `kora studio`
- local web UI
- browser auto-open
- system capability detection
- Ollama runtime check
- supported local model list
- recommended direct model
- KORA Boost recommendation
- model pull/download status
- project-based chat
- execution path panel
- model-call counter cards
- validation report viewer
- local storage

## MVP Non-Features

- no cloud sync
- no team accounts
- no billing
- no hosted SaaS
- no provider billing dashboard
- no energy dashboard
- no real provider adapter by default
- no production monitoring

## Success Criteria

- user can launch Studio locally
- user can see local runtime status
- user can choose a model
- user can switch Standard Mode / KORA Boost
- user can chat within a project
- user can inspect execution path
- user can see model-call counters
- user can open local validation reports

## Claim Safety

Do not describe KORA Studio v0.1 as proving production cost reduction, real API-cost reduction, energy reduction, production validation, or broad workload superiority.
