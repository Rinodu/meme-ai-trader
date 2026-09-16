import unittest
from pathlib import Path

from meme_ai_trader.config import SAFE_MODES, Settings
from meme_ai_trader.signer import ExecutionStatus, status


class SignalBotGuardTests(unittest.TestCase):
    def test_safe_modes_never_expose_execution(self):
        for mode in SAFE_MODES:
            self.assertEqual(mode, Settings.from_env({"MEME_AI_MODE": mode}).mode)
        self.assertEqual(ExecutionStatus.DISABLED, status())

    def test_runtime_has_no_wallet_or_submit_api(self):
        source = "\n".join(path.read_text(encoding="utf-8") for path in Path("meme_ai_trader").rglob("*.py"))
        for forbidden in ("private_key", "send_transaction", "/execute", "class Approval"):
            self.assertNotIn(forbidden, source.lower())
