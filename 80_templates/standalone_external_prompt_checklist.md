# Standalone External Prompt Checklist

Status: Active reusable checklist
Purpose: ensure every prompt intended for an AI or tool outside this repository contains everything needed for the highest-quality result without repository access

Use this checklist whenever a workflow creates a prompt that will be copied, pasted, uploaded, or sent to Claude, ChatGPT, an image model, a research AI, an automation service, or any other external system.

Internal source files remain the preparation source of truth. The delivered external prompt must inline the relevant instructions and facts from those files instead of expecting the target system to read local paths.

## Standalone Rule

A delivered external prompt must work when received alone, apart from any explicitly required attachments or source text supplied with it.

The prompt must not depend on:

- repository paths
- file names the target system cannot open
- prior chat context
- another prompt in the same pack
- unnamed brand guidance
- separate exact-text fields
- undocumented shorthand
- assumptions about the target model already knowing Drakkar Designs

## Required Prompt Contents

Include everything relevant to the task:

- role and objective
- target output or deliverable
- audience, channel, and use case
- approved source facts and supplied inputs
- applicable brand voice mode and the actual relevant voice rules
- applicable visual style, exact palette values, and typography rules
- literal required text, labels, wording, or data
- truthfulness, safety, and prohibited-claim constraints
- visible avoid rules or negative instructions
- required attachments or reference-image instructions
- for image prompts requiring attachments, a first prompt line that says `Please see attached "[plain-language item being attached]"`
- output format, structure, dimensions, file type, or aspect ratio
- quality criteria and final self-checks
- failure behavior when the target can safely act on it

Only include the instructions relevant to that prompt. Standalone does not mean dumping entire repository files into every prompt.

## Brand-Specific Prompt Rule

For Drakkar-specific external prompts:

- Use `00_brand/` while preparing the prompt.
- Inline the relevant brand guidance into the delivered prompt.
- Name and describe the applicable voice mode instead of saying only `follow VOICE.md`.
- Include exact color hex values when color fidelity matters.
- For image or graphic prompts, choose and state the actual background color or photo/overlay background treatment first.
- After the background choice, list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields.
- Include the relevant typography direction when text appears in a graphic.
- Include the relevant visual direction when creating graphics or images.
- Include literal in-image text inside the copied prompt.
- Keep customer-facing claims within approved facts and the shared voice rules.

## Prompt-Type Requirements

### Image And Graphic Prompts

- Describe subject, composition, setting, lighting, materials, product shape, and intended use.
- Inline visual direction and exact palette values when applicable.
- State the background color or background treatment first when the prompt includes brand colors.
- Do not tell the image model which palette color to use where except for the chosen background.
- Inline typography hierarchy and literal text for text-bearing graphics.
- Do not require Claude approval for image prompts, graphic prompts, overlay text, or literal in-image text.
- Include only short, concrete, visually checkable avoid rules. Do not add internal repo labels, pricing-policy explanations, or style-category lists the target model would not otherwise know.
- State aspect ratio or dimensions.
- Require supplied reference images when exact product fidelity depends on them.
- When an attached image is required, begin the copied prompt with `Please see attached "[plain-language item being attached]"`.
- Do not claim text-only prompting can guarantee an exact product match.
- For Facebook Marketplace listing images, exact product fidelity is always required. Require the approved catalog image or reference image attachment and stop instead of delivering a text-only approximation when the attachment is missing.
- For Facebook Marketplace price-card graphics, use one plain selling-price line from the approved FBM price. For a non-bundle variant-scope listing with different approved option prices, use one clear option-and-price chart listing every included variant and its exact approved price instead. In copied image prompts, specify the exact rendered text instead of explaining internal labels or retail-comparison exceptions.

### Writing And Claude Handoff Prompts

- Inline approved facts, requested fields, applicable voice mode, core voice rules, banned words/claims, channel context, and copy-shape guidance.
- For Claude final-copy prompts, include negative style rules: no em dashes or en dashes in final output, regular hyphens are okay when needed, and no AI-isms or common AI tells.
- For Claude final-copy prompts, instruct Claude to silently write several internal versions, analyze them, and then produce a stronger final version as the visible output.
- Do not tell the external writer to open `00_brand/VOICE.md`, a listing record, a prep packet, or another local file.
- Treat local paths as internal provenance only; remove them from the delivered prompt unless the actual file contents are attached.
- Resolve missing facts upstream before Claude handoff; prohibit invented facts instead of asking Claude to return blocked or missing-information fields.

### Research And Analysis Prompts

- State the research question, scope, geography, time window, allowed sources, evidence standard, and required output structure.
- Include known facts and exclusions.
- Require citations or source links when needed.
- State how uncertainty, missing evidence, and conflicting sources should be handled.

### Automation And Transformation Prompts

- Include the input schema, output schema, transformation rules, validation rules, examples when useful, and failure behavior.
- Do not rely on local templates or schemas unless their needed contents are embedded or attached.

## Delivery Gate

Before delivering or saving an external prompt, verify:

- It can be executed without repository access.
- All required facts and instructions are inside the prompt or explicitly attached.
- No local path is presented as an instruction to the target system.
- No required context exists only in surrounding notes.
- Required literal text is inside the copied prompt.
- Brand, voice, palette, typography, and visual rules are inlined when relevant.
- Image and graphic prompts explicitly choose the background color or photo/overlay background treatment.
- Remaining palette colors are listed without role assignments.
- Any image prompt that requires an attached image begins with `Please see attached "[plain-language item being attached]"`.
- Output format and quality criteria are explicit when relevant to the prompt type.
- Failure behavior is explicit for image, research, automation, or transformation prompts when relevant.
- The prompt asks for no unsupported or invented claims.
- Claude final-copy prompts include the no-em-dash/no-en-dash rule, the no-AI-isms rule, and the internal draft/analyze/improve instruction.
