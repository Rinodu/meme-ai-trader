"""Environment-only provider configuration; no provider is enabled by default."""

from dataclasses import dataclass, field
from os import environ
from typing import Mapping
from urllib.parse import urlparse


class ProviderConfigError(ValueError):
    pass


def _bool(values: Mapping[str, str], name: str) -> bool:
    value = values.get(name, "false").strip().lower()
    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False
    raise ProviderConfigError(f"{name} must be boolean")


def _url(value: str, name: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ProviderConfigError(f"{name} must be an http(s) URL")
    return value


@dataclass(frozen=True)
class ProviderConfig:
    birdeye_enabled: bool = False
    birdeye_api_key: str | None = field(default=None, repr=False)
    solana_rpc_enabled: bool = False
    solana_rpc_url: str = "https://api.mainnet.solana.com"
    goplus_enabled: bool = False
    goplus_api_key: str | None = field(default=None, repr=False)
    goplus_token_security_url: str = "https://api.gopluslabs.io/api/v1/solana/token_security"
    telegram_enabled: bool = False
    telegram_bot_token: str | None = field(default=None, repr=False)
    telegram_allowed_chat_id: str | None = None
    llm_enabled: bool = False
    llm_monthly_budget_idr: int = 0

    @classmethod
    def from_env(cls, values: Mapping[str, str] | None = None) -> "ProviderConfig":
        values = environ if values is None else values
        birdeye = _bool(values, "MEME_AI_BIRDEYE_ENABLED")
        rpc = _bool(values, "MEME_AI_SOLANA_RPC_ENABLED")
        goplus = _bool(values, "MEME_AI_GOPLUS_ENABLED")
        telegram = _bool(values, "MEME_AI_TELEGRAM_ENABLED")
        llm = _bool(values, "MEME_AI_LLM_ENABLED")
        key = values.get("BIRDEYE_API_KEY", "").strip() or None
        if birdeye and key is None:
            raise ProviderConfigError("BIRDEYE_API_KEY is required when Birdeye is enabled")
        goplus_key = values.get("GOPLUS_API_KEY", "").strip() or None
        if goplus and goplus_key is None:
            raise ProviderConfigError("GOPLUS_API_KEY is required when GoPlus is enabled")
        token = values.get("TELEGRAM_BOT_TOKEN", "").strip() or None
        chat_id = values.get("TELEGRAM_ALLOWED_CHAT_ID", "").strip() or None
        if telegram and (token is None or chat_id is None):
            raise ProviderConfigError("Telegram token and allowlisted chat ID are required when enabled")
        try:
            budget = int(values.get("MEME_AI_LLM_MONTHLY_BUDGET_IDR", "0"))
        except ValueError as error:
            raise ProviderConfigError("LLM budget must be an integer") from error
        if budget != 0 or llm:
            raise ProviderConfigError("LLM remains disabled with Rp0 budget")
        rpc_url = _url(values.get("SOLANA_RPC_URL", cls.solana_rpc_url), "SOLANA_RPC_URL")
        goplus_url = _url(values.get("GOPLUS_TOKEN_SECURITY_URL", cls.goplus_token_security_url), "GOPLUS_TOKEN_SECURITY_URL")
        return cls(birdeye, key, rpc, rpc_url, goplus, goplus_key, goplus_url, telegram, token, chat_id, False, 0)
