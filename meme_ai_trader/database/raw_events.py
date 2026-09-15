from collections.abc import Mapping
from pathlib import Path
from typing import Any

from psycopg import Connection
from psycopg.types.json import Jsonb


MIGRATION = Path(__file__).with_name("migrations") / "001_raw_events.sql"

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
    RETURNING raw_event_id
"""


def migrate(connection: Connection[Any]) -> None:
    connection.execute(MIGRATION.read_text(encoding="utf-8"))


class RawEventRepository:
    def __init__(self, connection: Connection[Any]) -> None:
        self.connection = connection

    def insert(self, event: Mapping[str, Any]) -> int:
        values = {name: event.get(name) for name in _COLUMNS}
        values["missing_fields"] = event.get("missing_fields", [])
        values["raw_payload"] = Jsonb(event["raw_payload"])
        row = self.connection.execute(_INSERT, values).fetchone()
        assert row is not None
        return int(row[0])
