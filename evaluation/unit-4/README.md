# Unit 4 Codex provider adaptation

The course starter at [codepath/ai301-unit4-starter](https://github.com/codepath/ai301-unit4-starter/tree/76e4b7382740da2a496e538ae2a0ece3f07272fd) pins Claude Sonnet. William explicitly requested Codex instead of Claude. This directory preserves `run_eval.original.py` byte for byte and provides the separately identified `run_eval.py` provider adaptation. The generated transcript names GPT-6.1 Sol; it is not an official Sonnet evaluation, and course equivalence has not been established.

The adapter retains the original frozen packages and gold labels, prompt template, four skill-file reads, empty-component guards, JSON parsing, retries, scoring, category floor, full-run requirement, and SHA-256 fingerprints. Static AST comparison confirms only `grade_one` (provider execution) and `write_run` (truthful provenance header) differ; the scoring `main` function is identical. The prompt-template SHA-256 is `67ed40cc6553e3dd1343c8f01e47699ac7944ce6393b25d167c8a8726228d158` in both copies. All 24 package pairs and the gold-label file are byte-identical to the pinned starter. The model receives one package and the four skill components. Gold labels enter only the scoring stage; they are never added to the judge prompt. `provider.patch` records the source difference.

The adapter invokes the already installed native Codex CLI 0.160.0 at `/home/wazimmerman/.local/share/mise/installs/codex/0.160.0/bin/codex`, with `gpt-6.1-sol`, medium reasoning, ephemeral sessions, no user configuration, an empty temporary working directory, and tools disabled. It removes `OPENAI_API_KEY`, `CODEX_API_KEY`, and `ANTHROPIC_API_KEY` from the child environment and uses existing ChatGPT authentication. It creates no API credentials or paid API fallback. `RUST_LOG=off` prevents inherited verbose transport logging from entering results.

The older CLI 0.128.0 on PATH rejected GPT-6.1 Sol and GPT-5.3-Codex before grading. A minimal `READY` request succeeded using native CLI 0.160.0 and GPT-6.1 Sol. Those startup diagnostics are not evaluation verdicts.

To reproduce, clone the pinned starter, copy this adapted `run_eval.py` into a separate copy of its `eval/` directory, and run from there:

```bash
python3 run_eval.py --skill ~/.claude/skills/pr-precheck --save-run eval-run.txt --out results.json
```

The installed skill is the canonical authored copy; `tools/pr-precheck/` is its submission snapshot. Never hand-edit the generated transcript. A 20-package Codex score measures agreement on this preserved set; it does not establish equivalence to the course's pinned Sonnet model.
