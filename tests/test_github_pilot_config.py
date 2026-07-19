"""Guardrails for the approved low-cost GitHub Pages pilot."""

import json
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class GitHubPilotConfigTest(unittest.TestCase):
    def test_github_pilot_is_chinese_pages_only_and_needs_one_user_secret(self) -> None:
        config = json.loads(
            (ROOT / "data" / "config.github.json").read_text(encoding="utf-8")
        )
        workflow = (ROOT / ".github" / "workflows" / "daily-summary.yml").read_text(
            encoding="utf-8"
        )

        self.assertEqual(config["ai"]["provider"], "deepseek")
        self.assertEqual(config["ai"]["api_key_env"], "DEEPSEEK_API_KEY")
        self.assertEqual(config["ai"]["languages"], ["zh"])
        self.assertEqual(config["filtering"]["ai_score_threshold"], 7.0)
        self.assertEqual(config["filtering"]["max_items"], 15)
        self.assertFalse(config["webhook"]["enabled"])

        enabled_rss = [item for item in config["sources"]["rss"] if item["enabled"]]
        self.assertTrue(enabled_rss)
        self.assertTrue(all("${" not in item["url"] for item in enabled_rss))
        self.assertTrue(config["sources"]["hackernews"]["enabled"])
        self.assertTrue(config["sources"]["telegram"]["enabled"])
        self.assertTrue(any(item["enabled"] for item in config["sources"]["github"]))

        self.assertIn("cron: '0 23 * * *'", workflow)
        self.assertIn("secrets.DEEPSEEK_API_KEY", workflow)
        for optional_secret in (
            "secrets.OPENAI_API_KEY",
            "secrets.ANTHROPIC_API_KEY",
            "secrets.GOOGLE_API_KEY",
            "secrets.LWN_KEY",
            "secrets.HORIZON_WEBHOOK_URL",
        ):
            self.assertNotIn(optional_secret, workflow)

    def test_boss_digest_covers_four_business_themes_with_balanced_limits(self) -> None:
        config = json.loads(
            (ROOT / "data" / "config.github.json").read_text(encoding="utf-8")
        )

        self.assertEqual(config["filtering"]["ai_score_threshold"], 7.0)
        self.assertEqual(config["filtering"]["max_items"], 15)
        groups = config["filtering"]["category_groups"]
        self.assertEqual(set(groups), {"steel", "construction", "ai", "edf"})
        self.assertEqual(sum(group["limit"] for group in groups.values()), 15)

        rss = config["sources"]["rss"]
        google_news = [
            source for source in rss
            if source["url"].startswith("https://news.google.com/rss/search?")
        ]
        self.assertEqual(len(google_news), 4)
        self.assertEqual(
            {source["category"] for source in google_news},
            {"steel", "construction", "ai", "edf"},
        )
        for source in google_news:
            query = parse_qs(urlsplit(source["url"]).query)["q"][0]
            self.assertIn(" OR ", query)
            self.assertIn("(", query)
            self.assertIn(")", query)
            self.assertIn("when:1d", query)

    def test_workflow_archives_only_the_chinese_digest_and_is_serialized(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "daily-summary.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("concurrency:", workflow)
        self.assertIn("老板行业日报", workflow)
        self.assertIn("git add -- 老板行业日报/", workflow)
        self.assertNotIn("git add .", workflow)

    def test_safe_local_sync_script_is_present(self) -> None:
        script = (ROOT / "scripts" / "sync-boss-digest.ps1").read_text(
            encoding="utf-8"
        )

        self.assertTrue(script.isascii())
        for codepoint in ("0x8001", "0x677F", "0x884C", "0x4E1A", "0x65E5", "0x62A5"):
            self.assertIn(codepoint, script)
        self.assertIn("Join-Path 'D:\\Obsidian' $digestName", script)
        self.assertIn("gongjunxian720807-cyber/Horizon", script)
        self.assertNotIn("Remove-Item", script)
        self.assertNotIn("git clean", script)


if __name__ == "__main__":
    unittest.main()
