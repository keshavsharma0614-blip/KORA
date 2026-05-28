"""Local fixture events for the KORA Studio execution viewer scaffold."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

EXECUTION_VIEWER_CLAIM_BOUNDARY = (
    "Execution Viewer events are local fixture/mock data. They do not execute models, call providers, "
    "download models, or prove production behavior."
)
STANDARD_VS_KORA_CLAIM_BOUNDARY = (
    "Standard Mode vs KORA Boost comparison data is a local fixture/mock comparison. It does not execute models, "
    "call providers, prove production savings, prove real API billing changes, or prove energy outcomes."
)

EXECUTION_EVENT_SCHEMA_FIELDS = [
    "run_id",
    "request_id",
    "stage_id",
    "stage_name",
    "route_class",
    "status",
    "started_at",
    "completed_at",
    "latency_ms",
    "model_called",
    "deterministic_route_used",
    "structured_lookup_used",
    "validation_result",
    "adapter_name",
    "adapter_mode",
    "provider_calls_enabled",
    "cloud_sync_enabled",
    "counters_snapshot",
    "error_code",
    "error_message",
]

FINAL_COUNTERS = {
    "total_requests": 1,
    "baseline_model_calls": 1,
    "kora_model_calls": 0,
    "avoided_model_calls": 1,
    "avoided_model_call_rate": 1.0,
    "deterministic_routes": 1,
    "structured_lookup_routes": 1,
    "policy_routes": 0,
    "model_escalations": 0,
    "validation_pass_count": 1,
    "validation_fail_count": 0,
    "error_count": 0,
    "fallback_count": 0,
}

STANDARD_VS_KORA_METRICS = {
    "baseline_model_calls": 1,
    "kora_model_calls": 0,
    "avoided_model_calls": 1,
    "deterministic_routes": 1,
    "model_escalations": 0,
    "validation_pass_count": 1,
}


def _event(
    *,
    stage_id: str,
    stage_name: str,
    route_class: str,
    status: str,
    started_at: str,
    completed_at: str,
    latency_ms: int,
    model_called: bool = False,
    deterministic_route_used: bool = False,
    structured_lookup_used: bool = False,
    validation_result: str = "not_applicable",
    counters_snapshot: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "run_id": "fixture-run-local-router-001",
        "request_id": "fixture-request-support-001",
        "stage_id": stage_id,
        "stage_name": stage_name,
        "route_class": route_class,
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at,
        "latency_ms": latency_ms,
        "model_called": model_called,
        "deterministic_route_used": deterministic_route_used,
        "structured_lookup_used": structured_lookup_used,
        "validation_result": validation_result,
        "adapter_name": "mock",
        "adapter_mode": "fixture",
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "counters_snapshot": deepcopy(counters_snapshot or {}),
        "error_code": None,
        "error_message": None,
    }


def get_execution_viewer_fixture_events() -> list[dict[str, Any]]:
    """Return deterministic fixture events without model execution or provider calls."""

    return [
        _event(
            stage_id="request_received",
            stage_name="Request received",
            route_class="input",
            status="completed",
            started_at="2026-05-29T00:00:00Z",
            completed_at="2026-05-29T00:00:00.010Z",
            latency_ms=10,
            counters_snapshot={"total_requests": 1, "baseline_model_calls": 1},
        ),
        _event(
            stage_id="deterministic_route_check",
            stage_name="Deterministic route check",
            route_class="deterministic_code",
            status="completed",
            started_at="2026-05-29T00:00:00.010Z",
            completed_at="2026-05-29T00:00:00.024Z",
            latency_ms=14,
            deterministic_route_used=True,
            counters_snapshot={"deterministic_routes": 1, "model_escalations": 0},
        ),
        _event(
            stage_id="structured_lookup",
            stage_name="Structured lookup",
            route_class="structured_lookup",
            status="completed",
            started_at="2026-05-29T00:00:00.024Z",
            completed_at="2026-05-29T00:00:00.041Z",
            latency_ms=17,
            deterministic_route_used=True,
            structured_lookup_used=True,
            counters_snapshot={"structured_lookup_routes": 1},
        ),
        _event(
            stage_id="validation_pass",
            stage_name="Validation pass",
            route_class="validation",
            status="completed",
            started_at="2026-05-29T00:00:00.041Z",
            completed_at="2026-05-29T00:00:00.052Z",
            latency_ms=11,
            deterministic_route_used=True,
            structured_lookup_used=True,
            validation_result="pass",
            counters_snapshot={"validation_pass_count": 1, "validation_fail_count": 0},
        ),
        _event(
            stage_id="model_fallback_skipped",
            stage_name="Model fallback skipped",
            route_class="local_model",
            status="skipped",
            started_at="2026-05-29T00:00:00.052Z",
            completed_at="2026-05-29T00:00:00.052Z",
            latency_ms=0,
            deterministic_route_used=True,
            structured_lookup_used=True,
            validation_result="pass",
            counters_snapshot={"kora_model_calls": 0, "avoided_model_calls": 1},
        ),
        _event(
            stage_id="final_counters",
            stage_name="Final counters",
            route_class="summary",
            status="completed",
            started_at="2026-05-29T00:00:00.052Z",
            completed_at="2026-05-29T00:00:00.052Z",
            latency_ms=0,
            deterministic_route_used=True,
            structured_lookup_used=True,
            validation_result="pass",
            counters_snapshot=FINAL_COUNTERS,
        ),
    ]


def validate_execution_viewer_event(event: dict[str, Any]) -> bool:
    """Return whether a fixture event includes the required UI/report schema fields."""

    return all(field in event for field in EXECUTION_EVENT_SCHEMA_FIELDS)


def get_execution_viewer_fixture_summary() -> dict[str, Any]:
    """Return the local execution viewer fixture summary for /status."""

    events = get_execution_viewer_fixture_events()
    return {
        "execution_viewer_status": "fixture_mock_scaffold",
        "execution_viewer_event_schema_fields": list(EXECUTION_EVENT_SCHEMA_FIELDS),
        "execution_viewer_fixture_event_count": len(events),
        "execution_viewer_fixture_events": events,
        "execution_viewer_claim_boundary": EXECUTION_VIEWER_CLAIM_BOUNDARY,
        "model_execution_connected": False,
        "download_connected": False,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
    }


def get_standard_vs_kora_comparison_fixture() -> dict[str, Any]:
    """Return local fixture comparison data without model execution or provider calls."""

    return {
        "comparison_status": "fixture_mock_scaffold",
        "fixture_id": "kora_studio_standard_vs_kora_comparison_v0_1",
        "fixture_type": "standard_vs_kora_comparison",
        "privacy_class": "synthetic",
        "comparison_input": "Classify a synthetic support request using a known local route.",
        "modes": [
            {
                "mode": "standard",
                "display_name": "Standard Mode",
                "route_summary": "Fixture baseline sends the request to the selected model path by default.",
                "model_call_count": 1,
                "deterministic_route_used": False,
                "structured_lookup_used": False,
                "validation_result": "not_applicable",
                "provider_calls_enabled": False,
                "cloud_sync_enabled": False,
                "model_execution_connected": False,
            },
            {
                "mode": "kora_boost",
                "display_name": "KORA Boost",
                "route_summary": (
                    "Fixture KORA path checks deterministic and structured routes first; validation passes and "
                    "model fallback is skipped."
                ),
                "model_call_count": 0,
                "deterministic_route_used": True,
                "structured_lookup_used": True,
                "validation_result": "pass",
                "provider_calls_enabled": False,
                "cloud_sync_enabled": False,
                "model_execution_connected": False,
            },
        ],
        "metrics": deepcopy(STANDARD_VS_KORA_METRICS),
        "metric_cards": [
            {
                "key": key,
                "label": label,
                "value": STANDARD_VS_KORA_METRICS[key],
                "claim_safety_note": "Display as local fixture/mock comparison data only.",
            }
            for key, label in [
                ("baseline_model_calls", "Baseline model calls"),
                ("kora_model_calls", "KORA model calls"),
                ("avoided_model_calls", "Avoided model calls"),
                ("deterministic_routes", "Deterministic routes"),
                ("model_escalations", "Model escalations"),
                ("validation_pass_count", "Validation passes"),
            ]
        ],
        "claim_boundary": STANDARD_VS_KORA_CLAIM_BOUNDARY,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
        "cost_claim_enabled": False,
        "energy_claim_enabled": False,
    }


def get_standard_vs_kora_status_fields() -> dict[str, Any]:
    """Return /status fields for the Standard Mode vs KORA Boost fixture."""

    comparison = get_standard_vs_kora_comparison_fixture()
    return {
        "standard_vs_kora_comparison_status": comparison["comparison_status"],
        "standard_vs_kora_comparison": comparison,
        "standard_vs_kora_metrics": deepcopy(comparison["metrics"]),
        "standard_vs_kora_metric_cards": deepcopy(comparison["metric_cards"]),
        "standard_vs_kora_claim_boundary": comparison["claim_boundary"],
    }
