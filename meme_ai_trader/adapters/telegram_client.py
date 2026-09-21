"""Allowlist-only Telegram sender for private diagnostic/signal messages."""

import json
from collections.abc import Callable, Mapping
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class TelegramError(RuntimeError):
    pass


class TelegramRateLimit(TelegramError):
    pass


class TelegramClient:
    def __init__(self, bot_token: str, allowed_chat_id: str, opener: Callable[..., Any] = urlopen, timeout: float = 10.0) -> None:
        if not bot_token or not allowed_chat_id:
            raise ValueError("Telegram token and allowlisted chat ID are required")
        self._url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        self._allowed_chat_id, self._opener, self._timeout = str(allowed_chat_id), opener, timeout

    def send_message(self, chat_id: str, text: str) -> Mapping[str, Any]:
        if str(chat_id) != self._allowed_chat_id:
            raise TelegramError("chat is not allowlisted")
        if not text.strip():
            raise ValueError("message text is required")
        body = json.dumps({"chat_id": str(chat_id), "text": text}).encode()
        request = Request(self._url, data=body, headers={"Accept": "application/json", "Content-Type": "application/json"})
        try:
            with self._opener(request, timeout=self._timeout) as response:
                if response.status == 429:
                    raise TelegramRateLimit("Telegram rate limit")
                if response.status != 200:
                    raise TelegramError(f"Telegram request failed ({response.status})")
                payload = json.loads(response.read())
        except TelegramError:
            raise
        except (HTTPError, URLError, TimeoutError) as error:
            raise TelegramError("Telegram network or timeout failure") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise TelegramError("Telegram returned invalid JSON") from error
        if not isinstance(payload, Mapping) or payload.get("ok") is not True:
            raise TelegramError("Telegram returned an unsuccessful response")
        result = payload.get("result")
        if not isinstance(result, Mapping):
            raise TelegramError("Telegram message result is missing")
        return result

    def send_test(self, chat_id: str, text: str) -> Mapping[str, Any]:
        if not text.startswith("TEST "):
            raise ValueError("diagnostic messages must start with TEST")
        return self.send_message(chat_id, text)
