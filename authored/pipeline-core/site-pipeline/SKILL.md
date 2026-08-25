---
name: site-pipeline
description: Routing table and phase map for building a cinematic, motion-rich website end to end. Use whenever a site, landing page, portfolio, brand page or scroll-driven experience is being planned, built, reviewed or shipped, and whenever more than one design, motion or 3D skill could apply and you need to know which one owns the question. Also use to reach the on-demand skill library that ships with this plugin.
---

# Site pipeline

This skill does not build anything by itself. It decides **which skill owns the question in front of you**, in what order the phases run, and where to find the 219 reference skills that ship with this plugin but stay out of your context until a phase calls for one.

Read it at the start of a site project, and again whenever two skills look like they both apply.

## The one rule about ownership

Exactly one skill owns each question. When two could fire, the table below wins, and you say out loud which one you are running.

**If the `10k-websites` / `chatgpt-scrollcraft` skill is installed, it governs the build.** Its phases, its gates, its approval loop, its quality floor. This skill then supplies only the routing table: at each of its phases, load the skills named below for that phase's craft decisions. Never let the two negotiate; never run a second "build me a website" skill beside it.

If it is not installed, run the phases here as written.

## Phases

| # | Phase | Load these | Gate before moving on |
|---|---|---|---|
| 0 | Intake | `landing-page-design` (intake questions only) | Brief agreed: audience, offer, one primary action |
| 1 | Architecture | — | User picks static / CMS / app. Do not skip |
| 2 | Direction | `tastemaker`, `generate-reference-inspired-brand-worlds`, `video-to-superprompt`, `stitched-full-page-capture`, `html-to-interaction-prompts` | A written art direction: palette, type, motion rhythm, references and what is being changed |
| 3 | Structure & copy | `landing-page-design`, `better-writing` | Section list approved, section by section |
| 4 | Build | `better-interface` (router → `better-layout`, `better-typography`, `better-colors`, `better-ui`, `better-accessibility`) | Each section reviewed in the real page |
| 5 | Motion | `animate` for new motion, `cinematic-scroll-storytelling` / `cinematic-gsap-lenis-motion-system` for scroll choreography, `animation-systems` for the system, `review-animations` before it lands | Motion reviewed, reduced-motion path exists |
| 6 | Media & 3D | `threejs`, `build-threejs-scroll-worlds`, `webgl-landing-steering` | Frame budget holds on the target device |
| 7 | QA | `interface-review`, `break`, `audit-reference-originality`, `accessibility-audit`, `design-qa-checklist`, `optimize-web-animations`, `iterate-until-verified` | Full-page review, not just per-section |
| 8 | Ship | `publish-project-to-github`, `browser-video-recording` for the case study | Deployed, verified live, rollback known |

## Conflict table

Read this before invoking anything in Phase 2-7.

| The question | Owner | Not |
|---|---|---|
| "Does this look generic / AI-made?" | `tastemaker` | `better-ui`, `build-awwwards-quality-sites` |
| "Is this interface correct?" | `better-interface` (it routes) | calling each `better-*` yourself |
| "Which of these directions?" | `variant` (UI) / `prototype` (interaction) | building one and defending it |
| "Should this animate at all?" | `find-animation-opportunities` | `animate` |
| "Build this animation" | `animate` | `improve-animations` |
| "Is the existing motion good?" | `review-animations` | `animate` |
| "What is that effect called?" | `animation-vocabulary` | guessing |
| "Scroll story / pinned scenes" | `cinematic-scroll-storytelling` | `animate` |
| "Page structure and conversion copy" | `landing-page-design` | `better-writing` (that owns microcopy) |
| "Is it too close to the reference?" | `audit-reference-originality` | your own judgement |
| "Is it fast?" | `optimize-web-animations` (web) / `optimize-threejs-games` (WebGL) | `iterate-until-verified` |

Two skills from different phases may run in one turn. Two skills from the same row may not.

## The library

219 more skills ship in `${CLAUDE_PLUGIN_ROOT}/library/`, deliberately **not** registered as skills so they cost nothing until you need them: 106 web-design and 3D recipes from MengTo, 105 UX and design-system skills from the Designer Skills Pack, and the rest.

How to use it:

1. Read `${CLAUDE_PLUGIN_ROOT}/library/INDEX.md` — one line per skill, grouped by upstream.
2. Read the one file you need: `${CLAUDE_PLUGIN_ROOT}/library/<upstream>/<name>/SKILL.md`.
3. Follow it as written. Report which library file you used.

Reach for it when a phase needs a specific technique the core does not carry: a named visual system (dither, glass, mesh gradient, brutalist editorial), a specific effect (falling leaves, marquee, progressive blur, liquid metal border), a research or design-ops artifact (journey map, IA, design tokens, heuristic evaluation), or a game/3D subsystem.

Do not load more than two library files for one decision. If you need more, the phase is under-specified: go back to Phase 2.

## References

- `references/phases.md` — what each phase produces and what "done" means for it
- `references/conflicts.md` — the long form of the conflict table, with the reasoning
