#!/usr/bin/env python3
"""Prepare a review-only learning-consolidation queue from durable workspace evidence."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

DECISION = re.compile(r"^\|\s*([^|]+)\s*\|\s*(DEC-(\d+))\s*\|\s*([^|]+)\s*\|", re.MULTILINE)
BASELINE = re.compile(
    rf"Last decision reviewed:\s*{chr(96)}?(DEC-(\d+)){chr(96)}?"
)
LAST_AUDIT = re.compile(r"Last audit:\s*\[[^\]]+\]\(([^)]+)\)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def decision_candidates(root: Path) -> tuple[str | None, list[tuple[str, str, str]]]:
    learning = read(root / "60_automation" / "workspace_maintenance" / "MAINTENANCE_LEARNINGS.md")
    baseline_match = BASELINE.search(learning)
    baseline = int(baseline_match.group(2)) if baseline_match else 0
    baseline_id = baseline_match.group(1) if baseline_match else None
    candidates = [
        (decision_id, date.strip(), title.strip())
        for date, decision_id, number, title in DECISION.findall(read(root / "12_DECISION_LOG.md"))
        if int(number) > baseline
    ]
    return baseline_id, candidates


def audit_summary(root: Path) -> tuple[str, list[str]]:
    status = root / "60_automation" / "workspace_maintenance" / "CURRENT_MAINTENANCE_STATUS.md"
    match = LAST_AUDIT.search(read(status))
    if not match:
        return "No maintenance audit is recorded.", []
    report = (status.parent / match.group(1)).resolve()
    report_text = read(report)
    summary = [
        line
        for line in report_text.splitlines()
        if line.startswith(
            (
                "- Errors:",
                "- Warnings:",
                "- Intentional copies:",
            )
        )
    ]
    return report.relative_to(root).as_posix(), summary


def render(root: Path) -> str:
    baseline, candidates = decision_candidates(root)
    report, summary = audit_summary(root)
    lines = [
        "# Learning Consolidation Review",
        "",
        f"Generated date: {dt.date.today().isoformat()}",
        "",
        "This is a review queue, not an automatic rule writer. It explicitly reads the latest maintenance audit because the audit is the requested evidence source.",
        "",
        "## Decision-Log Candidates",
        "",
        f"Baseline: {baseline or 'not set'}",
    ]
    if candidates:
        lines.extend(["", "| Decision | Date | Candidate lesson |", "|---|---|---|"])
        lines.extend(f"| {decision_id} | {date} | {title} |" for decision_id, date, title in candidates)
    else:
        lines.append("- No decision-log entries need learning review after the recorded baseline.")

    lines.extend(["", "## Latest Audit Evidence", "", f"- Report: {report}"])
    if summary:
        lines.extend(summary)
    else:
        lines.append("- No audit summary is available yet.")

    lines.extend(
        [
            "",
            "## Promotion Test",
            "",
            "Add an entry to MAINTENANCE_LEARNINGS.md only when the pattern is recurring, evidence-backed, and has a clear canonical source or durable pointer. Record a governance decision in 12_DECISION_LOG.md only when it changes operating behavior.",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="Write LEARNING_REVIEW.md.")
    action.add_argument("--check", action="store_true", help="Fail if LEARNING_REVIEW.md is stale.")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    target = root / "60_automation" / "workspace_maintenance" / "LEARNING_REVIEW.md"
    content = render(root)

    if args.write:
        target.write_text(content, encoding="utf-8")
        print(f"Wrote {target.relative_to(root).as_posix()}")
        return 0
    if not target.exists() or read(target) != content:
        print(f"Stale: {target.relative_to(root).as_posix()}")
        return 1
    print("Learning consolidation review is current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
