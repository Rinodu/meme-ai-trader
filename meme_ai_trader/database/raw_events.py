from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from psycopg import Connection
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb


MIGRATIONS = Path(__file__).with_name("migrations")

_COLUMNS = (
    "event_id",
    "source",
    "source_event_id",
    "schema_version",
    "chain_id",
    "mint_address",
    "pool_address",
    "token_program",
    "decimals",
    "event_time",
    "received_at",
    "source_slot",
    "commitment",
    "price",
    "quote_currency",
    "market_cap",
    "fdv",
    "liquidity",
    "volume_1m",
    "volume_5m",
    "volume_15m",
    "volume_1h",
    "buy_count",
    "sell_count",
    "unique_buyer_wallets",
    "unique_seller_wallets",
    "price_change_1m",
    "price_change_5m",
    "price_change_15m",
    "price_change_1h",
    "data_quality_status",
    "missing_fields",
    "raw_payload",
)

_INSERT = f"""
    INSERT INTO raw_events ({", ".join(_COLUMNS)})
    VALUES ({", ".join(f"%({name})s" for name in _COLUMNS)})
    ON CONFLICT DO NOTHING
    RETURNING raw_event_id
"""


def migrate(connection: Connection[Any]) -> None:
    for migration in sorted(MIGRATIONS.glob("*.sql")):
        connection.execute(migration.read_text(encoding="utf-8"))


def _utc(value: Any, name: str) -> datetime:
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise ValueError(f"{name} must be a timezone-aware datetime")
    return value.astimezone(timezone.utc)


class RawEventRepository:
    def __init__(self, connection: Connection[Any]) -> None:
        self.connection = connection

    def insert(self, event: Mapping[str, Any]) -> int:
        values = {name: event.get(name) for name in _COLUMNS}
        values["received_at"] = _utc(values["received_at"], "received_at")
        if values["event_time"] is not None:
            values["event_time"] = _utc(values["event_time"], "event_time")
        values["missing_fields"] = event.get("missing_fields", [])
        values["raw_payload"] = Jsonb(event["raw_payload"])
        row = self.connection.execute(_INSERT, values).fetchone()
        if row is not None:
            return int(row[0])
        rows = self.connection.execute(
            """SELECT raw_event_id FROM raw_events
               WHERE event_id = %(event_id)s
                  OR (source = %(source)s AND source_event_id = %(source_event_id)s
                      AND %(source_event_id)s IS NOT NULL)""",
            values,
        ).fetchall()
        if len(rows) != 1:
            raise ValueError("event identities conflict; no raw event was changed")
        return int(rows[0][0])

    def available_for_mint(
        self, chain_id: str, mint_address: str, as_of: datetime
    ) -> list[dict[str, Any]]:
        with self.connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """SELECT * FROM raw_events
                   WHERE chain_id = %s AND mint_address = %s AND received_at <= %s
                   ORDER BY event_time ASC NULLS LAST, received_at ASC, raw_event_id ASC""",
                (chain_id, mint_address, _utc(as_of, "as_of")),
            )
            return cursor.fetchall()

    def latest_for_mint(
        self, chain_id: str, mint_address: str, as_of: datetime
    ) -> dict[str, Any] | None:
        with self.connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """SELECT * FROM raw_events
                   WHERE chain_id = %s AND mint_address = %s AND received_at <= %s
                   ORDER BY received_at DESC, raw_event_id DESC LIMIT 1""",
                (chain_id, mint_address, _utc(as_of, "as_of")),
            )
            return cursor.fetchone()
