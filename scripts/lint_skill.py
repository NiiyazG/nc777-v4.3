#!/usr/bin/env python3
"""Structural/contract lint for NC777 skill package. Stdlib only."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'SKILL.md'; README=ROOT/'README.md'
ROLES=['prophet','architect','reviewer','developer','qa','saboteur','pitbull','cleaner','guardian','documenter','deployer']
FIELDS=['Inputs','Must do','Must NOT do','Output','Done when','Stop when','Fallback']
errors=[]; warnings=[]
def err(x): errors.append(x)
def warn(x): warnings.append(x)

def read(p):
    if not p.exists(): err(f"missing: {p.relative_to(ROOT)}"); return ''
    return p.read_text(encoding='utf-8')

skill=read(SKILL); readme=read(README)
if not skill.startswith('---\n'): err('SKILL.md must start with frontmatter')
else:
    end=skill.find('\n---\n',4)
    if end<0: err('frontmatter not closed')
    else:
        fm=skill[4:end]
        m=re.search(r'^name:\s*([^\n]+)$',fm,re.M)
        if not m or m.group(1).strip()!='nc777-ros': err('frontmatter name must be nc777-ros')
        if not re.search(r'^description:\s*.+$',fm,re.M): err('frontmatter description missing')
for name,text in [('SKILL.md',skill),('README.md',readme)]:
    if 'v4.3' not in text: err(f'{name}: v4.3 not found')

# role contracts: accept English Field labels used in v4.3.
for r in ROLES:
    p=ROOT/'references'/f'{r}.md'; t=read(p)
    for f in FIELDS:
        if f'| {f} |' not in t: err(f'{p.relative_to(ROOT)}: missing contract field {f}')

for p in [ROOT/'references'/'project-profile.md',ROOT/'references'/'artifact-contracts.md',ROOT/'tests'/'router-cases.yaml',ROOT/'scripts'/'test_routes.py']:
    if not p.exists(): err(f'missing: {p.relative_to(ROOT)}')

# One canonical tree: no duplicate hand-edited roles directory.
if (ROOT/'roles').exists(): err('duplicate roles/ tree forbidden; references/ is canonical')

# Relative links.
for md in ROOT.rglob('*.md'):
    t=md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',t):
        if target.startswith(('http://','https://','#','mailto:')): continue
        clean=target.split('#',1)[0]
        if not clean: continue
        rp=(md.parent/clean).resolve()
        try: rp.relative_to(ROOT.resolve())
        except ValueError: warn(f'{md.relative_to(ROOT)}: relative link leaves package: {target}'); continue
        if not rp.exists(): err(f'{md.relative_to(ROOT)}: broken link: {target}')

# Explicit interface contracts.
art=read(ROOT/'references'/'artifact-contracts.md')
for token in ['## QA Report','primary_lens:','failure_class:','## Security Report','## Pitbull Recovery Report']:
    if token not in art: err(f'artifact-contracts.md missing {token}')
qa=read(ROOT/'references'/'qa.md')
sab=read(ROOT/'references'/'saboteur.md')
dev=read(ROOT/'references'/'developer.md')
pit=read(ROOT/'references'/'pitbull.md')
clean=read(ROOT/'references'/'cleaner.md')
if '`primary_lens`' not in qa: err('QA must explicitly output primary_lens')
if '`primary_lens`' not in sab: err('Saboteur must consume primary_lens')
if re.search(r'write tests.*fix failures|test is failing.*fix it',qa,re.I|re.S): err('QA contains legacy fixer prompt')
if 'EXPECTED_RED' not in dev or 'EXPECTED_RED' not in pit: err('Developer/Pitbull must distinguish EXPECTED_RED')
if 'invalidate_previous_verification: true' not in clean or 'next_role: QA' not in clean: err('Cleaner must invalidate PASS and route QA')
if 'Pitbull is recovery-only' not in skill: err('SKILL must state Pitbull recovery-only')
for phrase in ['--sandbox danger-full-access','node --check','5% → 25% → 50% → 100%']:
    if phrase in skill: err(f'SKILL contains forbidden legacy default: {phrase}')

# JSON-as-YAML fixtures parse with stdlib.
try:
    data=json.loads(read(ROOT/'tests'/'router-cases.yaml'))
    if data.get('version')!='4.3': err('router cases version != 4.3')
    if len(data.get('cases',[]))<10: err('too few router regression cases')
except Exception as e: err(f'router-cases.yaml parse failed: {e}')

print(f'NC777 lint: {len(errors)} error(s), {len(warnings)} warning(s)')
for x in warnings: print('WARNING:',x)
for x in errors: print('ERROR:',x)
raise SystemExit(1 if errors else 0)
