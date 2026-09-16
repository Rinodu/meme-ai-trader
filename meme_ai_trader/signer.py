from enum import Enum

from .controls import Mode


class SignerStatus(str, Enum):
    UNAVAILABLE = "UNAVAILABLE"
    HALTED = "HALTED"
    READY = "READY"


def status(mode: Mode, configured: bool) -> SignerStatus:
    if mode is Mode.HALT_SIGNING:
        return SignerStatus.HALTED
    return SignerStatus.READY if configured else SignerStatus.UNAVAILABLE
