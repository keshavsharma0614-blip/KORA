from __future__ import annotations

from kora.studio_execution_fixture import (
    EXECUTION_EVENT_SCHEMA_FIELDS,
    EXECUTION_VIEWER_CLAIM_BOUNDARY,
    FINAL_COUNTERS,
    STANDARD_VS_KORA_CLAIM_BOUNDARY,
    STANDARD_VS_KORA_METRICS,
    get_execution_viewer_fixture_events,
    get_execution_viewer_fixture_summary,
    get_standard_vs_kora_comparison_fixture,
    get_standard_vs_kora_status_fields,
    validate_execution_viewer_event,
)


def test_execution_event_schema_includes_required_fields() -> None:
    required_fields = {
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
    }

    assert required_fields == set(EXECUTION_EVENT_SCHEMA_FIELDS)


def test_execution_viewer_fixture_events_cover_v0_1_stages() -> None:
    events = get_execution_viewer_fixture_events()
    stage_ids = [event["stage_id"] for event in events]

    assert stage_ids == [
        "request_received",
        "deterministic_route_check",
        "structured_lookup",
        "validation_pass",
        "model_fallback_skipped",
        "final_counters",
    ]
    assert all(validate_execution_viewer_event(event) for event in events)


def test_execution_viewer_fixture_is_local_only_and_claim_safe() -> None:
    events = get_execution_viewer_fixture_events()

    assert "local fixture/mock data" in EXECUTION_VIEWER_CLAIM_BOUNDARY
    assert "do not execute models" in EXECUTION_VIEWER_CLAIM_BOUNDARY
    assert "call providers" in EXECUTION_VIEWER_CLAIM_BOUNDARY
    assert "download models" in EXECUTION_VIEWER_CLAIM_BOUNDARY
    for event in events:
        assert event["adapter_name"] == "mock"
        assert event["adapter_mode"] == "fixture"
        assert event["provider_calls_enabled"] is False
        assert event["cloud_sync_enabled"] is False
        assert event["model_called"] is False
        assert event["error_code"] is None
        assert event["error_message"] is None


def test_execution_viewer_final_counters_match_fixture_summary() -> None:
    events = get_execution_viewer_fixture_events()
    final_event = events[-1]

    assert final_event["stage_id"] == "final_counters"
    assert final_event["counters_snapshot"] == FINAL_COUNTERS
    assert final_event["counters_snapshot"]["baseline_model_calls"] == 1
    assert final_event["counters_snapshot"]["kora_model_calls"] == 0
    assert final_event["counters_snapshot"]["avoided_model_calls"] == 1
    assert final_event["counters_snapshot"]["validation_pass_count"] == 1
    assert final_event["counters_snapshot"]["model_escalations"] == 0


def test_execution_viewer_fixture_summary_exposes_status_fields() -> None:
    summary = get_execution_viewer_fixture_summary()

    assert summary["execution_viewer_status"] == "fixture_mock_scaffold"
    assert summary["execution_viewer_fixture_event_count"] == 6
    assert summary["execution_viewer_event_schema_fields"] == EXECUTION_EVENT_SCHEMA_FIELDS
    assert summary["execution_viewer_fixture_events"]
    assert summary["execution_viewer_claim_boundary"] == EXECUTION_VIEWER_CLAIM_BOUNDARY
    assert summary["model_execution_connected"] is False
    assert summary["download_connected"] is False
    assert summary["provider_calls_enabled"] is False
    assert summary["cloud_sync_enabled"] is False


def test_standard_vs_kora_comparison_fixture_metrics_are_claim_safe() -> None:
    comparison = get_standard_vs_kora_comparison_fixture()
    modes = {mode["mode"]: mode for mode in comparison["modes"]}

    assert comparison["comparison_status"] == "fixture_mock_scaffold"
    assert comparison["metrics"] == STANDARD_VS_KORA_METRICS
    assert comparison["metrics"]["baseline_model_calls"] == 1
    assert comparison["metrics"]["kora_model_calls"] == 0
    assert comparison["metrics"]["avoided_model_calls"] == 1
    assert comparison["metrics"]["deterministic_routes"] == 1
    assert comparison["metrics"]["model_escalations"] == 0
    assert comparison["metrics"]["validation_pass_count"] == 1
    assert modes["standard"]["model_call_count"] == 1
    assert modes["kora_boost"]["model_call_count"] == 0
    assert modes["kora_boost"]["deterministic_route_used"] is True
    assert modes["kora_boost"]["validation_result"] == "pass"
    assert comparison["provider_calls_enabled"] is False
    assert comparison["cloud_sync_enabled"] is False
    assert comparison["model_execution_connected"] is False
    assert comparison["download_connected"] is False
    assert comparison["cost_claim_enabled"] is False
    assert comparison["energy_claim_enabled"] is False
    assert comparison["claim_boundary"] == STANDARD_VS_KORA_CLAIM_BOUNDARY
    assert "prove production savings" in comparison["claim_boundary"]
    assert "prove energy outcomes" in comparison["claim_boundary"]


def test_standard_vs_kora_status_fields_expose_metric_cards() -> None:
    status_fields = get_standard_vs_kora_status_fields()

    assert status_fields["standard_vs_kora_comparison_status"] == "fixture_mock_scaffold"
    assert status_fields["standard_vs_kora_metrics"] == STANDARD_VS_KORA_METRICS
    assert len(status_fields["standard_vs_kora_metric_cards"]) == 6
    assert status_fields["standard_vs_kora_claim_boundary"] == STANDARD_VS_KORA_CLAIM_BOUNDARY
    assert all(
        card["claim_safety_note"] == "Display as local fixture/mock comparison data only."
        for card in status_fields["standard_vs_kora_metric_cards"]
    )
