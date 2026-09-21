"""Read-only Solana JSON-RPC client."""

import json
from collections.abc import Callable, Mapping, Sequence
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class SolanaRPCError(RuntimeError):
    pass


class SolanaRPCRateLimit(SolanaRPCError):
    pass


class SolanaRPCClient:
    def __init__(self, url: str, opener: Callable[..., Any] = urlopen, timeout: float = 10.0) -> None:
        if not url.startswith(("http://", "https://")):
            raise ValueError("Solana RPC URL must be http(s)")
        self._url, self._opener, self._timeout = url, opener, timeout

    def request(self, method: str, params: Sequence[Any] = ()) -> Any:
        body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": list(params)}).encode()
        request = Request(self._url, data=body, headers={"Accept": "application/json", "Content-Type": "application/json"})
        try:
            with self._opener(request, timeout=self._timeout) as response:
                if response.status == 429:
                    raise SolanaRPCRateLimit("Solana RPC rate limit")
                if response.status != 200:
                    raise SolanaRPCError(f"Solana RPC request failed ({response.status})")
                payload = json.loads(response.read())
        except SolanaRPCError:
            raise
        except (HTTPError, URLError, TimeoutError) as error:
            raise SolanaRPCError("Solana RPC network or timeout failure") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise SolanaRPCError("Solana RPC returned invalid JSON") from error
        if not isinstance(payload, Mapping):
            raise SolanaRPCError("Solana RPC response must be an object")
        if payload.get("error") is not None:
            raise SolanaRPCError("Solana RPC returned an error")
        if "result" not in payload or payload["result"] is None:
            raise SolanaRPCError("Solana RPC result is missing")
        return payload["result"]

    def account_info(self, address: str, commitment: str = "confirmed") -> Any:
        if commitment not in {"confirmed", "finalized"}:
            raise ValueError("commitment must be confirmed or finalized")
        return self.request("getAccountInfo", [address, {"encoding": "jsonParsed", "commitment": commitment}])

    def token_supply(self, mint_address: str, commitment: str = "confirmed") -> Any:
        if commitment not in {"confirmed", "finalized"}:
            raise ValueError("commitment must be confirmed or finalized")
        return self.request("getTokenSupply", [mint_address, {"commitment": commitment}])
