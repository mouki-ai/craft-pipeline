#!/usr/bin/env python3
"""Vendor upstream agent skills and build the lookup catalog.

Reads scripts/sources.json, fetches each upstream at its pinned commit into
.cache/, then builds ONE plugin:

  plugins/pipeline-core/skills/       the router (authored here) - the only registered skill
  plugins/pipeline-core/library/      every vendored skill, read on demand, never auto-loaded
  plugins/pipeline-core/catalog/      one grep-able line per skill, so the router can choose
                                      without reading anything
  plugins/pipeline-core/bin/          find-skill, the lookup command

Re-run after bumping a commit in sources.json. Idempotent.
"""
import json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
CFG = json.loads((ROOT / "scripts" / "sources.json").read_text())
STRIP = set(CFG["library"]["strip_dirs"])
MAXB = CFG["library"]["max_file_bytes"]
PLUGIN = ROOT / "plugins" / "pipeline-core"

# tag vocabulary: tag -> regexes matched against "name description"
TAGS = {
    "motion": r"animat|motion|easing|transition|micro-interaction",
    "scroll": r"scroll|lenis|scrolltrigger|pinned|parallax",
    "3d": r"three\.?js|webgl|webgpu|shader|3d |mesh|globe",
    "type": r"typograph|typeface|font|type scale|readab|measure",
    "color": r"colou?r|palette|contrast|gradient|dark mode|theming",
    "layout": r"layout|grid|spacing|composition|hierarch|responsive",
    "copy": r"copy|writing|microcopy|content|ux writing|narrative",
    "a11y": r"accessib|wcag|screen reader|keyboard|focus state|reduced motion",
    "review": r"review|critique|audit|heuristic|qa|verify|test",
    "perf": r"performance|optimi[sz]|profil|frame|memory|budget",
    "style": r"design system|visual system|aesthetic|brand|glass|dither|skeuomorph|editorial|minimal",
    "landing": r"landing|hero|marketing page|pricing page|conversion",
    "media": r"video|image|photo|render|capture|screenshot|audio|tts",
    "research": r"research|interview|persona|journey|survey|usability|card sort",
    "system": r"token|component spec|pattern librar|naming|governance|documentation",
    "game": r"game|enemy|combat|inventory|level|rpg|fog of war",
    "ship": r"deploy|publish|release|changelog|github",
    "effect": r"particle|laser|blur|glow|marquee|cursor|reveal|ripple|leaves|orb",
}


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


def discover(repo: Path):
    out = {}
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
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        if any(part in STRIP or part == ".git" for part in rel.parts):
            continue
        if p.is_dir() or p.stat().st_size > MAXB:
            continue
        (dst / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst / rel)
    (dst / "_source.json").write_text(json.dumps(meta, indent=2) + "\n")


def tags_for(name, desc):
    hay = f"{name} {desc}".lower()
    return [t for t, rx in TAGS.items() if re.search(rx, hay)] or ["misc"]


def trigger_of(desc):
    """First clause of the description, trimmed to something a grep result can show."""
    d = re.sub(r"^(Use when|Use this skill when|Create|Build|Apply|Design)\b", r"\1", desc)
    d = d.split(". ")[0]
    return (d[:110] + "…") if len(d) > 110 else d


def main():
    print("fetching upstreams…")
    repos, skills = {}, {}
    for u in CFG["upstream"]:
        path = fetch(u)
        repos[u["id"]] = u
        skills[u["id"]] = discover(path)
        print(f"  {u['id']}: {len(skills[u['id']])} skills @ {u['commit'][:8]}")

    phase_of = {}
    for ph, spec in CFG["phases"].items():
        for uid, names in spec["owners"].items():
            for n in names:
                phase_of[(uid, n)] = ph

    if (ROOT / "plugins").exists():
        shutil.rmtree(ROOT / "plugins")
    (PLUGIN / ".claude-plugin").mkdir(parents=True)
    (PLUGIN / "skills").mkdir()
    (PLUGIN / "catalog" / "by-phase").mkdir(parents=True)

    reg = CFG["registered"]["pipeline-core"]
    for a in reg["authored"]:
        shutil.copytree(ROOT / "authored" / "pipeline-core" / a, PLUGIN / "skills" / a)
    if (ROOT / "authored" / "pipeline-core" / "bin").exists():
        shutil.copytree(ROOT / "authored" / "pipeline-core" / "bin", PLUGIN / "bin")
        for f in (PLUGIN / "bin").iterdir():
            f.chmod(0o755)

    print("\nvendoring → library/ and building catalog/")
    rows, total = [], 0
    for uid, table in skills.items():
        for name, (src, desc) in sorted(table.items()):
            u = repos[uid]
            copy_skill(src, PLUGIN / "library" / uid / name, {
                "upstream": u["repo"], "commit": u["commit"], "license": u["license"],
                "holder": u["holder"], "path": str(src.relative_to(CACHE / uid))})
            rows.append({"name": name, "phase": phase_of.get((uid, name), "-"),
                         "tags": ",".join(tags_for(name, desc)), "trigger": trigger_of(desc),
                         "path": f"library/{uid}/{name}/SKILL.md"})
            total += 1
        print(f"  {uid}: {len(table)}")

    rows.sort(key=lambda r: (r["phase"] == "-", r["phase"], r["name"]))
    head = "# name\tphase\ttags\ttrigger\tpath\n"
    (PLUGIN / "catalog" / "index.tsv").write_text(
        head + "".join(f"{r['name']}\t{r['phase']}\t{r['tags']}\t{r['trigger']}\t{r['path']}\n" for r in rows))
    for ph, spec in sorted(CFG["phases"].items()):
        sel = [r for r in rows if r["phase"] == ph]
        (PLUGIN / "catalog" / "by-phase" / f"{ph}-{spec['title'].lower().replace(' ', '-').replace('&', 'and')}.tsv").write_text(
            head + "".join(f"{r['name']}\t{r['phase']}\t{r['tags']}\t{r['trigger']}\t{r['path']}\n" for r in sel))
    counts = {}
    for r in rows:
        for t in r["tags"].split(","):
            counts[t] = counts.get(t, 0) + 1
    (PLUGIN / "catalog" / "tags.txt").write_text(
        "\n".join(f"{t}\t{c}" for t, c in sorted(counts.items(), key=lambda x: -x[1])) + "\n")

    (PLUGIN / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "pipeline-core", "description": reg["description"], "version": "0.2.0",
        "author": {"name": "Dart"}}, indent=2) + "\n")
    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": "craft-pipeline", "owner": {"name": "Dart"},
        "metadata": {"description": "One always-on router over 268 vendored design, motion and 3D skills.",
                     "version": "0.2.0"},
        "plugins": [{"name": "pipeline-core", "source": "./plugins/pipeline-core",
                     "description": reg["description"]}]}, indent=2) + "\n")

    idx_tokens = (PLUGIN / "catalog" / "index.tsv").stat().st_size // 4
    print(f"\nregistered skills: {len(reg['authored'])}   library: {total}")
    print(f"catalog/index.tsv: ~{idx_tokens} tokens if ever read whole (the router greps it instead)")


if __name__ == "__main__":
    main()
