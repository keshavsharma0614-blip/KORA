"""Local-only KORA Studio runtime availability scaffold."""

from __future__ import annotations

import shutil
from collections.abc import Callable
from copy import deepcopy
from typing import Any

ExecutableDetector = Callable[[str], str | None]

RUNTIME_STATUS_CLAIM_BOUNDARY = (
    "Runtime status is local-only and fail-closed. Catalog examples are not the same as installed models. "
    "Download and execution are not connected yet."
)

RUNTIME_CANDIDATES = [
    {
        "runtime_id": "ollama",
        "display_name": "Ollama",
        "commands": ["ollama"],
        "detection_method": "local_executable_path",
    },
    {
        "runtime_id": "llama_cpp",
        "display_name": "llama.cpp",
        "commands": ["llama-cli", "llama"],
        "detection_method": "local_executable_path",
    },
    {
        "runtime_id": "mock",
        "display_name": "Mock runtime",
        "commands": [],
        "detection_method": "built_in_mock_placeholder",
    },
]


def get_runtime_status(which: ExecutableDetector = shutil.which) -> list[dict[str, Any]]:
    """Return runtime status without starting services or executing models."""

    statuses: list[dict[str, Any]] = []
    for candidate in RUNTIME_CANDIDATES:
        commands = candidate["commands"]
        executable_path = None
        if commands:
            executable_path = next((which(command) for command in commands if which(command)), None)
        executable_detected = executable_path is not None or candidate["runtime_id"] == "mock"
        statuses.append(
            {
                "runtime_id": candidate["runtime_id"],
                "display_name": candidate["display_name"],
                "executable_detected": executable_detected,
                "executable_path": executable_path,
                "service_reachable": False,
                "service_check_status": "not_checked",
                "installed_models_detected": False,
                "installed_models": [],
                "detection_method": candidate["detection_method"],
                "detection_status": "detected" if executable_detected else "not_detected",
                "claim_boundary": RUNTIME_STATUS_CLAIM_BOUNDARY,
            }
        )
    return statuses


def summarize_installed_models(runtime_status: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize installed model detection without claiming unavailable data."""

    installed_models: list[dict[str, Any]] = []
    for runtime in runtime_status:
        models = runtime.get("installed_models", [])
        if isinstance(models, list):
            for model in models:
                if isinstance(model, dict):
                    installed_models.append(deepcopy(model))

    return {
        "installed_models_detected": bool(installed_models),
        "installed_models": installed_models,
        "installed_model_count": len(installed_models),
        "detection_status": "not_checked" if not installed_models else "detected",
        "claim_boundary": (
            "Installed model detection is local-only and may be unknown. Catalog examples are not installed models."
        ),
    }


def runtime_status_by_id(runtime_status: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Index runtime status by runtime id."""

    return {
        str(item["runtime_id"]): item
        for item in runtime_status
        if isinstance(item, dict) and "runtime_id" in item
    }
