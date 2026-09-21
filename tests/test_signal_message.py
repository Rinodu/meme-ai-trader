import unittest
from datetime import datetime, timezone

from meme_ai_trader.signal_message import SignalMessage, format_signal


class SignalMessageTests(unittest.TestCase):
    def test_message_contains_required_manual_signal_fields(self):
        text = format_signal(SignalMessage("mint", "TOK", "momentum", "volume naik", "1-2", "<1", "3", "exit di target", "30m", "likuiditas turun", datetime(2026, 9, 16, 8, tzinfo=timezone.utc), "80", "HIGH"))
        for field in ("mint", "Alasan", "Bukti", "Entry", "Invalidation/stop", "Target", "Exit", "Maks hold", "Exit awal", "Kedaluwarsa", "bukan probabilitas profit"):
            self.assertIn(field, text)
