# Evidence guide: where proof lives in a reproduction package

## Environment

Eval: compare the issue context and Repo facts with the environment record in the candidate repro report. Live: compare the issue page, repository setup docs and policy with the draft report. Good evidence identifies OS/platform, tested release or commit, and issue-relevant dependency, driver, build mode, or configuration. A different version or setup can still be useful when the difference is named and its effect considered; an unacknowledged mismatch cannot establish the issue's behavior.

## Steps

Eval: read the issue's trigger and the report's setup, input, commands, and actions. Live: use the issue page and the posted draft, including any commands or minimal example pasted in the comment. Good steps let a stranger start from a stated state and reach the trigger with public or included inputs; private files, omitted configs, and commands that exercise a different operation are not followable proof.

## Behavior shown

Eval: read output excerpts, logs, screenshots described in the package, measurements, and any control run against the issue's specific expected and actual behavior. Live: read only artifacts included or quoted in the draft comment, not unstated files on the student's machine. Good evidence shows the relevant symptom (including error class, exit status, output content, or visual state where material) or the actual result of a faithful cannot-reproduce attempt. A startup banner or mere assertion is not a symptom artifact. A different error from changed input is not the target.

## Honesty

Eval and live: compare the report's "observed", "expected", "reproduced", and any causal claims with the artifacts and the issue's own target. Good conclusions distinguish observation from hypothesis, acknowledge version/input differences, and limit confidence to what the run showed. An evidenced cannot-reproduce is ready when it describes the attempt and its limits. A guessed root cause, guaranteed fix, or claim of general reproducibility without supporting output is not.

## Comms

Eval: compare claim and report with the issue context, repo-facts contribution policy, and any stated issue-template asks. Live: read the issue thread, contributor docs and AI policy, the draft comments, and voice-guide.md. A good pre-reproduction claim names this issue and promises a concrete investigation and report without promising a fix or date. A good report uses the author's own evidence. Treat every course eval package as AI-assisted, even when its comments are silent about AI. Apply stated AI-disclosure requirements to the comments they cover: if the policy requires disclosing all AI use, silence in the candidate comments fails; if it requires disclosure only in PRs, do not invent an issue-comment requirement. Policy silence imposes no new rule.
