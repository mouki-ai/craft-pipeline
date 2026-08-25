# Implementation prompt library

Use this library when a reference needs to become a production-ready build brief. These prompts are not vague mood descriptions: they are compact design packages that connect visual intent to component structure, exact tokens, responsive behavior, motion timing, assets, robustness, and acceptance tests.

## Universal prompt shape

Write the prompt in this order:

1. **Build target** — framework, runtime, package choices, page count, scroll behavior, and required deliverable.
2. **Global tokens** — fonts and weights, background, text colors, accents, borders, radii, shadows, spacing rhythm, and heading rules.
3. **Architecture** — files/components, page wrapper, semantic regions, data boundaries, and dependencies such as icons or motion libraries.
4. **Asset map** — every image, SVG, video, or external URL with its role, crop rule, fallback, and whether it may be downloaded or must remain remote.
5. **Section specifications** — exact layout, dimensions, alignment, z-index, copy, controls, and visual hierarchy for each section.
6. **Responsive states** — explicit mobile/tablet/desktop breakpoints, what moves, hides, stacks, crops, or changes size, and any JS/CSS parity requirement.
7. **Motion system** — named animations, keyframes, duration, easing, delay/stagger order, fill mode, trigger, and reduced-motion fallback.
8. **Interaction and state** — menus, search, buttons, drawers, video playback, hover/focus/touch behavior, and failure states.
9. **Hard constraints** — no extra sections, no scroll, no invented copy, no replacement assets, exact background, exact placement, or other non-negotiables.
10. **Verification** — screenshots/states to inspect, code/build checks, accessibility/performance checks, asset loading, and acceptance criteria.

Do not describe a result only as “modern”, “premium”, or “aesthetic”. Convert those words into observable rules: grid, alignment, scale, contrast, crop, timing, motion family, and exit state.

## Prompt families in this library

### A. Visual recreation prompt — Targo

Use when the goal is to recreate a small number of reference sections with high visual fidelity in plain HTML/CSS/JS or an existing app.

- Establish exact font, palette, background, uppercase heading rules, and section height first.
- Describe video as a layout element: absolute position, width/offset per breakpoint, `object-fit`, scrim, autoplay retry, mute, and failure behavior.
- Specify navigation geometry, logo construction, links, CTA clip-path, mobile hamburger, and menu state.
- Describe the headline as a measured staircase: exact lines, indent, color change, font-size cap, viewport-height cap, and CTA alignment.
- Define the about section as a handoff: gradient boundary, left text column, right edge-flush media, blend-mode overlay, and no-right-padding rule.
- End with “exactly two sections”, “no footer”, “no extra content”, and desktop/mobile visual checks.

The key lesson is that a visual prompt should encode geometry and failure handling, not just copy and colors.

### B. Framework implementation prompt — Mentality

Use when the reference must be implemented as a componentized React/Vite/Tailwind page.

- Name the stack and entry files: `src/index.css`, `src/App.tsx`, `src/components/Navbar.tsx`, and `src/components/Hero.tsx`.
- Define Tailwind tokens and font roles before component markup.
- Map each visual region to a component and name the exact classes, grid columns, breakpoints, and animation props.
- Specify external media URLs and how to blend the media into the page background.
- Define inline SVG/UI motifs explicitly, including dimensions, border, radius, and icon geometry.
- State fixed/sticky navigation, mobile `AnimatePresence` drawer behavior, and the exact hero text line breaks.
- Include the “no artificial margins/padding below the video” constraint so the implementation does not fake viewport height.

The key lesson is to join design intent with code boundaries. A good framework prompt should be directly convertible into a file plan without inventing architecture.

### C. Responsive art-directed composition — CozyPaws

Use when the design is a dense viewport composition built from remote assets, cards, image strips, overlays, and breakpoint-specific arrangements.

- Start with page-height and overflow rules: `h-screen`, no scroll, `shrink-0`, and `overflow-hidden`.
- Provide an asset table with role and URL for logo, avatar, product card, video card, and each bottom image.
- Separate desktop, tablet, and mobile layouts instead of assuming one fluid arrangement will preserve the composition.
- Describe the visual stack with explicit absolute positions, flex ratios, max heights, `z-index`, image aspect ratios, overlay locations, and badge geometry.
- List icon dependencies and exact interaction controls: search, favorites, cart, play, arrow, star, and mobile navigation.
- Define a named animation vocabulary, keyframe endpoints, durations, easing, fill mode, and delay classes.
- Write a stagger timeline in human order: header, heading, side cards, photos, then overlays.
- Require remote-asset failure states, alt text, reduced motion, focus states, and a visual check at each breakpoint.

The key lesson is that complex hero compositions need an asset map and a timing score, not only CSS classes.

## Reusable prompt skeleton

```text
Build [page type] using [framework/runtime/libraries]. It must contain [sections], [scroll rule], and [delivery constraint].

Global tokens:
- Fonts: [family, weights, role, import method]
- Colors: [background, text, muted, accent, hover, border]
- Type rules: [case, size range, line-height, tracking]
- Shared controls: [radius/clip, padding, icon, focus, hover]

Architecture:
- [file/component] owns [region/state]
- [dependency] is used for [motion/icons/data]
- [wrapper constraints]

Assets:
| Role | URL/path | Size/aspect | Crop/blend | Fallback | Restrictions |

Section [name]:
- Purpose and exact copy: [text]
- Layout: [grid/flex/absolute positions/z-index]
- Desktop: [rules]
- Tablet: [rules]
- Mobile: [rules]
- Interaction: [trigger/state/fallback]
- Motion: [keyframe, duration, easing, delay, stagger]

Hard constraints:
- [must preserve]
- [must not add/change]

Verification:
- Build/type/lint/tests: [commands]
- Visual states: [viewports and scroll/state positions]
- Accessibility/performance: [checks]
- Acceptance criteria: [observable start/mid/end and failure behavior]
```

## Quality rules for prompts

- Preserve exact copy and line breaks when typography is part of the reference.
- Use `clamp()` for fluid values only when the prompt also defines breakpoint exceptions or viewport caps.
- Keep CSS media-query breakpoints and JS `innerWidth` logic identical when both are used.
- Specify `object-fit`, `object-position`, or `object-contain` explicitly for every important media element.
- Give every video an autoplay retry policy, `muted`, `playsInline`, poster/static fallback, and reduced-motion behavior.
- Give every motion sequence a stagger order and a static end state.
- Never use external assets without recording their role, provenance, licensing/permission status, and failure fallback.
- End every prompt with what must be tested and what is forbidden to invent.

## Review method

Before implementation, convert the prompt into four artifacts:

1. **Token sheet** — fonts, colors, spacing, radii, shadows, and breakpoints.
2. **Component/section map** — files, semantic regions, ownership, and state.
3. **Motion score** — trigger, timing, stagger, reduced-motion fallback, and exit state.
4. **Acceptance matrix** — viewport/state, expected result, evidence, and pass/fail.

If any value is missing, ask the user rather than silently choosing a “similar” value. After implementation, update the prompt with the actual deviations and the reason for each one.
