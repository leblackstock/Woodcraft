# CODEX.md

Guidance for Codex when working in this repository.

## Source Files

- Follow `AGENTS.md` for shared agent behavior.
- Follow `00_START_HERE.md`, `01_VISION.md`, `03_GOVERNANCE.md`, and `04_BUSINESS_RULES.md` before making strategic or workflow changes.
- Keep work markdown-first, bounded, and auditable.

## Image Prompt Text Rule

- Do not assume text should be excluded from image prompts.
- When the requested image should contain readable words, labels, signage, branding, catalog marks, price text, captions, packaging text, or other literal text, include that text directly in the prompt.
- ChatGPT Image 2 is considered capable for text-bearing image generation in this workflow. Do not remove requested text based on generic older image-model guidance.
- Remove or avoid in-image text only when the user explicitly asks for a text-free image, the text is not approved for the intended customer-facing use, or the target image tool is documented as unable to render it.

## Brand Source of Truth

- Use `00_brand/` as the current source of truth for reusable Drakkar Designs identity guidance and approved assets, including `VOICE.md`, `COLOR_PALETTE.md`, `TEXT_STYLE_RULES.md`, `VISUAL_STYLE.md`, logos, approved product photos, and provenance.
- Use the one shared voice in `00_brand/VOICE.md` and name its applicable Catalog, Brand Post, Marketplace, or Customer Reply mode. Do not create competing channel voice guides or let a mode override core voice and approved-fact rules.
- Move reusable brand-specific guidance into `00_brand/`; keep operational records in their workflow folders and point them to the relevant brand files.
- Any workflow or prompt work that creates brand-specific text, graphics, ads, copy, images, HTML, templates, prompt packs, or generated visuals must reference `00_brand/`.

## Copy Boundary

- Final customer-facing prose must come from Claude, per repo governance.
- Codex may prepare facts, outlines, validation notes, workflow state, and image prompt drafts unless the task crosses into final publishable customer copy.
- Codex may create image graphic text when an active review-by-exception image workflow assigns it that responsibility. Use approved facts and the applicable voice mode; do not request Claude approval for that image graphic text.

## Standalone External Prompt Rule

- Any prompt Codex creates for use outside this repository must pass `80_templates/standalone_external_prompt_checklist.md`.
- Local files are preparation sources only. Inline the relevant facts, instructions, brand rules, required text, constraints, inputs/attachments, output format, quality criteria, and failure behavior before delivering the prompt. For image and graphic prompts, choose the background color or photo/overlay background treatment first, then list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields.
- Never make an external prompt depend on repository paths, prior chat context, surrounding notes, another prompt, or undocumented shorthand.
- When a copied image prompt requires an attached image, make the first line `Please see attached "[plain-language item being attached]"` so the attachment requirement is visible before the user pastes the prompt into ChatGPT Image 2 or another image tool.

## Daily Session Briefing

- On the first substantive response in each chat, run python 60_automation/workspace_maintenance/session_repo_briefing.py --status.
- If due, the notice must tell the user to reply "Brief me" to generate the briefing.
- If today’s America/New_York briefing is due, issue one concise due notice while continuing the user’s request; do not repeat it during the chat.
- Treat "Brief me" as explicit confirmation to run --write and paste the complete printed briefing into chat in addition to the requested work.
- A daily briefing is read-only operational context. It must not publish, schedule, create customer copy, reprioritize work, or create policy/learning entries.

## Workspace Maintenance

- Default searches exclude `90_archive/` and `deprecated/`; use `rg --no-ignore` only when the task specifically needs historical material.
- Use `60_automation/workspace_maintenance/workspace_maintenance_prompt.md` for a deliberate maintenance pass and run its audit before changing workflow files.
- Consolidate accidental active duplication into canonical owners and short pointers. Keep required complete copies in separate agent rules, schemas, templates, and standalone external prompts.
- Limit automatic repairs to generated indexes, clear links, archive pointers, and obvious encoding in editable canonical files. Escalate policy/fact conflicts, source evidence, published records, customer copy, and uncertain archival choices.
