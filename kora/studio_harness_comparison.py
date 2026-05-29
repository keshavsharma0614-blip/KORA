"""Standard Mode vs KORA Boost comparison from local harness output."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from kora.studio_harness_events import build_local_harness_events
from kora.studio_harness_requests import get_local_harness_request_by_id

LOCAL_HARNESS_COMPARISON_CLAIM_BOUNDARY = (
    "Standard Mode vs KORA Boost comparison is generated from local deterministic harness data. It does not "
    "execute models, call providers, download models, prove production behavior, or prove cost or energy outcomes."
)

LOCAL_HARNESS_COMPARISON_METRIC_LABELS = {
    "baseline_model_calls": "Baseline model calls",
    "kora_model_calls": "KORA model calls",
    "avoided_model_calls": "Avoided model calls",
    "deterministic_routes": "Deterministic routes",
    "model_escalations": "Model escalations",
    "validation_pass_count": "Validation passes",
}


def build_local_harness_comparison(request: dict[str, Any] | str) -> dict[str, Any]:
    """Build a claim-safe Standard Mode vs KORA Boost comparison for one local request."""

    if isinstance(request, str):
        selected_request = get_local_harness_request_by_id(request)
        if selected_request is None:
            raise ValueError(f"Unknown local harness request id: {request}")
    else:
        selected_request = deepcopy(request)

    harness_run = build_local_harness_events(selected_request)
    counters = deepcopy(harness_run["counters_snapshot"])
    metrics = {
        key: counters[key]
        for key in [
            "baseline_model_calls",
            "kora_model_calls",
            "avoided_model_calls",
            "deterministic_routes",
            "model_escalations",
            "validation_pass_count",
        ]
    }
    model_needed = selected_request["expected_model_needed"]
    validation_result = selected_request["expected_validation_result"]

    return {
        "comparison_status": "local_deterministic_harness_generated",
        "comparison_source": "local_harness_summary",
        "request_id": selected_request["request_id"],
        "run_id": harness_run["run_id"],
        "privacy_class": "synthetic",
        "comparison_input": selected_request["input_text"],
        "expected_route_class": selected_request["expected_route_class"],
        "expected_model_needed": model_needed,
        "modes": [
            {
                "mode": "standard",
                "display_name": "Standard Mode",
                "route_summary": "Standard Mode counts the selected model path by default for this local sample.",
                "baseline_model_calls": 1,
                "model_call_counted": True,
                "model_called": False,
                "model_execution_connected": False,
                "deterministic_route_used": False,
                "structured_lookup_used": False,
                "validation_result": "not_applicable",
                "provider_calls_enabled": False,
                "cloud_sync_enabled": False,
            },
            {
                "mode": "kora_boost",
                "display_name": "KORA Boost",
                "route_summary": (
                    "KORA Boost uses the local harness route and validation result before any model path. "
                    "Model-needed boundaries remain not connected in this milestone."
                ),
                "baseline_model_calls": 0,
                "model_call_counted": False,
                "model_called": False,
                "model_execution_connected": False,
                "deterministic_route_used": counters["deterministic_routes"] > 0
                or counters["structured_lookup_routes"] > 0
                or counters["policy_routes"] > 0,
                "structured_lookup_used": counters["structured_lookup_routes"] > 0,
                "validation_result": validation_result,
                "model_needed_boundary": model_needed,
                "provider_calls_enabled": False,
                "cloud_sync_enabled": False,
            },
        ],
        "metrics": metrics,
        "comparison_counters": counters,
        "metric_cards": [
            {
                "key": key,
                "label": label,
                "value": metrics[key],
                "claim_safety_note": "Display as local deterministic harness output only.",
            }
            for key, label in LOCAL_HARNESS_COMPARISON_METRIC_LABELS.items()
        ],
        "harness_events": deepcopy(harness_run["events"]),
        "claim_boundary": LOCAL_HARNESS_COMPARISON_CLAIM_BOUNDARY,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "download_connected": False,
        "cost_claim_enabled": False,
        "energy_claim_enabled": False,
    }


def get_local_harness_comparison_status_fields(request_id: str = "local-harness-json-required-fields-001") -> dict[str, Any]:
    """Return /status fields for local harness-generated comparison data."""

    comparison = build_local_harness_comparison(request_id)
    return {
        "local_harness_comparison_status": comparison["comparison_status"],
        "local_harness_comparison": comparison,
        "comparison_counters": deepcopy(comparison["comparison_counters"]),
        "comparison_claim_boundary": comparison["claim_boundary"],
        "local_harness_comparison_metric_cards": deepcopy(comparison["metric_cards"]),
    }
