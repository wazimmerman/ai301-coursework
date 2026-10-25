# Procedure: how this tool grades a PR package

## 1. Read order

1. Select one package and mode. In live mode read scope.md first and refuse out-of-scope work or an unfilled Repo line; then read voice-guide.md. In eval mode read neither and use only the supplied bundle.
2. Read rubric.md and this procedure for authored content; stop if either is empty. Read references/evidence-guide.md. Report any missing component or uncovered step instead of creating an unstated rule.
3. Read repo facts, the issue and thread, then the accepted plan and repro before the diff or promotional description. Record the issue trigger, expected result, scope and exclusions, test plan, deviations, explicit maintainer direction, template asks and policy. Live sources are the named plan.md, issue thread, PR template and contributing file specified by the frame.
4. Read all committed changes and commits, then pr_draft.md/title and description, then test_evidence.md or their bundled equivalents. In live mode obtain git diff main...HEAD, git log main..HEAD --oneline, and git status --short. Record the base and head; uncommitted edits are not proof of the committed PR. Read the plan first so the candidate's confidence cannot redefine its scope.

## 2. Evidence gathering

1. For Plan fidelity build a paired list: each promised outcome/file and its implementing hunk, and each changed hunk/file and its plan allowance or recorded deviation. Compare the title/description's specific fidelity and coverage claims with that list. Record both omissions and additions, including promised documentation and controls.
2. For Reproduction and controls pair the accepted trigger and expected-after with the actual before/after observations and regression assertions. Record environment/commands or described actions, visible behavior, controls, and disclosed limits. Distinguish a test assertion from an assertion-shaped comment and a typed success claim from an observed result.
3. For Repository checks list each applicable stated command/gate beside its actual run and outcome, including exits, counts, errors, skips or 'not run' reasons where supplied. Do not infer execution from a test file, PR checkbox, or generic assurance. Frozen concrete command/result summaries count; literal raw logs are not universally required.
4. For Diff quality identify the fix and supporting tests, then inspect every remaining hunk and commit for unrelated edits or residue. A disclosed deviation can explain scope, but does not automatically make unrelated churn reviewable.
5. For Standards and communication pair each stated template/policy/thread ask with its concrete answer or supporting artifact. Check issue linkage, required changelog/docs, AI disclosure and any review conditions explicitly. Do not add requirements from personal taste. For Review navigation identify the described trigger, change and pointer to evidence. In live mode separately record outgoing voice-rule breaches with their quotes.

## 3. Check execution

1. Grade every row in rubric order using only its pass condition and the paired facts already gathered. Re-read the relevant paired source whenever a fact conflicts; do not re-read unrelated material without a reason.
2. Assign pass when the condition is supported, fail when a fact contradicts it or a mandatory item is absent, and unclear when the necessary source is unavailable or ambiguous. Give each check one concrete deciding fact or short quote, including a path/section where helpful. Missing evidence never becomes an assumed pass.
3. Read honest limitations against each check's actual rule: a justified scope deferral with matching description can pass, but a wrong-trigger test or a falsely claimed suite cannot. Do not silently strengthen a check to demand every conceivable test, raw log, template spelling, or public CI before a PR exists.
4. Execute all rows even after a required failure. Report any procedural gap without improvising around it, retaining unclear for an affected required check. Keep live voice findings separate because they alone do not decide this rubric.

## 4. Verdict assembly

1. Apply the rubric's verdict rule exactly: all required checks must pass for accept; required fail or unclear means reject; preferred grades never change the verdict.
2. State the result and a readable summary for every check. On reject, lead with the first failing or unclear required check in rubric order and quote its deciding fact; list the remaining failures too. On accept, identify the evidence for the bounded delivered result and any disclosed limits without inventing reservations as a third verdict.
3. In live mode include voice findings and any pending CI gate in the summary. End with the exact frame's JSON shape: item, checks in rubric order with name/grade/evidence, verdict. Make it the last fenced JSON block with nothing after it. Never include a score or extra fields.
