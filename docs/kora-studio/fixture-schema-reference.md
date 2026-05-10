# KORA Studio Fixture Schema Reference

## Purpose

This doc describes static fixture shapes for future KORA Studio UI work. The fixtures are planning samples only and do not mean KORA Studio is implemented.

## Common Fields

- `fixture_id`: stable identifier for the sample artifact.
- `fixture_type`: sample category, such as `local_validation_summary`, `dashboard_counters`, or `project_chat_session`.
- `mode`: validation or UI mode represented by the fixture.
- `provider`: local validation or runtime label represented by the fixture.
- `model`: model label represented by the fixture.
- `privacy_class`: fixture privacy class; public Studio fixtures should use `synthetic`.
- `claim_boundary`: explicit boundary text for what the fixture does and does not show.

## Counter Fields

- `total_requests`: number of requests or tasks represented by the sample.
- `baseline_model_calls`: model-call events recorded by the direct baseline path.
- `kora_model_calls`: model-call events recorded by the KORA-controlled path.
- `avoided_model_calls`: baseline model calls minus KORA model calls.
- `avoided_model_call_rate`: avoided model calls divided by baseline model calls when available.
- `deterministic_routes`: requests handled by deterministic or fast local paths.
- `model_escalations`: requests escalated to the selected model-call path.
- `validation_pass_count`: validation checks that passed.
- `validation_fail_count`: validation checks that failed.
- `error_count`: runtime or validation errors counted by the sample.
- `fallback_count`: requests that fell back because a route was unsupported or unresolved.

## Project Chat Fields

- `project`: project metadata, including project id, name, mode, selected model, runtime, and privacy class.
- `messages`: synthetic user and assistant messages for a future project chat UI mock.
- `execution_traces`: route-level trace objects connected to messages.

## Report Viewer Fields

- `report_title`: display title for the report.
- `report_path`: local sample path used for UI planning.
- `sections`: expected report sections for navigation.
- `counters`: aggregate counter object extracted from a report or companion JSON.
- `boundary_warnings`: warnings the UI should keep visible near report content.

## Claim-Safe Display Rules

- show measured counters only
- do not convert avoided model calls into cost savings
- do not show energy savings
- do not imply production validation
- label local/no-network validation clearly
