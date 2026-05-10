from __future__ import annotations

import json
from pathlib import Path
from typing import Any

FIXTURE_DIR = Path("docs/kora-studio/fixtures")
REQUIRED_COUNTERS = {
    "total_requests",
    "baseline_model_calls",
    "kora_model_calls",
    "avoided_model_calls",
    "avoided_model_call_rate",
    "deterministic_routes",
    "model_escalations",
    "validation_pass_count",
    "validation_fail_count",
    "error_count",
    "fallback_count",
}
APPROVED_BOOST_MESSAGE = "Less waiting. Better answers. No hardware upgrade."
BLOCKED_KEY_FRAGMENTS = {
    "api_key",
    "password",
    "raw_provider_response",
    "raw_response",
    "provider_response",
}
POSITIVE_CLAIM_PHRASES = {
    "production cost savings",
    "real api-cost savings",
    "energy savings",
    "production validated",
    "production validation proof",
}


def _fixture_paths() -> list[Path]:
    return sorted(FIXTURE_DIR.glob("*.json"))


def _walk(value: Any) -> list[Any]:
    items = [value]
    if isinstance(value, dict):
        for key, nested in value.items():
            items.append(key)
            items.extend(_walk(nested))
    elif isinstance(value, list):
        for nested in value:
            items.extend(_walk(nested))
    return items


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    assert isinstance(data, dict), f"{path} must contain a JSON object"
    return data


def test_kora_studio_json_fixtures_are_valid() -> None:
    paths = _fixture_paths()
    assert paths, "expected KORA Studio JSON fixtures"

    for path in paths:
        data = _load(path)
        assert data.get("fixture_id"), f"{path} missing fixture_id"
        assert data.get("fixture_type"), f"{path} missing fixture_type"


def test_kora_studio_fixtures_use_synthetic_privacy_class() -> None:
    for path in _fixture_paths():
        data = _load(path)
        privacy_class = data.get("privacy_class")
        if privacy_class is not None:
            assert privacy_class == "synthetic", f"{path} must use synthetic privacy"
        project = data.get("project")
        if isinstance(project, dict) and "privacy_class" in project:
            assert project["privacy_class"] == "synthetic", f"{path} project must be synthetic"


def test_kora_studio_fixtures_do_not_include_secret_or_raw_response_fields() -> None:
    for path in _fixture_paths():
        data = _load(path)
        for item in _walk(data):
            if not isinstance(item, str):
                continue
            lowered = item.lower()
            assert not lowered.startswith("sk-"), f"{path} contains secret-looking token"
            assert not lowered.startswith("ghp_"), f"{path} contains GitHub token-looking value"
            for blocked in BLOCKED_KEY_FRAGMENTS:
                assert blocked not in lowered, f"{path} contains blocked field or value {blocked!r}"


def test_kora_studio_summary_and_counter_fixtures_include_required_counters() -> None:
    for path in _fixture_paths():
        data = _load(path)
        fixture_type = str(data.get("fixture_type"))
        if fixture_type in {"local_validation_summary", "customer_support_triage_summary"}:
            assert REQUIRED_COUNTERS.issubset(data), f"{path} missing required counters"
        if fixture_type == "dashboard_counters":
            card_keys = {card.get("key") for card in data.get("cards", [])}
            assert REQUIRED_COUNTERS == card_keys, f"{path} dashboard cards must match counters"
        if fixture_type == "report_viewer_metadata":
            counters = data.get("counters")
            assert isinstance(counters, dict), f"{path} missing counters object"
            assert REQUIRED_COUNTERS.issubset(counters), f"{path} missing report counters"


def test_kora_boost_copy_fixture_uses_approved_marketing_message() -> None:
    data = _load(FIXTURE_DIR / "kora-boost-mode-card.sample.json")
    assert data["marketing_message"] == APPROVED_BOOST_MESSAGE
    assert data["kora_boost_copy"]["description"] == APPROVED_BOOST_MESSAGE


def test_kora_studio_fixtures_do_not_make_positive_cost_or_energy_claims() -> None:
    for path in _fixture_paths():
        data = _load(path)
        text_values = [item.lower() for item in _walk(data) if isinstance(item, str)]
        for text in text_values:
            for phrase in POSITIVE_CLAIM_PHRASES:
                assert phrase not in text, f"{path} contains positive claim phrase {phrase!r}"
