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

## Brand Asset Source of Truth

- Use `00_brand/` as the current source of truth for Drakkar Designs logos, approved product photos, palette notes, and brand asset provenance.
- Any workflow or prompt work that creates brand-specific text, graphics, ads, copy, images, HTML, templates, prompt packs, or generated visuals must reference `00_brand/`.

## Copy Boundary

- Final customer-facing prose must come from Claude, per repo governance.
- Codex may prepare facts, outlines, validation notes, workflow state, and image prompt drafts unless the task crosses into final publishable customer copy.
