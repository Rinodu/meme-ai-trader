import unittest

from meme_ai_trader.controls import Mode
from meme_ai_trader.signer import SignerStatus, status


class SignerBoundaryTests(unittest.TestCase):
    def test_halt_wins_and_missing_signer_is_unavailable(self):
        self.assertEqual(SignerStatus.UNAVAILABLE, status(Mode.RUNNING, False))
        self.assertEqual(SignerStatus.HALTED, status(Mode.HALT_SIGNING, True))
        self.assertEqual(SignerStatus.READY, status(Mode.RUNNING, True))
