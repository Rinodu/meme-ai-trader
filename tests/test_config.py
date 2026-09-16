import unittest

from meme_ai_trader.config import ConfigError, Settings


class SettingsTests(unittest.TestCase):
    def test_default_is_collect_only(self):
        settings = Settings.from_env({})
        self.assertEqual("collect_only", settings.mode)
        self.assertFalse(settings.birdeye_enabled)
        self.assertIsNone(settings.birdeye_api_key)

    def test_only_signal_bot_modes_are_accepted(self):
        for mode in ("collect_only", "replay", "paper_signal"):
            self.assertEqual(mode, Settings.from_env({"MEME_AI_MODE": mode}).mode)
        with self.assertRaisesRegex(ConfigError, "paper_signal"):
            Settings.from_env({"MEME_AI_MODE": "live_auto"})

    def test_invalid_feature_flag_is_rejected(self):
        with self.assertRaisesRegex(ConfigError, "must be true or false"):
            Settings.from_env({"MEME_AI_BIRDEYE_ENABLED": "sometimes"})

    def test_birdeye_key_is_required_only_when_enabled(self):
        Settings.from_env({"MEME_AI_BIRDEYE_ENABLED": "false"})
        with self.assertRaisesRegex(ConfigError, "BIRDEYE_API_KEY is required"):
            Settings.from_env({"MEME_AI_BIRDEYE_ENABLED": "true"})

    def test_secret_is_not_shown_in_repr(self):
        secret = "do-not-print-this"
        settings = Settings.from_env(
            {"MEME_AI_BIRDEYE_ENABLED": "true", "BIRDEYE_API_KEY": secret}
        )
        self.assertNotIn(secret, repr(settings))


if __name__ == "__main__":
    unittest.main()
