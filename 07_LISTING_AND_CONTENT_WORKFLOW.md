# 07 Listing and Content Workflow

Purpose: turn approved products into sales-ready listings and reusable trust content.

## End-to-End Flow

1. Product approved in [06_PRODUCT_DECISION_WORKFLOW.md](06_PRODUCT_DECISION_WORKFLOW.md)
2. Confirm the approved product record in [30_products/](30_products/)
3. Prepare Marketplace listing structure in [40_listings/](40_listings/) using [80_templates/listing_template.md](80_templates/listing_template.md)
4. Prepare photo/shot plan, fulfillment terms, and approved facts
5. Mark `approved_facts_status` and keep `publish_ready: No` until facts are complete
6. **Claude Final Copy Gate**
7. Record `claude_handoff_ref`, wait for human paste-back, then record `claude_output_ref`
8. Integrate approved Claude copy and move `customer_copy_status` to `Final Integrated`
9. Set `publish_ready: Yes` only after copy integration and required non-copy checks are complete
10. Publish Marketplace listing (manual)
11. Repurpose approved listing facts into Page + Instagram content prep
12. Run another **Claude Final Copy Gate** when final customer-facing captions or replies are needed
13. Schedule/queue follow-up posts (manual) only after the content asset is `publish_ready: Yes`
14. Log results and learnings

## Marketplace Listing Workflow (Sales-First)

- **Manual:** final pricing, platform publishing, buyer chat handling
- **GPT-5.4 orchestration:** field prep, approved-fact packaging, missing-info checks, workflow state, and Claude handoff generation
- **Claude:** final publishable listing title, description, and other customer-facing listing prose fields
- **Required before publish:**
  - clear photos
  - specs/dimensions
  - pickup/delivery terms
  - lead time
  - margin-safe price
  - Claude final copy pass completed
  - `publish_ready: Yes`

## Claude Final Copy Gate

- No listing or content asset becomes publish-ready until the Claude copy pass is complete.
- GPT-5.4 may advance the asset through all upstream prep steps.
- When final customer-facing prose is needed, GPT-5.4 must stop and produce a Claude handoff prompt using approved facts only.
- Record `claude_handoff_ref` when that valid handoff is prepared.
- The human pastes Claude output back into the workflow.
- Record `claude_output_ref` after the paste-back occurs.
- GPT-5.4 then integrates the approved Claude copy into the correct asset, sets `customer_copy_status: Final Integrated`, and may mark `publish_ready: Yes` if all other required checks are complete.
- If Claude copy is still pending, keep the asset in structured-prep form, move draft phrasing to `customer_copy_prep_notes`, or mark the field with `[[CLAUDE_FINAL_COPY_REQUIRED]]`.
- If the Claude gate is incomplete or `publish_ready: No`, keep `publish_status` in a non-publish state only.
- Prep-only assets may not use `Ready for Manual Publish`, `Ready to Schedule`, `Scheduled`, or `Published`, and `publish_date` stays blank until an actual publish event occurs.

## Facebook Page + Instagram Workflow (Trust/Support)

- Reuse listing source material; do not reinvent from scratch.
- Content types:
  - finished product spotlight
  - build-process snippet
  - before/after transformation
  - testimonial/proof post (when available)
- Keep copy short, visual-first, and localized where relevant.
- GPT-5.4 may prepare channel facts, post structure, CTA goals, and blocked/missing-info notes.
- Claude must write the final customer-facing caption before the post is considered publish-ready or schedulable.

## Promotion Workflow (Lightweight)

- Prioritize organic posting + relisting discipline first.
- Promote only proven listings with clear objective and stop rule.
- Log promotions and outcomes in [70_ads/](70_ads/) and record key decisions in [12_DECISION_LOG.md](12_DECISION_LOG.md).

## Where AI Helps Most

- converting rough notes into structured approved facts
- preparing listing and content fields before the customer-copy stage
- generating Claude handoff prompts from approved facts
- creating checklist reminders for missing listing elements

## What Remains Manual for Now

- final product quality review
- photo capture/staging
- platform posting actions
- customer messaging and negotiation
- final go/no-go on promotions
