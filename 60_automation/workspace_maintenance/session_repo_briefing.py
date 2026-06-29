#!/usr/bin/env python3
"""Create or inspect the daily Woodcraft session briefing.

The briefing reads current workspace records and writes only a dated snapshot plus
its live status pointer. Dates always use America/New_York.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

TIME_ZONE = ZoneInfo("America/New_York")
CONFIRMATION_PHRASE = "Brief me"
STATUS_NAME = "SESSION_BRIEFING_STATUS.md"
BRIEF_LATEST_JSON = "brief_latest.json"
REPORT_DIR = Path("90_archive/session_briefings")
BRIEFING_DATE = re.compile(r"^Briefing date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
STATUS_FIELD = re.compile(r"^-\s*([a-z_]+):\s*(.*)$", re.MULTILINE)
AUDIT_DATE = re.compile(r"maintenance_audit_(\d{4}-\d{2}-\d{2})")
SOCIAL_CADENCE_TRACKER = Path("50_content/social_post_cadence_tracker.md")
MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
LOCAL_PATH = re.compile(r"(?:\\\\\?\\)?[A-Za-z]:[\\/][^\s)]+")
REPO_PATH = re.compile(r"\b(?:\d{2}_[A-Za-z0-9_-]+|deprecated|90_archive)[\\/][^\s)]+")
SENSITIVE_TERM = re.compile(
    r"\b(?:api[_ -]?key|auth|bearer|password|private key|raw log|raw prompt|secret|token|tool output)\b",
    re.IGNORECASE,
)
EXCLUDED_FIELDS = [
    "raw_prompts",
    "logs",
    "full_local_paths",
    "auth_or_secret_values",
    "private_notes",
    "raw_source_file_contents",
]
DASHBOARD_TITLE_TARGET = 80
DASHBOARD_TITLE_MAX = 100
DASHBOARD_REASON_MAX = 180
DASHBOARD_DETAIL_MAX = 280


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


def json_path(root: Path) -> Path:
    return toolkit(root) / BRIEF_LATEST_JSON


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


def social_cadence_row(root: Path, briefing_day: date) -> dict[str, str] | None:
    content = read(root / SOCIAL_CADENCE_TRACKER)
    target_date = briefing_day.isoformat()
    for line in content.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 7 or cells[0] != target_date:
            continue
        return {
            "date": cells[0],
            "facebook_record": cells[1],
            "facebook_status": cells[2],
            "instagram_record": cells[3],
            "instagram_status": cells[4],
            "daily_status": cells[5],
            "notes": cells[6],
        }
    return None


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


def maintenance_status(root: Path, briefing_day: date) -> dict[str, object]:
    status_text = read(toolkit(root) / "CURRENT_MAINTENANCE_STATUS.md")
    date_match = AUDIT_DATE.search(status_text)
    if not date_match:
        return {
            "last_audit_date": None,
            "age_days": None,
            "freshness": "not_recorded",
            "errors": None,
            "warnings": None,
        }
    audit_day = date.fromisoformat(date_match.group(1))
    age = (briefing_day - audit_day).days
    errors = re.search(r"^- Errors:\s*(\d+)", status_text, re.MULTILINE)
    warnings = re.search(r"^- Warnings:\s*(\d+)", status_text, re.MULTILINE)
    freshness = "within the last week" if age <= 7 else "overdue by more than one week"
    return {
        "last_audit_date": audit_day.isoformat(),
        "age_days": age,
        "freshness": freshness,
        "errors": int(errors.group(1)) if errors else None,
        "warnings": int(warnings.group(1)) if warnings else None,
    }


def maintenance_summary(maintenance: dict[str, object]) -> list[str]:
    if not maintenance["last_audit_date"]:
        return ["- No valid maintenance audit is recorded."]
    return [
        f"- Last audit: {maintenance['last_audit_date']} "
        f"({maintenance['age_days']} day(s) ago; {maintenance['freshness']}).",
        f"- Errors: {maintenance['errors'] if maintenance['errors'] is not None else 'not recorded'}; "
        f"warnings: {maintenance['warnings'] if maintenance['warnings'] is not None else 'not recorded'}.",
    ]


def collect_briefing_data(root: Path, briefing_day: date) -> dict[str, object]:
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
    cadence = social_cadence_row(root, briefing_day)
    maintenance = maintenance_status(root, briefing_day)

    return {
        "briefing_date": briefing_day.isoformat(),
        "now_items": now_items,
        "soon_items": soon_items,
        "rollout_actions": rollout_actions,
        "product_counts": product_counts,
        "listing_counts": listing_counts,
        "ready_posts": ready_posts,
        "draft_posts": draft_posts,
        "published_posts": published_posts,
        "campaigns": campaigns,
        "cadence": cadence,
        "maintenance": maintenance,
    }


def render_briefing(root: Path, briefing_day: date) -> str:
    data = collect_briefing_data(root, briefing_day)
    now_items = data["now_items"]
    soon_items = data["soon_items"]
    rollout_actions = data["rollout_actions"]
    product_counts = data["product_counts"]
    listing_counts = data["listing_counts"]
    ready_posts = data["ready_posts"]
    draft_posts = data["draft_posts"]
    published_posts = data["published_posts"]
    campaigns = data["campaigns"]
    cadence = data["cadence"]

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
    if cadence:
        lines.append(
            "- Daily social cadence "
            f"({briefing_day.isoformat()}): {cadence['daily_status']}; "
            f"FB Page {cadence['facebook_status']} ({cadence['facebook_record']}); "
            f"Instagram {cadence['instagram_status']} ({cadence['instagram_record']})."
        )
    else:
        lines.append(
            "- Daily social cadence "
            f"({briefing_day.isoformat()}): not tracked yet; add a row in 50_content/social_post_cadence_tracker.md."
        )

    lines.extend(["", "## Maintenance", ""])
    lines.extend(maintenance_summary(data["maintenance"]))
    lines.extend(
        [
            "",
            "## Sources",
            "",
            "- 13_BACKLOG.md",
            "- 40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md",
            "- 30_products/, 40_listings/, 50_content/, and 70_ads/",
            "- 50_content/social_post_cadence_tracker.md",
            "- 60_automation/workspace_maintenance/CURRENT_MAINTENANCE_STATUS.md",
            "",
        ]
    )
    return "\n".join(lines)


def shorten_summary(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    shortened = text[: max_length - 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return f"{shortened or text[: max_length - 1].rstrip()}…"


def safe_summary(text: str, fallback: str, max_length: int = 140) -> str:
    summary = MARKDOWN_LINK.sub(r"\1", text)
    summary = summary.replace("`", "")
    summary = LOCAL_PATH.sub("[local path removed]", summary)
    summary = REPO_PATH.sub("[repo path removed]", summary)
    summary = re.sub(r"\s+", " ", summary).strip(" -*_")
    if SENSITIVE_TERM.search(summary):
        summary = fallback
    return shorten_summary(summary or fallback, max_length)


def sentence_summary(text: str, fallback: str, max_length: int) -> str:
    summary = safe_summary(text, fallback, max_length).strip().rstrip(".")
    if summary:
        summary = summary[0].upper() + summary[1:]
    return shorten_summary(f"{summary}.", max_length)


def normalize_dashboard_item(
    text: str,
    fallback_title: str,
    default_reason: str,
) -> dict[str, str]:
    """Return a short dashboard title plus sanitized supporting context."""
    safe_text = safe_summary(text, fallback_title, DASHBOARD_DETAIL_MAX)
    if safe_text == fallback_title:
        return {
            "title": shorten_summary(fallback_title, DASHBOARD_TITLE_MAX),
            "reason": shorten_summary(default_reason, DASHBOARD_REASON_MAX),
        }

    title = safe_text.rstrip(".")
    reason = default_reason
    detail = ""

    create_pack = re.fullmatch(
        r"Create (?:the )?(?P<wave>Wave \d+) "
        r"(?:Facebook Marketplace )?image prompt pack for (?P<scope>.+?) "
        r"from (?:their )?approved catalog references\.?",
        safe_text,
        re.IGNORECASE,
    )
    run_pack = re.fullmatch(
        r"Run (?:the )?(?P<wave>Wave \d+) pack for (?:SKU )?(?P<sku>[A-Za-z0-9_-]+) first:"
        r"\s*(?P<detail>.+)",
        safe_text,
        re.IGNORECASE,
    )
    cadence = re.fullmatch(
        r"(?:Maintain|Update) the daily Facebook Page \+ Instagram "
        r"(?:brand-post )?cadence tracker:\s*(?P<detail>.+)",
        safe_text,
        re.IGNORECASE,
    )

    if create_pack:
        scope = create_pack.group("scope").strip()
        sku_label = "SKUs" if "," in scope or re.search(r"\band\b", scope, re.IGNORECASE) else "SKU"
        title = f"Create {create_pack.group('wave')} image prompt pack for {sku_label} {scope}"
        reason = "Uses approved catalog references for the selected SKUs."
    elif run_pack:
        wave = run_pack.group("wave")
        sku = run_pack.group("sku")
        source_detail = run_pack.group("detail").strip()
        next_scope = re.search(
            r"\bbefore moving (?:one SKU at a time )?through (?P<scope>.+?)[.]?$",
            source_detail,
            re.IGNORECASE,
        )
        title = f"Run {wave} image pack for SKU {sku}"
        if next_scope:
            reason = f"SKU {sku} should be reviewed before moving through {next_scope.group('scope').rstrip('.')}."
            detail = source_detail[: next_scope.start()].strip()
        else:
            reason = f"Review SKU {sku} before continuing the remaining image-pack work."
            detail = source_detail
    elif cadence:
        title = "Update daily Facebook and Instagram cadence"
        reason = "Keeps the current social posting rhythm on track."
        detail = re.sub(
            r"\s+in\s+\[repo path removed\]\.?$",
            "",
            cadence.group("detail").strip(),
            flags=re.IGNORECASE,
        )
    else:
        title_context = re.fullmatch(r"(?P<title>[^:]+):\s*(?P<detail>.+)", safe_text)
        if title_context:
            title = title_context.group("title").strip()
            detail = title_context.group("detail").strip()
        elif len(title) > DASHBOARD_TITLE_TARGET:
            detail = safe_text

    normalized = {
        "title": shorten_summary(title.strip().rstrip(".:"), DASHBOARD_TITLE_TARGET),
        "reason": sentence_summary(reason, default_reason, DASHBOARD_REASON_MAX),
    }
    if detail:
        normalized["detail"] = sentence_summary(detail, "Additional context is available.", DASHBOARD_DETAIL_MAX)
    return normalized


def normalized_action_key(title: str) -> str:
    key = unicodedata.normalize("NFKC", title).casefold()
    key = key.replace("&", " and ").replace("+", " and ")
    key = re.sub(r"[\W_]+", " ", key, flags=re.UNICODE)
    return re.sub(r"\s+", " ", key).strip()


def stable_action_id(title: str) -> str:
    key = normalized_action_key(title) or "action"
    slug = re.sub(r"[^a-z0-9]+", "-", key).strip("-") or "action"
    slug = slug[:48].rstrip("-")
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:10]
    return f"woodcraft-brief-{slug}-{digest}"


def dedupe_dashboard_suggestions(
    priorities: list[dict[str, str]],
    next_actions: list[dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Keep one suggestion per practical action, preferring priorities."""
    seen: dict[str, dict[str, str]] = {}
    deduped_priorities: list[dict[str, str]] = []
    deduped_next_actions: list[dict[str, str]] = []

    for items, output in (
        (priorities, deduped_priorities),
        (next_actions, deduped_next_actions),
    ):
        for item in items:
            key = normalized_action_key(item["title"])
            if key in seen:
                retained = seen[key]
                if not retained.get("detail") and item.get("detail"):
                    retained["detail"] = item["detail"]
                continue
            retained = dict(item)
            retained["id"] = stable_action_id(retained["title"])
            seen[key] = retained
            output.append(retained)

    return deduped_priorities, deduped_next_actions


def render_dashboard_json(root: Path, briefing_day: date) -> dict[str, object]:
    data = collect_briefing_data(root, briefing_day)
    priorities = []
    for index, item in enumerate(data["now_items"][:3], start=1):
        summary = normalize_dashboard_item(
            item,
            f"Priority item {index}",
            "Keeps the current highest-priority backlog work moving.",
        )
        priorities.append(
            {
                "source": "brief_now",
                **summary,
                "urgency": "high",
                "project_key": "woodcraft",
                "status": "suggested",
            }
        )

    next_actions = []
    for index, item in enumerate(data["rollout_actions"][:3], start=1):
        summary = normalize_dashboard_item(
            item,
            f"Next action {index}",
            "Advances the current Marketplace rollout.",
        )
        next_actions.append(
            {
                "source": "brief_next_three_actions",
                **summary,
                "project_key": "woodcraft",
                "status": "open",
            }
        )

    priorities, next_actions = dedupe_dashboard_suggestions(priorities, next_actions)

    cadence = data["cadence"]
    maintenance = data["maintenance"]
    posting_schedule: dict[str, object] = {
        "scheduled_or_ready_count": len(data["ready_posts"]),
        "draft_count": len(data["draft_posts"]),
        "published_count": len(data["published_posts"]),
    }
    if cadence:
        posting_schedule["daily_cadence"] = {
            "date": cadence["date"],
            "facebook_status": safe_summary(cadence["facebook_status"], "Unavailable"),
            "instagram_status": safe_summary(cadence["instagram_status"], "Unavailable"),
            "daily_status": safe_summary(cadence["daily_status"], "Unavailable"),
        }
    else:
        posting_schedule["daily_cadence"] = {
            "date": briefing_day.isoformat(),
            "daily_status": "not_tracked",
        }

    return {
        "briefing_date": briefing_day.isoformat(),
        "timezone": "America/New_York",
        "state": "current",
        "source": "woodcraft_brief_me",
        "priorities": priorities,
        "next_actions": next_actions,
        "project_status": {
            "products_by_status": dict(sorted(data["product_counts"].items())),
            "listings_by_status": dict(sorted(data["listing_counts"].items())),
            "posting_schedule": posting_schedule,
            "campaigns": {"record_count": len(data["campaigns"])},
            "maintenance": {
                "last_audit_date": maintenance["last_audit_date"],
                "errors": maintenance["errors"] if maintenance["errors"] is not None else 0,
                "warnings": maintenance["warnings"] if maintenance["warnings"] is not None else 0,
                "audit_recorded": maintenance["last_audit_date"] is not None,
                "freshness": maintenance["freshness"],
            },
        },
        "excluded_fields": EXCLUDED_FIELDS,
    }


def write_dashboard_json(root: Path, briefing_day: date) -> Path:
    path = json_path(root)
    payload = render_dashboard_json(root, briefing_day)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def write_briefing(root: Path, briefing_day: date) -> tuple[str, bool, Path]:
    state, _, existing = status(root, briefing_day)
    if state == "current" and existing is not None:
        write_dashboard_json(root, briefing_day)
        return read(existing), False, existing

    report = report_path(root, briefing_day)
    report.parent.mkdir(parents=True, exist_ok=True)
    content = render_briefing(root, briefing_day)
    report.write_text(content, encoding="utf-8")
    write_dashboard_json(root, briefing_day)
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
