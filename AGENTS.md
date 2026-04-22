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

## Copy and Publishing Rules

- Final customer-facing prose must come from Claude, per repo governance.
- Other agents may prepare facts, outlines, and validation only.

## Preferred Working Style

1. Read the relevant source-of-truth file(s).
2. Confirm the last known good state.
3. Use the smallest safe action that advances the task.
4. Keep outputs short and useful.
5. Verify completion against the actual user request.