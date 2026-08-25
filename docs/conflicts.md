# Why the conflict table exists

Across the seven upstream collections vendored here, 39 skills mention motion, 30 mention layout, 28 mention review and 27 mention animation. Their descriptions overlap on purpose — each author wrote a complete system. Loaded together, they compete: two skills fire for one question, each gives a defensible answer, and the page ends up designed by committee.

The fix is not to pick the "best" author. It is to give each *question* one owner.

## The splits worth understanding

**Taste vs. craft.** `tastemaker` answers whether the thing looks made by someone with an eye. `better-ui` answers whether the details are executed properly. A page can pass one and fail the other. Run taste first: polished generic is still generic.

**Building motion vs. judging it.** `animate` decides easing, duration and origin for something that does not exist yet. `review-animations` judges motion already in the codebase against a craft bar. `improve-animations` surveys a whole codebase and prioritises. `find-animation-opportunities` looks for what should animate and rejects the rest. Asking `animate` to review, or `review-animations` to build, gets you a worse version of both.

**Page architecture vs. sentence craft.** `landing-page-design` owns section order, offer framing and conversion structure. `better-writing` owns the words inside a button, an error, an empty state. They are not competing; they operate at different altitudes.

**Interface review is routed, not called.** `better-interface` is a router: it inspects the screen and calls the `better-*` skills that apply. Calling five of them yourself gets five independent opinions with no adjudication.

**Reviews of a screen vs. reviews of a change.** `interface-review` reads uncommitted work, a branch or a PR. `break` renders one component in every state it can reach. The visual-critique skills in `library/designer/` critique a rendered screenshot. Pick by what you actually have in hand.

**Performance has two owners.** `optimize-web-animations` for DOM/CSS/GSAP work. `optimize-threejs-games` for WebGL scene cost. A stuttering hero with both needs both, in that order.

## When the table has no row

Then no skill owns it. Decide yourself, state the reasoning in one sentence, and if the decision keeps coming back, add a row.
