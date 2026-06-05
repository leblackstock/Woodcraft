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
- output format, structure, dimensions, file type, or aspect ratio
- quality criteria and final self-checks
- missing-information or blocked behavior

Only include the instructions relevant to that prompt. Standalone does not mean dumping entire repository files into every prompt.

## Brand-Specific Prompt Rule

For Drakkar-specific external prompts:

- Use `00_brand/` while preparing the prompt.
- Inline the relevant brand guidance into the delivered prompt.
- Name and describe the applicable voice mode instead of saying only `follow VOICE.md`.
- Include exact color hex values when color fidelity matters.
- Include the relevant typography direction when text appears in a graphic.
- Include the relevant visual direction when creating graphics or images.
- Include literal in-image text inside the copied prompt.
- Keep customer-facing claims within approved facts and the shared voice rules.

## Prompt-Type Requirements

### Image And Graphic Prompts

- Describe subject, composition, setting, lighting, materials, product shape, and intended use.
- Inline visual direction and exact palette values when applicable.
- Inline typography hierarchy and literal text for text-bearing graphics.
- Do not require Claude approval for image prompts, graphic prompts, overlay text, or literal in-image text.
- Include visible avoid rules.
- State aspect ratio or dimensions.
- Require supplied reference images when exact product fidelity depends on them.
- Do not claim text-only prompting can guarantee an exact product match.

### Writing And Claude Handoff Prompts

- Inline approved facts, requested fields, applicable voice mode, core voice rules, banned words/claims, channel context, and output format.
- Do not tell the external writer to open `00_brand/VOICE.md`, a listing record, a prep packet, or another local file.
- Treat local paths as internal provenance only; remove them from the delivered prompt unless the actual file contents are attached.
- Define missing-information behavior and prohibit invented facts.

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
- Output format and quality criteria are explicit.
- Missing-information behavior is explicit.
- The prompt asks for no unsupported or invented claims.
