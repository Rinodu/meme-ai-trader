from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from enum import StrEnum
from typing import Any


class SnapshotStatus(StrEnum):
    FRESH = "FRESH"
    STALE = "STALE"
    PARTIAL = "PARTIAL"
    MISSING = "MISSING"
    INVALID = "INVALID"


HARD_SAFETY_FIELDS = (
    "schema_version",
    "chain",
    "network",
    "mint_address",
    "observed_at",
    "source",
    "rpc_slot",
    "commitment",
    "token_supply",
    "decimals",
    "mint_authority",
    "freeze_authority",
)
OPTIONAL_FIELDS = ("holder_count", "top_holder_ratio", "liquidity", "liquidity_locked")
_NETWORKS = frozenset({"mainnet-beta", "devnet", "testnet", "localnet"})
_COMMITMENTS = frozenset({"confirmed", "finalized"})
_BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


@dataclass(frozen=True)
class OnChainSnapshot:
    schema_version: int | None
    chain: str | None
    network: str | None
    mint_address: str | None
    observed_at: datetime | None
    source: str | None
    rpc_slot: int | None
    commitment: str | None
    token_supply: Decimal | None
    decimals: int | None
    mint_authority: str | None
    freeze_authority: str | None
    holder_count: int | None
    top_holder_ratio: Decimal | None
    liquidity: Decimal | None
    liquidity_locked: bool | None
    data_status: SnapshotStatus
    missing_fields: tuple[str, ...]
    warnings: tuple[str, ...]

    def allows_signal(self) -> bool:
        return self.data_status in {SnapshotStatus.FRESH, SnapshotStatus.PARTIAL}

    def as_dict(self) -> dict[str, Any]:
        def number(value: Decimal | None) -> str | None:
            return None if value is None else str(value)

        return {
            "schema_version": self.schema_version,
            "chain": self.chain,
            "network": self.network,
            "mint_address": self.mint_address,
            "observed_at": self.observed_at.isoformat().replace("+00:00", "Z") if self.observed_at else None,
            "source": self.source,
            "rpc_slot": self.rpc_slot,
            "commitment": self.commitment,
            "token_supply": number(self.token_supply),
            "decimals": self.decimals,
            "mint_authority": self.mint_authority,
            "freeze_authority": self.freeze_authority,
            "holder_count": self.holder_count,
            "top_holder_ratio": number(self.top_holder_ratio),
            "liquidity": number(self.liquidity),
            "liquidity_locked": self.liquidity_locked,
            "data_status": self.data_status.value,
            "missing_fields": list(self.missing_fields),
            "warnings": list(self.warnings),
        }


def _timestamp(value: Any, field: str) -> datetime:
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError(f"{field} must be a valid ISO-8601 timestamp") from error
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field} must be timezone-aware")
    return value.astimezone(timezone.utc)


def _decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be numeric")
    try:
        number = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as error:
        raise ValueError(f"{field} must be numeric") from error
    if not number.is_finite():
        raise ValueError(f"{field} must be finite")
    return number


def _valid_address(value: Any) -> bool:
    if not isinstance(value, str) or not value or any(char not in _BASE58 for char in value):
        return False
    number = 0
    for char in value:
        number = number * 58 + _BASE58.index(char)
    decoded = number.to_bytes((number.bit_length() + 7) // 8, "big") if number else b""
    decoded = b"\x00" * (len(value) - len(value.lstrip("1"))) + decoded
    return len(decoded) == 32


def _empty_snapshot(status: SnapshotStatus, missing: tuple[str, ...], warning: str) -> OnChainSnapshot:
    return OnChainSnapshot(
        schema_version=None,
        chain=None,
        network=None,
        mint_address=None,
        observed_at=None,
        source=None,
        rpc_slot=None,
        commitment=None,
        token_supply=None,
        decimals=None,
        mint_authority=None,
        freeze_authority=None,
        holder_count=None,
        top_holder_ratio=None,
        liquidity=None,
        liquidity_locked=None,
        data_status=status,
        missing_fields=missing,
        warnings=(warning,),
    )


def assess_snapshot(
    snapshot: Mapping[str, Any] | None,
    current_time: datetime,
    max_snapshot_age_seconds: int = 120,
    future_tolerance_seconds: int = 5,
    expected_mint_address: str | None = None,
    expected_network: str | None = None,
    expected_rpc_slot: int | None = None,
) -> OnChainSnapshot:
    """Normalize one read-only Solana snapshot and fail closed on bad data."""
    if (
        isinstance(max_snapshot_age_seconds, bool)
        or isinstance(future_tolerance_seconds, bool)
        or not isinstance(max_snapshot_age_seconds, int)
        or not isinstance(future_tolerance_seconds, int)
        or max_snapshot_age_seconds <= 0
        or future_tolerance_seconds < 0
    ):
        raise ValueError("snapshot age must be positive and future tolerance non-negative")
    now = _timestamp(current_time, "current_time")
    if snapshot is None:
        return _empty_snapshot(SnapshotStatus.MISSING, HARD_SAFETY_FIELDS, "snapshot utama tidak tersedia")
    if not isinstance(snapshot, Mapping):
        raise ValueError("snapshot must be a mapping or None")

    missing = tuple(
        field for field in HARD_SAFETY_FIELDS
        if field not in snapshot or (snapshot.get(field) is None and field not in {"mint_authority", "freeze_authority"})
    )
    warnings: list[str] = []
    optional_missing = tuple(field for field in OPTIONAL_FIELDS if snapshot.get(field) is None)
    if missing:
        return _empty_snapshot(SnapshotStatus.INVALID, missing + optional_missing, "hard safety field tidak lengkap")

    try:
        schema_version = snapshot["schema_version"]
        if isinstance(schema_version, bool) or schema_version != 1:
            raise ValueError("schema_version tidak didukung")
        chain = snapshot["chain"]
        network = snapshot["network"]
        mint = snapshot["mint_address"]
        source = snapshot["source"]
        if chain != "solana" or not isinstance(network, str) or network not in _NETWORKS:
            raise ValueError("chain/network tidak valid")
        if not isinstance(source, str) or not source.strip():
            raise ValueError("source tidak valid")
        if not _valid_address(mint):
            raise ValueError("mint_address tidak valid")
        if expected_mint_address is not None and mint != expected_mint_address:
            raise ValueError("mint_address tidak konsisten")
        if expected_network is not None and network != expected_network:
            raise ValueError("network tidak konsisten")
        observed_at = _timestamp(snapshot["observed_at"], "observed_at")
        if observed_at > now + timedelta(seconds=future_tolerance_seconds):
            raise ValueError("observed_at berada terlalu jauh di masa depan")
        rpc_slot = snapshot["rpc_slot"]
        if isinstance(rpc_slot, bool) or not isinstance(rpc_slot, int) or rpc_slot < 0:
            raise ValueError("rpc_slot tidak valid")
        if expected_rpc_slot is not None and rpc_slot != expected_rpc_slot:
            raise ValueError("rpc_slot tidak konsisten")
        commitment = snapshot["commitment"]
        if commitment not in _COMMITMENTS:
            raise ValueError("commitment harus confirmed atau finalized")
        token_supply = _decimal(snapshot["token_supply"], "token_supply")
        if token_supply < 0:
            raise ValueError("token_supply tidak boleh negatif")
        decimals = snapshot["decimals"]
        if isinstance(decimals, bool) or not isinstance(decimals, int) or not 0 <= decimals <= 255:
            raise ValueError("decimals tidak valid")
        authorities = {}
        for field in ("mint_authority", "freeze_authority"):
            authority = snapshot[field]
            if authority is not None and not _valid_address(authority):
                raise ValueError(f"{field} tidak valid")
            authorities[field] = authority

        holder_count = snapshot.get("holder_count")
        if holder_count is not None and (isinstance(holder_count, bool) or not isinstance(holder_count, int) or holder_count < 0):
            raise ValueError("holder_count tidak valid")
        top_holder_ratio = snapshot.get("top_holder_ratio")
        if top_holder_ratio is not None:
            top_holder_ratio = _decimal(top_holder_ratio, "top_holder_ratio")
            if not 0 <= top_holder_ratio <= 1:
                raise ValueError("top_holder_ratio harus antara 0 dan 1")
        liquidity = snapshot.get("liquidity")
        if liquidity is not None:
            liquidity = _decimal(liquidity, "liquidity")
            if liquidity < 0:
                raise ValueError("liquidity tidak boleh negatif")
        liquidity_locked = snapshot.get("liquidity_locked")
        if liquidity_locked is not None and not isinstance(liquidity_locked, bool):
            raise ValueError("liquidity_locked harus boolean atau null")
    except (KeyError, TypeError, ValueError) as error:
        return _empty_snapshot(SnapshotStatus.INVALID, missing + optional_missing, str(error))

    age_seconds = (now - observed_at).total_seconds()
    status = SnapshotStatus.STALE if age_seconds > max_snapshot_age_seconds else (
        SnapshotStatus.PARTIAL if optional_missing else SnapshotStatus.FRESH
    )
    if optional_missing:
        warnings.append("field pendukung tidak tersedia")
    if status is SnapshotStatus.STALE:
        warnings.append(f"snapshot berumur {age_seconds:.3f} detik")
    return OnChainSnapshot(
        schema_version, chain, network, mint, observed_at, source, rpc_slot, commitment,
        token_supply, decimals, authorities["mint_authority"], authorities["freeze_authority"],
        holder_count, top_holder_ratio, liquidity, liquidity_locked, status,
        optional_missing, tuple(warnings)
    )
