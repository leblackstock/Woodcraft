# 12 Decision Log

Use this file to record major decisions so future sessions understand why the system is structured this way.

## Decision Table

| Date | Decision ID | Decision | Why | Impact | Owner/Approver |
|---|---|---|---|---|---|
| 2026-04-21 | DEC-001 | Facebook Marketplace set as primary sales channel | Best fit for low-budget local demand capture | Weekly execution prioritizes Marketplace listings first | Lauren |
| 2026-04-21 | DEC-002 | Facebook Page + Instagram set as support/trust channels | Supports credibility and content reuse without replacing core sales workflow | Content process anchored to repurposed listing assets | Lauren |
| 2026-04-21 | DEC-003 | Google Ads deferred to later phase for proven products only | Protects limited budget from early speculative spend | Ads restricted to controlled tests after organic proof | Lauren |
| 2026-04-21 | DEC-004 | Markdown-first planning architecture established before automation scripts | Prevents tool sprawl and improves consistency | Foundation created for later safe automation | Lauren |
| 2026-04-21 | DEC-005 | Prompt roadmap explicitly expanded to include image planning support | Product listings, social content, and later ad creative all need reusable image planning guidance | Prompt planning now covers listing, social, and ad image workflows | Lauren |
| 2026-04-21 | DEC-006 | Initial template/data-model alignment pass completed (later found incomplete; superseded by DEC-010) | The first scaffold needed a shared record baseline | Later audit showed operational fields and dual-model copy governance were not fully represented yet | Lauren |
| 2026-04-21 | DEC-007 | Starter profit floors added as temporary operating defaults | Pricing rules needed immediate usable guardrails before product-specific numbers exist | Products can be held, priced, or rejected with clearer interim thresholds | Lauren |
| 2026-04-21 | DEC-008 | Decision-log threshold clarified in governance rules | Change logging needed a precise threshold to prevent both drift and noisy over-logging | Governance now distinguishes log-worthy operating changes from routine cleanup | Lauren |
| 2026-04-21 | DEC-009 | GPT-5.4 set as workflow orchestrator and Claude set as exclusive final writer for customer-facing prose | The workspace needs a strict split between workflow control and final customer-copy generation | Final publishable customer copy must be produced by Claude, pasted back by the human, and then integrated before the workflow continues | Lauren |
| 2026-04-21 | DEC-010 | Data model expanded to match operational templates and add record-level Claude gate fields | Release-blocker audit found schema drift and no durable proof of final-copy completion | Listing/content records now track facts approval, copy status, handoff reference, Claude output reference, and publish readiness directly | Lauren |
| 2026-04-21 | DEC-011 | Completed weekly review instances stored in `90_archive/weekly_reviews/` | Recurring weekly records should not clutter root navigation | Root structure stays cleaner as operating cycles accumulate | Lauren |
