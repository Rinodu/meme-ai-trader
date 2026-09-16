import unittest

from meme_ai_trader.telegram import allowed


class TelegramAllowlistTests(unittest.TestCase):
    def test_sender_and_command_must_both_be_allowlisted(self):
        senders, commands = frozenset({1}), frozenset({"/status"})
        self.assertTrue(allowed(1, "/status", senders, commands))
        self.assertFalse(allowed(2, "/status", senders, commands))
        self.assertFalse(allowed(1, "/approve", senders, commands))
