# KORA First Paper Citation Audit v0.1

## Purpose

This audit checks reference consistency, citation safety, and claim boundaries for manuscript v0.2. It is a bibliography-readiness document, not a final bibliography and not a submission-readiness claim.

## Scope

This audit covers:

- manuscript v0.2
- references [R01] through [R10]
- preliminary references section
- related work framing
- claim boundary language

It does not add BibTeX, final citation style, new references, or new evidence claims.

## Citation Inventory

| ID | Reference topic | Appears in manuscript | Appears in References section | Tracker status | Action |
|---|---|---|---|---|---|
| [R01] | vLLM / PagedAttention | Yes | Yes | verified | normalize later |
| [R02] | MLPerf Inference | Yes | Yes | verified | normalize later |
| [R03] | ONNX Runtime docs | Yes | Yes | verified | needs citation style decision |
| [R04] | LangGraph Graph API docs | Yes | Yes | verified | needs citation style decision |
| [R05] | DSPy | Yes | Yes | verified | normalize later |
| [R06] | Retrieval-Augmented Generation | Yes | Yes | verified | normalize later |
| [R07] | Apache Airflow DAG docs | Yes | Yes | verified | needs citation style decision |
| [R08] | Snakemake | Yes | Yes | verified | normalize later |
| [R09] | llama.cpp | Yes | Yes | verified | needs citation style decision |
| [R10] | ACM Artifact Review and Badging | Yes | Yes | verified | needs citation style decision |

## Reference Normalization Status

### [R01] vLLM / PagedAttention

- Preliminary reference usability: usable as a preliminary paper reference.
- Metadata still missing: final venue/citation-format normalization.
- BibTeX ready: no.
- Source traceability: traceable to arXiv URL and DOI recorded in the tracker.

### [R02] MLPerf Inference

- Preliminary reference usability: usable as a preliminary benchmark-methodology reference.
- Metadata still missing: final citation-format normalization and full author handling.
- BibTeX ready: no.
- Source traceability: traceable to arXiv URL recorded in the tracker.

### [R03] ONNX Runtime docs

- Preliminary reference usability: usable as official documentation context.
- Metadata still missing: final documentation citation style and exact access-date formatting.
- BibTeX ready: no.
- Source traceability: traceable to official documentation URL recorded in the tracker.

### [R04] LangGraph Graph API docs

- Preliminary reference usability: usable as official documentation context.
- Metadata still missing: final documentation citation style and exact access-date formatting.
- BibTeX ready: no.
- Source traceability: traceable to official documentation URL recorded in the tracker.

### [R05] DSPy

- Preliminary reference usability: usable as a preliminary programmatic-LM-workflow reference.
- Metadata still missing: final venue/citation-format normalization.
- BibTeX ready: no.
- Source traceability: traceable to arXiv URL recorded in the tracker.

### [R06] Retrieval-Augmented Generation

- Preliminary reference usability: usable as a preliminary RAG background reference.
- Metadata still missing: final citation-format normalization.
- BibTeX ready: no.
- Source traceability: traceable to arXiv URL and DOI recorded in the tracker.

### [R07] Apache Airflow DAG docs

- Preliminary reference usability: usable as official DAG/workflow documentation context.
- Metadata still missing: final documentation citation style and exact access-date formatting.
- BibTeX ready: no.
- Source traceability: traceable to official Apache Airflow documentation URL recorded in the tracker.

### [R08] Snakemake

- Preliminary reference usability: usable as a preliminary workflow-engine reference.
- Metadata still missing: final citation-format normalization.
- BibTeX ready: no.
- Source traceability: traceable to DOI recorded in the tracker.

### [R09] llama.cpp

- Preliminary reference usability: usable as official repository context for future local runtime work.
- Metadata still missing: final software/repository citation style and exact access-date formatting.
- BibTeX ready: no.
- Source traceability: traceable to official GitHub repository URL recorded in the tracker.

### [R10] ACM Artifact Review and Badging

- Preliminary reference usability: usable as official artifact-practice guidance context.
- Metadata still missing: final policy/documentation citation style.
- BibTeX ready: no.
- Source traceability: traceable to official ACM policy URL recorded in the tracker.

## Claim-Support Mapping

| Claim or statement type | References used | Supported use | Boundary |
|---|---|---|---|
| LLM serving systems context | [R01], [R02], [R03] | Background on model serving, inference benchmarking, and runtime context | Does not support KORA outperforming serving systems. |
| Workflow/DAG orchestration context | [R07], [R08] | Background on explicit workflows, DAGs, and reproducible pipelines | Does not support KORA replacing workflow systems. |
| Agent/programmatic AI context | [R04], [R05] | Background on graph-based agent execution and programmatic LM workflows | Does not support KORA replacing agent frameworks. |
| RAG context | [R06] | Background for retrieval-grounded generation and contrast with KORA routing | Does not support KORA replacing RAG. |
| Local runtime context | [R03], [R09] | Future-work context for local model/runtime systems | Does not support current local runtime validation evidence. |
| Benchmarking/reproducibility context | [R02] | Benchmark-methodology background | Does not support KORA production benchmark proof. |
| Artifact evaluation context | [R10] | Artifact-practice and transparency background | Does not indicate formal artifact evaluation approval. |
| KORA 80/100 result | KORA benchmark docs and reproducible deterministic-heavy benchmark evidence | Supports the approved deterministic-heavy benchmark claim | External references do not imply production savings, real API-cost reduction, energy reduction, or broad superiority. |

## Forbidden Citation Uses

- Do not cite external systems as proof KORA is superior.
- Do not cite references as production cost reduction proof.
- Do not cite references as real API-cost reduction proof.
- Do not cite references as energy reduction evidence.
- Do not cite references as production benchmark evidence.
- Do not cite references as formal artifact evaluation approval.

## Bibliography Gaps

- Final citation style selection pending.
- BibTeX pending.
- Exact venue/metadata audit pending where needed.
- Additional references needed for agent/tool-use.
- Semantic caching references may be needed.
- Synthetic workload reproducibility references may be needed.
- Local runtime references may need expansion.
- Venue-specific artifact guidance may be needed.

## Next Step

- Task 316C or later: bibliography normalization pass after citation style decision.
- Optional additional reference verification pass for missing categories.
- Manuscript v0.3 only after bibliography and claim audit are stable.
