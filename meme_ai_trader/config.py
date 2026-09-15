from dataclasses import dataclass, field
from os import environ
from typing import Mapping


class ConfigError(ValueError):
    pass


def _boolean(values: Mapping[str, str], name: str) -> bool:
    raw = values.get(name, "false").strip().lower()
    if raw in {"1", "true", "yes", "on"}:
        return True
    if raw in {"0", "false", "no", "off"}:
        return False
    raise ConfigError(f"{name} must be true or false")


@dataclass(frozen=True)
class Settings:
    mode: str
    birdeye_enabled: bool
    birdeye_api_key: str | None = field(repr=False)

    @classmethod
    def from_env(cls, values: Mapping[str, str] | None = None) -> "Settings":
        values = environ if values is None else values
        mode = values.get("MEME_AI_MODE", "collect_only").strip().lower()
        if mode != "collect_only":
            raise ConfigError("MEME_AI_MODE currently supports only collect_only")

        birdeye_enabled = _boolean(values, "MEME_AI_BIRDEYE_ENABLED")
        birdeye_api_key = values.get("BIRDEYE_API_KEY", "").strip() or None
        if birdeye_enabled and birdeye_api_key is None:
            raise ConfigError("BIRDEYE_API_KEY is required when Birdeye is enabled")

        return cls(mode, birdeye_enabled, birdeye_api_key if birdeye_enabled else None)
