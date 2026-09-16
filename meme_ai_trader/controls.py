from enum import Enum


class Mode(Enum):
    RUNNING = "RUNNING"
    PAUSE_ENTRIES = "PAUSE_ENTRIES"
    REDUCE_ONLY = "REDUCE_ONLY"
    HALT_SIGNING = "HALT_SIGNING"


def entry_allowed(mode: Mode) -> bool:
    return mode is Mode.RUNNING


def exit_allowed(mode: Mode) -> bool:
    return mode is not Mode.HALT_SIGNING
