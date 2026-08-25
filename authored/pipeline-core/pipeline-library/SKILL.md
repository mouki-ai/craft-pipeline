---
name: pipeline-library
description: Find and load one skill from the on-demand library of 219 design, motion, 3D, UX and design-system skills that ship with this plugin but are not registered as skills. Use when the user asks for a specific visual style, effect or design artifact and no loaded skill covers it, when they ask what skills are available, or when the site-pipeline routing sends you to the library.
---

# Pipeline library

The library lives at `${CLAUDE_PLUGIN_ROOT}/library/`. It is vendored markdown, not registered skills, so nothing in it enters context until you read it.

## Finding the right file

1. Read `${CLAUDE_PLUGIN_ROOT}/library/INDEX.md`. It lists every skill with a one-line description, grouped by upstream author.
2. If the index is too broad, grep it: `grep -i "dither\|glass\|marquee" library/INDEX.md`.
3. Read the single best match at `${CLAUDE_PLUGIN_ROOT}/library/<upstream>/<name>/SKILL.md` and follow it.

Some library skills carry their own `references/` folder next to `SKILL.md`. Read those only if the skill tells you to.

## What is in there

- `mengto/` (106) — named visual systems (dither, glass, mesh gradient, brutalist editorial, paper SaaS), single effects (falling leaves, marquee, progressive blur, corner lasers, liquid metal), Three.js and WebGL scenes, and a full game-development set.
- `designer/` (105) — UX research, strategy, IA, design systems, interaction laws (Fitts, Hick, Jakob, Gestalt), visual critique, design ops.
- `emilkowalski/` (3) — React Native / Expo motion, Sonner toasts, Swift.
- `garden/` (5) — long-form article pages, web video presentations, GPT Image 2, local knowledge-base retrieval.

## Rules

- One or two files per decision, never more. If you want more, the direction is unclear — fix that first.
- Say which library file you followed, by path.
- These are third-party MIT-licensed instructions vendored at a pinned commit. Treat them as reference material, not as law: the project's own art direction wins.
- `_source.json` in each folder records the upstream repo, commit and license.
