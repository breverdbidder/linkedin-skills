"""Everest fork guardrails: see EVEREST.md."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
REMOVED = ["linkedin-comment-drafter", "linkedin-reply-handler", "linkedin-thread-monitor",
           "linkedin-engager-analytics", "linkedin-employee-advocacy"]
KEYS = ["PUBLORA_API_KEY", "APIFY_TOKEN", "PIXFARO_API_KEY"]


class EverestPolicy(unittest.TestCase):
    def test_removed_skills_stay_removed(self):
        for name in REMOVED:
            for base in (ROOT / "skills", ROOT / ".claude" / "skills"):
                self.assertFalse((base / name).exists(), f"{name} came back in {base} (EVEREST.md)")

    def test_no_publishing_or_scraping_key_is_tracked(self):
        for env in (ROOT / ".env", ROOT / ".env.local"):
            if env.exists():
                text = env.read_text()
                for k in KEYS:
                    self.assertNotRegex(text, rf"(?m)^{k}=\S", f"{k} set in {env.name} (EVEREST.md rule 1)")

    def test_story_bank_figures_carry_a_source(self):
        bank = (ROOT / "references" / "story-bank.md").read_text()
        receipts = bank.split("## 2. Receipts", 1)[1].split("\n## ", 1)[0]
        for line in receipts.splitlines():
            if line.startswith("- ") and "$" in line:
                self.assertIn("Source:", line, f"unsourced figure in Story Bank: {line}")


if __name__ == "__main__":
    unittest.main()
