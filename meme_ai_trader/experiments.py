from dataclasses import dataclass
from hashlib import sha256
from typing import Mapping


@dataclass(frozen=True)
class FrozenExperiment:
    strategy_version: str
    parameters: tuple[tuple[str, str], ...]
    fingerprint: str


def freeze(strategy_version: str, parameters: Mapping[str, object]) -> FrozenExperiment:
    if not strategy_version.strip() or not parameters:
        raise ValueError("strategy version and parameters are required")
    frozen = tuple(sorted((str(key), str(value)) for key, value in parameters.items()))
    payload = repr((strategy_version, frozen)).encode()
    return FrozenExperiment(strategy_version, frozen, sha256(payload).hexdigest())
