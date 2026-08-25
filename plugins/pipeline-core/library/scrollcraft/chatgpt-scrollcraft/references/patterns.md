# Scrollcraft patterns

## Contents

- [Device selection](#device-selection)
- [Signature move test](#signature-move-test)
- [Responsive fallback](#responsive-fallback)

## Device selection

| Device | Best for | Main risk | Fallback |
|---|---|---|---|
| Pin + copy | one clear argument | dead scroll | staged opacity and transform |
| Scrubbed video | tactile process or product reveal | decode/autoplay failure | poster image plus short transition |
| Image reveal | before/after or transformation | unreadable midpoint | static comparison |
| Horizontal rail | range, cases, or options | hidden content on touch | snap-scrolling rail |
| Split stage | contrast or two paths | visual clutter | stacked comparison |
| Typography assembly | a short statement or name | poor mobile wrapping | static heading with simple fade |
| Pointer response | deliberate desktop detail | no pointer on mobile | tap or passive state |
| Stateful choice | exploration and agency | unclear exit | visible tabs and URL-safe state |

Use one device for one job. If an interaction does not change understanding, emotion, or choice, remove it.

## Signature move test

The signature move passes only if all are true:

1. It comes from the product or story, not from a generic animation library.
2. The user can understand the result without a tooltip.
3. It has a graceful static, touch, and reduced-motion state.
4. It appears once, at the intended peak or transition.
5. Removing it would make this page materially less distinctive.

## Responsive fallback

Every desktop-only idea needs a mobile equivalent. Replace hover with tap or visible state, horizontal pointer scenes with swipe or stacked content, large background video with a poster or short portrait clip, and dense overlays with a deliberate reading order.
