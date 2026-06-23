from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TOOLKIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLKIT))

import audit_workspace
import consolidate_learning_candidates
import refresh_live_indexes
import session_repo_briefing


class AuditWorkspaceTests(unittest.TestCase):
    def make_root(self) -> tempfile.TemporaryDirectory[str]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "90_archive").mkdir()
        return temp

    def test_default_scan_excludes_archive(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "live.md").write_text("[bad](missing.md)", encoding="utf-8")
        (root / "90_archive" / "historical.md").write_text("[old](also-missing.md)", encoding="utf-8")

        self.assertEqual(1, len(audit_workspace.find_broken_links(root, False)))
        self.assertEqual(2, len(audit_workspace.find_broken_links(root, True)))

    def test_retired_reference_is_reported(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "retired.md").write_text("Status: Retired\n", encoding="utf-8")
        (root / "live.md").write_text("Read retired.md only for traceability.\n", encoding="utf-8")

        retired = audit_workspace.find_retired_files(root, False)
        findings = audit_workspace.find_retired_references(root, retired, False)
        self.assertEqual(["retired.md"], sorted(retired))
        self.assertEqual(1, len(findings))

    def test_mojibake_is_detected(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "bad.md").write_text("Bad \u00c3\u00a9 text\n", encoding="utf-8")

        findings = audit_workspace.find_mojibake(root, False)
        self.assertEqual("error", findings[0].severity)

    def test_raw_source_mojibake_is_ignored(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        source = root / "20_research" / "catalog_exports" / "source"
        source.mkdir(parents=True)
        (source / "raw.md").write_text("Raw \u00c3\u00a9 text\n", encoding="utf-8")

        findings = audit_workspace.find_mojibake(root, False)
        self.assertEqual([], findings)

    def test_long_duplicate_is_classified(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        repeated = "This is intentionally long repeated guidance text that exceeds one hundred characters so the duplicate-guidance classifier will inspect it safely."
        (root / "00_START_HERE.md").write_text(repeated, encoding="utf-8")
        (root / "03_GOVERNANCE.md").write_text(repeated, encoding="utf-8")

        findings = audit_workspace.find_duplicate_guidance(root, False)
        self.assertEqual(1, len(findings))
        self.assertIn("choose canonical owner", findings[0].detail)

    def test_workflow_document_classifier_includes_rules_and_excludes_instance_records(self) -> None:
        self.assertTrue(audit_workspace.is_workflow_document("00_brand/VOICE.md"))
        self.assertTrue(audit_workspace.is_workflow_document("40_listings/prompts/listing_prompt.md"))
        self.assertTrue(audit_workspace.is_workflow_document("80_templates/social_post_template.md"))
        self.assertTrue(audit_workspace.is_workflow_document("30_products/product_to_family_conversion_workflow.md"))
        self.assertTrue(audit_workspace.is_workflow_document("50_content/facebook_brand_post_rules.md"))
        self.assertTrue(audit_workspace.is_workflow_document("60_automation/workspace_maintenance/audit_workspace.md"))
        self.assertFalse(audit_workspace.is_workflow_document("30_products/prod_cedar_planter_001.md"))
        self.assertFalse(audit_workspace.is_workflow_document("40_listings/list_marketplace_planter_001.md"))
        self.assertFalse(audit_workspace.is_workflow_document("50_content/content_fbpage_planter_001.md"))
        self.assertFalse(audit_workspace.is_workflow_document("20_research/notes.md"))
        self.assertFalse(audit_workspace.is_workflow_document("90_archive/old_workflow.md"))

    def test_workflow_trace_baseline_is_persistent_only_when_written(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        workflow = root / "40_listings" / "variant_scope_marketplace_listing_workflow.md"
        workflow.parent.mkdir()
        workflow.write_text("# Workflow\n", encoding="utf-8")

        first = audit_workspace.build_workflow_trace(root)
        self.assertFalse(first.baseline_exists)
        self.assertEqual(["initial"], [change.change_type for change in first.changes])
        self.assertFalse(audit_workspace.workflow_trace_baseline_path(root).exists())

        audit_workspace.write_workflow_trace_baseline(root, first.fingerprints)
        second = audit_workspace.build_workflow_trace(root)
        self.assertTrue(second.baseline_exists)
        self.assertEqual([], second.changes)

        workflow.write_text("# Workflow\n\nChanged\n", encoding="utf-8")
        third = audit_workspace.build_workflow_trace(root)
        self.assertEqual(["modified"], [change.change_type for change in third.changes])
        self.assertEqual(first.fingerprints, audit_workspace.load_workflow_trace_baseline(root))

    def test_workflow_change_classification_handles_add_rename_and_remove(self) -> None:
        previous = {"old.md": "same", "modified.md": "old", "removed.md": "gone"}
        current = {"renamed.md": "same", "modified.md": "new", "added.md": "added"}

        changes = audit_workspace.classify_workflow_changes(previous, current)

        self.assertEqual(
            [
                ("added.md", "added", None),
                ("modified.md", "modified", None),
                ("renamed.md", "renamed", "old.md"),
                ("removed.md", "removed", None),
            ],
            [(change.path, change.change_type, change.previous_path) for change in changes],
        )

    def test_package_trace_follows_links_and_reports_proven_findings(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name in audit_workspace.GOVERNANCE_ROOTS:
            (root / name).write_text(f"# {name}\n", encoding="utf-8")
        workflow = root / "40_listings" / "variant_scope_marketplace_listing_workflow.md"
        workflow.parent.mkdir()
        rules = root / "50_content" / "facebook_brand_post_rules.md"
        rules.parent.mkdir()
        child = root / "40_listings" / "linked_rules.md"
        retired = root / "40_listings" / "retired_rule.md"
        archived = root / "90_archive" / "retired.md"
        long_rule = "This active rule is deliberately long enough to be detected as an exact repeated rule in this package trace without relying on prose heuristics."
        workflow.write_text(
            "[child](linked_rules.md)\n"
            "[retired](retired_rule.md)\n"
            "[archive](../90_archive/retired.md)\n"
            "[missing](missing.md)\n"
            f"{long_rule}\n",
            encoding="utf-8",
        )
        child.write_text(f"[brand](../00_brand/VOICE.md)\n{long_rule}\n", encoding="utf-8")
        (root / "00_brand").mkdir()
        (root / "00_brand" / "VOICE.md").write_text("# Voice\n", encoding="utf-8")
        rules.write_text("[workflow](../40_listings/variant_scope_marketplace_listing_workflow.md)\n", encoding="utf-8")
        retired.write_text("Status: Retired\n", encoding="utf-8")
        archived.write_text("Status: Retired\n", encoding="utf-8")

        live_paths = {audit_workspace.rel(path, root): path for path in audit_workspace.markdown_files(root, False)}
        outgoing, incoming = audit_workspace.build_live_link_index(root, live_paths)
        trace = audit_workspace.build_package_trace(
            root,
            audit_workspace.WorkflowChange("40_listings/variant_scope_marketplace_listing_workflow.md", "modified"),
            live_paths,
            outgoing,
            incoming,
            audit_workspace.find_retired_files(root, False),
        )

        self.assertIn("00_START_HERE.md", trace.members)
        self.assertIn("40_listings/linked_rules.md", trace.members)
        self.assertIn("00_brand/VOICE.md", trace.members)
        self.assertIn("50_content/facebook_brand_post_rules.md", trace.members)
        self.assertNotIn("90_archive/retired.md", trace.members)
        self.assertEqual(
            [("40_listings/variant_scope_marketplace_listing_workflow.md", 1)],
            [(link.source, link.line) for link in trace.link_evidence if link.resolved == "40_listings/linked_rules.md"],
        )
        self.assertTrue(any(finding.category == "package-broken-relative-link" and finding.line == 4 for finding in trace.findings))
        self.assertTrue(any(finding.category == "retired-reference" and finding.line == 2 for finding in trace.findings))
        self.assertTrue(any(finding.category == "package-repeated-guidance" for finding in trace.findings))

    def test_package_duplicate_guidance_ignores_intentional_prompt_and_template_copy(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        prompt = root / "50_content" / "prompts" / "prompt.md"
        template = root / "80_templates" / "template.md"
        prompt.parent.mkdir(parents=True)
        template.parent.mkdir()
        repeated = "This standalone prompt rule is deliberately long enough to prove that intentional prompt and template copies remain excluded from redundancy warnings."
        prompt.write_text(repeated, encoding="utf-8")
        template.write_text(repeated, encoding="utf-8")

        findings = audit_workspace.find_package_duplicate_guidance(
            root,
            ["50_content/prompts/prompt.md", "80_templates/template.md"],
        )

        self.assertEqual([], findings)

    def test_trace_report_and_status_include_baseline_summary(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        workflow = root / "40_listings" / "variant_scope_marketplace_listing_workflow.md"
        workflow.parent.mkdir()
        workflow.write_text("# Workflow\n", encoding="utf-8")
        trace = audit_workspace.build_workflow_trace(root)
        report = audit_workspace.render_report(root, [], False, trace)

        self.assertIn("## Workflow Package Trace", report)
        written = audit_workspace.write_report(root, report, trace)
        status = (root / "60_automation" / "workspace_maintenance" / "CURRENT_MAINTENANCE_STATUS.md").read_text(encoding="utf-8")

        self.assertTrue(written.exists())
        self.assertTrue(audit_workspace.workflow_trace_baseline_path(root).exists())
        self.assertIn("Workflow package trace: 1 changed workflow documents", status)

    def test_package_broken_link_is_not_counted_twice_in_summary(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        workflow = root / "40_listings" / "variant_scope_marketplace_listing_workflow.md"
        workflow.parent.mkdir()
        workflow.write_text("[missing](missing.md)\n", encoding="utf-8")

        trace = audit_workspace.build_workflow_trace(root)
        report = audit_workspace.render_report(
            root,
            audit_workspace.find_broken_links(root, False),
            False,
            trace,
        )

        self.assertIn("- Errors: 1", report)


class RefreshLiveIndexesTests(unittest.TestCase):
    def test_outputs_are_deterministic_and_exclude_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            (root / "00_brand").mkdir()
            (root / "20_research" / "competitor_snapshots" / "sample").mkdir(parents=True)
            (root / "60_automation" / "workspace_maintenance").mkdir(parents=True)
            (root / "live.md").write_text("# Live\n", encoding="utf-8")
            (root / "90_archive").mkdir()
            (root / "90_archive" / "hidden.md").write_text("# Historical\n", encoding="utf-8")
            (root / "60_automation" / "workspace_maintenance" / "WORKFLOW_TRACE_BASELINE.json").write_text(
                "{}\n",
                encoding="utf-8",
            )

            first = refresh_live_indexes.expected_outputs(root)
            second = refresh_live_indexes.expected_outputs(root)
            self.assertEqual(first, second)
            live_map = next(iter(first.values()))
            self.assertNotIn("hidden.md", live_map)
            self.assertNotIn("WORKFLOW_TRACE_BASELINE.json", live_map)


class LearningConsolidationTests(unittest.TestCase):
    def test_only_new_decisions_are_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            toolkit = root / "60_automation" / "workspace_maintenance"
            toolkit.mkdir(parents=True)
            (root / "90_archive" / "maintenance_audits").mkdir(parents=True)
            (toolkit / "MAINTENANCE_LEARNINGS.md").write_text(
                f"Last decision reviewed: {chr(96)}DEC-096{chr(96)}\n",
                encoding="utf-8",
            )
            (root / "12_DECISION_LOG.md").write_text(
                "| 2026-06-22 | DEC-096 | Baseline | Existing |\n"
                "| 2026-06-23 | DEC-097 | New pattern | Candidate |\n",
                encoding="utf-8",
            )
            report = root / "90_archive" / "maintenance_audits" / "audit.md"
            report.write_text("- Errors: 0\n- Warnings: 1\n", encoding="utf-8")
            (toolkit / "CURRENT_MAINTENANCE_STATUS.md").write_text(
                "Last audit: [audit.md](../../90_archive/maintenance_audits/audit.md)\n",
                encoding="utf-8",
            )

            rendered = consolidate_learning_candidates.render(root)
            self.assertIn("DEC-097", rendered)
            self.assertNotIn("| DEC-096 |", rendered)
            self.assertIn("- Warnings: 1", rendered)
            (toolkit / "LEARNING_REVIEW.md").write_text(rendered, encoding="utf-8")
            self.assertEqual(
                0,
                consolidate_learning_candidates.main(["--root", str(root), "--check"]),
            )


class SessionRepoBriefingTests(unittest.TestCase):
    def make_root(self) -> tempfile.TemporaryDirectory[str]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "60_automation" / "workspace_maintenance").mkdir(parents=True)
        (root / "30_products").mkdir()
        (root / "40_listings").mkdir()
        (root / "50_content").mkdir()
        (root / "70_ads").mkdir()
        (root / "13_BACKLOG.md").write_text(
            "# Backlog\n\n## Now (Highest Priority)\n\n"
            "1. First priority\n2. Second priority\n3. Third priority\n4. Fourth priority\n\n"
            "## Soon\n\n1. Later priority\n",
            encoding="utf-8",
        )
        (root / "40_listings" / "facebook_marketplace_catalog_rollout_2026-06-03.md").write_text(
            "## Next Three Actions\n\n1. Finish first action\n2. Finish second action\n3. Finish third action\n",
            encoding="utf-8",
        )
        (root / "30_products" / "prod_one.md").write_text("- status: Candidate\n", encoding="utf-8")
        (root / "40_listings" / "list_one.md").write_text("- publish_status: Draft\n", encoding="utf-8")
        (root / "50_content" / "content_draft.md").write_text(
            "- content_id: draft-post\n- platform: Instagram\n- publish_status: Draft\n- publish_date:\n",
            encoding="utf-8",
        )
        (root / "50_content" / "content_ready.md").write_text(
            "- content_id: ready-post\n- platform: FB Page\n- publish_status: Ready to Schedule\n- publish_date: 2026-06-23\n",
            encoding="utf-8",
        )
        (root / "60_automation" / "workspace_maintenance" / "CURRENT_MAINTENANCE_STATUS.md").write_text(
            "Last audit: [audit](../../90_archive/maintenance_audits/maintenance_audit_2026-06-14_120000.md)\n"
            "- Errors: 0\n- Warnings: 2\n",
            encoding="utf-8",
        )
        return temp

    def test_eastern_date_boundary(self) -> None:
        utc = ZoneInfo("UTC")
        before_midnight = datetime(2026, 6, 23, 3, 59, tzinfo=utc)
        after_midnight = datetime(2026, 6, 23, 4, 1, tzinfo=utc)
        self.assertEqual(date(2026, 6, 22), session_repo_briefing.eastern_today(before_midnight))
        self.assertEqual(date(2026, 6, 23), session_repo_briefing.eastern_today(after_midnight))

    def test_confirmation_phrase_is_stable(self) -> None:
        self.assertEqual("Brief me", session_repo_briefing.CONFIRMATION_PHRASE)
        repo_root = TOOLKIT.parents[1]
        instruction_files = (
            "AGENTS.md",
            "CODEX.md",
            "CLAUDE.md",
            ".cursorrules",
            ".clinerules",
            "00_START_HERE.md",
            "03_GOVERNANCE.md",
            "60_automation/workspace_maintenance/session_repo_briefing.md",
        )
        for relative_path in instruction_files:
            text = (repo_root / relative_path).read_text(encoding="utf-8")
            self.assertIn(session_repo_briefing.CONFIRMATION_PHRASE, text, relative_path)

    def test_due_current_and_idempotent_write(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        briefing_day = date(2026, 6, 22)

        self.assertEqual("due", session_repo_briefing.status(root, briefing_day)[0])
        first, created, report = session_repo_briefing.write_briefing(root, briefing_day)
        second, created_again, same_report = session_repo_briefing.write_briefing(root, briefing_day)

        self.assertTrue(created)
        self.assertFalse(created_again)
        self.assertEqual(report, same_report)
        self.assertEqual(first, second)
        self.assertEqual("current", session_repo_briefing.status(root, briefing_day)[0])
        self.assertEqual(1, len(list((root / "90_archive" / "session_briefings").glob("*.md"))))
        self.assertNotIn(report, list(audit_workspace.markdown_files(root, False)))

    def test_summary_separates_schedules_drafts_campaigns_and_stale_maintenance(self) -> None:
        temp = self.make_root()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)

        briefing = session_repo_briefing.render_briefing(root, date(2026, 6, 22))
        self.assertIn("No active ad campaign records exist", briefing)
        self.assertIn("Scheduled or ready: ready-post on FB Page", briefing)
        self.assertIn("Drafts awaiting schedule: 1.", briefing)
        self.assertIn("overdue by more than one week", briefing)
        self.assertNotIn("Scheduled or ready: draft-post", briefing)


if __name__ == "__main__":
    unittest.main()
