#!/usr/bin/env python3
"""Check the built plugin before committing: frontmatter, catalog integrity, context cost."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "pipeline-core"
errors, warn = [], []

mk = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
for p in mk["plugins"]:
    if not (ROOT / p["source"].lstrip("./") / ".claude-plugin" / "plugin.json").exists():
        errors.append(f"{p['name']}: no plugin.json")

registered = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
reg_desc = 0
for sk in registered:
    m = re.match(r"---\n(.*?)\n---", sk.read_text(errors="ignore"), re.S)
    if not m:
        errors.append(f"{sk}: no frontmatter"); continue
    name = re.search(r"^name:\s*(.+)$", m.group(1), re.M)
    desc = re.search(r"description:\s*(.*?)(?=\n[a-z_]+:\s|\Z)", m.group(1), re.S)
    if not name: errors.append(f"{sk}: no name")
    if not desc: errors.append(f"{sk}: no description")
    else: reg_desc += len(desc.group(1))
    if name and name.group(1).strip() != sk.parent.name:
        warn.append(f"{sk.parent.name}: frontmatter name is '{name.group(1).strip()}'")

rows = [l.split("\t") for l in (PLUGIN / "catalog" / "index.tsv").read_text().splitlines()
        if not l.startswith("#")]
names = set()
for r in rows:
    if len(r) != 6:
        errors.append(f"malformed catalog row: {r[:1]}"); continue
    if not (PLUGIN / r[5]).exists():
        errors.append(f"catalog points at a missing file: {r[5]}")
    if r[0] in names:
        errors.append(f"duplicate catalog name: {r[0]}")
    names.add(r[0])

lib = list((PLUGIN / "library").glob("*/*/SKILL.md"))
if len(lib) != len(rows):
    errors.append(f"catalog has {len(rows)} rows but library has {len(lib)} skills")
for l in lib:
    if l.parent.name in {s.parent.name for s in registered}:
        errors.append(f"'{l.parent.name}' is both registered and in the library")

fs = PLUGIN / "bin" / "find-skill"
if not fs.exists():
    errors.append("bin/find-skill missing")
else:
    if not fs.stat().st_mode & 0o111:
        errors.append("bin/find-skill is not executable")
    out = subprocess.run([sys.executable, str(fs), "scroll", "pinned"], capture_output=True, text=True)
    if out.returncode or len(out.stdout.splitlines()) < 3:
        errors.append(f"find-skill smoke test failed: {out.stderr.strip()[:200]}")
    elif len(out.stdout) > 2000:
        warn.append(f"find-skill output is {len(out.stdout)} bytes; keep it under ~1500")

for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and ".cache" not in f.parts and f.stat().st_size > 262144:
        warn.append(f"large file {f.relative_to(ROOT)} ({f.stat().st_size // 1024}KB)")

print(f"registered skills: {len(registered)}  (~{reg_desc // 4} tokens of descriptions, always loaded)")
print(f"library skills: {len(lib)}   catalog rows: {len(rows)}")
print(f"router body: ~{(PLUGIN / 'skills' / 'site-pipeline' / 'SKILL.md').stat().st_size // 4} tokens when it fires")
print(f"one lookup: ~{len(out.stdout) // 4} tokens" if fs.exists() else "")
for w in warn: print(f"warn: {w}")
for e in errors: print(f"ERROR: {e}")
sys.exit(1 if errors else 0)
