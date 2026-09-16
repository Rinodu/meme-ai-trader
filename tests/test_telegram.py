import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from uuid import uuid4

from meme_ai_trader.telegram import Approval, allowed


class TelegramAllowlistTests(unittest.TestCase):
    def test_sender_and_command_must_both_be_allowlisted(self):
        senders, commands = frozenset({1}), frozenset({"/status"})
        self.assertTrue(allowed(1, "/status", senders, commands))
        self.assertFalse(allowed(2, "/status", senders, commands))
        self.assertFalse(allowed(1, "/approve", senders, commands))

    def test_approval_is_bound_expiring_and_single_use(self):
        now, intent = datetime(2026, 9, 16, 8, tzinfo=timezone.utc), uuid4()
        approval = Approval(intent, "mint", "BUY", Decimal("10"), now + timedelta(minutes=1))
        used = approval.consume(now, intent, "mint", "BUY", Decimal("10"))
        self.assertTrue(used.used)
        self.assertIsNone(used.consume(now, intent, "mint", "BUY", Decimal("10")))
        self.assertIsNone(approval.consume(now + timedelta(minutes=1), intent, "mint", "BUY", Decimal("10")))
