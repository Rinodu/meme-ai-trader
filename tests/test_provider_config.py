import unittest

from meme_ai_trader.provider_config import ProviderConfig, ProviderConfigError


class ProviderConfigTests(unittest.TestCase):
    def test_defaults_are_disabled_and_llm_zero(self):
        config = ProviderConfig.from_env({})
        self.assertFalse(config.birdeye_enabled)
        self.assertFalse(config.solana_rpc_enabled)
        self.assertEqual(0, config.llm_monthly_budget_idr)

    def test_enabled_provider_requires_secret_or_allowlist(self):
        with self.assertRaises(ProviderConfigError):
            ProviderConfig.from_env({"MEME_AI_BIRDEYE_ENABLED": "true"})
        with self.assertRaises(ProviderConfigError):
            ProviderConfig.from_env({"MEME_AI_TELEGRAM_ENABLED": "true", "TELEGRAM_BOT_TOKEN": "x"})

    def test_secrets_are_not_in_repr(self):
        config = ProviderConfig.from_env({"MEME_AI_BIRDEYE_ENABLED": "true", "BIRDEYE_API_KEY": "secret"})
        self.assertNotIn("secret", repr(config))

    def test_llm_hard_stop(self):
        with self.assertRaises(ProviderConfigError):
            ProviderConfig.from_env({"MEME_AI_LLM_ENABLED": "true"})
        with self.assertRaises(ProviderConfigError):
            ProviderConfig.from_env({"MEME_AI_LLM_MONTHLY_BUDGET_IDR": "50000"})
