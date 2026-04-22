# 11 Weekly Operations

Purpose: convert strategy into a repeatable weekly rhythm that survives low-energy weeks.

## Recommended Weekly Cadence

## Monday — Research + Prioritization

- Review local pricing/demand signals in [20_research/](20_research/)
- Update top product candidates in [30_products/](30_products/)
- Select 1–2 priority products for this week

## Tuesday — Spec / Build / Prep Day

- Lock the standard launch spec for the week's priority items
- Set the truthful `build_model` for each priority item (`Made to Order`, `In Stock`, or `Sample Built`)
- Build or prep priority items when useful, but do not treat a fresh build as a universal pre-list requirement
- Capture one raw verification evidence bundle (spec/dimensions note, current cost inputs, labor note, delivery/lead-time note, and media provenance note when needed)
- Confirm costs, labor time, margin assumptions, and lead-time logic in a live cost sheet or linked product record
- Capture progress notes for listing assets and any actual build learnings already available

## Wednesday — Listing Day

- Draft/refine Marketplace listings in [40_listings/](40_listings/)
- Use truthful made-to-order listing prep when a fresh build does not yet exist
- Assemble one bundled verification packet and escalate only true exceptions or blockers
- Finalize pricing, lead times, pickup/delivery terms, media-truth status, and approved facts only after the packet is approved
- If facts are complete, prepare Claude handoff and wait for human paste-back
- Integrate Claude final listing copy and set `publish_ready: Yes` only when the listing record is fully complete
- Publish listings (manual) only after `publish_ready: Yes` and human approval

## Thursday — Content Day

- Repurpose listings into Facebook Page + Instagram posts in [50_content/](50_content/)
- Prepare content facts and channel angle from approved listing records
- Run the Claude caption gate before any post becomes ready to schedule
- Queue simple follow-up content only after the content record is `publish_ready: Yes`

## Friday — Review + Improvement Day

- Start or update the current weekly review draft using [80_templates/weekly_review_template.md](80_templates/weekly_review_template.md) in `15_weekly_review_drafts/`
- Move the review into `90_archive/weekly_reviews/` only after the review period is actually complete
- If any made-to-order sale/build finished this week, capture actual receipts, labor, finished dimensions, finished photos, and pricing learnings before closing the week
- Log decisions in [12_DECISION_LOG.md](12_DECISION_LOG.md)
- Update [13_BACKLOG.md](13_BACKLOG.md) with next highest-value tasks

## Minimum-Viable Week (Low Energy Mode)

If capacity is low, execute only:

1. Complete verification packet + approved facts + Claude handoff for **one** Marketplace listing and publish only if the listing reaches `publish_ready: Yes`
2. Prepare **one** repurposed trust/support post and schedule/post it only if the Claude caption gate is complete
3. Perform **one** 20-minute weekly review and backlog reset

If the listing is `Made to Order`, the minimum-viable version may be a truthful listing-first packet rather than a fresh build.

This keeps momentum without burning out.

## Weekly Non-Negotiables

- Marketplace listing activity happens every week.
- At least one decision/learning is logged each week.
- Backlog is re-prioritized weekly.
- Upcoming or in-progress weekly review drafts stay in `15_weekly_review_drafts/`.
- Completed weekly review files are stored in `90_archive/weekly_reviews/`.
