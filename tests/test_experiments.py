import unittest

from meme_ai_trader.experiments import freeze


class ExperimentTests(unittest.TestCase):
    def test_freeze_is_stable_and_changes_with_parameters(self):
        first = freeze("m4.2", {"warmup": 2, "threshold": "0.5"})
        self.assertEqual(first, freeze("m4.2", {"threshold": "0.5", "warmup": 2}))
        self.assertNotEqual(first.fingerprint, freeze("m4.2", {"warmup": 3, "threshold": "0.5"}).fingerprint)
