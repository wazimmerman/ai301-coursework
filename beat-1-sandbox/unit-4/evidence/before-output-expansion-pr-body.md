## Summary

A top-level JSON array reached `_parse_json_output`, which called `.items()` on a list and raised `AttributeError`. Both raw and fenced JSON paths now pass only dictionaries to the structured parser. Arrays and other non-object JSON values use the existing plaintext fallback, preserving the complete original input as one `general_feedback` section.

## Issue

Closes #69

## Changes

- Guard both `json.loads` results with `isinstance(data, dict)` before calling `_parse_json_output`.
- Remove the strict H-02 xfail and assert the exact raw-array fallback, including content, confidence, and suggestions.
- Cover fenced arrays, empty arrays, strings, numbers, null, booleans, and raw/fenced populated and empty object controls.

## Testing

- [x] **CI is green on this PR (all five jobs)** — lint, typecheck, test-unit, test-integration, and frontend succeeded on this PR; the additional RAG eval job also succeeded. [CI run](https://github.com/codepath/pathreview-ai301-fa26-s1/actions/runs/40245136994), [RAG eval run](https://github.com/codepath/pathreview-ai301-fa26-s1/actions/runs/40245136997).
- [x] Unit tests pass (`make test-unit`) — 391 passed, 52 xfailed, exit 0.
- [ ] Integration tests pass (`make test-integration`) — collected 0 tests; pytest exit 5, make exit 2. No integration tests are claimed to have passed. The CI integration job succeeded under upstream's explicit exit-5 allowance for the currently empty suite.
- [x] Linter passes (`make lint`) — all checks passed, exit 0.
- [x] Type checker passes (`make typecheck`) — no issues in 76 source files, exit 0.
- [x] New/updated tests cover the changes — 34 parser tests pass; the focused array test also passes with `--runxfail`.
- [x] If this fixes a seeded bug: removed its `@pytest.mark.xfail` marker (and any matching suppression in `pyproject.toml`) — H-02 marker removed; no matching issue #69 suppression applies.

The original raw-array command raised `.items()` `AttributeError` on `f89c06f`. On `639f490`, it returns one `FeedbackSection('general_feedback', original_raw_text, 0.7, [])`; the `{"summary": "Works"}` control keeps its structured result at confidence 0.85. `black --check .` passes with 110 files unchanged. Frontend `npm test -- --run` passes all 18 tests. Backend checks used Python 3.11.15, `LLM_PROVIDER=mock`, and a local cache of public tiktoken data; no LLM API call was needed.

## Screenshots / Demo

N/A: this is a parser-only change with no UI change. The before/after parser output and exact-value regression assertions demonstrate the behavior.

## Notes for Reviewers

This implements the [plan posted before implementation](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-6404816771), based on [my Unit 2 reproduction](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-5863094246). Only the planned parser function and test file changed. Object parsing, malformed-JSON handling, the structured helper, and unrelated seeded material retain their existing behavior. A non-object JSON fence still reaches the existing raw-JSON attempt and may emit its existing warning before plaintext fallback.

OpenAI Codex assisted the investigation, plan, implementation, tests, diff inspection, and this PR description. The plan-check and pr-precheck evaluations use GPT-6.1 Sol through Codex CLI 0.160.0 with existing ChatGPT authentication. The course harness is pinned to Claude Sonnet; the separately disclosed Codex provider adaptation preserves its prompts, packages, scoring, and fingerprints, but course equivalence is unconfirmed. No Claude run or human review is claimed. Full recorded evidence and evaluation provenance are in the [coursework repository](https://github.com/wazimmerman/ai301-coursework).
