#!/usr/bin/env python3
"""Read-only integrity audit for the live Woodcraft workspace.

Default scans exclude 90_archive and deprecated paths. Use --include-archive
only when historical material is explicitly in scope. --write-report creates a
dated historical report and refreshes the current maintenance-status pointer.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ARCHIVE_DIRS = {"90_archive", "deprecated", ".git", "__pycache__"}
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


def find_broken_links(root: Path, include_archive: bool) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root, include_archive):
        for target in MARKDOWN_LINK.findall(read_text(path)):
            resolved = resolve_link(path, target)
            if resolved is not None and not resolved.exists():
                findings.append(Finding("broken-relative-link", rel(path, root), target, "error"))
    return findings


def find_retired_files(root: Path, include_archive: bool) -> dict[str, Path]:
    retired: dict[str, Path] = {}
    for path in markdown_files(root, include_archive):
        if RETIRED_STATUS.search(read_text(path)):
            retired[rel(path, root)] = path
    return retired


def find_retired_references(
    root: Path,
    retired: dict[str, Path],
    include_archive: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    for path in markdown_files(root, include_archive):
        content = read_text(path)
        current = rel(path, root)
        for retired_path in retired:
            if retired_path != current and retired_path in content:
                findings.append(Finding("retired-reference", current, retired_path))
    return findings


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


def normalized_long_lines(path: Path) -> set[str]:
    lines = set()
    for line in read_text(path).splitlines():
        clean = re.sub(r"\s+", " ", line.strip())
        if len(clean) >= 100 and not clean.startswith(("|", chr(96) * 3)):
            lines.add(clean)
    return lines


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
            detail = f"{classification} | {line[:180]}"
            findings.append(Finding("repeated-guidance", "; ".join(unique_paths), detail, severity))
    return findings


def render_report(root: Path, findings: list[Finding], include_archive: bool) -> str:
    now = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()
    grouped: dict[str, list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[finding.category].append(finding)
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
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
    if not findings:
        lines.extend(["", "No findings."])
    for category, items in sorted(grouped.items()):
        lines.extend(["", f"## {category.replace('-', ' ').title()}", ""])
        for item in items:
            lines.append(f"- **{item.severity}** — {item.path}: {item.detail}")
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


def write_report(root: Path, report: str) -> Path:
    archive = root / "90_archive" / "maintenance_audits"
    archive.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_path = archive / f"maintenance_audit_{stamp}.md"
    report_path.write_text(report, encoding="utf-8")

    errors = sum("**error**" in line for line in report.splitlines())
    warnings = sum("**warning**" in line for line in report.splitlines())
    relative_report = rel(report_path, root)
    status = root / "60_automation" / "workspace_maintenance" / "CURRENT_MAINTENANCE_STATUS.md"
    status.write_text(
        "# Current Maintenance Status\n\n"
        f"Last audit: [{report_path.name}](../../{relative_report})\n\n"
        f"- Errors: {errors}\n"
        f"- Warnings: {warnings}\n"
        "- Scope: live paths only unless an audit explicitly says otherwise.\n"
        "- Next action: resolve errors first, then classify warnings before changing non-generated records.\n",
        encoding="utf-8",
    )
    return report_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--include-archive", action="store_true", help="Include archived and deprecated paths.")
    parser.add_argument("--write-report", action="store_true", help="Write a dated historical report and current-status pointer.")
    args = parser.parse_args(argv)
    root = args.root.resolve()

    retired = find_retired_files(root, args.include_archive)
    findings = (
        find_broken_links(root, args.include_archive)
        + find_retired_references(root, retired, args.include_archive)
        + find_mojibake(root, args.include_archive)
        + find_duplicate_guidance(root, args.include_archive)
    )
    report = render_report(root, findings, args.include_archive)
    print(report)
    if args.write_report:
        written = write_report(root, report)
        print(f"Wrote report: {rel(written, root)}")
    return 1 if any(item.severity == "error" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
