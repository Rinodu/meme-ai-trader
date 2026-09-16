import unittest
from meme_ai_trader.controls import Mode, entry_allowed, exit_allowed

class ControlTests(unittest.TestCase):
    def test_pause_and_reduce_block_entry_but_preserve_exit(self):
        for mode in (Mode.PAUSE_ENTRIES, Mode.REDUCE_ONLY):
            self.assertFalse(entry_allowed(mode))
            self.assertTrue(exit_allowed(mode))
        self.assertFalse(exit_allowed(Mode.HALT_SIGNING))
