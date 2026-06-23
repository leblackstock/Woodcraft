# AGENTS.md

Guidance for any coding or automation agent working in this repository.

## Repository Priorities

1. Respect `00_START_HERE.md`, `01_VISION.md`, `03_GOVERNANCE.md`, and `04_BUSINESS_RULES.md`.
2. Keep the workspace markdown-first and process-first.
3. Prefer low-risk, auditable changes over clever shortcuts.

## Known Failure Modes To Avoid

This repository has already encountered these problems:

- PowerShell/PSReadLine crashes from long inline `python -c` commands.
- Commands stuck in multiline continuation mode (`>>`).
- Huge HTML/XML/JS dumps flooding the console.
- Re-running broad discovery steps instead of resuming from the last confirmed result.

Agents must actively avoid repeating those patterns.

## Command Safety Rules

- Do not use long inline Python in PowerShell.
- If logic is non-trivial, write a temporary script file and execute it.
- Do not use multiline shell input when a script or direct file edit is safer.
- Keep all commands non-interactive and bounded.
- Add timeouts to network requests where practical.
- If output could be large, redirect to a file and inspect only filtered results.

## Data Extraction Rules

- Never dump full HTML, XML, minified JS, or large JSON into the terminal.
- Use targeted extraction only.
- Prefer structured sources such as sitemaps, known files, or templates before noisy page scraping.
- Reuse already-established findings instead of re-fetching and reprinting them.

## File Update Rules

- Treat templates as field/schema references.
- Preserve existing document structure.
- Use explicit placeholders for unknowns rather than guessing.
- Record meaningful governance or workflow changes in `12_DECISION_LOG.md`.

## Brand Source of Truth

- `00_brand/` is the current source of truth for reusable Drakkar Designs identity guidance and approved assets, including `VOICE.md`, `COLOR_PALETTE.md`, `TEXT_STYLE_RULES.md`, `VISUAL_STYLE.md`, logos, approved product photos, and provenance.
- Use the one shared voice in `00_brand/VOICE.md` and name its applicable Catalog, Brand Post, Marketplace, or Customer Reply mode. Do not create competing channel voice guides or let a mode override core voice and approved-fact rules.
- Reusable brand-specific guidance belongs in `00_brand/`. Operational records stay in their workflow folders and point to the relevant brand files.
- Any workflow that creates brand-specific text, graphics, ads, copy, images, HTML, templates, prompt packs, or generated visuals must reference `00_brand/` before using brand identity or assets.

## Copy and Publishing Rules

- Final customer-facing prose must come from Claude, per repo governance.
- Other agents may prepare facts, outlines, and validation only.
- Image graphic text is the exception when an active review-by-exception image workflow assigns it to GPT/Codex. It does not require Claude approval, but it must use approved facts and the applicable voice mode.

## Standalone External Prompt Rules

- Every prompt intended to be copied, pasted, uploaded, or sent to an AI/tool outside this repository must pass `80_templates/standalone_external_prompt_checklist.md`.
- Use repository files while preparing the prompt, then inline all relevant context, facts, brand guidance, voice rules, palette values, typography/visual direction, literal required text, constraints, reference instructions, output format, quality criteria, and failure behavior into the delivered prompt. For image and graphic prompts, choose the background color or photo/overlay background treatment first, then list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields.
- Do not expect an external target to open repository paths, know prior chat context, read another prompt, or infer undocumented shorthand.
- If exact fidelity requires an attachment or reference image, state that requirement explicitly.
- If an image prompt requires an attached image, the first line of the copied prompt must be `Please see attached "[plain-language item being attached]"` so the operator knows what to attach before generation.

## Image Prompt Rules

- Do not assume text should be excluded from image prompts.
- When the requested image needs readable text, labels, signage, branding, catalog marks, price tags, captions, package text, or other literal words inside the image, keep that text in the prompt and make it explicit.
- ChatGPT Image 2 is considered capable for text-bearing image generation in this workflow. Do not apply older generic advice that image models cannot or should not render words.
- Only remove text from an image prompt when the user explicitly asks for a text-free image or when the target workflow is documented as not supporting text.

## Daily Session Briefing

- On the first substantive response in each chat, run python 60_automation/workspace_maintenance/session_repo_briefing.py --status.
- If due, the notice must tell the user to reply "Brief me" to generate the briefing.
- If today’s America/New_York briefing is due, say once that it is due and continue the user’s actual request. Do not repeat the notice in the same chat.
- Treat "Brief me" as explicit confirmation to run --write. Paste the complete printed briefing into chat as an addition to the requested work; a saved report alone is insufficient.
- If the briefing is current, continue normally without replaying it unless the user explicitly asks for the daily briefing.

## Workspace Maintenance

- Default repository searches exclude `90_archive/` and `deprecated/` paths through the root .ignore file. Search them only when historical material is explicitly requested, using `rg --no-ignore`.
- For deliberate cleanup, read `60_automation/workspace_maintenance/workspace_maintenance_prompt.md` and run the read-only audit before changing records.
- Keep one canonical owner for active rules and use short pointers elsewhere. Preserve complete intentional copies in agent instructions, schemas, templates, and standalone external prompts.
- Automatically repair only generated indexes, clear relative links, archive-ledger pointers, and obvious encoding in editable canonical files. Escalate factual or policy conflicts, published records, customer copy, raw source evidence, and uncertain archive decisions.

## Preferred Working Style

1. Read the relevant source-of-truth file(s).
2. Confirm the last known good state.
3. Use the smallest safe action that advances the task.
4. Keep outputs short and useful.
5. Verify completion against the actual user request.
