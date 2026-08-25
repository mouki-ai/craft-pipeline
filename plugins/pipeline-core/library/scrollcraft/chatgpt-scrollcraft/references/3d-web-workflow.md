# 3D web direction and production workflow

Offer 3D when it improves understanding, product interaction, spatial storytelling, or a memorable signature moment. Do not add 3D merely because it is technically impressive.

## Discovery questions

- What should the visitor understand or feel because the object is three-dimensional?
- Is the object a product, environment, character, data surface, abstract material, or decorative layer?
- Does the visitor need to rotate, zoom, explore, configure, or simply watch it move?
- Should 3D respond to scroll, pointer, touch, time, or a direct control?
- Is accurate geometry/brand identity required, or can the object be art-directed?
- What are the mobile, reduced-motion, low-power, and low-bandwidth fallbacks?

## Choose the lightest viable route

| Route | Use when | Main tradeoff | Fallback |
|---|---|---|---|
| 2.5D layers | Depth illusion is enough | Limited viewpoint | Static layered composition |
| Pre-rendered video | Cinematic motion matters more than interaction | Large media and limited control | Poster or short mobile clip |
| Canvas/WebGL | Real-time interaction or shader effect is central | Performance, accessibility, and complexity | Video or static render |
| Three.js scene | Product/environment must respond to input | Asset optimization and implementation cost | Pre-rendered sequence |
| 3D viewer | Product inspection/configuration is the user goal | Requires accurate model and controls | Image gallery |

## Production loop

1. Define the object, camera, lighting, material, background, copy-safe negative space, and interaction contract.
2. Create a still keyframe or low-cost blockout and approve composition before modeling or rendering a full asset.
3. Generate/adapt the object with the appropriate tool: Higgsfield or image generation for concept frames, Blender/Three.js for deterministic geometry, and video generation for cinematic motion.
4. Keep identity locks for products, people, logos, colors, and camera direction.
5. Optimize for the web: compressed textures, glTF/GLB where appropriate, limited polygon count, lazy loading, poster frame, and no blocking first paint.
6. Integrate the scene into the real page and test the worst frame for text contrast, CTA visibility, layout stability, touch, and reduced motion.
7. Measure performance on a mid-range phone and provide a non-WebGL fallback before release.

## Scroll and interaction rules

- Map scroll to a small number of meaningful scene properties such as camera orbit, object rotation, reveal, material state, or depth—not every pixel of motion.
- Pin a scene only when the user gains understanding or control from the pause.
- Keep a clear start, midpoint, and settled end state; avoid endless spinning objects.
- Support pointer and touch without making hover mandatory.
- Respect `prefers-reduced-motion`, keyboard focus, screen readers, and an accessible textual equivalent for meaningful content.
- Do not put important text inside a 3D canvas.

## 3D acceptance checklist

- The object loads or fails gracefully without blocking the page.
- The first meaningful content paints before heavy assets finish.
- Mobile has a tested fallback and no horizontal overflow.
- The scene does not compete with the headline or CTA.
- Interaction is understandable without a tooltip.
- GPU usage, memory, network size, and frame rate are acceptable on a mid-range mobile device.
- No third-party model, texture, HDRI, or generated asset is used without provenance and permission review.
- Security review covers remote model URLs, texture loaders, user-uploaded models, URL parameters, and any server-side conversion pipeline.
