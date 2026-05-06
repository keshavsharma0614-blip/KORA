# KORA Category Thesis

Date: `2026-05-06`

## Category Ambition

KORA is not a feature.

KORA is not an agent framework.

KORA is not a prompt wrapper.

KORA is not a model server.

KORA aims to define the AI Execution Control Layer category.

## Category Framing

- Category: AI Execution Control Layer
- Vision phrase: Inference OS for AI systems
- Technical mechanism: task graph, deterministic routing, validation, fallback, telemetry

KORA sits before inference escalation. Its purpose is to structure execution, route deterministic work, validate outputs, and invoke models only when needed.

## vLLM Analogy

vLLM became category-defining for LLM serving.

KORA aims to become category-defining for execution control before unnecessary inference is invoked.

This is an ambition and positioning analogy. It does not claim KORA has already achieved vLLM-level adoption.

## Problem Statement

AI systems are too often LLM-first.

That default creates avoidable pressure across:

- cost
- latency
- reliability
- verification
- infrastructure utilization

When every request moves directly to a model, systems lose the chance to handle deterministic work with cheaper, more reliable, and more inspectable execution paths.

## KORA Thesis

Structure intelligence before scaling it.

KORA's thesis:

- Convert requests into task graphs.
- Route deterministic work away from unnecessary model invocation.
- Escalate only when needed.
- Preserve correctness checks and telemetry.
- Keep model inference as a bounded service rather than the default execution path.

## Category Map

| Area | Examples | Role |
|---|---|---|
| Model serving | vLLM, TGI, Triton | Run and serve models efficiently. |
| Agent frameworks | LangChain, CrewAI, AutoGen | Compose agent workflows and tool use. |
| Observability | LangSmith, Helicone, Arize | Observe model and application behavior. |
| Workflow orchestration | Airflow, Temporal | Coordinate general workflow execution. |
| KORA | AI Execution Control Layer | Control execution before inference escalation. |

## Current Evidence

- Public release: `v0.2.0-alpha`
- Release URL: https://github.com/Krako-Labs/KORA/releases/tag/v0.2.0-alpha
- Benchmark: reproducible 100-task deterministic-heavy benchmark
- Direct-baseline simulated model invocations: `100`
- KORA-controlled simulated model invocations: `20`
- Avoided simulated model invocations: `80`
- Deterministic outputs checked: `80`
- Mismatches: `0`

Current safe benchmark claim:

> In a reproducible 100-task deterministic-heavy benchmark workload, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline.

## Claim Boundaries

The current evidence does not claim:

- production cost reduction proof
- real API-cost reduction proof
- production benchmark proof
- full runtime-integrated benchmark evidence yet
- broad workload superiority proof
- energy reduction evidence yet

## Why This Matters

OSS community:

- gives contributors a clear category to build around
- creates issue, docs, and benchmark tracks that are bigger than one feature
- makes KORA easier to explain to early builders

Paper/publication:

- frames KORA as an execution-control problem, not only a tooling project
- gives the paper a category thesis and evidence boundary
- separates current simulated evidence from future runtime-integrated evaluation

EIC Accelerator:

- positions KORA as infrastructure with ecosystem potential
- clarifies why execution control matters before scaling inference infrastructure
- gives a bounded, evidence-aware narrative

Investors:

- explains why KORA can become a platform category
- distinguishes KORA from agent frameworks, observability tools, and model serving
- keeps traction and evidence claims reviewable

Cloud/data center/telco partners:

- frames KORA around inference demand control and workload routing
- creates a technical bridge to infrastructure utilization conversations
- avoids presenting partner interest as validation unless formally documented

Future grants:

- gives a research and infrastructure thesis
- creates a path from open-source evidence to larger evaluation programs
- supports funding narratives without overclaiming current results
