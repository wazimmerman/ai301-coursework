# Unit 4 evidence

- `test_evidence.md`: exact final committed-branch commands/stdout/stderr/exits, actual before/after comparison, and observed CI. `final-results.json` contains the same raw process records and code state.
- `baseline-test-unit.*`: original restricted-network tokenizer setup failure on the unchanged baseline. `baseline-test-unit-cached.*`: separate successful baseline retry after a permitted public-data cache download. Hashes are in `baseline-log-hashes.json`; neither baseline run is the final branch result.
- `plan.md`, `pr_draft.md`, `pr-body.md`: named live inputs. The source branch contains only the two parser/test files; drafts were never added to its source commit.
- `live-precheck-pre-open.*`, `live-precheck-post-open.*`, and final `live-precheck-post-output-expansion.*`: actual Codex 0.160.0 / GPT-6.1 Sol live outputs, complete input snapshots and captured committed git state. The later runs include the unchanged staff contract and observed CI. The final run reads the expanded published PR description with literal commands and complete required-check outputs. Final verdict: accept, every check pass. Prompt snapshots contain public issue-thread context with original authors identified, not a claim that classmates' work is William's.
- `pr-initial.json`, `pr-final.json`, `ci-status.json`: GitHub response snapshots establishing personal account, source SHA, base, exact body and successful checks. No merge was performed.
- Capture scripts preserve the actual local workflow and paths. Eval provenance, original/adapted source, patch, and scored results are separately under `evaluation/unit-4/`. Full evaluation transcript in `../eval-run.txt` is the generated, unchanged Codex measurement, not an official Sonnet result.

OpenAI Codex assisted preparation, implementation, command execution, grading and documentation. No human review, Claude usage or guaranteed course acceptance is claimed.
