# Video production for scroll and web motion

## Contents

- [Choose the route](#choose-the-route)
- [Prompt requirements](#prompt-requirements)
- [Scroll-readiness](#scroll-readiness)
- [Iteration rules](#iteration-rules)

## Choose the route

1. **User supplies video:** analyze it, identify the usable range, request a clean source if needed, and convert it into a scrub-friendly asset.
2. **User generates externally:** provide a complete prompt, reference map, model choice, settings, and a checklist for the returned file.
3. **ChatGPT generates through Higgsfield:** show the prompt and cost estimate, wait for approval, submit the minimum useful generation, and inspect the result before encoding.

For a website hero, prefer this composition-first route:

1. Lock the page layout, copy lane, crop, and subject placement before writing a video prompt.
2. Create a still keyframe with deliberate negative space where the heading and CTA will live. Treat the keyframe as the composition contract.
3. Approve the keyframe and its crop at desktop and mobile sizes.
4. Animate the approved image with image-to-video. Start with one restrained motion: a glow pulse, breathing atmosphere, slow camera drift, fabric movement, or a single controlled subject action.
5. Generate the smallest useful clip, inspect it, and only then add complexity or alternate shots.
6. Integrate the clip into the real hero and compare the video, text legibility, and CTA hierarchy in the actual page—not in an isolated player.

The goal is to make the video serve the page's story and typography. A technically impressive clip that competes with the headline is a failed hero asset.

Use Cinema Studio for an original cinematic shot when its strengths match the brief. Use Seedance 2.5 for complex continuity, reference-heavy action, or a longer coherent arc. Use a cheaper model for simple low-risk motion. This is a routing decision, not a promise that one model always wins.

When Seedance 2.5 is available through the connected Higgsfield workflow, consider it for image-to-video hero motion and reference-guided continuity. Verify the live model catalog and current controls first; do not hard-code a model name or assume that a model advertised in a tutorial is available in the current workspace.

## Prompt requirements

For every shot, define: subject, one dominant action, environment, spatial geography, framing, one primary camera move and its reason, lens/optical character, light direction and color, physical micro-action, environmental pressure, sound or visual motif, duration, and final frame.

For multi-shot work, repeat continuity locks in each prompt and preserve screen direction. Split a complex scene instead of hiding incompatible locations or actions in one clip.

Use a concise negative guidance list only for likely failures: identity drift, malformed hands, duplicate objects, texture crawl, lighting drift, camera jumps, focus pumping, accidental text, or watermark. Do not dilute the prompt with a giant universal negative list.

## Scroll-readiness

- Prefer a clean start frame and a decisive end frame.
- Keep the copy-safe negative space stable throughout the clip; the subject must not drift into the text lane.
- Keep the subject and key motion inside the crop-safe area for the target viewport.
- Remove audio unless the site deliberately uses sound and autoplay behavior is designed.
- Encode or process for seeking, not only playback. Test scrubbing at 0%, 25%, 50%, 75%, and 100%.
- Provide a poster frame, reduced-motion fallback, mobile crop, and static fallback.
- Choose a short clip that earns its scroll span. Longer footage is not automatically more immersive.
- For a scroll hero, test the clip as a scrubbed timeline: the first frame must establish the composition, the middle must add readable motion, and the final frame must settle without hiding the CTA.

## Iteration rules

Change one major variable per generation: subject identity, action, camera, lighting, composition, or timing. Keep accepted variables locked. Record failures and fixes in `GENERATION_LOG.md` so credits are not spent repeating the same mistake.
