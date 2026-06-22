# 14 Glossary

Use these definitions consistently across this workspace.

## Core Terms

- **Primary Channel**: The channel where most sales effort and execution time goes (currently Facebook Marketplace).
- **Support Channel**: A channel that builds trust/awareness and supports conversion indirectly (Facebook Page, Instagram).
- **Product Candidate**: An item under evaluation before approval for regular build/listing.
- **Approved Product**: A product that passed scoring and business guardrails and is ready for listing workflow.
- **Listing Packet**: Complete listing-ready set (title, description, price, photos, terms, CTA, FAQs).
- **Organic Proof**: Non-paid signs of demand (messages, saves, sales, repeat inquiries).
- **Tiny-Budget Test**: Controlled ad experiment with strict spend cap and stop rule.
- **Margin Guardrail**: Minimum profitability threshold that must be met before listing/scaling.
- **Decision Trail**: Documented record of key choices and rationale (see [12_DECISION_LOG.md](12_DECISION_LOG.md)).

## Workflow Terms

- **Intake**: Capturing a new product idea in structured format.
- **Scoring**: Evaluating product viability using defined dimensions/rubric.
- **Hold**: Candidate paused pending missing information or constraints.
- **Queue**: Prioritized sequence of approved tasks/products to execute.
- **Low-Energy Week**: Reduced-capacity week where minimum viable operations are followed.
- **Approved Facts**: Product/listing/content facts that have been checked enough to support a valid Claude handoff without invention.
- **Claude Gate**: Required stop where final customer-facing prose must be handed to Claude before publish-ready status is allowed.
- **Customer Copy Status**: Governed record state showing whether customer-facing prose is still prep-only, handoff-ready, pasted back, or fully integrated.
- **Copy Provenance**: The record trail showing which handoff and pasted-back Claude output produced the final customer-facing prose.
- **Publish Ready**: Record state showing an asset may proceed to manual publish/schedule review because facts, final copy, and required fields are complete.
- **Publish Status**: Operational state label for the asset. It may not imply readiness, scheduling, or publication ahead of the Claude gate and `publish_ready`.
- **Historical Operator Evidence**: Audit-only status for an already-published asset whose visible copy and publication evidence were captured after the fact, but whose Claude output was not recorded. It cannot be used for new, revised, scheduled, or republished work.
- **Weekly Review Draft**: Upcoming or in-progress weekly review record kept outside the completed archive until the review period is actually complete.
- **Pilot Build**: An initial repeatable build being validated. It is not current inventory and must never support an in-stock claim.
- **Configurable Product Family**: The parent record for a repeatable product with separately priced standard choices. It owns the stable `product_id`, catalog ID, and shared facts.
- **Variant**: A permanent, separately priced standard option inside a configurable product family. It uses its own `variant_id` and `variant_code`, not its own catalog ID.
- **Variant Scope**: The exact set of active Variant codes included in one non-bundle listing or product-family showcase.
- **Scope Reference**: A grouped clean reference that shows exactly a declared variant scope. It supplements rather than replaces each Variant's individual clean reference and activation evidence.

## Automation Terms

- **Manual**: Human does the step end-to-end.
- **Semi-Automated**: AI/tools assist preparation, but human approves and executes key actions.
- **Fully Automated**: System executes without manual intervention (not default in this workspace).
