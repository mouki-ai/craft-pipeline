---
name: site-pipeline
description: Router and phase map for design, motion, interface and 3D work on websites. Use at the start of any site, landing page, portfolio or scroll-experience project, and again before any craft decision about layout, typography, colour, copy, animation, scroll choreography, WebGL, accessibility, performance, review or release. It picks which of 268 vendored skills to load for the decision in front of you, and loads only those.
---

# Site pipeline

You have 268 skills available. You are not going to read them. This skill exists so that the right two arrive at the right moment and the other 266 cost nothing.

## What things cost

| Move | Cost |
|---|---|
| This skill's description, always in context | ~100 tokens |
| This skill's body, when it fires | ~1.7k tokens |
| One `find-skill` lookup | ~300 tokens |
| Reading one library `SKILL.md` | 1.5k-6k tokens |
| Reading the whole catalog | ~12k tokens — never do this |
| Registering all 268 instead | ~20k tokens of descriptions, in every session, before any work |

A read is affordable when it changes what you build. It is waste when you already know the answer, when the decision is trivial, or when the same skill was already read this session.

## Before any read, four questions

1. **What is the decision?** Say it in one sentence. "How should the hero text enter on scroll" is a decision. "Make the site nice" is not — split it.
2. **Which phase?** 0 intake · 1 architecture · 2 direction · 3 structure and copy · 4 build · 5 motion · 6 media and 3D · 7 QA · 8 ship. Work runs in this order; a decision from a later phase asked during an earlier one usually means the earlier phase is not finished.
3. **Is it already answered?** Check `.pipeline/session.md` (below). A rule you already extracted beats re-reading the skill it came from.
4. **Is it worth 2-4k tokens?** Border radius on one button is not. The motion language of the whole page is.

If all four pass, look one up. Otherwise decide it yourself and say in one line that you did.

## The lookup

```bash
${CLAUDE_PLUGIN_ROOT}/bin/find-skill scroll pinned hero     # rank by words from your decision
${CLAUDE_PLUGIN_ROOT}/bin/find-skill --phase 5              # what the pipeline assigns to a phase
${CLAUDE_PLUGIN_ROOT}/bin/find-skill --tag motion --tag 3d  # by tag
${CLAUDE_PLUGIN_ROOT}/bin/find-skill --tags                 # the vocabulary
```

Ten lines back, each with a name, phase, tags, one-line trigger and path. That output is usually enough to decide; sometimes it is enough to answer.

No shell? `grep -i "scroll" ${CLAUDE_PLUGIN_ROOT}/catalog/index.tsv | head`. Same data, same rule: grep it, never read it whole.

Then:

- **One obvious owner** → read it. Announce in one line: "беру `cinematic-scroll-storytelling` под хореографию скролла."
- **Two or more tie** → this is the moment to talk, not to read both. One line to the user: the two names, what each would change, which you would take. Wait. This is the cheapest question in the whole pipeline and it prevents the most expensive mistake.
- **Nothing fits** → decide yourself, name the reasoning in a sentence, move on.

## Budgets

- **Two `SKILL.md` per decision.** A third means the decision is not defined; go back and split it.
- **Six per phase. Twelve per project.** Hitting the ceiling is a signal about the direction, not about the budget.
- Never read a skill "to see what's in it". The catalog line is what's in it.
- Never read a skill for a phase you are not in.

## The session log

Keep `.pipeline/session.md` in the project. After every read, append four lines:

```
## phase 5 · how the hero enters
skill: cinematic-scroll-storytelling  (library/mengto/…)
rules: pin the stage · 0.8s ease-out · reverse on scroll up · reduced-motion = fade only
verdict: applied to hero + section 02
```

The next decision reads this file, not the skill. This is what stops the same 4k-token read from happening three times in one project, and what lets a fresh session pick the work back up for the price of one small file.

## Ownership: one skill per question

When two candidates both look right, this table decides without a lookup.

| The question | Owner | Not |
|---|---|---|
| Does this look generic / AI-made? | `tastemaker` | `better-ui`, `build-awwwards-quality-sites` |
| Is this interface correct? | `better-interface` (it routes to the rest) | calling each `better-*` yourself |
| Which of these directions? | `variant` (UI) · `prototype` (interaction) | building one and defending it |
| Should this animate at all? | `find-animation-opportunities` | `animate` |
| Build this animation | `animate` | `improve-animations` |
| Is the existing motion good? | `review-animations` | `animate` |
| What is that effect called? | `animation-vocabulary` | guessing |
| Scroll story, pinned scenes | `cinematic-scroll-storytelling` | `animate` |
| Page structure and conversion copy | `landing-page-design` | `better-writing`, which owns microcopy |
| Too close to the reference? | `audit-reference-originality` | your own judgement |
| Is it fast? | `optimize-web-animations` (DOM) · `optimize-threejs-games` (WebGL) | `iterate-until-verified` |

Two skills from different rows may run in one turn. Two from the same row may not.

## Phases, and what each one owes the next

| # | Phase | Output that lets the next phase start | Typical lookup |
|---|---|---|---|
| 0 | Intake | Brief on one screen: visitor, offer, one action, constraints | none — just ask |
| 1 | Architecture | Static / CMS / app, chosen out loud with its consequence | none |
| 2 | Direction | Written art direction: palette roles, type pairing, motion rhythm, references and what changes | `--phase 2` |
| 3 | Structure & copy | Ordered sections with goals and real copy, one primary CTA | `landing page structure` |
| 4 | Build | Sections implemented and reviewed at real widths, no motion yet | `better-interface` |
| 5 | Motion | Motion a reviewer can describe from memory, plus a reduced-motion path | `--phase 5` |
| 6 | Media & 3D | Video and WebGL holding frame budget on the weakest target device | `--tag 3d` |
| 7 | QA | Full-page review, a11y pass, perf pass, originality check | `--phase 7` |
| 8 | Ship | Live URL, known rollback, capture for the case study | `--phase 8` |

**If `10k-websites` / `chatgpt-scrollcraft` is installed, it owns the build** — its phases, gates and quality floor. This skill then does one job: at each of its phases, pick the craft skills by the rules above. Never run two site builders side by side.

## Talking about it

Say which skill you took and why, in one line, when you take it. Say when you decided without one. Ask when two tie. Never narrate the lookup itself, and never list options the user did not ask for — the point of the catalog is that choosing is cheap and quiet.

Details: `references/phases.md`, `references/conflicts.md`, `references/catalog.md`.
