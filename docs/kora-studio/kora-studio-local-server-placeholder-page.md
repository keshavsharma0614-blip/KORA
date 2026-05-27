# KORA Studio Local Server Preview Page

## Status

The KORA Studio local server root now renders a static UI prototype v0.1 for the server skeleton. It is still not a full frontend and does not make KORA Studio production-ready.

The preview should frame KORA Studio as a local-first AI Task Execution Router workspace. It should not describe Studio as an LM Studio replacement or a generic local chatbot.

## Static UI Prototype v0.1

The page is a self-contained HTML preview served from `/`. It uses embedded CSS only and does not load external scripts, external stylesheets, CDNs, generated assets, frontend build tools, or runtime integrations.

Page sections:

- Header with `KORA Studio`, `Local v0.1 Skeleton`, and AI Task Execution Router workspace copy
- Status cards for local server state, disabled provider calls, disconnected model/runtime integration, disabled browser launch, and disconnected Ollama integration
- Endpoint panel for `/health` and `/status`
- Workflow preview for request handling, deterministic checks, local status, and a future runtime placeholder
- Limitations panel with explicit no-provider, no-model/runtime, no-Ollama, no-browser-launch, and no unsupported-claims boundaries
- Footer with local-only and claim-safe wording

Required future UI narrative:

- System Profile: show what the computer can physically run, including OS, CPU/GPU, RAM/VRAM/unified memory, runtime, and installed models.
- Model Capability: distinguish physically runnable local models, larger-model workflow feasibility, and optional external/provider/distributed routes.
- KORA Boost Explanation: explain that Standard Mode sends every step to the model, while KORA Boost routes deterministic and structured work to CPU/local fast paths first.
- Execution Path UI: show deterministic code, structured lookup, local model, larger model, and external/provider/distributed route disabled by default.

## How to Run

```bash
python3 -m kora studio --serve
```

Open the local page at:

```text
http://127.0.0.1:8765/
```

The server remains localhost-only by default. Browser auto-launch is not implemented.

Planned default launch behavior is `kora studio`: start the localhost-only Studio server, open the default browser automatically, keep provider calls and cloud sync disabled by default, and require no API key for default local mode. If browser launch fails, Studio should print the local URL and keep serving locally.

Planned developer options include `kora studio --no-browser`, `kora studio --port 8765`, and an optional future browser selector such as `--browser chrome`.

## Endpoints

- `/` serves the static UI prototype v0.1
- `/health` returns local health status JSON
- `/status` returns local preview status, KORA Boost copy, docs paths, and fixture paths

## Current Limitations

- no full frontend yet
- no browser launch
- no Ollama integration
- no provider calls
- no model/runtime integration yet
- no project UI yet
- no API keys required
- no client-side calls, telemetry, local storage, or session storage

## Claim Boundary

The page is for deterministic-first local workflow exploration. It does not create production claims, API-cost claims, energy claims, benchmark claims, provider-validation claims, or deployment-readiness claims.

KORA does not make large models smaller, does not remove RAM/VRAM/unified-memory/model-loading requirements, and does not claim to run unsupported larger models on local hardware. Larger-model workflow feasibility depends on actual memory, runtime support, quantization, and validation.

## Privacy Boundary

The placeholder page is static and self-contained. It does not expose environment variables, provider responses, private data, private internals, campaign material, or proprietary datasets.
