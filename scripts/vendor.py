#!/usr/bin/env python3
"""Vendor upstream agent skills into this repo.

Reads scripts/sources.json, fetches each upstream repo at its pinned commit into
.cache/, then lays the skills out in two tiers:

  plugins/<plugin>/skills/<name>/   curated core, auto-discoverable by the agent
  library/<upstream>/<name>/        everything else, read on demand by the pipeline

Heavy demo folders and large binaries are stripped so a clone stays small.
Re-run after bumping a commit in sources.json. Idempotent: it rebuilds both trees.
"""
import json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
CFG = json.loads((ROOT / "scripts" / "sources.json").read_text())
STRIP = set(CFG["library"]["strip_dirs"])
MAXB = CFG["library"]["max_file_bytes"]


def sh(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def fetch(u):
    dest = CACHE / u["id"]
    if not (dest / ".git").exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"  clone {u['repo']}")
        sh("git", "clone", "--filter=blob:none", "--no-checkout", u["repo"], str(dest))
    try:
        sh("git", "checkout", "-q", u["commit"], cwd=dest)
    except subprocess.CalledProcessError:
        sh("git", "fetch", "-q", "origin", u["commit"], cwd=dest)
        sh("git", "checkout", "-q", u["commit"], cwd=dest)
    return dest


def frontmatter(p: Path):
    t = p.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    fm = m.group(1) if m else ""
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"description:\s*(.*?)(?=\n[a-z_]+:\s|\Z)", fm, re.S)
    return (name.group(1).strip() if name else p.parent.name,
            " ".join(desc.group(1).split()).strip('">') if desc else "")


def discover(repo: Path, single=False):
    """name -> (skill_dir, description). For single-skill repos the root is the skill."""
    out = {}
    if single:
        n, d = frontmatter(repo / "SKILL.md")
        out[n] = (repo, d)
        return out
    for sk in sorted(repo.rglob("SKILL.md")):
        if ".git" in sk.relative_to(repo).parts:
            continue
        n, d = frontmatter(sk)
        out.setdefault(n, (sk.parent, d))
    return out


def copy_skill(src: Path, dst: Path, meta: dict):
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    kept, skipped = 0, 0
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        if any(part in STRIP or part == ".git" for part in rel.parts):
            skipped += 1
            continue
        if p.is_dir():
            continue
        if p.stat().st_size > MAXB:
            skipped += 1
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        kept += 1
    (dst / "_source.json").write_text(json.dumps(meta, indent=2) + "\n")
    return kept, skipped


def main():
    print("fetching upstreams…")
    repos, skills = {}, {}
    for u in CFG["upstream"]:
        path = fetch(u)
        repos[u["id"]] = u
        skills[u["id"]] = discover(path, u.get("single_skill", False))
        print(f"  {u['id']}: {len(skills[u['id']])} skills @ {u['commit'][:8]}")

    # which (upstream, name) pairs are claimed by the core tier
    claimed, plugins = set(), []
    for plug, spec in CFG["core"].items():
        for uid, names in spec["skills"].items():
            for n in names:
                real = list(skills[uid])[0] if n == "__single__" else n
                claimed.add((uid, real))

    LIB = ROOT / "plugins" / "pipeline-core" / "library"
    if (ROOT / "plugins").exists():
        shutil.rmtree(ROOT / "plugins")

    print("\nvendoring core → plugins/")
    for plug, spec in CFG["core"].items():
        pdir = ROOT / "plugins" / plug
        (pdir / "skills").mkdir(parents=True, exist_ok=True)
        listed = []
        for uid, names in spec["skills"].items():
            for n in names:
                real = list(skills[uid])[0] if n == "__single__" else n
                if real not in skills[uid]:
                    print(f"  !! missing {uid}/{real}", file=sys.stderr)
                    continue
                src, desc = skills[uid][real]
                u = repos[uid]
                meta = {"upstream": u["repo"], "commit": u["commit"], "license": u["license"],
                        "holder": u["holder"], "path": str(src.relative_to(CACHE / uid)) or "."}
                copy_skill(src, pdir / "skills" / real, meta)
                listed.append((real, uid, desc))
        (pdir / ".claude-plugin").mkdir(exist_ok=True)
        (pdir / ".claude-plugin" / "plugin.json").write_text(json.dumps({
            "name": plug, "description": spec["description"], "version": "0.1.0",
            "author": {"name": "Dart"}}, indent=2) + "\n")
        for a in CFG.get("authored", {}).get(plug, []):
            asrc = ROOT / "authored" / plug / a
            adst = pdir / "skills" / a
            if asrc.exists():
                shutil.copytree(asrc, adst)
                listed.append((a, "authored", frontmatter(asrc / "SKILL.md")[1]))
        rows = "\n".join(f"| `{n}` | {u} | {d[:110]} |" for n, u, d in sorted(listed))
        (pdir / "README.md").write_text(
            f"# {plug}\n\n{spec['description']}\n\n"
            f"| Skill | Upstream | What it does |\n|---|---|---|\n{rows}\n")
        plugins.append({"name": plug, "source": f"./plugins/{plug}", "description": spec["description"]})
        print(f"  {plug}: {len(listed)} skills")

    print("\nvendoring the rest → plugins/pipeline-core/library/")
    index, total = {}, 0
    for uid, table in skills.items():
        for name, (src, desc) in sorted(table.items()):
            if (uid, name) in claimed:
                continue
            u = repos[uid]
            meta = {"upstream": u["repo"], "commit": u["commit"], "license": u["license"],
                    "holder": u["holder"], "path": str(src.relative_to(CACHE / uid))}
            copy_skill(src, LIB / uid / name, meta)
            index.setdefault(uid, []).append((name, desc))
            total += 1
        if uid in index:
            print(f"  {uid}: {len(index[uid])}")

    lines = ["# Library index", "",
             f"{total} reference skills, vendored but **not** auto-loaded. The pipeline reads them by",
             "path when a phase calls for one; you can also point the agent at any file directly:",
             "", "```", "Read library/mengto/falling-leaves/SKILL.md and apply it to the hero.", "```", ""]
    for uid in sorted(index):
        u = repos[uid]
        lines += [f"## {uid} — [{u['repo'].split('github.com/')[-1]}]({u['repo']}) ({u['license']})", ""]
        lines += [f"- **{n}** — `{uid}/{n}/SKILL.md` — {d[:150]}" for n, d in index[uid]]
        lines += [""]
    (LIB / "INDEX.md").write_text("\n".join(lines))

    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": "craft-pipeline",
        "owner": {"name": "Dart"},
        "metadata": {"description": "Cinematic site pipeline: one orchestrator plus curated design, motion and 3D skills.",
                     "version": "0.1.0"},
        "plugins": plugins}, indent=2) + "\n")

    print(f"\ncore: {sum(len(s['skills'][u]) for s in CFG['core'].values() for u in s['skills'])} skills, "
          f"library: {total} skills")


if __name__ == "__main__":
    main()
