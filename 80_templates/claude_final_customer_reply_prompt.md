# Claude Final Customer Reply Prompt Template

Use this template when Claude is needed to write a final customer-facing reply or message.

## Response Context

- response_scenario:
- channel:
- current_asset:

## Fields Needed

- final_reply:

## Approved Facts Only

- approved_facts:
- things_that_must_be_said:
- things_that_must_not_be_said:

## Tone and Fallback

- tone:
- preapproved_fallback_reply:

## Hard Rules

- Write only the final customer-facing reply.
- Use approved facts only.
- Do not invent pricing, availability, timelines, policies, or commitments.
- Use fallback language only if it is preapproved, fact-safe, and does not imply missing facts.
- Do not add explanations outside the reply itself.

## Output-Only Rule

- If information is sufficient, return only the final reply.

## Missing-Info Behavior

- Use fallback only when the preapproved safe language can acknowledge the gap without inventing or implying missing facts.
- If required facts are needed for a normal final reply, return only:
  - status: BLOCKED
  - missing_info: