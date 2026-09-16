import unittest

from meme_ai_trader.signer import ExecutionStatus, status


class ExecutionBoundaryTests(unittest.TestCase):
    def test_execution_is_always_disabled(self):
        self.assertEqual(ExecutionStatus.DISABLED, status())
