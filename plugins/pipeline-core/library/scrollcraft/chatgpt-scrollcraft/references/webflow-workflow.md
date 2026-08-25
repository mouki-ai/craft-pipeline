# Webflow production workflow

Use this reference when building a template, landing page, CMS site, interactive marketing site, or 3D-enhanced experience in Webflow. Verify current Webflow UI, plan requirements, permissions, and connector availability before acting; Webflow changes quickly.

## Current platform routing

- Use native Webflow Designer for semantic structure, responsive layout, Variables, classes, Components, page templates, CMS Collections, interactions, SEO, accessibility, and publishing.
- Use Webflow Components and the Component Canvas for reusable sections, variants, props, slots, and responsive states. Test the main component and all variants after structural changes.
- Use Webflow CMS for content that will change: blog posts, cases, services, team, products, locations, events, testimonials, and multilingual content. Do not hard-code content that the client expects to update.
- Use Webflow AI for constrained generation/refinement, but review every result against the approved design system and accessibility requirements.
- Webflow AI Code Components are React, single-file components intended for advanced interactive functionality. They require the appropriate role/plan and are not a replacement for native Webflow structure. Current limitations include no visual editing of their internals, no CMS Content Delivery API integration, no Vue/Angular/Svelte, and no DevLink export/interoperability. Keep them isolated and expose narrow props.
- Treat Webflow App Gen as legacy/transitioning: Webflow's current help says development is paused and deprecation is beginning. Do not choose it for a new product without confirming its current status and migration path.
- Use custom code or DevLink for capabilities that need an external codebase, multi-file React architecture, full WebGL/Three.js control, complex data, or a server-side API. Never hide the core content or critical CTA only inside custom code.
- Use Webflow MCP/connector only when it is actually connected and authorized. It can be useful for CMS bulk edits, SEO/content/design-system audits, and structural updates, but inspect the available actions and preview changes before publishing.

## Discovery gates before choosing Webflow

Ask:

1. Is this a visual marketing site, a CMS-driven site, a template, an interactive application, or a product with authenticated/server-side logic?
2. Who will update content and how often? Which fields must be editable without touching design?
3. Are localization, ecommerce, forms, memberships, analytics, A/B testing, or external APIs required?
4. Does the signature interaction require native Webflow Interactions, custom JS, AI Code Components, DevLink, WebGL, or pre-rendered video?
5. What must remain portable if the site later moves away from Webflow?
6. What are the hosting, plan, Workspace role, domain, staging, backup, and publishing constraints?

Do not force a complex application into a Webflow-only architecture. Route it to a hybrid or external app when authentication, payments, high-frequency data, private APIs, or extensive real-time 3D are central.

## Build order

### 1. Audit and architecture

Inspect the existing site, pages, Collections, classes, Variables, Components, custom code, interactions, forms, locales, integrations, and publishing settings. Record the current structure before changing it.

Create an architecture map:

| Concern | Webflow decision | Owner | Editable by |
|---|---|---|---|
| Global tokens | Variables and semantic classes | Designer | Designer |
| Reusable layout | Components and variants | Designer | Designer/Marketer via props |
| Dynamic content | CMS Collections and templates | Designer | Content editor |
| Motion | Interactions or isolated custom code | Designer/developer | Designer |
| Advanced app logic | AI Code Component, DevLink, or external app | Developer | Developer |
| SEO/accessibility | Page settings, semantic structure, audits | Designer/content owner | Approved roles |

### 2. Build the design system first

- Define Variables for color roles, typography roles, spacing, radii, borders, shadows, motion durations, and breakpoints.
- Use semantic class names and predictable combo-class rules. Avoid one-off arbitrary classes that make future edits unsafe.
- Create components for navigation, buttons, cards, media blocks, forms, CTA, footer, and repeated interactive units.
- Define variants for desktop/mobile behavior, emphasis, loading, empty, error, and reduced-motion states.
- Keep content in CMS fields or component props. Keep design behavior in components and classes.

### 3. Build the static page

Implement semantic HTML, responsive layout, real content, alt text, form labels, keyboard order, visible focus, and a usable no-motion state before adding cinematic transitions.

### 4. Add motion and advanced visuals

- Prefer native Webflow interactions for simple reveal, hover, sticky, scroll progress, and transform/opacity effects.
- Use custom code/GSAP only when the interaction cannot be expressed safely in native interactions; isolate it, document initialization/cleanup, and provide a static fallback.
- Use video for cinematic background motion when interaction is not required. Provide poster, reduced-motion, mobile, and failed-load fallbacks.
- Use AI Code Components for narrow React widgets such as calculators, multi-step forms, image galleries, or other encapsulated UI—not for the whole page shell.
- Use Three.js/WebGL via a controlled embed or DevLink/external code when 3D is central. Do not put important text, navigation, or the only CTA inside the canvas.

### 5. Connect CMS and editing workflow

- Model Collections before designing Collection templates.
- Use field types that match real content behavior: plain text, rich text, image, video URL, reference, multi-reference, switch, date, and SEO fields.
- Create realistic test records including long titles, missing images, translations, empty states, and unusually long rich text.
- Give content editors safe templates and components; do not let routine content changes require structural edits.
- Preview locale, CMS, and component variants before publishing.

## Webflow-specific prompt format

When writing a prompt for a Webflow implementation, include:

```text
Platform: Webflow [site type/plan/role constraints]
Architecture: native Designer / CMS / Components / AI Code Component / DevLink / custom code
Design system: Variables, semantic classes, typography, spacing, breakpoints, variants
CMS: Collections, fields, references, templates, editable content, sample records
Interactions: trigger, target, property, duration, easing, sticky/pin behavior, cleanup
Advanced media: video/3D source, poster, crop, loading, mobile and reduced-motion fallback
Accessibility: landmarks, heading order, labels, focus, contrast, reduced motion
SEO/AEO: title, description, OG, canonical, schema, sitemap, robots, structured content
Publishing: staging, domain, forms, analytics, integrations, rollback and approval owner
Hard constraints: what must not be embedded, hard-coded, duplicated, or changed
Acceptance tests: desktop/tablet/mobile, CMS extremes, slow media, no-JS fallback, console, performance
```

## MCP and AI assistant operating rules

- Before using a Webflow MCP connector, confirm connection, workspace, site, role, and available write actions.
- Start with read-only inspection: pages, Collections, Variables, Components, current classes, SEO, and publishing state.
- Generate a plan and a small preview change before bulk CMS, class, or design-system edits.
- Use dry-run or branch/staging behavior when available. Never publish directly after an AI-generated bulk mutation without review.
- Keep content edits separate from structural/design-system edits so changes can be reviewed and rolled back independently.
- After AI changes, inspect the Designer preview, CMS records, console, responsive breakpoints, keyboard flow, and published staging URL.
- Do not expose API keys, private CMS data, payment data, or privileged site tokens to prompts or client-side code.

## Webflow release gates

- Check semantic structure, headings, alt text, labels, focus, contrast, reduced motion, and keyboard navigation.
- Test all native interactions at desktop, tablet, mobile, touch, slow media, and reduced motion.
- Check CMS long content, missing fields, empty states, pagination, filters, references, and localization inheritance.
- Audit SEO/AEO: page titles, descriptions, canonical, Open Graph, sitemap, robots, structured data, and meaningful text outside canvas-only graphics.
- Audit performance: image formats/sizes, video preload/poster, lazy loading, third-party scripts, font loading, layout shift, and WebGL GPU/memory cost.
- Run the general code/security gates in `references/release-security.md`; pay special attention to forms, custom code, embeds, API keys, external URLs, user-uploaded media, and AI-generated code components.
- Verify staging and production separately, record the published URL, test forms and analytics, and confirm rollback/version history.

## Official study sources

- Webflow AI overview: https://help.webflow.com/hc/en-us/articles/34297897805715-Webflow-AI-overview
- AI code components: https://help.webflow.com/hc/en-us/articles/51168990228499-Build-AI-code-components
- Webflow MCP/Claude connector: https://webflow.com/updates/use-the-webflow-connector-in-claude
- Component Canvas: https://help.webflow.com/hc/en-us/articles/49505240420755-Component-canvas
- Webflow Designer guide: https://university.webflow.com/resources/guides/quick-guide-designer-role
- Webflow video library: https://university.webflow.com/videos
- Webflow courses: https://university.webflow.com/courses
