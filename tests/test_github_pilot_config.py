"""Guardrails for the approved low-cost GitHub Pages pilot."""

import json
import unittest
from pathlib import Path


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
        self.assertEqual(config["filtering"]["ai_score_threshold"], 8.0)
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


if __name__ == "__main__":
    unittest.main()
