#!/usr/bin/env python3
"""Create or inspect the daily Woodcraft session briefing.

The briefing reads current workspace records and writes only a dated snapshot plus
its live status pointer. Dates always use America/New_York.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TIME_ZONE = ZoneInfo("America/New_York")
CONFIRMATION_PHRASE = "Brief me"
STATUS_NAME = "SESSION_BRIEFING_STATUS.md"
REPORT_DIR = Path("90_archive/session_briefings")
BRIEFING_DATE = re.compile(r"^Briefing date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
STATUS_FIELD = re.compile(r"^-\s*([a-z_]+):\s*(.*)$", re.MULTILINE)
AUDIT_DATE = re.compile(r"maintenance_audit_(\d{4}-\d{2}-\d{2})")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def eastern_today(now: datetime | None = None) -> date:
    current = now or datetime.now(TIME_ZONE)
    if current.tzinfo is None:
        current = current.replace(tzinfo=TIME_ZONE)
    return current.astimezone(TIME_ZONE).date()


def toolkit(root: Path) -> Path:
    return root / "60_automation" / "workspace_maintenance"


def status_path(root: Path) -> Path:
    return toolkit(root) / STATUS_NAME


def report_path(root: Path, briefing_day: date) -> Path:
    return root / REPORT_DIR / f"session_repo_briefing_{briefing_day.isoformat()}.md"


def status(root: Path, briefing_day: date) -> tuple[str, str, Path | None]:
    content = read(status_path(root))
    match = BRIEFING_DATE.search(content)
    if not match:
        return "due", "No daily briefing has been recorded.", None
    recorded_day = date.fromisoformat(match.group(1))
    report = report_path(root, recorded_day)
    if recorded_day != briefing_day:
        return "due", f"Latest briefing is from {recorded_day.isoformat()}.", report
    if not report.exists():
        return "due", "Today's briefing report is missing.", report
    return "current", "Today's briefing is already recorded.", report


def markdown_section_items(text: str, heading: str) -> list[str]:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return []
    after = text[match.end():]
    next_heading = re.search(r"^## ", after, re.MULTILINE)
    section = after[: next_heading.start()] if next_heading else after
    return [
        item.strip()
        for item in re.findall(r"^\d+\.\s+(.+)$", section, re.MULTILINE)
    ]


def field(text: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def status_counts(folder: Path, pattern: str, field_name: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in sorted(folder.glob(pattern)):
        value = field(read(path), field_name)
        if value:
            counts[value] += 1
    return counts


def content_records(root: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for path in sorted((root / "50_content").glob("content_*.md")):
        content = read(path)
        records.append(
            {
                "path": path.relative_to(root).as_posix(),
                "content_id": field(content, "content_id") or path.stem,
                "platform": field(content, "platform") or "Unspecified",
                "publish_status": field(content, "publish_status") or "Unspecified",
                "publish_date": field(content, "publish_date"),
                "publish_ready": field(content, "publish_ready"),
            }
        )
    return records


def campaign_records(root: Path) -> list[tuple[str, str]]:
    folder = root / "70_ads"
    records: list[tuple[str, str]] = []
    if not folder.exists():
        return records
    for path in sorted(folder.rglob("*.md")):
        if path.name.startswith("."):
            continue
        content = read(path)
        campaign_status = field(content, "campaign_status") or field(content, "ad_status") or field(content, "status")
        records.append((path.relative_to(root).as_posix(), campaign_status or "Status not recorded"))
    return records


def maintenance_summary(root: Path, briefing_day: date) -> list[str]:
    status_text = read(toolkit(root) / "CURRENT_MAINTENANCE_STATUS.md")
    date_match = AUDIT_DATE.search(status_text)
    if not date_match:
        return ["- No valid maintenance audit is recorded."]
    audit_day = date.fromisoformat(date_match.group(1))
    age = (briefing_day - audit_day).days
    errors = re.search(r"^- Errors:\s*(\d+)", status_text, re.MULTILINE)
    warnings = re.search(r"^- Warnings:\s*(\d+)", status_text, re.MULTILINE)
    freshness = "within the last week" if age <= 7 else "overdue by more than one week"
    return [
        f"- Last audit: {audit_day.isoformat()} ({age} day(s) ago; {freshness}).",
        f"- Errors: {errors.group(1) if errors else 'not recorded'}; warnings: {warnings.group(1) if warnings else 'not recorded'}.",
    ]


def render_briefing(root: Path, briefing_day: date) -> str:
    backlog = read(root / "13_BACKLOG.md")
    now_items = markdown_section_items(backlog, "Now (Highest Priority)")
    soon_items = markdown_section_items(backlog, "Soon")
    rollout = read(root / "40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md")
    rollout_actions = markdown_section_items(rollout, "Next Three Actions")
    product_counts = status_counts(root / "30_products", "prod_*.md", "status")
    listing_counts = status_counts(root / "40_listings", "list_*.md", "publish_status")
    posts = content_records(root)
    ready_posts = [
        post
        for post in posts
        if post["publish_status"].lower().startswith(("scheduled", "ready"))
    ]
    draft_posts = [post for post in posts if post["publish_status"].lower() == "draft"]
    published_posts = [post for post in posts if post["publish_status"].lower() == "published"]
    campaigns = campaign_records(root)

    lines = [
        "# Daily Woodcraft Repo Briefing",
        "",
        f"Briefing date: {briefing_day.isoformat()}",
        "Timezone: America/New_York",
        "",
        "## Todos",
        "",
        f"- Now: {len(now_items)} item(s).",
    ]
    for index, item in enumerate(now_items[:3], start=1):
        lines.append(f"{index}. {item}")
    if len(now_items) > 3:
        lines.append(f"- {len(now_items) - 3} additional Now item(s) remain in 13_BACKLOG.md.")
    lines.append(f"- Soon: {len(soon_items)} item(s).")

    lines.extend(["", "## Open Projects", ""])
    if rollout_actions:
        for index, item in enumerate(rollout_actions[:3], start=1):
            lines.append(f"{index}. {item}")
    else:
        lines.append("- No rollout next actions are recorded.")
    product_text = ", ".join(f"{name}: {count}" for name, count in sorted(product_counts.items()))
    listing_text = ", ".join(f"{name}: {count}" for name, count in sorted(listing_counts.items()))
    lines.append(f"- Product records by status: {product_text or 'none recorded'}.")
    lines.append(f"- Marketplace listings by status: {listing_text or 'none recorded'}.")

    lines.extend(["", "## Campaigns", ""])
    if campaigns:
        lines.extend(f"- {path}: {campaign_status}." for path, campaign_status in campaigns)
    else:
        lines.append("- No active ad campaign records exist in 70_ads/.")

    lines.extend(["", "## Posting Schedules", ""])
    if ready_posts:
        lines.extend(
            f"- Scheduled or ready: {post['content_id']} on {post['platform']} ({post['publish_status']}; date: {post['publish_date'] or 'not set'})."
            for post in ready_posts
        )
    else:
        lines.append("- Scheduled or ready: none.")
    lines.append(f"- Drafts awaiting schedule: {len(draft_posts)}.")
    lines.append(f"- Published content records: {len(published_posts)}.")

    lines.extend(["", "## Maintenance", ""])
    lines.extend(maintenance_summary(root, briefing_day))
    lines.extend(
        [
            "",
            "## Sources",
            "",
            "- 13_BACKLOG.md",
            "- 40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md",
            "- 30_products/, 40_listings/, 50_content/, and 70_ads/",
            "- 60_automation/workspace_maintenance/CURRENT_MAINTENANCE_STATUS.md",
            "",
        ]
    )
    return "\n".join(lines)


def write_briefing(root: Path, briefing_day: date) -> tuple[str, bool, Path]:
    state, _, existing = status(root, briefing_day)
    if state == "current" and existing is not None:
        return read(existing), False, existing

    report = report_path(root, briefing_day)
    report.parent.mkdir(parents=True, exist_ok=True)
    content = render_briefing(root, briefing_day)
    report.write_text(content, encoding="utf-8")
    relative_report = report.relative_to(root).as_posix()
    status_path(root).write_text(
        "# Session Briefing Status\n\n"
        f"Briefing date: {briefing_day.isoformat()}\n"
        "Timezone: America/New_York\n"
        f"Report: [daily briefing](../../{relative_report})\n"
        "- state: current\n"
        "- The report is an operational snapshot, not an automatic task, learning, or policy change.\n",
        encoding="utf-8",
    )
    return content, True, report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--status", action="store_true", help="Report whether today's briefing exists.")
    action.add_argument("--write", action="store_true", help="Create or replay today's briefing.")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    briefing_day = eastern_today()

    if args.status:
        state, reason, report = status(root, briefing_day)
        print(f"state: {state}")
        print(f"briefing_date: {briefing_day.isoformat()}")
        print(f"reason: {reason}")
        print(f"confirmation_phrase: {CONFIRMATION_PHRASE}")
        if report is not None:
            print(f"report: {report.relative_to(root).as_posix()}")
        return 0

    content, created, report = write_briefing(root, briefing_day)
    print(content)
    print(f"Report: {report.relative_to(root).as_posix()} ({'created' if created else 'replayed'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
