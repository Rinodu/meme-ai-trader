from enum import Enum


class ExecutionStatus(str, Enum):
    DISABLED = "DISABLED"


def status() -> ExecutionStatus:
    """Signal Bot never exposes a transaction execution capability."""
    return ExecutionStatus.DISABLED
