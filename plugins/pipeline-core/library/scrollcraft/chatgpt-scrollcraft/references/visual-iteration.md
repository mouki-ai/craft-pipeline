# Taste library and visual iteration workflow

Use this workflow to prevent generic AI output and replace one-shot prompting with visible, reversible decisions. The user remains the taste authority; the assistant organizes options, explains tradeoffs, and records accepted and rejected directions.

## Taste library

Create a searchable library of screenshots, live URLs, videos, and approved generated assets. Each entry should contain its source, permission/provenance status, category, observable tags, liked/rejected details, actionable brief, mobile behavior, accessibility concerns, and what must not be copied. Keep separate collections for hero references and body/layout references.

## Four-pass funnel

1. Produce five materially different aesthetic directions from the approved taste library.
2. Compare them side by side and select three, recording why the others were rejected.
3. Create several body/layout directions using the shortlist and compare hierarchy, reading rhythm, CTA placement, and mobile consequences.
4. Create the smallest useful set of hero assets, compare variants, choose a color grade, and expose only safe temporary controls for final tweaks.

The exact number can shrink for small projects, but show differences before committing.

## Visual comparison

Render options in comparable frames with the same viewport, copy length, and content density. Compare first impression, hierarchy, typography, image crop, negative space, motion, mobile transformation, implementation risk, and originality.

| Option | What changed | What works | What fails | Keep/change/remove | Decision |
|---|---|---|---|---|---|

Do not average incompatible options into a muddy compromise. Choose a dominant direction and borrow only explicitly approved principles from the others.

## Live tweaks bar

For uncertain typography, accent color, spacing, reveal distance, image treatment, or motion intensity, build a development-only tweaks bar. It should expose named tokens, update CSS variables or props, support reset and copy/export, show desktop/mobile consequences, and never ship unless intentionally converted into a user feature.

## Reference feedback loop

When a build is weak, attach evidence instead of adjectives: identify the exact region/state, change one major variable, render before/after, accept or reject, and save the result as a reference or anti-pattern. Every finished project returns useful tokens, layout recipes, motion patterns, failed directions, and decision reasons to the library.

## Guardrails

- Never reproduce another site's brand, copy, logo, imagery, or source code.
- Do not generate a large asset batch before a style frame or direction is approved.
- Do not treat the first model output as the quality baseline.
- Do not let a tool's suggested style override approved references.
- Do not call a direction final until preview, mobile, reduced-motion, and content-length checks pass.
