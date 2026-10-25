---
name: pr-precheck
description: Grade a PR package (a candidate pull request read against the plan it claims to implement and the issue that plan belongs to) and decide whether it is ready to submit. Use when checking your own branch, draft PR title, and description before opening the pull request, or when grading an eval package bundle.
---

# pr-precheck: rubric-driven PR grading

## The question

Decide one question about one PR package: is this ready to submit? Read its title, description, commits, diff, and test evidence against the plan it claims to implement and the issue that plan belongs to. Grade the submitted change, including its stated limits; do not redesign the project or grade the author's confidence.

## Inputs and modes

Choose LIVE MODE for an actual candidate and EVAL MODE for one frozen bundle. Never mix the modes or grade multiple packages in one run.

In live mode require named paths to `plan.md` including its deviations, `pr_draft.md` with the first line as the title and the remaining text as the description, and `test_evidence.md` with actual commands, outputs, exits, and code state. Read commits with `git log main..HEAD --oneline` and produce the complete committed branch diff from the working copy with `git diff main...HEAD` (three dots). Check `git status --short` and report uncommitted changes that are absent from the graded diff. Verify the base repository/default branch rather than substituting a working-tree diff. Read the issue body and full thread on the real scoped repository, `.github/PULL_REQUEST_TEMPLATE.md`, and `docs/CONTRIBUTING.md`. Record unavailable sources as missing evidence. A house-chain student supplies the designated house plan and house repro pack in place of the personal plan and reproduction; apply the same checks. Use the candidate PR URL as item when one exists; before opening use the candidate's repository compare URL so the output still identifies the actual PR package.

In eval mode the supplied bundle is the whole world. Read its repo facts, issue and thread, accepted plan context and deviations, candidate title/description/commits/diff, and test evidence. Fetch nothing and read no other files, pages, repository, source issue, gold labels, or prior verdict. Execute every rubric check and the full verdict rule. Ignore scope.md and voice-guide.md entirely.

## The scope seam (live mode only)

Read scope.md before any live package input. Enforce its target repository and house rules; a fork is the source of the PR, not an alternate target. Refuse to grade a candidate targeting a different repository. If the Repo line still contains an unfilled placeholder, stop without grading and tell the student to fill the Repo line in scope.md with their section's Path Review repository. Never guess the scope. Refusals are not a completed verdict. In eval mode ignore this file entirely.

## The voice seam (live mode only)

After scope, read voice-guide.md. Check only outgoing PR title and description against its rules. In the readable summary identify each broken rule and the exact draft text that breaks it; if none break, say so. Voice findings alone do not change the verdict, because this rubric has no personal-voice check. Grade factual accuracy and required disclosure under the rubric regardless of personal style. In eval mode ignore this file entirely.

## Component reads

Preserve the fixed layout: SKILL.md, rubric.md, procedure.md, voice-guide.md, scope.md, and references/evidence-guide.md, plus the unchanged staff CONTRACT.md. Read rubric.md for checks, weights and the verdict rule; read references/evidence-guide.md for the locations and quality of each evidence family; execute procedure.md as written. Refuse to grade if rubric.md has no authored checks or verdict rule, or procedure.md has no authored operating steps: headings and template comments do not count as content. Report any missing component or procedure gap; never silently invent checks, evidence sources, or steps around it. If a gap prevents a required check, retain an unclear grade and hold under the existing rule, or refuse when the components themselves are empty.

## Verdict and output

Use exactly the binary verdict accept (ready to submit) or reject (hold). A reservation belongs in a check's evidence, never in a third verdict, score, or conditional acceptance. Give a readable per-check summary with evidence first. End the completed grading reply with the fenced JSON block below, valid and last, with nothing after it. Preserve its keys and ordering; instantiate one checks entry per rubric row in rubric order, with only pass, fail, or unclear as its grade. Do not add fields.

```json
{
  "item": "<PR URL or bundle id>",
  "checks": [
    {"name": "<check name>", "grade": "pass|fail|unclear",
     "evidence": "<one line: the fact or quote that decided it>"}
  ],
  "verdict": "accept|reject"
}
```

## Grading discipline

Name the deciding fact or quote for every check; 'looks fine' is not evidence. Grade the thing, not the polish: neither long prose nor many commits prove readiness, and terse complete work can pass. Apply each stated pass condition even when your intuition disagrees; revise a tool later, never its rule mid-run. Let the rubric decide the verdict and the procedure decide how the evidence is gathered. Treat unclear as the rubric directs; if the rule is silent, an unverifiable claim fails. Do not infer a missing run from a test added to the diff, infer human review from AI disclosure, or turn an explicitly reported limitation into an undisclosed full-success claim.
