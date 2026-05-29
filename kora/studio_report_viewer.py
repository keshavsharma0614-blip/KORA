"""Local report viewer placeholder data for KORA Studio."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

REPORT_VIEWER_FIXTURE_PATH = "docs/kora-studio/fixtures/report-viewer-metadata.sample.json"
REPORT_VIEWER_CLAIM_BOUNDARY = (
    "Report viewer data is local summary metadata only. It does not scan arbitrary local files, upload reports, "
    "commit generated reports, call providers, or create new benchmark evidence."
)
REPORT_EXPORT_CLAIM_BOUNDARY = (
    "Report export is a placeholder in this scaffold. No report file is generated, uploaded, or committed."
)

REPORT_VIEWER_COUNTERS = {
    "total_requests": 12,
    "baseline_model_calls": 12,
    "kora_model_calls": 4,
    "avoided_model_calls": 8,
    "avoided_model_call_rate": 0.6667,
    "deterministic_routes": 8,
    "model_escalations": 4,
    "validation_pass_count": 12,
    "validation_fail_count": 0,
    "error_count": 0,
    "fallback_count": 0,
}


def get_report_viewer_placeholder(
    counters: dict[str, Any] | None = None,
    *,
    report_source: str = "fixture_metadata",
) -> dict[str, Any]:
    """Return claim-safe report viewer placeholder data without local file scanning."""

    report_status = (
        "local_harness_summary_placeholder"
        if report_source == "local_harness_summary"
        else "fixture_metadata_placeholder"
    )
    report_title = (
        "Local Harness Summary Report"
        if report_source == "local_harness_summary"
        else "Local No-Network Validation Report"
    )
    report_path_display = "local_harness_summary" if report_source == "local_harness_summary" else "/tmp/kora_customer_support_validation.md"

    return {
        "report_viewer_status": report_status,
        "report_status": report_status,
        "report_source": report_source,
        "fixture_id": "kora_studio_report_viewer_metadata_v0_1",
        "fixture_type": "report_viewer_metadata",
        "report_title": report_title,
        "report_fixture_path": REPORT_VIEWER_FIXTURE_PATH,
        "report_path_display": report_path_display,
        "privacy_class": "synthetic",
        "supported_fixture_only": True,
        "arbitrary_local_file_scan_enabled": False,
        "local_file_picker_connected": False,
        "upload_enabled": False,
        "provider_calls_enabled": False,
        "cloud_sync_enabled": False,
        "model_execution_connected": False,
        "generated_report_commit_enabled": False,
        "file_export_enabled": False,
        "file_written": False,
        "production_evidence_claim": False,
        "cost_claim_enabled": False,
        "energy_claim_enabled": False,
        "sections": ["Summary", "Counters", "Boundary", "Reproduction", "Notes"],
        "counters": deepcopy(counters or REPORT_VIEWER_COUNTERS),
        "boundary_warnings": [
            "Local/no-network summary metadata only.",
            "No arbitrary local file scan is performed.",
            "No cloud upload is connected.",
            "Do not commit generated reports by default.",
            "Do not treat local harness counters as production evidence.",
        ],
        "claim_boundary": REPORT_VIEWER_CLAIM_BOUNDARY,
    }


def get_report_export_placeholder() -> dict[str, Any]:
    """Return disabled local report export placeholder state."""

    return {
        "report_export_status": "placeholder_not_connected",
        "export_formats_planned": ["json_summary", "markdown_summary"],
        "export_action_enabled": False,
        "export_action_label": "Export not connected yet",
        "export_action_reason": "Local report export is planned but not connected in this scaffold.",
        "writes_generated_reports": False,
        "file_written": False,
        "file_export_enabled": False,
        "uploads_reports": False,
        "commits_generated_reports": False,
        "claim_boundary": REPORT_EXPORT_CLAIM_BOUNDARY,
    }


def get_report_viewer_status_fields(
    counters: dict[str, Any] | None = None,
    *,
    report_source: str = "fixture_metadata",
) -> dict[str, Any]:
    """Return /status fields for the report viewer placeholder."""

    viewer = get_report_viewer_placeholder(counters, report_source=report_source)
    export = get_report_export_placeholder()
    return {
        "report_viewer_status": viewer["report_viewer_status"],
        "report_viewer_placeholder": viewer,
        "report_viewer_claim_boundary": viewer["claim_boundary"],
        "report_export_status": export["report_export_status"],
        "report_export_placeholder": export,
        "report_export_claim_boundary": export["claim_boundary"],
    }
