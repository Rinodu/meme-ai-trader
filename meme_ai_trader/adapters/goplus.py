"""Read-only GoPlus Solana token security client."""

import json
from collections.abc import Callable, Mapping
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class GoPlusError(RuntimeError):
    pass


class GoPlusRateLimit(GoPlusError):
    pass


class GoPlusClient:
    def __init__(self, api_key: str, url: str, opener: Callable[..., Any] = urlopen, timeout: float = 10.0) -> None:
        if not api_key:
            raise ValueError("GoPlus API key is required")
        if not url.startswith(("http://", "https://")):
            raise ValueError("GoPlus URL must be http(s)")
        self._api_key, self._url, self._opener, self._timeout = api_key, url, opener, timeout

    def token_security(self, mint_address: str) -> Mapping[str, Any]:
        if not mint_address.strip():
            raise ValueError("mint_address is required")
        request = Request(
            f"{self._url}?{urlencode({'contract_addresses': mint_address})}",
            headers={"Accept": "application/json", "Authorization": self._api_key},
        )
        try:
            with self._opener(request, timeout=self._timeout) as response:
                if response.status == 429:
                    raise GoPlusRateLimit("GoPlus rate limit")
                if response.status != 200:
                    raise GoPlusError(f"GoPlus request failed ({response.status})")
                payload = json.loads(response.read())
        except GoPlusError:
            raise
        except (HTTPError, URLError, TimeoutError) as error:
            raise GoPlusError("GoPlus network or timeout failure") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise GoPlusError("GoPlus returned invalid JSON") from error
        if not isinstance(payload, Mapping) or payload.get("code") not in {1, "1"}:
            raise GoPlusError("GoPlus returned an unsuccessful response")
        result = payload.get("result")
        if not isinstance(result, Mapping) or not result:
            raise GoPlusError("GoPlus security data is missing")
        return result
