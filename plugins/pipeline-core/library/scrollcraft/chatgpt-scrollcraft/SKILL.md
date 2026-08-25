---
name: chatgpt-scrollcraft
description: Build premium reference-led scroll-driven websites in ChatGPT Work. Use when the user supplies example websites, screenshots, videos, or named effects and wants a close, carefully confirmed implementation. Interview until the visual target is unambiguous, request missing materials, obtain style approvals before spending generation credits, use Higgsfield as the primary visual production tool when available, use GPT Image 2 for controlled stills and edits, generate or adapt video for scroll animation, build semantic responsive code, preview the result, and verify desktop/mobile behavior before delivery.
---

# ChatGPT Scrollcraft

Treat scrolling as a timeline, not as a way to move past a stack of sections. Build an experience with a clear story, varied interaction, real text, responsive behavior, and a verifiable result.

## Operating rules

- Use the user's existing project, brand assets, copy, and images before inventing replacements.
- Keep text in HTML or the app's data model. Never bake important copy into generated images.
- Make the page accessible: semantic headings, keyboard focus, reduced-motion behavior, sufficient contrast, and touch-safe controls.
- Prefer lightweight CSS/JavaScript and progressive enhancement. A page must remain understandable if animation, video, or WebGL fails.
- Do not generate visual assets or write substantial code until the brief and journey are approved, unless the user explicitly asks for autonomous execution.
- Use at least four interaction families across a long page, with no identical family in adjacent acts. Avoid making every section a pinned hero.
- Design one memorable interaction that is specific to this project. A color change, parallax offset, or generic hover is not enough.
- Use real statistics only. If a number is not sourced or supplied, remove it.
- Avoid default AI signals: fake dashboards, arbitrary counters, gradient text, purple glow, repetitive feature-card grids, endless centered copy, scroll arrows, and visible `01 / 06` counters.
- Do not claim a site was tested or deployed until you actually preview or inspect it.
- Treat reference websites as the source of truth for visual intent. Do not replace them with a generic interpretation of “modern”, “premium”, or “cinematic”.
- Do not rely on one-shot prompting. Build and compare visible alternatives, narrow the direction with the user, and keep a reusable taste library so each project starts from evidence rather than model defaults.
- Never claim 100% pixel or behavior identity before checking the target state against the reference. State what is matched exactly, what is approximated, and what cannot be observed.
- Ask focused questions until every requested reference effect has an observable acceptance criterion. Do not begin an expensive generation while a key effect is ambiguous.
- Before any paid image/video generation, show the planned style, reference roles, model, aspect ratio, duration, and estimated credits. Generate only after the user confirms, unless the user explicitly authorizes autonomous spending.
- Prefer Higgsfield for production assets when it is connected. Use GPT Image 2 for typography-sensitive graphics, controlled edits, compositing, and cases where its output is a better fit. Do not silently substitute one for the other.
- Never assume a named Higgsfield model exists. Inspect the live catalog. If it is unavailable, explain the nearest supported model and its tradeoff before generation.
- Build video heroes from composition-first keyframes: reserve intentional negative space for copy, approve the still, then use image-to-video with one subtle dominant motion before attempting complex scenes.
- Offer a 3D direction during discovery when the product or story benefits from depth, spatial exploration, product manipulation, or a signature scroll moment. Choose the lightest viable route: layered 2.5D, pre-rendered video, canvas/WebGL, or a real-time Three.js scene.
- When Webflow is selected, route implementation through the Webflow workflow in [references/webflow-workflow.md](references/webflow-workflow.md): establish Variables, classes, Components, CMS, accessibility, and publishing boundaries before adding custom motion or AI-generated code.
- Treat the reference library as a curated source of patterns, not a collection of sites to clone. Save only analyzed, attributable, reusable patterns and record what is original in the new build.
- Before release, run the applicable code-quality, accessibility, performance, privacy, dependency, and security checks. Do not call a site production-ready while a critical or high-risk finding remains unexplained and accepted by the user.
- Match security testing to the actual feature set. A static marketing page needs a lighter review than a site with accounts, payments, uploads, admin tools, APIs, or an AI agent.

## Phase 0: Reference intake and fidelity contract

When the user provides 3–5 websites or visual references, create a reference matrix before coding. For each reference record: URL or file, exact section, timestamp/scroll position, target property, what must be copied, what must not be copied, and acceptance test.

Separate reference roles:

- **Structure:** layout, section order, hierarchy, navigation, spacing.
- **Interaction:** scroll progress, hover, pinning, reveal, cursor, transition, video scrub, or state change.
- **Art direction:** palette, type, lighting, image treatment, texture, depth, and motion feel.
- **Content behavior:** wording density, line breaks, CTA placement, and information rhythm.

Never blend several references into an undefined mood. Ask the user to assign each requested effect to a source reference and to identify the priority when references conflict.

For every effect, write a fidelity contract:

| Effect | Source state | User-visible behavior | Input | End state | Acceptance test |
|---|---|---|---|---|---|
| hero reveal | URL + scroll/hover state | exact layers and transition | wheel / pointer / touch | named final composition | compare at 0%, 50%, 100% |

Before implementation show the user: “I understand the effect as…”, the proposed mechanism, the materials required, and the visual/style sample to approve. If the user says it is not correct, revise the contract instead of coding around a misunderstanding.

Request materials by function, not vaguely. Examples: original logo SVG for crisp scaling; transparent subject cutouts for independent hero layers; desktop and mobile screenshots for responsive comparison; a clean first frame and last frame for video transition; a font license or exact font files for line-break fidelity; a screen recording when timing cannot be inferred from a URL; and the original video when scroll-scrubbing is required.

Keep `STYLE_LEDGER.md` as the single source of truth for approved references, rejected directions, tokens, image treatment, camera language, and user approvals. Do not add a style to the ledger because it merely seems tasteful. Build style only from the user's supplied examples unless the user explicitly asks for exploration. You may offer candidates from the style library, but label them as proposals and wait for selection. Every approved direction gets a small proof sheet before a full asset batch.

## Phase 1: Interview and project audit

Ask one compact set of questions before implementation. Preserve the user's wording in `SCROLL_BRIEF.md`.

1. What is the product, service, or person, and who is the audience?
2. What must the visitor believe or feel by the end?
3. What single action should the visitor take next?
4. Describe the desired vibe in 3–5 words and name up to three non-website references.
5. Describe the visitor's journey from first screen to final action.
6. Where should the experience be calm, tense, surprising, or decisive? Name one peak moment.
7. Should the site feel like one continuous world, distinct chapters, an editorial story, a gallery, or a live interactive surface?
8. What assets already exist: logo, fonts, brand rules, photos, video, illustrations, copy, repository, or hosting?
9. What must not change?
10. Which parts of each reference are mandatory, inspiration only, or forbidden to copy?
11. Should approval happen after each style frame, each effect prototype, or each full section?

If the user has already answered some questions in the conversation, reuse those answers and ask only the missing questions. If autonomous work is explicitly requested, author the missing parts, mark the brief `Self-authored`, and list assumptions in the final report. For reference-led work, ask no more than five high-value questions per round, then wait for the answers. Repeat rounds when required for fidelity.

Before coding, inspect the project structure, existing routes, package scripts, assets, and any `.openai/hosting.json`. If it is a hosted Sites project, follow the Sites workflow. If it is an existing repository, preserve its framework and conventions.

When the visual direction is not already locked, use the visual iteration workflow in [references/visual-iteration.md](references/visual-iteration.md): collect or inspect references, generate multiple directions, compare them side by side, select a small shortlist, and only then lock the page grammar, assets, and implementation plan.

When a 3D idea may improve the experience, use [references/3d-web-workflow.md](references/3d-web-workflow.md) before committing to WebGL or generated 3D assets.

When the target platform is Webflow, use [references/webflow-workflow.md](references/webflow-workflow.md) before designing the component architecture or choosing AI Code Components, custom code, DevLink, CMS, or MCP operations.

## Phase 2: Journey, grammar, and score

Turn the interview into four to seven beats. Each beat must change what the visitor knows or feels:

| Beat | Question it answers |
|---|---|
| Recognition | Why should I care? |
| Tension | What problem or desire is real? |
| Turn | What changes? |
| Proof | Why should I believe it? |
| Range | What can I explore or choose? |
| Commitment | What do I do now? |

Choose one page grammar before choosing animations:

- **Filmic cutlist:** distinct full-bleed scenes with deliberate cuts.
- **Chaptered editorial:** typography, image, and side notes advance like a magazine.
- **Continuous world:** one spatial stage changes as the visitor travels through it.
- **Gallery:** a sequence of works/products with focused transitions and quiet reading.
- **Typographic poster:** large type and controlled composition do most of the storytelling.
- **Split stage:** two states or characters respond to the same scroll position.
- **Live surface:** data, cursor, or user input makes the page feel active.
- **Rhythmic cutlist:** short visual beats alternate with longer reading moments.

Do not mix grammars accidentally. Record the chosen grammar and why the strongest alternatives lost in `SCROLL_PLAN.md`.

Write a feeling curve before assigning devices. Then create a score table with: beat, emotional job, visual state, interaction family, copy, asset, scroll span, mobile fallback, and exit condition. The peak receives the clearest visual change, the most breathing room, and a quieter setup immediately before it.

Use interaction families deliberately: pinned copy, scrubbed video, image reveal, horizontal rail, scale/depth transition, cursor response, typography assembly, split comparison, or stateful choice. Keep the total page to roughly 8–14 viewport-heights unless the story genuinely needs more.

Pause for approval after presenting the brief, reference matrix, fidelity contracts, journey, grammar, feeling curve, signature move, and score. If the user asks to proceed without approval, continue and record that choice. Also pause before each materially different visual style and before every paid generation batch.

## Phase 2.5: Asset and video production

Use the production policy in [references/higgsfield.md](references/higgsfield.md) and the composition-first video workflow in [references/video-production.md](references/video-production.md). The minimum loop is: inspect references → map the copy-safe composition → create a style frame/keyframe → show it → receive approval → estimate cost → generate the smallest useful asset → inspect the result → integrate it into the hero → revise one major variable at a time.

For video, first decide whether the user will provide a clip or wants a generation. A user-provided clip must be analyzed for usable start/end frames, subject continuity, motion direction, camera path, duration, and whether it can be scrubbed. A generated clip must receive a model recommendation, cost estimate, and a production prompt before submission. Offer a self-generation route with a copy-ready prompt and exact settings when the user wants to generate outside ChatGPT.

Use the video discipline in [references/video-production.md](references/video-production.md): one dominant subject/action per shot, motivated camera, concrete physical details, clear final frame, continuity locks, and a model-specific prompt. For complex scenes, make a keyframe board or multi-clip plan before video generation.

## Phase 3: Build in controlled passes

Work in this order:

1. Create or update `SCROLL_BRIEF.md`, `SCROLL_PLAN.md`, and a small design-token layer.
2. Build the static semantic skeleton: navigation, headings, paragraphs, media, links, and CTA.
3. Make the static page responsive and usable without animation.
4. Add the interaction families one act at a time. Use transforms, opacity, clip-path, and CSS custom properties; avoid `transition: all` and layout-thrashing animation.
5. Add the signature move as bespoke page code, keeping it isolated from reusable layout primitives.
6. Add supplied assets. Generate new images only when needed, using one consistent art direction and checking each result before integration.
7. Add motion alternatives: `prefers-reduced-motion`, low-bandwidth poster frames, mobile layout, and touch behavior.
8. Run the available project checks and start a local preview or Sites preview.

For ChatGPT-native work, use the available site-building workflow when the project is a Sites project, Higgsfield for approved production assets, GPT Image 2 for controlled stills or edits, and filesystem/code tools for an existing project. Do not force a proprietary engine into a framework that already has a working animation system. Keep interactions in the project's own components and tokens.

## Phase 4: Verify and iterate

Inspect the rendered page at minimum in these states:

- desktop wide, desktop compact, and phone portrait;
- top, middle, peak, and closing positions;
- keyboard navigation and visible focus;
- reduced motion;
- slow or missing media;
- long and short text where layout could break.

Run the applicable release gates in [references/release-security.md](references/release-security.md). At minimum, inspect the code and dependency graph, run the project's tests and build, scan for secrets, verify security headers and cookie settings, test authorization boundaries, and perform a permitted non-destructive dynamic security pass. For payments, webhooks, uploads, accounts, or AI-agent features, use the corresponding mandatory gates in that reference.

Look specifically for dead scroll, unreadable text over bright imagery, copy that never reaches full opacity, frozen video, horizontal overflow, sticky elements covering the CTA, broken touch interactions, and a close that simply fades away. Read the screenshots or preview yourself. A passing build check is not visual approval.

Fix the highest-impact issue first, then re-preview. Record what was actually verified and what could not be verified in `SCROLL_REPORT.md`.

## Delivery

Deliver the working project or artifact, plus a concise report containing:

- chosen grammar and signature move;
- journey and feeling peak;
- files changed and assets used;
- preview or deployment link if available;
- desktop/mobile/reduced-motion checks performed;
- code, accessibility, performance, privacy, and security checks performed, including tool names, scope, date, and unresolved findings;
- known limitations and the next recommended improvement.

When continuing an existing build, read the existing brief and report first, preserve accepted decisions, and change only what the user requests unless a defect requires a broader fix.

For detailed pattern selection and QA gates, read [references/patterns.md](references/patterns.md) and [references/qa.md](references/qa.md).
For reference curation and reusable effect entries, read [references/reference-library.md](references/reference-library.md). For release checks and feature-specific security gates, read [references/release-security.md](references/release-security.md).
For turning a visual reference into a precise implementation brief, read [references/prompt-library.md](references/prompt-library.md).
For public prompt-library methodology analysis and external-source curation, read [references/motionsites-analysis.md](references/motionsites-analysis.md).
For taste libraries, visual comparison, and iterative design narrowing, read [references/visual-iteration.md](references/visual-iteration.md).
For 3D direction selection, asset production, and WebGL/scroll integration, read [references/3d-web-workflow.md](references/3d-web-workflow.md).
