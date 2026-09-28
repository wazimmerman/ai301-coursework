# Unit 1 — Issue Selection

Path: `beat-1-sandbox/unit-1/selection.md`

## Selected issue

**Issue link**

https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69

**Verdict output**

## Evidence summary

**Repo-level (shared across all three)**
- Not archived, pushed 2026‑09‑16, human-authored commits by Andrew Burke (`Aburke225`) as recently as 2026‑09‑16 — well within the 180/365‑day windows. → **Maintainer activity: pass, Repository in use: pass** for all three.
- `docs/CONTRIBUTING.md` is silent on AI-assisted contributions (no AI policy file, no ban language). → **AI contribution policy: pass** for all three.

**#69 — Output parser crashes on a top-level JSON array fallback**
- Bounded: single AttributeError, named files/test, explicit "2–4 hours" estimate → pass
- Available: no assignee, no linked PR; only student claim/repro/plan comments (ignored per house rule) → pass
- Fit: isolated Python fix in `output_parser.py`, existing xfail test, explicit few-hour estimate → strong pass
- **Verdict: accept**

**#60 — Faithfulness checker crashes on `text: None`**
- Bounded: single TypeError, clear repro, named test → pass
- Available: **open PR #74** ("Closes #60", state OPEN, unmerged) is an active implementation claim per the evidence guide ("an open one is an active claim") — this is a PR, not a claim comment, so the Path Review house rule (which only exempts classmates' *claim comments*) does not rescue it → **fail**
- **Verdict: reject**

**#56 — Structural chunker drops headingless documents**
- Bounded: single observable bug, root cause already traced to two conditions in `_extract_sections()`, named test; fix strategy (single block vs. fallback) is left open by design, not by unresolved debate → pass
- Available: no assignee, `closedByPullRequestsReferences` empty; only student claim/repro comments (ignored) → pass
- Fit: isolated Python fix, focused xfail test, but no explicit effort estimate and touches sub-chunking interaction (slightly more open-ended than #69) → pass, ranks below #69
- **Verdict: accept**

**Ranking rationale:** #69 fits the profile best — it has an explicit "2–4 hours" estimate and the fix is a mechanical `isinstance` guard at two call sites. #56 is also a good fit (isolated Python file, existing focused test) but requires picking a fallback strategy and interacts with the sub-chunking token-limit path, so it's a bit less bounded than #69. #60 is rejected outright on availability.

```json
[
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69",
    "checks": [
      {"name": "Maintainer activity", "grade": "pass", "evidence": "Human commit by Andrew Burke (Aburke225) on 2026-09-16, 11 days before today."},
      {"name": "Repository in use", "grade": "pass", "evidence": "Repo not archived; pushed_at 2026-09-16, open_issues_count 76."},
      {"name": "Bounded contribution", "grade": "pass", "evidence": "Single AttributeError on .items() call, files and test named, 'Estimated effort: 2-4 hours' in the issue body."},
      {"name": "Available to take", "grade": "pass", "evidence": "assignees: [], no closedByPullRequestsReferences; only student claim/repro/plan comments, which the Path Review house rule ignores."},
      {"name": "AI contribution policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md contains no mention of AI-generated contributions; silence passes."},
      {"name": "Personal fit", "grade": "pass", "evidence": "Isolated Python fix in rag/generator/output_parser.py with an existing xfail test and an explicit 2-4 hour estimate matching the fit profile."}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/56",
    "checks": [
      {"name": "Maintainer activity", "grade": "pass", "evidence": "Human commit by Andrew Burke (Aburke225) on 2026-09-16, within 180 days."},
      {"name": "Repository in use", "grade": "pass", "evidence": "Repo not archived; pushed_at 2026-09-16."},
      {"name": "Bounded contribution", "grade": "pass", "evidence": "Single observable bug (chunk() returns [] for headingless docs); root cause already traced to _extract_sections() lines 120/124 by a commenter, named xfail test test_document_with_no_headings."},
      {"name": "Available to take", "grade": "pass", "evidence": "assignees: [], closedByPullRequestsReferences: []; only student claim/repro comments, ignored per house rule."},
      {"name": "AI contribution policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md silent on AI use."},
      {"name": "Personal fit", "grade": "pass", "evidence": "Isolated Python fix in ingestion/chunking/structural_chunker.py with a focused xfail test, though the fallback strategy and SECTION_TOKEN_LIMIT interaction leave slightly more open-endedness than #69."}
    ],
    "verdict": "accept"
  },
  {
    "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/60",
    "checks": [
      {"name": "Maintainer activity", "grade": "pass", "evidence": "Human commit by Andrew Burke (Aburke225) on 2026-09-16, within 180 days."},
      {"name": "Repository in use", "grade": "pass", "evidence": "Repo not archived; pushed_at 2026-09-16."},
      {"name": "Bounded contribution", "grade": "pass", "evidence": "Single TypeError on '.join()' with None text, clear repro snippet and named test test_none_context_chunk_text."},
      {"name": "Available to take", "grade": "fail", "evidence": "closedByPullRequestsReferences shows PR #74 ('Closes #60'), state OPEN and unmerged — an active implementation PR, not merely a classmate claim comment, so the house rule does not exempt it."},
      {"name": "AI contribution policy", "grade": "pass", "evidence": "docs/CONTRIBUTING.md silent on AI use."},
      {"name": "Personal fit", "grade": "pass", "evidence": "Would otherwise be an isolated Python fix in rag/evaluator/faithfulness_checker.py with a focused test, but does not affect the reject verdict."}
    ],
    "verdict": "reject"
  }
]
```

## Eval iterations

**Run history**

1. First full run, original scope check: `agreement: 15/20 scored items  (bar: 18/20: below the bar)`.
2. After revising the scope check, targeted `--only issue-01,issue-04,issue-05,issue-10,issue-15,issue-19,issue-20`: `agreement: 7/7 scored items`. This partial run tested the five disagreements plus two rejection canaries; it was not saved as the submission run.
3. Confirming full run, matching the committed `eval-run.txt`: `agreement: 19/20 scored items  (bar: 18/20: PASS)`; its category line is `categories: claimed 4/4  clear-accept 8/8  dead-repo 3/3  policy 1/1  scope 3/4`.

**Issue analysis**

`issue-15` is the one remaining disagreement. The final rubric's verdict was `accept`; the instructor gold label is `reject`. The snapshot says `this issue: assignees: none; linked PRs: zulip/zulip#20840 (closed); zulip/zulip#23123 (closed)` and `Comments (97 total, first 40 shown)`. The skill read the proposed `command`/`text` split and an early maintainer response as a checkable, settled feature, and treated the two closed PRs as inactive claims. The gold label instead treats the long design discussion and abandoned attempts as evidence that the present approach is still unresolved. The rubric now warns about that pattern, but this run shows its threshold can still miss it.

**Check rationale**

Current `rubric.md` row, quoted exactly:

```markdown
| Bounded contribution | Eval: issue body and every shown comment, including linked-attempt history. Live: issue body and full thread, including maintainer clarification. | Pass a single observable bug, a coherent docs workflow, or one feature family whose result can be checked, even when it spans several files, includes optional tactics, or is tersely described by a maintainer as a good first issue. Fail an explicit umbrella/tracker, a support question, or an unsettled design discussion with no current maintainer decision. Also fail when years of debate and multiple abandoned PRs leave the present approach unresolved, or when a new feature depends on an unspecified product choice or asset (such as which branding/logo to ship). A short bug report, missing repro steps, or multiple suggested causes alone do not fail. | required |
```

The first full run rejected `issue-01`, `issue-04`, and `issue-19` because it equated multiple touched files, terse examples, or several suggested causes with unbounded work. I changed the condition to look for one observable outcome or coherent feature family, while keeping explicit umbrella issues, unresolved design, and unspecified product decisions as failures. That made these three accepts agree with the gold labels and kept `issue-20` rejected.

**Trade-offs**

The broader acceptance of coherent work can admit an old issue whose proposed outcome looks concrete while its thread still lacks a current decision: `issue-15` is the observed miss. The targeted canaries `issue-05` and `issue-10` remained `reject`, so the revision did not erase the obvious umbrella/tracking boundary in those cases.

## Selection rationale

**Selection rationale**

1. I chose #69 because I am comfortable with Python, its parser failure has a direct trigger and an existing focused expected-failure test, and the issue estimates 2–4 hours—within the time I have for these units.
2. The live verdict correctly identified an active repository, a specific crash, an unassigned issue with no open linked PR, and a good fit for my Python workflow. The rubric cannot decide which accepted bug I would find most useful to learn from; I prefer #69's clear input-to-traceback path over #56's more open-ended fallback behavior.
3. Other classmates have commented on #69. The Path Review house rule allows a separate claim, but I still need to write a specific claim in my own voice before investigating and then post my own reproduction evidence rather than relying on theirs.
