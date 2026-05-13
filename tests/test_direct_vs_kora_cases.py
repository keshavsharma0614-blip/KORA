import builtins
import importlib.util
from pathlib import Path


def _load_direct_vs_kora_module():
    script_path = Path("examples/direct_vs_kora/run.py")
    spec = importlib.util.spec_from_file_location("direct_vs_kora_run", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load direct_vs_kora module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_run_cases_offline_has_expected_short_and_long_llm_calls() -> None:
    module = _load_direct_vs_kora_module()
    result = module.run_cases(offline=True)

    assert result["cases"]["short"]["kora"]["llm_calls"] == 0
    assert result["cases"]["long"]["kora"]["llm_calls"] == 1


def test_run_cases_offline_does_not_require_requests(monkeypatch) -> None:
    real_import = builtins.__import__

    def import_without_requests(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "requests":
            raise ModuleNotFoundError("No module named 'requests'")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", import_without_requests)

    module = _load_direct_vs_kora_module()
    result = module.run_cases(offline=True)

    assert result["cases"]["short"]["kora"]["llm_calls"] == 0
    assert result["cases"]["long"]["kora"]["llm_calls"] == 1
