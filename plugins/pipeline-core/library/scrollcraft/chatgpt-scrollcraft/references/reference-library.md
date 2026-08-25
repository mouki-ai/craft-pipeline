# Reference and effect library

Use this library to turn approved examples into reusable design knowledge. It is not a moodboard dump and it is not permission to reproduce another site's identity.

## Site analysis card

For every retained site reference, record:

- URL, owner/creator, date reviewed, and exact section or state;
- why the user selected it and which role it has: structure, interaction, art direction, content behavior, responsive behavior, or motion;
- viewport, scroll position, pointer state, and video timestamp used for the observation;
- layout grid, typography hierarchy, spacing rhythm, color/contrast, image treatment, and loading behavior;
- interaction trigger, pinned region, progress mapping, easing, exit condition, touch fallback, and reduced-motion fallback;
- what must be copied as a requirement, what is inspiration only, and what must not be copied;
- an acceptance test that can be checked in a preview.

## Effect card

Save each reusable effect separately with:

| Field | Required content |
|---|---|
| Name | Plain-language name and implementation family |
| User purpose | What understanding, feeling, or choice it changes |
| Trigger | Scroll, pointer, tap, keyboard, time, or state |
| Mechanism | Pin, scrub, reveal, rail, depth, split, assembly, or choice |
| Inputs | Required assets, copy, dimensions, and timing |
| Safe fallback | Static, touch, reduced-motion, and slow-media behavior |
| Acceptance test | Observable start, midpoint, end, and exit behavior |
| Provenance | Source reference and the original adaptation made |

Do not store an effect as “premium”, “Apple-like”, or “cool”. Describe the visible behavior and the reason it exists.

## Recipe card

After a pattern has worked in a real project, save a recipe containing the story beat, compatible interaction families, asset requirements, responsive constraints, known failure modes, and the project where it was verified. Keep recipes compositional and original; never present a site's exact layout, copy, logo, imagery, or source code as a reusable template.

## Curation loop

1. Capture the reference state.
2. Separate observation from interpretation.
3. Ask the user to confirm the intended effect.
4. Build a small proof of concept.
5. Record the accepted adaptation and its fallback.
6. Add it only after preview verification.

The assistant should keep asking focused questions during implementation. The library preserves decisions between projects; it does not replace discovery, approval, or project-specific judgment.
