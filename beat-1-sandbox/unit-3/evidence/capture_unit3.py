"""Capture commands and unmodified stdout/stderr from actual repository runs."""
import argparse
import shlex
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
repo = root / 'pathreview-unit3'
ap = argparse.ArgumentParser()
ap.add_argument('phase', choices=['before', 'after', 'checks'])
a = ap.parse_args()
array = '''import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps(["First feedback item", "Second feedback item"])
print(parse_review_output(raw))
'''
obj = '''import json
from rag.generator.output_parser import parse_review_output
raw = json.dumps({"summary": "Works"})
print(parse_review_output(raw))
'''
fence = '''from rag.generator.output_parser import parse_review_output
raw = '```json\\n["First feedback item", "Second feedback item"]\\n```'
print(parse_review_output(raw))
'''
scalars = '''import json
from rag.generator.output_parser import parse_review_output
for value in ["just text", 42, None, True]:
    for fenced in [False, True]:
        raw = json.dumps(value)
        if fenced:
            raw = "```json\\n" + raw + "\\n```"
        try:
            result = parse_review_output(raw)
            print(repr(value), "fenced=" + str(fenced), repr(result))
        except Exception as exc:
            print(repr(value), "fenced=" + str(fenced), type(exc).__name__ + ":", str(exc))
'''
py = '.venv/bin/python'
commands = [
    (['git', 'rev-parse', 'HEAD'], None),
    (['git', 'status', '--short'], None),
    ([py, '--version'], None),
    ([py, '-'], array),
    ([py, '-'], fence),
    ([py, '-'], obj),
    ([py, '-'], scalars),
    ([py, '-m', 'pytest', 'tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback', '--runxfail', '-q', '--tb=short'], None),
]
if a.phase == 'checks':
    commands = [(['make', 'check'], None), (['make', 'test-unit'], None)]
dest = root / 'evidence-unit3' / f'{a.phase}.txt'
with dest.open('w') as out:
    out.write(f'cwd: {repo}\n')
    for cmd, inp in commands:
        display = shlex.join(cmd)
        if inp is not None:
            display = display.removesuffix(' -') + " - <<'PYCODE'\n" + inp + 'PYCODE'
        out.write('\n$ ' + display + '\n')
        out.flush()
        proc = subprocess.run(cmd, cwd=repo, input=inp, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out.write(proc.stdout)
        out.write(f'[exit {proc.returncode}]\n')
        out.flush()
        print(display.splitlines()[0], 'exit', proc.returncode, flush=True)
print(dest)
