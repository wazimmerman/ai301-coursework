# Unit 3 — Plan and Build

Path: `beat-1-sandbox/unit-3/plan-and-implement.md`

## Posted upstream

**GitHub username**

wazimmerman

**Plan comment**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-6404816771

The following is the exact posted text, preserved in `evidence/comment.md` and verified against the returned GitHub comment body. It was posted before source implementation.

My reproduction for issue #69 is [above](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-5863094246): the raw JSON array reached `_parse_json_output` and failed at `data.items()`, while `{"summary": "Works"}` returned a structured section. I reran that command on my fork's `f89c06f` baseline today with Python 3.11.15 and confirmed the same failure. The fenced-array path also crashes; independently checked strings, numbers, null and booleans reach the same type mismatch in both paths.

The cause is that both `json.loads` call sites pass any parsed value into a helper that requires a dict. My plan is to guard both calls with `isinstance(data, dict)` and let other top-level types reach the existing plaintext fallback, preserving the full original input. This follows the fallback requested by the issue and avoids inventing section names for array elements.

The change is limited to `parse_review_output` in `rag/generator/output_parser.py` and focused tests in `tests/unit/test_output_parser.py`, on my fork's `fix/69-json-array-fallback` branch. I'll remove the strict H-02 `xfail`, assert the exact `general_feedback` fallback for raw and fenced arrays, cover empty arrays and the independently reproduced scalars, and retain raw/fenced object controls. The direct array reproduction should return one section containing the original text at confidence 0.7 instead of raising; objects should retain their structured result. I'll rerun the Unit 2 command and focused test, the complete parser test file, `make check`, and `make test-unit`, and report the actual results.

Other students' plans do not replace my own evidence or tests. This work stays on my fork; `_parse_json_output`, the deliberately retained accumulator line, the review generator and other seeded defects are out of scope. The main risk is changing object behavior while fixing the boundary, so the object controls are explicit. If implementation changes this plan, I'll record the reason and recheck it before posting an update.

OpenAI Codex helped inspect the code, draft this plan and evaluate it with GPT-6.1 Sol using existing ChatGPT authentication. The course's official evaluator is pinned to Sonnet; my disclosed Codex provider adaptation is not an official Sonnet run, and course equivalence is unconfirmed. I will use Codex for implementation and report only captured command results; I am not claiming human review or maintainer approval.


## Your branch

**Branch**

`fix/69-json-array-fallback` on https://github.com/wazimmerman/pathreview-ai301-fa26-s1/tree/fix/69-json-array-fallback

Implementation commit: https://github.com/wazimmerman/pathreview-ai301-fa26-s1/commit/639f49027473664f14bbf70512968dbc5b1f0629

The source commit contains only `rag/generator/output_parser.py` and `tests/unit/test_output_parser.py`. The untracked plan and comment drafts were preserved locally for Unit 4; their submission copies live here. No merge was performed.

**Evidence**

The commands below ran against the real parser module. The before state is the unchanged `f89c06f` baseline; the after state includes the focused fix. Full stdout/stderr and exit codes are pasted verbatim. Logs reflect the actual test environment and are not synthetic stand-ins.

Before:

```text
cwd: /home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3

$ git rev-parse HEAD
f89c06fc3ff292df2a04a39ac51319d32a76b779
[exit 0]

$ git status --short
[exit 0]

$ .venv/bin/python --version
Python 3.11.15
[exit 0]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps(["First feedback item", "Second feedback item"])
print(parse_review_output(raw))
PYCODE
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3/rag/generator/output_parser.py", line 48, in parse_review_output
    return _parse_json_output(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3/rag/generator/output_parser.py", line 68, in _parse_json_output
    for key, value in data.items():
                      ^^^^^^^^^^
AttributeError: 'list' object has no attribute 'items'
[exit 1]

$ .venv/bin/python - <<'PYCODE'
from rag.generator.output_parser import parse_review_output
raw = '```json\n["First feedback item", "Second feedback item"]\n```'
print(parse_review_output(raw))
PYCODE
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3/rag/generator/output_parser.py", line 41, in parse_review_output
    return _parse_json_output(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3/rag/generator/output_parser.py", line 68, in _parse_json_output
    for key, value in data.items():
                      ^^^^^^^^^^
AttributeError: 'list' object has no attribute 'items'
[exit 1]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps({"summary": "Works"})
print(parse_review_output(raw))
PYCODE
2026-10-25 17:09:36 [info     ] json_output_parsed             section_count=1
[FeedbackSection(section_name='summary', content='Works', confidence=0.85, suggestions=[])]
[exit 0]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
for value in ["just text", 42, None, True]:
    for fenced in [False, True]:
        raw = json.dumps(value)
        if fenced:
            raw = "```json\n" + raw + "\n```"
        try:
            result = parse_review_output(raw)
            print(repr(value), "fenced=" + str(fenced), repr(result))
        except Exception as exc:
            print(repr(value), "fenced=" + str(fenced), type(exc).__name__ + ":", str(exc))
PYCODE
'just text' fenced=False AttributeError: 'str' object has no attribute 'items'
'just text' fenced=True AttributeError: 'str' object has no attribute 'items'
42 fenced=False AttributeError: 'int' object has no attribute 'items'
42 fenced=True AttributeError: 'int' object has no attribute 'items'
None fenced=False AttributeError: 'NoneType' object has no attribute 'items'
None fenced=True AttributeError: 'NoneType' object has no attribute 'items'
True fenced=False AttributeError: 'bool' object has no attribute 'items'
True fenced=True AttributeError: 'bool' object has no attribute 'items'
[exit 0]

$ .venv/bin/python -m pytest tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback --runxfail -q --tb=short
F                                                                        [100%]
=================================== FAILURES ===================================
__________________ TestOutputParser.test_json_array_fallback ___________________
tests/unit/test_output_parser.py:149: in test_json_array_fallback
    result = parse_review_output(raw_output)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
rag/generator/output_parser.py:48: in parse_review_output
    return _parse_json_output(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
rag/generator/output_parser.py:68: in _parse_json_output
    for key, value in data.items():
                      ^^^^^^^^^^
E   AttributeError: 'list' object has no attribute 'items'
=========================== short test summary info ============================
FAILED tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback
1 failed in 0.33s
[exit 1]
```

After:

```text
cwd: /home/wazimmerman/Documents/Codex/2026-10-25/task/pathreview-unit3

$ git rev-parse HEAD
f89c06fc3ff292df2a04a39ac51319d32a76b779
[exit 0]

$ git status --short
 M rag/generator/output_parser.py
 M tests/unit/test_output_parser.py
?? comment.md
?? plan.md
[exit 0]

$ .venv/bin/python --version
Python 3.11.15
[exit 0]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps(["First feedback item", "Second feedback item"])
print(parse_review_output(raw))
PYCODE
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=47
[FeedbackSection(section_name='general_feedback', content='["First feedback item", "Second feedback item"]', confidence=0.7, suggestions=[])]
[exit 0]

$ .venv/bin/python - <<'PYCODE'
from rag.generator.output_parser import parse_review_output
raw = '```json\n["First feedback item", "Second feedback item"]\n```'
print(parse_review_output(raw))
PYCODE
2026-10-25 17:22:02 [warning  ] raw_json_parsing_failed
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=59
[FeedbackSection(section_name='general_feedback', content='```json\n["First feedback item", "Second feedback item"]\n```', confidence=0.7, suggestions=[])]
[exit 0]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps({"summary": "Works"})
print(parse_review_output(raw))
PYCODE
2026-10-25 17:22:02 [info     ] json_output_parsed             section_count=1
[FeedbackSection(section_name='summary', content='Works', confidence=0.85, suggestions=[])]
[exit 0]

$ .venv/bin/python - <<'PYCODE'
import json
from rag.generator.output_parser import parse_review_output
for value in ["just text", 42, None, True]:
    for fenced in [False, True]:
        raw = json.dumps(value)
        if fenced:
            raw = "```json\n" + raw + "\n```"
        try:
            result = parse_review_output(raw)
            print(repr(value), "fenced=" + str(fenced), repr(result))
        except Exception as exc:
            print(repr(value), "fenced=" + str(fenced), type(exc).__name__ + ":", str(exc))
PYCODE
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=11
'just text' fenced=False [FeedbackSection(section_name='general_feedback', content='"just text"', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [warning  ] raw_json_parsing_failed
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=23
'just text' fenced=True [FeedbackSection(section_name='general_feedback', content='```json\n"just text"\n```', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=2
42 fenced=False [FeedbackSection(section_name='general_feedback', content='42', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [warning  ] raw_json_parsing_failed
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=14
42 fenced=True [FeedbackSection(section_name='general_feedback', content='```json\n42\n```', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=4
None fenced=False [FeedbackSection(section_name='general_feedback', content='null', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [warning  ] raw_json_parsing_failed
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=16
None fenced=True [FeedbackSection(section_name='general_feedback', content='```json\nnull\n```', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=4
True fenced=False [FeedbackSection(section_name='general_feedback', content='true', confidence=0.7, suggestions=[])]
2026-10-25 17:22:02 [warning  ] raw_json_parsing_failed
2026-10-25 17:22:02 [info     ] plaintext_output_parsed        content_length=16
True fenced=True [FeedbackSection(section_name='general_feedback', content='```json\ntrue\n```', confidence=0.7, suggestions=[])]
[exit 0]

$ .venv/bin/python -m pytest tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback --runxfail -q --tb=short
.                                                                        [100%]
1 passed in 0.09s
[exit 0]
```

The parser file passed all **34 tests**. `make check` exited 0; `make test-unit` exited 0 with **391 passed, 52 xfailed**. These checks ran with `LLM_PROVIDER=mock` and `TIKTOKEN_CACHE_DIR=/tmp/ai301-unit4-tiktoken-cache`. The full required-check transcript is in [evidence/checks.txt](evidence/checks.txt). The as-built plan was regraded in [evidence/live-asbuilt.md](evidence/live-asbuilt.md) with per-check JSON in the adjacent file. Its verdict is `accept`; this is actual Codex skill output, not human review.

## Eval iterations

**Run history**

The official starter is pinned to `claude -p --model sonnet` with no provider flag. No Claude run or official Sonnet score is claimed. The user explicitly selected Codex. The separately named provider adapter preserves the official prompts, packages, gold labels, scoring and generated fingerprints, and its generated run header names the actual backend/model. CodePath equivalence remains unconfirmed. See [evidence/PROVENANCE.md](evidence/PROVENANCE.md) and [evidence/harness-adaptation.diff](evidence/harness-adaptation.diff).

Infrastructure starts through a stale PATH wrapper (Codex 0.128.0) failed before completion and were stopped. They produced no complete agreement score and no saved full-run file. A current installed Codex 0.160.0 authentication probe succeeded; grading then used that binary through existing ChatGPT login, with API-key environment variables removed. No new credentials or paid API usage occurred.

1. Complete full run, `gpt-6.1-sol`, medium reasoning, Codex CLI 0.160.0: **18/20**. Categories: clear-accept 5/7; scope-creep 4/4; thread-convention 2/2; unbuildable 3/3; wrong-cause 4/4. There were no errored packages. Every category has at least one agreement. This was the only completed scored run and is the final full run; the authored components were not revised after it. Its generated file was copied byte-for-byte into `eval-run.txt`, without editing.

Exact final agreement line:

```text
agreement: 18/20 scored items  (bar: 18/20: PASS)
```

This is the adapter's genuine measured agreement against the official labels, not a claim that the Sonnet-validated course bar transfers to Codex. No partial revision runs or canaries were needed because the first complete measurement met 18/20 and the category floor. [evidence/eval-results.json](evidence/eval-results.json) retains every check for all 20 packages.

**Package analysis**

**pkg-03** was `reject`, while gold was `accept`. The package says, exactly, "gzip, bzip2, xz, zstd, lz4, and brotli all accept `--` as end-of-options (GNU-style parsing); I have verified gzip, xz, and zstd locally and will verify the remaining three against their manpages before the PR". The honesty check read the universal claim as stronger than its stated verification, although the plan also commits to checking the remaining tools. That conservative reading created a false negative relative to gold. This is analysis after grading; gold labels were not supplied to the model. All 20 actual verdicts and deciding evidence remain in [evidence/package-analysis.md](evidence/package-analysis.md) and the full results JSON.

**Check rationale**

This is one complete check quoted exactly from the uploaded `tools/plan-check/rubric.md`:

> | Observable regression proof | Plan's test steps and expected results compared with the accepted repro's triggering inputs, environment, failure, and controls | At least one named or clearly referenced test replays the reproduced failure and states the observable result that distinguishes the fix from the broken behavior. Preserve relevant controls or adjacent shared paths when identified. A broad suite alone, or merely saying tests pass or it works, does not prove the regression. | required |

The check requires an observable discriminator tied to the accepted reproduction. The fallback design rejected counting headings or treating a suite-only statement as proof: calib-04 says "Run the full test suite (`cargo test --workspace`) and make sure nothing regresses," which does not replay the two-working-directory failure. Calib-01's "at step 3 the color must flip without leaving the view" does name the observable result. That distinction informed the check before the full run; no later wording revision was made.

**Trade-offs**

The honesty rule favors holding plans whose causal certainty exceeds their shown evidence. It accepts the cost of false negatives on pkg-03 and pkg-14, whose gold labels favor their explicit verification paths and bounded proposals. Relaxing it could improve those two labels while weakening protection against wrong-cause plans; this submission did not loosen the rule merely to fit those labels. The unchanged full run still agreed on all four wrong-cause, all four scope-creep, all three unbuildable and both thread-convention packages, and five of seven clear accepts. That complete measured run is the evidence for retaining this version, not a claim that every future plan will be graded correctly.

The group worksheet's authored rubric and procedure fields were blank templates, so these components use the authorized fallback transparently. The Unit 2 voice guide was carried over unchanged. OpenAI Codex assisted authoring, live grading, implementation, tests and write-up assembly. There is no invented personal reflection, human review or maintainer approval.
