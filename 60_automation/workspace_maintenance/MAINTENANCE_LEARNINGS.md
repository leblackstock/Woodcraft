# Maintenance Learnings

Record only confirmed recurring patterns. A maintenance audit may draft an entry, but a new durable rule requires verification and operator approval.

Last decision reviewed: `DEC-099`

## Entry Format

### YYYY-MM-DD — Short pattern name

- Observed pattern:
- Canonical source:
- Durable pointer or rule:
- Evidence:
- Follow-up:

## Confirmed Learnings

### 2026-06-22 — Classify required repetition before consolidating

- Observed pattern: the first live-workspace audit found repeated guidance across agent rules, schemas, templates, and standalone prompts.
- Canonical source: `60_automation/workspace_maintenance/RULE_OWNERSHIP_MAP.md`.
- Durable pointer or rule: reduce only accidental active duplicates; retain complete context where a separate agent tool, schema, template, or external target cannot follow a repository pointer.
- Evidence: `90_archive/maintenance_audits/maintenance_audit_2026-06-22_162507.md`; DEC-096.
- Follow-up: review new duplicate findings during the weekly maintenance pass and promote only verified recurring patterns.
