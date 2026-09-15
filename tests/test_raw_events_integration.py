import os
import unittest
import uuid
from datetime import datetime, timezone
from decimal import Decimal

import psycopg
from psycopg import sql

from meme_ai_trader.database.raw_events import RawEventRepository, migrate


@unittest.skipUnless(os.environ.get("PGPASSWORD"), "PGPASSWORD is required")
class RawEventRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.connection = psycopg.connect("dbname=postgres host=localhost user=postgres")
        self.schema = f"test_meme_ai_{uuid.uuid4().hex}"
        self.connection.execute(
            sql.SQL("CREATE SCHEMA {}; SET search_path TO {}").format(
                sql.Identifier(self.schema), sql.Identifier(self.schema)
            )
        )
        migrate(self.connection)
        self.connection.commit()

    def tearDown(self):
        self.connection.rollback()
        self.connection.execute("SET search_path TO public")
        self.connection.execute(
            sql.SQL("DROP SCHEMA {} CASCADE").format(sql.Identifier(self.schema))
        )
        self.connection.commit()
        self.connection.close()

    def test_migration_and_raw_event_round_trip(self):
        migrate(self.connection)
        event_time = datetime(2026, 9, 15, 8, 0, tzinfo=timezone.utc)
        received_at = datetime(2026, 9, 15, 8, 0, 1, tzinfo=timezone.utc)
        raw_event_id = RawEventRepository(self.connection).insert(
            {
                "event_id": uuid.uuid4(),
                "source": "fixture",
                "schema_version": 1,
                "chain_id": "solana-mainnet",
                "mint_address": "mint-fixture",
                "event_time": event_time,
                "received_at": received_at,
                "price": Decimal("0"),
                "market_cap": None,
                "data_quality_status": "PARTIAL",
                "missing_fields": ["market_cap"],
                "raw_payload": {"price": 0, "market_cap": None},
            }
        )
        self.connection.commit()

        row = self.connection.execute(
            """SELECT event_time, received_at, price, market_cap,
                      missing_fields, raw_payload
               FROM raw_events WHERE raw_event_id = %s""",
            (raw_event_id,),
        ).fetchone()

        self.assertEqual(event_time, row[0])
        self.assertEqual(received_at, row[1])
        self.assertEqual(Decimal("0"), row[2])
        self.assertIsNone(row[3])
        self.assertEqual(["market_cap"], row[4])
        self.assertEqual({"price": 0, "market_cap": None}, row[5])
