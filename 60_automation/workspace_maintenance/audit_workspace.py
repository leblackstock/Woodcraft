#!/usr/bin/env python3
"""Read-only integrity audit for the live Woodcraft workspace.

Default scans exclude 90_archive and deprecated paths. Use --include-archive
only when historical material is explicitly in scope. --write-report creates a
dated historical report, refreshes the current maintenance-status pointer, and
persists the workflow package-trace baseline.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ARCHIVE_DIRS = {"90_archive", "deprecated", ".git", "__pycache__"}
TRACE_BASELINE_NAME = "WORKFLOW_TRACE_BASELINE.json"
GENERATED_MAINTENANCE_NAMES = {
    "ASSET_LOCATOR.md",
    "CURRENT_MAINTENANCE_STATUS.md",
    "LEARNING_REVIEW.md",
    "LIVE_FILE_MAP.md",
    "RULE_OWNERSHIP_MAP.md",
    "SESSION_BRIEFING_STATUS.md",
    TRACE_BASELINE_NAME,
}
GOVERNANCE_ROOTS = (
    "00_START_HERE.md",
    "01_VISION.md",
    "03_GOVERNANCE.md",
    "04_BUSINESS_RULES.md",
)
IMPORTANT_FILES = {
    "00_START_HERE.md",
    "01_VISION.md",
    "02_INDEX.md",
    "03_GOVERNANCE.md",
    "04_BUSINESS_RULES.md",
    "06_PRODUCT_DECISION_WORKFLOW.md",
    "07_LISTING_AND_CONTENT_WORKFLOW.md",
    "08_AUTOMATION_ROADMAP.md",
    "09_DATA_MODEL.md",
    "10_PROMPTS_INDEX.md",
    "11_WEEKLY_OPERATIONS.md",
    "AGENTS.md",
    "CODEX.md",
    "CLAUDE.md",
    ".cursorrules",
    ".clinerules",
    "40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md",
    "50_content/facebook_brand_post_rules.md",
    "80_templates/standalone_external_prompt_checklist.md",
}
IMPORTANT_PREFIXES = (
    "00_brand/",
    "40_listings/prompts/",
    "80_templates/",
    "60_automation/workspace_maintenance/",
)
WORKFLOW_ROOT_FILES = {
    "00_START_HERE.md",
    "01_VISION.md",
    "02_INDEX.md",
    "03_GOVERNANCE.md",
    "04_BUSINESS_RULES.md",
    "05_CHANNEL_STRATEGY.md",
    "06_PRODUCT_DECISION_WORKFLOW.md",
    "07_LISTING_AND_CONTENT_WORKFLOW.md",
    "08_AUTOMATION_ROADMAP.md",
    "09_DATA_MODEL.md",
    "10_PROMPTS_INDEX.md",
    "11_WEEKLY_OPERATIONS.md",
    "AGENTS.md",
    "CODEX.md",
    "CLAUDE.md",
}
MAINTENANCE_WORKFLOW_FILES = {
    "README.md",
    "audit_workspace.md",
    "run_weekly_maintenance.md",
    "session_repo_briefing.md",
    "workspace_maintenance_prompt.md",
}
OPERATIONAL_WORKFLOW_PREFIXES = (
    "30_products/",
    "40_listings/",
    "50_content/",
    "70_ads/",
)
INSTANCE_PREFIXES = ("prod_", "cost_", "spec_", "variant_", "list_", "content_")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
RETIRED_STATUS = re.compile(
    r"^(?:Status|Use status):\s*(?:Deprecated|Retired|Superseded)\b",
    re.IGNORECASE | re.MULTILINE,
)
MOJIBAKE = re.compile(r"[\u00c3\u00e2\ufffd]")


@dataclass(frozen=True)
class Finding:
    category: str
    path: str
    detail: str
    severity: str = "warning"
    line: int | None = None


@dataclass(frozen=True)
class LinkReference:
    source: str
    target: str
    line: int
    resolved: str | None
    is_broken: bool


@dataclass(frozen=True)
class WorkflowChange:
    path: str
    change_type: str
    previous_path: str | None = None


@dataclass
class PackageTrace:
    change: WorkflowChange
    members: dict[str, set[str]]
    link_evidence: list[LinkReference]
    retired_members: set[str]
    findings: list[Finding]


@dataclass
class WorkflowTraceResult:
    baseline_exists: bool
    fingerprints: dict[str, str]
    changes: list[WorkflowChange]
    packages: list[PackageTrace]
    findings: list[Finding]


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_excluded(path: Path, root: Path, include_archive: bool) -> bool:
    if include_archive:
        return False
    parts = set(path.relative_to(root).parts)
    return bool(parts & ARCHIVE_DIRS)


def markdown_files(root: Path, include_archive: bool = False) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if not is_excluded(path, root, include_archive):
            yield path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def resolve_link(source: Path, target: str) -> Path | None:
    target = target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    return (source.parent / target).resolve()


def markdown_link_references(root: Path, path: Path) -> list[LinkReference]:
    references: list[LinkReference] = []
    content = read_text(path)
    source = rel(path, root)
    for match in MARKDOWN_LINK.finditer(content):
        target = match.group(1)
        resolved_path = resolve_link(path, target)
        line = content.count("\n", 0, match.start()) + 1
        is_broken = resolved_path is not None and not resolved_path.exists()
        resolved: str | None = None
        if resolved_path is not None and resolved_path.exists():
            try:
                resolved = rel(resolved_path, root)
            except ValueError:
                resolved = None
        references.append(LinkReference(source, target, line, resolved, is_broken))
    return references


def find_broken_links(root: Path, include_archive: bool) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root, include_archive):
        for reference in markdown_link_references(root, path):
            if reference.is_broken:
                findings.append(
                    Finding(
                        "broken-relative-link",
                        reference.source,
                        reference.target,
                        "error",
                        reference.line,
                    )
                )
    return findings


def find_retired_files(root: Path, include_archive: bool) -> dict[str, Path]:
    retired: dict[str, Path] = {}
    for path in markdown_files(root, include_archive):
        if RETIRED_STATUS.search(read_text(path)):
            retired[rel(path, root)] = path
    return retired


def find_retired_references_in_paths(
    root: Path,
    paths: Iterable[Path],
    retired: dict[str, Path],
) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        content = read_text(path)
        current = rel(path, root)
        linked_retired_paths: set[str] = set()
        for reference in markdown_link_references(root, path):
            if reference.resolved in retired and reference.resolved != current:
                findings.append(
                    Finding(
                        "retired-reference",
                        current,
                        reference.resolved,
                        "warning",
                        reference.line,
                    )
                )
                linked_retired_paths.add(reference.resolved)
        for retired_path in retired:
            if retired_path == current or retired_path in linked_retired_paths:
                continue
            position = content.find(retired_path)
            if position >= 0:
                line = content.count("\n", 0, position) + 1
                findings.append(Finding("retired-reference", current, retired_path, "warning", line))
    return findings


def find_retired_references(
    root: Path,
    retired: dict[str, Path],
    include_archive: bool,
) -> list[Finding]:
    return find_retired_references_in_paths(root, markdown_files(root, include_archive), retired)


def find_mojibake(root: Path, include_archive: bool) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root, include_archive):
        content = read_text(path)
        if MOJIBAKE.search(content):
            relative = rel(path, root)
            if "/source/" in relative:
                continue
            findings.append(
                Finding(
                    "possible-mojibake",
                    relative,
                    "UTF-8 decoding artifacts detected",
                    "error",
                )
            )
    return findings


def is_important(path_text: str) -> bool:
    return path_text in IMPORTANT_FILES or path_text.startswith(IMPORTANT_PREFIXES)


def normalized_long_line_locations(path: Path) -> dict[str, list[int]]:
    locations: dict[str, list[int]] = defaultdict(list)
    for line_number, line in enumerate(read_text(path).splitlines(), start=1):
        clean = re.sub(r"\s+", " ", line.strip())
        if len(clean) >= 100 and not clean.startswith(("|", chr(96) * 3)):
            locations[clean].append(line_number)
    return locations


def normalized_long_lines(path: Path) -> set[str]:
    return set(normalized_long_line_locations(path))


def duplicate_classification(paths: list[str]) -> tuple[str, str]:
    agent_files = {"AGENTS.md", "CODEX.md", "CLAUDE.md", ".cursorrules", ".clinerules"}
    if set(paths) & agent_files:
        return "intentional agent-specific instruction copy", "info"
    if any(path.startswith("80_templates/") or "/prompts/" in path for path in paths):
        return "intentional standalone or template copy", "info"
    return "review: choose canonical owner or reduce to a pointer", "warning"


def find_duplicate_guidance(root: Path, include_archive: bool) -> list[Finding]:
    by_line: dict[str, list[str]] = defaultdict(list)
    for path in markdown_files(root, include_archive):
        relative = rel(path, root)
        if is_important(relative):
            for line in normalized_long_lines(path):
                by_line[line].append(relative)
    findings: list[Finding] = []
    for line, paths in sorted(by_line.items()):
        unique_paths = sorted(set(paths))
        if len(unique_paths) > 1:
            classification, severity = duplicate_classification(unique_paths)
            detail = f"{classification} | {line[:180].rstrip()}"
            findings.append(Finding("repeated-guidance", "; ".join(unique_paths), detail, severity))
    return findings


def is_workflow_document(path_text: str) -> bool:
    if path_text in WORKFLOW_ROOT_FILES:
        return True
    if path_text.startswith("00_brand/"):
        return True
    if "/prompts/" in f"/{path_text}":
        return True
    if path_text.startswith("80_templates/"):
        return True
    maintenance_prefix = "60_automation/workspace_maintenance/"
    if path_text.startswith(maintenance_prefix):
        name = Path(path_text).name
        return name in MAINTENANCE_WORKFLOW_FILES and name not in GENERATED_MAINTENANCE_NAMES
    if not path_text.startswith(OPERATIONAL_WORKFLOW_PREFIXES):
        return False
    name = Path(path_text).name
    is_named_workflow = (
        name.endswith("_workflow.md")
        or name.endswith("_rules.md")
        or "rollout" in name
        or "handoff_prep" in name
    )
    if name.startswith(INSTANCE_PREFIXES) and not name.endswith(("_workflow.md", "_rules.md")):
        return False
    return is_named_workflow


def workflow_markdown_files(root: Path) -> list[Path]:
    return [
        path
        for path in markdown_files(root, False)
        if is_workflow_document(rel(path, root))
    ]


def workflow_fingerprints(root: Path) -> dict[str, str]:
    return {
        rel(path, root): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in workflow_markdown_files(root)
    }


def workflow_trace_baseline_path(root: Path) -> Path:
    return root / "60_automation" / "workspace_maintenance" / TRACE_BASELINE_NAME


def load_workflow_trace_baseline(root: Path) -> dict[str, str] | None:
    path = workflow_trace_baseline_path(root)
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    files = payload.get("files")
    if payload.get("schema_version") != 1 or not isinstance(files, dict):
        raise ValueError(f"Invalid workflow trace baseline: {rel(path, root)}")
    if not all(isinstance(name, str) and isinstance(digest, str) for name, digest in files.items()):
        raise ValueError(f"Invalid workflow trace baseline: {rel(path, root)}")
    return dict(files)


def write_workflow_trace_baseline(root: Path, fingerprints: dict[str, str]) -> Path:
    path = workflow_trace_baseline_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "files": dict(sorted(fingerprints.items())),
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def classify_workflow_changes(
    previous: dict[str, str] | None,
    current: dict[str, str],
) -> list[WorkflowChange]:
    if previous is None:
        return [WorkflowChange(path, "initial") for path in sorted(current)]

    previous_only = set(previous) - set(current)
    current_only = set(current) - set(previous)
    changes: list[WorkflowChange] = []

    for path in sorted(set(previous) & set(current)):
        if previous[path] != current[path]:
            changes.append(WorkflowChange(path, "modified"))

    matched_previous: set[str] = set()
    previous_by_hash: dict[str, list[str]] = defaultdict(list)
    for path in previous_only:
        previous_by_hash[previous[path]].append(path)
    for paths in previous_by_hash.values():
        paths.sort()

    for path in sorted(current_only):
        matches = previous_by_hash.get(current[path], [])
        previous_path = next((candidate for candidate in matches if candidate not in matched_previous), None)
        if previous_path is None:
            changes.append(WorkflowChange(path, "added"))
        else:
            matched_previous.add(previous_path)
            changes.append(WorkflowChange(path, "renamed", previous_path))

    for path in sorted(previous_only - matched_previous):
        changes.append(WorkflowChange(path, "removed"))
    priority = {"added": 0, "modified": 1, "renamed": 2, "removed": 3}
    return sorted(changes, key=lambda change: (priority[change.change_type], change.path))


def build_live_link_index(
    root: Path,
    live_paths: dict[str, Path],
) -> tuple[dict[str, list[LinkReference]], dict[str, list[LinkReference]]]:
    outgoing: dict[str, list[LinkReference]] = {}
    incoming: dict[str, list[LinkReference]] = defaultdict(list)
    for source, path in live_paths.items():
        references = markdown_link_references(root, path)
        outgoing[source] = references
        for reference in references:
            if reference.resolved in live_paths:
                incoming[reference.resolved].append(reference)
    return outgoing, incoming


def find_package_duplicate_guidance(
    root: Path,
    member_paths: Iterable[str],
) -> list[Finding]:
    by_line: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for path_text in sorted(path for path in member_paths if is_workflow_document(path)):
        path = root / path_text
        for line, locations in normalized_long_line_locations(path).items():
            by_line[line].extend((path_text, location) for location in locations)
    findings: list[Finding] = []
    for line, locations in sorted(by_line.items()):
        paths = sorted({path for path, _ in locations})
        if len(paths) < 2:
            continue
        classification, severity = duplicate_classification(paths)
        if severity == "info":
            continue
        evidence = ", ".join(f"{path}:{line_number}" for path, line_number in locations)
        findings.append(
            Finding(
                "package-repeated-guidance",
                "; ".join(paths),
                f"{classification} | line evidence: {evidence} | {line[:140].rstrip()}",
                severity,
            )
        )
    return findings


def build_package_trace(
    root: Path,
    change: WorkflowChange,
    live_paths: dict[str, Path],
    outgoing: dict[str, list[LinkReference]],
    incoming: dict[str, list[LinkReference]],
    retired: dict[str, Path],
) -> PackageTrace:
    members: dict[str, set[str]] = defaultdict(set)
    for path_text in GOVERNANCE_ROOTS:
        if path_text in live_paths:
            members[path_text].add("governance root")
    members[change.path].add("changed workflow document")

    link_evidence: list[LinkReference] = []
    queued = [change.path]
    traversed: set[str] = set()
    while queued:
        source = queued.pop(0)
        if source in traversed:
            continue
        traversed.add(source)
        for reference in outgoing.get(source, []):
            if reference.resolved not in live_paths:
                continue
            target = reference.resolved
            if target not in members:
                queued.append(target)
            members[target].add(f"outbound link from {source}")
            link_evidence.append(reference)

    for reference in incoming.get(change.path, []):
        members[reference.source].add("direct inbound link")
        link_evidence.append(reference)

    member_paths = sorted(members)
    findings: list[Finding] = []
    for path_text in member_paths:
        for reference in outgoing.get(path_text, []):
            if reference.is_broken:
                findings.append(
                    Finding(
                        "package-broken-relative-link",
                        reference.source,
                        reference.target,
                        "error",
                        reference.line,
                    )
                )
    findings.extend(
        find_retired_references_in_paths(
            root,
            (live_paths[path_text] for path_text in member_paths),
            retired,
        )
    )
    findings.extend(find_package_duplicate_guidance(root, member_paths))
    return PackageTrace(
        change=change,
        members=dict(members),
        link_evidence=sorted(
            link_evidence,
            key=lambda item: (item.source, item.line, item.target),
        ),
        retired_members=set(member_paths) & set(retired),
        findings=findings,
    )


def build_workflow_trace(root: Path) -> WorkflowTraceResult:
    baseline = load_workflow_trace_baseline(root)
    fingerprints = workflow_fingerprints(root)
    changes = classify_workflow_changes(baseline, fingerprints)
    live_paths = {rel(path, root): path for path in markdown_files(root, False)}
    outgoing, incoming = build_live_link_index(root, live_paths)
    retired = find_retired_files(root, False)
    packages: list[PackageTrace] = []
    findings: list[Finding] = []
    for change in changes:
        if change.change_type == "removed":
            findings.append(
                Finding(
                    "workflow-file-removed",
                    change.path,
                    "Removed since the prior workflow-trace baseline; confirm a Deprecated, Retired, or Superseded lifecycle and archive-ledger entry.",
                )
            )
            continue
        packages.append(build_package_trace(root, change, live_paths, outgoing, incoming, retired))
    findings.extend(finding for package in packages for finding in package.findings)
    return WorkflowTraceResult(
        baseline_exists=baseline is not None,
        fingerprints=fingerprints,
        changes=changes,
        packages=packages,
        findings=findings,
    )


def finding_location(finding: Finding) -> str:
    if finding.line is None:
        return finding.path
    return f"{finding.path}:{finding.line}"


def unique_findings(findings: Iterable[Finding]) -> list[Finding]:
    unique: list[Finding] = []
    seen: set[tuple[str, str, str, str, int | None]] = set()
    for finding in findings:
        category = finding.category.removeprefix("package-")
        key = (category, finding.path, finding.detail, finding.severity, finding.line)
        if key not in seen:
            seen.add(key)
            unique.append(finding)
    return unique


def render_workflow_trace(trace: WorkflowTraceResult) -> list[str]:
    state = "previous persisted snapshot" if trace.baseline_exists else "initial snapshot"
    lines = [
        "## Workflow Package Trace",
        "",
        f"- Baseline: {state}.",
        f"- Eligible live workflow documents: {len(trace.fingerprints)}",
        f"- Changed workflow documents: {len(trace.changes)}",
        "- Checks: broken package links, active references to retired files, and non-intentional exact repeated guidance.",
        "- Free-form prose is trace context for human review; this audit does not claim semantic contradictions.",
    ]
    if not trace.changes:
        lines.extend(["", "No workflow-document changes since the prior persisted audit."])
        return lines

    package_by_path = {package.change.path: package for package in trace.packages}
    for change in trace.changes:
        lines.extend(["", f"### {change.path}", ""])
        if change.change_type == "renamed":
            lines.append(f"- Change: renamed from `{change.previous_path}`.")
        else:
            lines.append(f"- Change: {change.change_type}.")
        if change.change_type == "removed":
            lines.append(
                "- **warning** — removed workflow document; confirm its lifecycle and archive-ledger entry before treating the removal as complete."
            )
            continue
        package = package_by_path[change.path]
        lines.append("- Package members:")
        for path_text, roles in sorted(package.members.items()):
            lifecycle = "; marked Deprecated/Retired/Superseded" if path_text in package.retired_members else ""
            lines.append(f"  - `{path_text}` — {', '.join(sorted(roles))}{lifecycle}.")
        if package.link_evidence:
            lines.append("- Link evidence:")
            for reference in package.link_evidence:
                target = reference.resolved or reference.target
                lines.append(f"  - `{reference.source}:{reference.line}` → `{target}`")
        else:
            lines.append("- Link evidence: none.")
        if package.findings:
            lines.append("- Package findings:")
            for finding in package.findings:
                lines.append(
                    f"  - **{finding.severity}** — {finding_location(finding)}: {finding.detail}"
                )
        else:
            lines.append("- Package findings: none.")
    return lines


def render_report(
    root: Path,
    findings: list[Finding],
    include_archive: bool,
    trace: WorkflowTraceResult | None = None,
) -> str:
    now = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()
    all_findings = unique_findings(findings + (trace.findings if trace is not None else []))
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.category].append(finding)
    errors = sum(item.severity == "error" for item in all_findings)
    warnings = sum(item.severity == "warning" for item in all_findings)
    intentional = sum(
        item.category == "repeated-guidance" and item.severity == "info"
        for item in findings
    )
    lines = [
        "# Workspace Maintenance Audit",
        "",
        f"Generated: {now}",
        f"Scope: {'live and archive' if include_archive else 'live paths only'}",
        "",
        "## Summary",
        "",
        f"- Errors: {errors}",
        f"- Warnings: {warnings}",
        f"- Intentional copies: {intentional}",
        "- Archive searches are excluded unless --include-archive is supplied.",
    ]
    if not all_findings:
        lines.extend(["", "No findings."])
    for category, items in sorted(grouped.items()):
        lines.extend(["", f"## {category.replace('-', ' ').title()}", ""])
        for item in items:
            lines.append(
                f"- **{item.severity}** — {finding_location(item)}: {item.detail}"
            )
    if trace is not None:
        lines.extend([""] + render_workflow_trace(trace))
    lines.extend(
        [
            "",
            "## Repair Boundary",
            "",
            "Repair only generated indexes, clear relative links, archive-ledger pointers, "
            "and encoding in editable canonical files without additional approval. Escalate "
            "business-policy conflicts, uncertain ownership, customer-facing copy, published "
            "records, and source evidence.",
            "",
        ]
    )
    return "\n".join(lines)


def write_report(
    root: Path,
    report: str,
    trace: WorkflowTraceResult | None = None,
) -> Path:
    archive = root / "90_archive" / "maintenance_audits"
    archive.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_path = archive / f"maintenance_audit_{stamp}.md"
    report_path.write_text(report, encoding="utf-8")
    if trace is not None:
        write_workflow_trace_baseline(root, trace.fingerprints)

    summary_counts: dict[str, int] = {}
    for line in report.splitlines():
        match = re.fullmatch(r"- (Errors|Warnings): (\d+)", line)
        if match:
            summary_counts[match.group(1)] = int(match.group(2))
    errors = summary_counts.get("Errors", sum("**error**" in line for line in report.splitlines()))
    warnings = summary_counts.get("Warnings", sum("**warning**" in line for line in report.splitlines()))
    relative_report = rel(report_path, root)
    status = root / "60_automation" / "workspace_maintenance" / "CURRENT_MAINTENANCE_STATUS.md"
    status_lines = [
        "# Current Maintenance Status",
        "",
        f"Last audit: [{report_path.name}](../../{relative_report})",
        "",
        f"- Errors: {errors}",
        f"- Warnings: {warnings}",
        "- Scope: live paths only unless an audit explicitly says otherwise.",
    ]
    if trace is not None:
        status_lines.append(
            f"- Workflow package trace: {len(trace.changes)} changed workflow documents; "
            f"{len(trace.fingerprints)} eligible documents fingerprinted."
        )
    status_lines.extend(
        [
            "- Next action: resolve errors first, then classify warnings before changing non-generated records.",
            "",
        ]
    )
    status.write_text("\n".join(status_lines), encoding="utf-8")
    return report_path


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--include-archive", action="store_true", help="Include archived and deprecated paths.")
    parser.add_argument("--write-report", action="store_true", help="Write a dated historical report, current-status pointer, and workflow trace baseline.")
    args = parser.parse_args(argv)
    root = args.root.resolve()

    retired = find_retired_files(root, args.include_archive)
    findings = (
        find_broken_links(root, args.include_archive)
        + find_retired_references(root, retired, args.include_archive)
        + find_mojibake(root, args.include_archive)
        + find_duplicate_guidance(root, args.include_archive)
    )
    trace = build_workflow_trace(root)
    report = render_report(root, findings, args.include_archive, trace)
    print(report)
    if args.write_report:
        written = write_report(root, report, trace)
        print(f"Wrote report: {rel(written, root)}")
    return 1 if any(item.severity == "error" for item in unique_findings(findings + trace.findings)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
