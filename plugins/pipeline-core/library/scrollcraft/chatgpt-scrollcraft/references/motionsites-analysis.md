# MotionSites methodology analysis

This note captures the publicly observable prompt methodology from MotionSites and converts it into original guidance for `chatgpt-scrollcraft`. It is a pattern study, not a copy of the site's paid prompt catalog.

## Public scope

MotionSites presents a library of website, app, and section prompts for AI builders such as Lovable, Bolt, Cursor, Claude, and similar tools. Its public pages advertise 500+ prompts through the MCP product, while individual premium prompt copies may require an account or paid access. Use the public material to study structure and workflow; do not reproduce a closed catalog or paste full third-party prompt text into this skill without permission.

Primary public pages:

- https://motionsites.ai/
- https://motionsites.ai/sections
- https://motionsites.ai/apps
- https://motionsites.ai/mcp
- https://motionsites.ai/academy
- https://motionsites.ai/lesson/build-animated-website-with-motionsites
- https://motionsites.ai/lesson/build-animated-website-with-ai

## What the methodology does well

### 1. It starts with a build contract

The public examples identify the framework, runtime, styling system, animation library, icon library, page count, and whether the first pass should be generated completely before refinement. This reduces ambiguity for AI coding tools.

### 2. It turns visual intent into implementation details

The prompts commonly specify:

- exact fonts, weights, imports, smoothing, selection, and global background;
- design tokens and Tailwind extensions;
- file/component ownership;
- exact copy and forced line breaks;
- asset URLs, image roles, dimensions, aspect ratios, and crop rules;
- z-index layers, absolute/sticky/fixed behavior, grids, flex ratios, and viewport heights;
- desktop, tablet, and mobile differences;
- icon package and named icons;
- animation keyframes, easing, duration, delay, stagger order, and `AnimatePresence` behavior;
- a final visual inspection list and small follow-up refinements.

This is the correct level of precision for a first implementation prompt, but it still needs our additional accessibility, licensing, security, and failure-state gates.

### 3. It uses a two-pass workflow

The public academy workflow is:

1. Select a visual direction or section.
2. Generate a complete first version.
3. Preview it at multiple screen sizes.
4. Make small, isolated refinements.
5. Replace generic assets and publish.

Use this as a production rhythm, but add our approval gates before paid generation, before architecture lock, and before release.

### 4. It treats sections as reusable design units

The public taxonomy separates complete sites, apps, and sections such as hero, features, pricing, CTA, footer, and social media. This maps well to our effect and recipe library, provided each unit also records its story role, compatibility, mobile fallback, and provenance.

## Original MotionSites-inspired prompt recipe

Use this structure when creating a new implementation prompt:

```text
Build [product/site] as [framework + runtime + styling + motion + icon stack].
Scope: [exact sections], [scroll/page-height rule], [what must not be added].

GLOBAL SYSTEM
- Fonts and weights: [families, import, roles]
- Tokens: [background, text, muted, accent, border, hover, radius, shadow]
- Global CSS: [reset, smoothing, selection, overflow, reduced-motion baseline]

PROJECT MAP
- [file] owns [component/state]
- [library] handles [motion/icons/data]
- [data boundary] separates content from presentation

ASSET MAP
| role | source | dimensions/aspect | fit/position | fallback | permission |

SECTION [name]
- Purpose: [user-visible job]
- Exact copy and line breaks: [copy]
- Desktop: [grid, offsets, size, z-index, crop]
- Tablet: [changes]
- Mobile: [changes and touch behavior]
- Interaction: [trigger, state, close/exit]
- Motion: [keyframes, duration, easing, stagger]

ROBUSTNESS
- [video retry/poster/muted policy]
- [asset failure and loading states]
- [keyboard/focus/reduced motion]
- [privacy, security, and external-resource rules]

GENERATE AND VERIFY
- Complete the first pass before cosmetic edits.
- Preview desktop, compact desktop, tablet, and phone.
- Check exact acceptance states and report deviations.
- Apply one isolated correction per iteration.
```

## Patterns worth importing into Scrollcraft

Keep these as reusable methods, not brand-specific copies:

- sticky background video with content crossing over it;
- liquid-glass navigation and CTA surfaces;
- fixed responsive nav with animated mobile drawer and body-scroll lock;
- parallax background/foreground layers with a fixed title plane;
- staggered word entrance and blurred text reveal;
- viewport-height hero compositions with explicit no-scroll behavior;
- asset-map-driven cards, image strips, overlays, badges, and icon systems;
- “generate full first version, then refine one variable” workflow;
- prompt categories for full landing pages, apps, hero sections, feature sections, pricing, CTA, and footer.

## What to add beyond MotionSites

Before implementation, our workflow must still add:

- discovery: product, audience, conversion goal, content lifecycle, platform/CMS, and ownership;
- 3–5 reference matrix and a fidelity contract for each borrowed effect;
- original adaptation note instead of copying another site's identity;
- asset provenance, licensing, and remote-asset failure policy;
- semantic HTML, keyboard/focus behavior, reduced motion, contrast, and touch checks;
- code/build/dependency/secret/security checks from `references/release-security.md`;
- payment, auth, upload, API, bot-detection, and AI-agent gates when applicable;
- acceptance matrix with screenshots or preview evidence;
- a deviation report instead of claiming pixel-perfect identity without verification.

## Library entry format

For every future external prompt source, record:

1. source URL and access date;
2. public, user-provided, licensed, or restricted status;
3. prompt family and implementation stack;
4. reusable structural patterns;
5. responsive and motion patterns;
6. missing safety/quality gates;
7. original Scrollcraft recipe derived from the observation;
8. what must not be copied.
