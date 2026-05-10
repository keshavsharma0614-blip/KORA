# KORA Studio MVP User Flow

## Overview

1. Install/launch from CLI.
2. Run `kora studio`.
3. Browser opens local Studio UI.
4. Studio checks local system and runtime.
5. User sees recommended local model.
6. User compares Standard Mode and KORA Boost.
7. User pulls/downloads model if needed.
8. User creates/opens project.
9. User starts chat.
10. User sees answer plus execution trace.
11. User views model-call counters.
12. User opens validation/report history.

## Flow 1 — First Launch

- local-only intro
- Mac/Linux support
- no API key required
- runtime check
- Open Studio CTA

## Flow 2 — Model Selection

- detected machine panel
- direct model recommendation
- KORA Boost recommended workflow
- Ollama status
- model pull status

## Flow 3 — Project Chat

- project sidebar
- chat panel
- model selector
- Standard Mode / KORA Boost toggle
- local runtime status

## Flow 4 — Execution Trace

- selected route
- model called yes/no
- deterministic path used
- validation result
- latency
- counters

## Flow 5 — Reports / Validation Viewer

- local report list
- Markdown report preview
- counter summary
- claim boundary note
- no cloud upload by default

## Error States

- Ollama not installed
- model not downloaded
- local runtime unavailable
- report path missing
- unsupported adapter selected
- `local_runtime_placeholder` fail-closed
