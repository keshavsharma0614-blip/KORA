from __future__ import annotations

import pytest

from kora.studio_harness_comparison import (
    LOCAL_HARNESS_COMPARISON_CLAIM_BOUNDARY,
    build_local_harness_comparison,
    get_local_harness_comparison_status_fields,
)


def test_local_harness_comparison_counts_standard_and_kora_paths() -> None:
    comparison = build_local_harness_comparison("local-harness-json-required-fields-001")
    modes = {mode["mode"]: mode for mode in comparison["modes"]}

    assert comparison["comparison_status"] == "local_deterministic_harness_generated"
    assert comparison["comparison_source"] == "local_harness_summary"
    assert comparison["request_id"] == "local-harness-json-required-fields-001"
    assert comparison["metrics"]["baseline_model_calls"] == 1
    assert comparison["metrics"]["kora_model_calls"] == 0
    assert comparison["metrics"]["avoided_model_calls"] == 1
    assert comparison["metrics"]["deterministic_routes"] == 1
    assert comparison["metrics"]["model_escalations"] == 0
    assert comparison["metrics"]["validation_pass_count"] == 1
    assert modes["standard"]["model_call_counted"] is True
    assert modes["standard"]["model_called"] is False
    assert modes["standard"]["model_execution_connected"] is False
    assert modes["kora_boost"]["model_call_counted"] is False
    assert modes["kora_boost"]["deterministic_route_used"] is True
    assert modes["kora_boost"]["model_called"] is False
    assert modes["kora_boost"]["model_execution_connected"] is False


def test_local_harness_comparison_handles_model_needed_boundary_without_execution() -> None:
    comparison = build_local_harness_comparison("local-harness-ambiguous-model-needed-001")
    kora_mode = next(mode for mode in comparison["modes"] if mode["mode"] == "kora_boost")

    assert comparison["expected_model_needed"] is True
    assert comparison["metrics"]["baseline_model_calls"] == 1
    assert comparison["metrics"]["kora_model_calls"] == 0
    assert comparison["metrics"]["avoided_model_calls"] == 0
    assert comparison["metrics"]["model_escalations"] == 1
    assert kora_mode["model_needed_boundary"] is True
    assert kora_mode["model_called"] is False
    assert any(event["stage_id"] == "model_needed_boundary" for event in comparison["harness_events"])


def test_local_harness_comparison_is_local_only_and_claim_safe() -> None:
    comparison = build_local_harness_comparison("local-harness-known-faq-001")

    assert comparison["claim_boundary"] == LOCAL_HARNESS_COMPARISON_CLAIM_BOUNDARY
    assert "local deterministic harness data" in comparison["claim_boundary"]
    assert "does not execute models" in comparison["claim_boundary"]
    assert "call providers" in comparison["claim_boundary"]
    assert "prove cost or energy outcomes" in comparison["claim_boundary"]
    assert comparison["provider_calls_enabled"] is False
    assert comparison["cloud_sync_enabled"] is False
    assert comparison["model_execution_connected"] is False
    assert comparison["download_connected"] is False
    assert comparison["cost_claim_enabled"] is False
    assert comparison["energy_claim_enabled"] is False
    assert all(card["claim_safety_note"] == "Display as local deterministic harness output only." for card in comparison["metric_cards"])


def test_local_harness_comparison_status_fields() -> None:
    status_fields = get_local_harness_comparison_status_fields()

    assert status_fields["local_harness_comparison_status"] == "local_deterministic_harness_generated"
    assert status_fields["local_harness_comparison"]["comparison_source"] == "local_harness_summary"
    assert status_fields["comparison_counters"]["baseline_model_calls"] == 1
    assert status_fields["comparison_counters"]["kora_model_calls"] == 0
    assert status_fields["comparison_counters"]["avoided_model_calls"] == 1
    assert status_fields["comparison_claim_boundary"] == LOCAL_HARNESS_COMPARISON_CLAIM_BOUNDARY
    assert len(status_fields["local_harness_comparison_metric_cards"]) == 6


def test_local_harness_comparison_rejects_unknown_request_id() -> None:
    with pytest.raises(ValueError, match="Unknown local harness request id"):
        build_local_harness_comparison("missing-request")
