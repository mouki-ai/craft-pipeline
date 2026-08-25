# craft-pipeline

268 agent skills from seven open collections, plus one router that decides which two of
them to read for the decision in front of you — and leaves the other 266 unread.

**Always in context: ~100 tokens.** Not 20k.

## The problem this solves

Installing 268 skills does not give an agent 268 abilities. Their descriptions collide —
57 mention motion, 63 mention layout, 71 mention review — so two or three fire for the
same question and the page ends up designed by committee. The descriptions alone cost
about 20k tokens in every session, before any work starts.

## How it works

| Layer | What it costs | When |
|---|---|---|
| `site-pipeline` description | ~100 tokens | always |
| `site-pipeline` body: phase map, cost model, ownership table, budgets | ~1.7k tokens | when a design/motion/interface decision comes up |
| `bin/find-skill <words>` | ~300 tokens | once per decision |
| One library `SKILL.md` | 1.5k-6k tokens | at most twice per decision |

One registered skill. Everything else is a catalog line until it is needed.

```bash
$ find-skill scroll pinned hero
scroll-scrubbed-visual-sequence  p5  [scroll,landing,media]  Build reversible scroll-controlled…
cinematic-scroll-storytelling    p5  [motion,scroll,type]    Create cinematic scroll-driven landing…
build-threejs-scroll-worlds      p6  [scroll,3d,copy]        Build rich, scroll-controlled real-time…
…
```

Eight lines back — name, phase, tags, trigger. Usually enough to decide; sometimes enough to
answer. When two tie, the router asks you one line instead of reading both. That question is
the cheapest move in the pipeline and it prevents the most expensive mistake.

## Install

```
/plugin marketplace add <your-github-user>/craft-pipeline
/plugin install pipeline-core@craft-pipeline
```

## What the router carries

- **Four questions before any read** — name the decision, name the phase, check the session
  log, judge whether it is worth the tokens.
- **A phase map**, 0 to 8: intake, architecture, direction, structure and copy, build, motion,
  media and 3D, QA, ship. Each phase states what it owes the next one.
- **An ownership table** so competing skills resolve without a lookup: taste is `tastemaker`,
  interface correctness is `better-interface`, building motion is `animate`, judging motion is
  `review-animations`, page structure is `landing-page-design`.
- **Budgets**: two reads per decision, six per phase, twelve per project. Hitting the ceiling
  is a signal about the direction, not the budget.
- **A session log** at `.pipeline/session.md` — the rules extracted from a skill, so the next
  decision reads four lines instead of re-reading 4k tokens.
- **Deference**: if `10k-websites` / `chatgpt-scrollcraft` is installed, that skill owns the
  build and this one only routes underneath it.

## Layout

```
authored/pipeline-core/     hand-written: the router, its references, bin/find-skill
plugins/pipeline-core/      generated — do not hand-edit
  skills/site-pipeline/       the one registered skill
  library/<upstream>/<name>/  268 vendored skills, never auto-loaded
  catalog/index.tsv           one grep-able line per skill
  catalog/by-phase/*.tsv      the curated per-phase shortlists
  bin/find-skill              the lookup command
scripts/sources.json        pinned commits, phase assignments, tag rules
scripts/vendor.py           rebuilds plugins/ from the pinned upstreams
scripts/validate.py         frontmatter, catalog integrity, context cost
```

## Updating

```bash
python3 scripts/vendor.py     # re-fetch at pinned commits, rebuild library + catalog
python3 scripts/validate.py   # frontmatter, dead catalog paths, cost report
```

Bump a `commit` in `scripts/sources.json` to move an upstream forward. Promote a skill into a
phase by naming it under `phases.<n>.owners.<upstream>` — that changes ranking and `--phase`
output and costs no context. Author your own always-on skills in
`authored/pipeline-core/<name>/`; they survive every rebuild.

## Licences

All seven upstreams are MIT. Each vendored folder carries `_source.json` with repo, commit,
licence and holder. `NOTICE.md` has the full table, plus the one collection referenced rather
than vendored for want of a licence.
