# Plan: issue #69 JSON array fallback

Issue: https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69
Author: wazimmerman. Fork: https://github.com/wazimmerman/pathreview-ai301-fa26-s1
Branch: `fix/69-json-array-fallback`, based on `f89c06fc3ff292df2a04a39ac51319d32a76b779`.

## Diagnosis and Unit 2 evidence

My own posted Unit 2 reproduction is https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-5863094246. Its recorded environment was CachyOS Linux, Python 3.11.14, uv 0.12.13; this build checkout uses Python 3.11.15. The following is quoted from that report, not a classmate's result:

> **Reproduced issue #69** on my fork at `f89c06fc3ff292df2a04a39ac51319d32a76b779` (`main`, clean worktree). A top-level JSON array reaches `_parse_json_output`, where `.items()` is called on a list. This matches the issue's reported `AttributeError`.

The actual quoted Unit 2 triggering command was:

```bash
.venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps(["First feedback item", "Second feedback item"])
print(parse_review_output(raw))
PYCODE
```

Its captured traceback included:

```text
  File "/home/wazimmerman/git/codepath/ai301/pathreview/rag/generator/output_parser.py", line 48, in parse_review_output
    return _parse_json_output(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wazimmerman/git/codepath/ai301/pathreview/rag/generator/output_parser.py", line 68, in _parse_json_output
    for key, value in data.items():
                      ^^^^^^^^^^
AttributeError: 'list' object has no attribute 'items'
```

The report's object control `json.dumps({"summary": "Works"})` returned:

```text
[FeedbackSection(section_name='summary', content='Works', confidence=0.85, suggestions=[])]
```

The same report forced the existing expected-failure test to execute:

```bash
.venv/bin/python -m pytest tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback --runxfail -q --tb=short
```

```text
E   AttributeError: 'list' object has no attribute 'items'
FAILED tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback
1 failed in 0.08s
```

The fresh pre-build run in `evidence/before.txt` independently confirms that raw arrays fail through line 48 and fenced arrays fail through line 41 into `.items()` at line 68. The object control still succeeds. Independently checked raw and fenced `"just text"`, `42`, `null`, and `true` fail with the corresponding str/int/NoneType/bool AttributeErrors. Those scalar observations are additional current evidence, not claims from the historical report.

Both `json.loads` sites accept any JSON top-level type and pass it to a helper that requires a dict. `JSONDecodeError` handling cannot catch this valid-JSON type mismatch. The cause is the missing object-type boundary at those two call sites, and the issue explicitly requests the fallback path.

## Scope and non-goals

One bounded change: only parsed dictionaries reach `_parse_json_output`; every other valid JSON top-level type follows the existing plaintext fallback with the entire original raw input preserved. Apply this at both the fenced and raw entry paths.

Files: `rag/generator/output_parser.py` (`parse_review_output` only) and `tests/unit/test_output_parser.py` (the H-02 test and targeted raw/fenced regression cases).

Non-goals: no one-section-per-array-item mapping, no helper redesign, no changes to the deliberate `sections = []  # noqa: F841` seeded material, no review-generator or unrelated defect cleanup, no credentials or LLM API calls. Plan and comment drafts remain untracked in the fix branch and are copied into coursework evidence, not source commits.

## Approach

1. At each `json.loads` result, return `_parse_json_output(data)` only when `isinstance(data, dict)` holds. Let other types reach the existing `_parse_plaintext_output(raw)` return. Preserve malformed-JSON handling and structured-object behavior; do not catch broad exceptions.
2. Remove the strict H-02 `xfail` marker and strengthen the raw-array test to require one `general_feedback` section containing the exact raw string at confidence 0.7 with no suggestions. Add fenced-array coverage that checks the entire original fence is preserved.
3. Add parameterized raw/fenced scalar and empty-array regressions from the independently verified type boundary, and exact raw/fenced object controls. These exercise the same dict contract, not a second feature.
4. Inspect every source diff, rerun the actual Unit 2 command and focused test, then the parser file and repository Python checks. Save literal commands, output, and exit codes. Push only these two source/test files to my fork branch for the Unit 4 PR; do not merge.

## Test plan and expected observations

- Repeat the quoted Unit 2 raw-array command: it must exit 0 and return `[FeedbackSection(section_name='general_feedback', content='["First feedback item", "Second feedback item"]', confidence=0.7, suggestions=[])]`, replacing the observed exception.
- Repeat with the same array inside a JSON fence: return one fallback section with the full input including fences, exit 0. The fenced path must not retain the crash.
- Repeat raw/fenced strings, numbers, null, booleans and empty arrays: one exact-content fallback section each. Keep both raw/fenced object controls returning `summary`, `Works`, confidence 0.85, and no suggestions; `{}` should still produce an empty list.
- Run `.venv/bin/python -m pytest tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback --runxfail -q --tb=short`, then `.venv/bin/python -m pytest tests/unit/test_output_parser.py -q`: the former passes without any xfail marker and the complete parser tests pass.
- Run `make check` and `make test-unit` per `docs/CONTRIBUTING.md`. Inspect any formatting edits so unrelated files cannot enter the fix. If dependency or baseline findings block a broad check, record actual output and compare the unchanged baseline before deciding on scope; do not claim green. Frontend and integration CI readiness are coordinated in Unit 4.

## Risks and unknowns

Array items do not name feedback sections, and the issue asks for the fallback. Preserving the original raw text avoids inventing array semantics. A non-object fenced value proceeds through the existing raw-JSON attempt before plaintext; the second decode may log its existing warning, which is acceptable and does not change the result. Top-level objects must retain their existing parsing semantics. Other seeded defects remain outside this fix.

The plan-check evaluation uses GPT-6.1 Sol through the Codex CLI and existing ChatGPT login. The official harness is Sonnet-only. A separately named, disclosed provider adapter preserves its prompts, packages, scoring, gold labels and generated fingerprints; course equivalence is unconfirmed. No official Sonnet result or human review is claimed. OpenAI Codex assisted the plan, grading, implementation and evidence preparation; every reported runtime result comes from an actual command.

## Deviations

No implementation deviation: the posted plan held. Both JSON decoding paths now pass only dictionaries to the structured helper, and all other top-level values reach the existing plaintext fallback. Only the two planned source/test files changed. The H-02 marker was removed; regression coverage includes raw/fenced arrays, empty arrays, strings, numbers, null, booleans, and raw/fenced populated/empty object controls as planned.

The new and strengthened regression tests were run before adding the guards: 12 failed and 22 passed. After adding the guards, the complete parser file passed all 34 tests. The repeated Unit 2 direct command and forced focused test now pass; exact captures are in `evidence/after.txt`. Repository checks and their actual outcomes are recorded in `evidence/checks.txt`. Those checks use `LLM_PROVIDER=mock` and an existing local tiktoken cache, avoiding LLM API calls or a network dependency during the unit run.

The GitHub integration denied the initial comment POST with HTTP 403 and did not post it. After explicit approval of the already authenticated personal GitHub CLI route, the same accepted text was posted and verified as `wazimmerman` at https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-6404816771, created `2026-10-25T23:21:14Z`, before source implementation. No credential or permission changes were made. This publication transport change did not change the checked plan's content or implementation scope.
