from pathlib import Path
import json,os,platform,subprocess
root=Path(__file__).resolve().parent.parent/'pathreview-unit4'
env=os.environ.copy();env['LLM_PROVIDER']='mock';env['RUST_LOG']='off'
commands=[
 ['git','rev-parse','HEAD'],
 ['git','status','--short'],
 ['.venv/bin/python','--version'],
 ['uv','--version'],
 ['.venv/bin/python','-c','import json; from rag.generator.output_parser import parse_review_output; raw=json.dumps(["First feedback item", "Second feedback item"]); print(parse_review_output(raw))'],
 ['.venv/bin/python','-c','import json; from rag.generator.output_parser import parse_review_output; print(parse_review_output(json.dumps({"summary": "Works"})))'],
 ['.venv/bin/python','-m','pytest','tests/unit/test_output_parser.py::TestOutputParser::test_json_array_fallback','--runxfail','-q','--tb=short']
]
records=[]
for cmd in commands:
 p=subprocess.run(cmd,cwd=root,env=env,capture_output=True,text=True)
 records.append({'command':cmd,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 print(json.dumps({'command':cmd,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}))
Path(__file__).with_name('before-repro.json').write_text(json.dumps({'platform':platform.platform(),'records':records},indent=2))
