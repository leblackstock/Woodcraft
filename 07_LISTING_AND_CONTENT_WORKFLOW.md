# 07 Listing and Content Workflow

Purpose: turn approved products into truthful made-to-order or in-stock listings and reusable trust content.

## End-to-End Flow

1. Product approved in [06_PRODUCT_DECISION_WORKFLOW.md](06_PRODUCT_DECISION_WORKFLOW.md)
2. Confirm the approved product record in [30_products/](30_products/) and lock the current standard launch spec when available
3. Set `build_model` truthfully (`Made to Order`, `In Stock`, or `Sample Built`)
4. Record plan/source truth plus locked pre-sale dimensions/specs from plan, reference, or standard spec
5. Draft or update the estimated cost sheet using [80_templates/cost_sheet_template.md](80_templates/cost_sheet_template.md), including both pricing strategies and reverse checks for any already-set price
6. Record estimated labor time, made-to-order lead time, and delivery/pickup terms
7. Assemble a truthful media plan using governed media types only
8. GPT-5.5 assembles one verification packet using standard spec defaults, draft assumption-based cost math, dual-strategy pricing checks, confidence labels, media-truth notes, and highlighted exceptions only
9. Operator approves or edits one bundled approval block, including the pre-sale labor/pricing assumptions used for made-to-order pricing; update verification refs/status without inventing missing facts
10. Mark `approved_facts_status` only when facts are truly approved and keep `publish_ready: No` until facts are complete
11. Prepare Marketplace listing structure in [40_listings/](40_listings/) using [80_templates/listing_template.md](80_templates/listing_template.md)
12. **Claude Final Copy Gate**
13. Record `claude_handoff_ref`, wait for human paste-back, then record `claude_output_ref`
14. Integrate approved Claude copy and move `customer_copy_status` to `Final Integrated`
15. Set `publish_ready: Yes` only after copy integration and required non-copy checks are complete
16. Publish Marketplace listing (manual)
17. After first sale/build, capture actual receipts, labor, finished dimensions, finished photos, and pricing learnings
18. Decide keep / drop / reprice if the actual build changes the economics or offer truth
19. Repurpose approved listing facts and truthful media into Page + Instagram content prep
20. Run another **Claude Final Copy Gate** when final customer-facing captions or replies are needed
21. Schedule/queue follow-up posts (manual) only after the content asset is `publish_ready: Yes`
22. Log results and learnings

## Marketplace Listing Workflow (Listing-First, Made-to-Order Allowed)

- **Manual:** final pricing approval, verification-packet approval, platform publishing, buyer chat handling
- **GPT-5.5 orchestration:** field prep, standard-spec defaulting, draft cost math, bundled missing-info escalation, approved-fact packaging, workflow state, and Claude handoff generation
- **Claude:** final publishable listing title, description, and other customer-facing listing prose fields
- Fresh build completion is not a universal pre-list requirement. `build_model: Made to Order` may be listed before a new build exists if the pre-sale facts are locked and truthful.
- For `build_model: Made to Order`, locked standard-spec dimensions or approved plan/reference dimensions are valid pre-sale size truth.
- For `build_model: Made to Order`, a draft estimated cost sheet and draft labor assumption may be approved as the pre-sale pricing basis before the first real build exists.
- **Required before publish:**
  - approved verification packet or equivalent approved fact review
  - `build_model` recorded truthfully
  - specs/dimensions locked from the standard spec or approved plan/reference
  - pickup/delivery terms
  - lead time
  - operator-approved price reviewed against both strategies using approved pre-sale assumptions, with Strategy 2 as the default baseline unless otherwise stated and a warning surfaced whenever Strategy 1 differs by more than 15%
  - truthful listing media under the media-governance rules below
  - Claude final copy pass completed
  - `publish_ready: Yes`
- Actual measured finished dimensions are post-build validation for made-to-order items and are not a universal pre-publish blocker unless the launch spec is still unresolved.
- Actual receipts and actual labor time are also post-build validation inputs for made-to-order items; they improve later repricing decisions but are not universal pre-publish blockers when the pre-sale assumptions have been explicitly approved.

## Minimal-Input Verification Workflow (Approved Products + Listings)

- Goal: do maximum internal work first, then escalate a single approval packet instead of repeated tiny questions.
- Minimal operator evidence should be collected once and may include:
  - locked spec/dimensions note or linked standard spec used as pre-sale truth
  - current material-cost note, prior known cost reference, or receipt snapshot
  - estimated labor-hours note used as the pre-sale labor assumption
  - delivery/lead-time note
  - media provenance note when listing media is not a fresh current-build photo set
  - any actual-build notes already available
- GPT-5.5 may infer/default-fill from the linked standard spec, business guardrails, and existing approved records only when the inferred value is clearly framed as a default or recommendation.
- GPT-5.5 must calculate both approved pricing strategies whenever price is proposed or reviewed:
  - Strategy 1: current total-cost guardrail pricing
  - Strategy 2: materials cost at 30% of finished price
- GPT-5.5 must also reverse-check any already-set target/list price against both strategies before calling pricing acceptable.
- Strategy 2 is the default pricing baseline unless the operator explicitly states otherwise.
- If Strategy 1 differs from Strategy 2 by more than **15%** in either direction, GPT-5.5 must warn the operator, show both calculations, and request an explicit price choice before treating pricing as final.
- GPT-5.5 must label verification confidence per field using:
  - `Auto-verified`
  - `Recommended`
  - `Needs operator confirmation`
  - `Blocked`
- GPT-5.5 may not invent physical facts, delivery promises, measured values, costs, market claims, or media ownership.
- if cost uncertainty is too high for truthful pricing, or a real-world fact needed for truthful pre-sale claims is still missing, set `verification_status: Blocked` and escalate only the true blockers in one bundled approval block. Strategy variance by itself is a warning/escalation condition, not an automatic block.
- If defaults are usable and only a small number of exceptions remain, prepare `verification_status: Packet Ready` and present highlighted exceptions only.
- For made-to-order items, approval of the standard offer may rely on draft labor, pricing, and fulfillment assumptions when those assumptions are explicitly labeled and approved; actual receipts/labor then move to the post-build validation loop.
- `verification_status` supports movement toward `approved_facts_status: Approved`, but it does not replace approved-facts review, the Claude gate, or manual approval for pricing/publishing.

## Media Truth Governance

- Use `media_truth_status` to classify the actual listing-media type in play.
- Allowed governed media types:
  - `Owned Real Photo` — real photos from an owned prior build, current sample, or current finished piece
  - `Owned AI-Assisted Photo` — AI-assisted image derived from an owned real photo
  - `Concept / Mockup` — concept-only or mockup media that must never be implied to be a fresh finished build photo
  - `Third-Party Reference Only` — source, tutorial, plan, inspiration, or competitor media that may be kept for internal reference only
- Listing use rules:
  - owned real photos from prior builds are allowed for listing use
  - owned AI-assisted images are allowed only when derived from owned real photos and still used truthfully
  - third-party/source/tutorial/plan images must not be used as listing photos
  - planning docs may store third-party media as reference-only, but listing media fields must distinguish those assets from publishable media
- If media truth could be misunderstood, record a short `media_provenance_note` in the product or listing record.

## Claude Final Copy Gate

- No listing or content asset becomes publish-ready until the Claude copy pass is complete.
- GPT-5.5 may advance the asset through all upstream prep steps.
- When final customer-facing prose is needed, GPT-5.5 must stop and produce a Claude handoff prompt using approved facts only.
- Record `claude_handoff_ref` when that valid handoff is prepared.
- The human pastes Claude output back into the workflow.
- Record `claude_output_ref` after the paste-back occurs.
- GPT-5.5 then integrates the approved Claude copy into the correct asset, sets `customer_copy_status: Final Integrated`, and may mark `publish_ready: Yes` if all other required checks are complete.
- If Claude copy is still pending, keep the asset in structured-prep form, move draft phrasing to `customer_copy_prep_notes`, or mark the field with `[[CLAUDE_FINAL_COPY_REQUIRED]]`.
- If the Claude gate is incomplete or `publish_ready: No`, keep `publish_status` in a non-publish state only.
- Prep-only assets may not use `Ready for Manual Publish`, `Ready to Schedule`, `Scheduled`, or `Published`, and `publish_date` stays blank until an actual publish event occurs.

## Post-Sale / Post-Build Validation Loop

After the first real sale/build for a made-to-order listing:

- capture actual receipts
- capture actual labor time
- capture actual finished dimensions
- capture actual finished photos
- update the cost sheet and any pricing learnings
- decide whether to keep, drop, or reprice the listing
- replace weaker concept/pre-sale media with stronger actual media when available

## Facebook Page + Instagram Workflow (Trust/Support)

- Reuse listing source material; do not reinvent from scratch.
- Content types:
  - finished product spotlight
  - build-process snippet
  - before/after transformation
  - testimonial/proof post (when available)
- Keep copy short, visual-first, and localized where relevant.
- GPT-5.5 may prepare channel facts, post structure, CTA goals, and blocked/missing-info notes.
- Claude must write the final customer-facing caption before the post is considered publish-ready or schedulable.

## Promotion Workflow (Lightweight)

- Prioritize organic posting + relisting discipline first.
- Promote only proven listings with clear objective and stop rule.
- Log promotions and outcomes in [70_ads/](70_ads/) and record key decisions in [12_DECISION_LOG.md](12_DECISION_LOG.md).

## Where AI Helps Most

- converting rough notes into structured approved facts
- turning minimal raw evidence into one verification packet with standard defaults, dual pricing checks, and cost checks
- turning draft build-to-order assumptions into one approval-ready standard-offer packet before the first build exists
- preparing listing and content fields before the customer-copy stage
- generating Claude handoff prompts from approved facts
- creating checklist reminders for missing listing elements

## What Remains Manual for Now

- final product quality review
- new photo capture/staging when needed
- one-shot approval of verification exceptions and final pricing
- platform posting actions
- customer messaging and negotiation
- final go/no-go on promotions
