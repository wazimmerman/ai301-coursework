from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "pathreview-unit4"
env = os.environ.copy()
env.update(LLM_PROVIDER="mock", TIKTOKEN_CACHE_DIR="/tmp/ai301-unit4-tiktoken-cache", RUST_LOG="off")
commands = [
    ("raw-array", [".venv/bin/python", "-c", 'import json; from rag.generator.output_parser import parse_review_output; raw=json.dumps(["First feedback item", "Second feedback item"]); print(parse_review_output(raw))'], ROOT),
    ("object-control", [".venv/bin/python", "-c", 'import json; from rag.generator.output_parser import parse_review_output; print(parse_review_output(json.dumps({"summary": "Works"})))'], ROOT),
    ("focused", [".venv/bin/python", "-m", "pytest", "tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback", "--runxfail", "-q", "--tb=short"], ROOT),
    ("parser", [".venv/bin/python", "-m", "pytest", "tests/unit/test_output_parser.py", "-q"], ROOT),
    ("unit", ["make", "test-unit"], ROOT),
    ("integration", ["make", "test-integration"], ROOT),
    ("lint", ["make", "lint"], ROOT),
    ("typecheck", ["make", "typecheck"], ROOT),
    ("format", [".venv/bin/black", "--check", "."], ROOT),
    ("frontend", ["npm", "test", "--", "--run"], ROOT / "frontend"),
]


def run(item):
    label, cmd, cwd = item
    started = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    (HERE / f"final-{label}.stdout.txt").write_text(p.stdout)
    (HERE / f"final-{label}.stderr.txt").write_text(p.stderr)
    record = {"label": label, "command": cmd, "cwd": str(cwd), "started_at": started,
              "exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
    print(json.dumps({"label": label, "exit": p.returncode,
                      "stdout_tail": p.stdout[-450:], "stderr_tail": p.stderr[-250:]}), flush=True)
    return record


metadata = {"captured_at": datetime.now(timezone.utc).isoformat(),
            "env": {k: env[k] for k in ["LLM_PROVIDER", "TIKTOKEN_CACHE_DIR"]}}
for label, cmd in [("head", ["git", "rev-parse", "HEAD"]), ("base", ["git", "rev-parse", "main"]),
                   ("status_before", ["git", "status", "--short"]),
                   ("python", [".venv/bin/python", "--version"]), ("node", ["node", "--version"]),
                   ("uv", ["uv", "--version"])]:
    metadata[label] = subprocess.check_output(cmd, cwd=ROOT, text=True).strip()
with ThreadPoolExecutor(max_workers=5) as pool:
    records = list(pool.map(run, commands))
metadata["status_after"] = subprocess.check_output(["git", "status", "--short"], cwd=ROOT, text=True).strip()
(HERE / "final-results.json").write_text(json.dumps({"metadata": metadata, "records": records}, indent=2))
