# Unit 4 — Test and Submit

Path: `beat-1-sandbox/unit-4/pull-request.md`

## Your pull request

**Pull request**

https://github.com/codepath/pathreview-ai301-fa26-s1/pull/241

Opened as personal GitHub account `wazimmerman` against `codepath/pathreview-ai301-fa26-s1:main`. It is an open pull request, not a merge. The posted pre-build plan is https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69#issuecomment-6404816771.

**Branch**

`fix/69-json-array-fallback` on William's fork, `wazimmerman/pathreview-ai301-fa26-s1`.

Remote source commit: https://github.com/wazimmerman/pathreview-ai301-fa26-s1/commit/639f49027473664f14bbf70512968dbc5b1f0629

Only `rag/generator/output_parser.py` and `tests/unit/test_output_parser.py` changed. There was no implementation deviation from the posted plan. The branch's complete committed `git diff main...HEAD`, plan, PR draft, and actual command outputs were graded by the installed `pr-precheck` skill in live mode before opening: **accept**, all six checks pass. No voice-guide violations were reported. The first live report noted that the unchanged staff contract was not inlined; that contract had been read during construction and is included in the later live run.

Independent final-branch checks at that exact commit: 34 parser tests; 391 unit tests passed, 52 expected failures; lint; mypy across 76 files; black check (110 unchanged); 18 frontend tests. The original raw-array call now produces one exact-content plaintext fallback section; the object control is unchanged. Local `make test-integration` collected no tests (pytest exit 5; make exit 2), which is disclosed rather than marked passed. Upstream CI has an explicit empty-suite exit-5 allowance. Full literal commands, stdout, stderr and exits are in [evidence/test_evidence.md](evidence/test_evidence.md). The PR Testing section itself also pastes the captured before/after commands and outputs, the complete four required check logs in collapsible sections, and the focused/parser/formatter/frontend captures. Those outputs were copied from the original process records; no test rerun or synthesized output was used for the description correction. Earlier baseline setup failure and cached-success logs are separate and preserved; they do not substitute for final branch evidence.

All five required CI jobs passed on the PR, along with the additional RAG eval job: [CI run](https://github.com/codepath/pathreview-ai301-fa26-s1/actions/runs/40245136994), [RAG eval run](https://github.com/codepath/pathreview-ai301-fa26-s1/actions/runs/40245136997). Actual check names, states and links are recorded in [evidence/ci-status.json](evidence/ci-status.json). The PR's CI checkbox was then updated from those observed successful results; the local empty integration suite remains explicitly disclosed. No portal submission, credential change or merge was performed. The final [final live audit of the expanded PR](evidence/live-precheck-post-output-expansion.txt) returned **accept** for PR #241, with all six checks passing and no CI gate pending. Its exact per-check JSON is [preserved here](evidence/live-precheck-post-output-expansion.json). All live runs used the installed evaluated skill unchanged. The final tool saw the individual `make check` components and successful PR CI; Unit 3 separately retains the aggregate `make check` execution in its own evidence.

## Eval iterations

**Run history**

1. Initial three-package startup attempt through PATH CLI 0.128.0: no package verdicts, no score (the script printed `agreement: 0/0 scored items`). GPT-6.1 Sol was rejected by that old CLI. The attempt did not produce eval-run.txt. A GPT-5.3-Codex availability probe also failed; it was not a package evaluation.
2. Smoke after selecting the existing native Codex CLI 0.160.0 with GPT-6.1 Sol: `agreement: 3/3 scored items`. Partial runs do not decide the bar or category floor.
3. First and final full run: `agreement: 19/20 scored items  (bar: 18/20: PASS)`. Category matches: clear-accept 6/7, not-tested 4/4, silent-drift 4/4, standards-wall 2/2, unreviewable 3/3. No rubric revision or further full run followed this measured result.

This is a genuine GPT-6.1 Sol/Codex run with existing ChatGPT authentication, not Claude or Sonnet. The source harness pins Sonnet; the explicit provider adaptation, unchanged original source, and diff are in evaluation/unit-4/. Course equivalence remains unverified. The harness wrote eval-run.txt normally; it was copied byte for byte without editing.

**Package analysis**

Scored package `pkg-16`: the rubric's model execution returned **reject**; the gold label is **accept**. Its failed Plan fidelity evidence was: "The plan promises unchanged start-path tolerance, but shared DoLoadImages now returns an error on total failure without a start-path safeguard in the diff."

The package's plan explicitly says "Deliberately deferred, stated in the plan: the start-time loading path" and the PR restates that limitation. The diff adds an error when `len(succeeded) == 0` in a shared helper, and retains the comment "Partial success stays non-fatal for the multi-node start path." The model took the lack of a shown caller safeguard as scope drift. The gold acceptance instead recognizes the bounded image-load result and disclosed start-path deferral. The frozen package does not include all call sites; the model's inferred side effect is less direct evidence than an observed contradictory hunk. This is a false rejection on the scored set, not a reason to rewrite the gold label. All five remaining checks passed, including the invalid/valid tarball observations and named Go suite result.

**Check rationale**

Exact current rubric check:

```text
| Plan fidelity | Plan context or plan.md scope, exclusions and deviations paired with every changed file/hunk, commits, and candidate title/description | The diff implements the bounded plan in both directions and its claims match the delivered behavior. Any added, deferred, or altered work is explicitly justified in the plan's deviation notes and represented honestly in the description. A disclosed, bounded shortfall can pass; silent extra work, silent omissions, or a false exact-plan/full-coverage claim fails. | required |
```

I kept this rule in its initial form after the 19/20 full run. The real Unit 4 worksheet identified an unplanned `src/language-js/print/property.js` refactor and a false exact-plan claim; that motivates checking both extra and missing work. Its missing all-comments and nested-chain fixtures also motivate reading promised outcomes against real assertions. I rejected a blanket rule that any deferral means reject: the source contract and packages permit an honest bounded shortfall. The explicit deviation sentence preserves that distinction.

**Trade-offs**

The conservative Plan fidelity check caught every silent-drift package (4/4), but its application falsely rejected clear-accept `pkg-16` by inferring an unshown caller consequence. I retained this known limitation and documented the miss instead of tuning to a gold label after reaching the required numerical bar. The final run also matched both standards-wall cases and all three unreviewable cases, so there is measured category coverage rather than an assumption that the check sees them. No check was loosened after the full run, so there was no targeted revise/canary loop or second full run to report. If this rule is loosened later, rerun pkg-16 with agreeing silent-drift and standards-wall canaries before another full run.


Related paths: [eval-run.txt](eval-run.txt), [tools/pr-precheck](../../../tools/pr-precheck), [provider provenance](../../../evaluation/unit-4/README.md), and the captured live evidence in `evidence/`.
