"""Run the installed Unit 4 skill on captured live sources and committed code.

The collector reads scope first, then records actual command output. It never
repairs the package or substitutes an uncommitted working-tree diff.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "pathreview-unit4"
SKILL = Path.home() / ".claude/skills/pr-precheck"
CODEX = "/home/wazimmerman/.local/share/mise/installs/codex/0.160.0/bin/codex"

scope = (SKILL / "scope.md").read_text()
if "- Repo: `codepath/pathreview-ai301-fa26-s1`" not in scope:
    raise SystemExit("Scope is not the authorized Path Review target")


def capture(args):
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"{args!r} exited {p.returncode}: {p.stderr}")
    return p.stdout


commands = [
    ["git", "rev-parse", "main"],
    ["git", "rev-parse", "HEAD"],
    ["git", "branch", "--show-current"],
    ["git", "remote", "-v"],
    ["git", "status", "--short"],
    ["git", "log", "main..HEAD", "--oneline"],
    ["git", "diff", "main...HEAD"],
]
ledger = [{"command": c, "stdout": capture(c), "exit": 0} for c in commands]
stamp = datetime.now(timezone.utc).isoformat()
tag = sys.argv[1] if len(sys.argv) > 1 else "pre-open"
branch = capture(["git", "branch", "--show-current"]).strip()
item = ((HERE / "pr-url.txt").read_text().strip() if (HERE / "pr-url.txt").exists()
        else "https://github.com/codepath/pathreview-ai301-fa26-s1/compare/main...wazimmerman:" + branch)
parts = [
    "Run the installed pr-precheck skill in LIVE MODE on this one actual "
    "candidate for codepath/pathreview-ai301-fa26-s1#69. Item: " + item + ". The following source "
    "files and git commands were actually read by the collector at " + stamp + ". "
    "Use the complete captured live inputs below; do not fetch external context "
    "or invent human review, test runs, or CI status. The target is the upstream "
    "main branch; the source is William's fork branch. Apply every check and end "
    "with the exact fenced JSON verdict. Identify any missing evidence honestly."
]
for name in ["scope.md", "voice-guide.md", "CONTRACT.md", "SKILL.md", "rubric.md", "procedure.md", "references/evidence-guide.md"]:
    parts.append(f"\n# Installed component: {SKILL / name}\n\n" + (SKILL / name).read_text())
for name in ["plan.md", "pr_draft.md", "test_evidence.md"]:
    parts.append(f"\n# Named live input: {HERE / name}\n\n" + (HERE / name).read_text())
for name in [".github/PULL_REQUEST_TEMPLATE.md", "docs/CONTRIBUTING.md", ".github/workflows/ci.yml"]:
    parts.append(f"\n# Repository source: {ROOT / name}\n\n" + (ROOT / name).read_text())
parts.append("\n# Actual committed diff and state\n\n" + json.dumps(ledger, indent=2))
for name in ["issue-69.json", "issue-69-comments.json"]:
    parts.append(f"\n# Live GitHub source captured with gh api: {name}\n\n" + (HERE.parent / name).read_text())
if (HERE / "ci-status.json").exists():
    parts.append("\n# Actual PR checks captured from GitHub\n\n" + (HERE / "ci-status.json").read_text())
prompt = "\n".join(parts)
(HERE / f"live-precheck-{tag}.prompt.txt").write_text(prompt)
(HERE / f"live-precheck-{tag}.sources.json").write_text(json.dumps({"captured_at": stamp, "commands": ledger}, indent=2))
env = os.environ.copy()
for key in ["OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY"]:
    env.pop(key, None)
env["RUST_LOG"] = "off"
cmd = [CODEX, "exec", "--ignore-user-config", "--ephemeral", "--model", "gpt-6.1-sol",
       "--sandbox", "read-only", "--disable", "shell_tool", "--disable", "multi_agent",
       "--disable", "apps", "--disable", "plugins", "--disable", "browser_use",
       "--disable", "computer_use", "--disable", "image_generation", "--disable", "tool_search",
       "--config", 'web_search="disabled"', "--config", 'model_reasoning_effort="medium"',
       "--output-last-message", str(HERE / f"live-precheck-{tag}.txt"), "-"]
p = subprocess.run(cmd, input=prompt, cwd=ROOT, env=env, capture_output=True, text=True)
(HERE / f"live-precheck-{tag}.stdout.txt").write_text(p.stdout)
(HERE / f"live-precheck-{tag}.stderr.txt").write_text(p.stderr)
print(f"Codex live precheck exit: {p.returncode}")
print(p.stdout if p.returncode == 0 else p.stderr[-1500:])
raise SystemExit(p.returncode)
