# craft-pipeline

A single pipeline for building cinematic, motion-rich websites, assembled from seven
open skill collections and one routing layer that decides which of them owns each
decision.

268 skills went in. 51 are loaded by default; the other 219 sit in a library the
pipeline reads on demand, so they cost nothing until a phase calls for one.

## Why it is split in two

Installing 268 skills at once does not give an agent 268 abilities. Their
descriptions collide — 39 mention motion, 30 mention layout, 28 mention review —
so two or three fire for the same question and the page ends up designed by
committee. The descriptions alone would also cost roughly 20k tokens of context in
every session.

So the repo has two tiers:

- **Core** (`plugins/*/skills/`, 51 skills, ~4.4k tokens of descriptions) — the
  skills a site project actually reaches for, grouped by phase, with one skill per
  question.
- **Library** (`plugins/pipeline-core/library/`, 219 skills) — vendored markdown that
  is *not* registered as skills. The `site-pipeline` and `pipeline-library` skills
  read `library/INDEX.md` and pull the single file a phase needs.

## Install

```
/plugin marketplace add <your-github-user>/craft-pipeline
/plugin install pipeline-core@craft-pipeline
```

`pipeline-core` is the one to install first: it carries the routing table and the
whole library. Add the others as the work needs them.

| Plugin | Skills | What it covers |
|---|---|---|
| `pipeline-core` | 4 + library | Routing table, phase map, verification loop, 219-skill library |
| `craft-direction` | 10 | Taste, art direction, reference intake, brand worlds |
| `craft-interface` | 11 | Layout, typography, colour, accessibility, UI craft, reviews |
| `craft-motion` | 17 | Animation decisions, scroll choreography, motion review |
| `craft-3d` | 4 | Three.js, WebGL landing pages, scene performance |
| `craft-ship` | 5 | Performance, QA checklists, accessibility audit, release |

## How it runs

`site-pipeline` maps the work to nine phases — intake, architecture, direction,
structure and copy, build, motion, media and 3D, QA, ship — and names the skills
that own each one. It also carries a conflict table: taste is `tastemaker`, interface
correctness is `better-interface`, building motion is `animate`, judging motion is
`review-animations`, and so on. One owner per question, stated out loud.

If you already run the `10k-websites` / `chatgpt-scrollcraft` skill, that skill keeps
the build: its phases, its gates, its quality floor. `site-pipeline` then serves only
as the routing table underneath it. See `docs/phases.md`.

## Updating

Every upstream is pinned to a commit in `scripts/sources.json`. To pull newer
versions:

```bash
python3 scripts/vendor.py     # re-fetch at the pinned commits, rebuild both tiers
python3 scripts/validate.py   # frontmatter, name collisions, size, context cost
```

Bump a `commit` field first to move an upstream forward. Nothing in `plugins/` or
`library/` is hand-edited — both trees are generated, and local changes there are
overwritten. Author your own skills in `authored/<plugin>/<skill>/`; the vendor
script copies them into the plugin on every build.

## Licences

All seven upstreams are MIT. Each vendored folder carries a `_source.json` with its
repo, commit, licence and holder. See `NOTICE.md` for the full table and for the one
collection that is referenced rather than vendored.
