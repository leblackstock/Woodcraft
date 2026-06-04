from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = REPO_ROOT / "20_research" / "YouTubeTranscripts" / "analysis" / "woodcraft_research.sqlite"
VIDEO_INDEX_PATH = (
    REPO_ROOT
    / "20_research"
    / "YouTubeTranscripts"
    / "analysis"
    / "whosthevoss_video_concept_product_index_2026-04-30.md"
)
CROSSREF_PATH = (
    REPO_ROOT
    / "20_research"
    / "YouTubeTranscripts"
    / "analysis"
    / "whosthevoss_video_to_current_products_cross_reference_2026-04-30.md"
)
TRANSCRIPT_DIR = REPO_ROOT / "20_research" / "YouTubeTranscripts" / "WhosTheVoss_transcripts"
PRODUCT_DIR = REPO_ROOT / "30_products"


MOJIBAKE_FIXES = {
    "\u00e2\u20ac\u2122": "'",
    "\u00e2\u20ac\u02dc": "'",
    "\u00e2\u20ac\u0153": '"',
    "\u00e2\u20ac\u009d": '"',
    "\u00e2\u20ac": '"',
    "\u00e2\u20ac\u201c": "-",
    "\u00e2\u20ac\u201d": "-",
    "\u00e2\u20ac\u00a6": "...",
    "\u00c2\u00b0": " degrees",
    "\u00c2": "",
}


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    text = value.replace("\ufeff", "").replace("\r\n", "\n")
    for bad, good in MOJIBAKE_FIXES.items():
        text = text.replace(bad, good)
    return text.strip()


def strip_md_links(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", value)
    value = value.replace("`", "")
    return clean_text(value)


def first_money(value: str | None) -> str:
    match = re.search(r"\$\d+(?:,\d{3})*(?:\.\d+)?", value or "")
    return match.group(0) if match else ""


def first_percent(value: str | None) -> str:
    match = re.search(r"\d+(?:\.\d+)?%", value or "")
    return match.group(0) if match else ""


def money(value: float) -> str:
    return f"${value:.2f}"


def money_float(value: str | None) -> float | None:
    amount = first_money(value)
    if not amount:
        return None
    return float(amount.replace("$", "").replace(",", ""))


def spec_quantity(spec: str, pattern: str) -> float:
    match = re.search(pattern, spec, flags=re.IGNORECASE)
    if not match:
        return 0.0
    if match.lastindex and match.lastindex >= 2 and match.group(2):
        return float(match.group(2))
    return float(match.group(1))


def derived_materials_cost(fields: dict[str, str]) -> tuple[str, str]:
    spec = fields.get("material_spec", "")
    if not spec or spec.lower().startswith("pending"):
        return "", ""

    pickets = spec_quantity(spec, r"(\d+(?:\.\d+)?)(?:\s*[-–]\s*(\d+(?:\.\d+)?))?\s+cedar pickets?")
    treated_4x4 = spec_quantity(spec, r"(\d+(?:\.\d+)?)\s+treated\s+4x4x8")
    treated_2x4 = spec_quantity(spec, r"(\d+(?:\.\d+)?)\s+treated\s+2x4x8")
    glue_oz = spec_quantity(spec, r"(\d+(?:\.\d+)?)\s+oz\s+glue")
    nails = spec_quantity(spec, r"(\d+(?:\.\d+)?)(?:\s*[-–]\s*(\d+(?:\.\d+)?))?\s+nails?")
    screws = spec_quantity(spec, r"(\d+(?:\.\d+)?)\s+screws?")

    total = 0.0
    parts: list[str] = []
    if pickets:
        total += pickets * 3.68
        parts.append(f"{pickets:g} cedar pickets")
    if treated_4x4:
        total += treated_4x4 * 9.98
        parts.append(f"{treated_4x4:g} treated 4x4x8")
    if treated_2x4:
        total += treated_2x4 * 4.28
        parts.append(f"{treated_2x4:g} treated 2x4x8")
    if glue_oz:
        total += glue_oz * (40.00 / 128)
        parts.append(f"{glue_oz:g} oz glue")
    if nails:
        total += nails * (10.00 / 5000)
        parts.append(f"{nails:g} nails")
    if screws:
        total += screws * 0.04
        parts.append(f"{screws:g} screws")

    if not parts:
        return "", ""
    return money(total), "Derived from material_spec using 20_research/material_cost_reference.md: " + ", ".join(parts)


def effective_materials_cost(fields: dict[str, str]) -> str:
    derived_cost = derived_materials_cost(fields)[0]
    source = first_money(fields.get("materials_cost_estimate"))
    source_text = fields.get("materials_cost_estimate", "").lower()
    if derived_cost and "owner-confirmed" not in source_text and "owner confirmed" not in source_text:
        return derived_cost
    return source or derived_cost


def strategy_1_pending(fields: dict[str, str]) -> bool:
    text = " ".join(
        fields.get(key, "")
        for key in ["pricing_strategy_1_price_floor", "pricing_strategy_review", "pricing_validation"]
    ).lower()
    return (
        ("strategy 1" in text or "labor-inclusive" in text or "labor inclusive" in text)
        and ("pending" in text or "blocked" in text or "incomplete" in text)
    )


def materials_amount_status(fields: dict[str, str]) -> str:
    materials = fields.get("materials_cost_estimate")
    unit_cost = fields.get("unit_cost_estimate")
    derived_cost = derived_materials_cost(fields)[0]
    source_text = (materials or "").lower()
    if derived_cost and "owner-confirmed" not in source_text and "owner confirmed" not in source_text:
        return "Derived from list"
    if first_money(materials):
        return "Amount present"
    if first_money(unit_cost):
        return "Unit cost only"
    if (materials or "").strip():
        return "No amount"
    return "Missing"


def pricing_status(fields: dict[str, str]) -> str:
    text = " ".join(
        fields.get(key, "")
        for key in ["pricing_strategy_review", "pricing_validation", "target_price"]
    ).lower()
    if not first_money(fields.get("target_price")):
        return "Missing Price"
    if not effective_materials_cost(fields) and not first_money(fields.get("pricing_strategy_2_price_floor")):
        return "Missing Materials"
    if not text:
        return "Missing"
    if "owner-confirmed" in text or "owner confirmed" in text or "approved override" in text:
        return "Owner Confirmed"
    if "blocked" in text and not strategy_1_pending(fields):
        return "Blocked"
    if "below" in text:
        return "Warning"
    if "warning" in text or "fail" in text or "below" in text:
        return "Warning"
    if "needs approval" in text or "draft" in text:
        return "Needs Approval"
    if "pending" in text or "not started" in text:
        return "Pending"
    if "assumption" in text or "estimate" in text or "guide" in text or "reference" in text:
        return "Estimated"
    if "confirmed" in text or "approved" in text or "pass" in text:
        return "Confirmed"
    return "Review"


def cost_sheet_status(value: str | None) -> str:
    text = (value or "").lower()
    if not text:
        return "Missing"
    if "guide-only" in text:
        return "Guide Only"
    if text.startswith("pending") or "not started" in text:
        return "Pending"
    return "Linked"


def costing_method(fields: dict[str, str]) -> str:
    combined = " ".join(
        fields.get(key, "")
        for key in ["cost_sheet_ref", "materials_cost_estimate", "unit_cost_estimate", "pricing_strategy_review"]
    ).lower()
    if not combined.strip():
        return "Unknown"
    if not effective_materials_cost(fields):
        if first_money(fields.get("unit_cost_estimate")):
            return "Unit cost only"
        return "Missing cost amount"
    if not first_money(fields.get("materials_cost_estimate")):
        return "Derived materials list"
    if "owner-confirmed" in combined or "owner confirmed" in combined or "owner estimate" in combined:
        return "Owner estimate"
    if cost_sheet_status(fields.get("cost_sheet_ref")) == "Linked":
        return "Live cost sheet"
    if "guide-only" in combined or "guide-based" in combined or "guide cost" in combined or "guide cost estimate" in combined:
        return "Guide-based estimate"
    if "blocked" in combined:
        return "Blocked pending inputs"
    if "pending" in combined or "not started" in combined:
        return "Pending cost sheet"
    if "assumption" in combined or "placeholder" in combined or "estimate" in combined:
        return "Assumption / placeholder"
    return "Review source note"


def sale_pricing_method(fields: dict[str, str]) -> str:
    combined = " ".join(
        fields.get(key, "")
        for key in ["target_price", "pricing_strategy_review", "pricing_validation"]
    ).lower()
    target = (fields.get("target_price") or "").lower()
    if not combined.strip():
        return "Unknown"
    if "owner-confirmed" in combined or "owner confirmed" in combined or "approved override" in combined:
        return "Owner-confirmed override"
    if "guide selling price" in target:
        return "Guide selling price"
    if "local list price" in target or "local price" in target:
        return "Local list price assumption"
    if "blocked" in combined:
        return "Blocked pending pricing"
    if "pending" in combined or "not started" in combined:
        return "Pending price"
    if "recommended_price_floor" in combined or "recommended floor" in combined:
        return "Floor-based review"
    if "assumption" in combined or "estimate" in combined or "guide" in combined or "draft" in combined:
        return "Assumption / estimate"
    if first_money(fields.get("target_price")):
        return "Stated target price"
    return "Review source note"


def pricing_action(fields: dict[str, str]) -> str:
    if not first_money(fields.get("target_price")):
        return "Set target price"
    if not effective_materials_cost(fields):
        return "Add materials amount"
    if not first_money(fields.get("pricing_strategy_2_price_floor")) and not effective_materials_cost(fields):
        return "Run Strategy 2"
    if "approval" in (fields.get("pricing_strategy_review", "") + fields.get("pricing_validation", "")).lower():
        return "Owner price approval"
    if cost_sheet_status(fields.get("cost_sheet_ref")) in {"Missing", "Pending", "Guide Only"}:
        return "Create live cost sheet when ready"
    return "Review pricing"


def pricing_issue_flags(fields: dict[str, str]) -> str:
    flags: list[str] = []
    if not first_money(fields.get("target_price")):
        flags.append("missing price")
    if not effective_materials_cost(fields):
        if first_money(fields.get("unit_cost_estimate")):
            flags.append("missing materials amount")
        else:
            flags.append("missing cost amount")
    if "warning" in (fields.get("pricing_strategy_review", "") + fields.get("pricing_validation", "")).lower():
        flags.append("warning")
    if "below" in (fields.get("pricing_strategy_review", "") + fields.get("pricing_validation", "")).lower():
        flags.append("below benchmark")
    if "approval" in (fields.get("pricing_strategy_review", "") + fields.get("pricing_validation", "")).lower():
        flags.append("needs approval")
    return "; ".join(flags) if flags else "none"


def pricing_note_flags(fields: dict[str, str]) -> str:
    flags: list[str] = []
    combined = " ".join(
        fields.get(key, "")
        for key in ["cost_sheet_ref", "unit_cost_estimate", "materials_cost_estimate", "pricing_strategy_review"]
    ).lower()
    if strategy_1_pending(fields):
        flags.append("labor-inclusive Strategy 1 pending")
    derived_cost = derived_materials_cost(fields)[0]
    source_amount = money_float(fields.get("materials_cost_estimate"))
    derived_amount = money_float(derived_cost)
    if derived_cost:
        flags.append("materials cost derived from list")
    if source_amount is not None and derived_amount is not None and abs(source_amount - derived_amount) >= 0.01:
        flags.append("source materials amount differs from list cost")
    if not effective_materials_cost(fields) and first_money(fields.get("unit_cost_estimate")):
        flags.append("unit cost amount present only")
    if cost_sheet_status(fields.get("cost_sheet_ref")) in {"Missing", "Pending", "Guide Only"}:
        flags.append("live cost sheet pending")
    if "guide-only" in combined or "guide-based" in combined:
        flags.append("guide-only estimate")
    return "; ".join(flags) if flags else "none"


def pricing_normalized(fields: dict[str, str]) -> dict[str, str]:
    derived_cost, derived_basis = derived_materials_cost(fields)
    materials_cost = effective_materials_cost(fields)
    strategy_2_floor = first_money(fields.get("pricing_strategy_2_price_floor"))
    if materials_amount_status(fields) == "Derived from list" and materials_cost:
        strategy_2_floor = money(float(materials_cost.replace("$", "").replace(",", "")) / 0.30)
    elif not strategy_2_floor and materials_cost:
        strategy_2_floor = money(float(materials_cost.replace("$", "").replace(",", "")) / 0.30)
    return {
        "materials_cost_value": materials_cost,
        "materials_amount_status": materials_amount_status(fields),
        "materials_cost_basis": derived_basis,
        "unit_cost_value": first_money(fields.get("unit_cost_estimate")),
        "target_price_value": first_money(fields.get("target_price")),
        "pricing_strategy_1_floor_value": first_money(fields.get("pricing_strategy_1_price_floor")),
        "pricing_strategy_2_floor_value": strategy_2_floor,
        "recommended_price_floor_value": first_money(fields.get("recommended_price_floor")),
        "material_cost_percent_value": first_percent(fields.get("material_cost_percent_of_price")),
        "pricing_status": pricing_status(fields),
        "costing_method": costing_method(fields),
        "sale_pricing_method": sale_pricing_method(fields),
        "cost_sheet_status": cost_sheet_status(fields.get("cost_sheet_ref")),
        "pricing_issue_flags": pricing_issue_flags(fields),
        "pricing_note_flags": pricing_note_flags(fields),
        "pricing_next_action": pricing_action(fields),
    }


def split_md_table_row(line: str) -> list[str]:
    row = line.strip()
    if not row.startswith("|"):
        return []
    row = row.strip("|")
    return [clean_text(part) for part in row.split("|")]


def read_text(path: Path) -> str:
    return clean_text(path.read_text(encoding="utf-8", errors="replace"))


def parse_bullets(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = clean_text(raw_line)
        match = re.match(r"^-\s+([A-Za-z0-9_]+):\s*(.*)$", line)
        if match and match.group(1) not in fields:
            fields[match.group(1)] = strip_md_links(match.group(2))
    return fields


def parse_video_index(path: Path) -> list[dict[str, str]]:
    videos: list[dict[str, str]] = []
    in_table = False
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = clean_text(raw_line)
        if line.startswith("| # | Video | URL |"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table or not line.startswith("|"):
            continue
        if re.match(r"^\|\s*-+", line):
            continue
        cells = split_md_table_row(line)
        if len(cells) < 6 or not cells[0].isdigit():
            continue
        videos.append(
            {
                "video_no": cells[0],
                "title": cells[1],
                "url": cells[2],
                "woodworking_relevance": cells[3],
                "concept": cells[4],
                "products_text": cells[5],
            }
        )
    return videos


def transcript_for_video(video_no: int) -> tuple[str, str]:
    prefix = f"{video_no:03d}"
    matches = sorted(TRANSCRIPT_DIR.glob(f"{prefix}*.txt"))
    if not matches:
        return "", ""
    path = matches[0]
    return str(path.relative_to(REPO_ROOT)), read_text(path)


def parse_products() -> list[dict[str, str]]:
    products: list[dict[str, str]] = []
    for path in sorted(PRODUCT_DIR.glob("prod_*.md")):
        fields = parse_bullets(path)
        product_id = fields.get("product_id") or path.stem
        normalized = pricing_normalized(fields)
        products.append(
            {
                "product_id": product_id,
                "catalog_id": fields.get("catalog_id", ""),
                "product_name": fields.get("product_name", ""),
                "product_file": str(path.relative_to(REPO_ROOT)),
                "category": fields.get("category", ""),
                "status": fields.get("status", ""),
                "build_model": fields.get("build_model", ""),
                "reference_code": fields.get("reference_code", ""),
                "reference_source": fields.get("reference_source", ""),
                "plans_available": fields.get("plans_available", ""),
                "plans_source_ref": fields.get("plans_source_ref", ""),
                "source_links": fields.get("source_links", ""),
                "cost_sheet_ref": fields.get("cost_sheet_ref", ""),
                "verification_status": fields.get("verification_status", ""),
                "primary_use_case": fields.get("primary_use_case", ""),
                "target_buyer": fields.get("target_buyer", ""),
                "build_time_estimate": fields.get("build_time_estimate", ""),
                "lead_time_estimate": fields.get("lead_time_estimate", ""),
                "unit_cost_estimate": fields.get("unit_cost_estimate", ""),
                "materials_cost_estimate": fields.get("materials_cost_estimate", ""),
                "pricing_strategy_1_price_floor": fields.get("pricing_strategy_1_price_floor", ""),
                "pricing_strategy_2_price_floor": fields.get("pricing_strategy_2_price_floor", ""),
                "target_price": fields.get("target_price", ""),
                "margin_estimate": fields.get("margin_estimate", ""),
                "material_cost_percent_of_price": fields.get("material_cost_percent_of_price", ""),
                "recommended_price_floor": fields.get("recommended_price_floor", ""),
                "pricing_strategy_review": fields.get("pricing_strategy_review", ""),
                "pricing_validation": fields.get("pricing_validation", ""),
                **normalized,
                "next_action": fields.get("next_action", ""),
                "full_text": read_text(path),
            }
        )
    return products


def parse_crossrefs(path: Path) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    crossrefs: list[dict[str, str]] = []
    current_unmatched: list[dict[str, str]] = []
    video_gaps: list[dict[str, str]] = []
    section = ""

    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = clean_text(raw_line)
        if line.startswith("## "):
            section = line.lstrip("# ").strip()
            continue
        if not line.startswith("|") or re.match(r"^\|\s*-+", line):
            continue
        cells = split_md_table_row(line)
        if not cells:
            continue

        if section in {"Confirmed or High-Confidence Matches", "Related but Not Exact Enough for Direct Product Mapping"}:
            if len(cells) < 6 or cells[0].startswith("Current product"):
                continue
            crossrefs.append(
                {
                    "section": section,
                    "product_id": cells[0].strip("`"),
                    "product_name": cells[1],
                    "reference_code": cells[2],
                    "matched_videos": cells[3],
                    "confidence": cells[4],
                    "how_identified": cells[5],
                }
            )
        elif section == "Current Product Records With No Direct Saved-Video Match Found":
            if len(cells) < 5 or cells[0].startswith("Current product"):
                continue
            current_unmatched.append(
                {
                    "product_id": cells[0].strip("`"),
                    "product_name": cells[1],
                    "reference_code": cells[2],
                    "status": cells[3],
                    "notes": cells[4],
                }
            )
        elif section == "Video Ideas That Are Not Current Product Records Yet":
            if len(cells) < 4 or cells[0].startswith("Video idea"):
                continue
            video_gaps.append(
                {
                    "idea": cells[0],
                    "source_videos": cells[1],
                    "current_product_record": cells[2],
                    "notes": cells[3],
                }
            )

    return crossrefs, current_unmatched, video_gaps


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        DROP TABLE IF EXISTS metadata;
        DROP TABLE IF EXISTS videos;
        DROP TABLE IF EXISTS video_product_ideas;
        DROP TABLE IF EXISTS current_products;
        DROP TABLE IF EXISTS product_crossrefs;
        DROP TABLE IF EXISTS current_products_without_video_match;
        DROP TABLE IF EXISTS video_ideas_without_product_record;
        DROP TABLE IF EXISTS videos_fts;
        DROP TABLE IF EXISTS products_fts;
        DROP TABLE IF EXISTS crossrefs_fts;

        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE videos (
            video_no INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT,
            woodworking_relevance TEXT,
            concept TEXT,
            products_text TEXT,
            source_index_path TEXT,
            transcript_path TEXT,
            transcript_text TEXT
        );

        CREATE TABLE video_product_ideas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_no INTEGER NOT NULL,
            idea TEXT NOT NULL,
            FOREIGN KEY(video_no) REFERENCES videos(video_no)
        );

        CREATE TABLE current_products (
            product_id TEXT PRIMARY KEY,
            catalog_id TEXT,
            product_name TEXT,
            product_file TEXT,
            category TEXT,
            status TEXT,
            build_model TEXT,
            reference_code TEXT,
            reference_source TEXT,
            plans_available TEXT,
            plans_source_ref TEXT,
            source_links TEXT,
            cost_sheet_ref TEXT,
            verification_status TEXT,
            primary_use_case TEXT,
            target_buyer TEXT,
            build_time_estimate TEXT,
            lead_time_estimate TEXT,
            unit_cost_estimate TEXT,
            materials_cost_estimate TEXT,
            pricing_strategy_1_price_floor TEXT,
            pricing_strategy_2_price_floor TEXT,
            target_price TEXT,
            margin_estimate TEXT,
            material_cost_percent_of_price TEXT,
            recommended_price_floor TEXT,
            pricing_strategy_review TEXT,
            pricing_validation TEXT,
            materials_cost_value TEXT,
            materials_amount_status TEXT,
            materials_cost_basis TEXT,
            unit_cost_value TEXT,
            target_price_value TEXT,
            pricing_strategy_1_floor_value TEXT,
            pricing_strategy_2_floor_value TEXT,
            recommended_price_floor_value TEXT,
            material_cost_percent_value TEXT,
            pricing_status TEXT,
            costing_method TEXT,
            sale_pricing_method TEXT,
            cost_sheet_status TEXT,
            pricing_issue_flags TEXT,
            pricing_note_flags TEXT,
            pricing_next_action TEXT,
            next_action TEXT,
            full_text TEXT
        );

        CREATE TABLE product_crossrefs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section TEXT,
            product_id TEXT,
            catalog_id TEXT,
            product_name TEXT,
            reference_code TEXT,
            matched_videos TEXT,
            confidence TEXT,
            how_identified TEXT
        );

        CREATE TABLE current_products_without_video_match (
            product_id TEXT PRIMARY KEY,
            catalog_id TEXT,
            product_name TEXT,
            reference_code TEXT,
            status TEXT,
            notes TEXT
        );

        CREATE TABLE video_ideas_without_product_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idea TEXT,
            source_videos TEXT,
            current_product_record TEXT,
            notes TEXT
        );

        CREATE VIRTUAL TABLE videos_fts USING fts5(
            video_no UNINDEXED,
            title,
            concept,
            products_text,
            transcript_text
        );

        CREATE VIRTUAL TABLE products_fts USING fts5(
            product_id UNINDEXED,
            catalog_id,
            product_name,
            reference_code,
            source_links,
            primary_use_case,
            full_text
        );

        CREATE VIRTUAL TABLE crossrefs_fts USING fts5(
            row_id UNINDEXED,
            product_id,
            catalog_id,
            product_name,
            reference_code,
            matched_videos,
            how_identified
        );
        """
    )


def insert_data(conn: sqlite3.Connection) -> dict[str, int]:
    videos = parse_video_index(VIDEO_INDEX_PATH)
    products = parse_products()
    crossrefs, unmatched_products, unmatched_ideas = parse_crossrefs(CROSSREF_PATH)
    catalog_by_product_id = {product["product_id"]: product["catalog_id"] for product in products}

    conn.executemany(
        """
        INSERT INTO videos (
            video_no, title, url, woodworking_relevance, concept, products_text,
            source_index_path, transcript_path, transcript_text
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                int(video["video_no"]),
                video["title"],
                video["url"],
                video["woodworking_relevance"],
                video["concept"],
                video["products_text"],
                str(VIDEO_INDEX_PATH.relative_to(REPO_ROOT)),
                transcript_for_video(int(video["video_no"]))[0],
                transcript_for_video(int(video["video_no"]))[1],
            )
            for video in videos
        ],
    )

    idea_rows: list[tuple[int, str]] = []
    for video in videos:
        for idea in video["products_text"].split(";"):
            idea = clean_text(idea.rstrip("."))
            if idea:
                idea_rows.append((int(video["video_no"]), idea))
    conn.executemany("INSERT INTO video_product_ideas (video_no, idea) VALUES (?, ?)", idea_rows)

    conn.executemany(
        """
        INSERT INTO current_products (
            product_id, catalog_id, product_name, product_file, category, status, build_model,
            reference_code, reference_source, plans_available, plans_source_ref, source_links,
            cost_sheet_ref, verification_status, primary_use_case, target_buyer,
            build_time_estimate, lead_time_estimate, unit_cost_estimate, materials_cost_estimate,
            pricing_strategy_1_price_floor, pricing_strategy_2_price_floor, target_price,
            margin_estimate, material_cost_percent_of_price, recommended_price_floor,
            pricing_strategy_review, pricing_validation, materials_cost_value, materials_amount_status,
            materials_cost_basis, unit_cost_value, target_price_value, pricing_strategy_1_floor_value, pricing_strategy_2_floor_value,
            recommended_price_floor_value, material_cost_percent_value, pricing_status,
            costing_method, sale_pricing_method, cost_sheet_status, pricing_issue_flags,
            pricing_note_flags, pricing_next_action, next_action, full_text
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                product["product_id"],
                product["catalog_id"],
                product["product_name"],
                product["product_file"],
                product["category"],
                product["status"],
                product["build_model"],
                product["reference_code"],
                product["reference_source"],
                product["plans_available"],
                product["plans_source_ref"],
                product["source_links"],
                product["cost_sheet_ref"],
                product["verification_status"],
                product["primary_use_case"],
                product["target_buyer"],
                product["build_time_estimate"],
                product["lead_time_estimate"],
                product["unit_cost_estimate"],
                product["materials_cost_estimate"],
                product["pricing_strategy_1_price_floor"],
                product["pricing_strategy_2_price_floor"],
                product["target_price"],
                product["margin_estimate"],
                product["material_cost_percent_of_price"],
                product["recommended_price_floor"],
                product["pricing_strategy_review"],
                product["pricing_validation"],
                product["materials_cost_value"],
                product["materials_amount_status"],
                product["materials_cost_basis"],
                product["unit_cost_value"],
                product["target_price_value"],
                product["pricing_strategy_1_floor_value"],
                product["pricing_strategy_2_floor_value"],
                product["recommended_price_floor_value"],
                product["material_cost_percent_value"],
                product["pricing_status"],
                product["costing_method"],
                product["sale_pricing_method"],
                product["cost_sheet_status"],
                product["pricing_issue_flags"],
                product["pricing_note_flags"],
                product["pricing_next_action"],
                product["next_action"],
                product["full_text"],
            )
            for product in products
        ],
    )

    conn.executemany(
        """
        INSERT INTO product_crossrefs (
            section, product_id, catalog_id, product_name, reference_code, matched_videos,
            confidence, how_identified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["section"],
                row["product_id"],
                catalog_by_product_id.get(row["product_id"], ""),
                row["product_name"],
                row["reference_code"],
                row["matched_videos"],
                row["confidence"],
                row["how_identified"],
            )
            for row in crossrefs
        ],
    )

    conn.executemany(
        """
        INSERT INTO current_products_without_video_match (
            product_id, catalog_id, product_name, reference_code, status, notes
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["product_id"],
                catalog_by_product_id.get(row["product_id"], ""),
                row["product_name"],
                row["reference_code"],
                row["status"],
                row["notes"],
            )
            for row in unmatched_products
        ],
    )

    conn.executemany(
        """
        INSERT INTO video_ideas_without_product_record (
            idea, source_videos, current_product_record, notes
        )
        VALUES (?, ?, ?, ?)
        """,
        [
            (
                row["idea"],
                row["source_videos"],
                row["current_product_record"],
                row["notes"],
            )
            for row in unmatched_ideas
        ],
    )

    conn.executemany(
        "INSERT INTO videos_fts (video_no, title, concept, products_text, transcript_text) VALUES (?, ?, ?, ?, ?)",
        [
            (
                int(row["video_no"]),
                row["title"],
                row["concept"],
                row["products_text"],
                transcript_for_video(int(row["video_no"]))[1],
            )
            for row in videos
        ],
    )
    conn.executemany(
        """
        INSERT INTO products_fts (
            product_id, catalog_id, product_name, reference_code, source_links, primary_use_case, full_text
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                row["product_id"],
                row["catalog_id"],
                row["product_name"],
                row["reference_code"],
                row["source_links"],
                row["primary_use_case"],
                row["full_text"],
            )
            for row in products
        ],
    )
    conn.executemany(
        """
        INSERT INTO crossrefs_fts (
            row_id, product_id, catalog_id, product_name, reference_code, matched_videos, how_identified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                index + 1,
                row["product_id"],
                catalog_by_product_id.get(row["product_id"], ""),
                row["product_name"],
                row["reference_code"],
                row["matched_videos"],
                row["how_identified"],
            )
            for index, row in enumerate(crossrefs)
        ],
    )

    metadata = {
        "built_at": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(REPO_ROOT),
        "video_index_path": str(VIDEO_INDEX_PATH.relative_to(REPO_ROOT)),
        "crossref_path": str(CROSSREF_PATH.relative_to(REPO_ROOT)),
        "transcript_dir": str(TRANSCRIPT_DIR.relative_to(REPO_ROOT)),
        "product_dir": str(PRODUCT_DIR.relative_to(REPO_ROOT)),
    }
    conn.executemany("INSERT INTO metadata (key, value) VALUES (?, ?)", metadata.items())

    return {
        "videos": len(videos),
        "video_product_ideas": len(idea_rows),
        "current_products": len(products),
        "product_crossrefs": len(crossrefs),
        "current_products_without_video_match": len(unmatched_products),
        "video_ideas_without_product_record": len(unmatched_ideas),
    }


def build_database(db_path: Path) -> dict[str, int]:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    try:
        create_schema(conn)
        counts = insert_data(conn)
        conn.commit()
    finally:
        conn.close()
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the local Woodcraft research SQLite database.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help="Output SQLite database path.")
    args = parser.parse_args()

    db_path = args.db if args.db.is_absolute() else REPO_ROOT / args.db
    counts = build_database(db_path)
    print(f"Built {db_path}")
    for key, value in counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
