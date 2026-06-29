# Social Brand-Post Cadence Tracker

Status: Active operational tracker
Timezone: America/New_York
Requirement decision: DEC-115
Minimum cadence: One Facebook Page brand post and one Instagram brand/support post per calendar day.

## Source Routing

- Brand source of truth: `00_brand/`
- Brand Post Mode voice: `00_brand/VOICE.md`
- Content workflow: `07_LISTING_AND_CONTENT_WORKFLOW.md`
- Content record template: `80_templates/social_post_template.md`
- Social brand-post rules: `50_content/facebook_brand_post_rules.md`
- Active social brand-post generator: `50_content/prompts/prompt_social_brand_post_generator_v2.0.md`
- Content records: `50_content/content_*.md`

## Cadence Rules

- Each America/New_York calendar day needs at least one Facebook Page brand post and one Instagram brand/support post.
- Track the Facebook Page and Instagram channel separately. A Facebook Page post does not satisfy the Instagram minimum, and an Instagram post does not satisfy the Facebook Page minimum.
- A dual `platform: FB Page + Instagram` content record may appear in both channel columns for the same date, but each channel still needs its own Claude output, readiness status, and manual publish/schedule evidence before that channel is satisfied.
- Use existing approved listing/product facts and governed media where possible; do not invent daily content just to fill the tracker.
- Final Facebook Page post copy and Instagram captions still require the Claude final-copy gate before the asset can become publish-ready, scheduled, or published.
- Draft, prep-only, and handoff-prepared work does not satisfy the daily minimum. It only shows the next action.
- Mark a channel `Published` only when the manual platform post is live and the linked content record has the actual `publish_date`.
- Mark a channel `Scheduled` only when the post is scheduled in-platform for that date and the linked content record has cleared the normal publish-ready gates.
- Use `Waived` only when Lauren explicitly waives that channel for the date, and record the reason in `Notes`.
- Use `Missed` when the day ends without a published, scheduled, or waived post for that channel.
- Keep final customer-facing prose out of this tracker; link the content record and Claude output instead.

## Status Values

- Channel status: `Unassigned`, `Draft`, `Handoff Prepared`, `Ready to Schedule`, `Scheduled`, `Published`, `Missed`, `Waived`.
- Daily status: `Not Planned`, `Not Met`, `Partially Met`, `Met`, `Waived`.

## Daily Log

| Date | Facebook Page record | Facebook Page status | Instagram record | Instagram status | Daily status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-06-24 | `content_social_usa1_l_nat_fourth_july_001` | Draft — Handoff Prepared | `content_social_usa1_l_nat_fourth_july_001` | Draft — Handoff Prepared | Not Met | Old queued candidates were unassigned. Replaced with one dual Facebook Page + Instagram feed package for the active USA1-L-NAT Wavy Wooden American Flag. Both channels still need Claude output pasted back, readiness checks, and manual publish/schedule evidence before the cadence is satisfied. |
