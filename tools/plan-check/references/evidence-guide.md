# Evidence guide: where evidence lives in a plan package

## Diagnosis and grounding

Eval: read Issue and Repro evidence before Candidate plan / Diagnosis and Candidate plan comment. Collect expected behavior, exact inputs, failure boundary, error or timing artifacts and controls. Live: fetch the issue body and the student's own posted Unit 2 reproduction, then compare their quoted evidence in plan.md and comment.md. A classmate's report cannot establish the student's reproduction.

Good: the explanation accounts for the observed boundary and controls; an unverified mechanism is labelled with a concrete check. Practice calib-03 shows why pager speculation cannot explain slow rendering with no pager in the loop. A thread assertion does not outrank that control. The proposed change must affect the evidenced cause, not just swallow its symptom.

## Scope

Eval: Candidate plan's Scope, Change, Files or equivalent terse sentences, cross-read with Issue and Thread highlights. Live: the same draft sections and maintainer requests in the full issue thread. Extract behaviors and areas included and excluded; an explicit non-goals heading is optional when the boundary is clear.

Good: one connected fix plus its tests and needed docs. Practice calib-01 bounds the post-push refresh callback and excludes changes to status computation and other views. A convenient refactor or new feature that the failure does not require expands the scope.

## Executability

Eval: Candidate plan's Approach, Changes, Files, prerequisites, or equivalent prose. Live: plan.md and comment.md checked against repository docs/CONTRIBUTING.md, docs/SETUP.md, Makefile, source locations and workflows as relevant. Record the start point and actual operation, not an intention to investigate eventually.

Good: a stranger knows which component to alter and how. Calib-01's push completion callback and added refresh context are executable despite its short form. Calib-02's 'poke around the editor components' leaves the mechanism and start point undecided. Exact filenames are useful but unambiguous functional locations also count.

## Test plan

Eval: Candidate plan's Test plan/Test compared directly to Repro evidence's steps and controls. Live: quoted Unit 2 command or manual steps and expected result in the drafts; use the posted repro to verify the quote. Do not import an unmentioned test from another file into the plan being graded.

Good: a trigger and observable output that would fail before and succeed after, plus identified shared-path controls. Calib-01 points at repro step 3 and requires the color to update without leaving the view. Calib-04's cargo test --workspace alone never checks the two working directories, so suite success alone cannot establish the specific regression.

## Honesty

Eval: diagnosis confidence, risks/unknowns and commitments throughout both candidate drafts, cross-read with Repro evidence, Thread highlights and Repo facts. Live: those drafts, their ## Deviations entry, the student's evidence, and any posted plan being updated. Record a known uncertainty's decision/check path and each actual deviation's reason.

Good: evidence is described at its actual strength, hypotheses remain testable, results and review are not fabricated, and a build deviation is visible before a follow-up is posted. No separate risk paragraph is necessary for a small evidenced fix. Calib-02's completion promise and undefined mechanism cannot be upgraded into proof by confident wording.

## Comms

Eval: Candidate plan comment read against the plan, Issue, Thread highlights, and Repo facts' stated contribution, template and AI policies. Live: the complete issue/comment thread, repository docs/CONTRIBUTING.md and any stated AI policy, scope house rules, and the installed Unit 2 voice-guide.md. Fetch all comments before posting to detect an existing own plan and avoid duplicates.

Good: the comment stands on the student's own diagnosis and reproduction, names the bounded operation and verification, and meets explicit maintainer prerequisites and applicable AI disclosure rules. A selective-review policy (calib-01) is not a ban; a human-authored-comments policy (calib-04) must be respected on its own terms. Do not invent policies where Repo facts says none; do not require every bug-report-template field to be repeated in an existing issue's plan comment. Live Path Review house rules allow classmates' parallel plans, but not piggybacked writing.
