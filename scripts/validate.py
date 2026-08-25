#!/usr/bin/env python3
"""Sanity-check the vendored tree before committing."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors, warn = [], []

mk = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
for p in mk["plugins"]:
    d = ROOT / p["source"].lstrip("./")
    if not (d / ".claude-plugin" / "plugin.json").exists():
        errors.append(f"{p['name']}: no plugin.json")

core = {}
for sk in sorted((ROOT / "plugins").rglob("skills/*/SKILL.md")):
    t = sk.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    if not m:
        errors.append(f"{sk}: no frontmatter"); continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)", fm, re.M)
    if not name: errors.append(f"{sk}: no name")
    if not desc: errors.append(f"{sk}: no description")
    if name:
        n = name.group(1).strip()
        if n != sk.parent.name:
            warn.append(f"{sk.parent.name}: frontmatter name is '{n}'")
        core.setdefault(n, []).append(str(sk.relative_to(ROOT)))

for n, paths in core.items():
    if len(paths) > 1:
        errors.append(f"duplicate core skill name '{n}': {paths}")

lib = list((ROOT / "plugins" / "pipeline-core" / "library").glob("*/*/SKILL.md"))
for n in core:
    for l in lib:
        if l.parent.name == n:
            errors.append(f"'{n}' is in core AND library ({l.relative_to(ROOT)})")

big = [f for f in ROOT.rglob("*") if f.is_file() and ".git" not in f.parts
       and ".cache" not in f.parts and f.stat().st_size > 262144]
for f in big: warn.append(f"large file {f.relative_to(ROOT)} ({f.stat().st_size//1024}KB)")

desc_tokens = sum(len(re.search(r"^description:\s*(.+)", (ROOT / p[0]).read_text(errors="ignore"), re.M).group(1))
                  for p in core.values()) // 4
print(f"core skills: {len(core)}  library skills: {len(lib)}")
print(f"approx context cost of core descriptions: ~{desc_tokens} tokens")
for w in warn: print(f"warn: {w}")
for e in errors: print(f"ERROR: {e}")
sys.exit(1 if errors else 0)
