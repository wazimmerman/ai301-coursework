# Procedure: how this skill grades a plan package

## Read order

1. Select live or eval mode. Live: read scope.md first, confirm the exact issue repository and issue identity, then read voice-guide.md. Stop without grading if scope is unfilled or the issue is outside it. Eval: use only the supplied bundle; ignore scope and personal voice, and do not fetch files or URLs.
2. Read this procedure, rubric.md, and references/evidence-guide.md. List the rubric checks in their table order and note the required-check verdict rule. If a required authored component is empty, stop and name it.
3. Read issue context, thread signals, and repo facts before the candidate writing. Record the expected behavior, constraints, and any contribution or AI policy. Then read the accepted reproduction before the plan: record the exact trigger, observed failure, controls, and artifacts so that a confident plan cannot redefine the evidence.
4. Read candidate plan, draft plan comment, risks and deviations last. Record the claimed cause, intervention, boundary, change site, verification and expected result. Grade the two drafts as one package; the comment must faithfully summarize the plan, but need not duplicate every implementation detail.

## Evidence gathering

5. For diagnosis and cause, pair each material causal claim with the reproduction step, traceback, control or artifact that supports or contradicts it. Distinguish an observation from a hypothesis; record the proposed check for any unverified mechanism.
6. For scope and executability, extract the operations, affected files or unambiguous functional areas, exclusions, dependencies, and start point from the candidate plan. Ask what behavior each operation changes and whether it is needed for this issue. Do not score headings or verbosity.
7. For tests, map each promised test to the reproduced trigger and write the explicit before/after discriminator. Record any control or shared path the plan promises to preserve; flag suite-only statements that never replay the failure.
8. For honesty, compare the plan and comment's certainty, promises and risks with the evidence; locate deviations and their reasons. An absent uncertainty heading alone is not a defect. For comms, compare outgoing text with the recorded maintainer requests, relevant repo policy and, live only, each voice-guide rule. Use the evidence guide's exact locations; live, fetch the issue, all comments, the student's own posted repro and repository contribution documents, rather than using a classmate's proof as theirs.
9. Keep an evidence ledger per check containing a short source-labelled quotation or precise fact, any opposing fact, and any genuinely absent fact. Eval evidence stays inside the frozen bundle; live evidence beyond the drafts may establish issue context but cannot fill claims or repro quotations missing from the drafts.

## Check execution

10. Execute every rubric row in table order, including rows after a failure. Compare the gathered evidence to that row's entire pass condition. Use pass when the outcome is demonstrated, fail when an explicit fact violates it, and unclear when a decisive fact is missing or irreconcilable. Do not repair the plan while grading it.
11. Quote or name the deciding evidence for each grade. Reuse a ledger fact for another check when applicable without rereading the entire package; reread the cited section when facts conflict. Prefer the accepted reproduction over an unsupported causal thread claim. Do not infer blanket bans, require unnecessary formatting, or add personal criteria.
12. In live mode, report draft comment violations with the exact voice-guide rule. Voice notes change the verdict only through a rubric row that reads them. For a deviation rerun, grade the full updated package and recorded reason, rather than granting an automatic exception.

## Verdict assembly

13. Apply the rubric rule mechanically: all required pass means accept/ready; any required fail or unclear means reject/hold. Preferred grades never change this. State any procedure gap explicitly rather than silently inventing a grading rule.
14. Give a readable line per check with source evidence and a concrete repair for each fail or unclear. Summarize the deciding required checks and any live voice notes without claiming tests were executed during plan grading.
15. End with one valid fenced JSON object containing item (issue URL or bundle id), checks (one object per rubric row with name, grade and deciding evidence), and verdict (accept or reject). Emit nothing after the JSON block. Never turn readiness into a claim of implementation, maintainer approval, human review or official course credit.
