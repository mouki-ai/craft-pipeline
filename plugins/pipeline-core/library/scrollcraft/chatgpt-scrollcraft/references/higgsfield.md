# Higgsfield production policy

## Contents

- [Approval gate](#approval-gate)
- [Model routing](#model-routing)
- [Credit discipline](#credit-discipline)
- [Reference roles](#reference-roles)
- [Inspection loop](#inspection-loop)

## Approval gate

Before a non-free generation, show:

1. target asset and its role on the page;
2. approved style ledger entry and reference images;
3. prompt summary;
4. model ID and why it fits;
5. aspect ratio, resolution, duration, audio, and other supported controls;
6. estimated credit cost and number of generations;
7. expected fallback if the result fails.

Wait for explicit approval unless the user authorized autonomous spending for this project.

## Model routing

Inspect Higgsfield's live model catalog or use its recommendation tool for each materially different task. Do not hard-code stale model names.

- **GPT Image 2:** typography-sensitive graphics, precise edits, compositing, product layouts, and controlled 1k/2k/4k stills.
- **Soul Cinema / Cinema Studio Image:** cinematic stills and visual keyframes when the approved style calls for filmic lighting or dramatic composition.
- **Seedance 2.5:** default for coherent image-to-video or text-to-video scenes, continuity, longer controlled action, and reference-heavy shots when available.
- **Cinema Studio Video 3.0:** high-end short cinematic shots when the live catalog supports it and the brief needs premium camera/light behavior.
- **Cinema Studio Video V2:** lower-cost cinematic motion, genre control, speed ramps, or custom multi-shot mode when the scene is simpler.
- **Kling 3.0:** consider when the live catalog recommends multi-shot, audio, or motion transfer.
- **Cheaper models:** use for simple camera moves, abstract backgrounds, low-risk transitions, or tests where identity and fine physics do not matter.

If the user names “Cinema Studio 4”, verify it first. If absent, say it is unavailable in the current catalog and offer the nearest supported Cinema Studio or Seedance option. Never label a substitute as version 4.

## Credit discipline

- Estimate before every paid batch. Do not spend credits to discover a style that could be tested with a single still.
- Use one approved style frame before generating a family of assets.
- Generate one result first for uncertain style or composition; use batches only after the direction is approved.
- Use the smallest duration, resolution, and number of outputs that can answer the current question.
- Keep a ledger of estimated and actual spend, model, prompt version, and result status in `GENERATION_LOG.md`.
- If the connector reports an unlimited-generation choice, surface that choice to the user. Do not silently choose credits or free allowance.

## Reference roles

Assign every input one role: identity, wardrobe, product, location, style, composition, motion, start frame, end frame, video, or audio. State what to use and what to ignore. Do not treat a moodboard as permission to copy unrelated faces, logos, or backgrounds.

## Inspection loop

After every result, inspect the actual media. Check identity, anatomy, geometry, lighting, reflections, texture stability, composition, negative space for text, and whether the intended website crop survives. Reject a result before integrating it if it fails the fidelity contract.
