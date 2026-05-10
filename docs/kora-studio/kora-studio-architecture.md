# KORA Studio Architecture

## Architecture Status

This is a planning architecture. KORA Studio is not implemented yet.

## Components

### CLI Launcher

Responsibilities:

- `kora studio`
- start local Studio server
- open browser
- pass local configuration

### Local Studio Server

Responsibilities:

- serve web UI
- detect system/runtime status
- expose local APIs
- manage project/session state
- invoke KORA execution paths
- read local validation reports
- never upload data by default

### Web UI

Responsibilities:

- welcome/setup screen
- model selection
- project chat
- execution trace panel
- counter dashboard
- report viewer

### KORA Runtime Layer

Responsibilities:

- Standard Mode direct local model path
- KORA Boost execution-control path
- deterministic/fast path routing
- model escalation
- validation result
- telemetry counters

### Local Model Runtime

Initial runtime:

- Ollama first

Future runtimes:

- llama.cpp
- MLX
- vLLM
- other local runtimes

Future runtime support must be explicit opt-in and fail-closed until implemented.

### Local Storage

Options:

- SQLite or local JSON first
- project metadata
- conversation history
- execution traces
- report references

## Data Flow

```text
CLI -> Local Studio Server -> Browser UI
Browser UI -> KORA Runtime Layer -> Local Runtime
KORA Runtime Layer -> Execution Trace -> Counter Dashboard
Validation Reports -> Report Viewer
```

## Security and Privacy

- local-first
- no API keys required for v0.1 local flow
- no cloud upload by default
- no raw provider responses committed
- no private data in public artifacts

## Non-Goals

- no hosted cloud dashboard
- no user accounts
- no billing
- no production monitoring
- no provider cost dashboard in v0.1
