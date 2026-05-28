from __future__ import annotations

from kora.studio_runtime_status import (
    RUNTIME_STATUS_CLAIM_BOUNDARY,
    get_runtime_status,
    summarize_installed_models,
)


def test_runtime_status_returns_safe_default_fields() -> None:
    statuses = get_runtime_status(which=lambda command: None)

    assert {item["runtime_id"] for item in statuses} == {"ollama", "llama_cpp", "mock"}
    for status in statuses:
        assert "runtime_id" in status
        assert "display_name" in status
        assert status["service_reachable"] is False
        assert status["service_check_status"] == "not_checked"
        assert status["installed_models_detected"] is False
        assert status["installed_models"] == []
        assert status["claim_boundary"] == RUNTIME_STATUS_CLAIM_BOUNDARY


def test_runtime_executable_detection_can_be_mocked() -> None:
    def fake_which(command: str) -> str | None:
        return f"/mock/bin/{command}" if command == "ollama" else None

    statuses = get_runtime_status(which=fake_which)
    by_id = {item["runtime_id"]: item for item in statuses}

    assert by_id["ollama"]["executable_detected"] is True
    assert by_id["ollama"]["executable_path"] == "/mock/bin/ollama"
    assert by_id["ollama"]["service_reachable"] is False
    assert by_id["llama_cpp"]["executable_detected"] is False
    assert by_id["mock"]["executable_detected"] is True


def test_installed_model_summary_does_not_claim_models_by_default() -> None:
    summary = summarize_installed_models(get_runtime_status(which=lambda command: None))

    assert summary["installed_models_detected"] is False
    assert summary["installed_models"] == []
    assert summary["installed_model_count"] == 0
    assert summary["detection_status"] == "not_checked"
    assert "Catalog examples are not installed models" in summary["claim_boundary"]
