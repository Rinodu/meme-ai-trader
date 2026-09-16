import os
import unittest
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import psycopg
from psycopg import sql

from meme_ai_trader.adapters.birdeye import collect_snapshot, raw_event
from meme_ai_trader.database.feed import reconcile
from meme_ai_trader.database.raw_events import RawEventRepository, migrate
from meme_ai_trader.quant import for_mint
from meme_ai_trader.database.reservations import InsufficientFunds, ReservationRepository
from meme_ai_trader.database.ledger import Ledger


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

    def test_retry_uses_both_event_id_and_provider_identity(self):
        repo = RawEventRepository(self.connection)
        event = {
            "event_id": uuid.uuid4(),
            "source": "fixture",
            "source_event_id": "provider-1",
            "schema_version": 1,
            "chain_id": "solana-mainnet",
            "mint_address": "mint-fixture",
            "received_at": datetime(2026, 9, 15, 8, tzinfo=timezone.utc),
            "data_quality_status": "PARTIAL",
            "raw_payload": {"price": None},
        }
        first_id = repo.insert(event)
        self.assertEqual(first_id, repo.insert(event))
        self.assertEqual(first_id, repo.insert({**event, "event_id": uuid.uuid4()}))
        self.assertEqual(1, self.connection.execute("SELECT count(*) FROM raw_events").fetchone()[0])

        other = {**event, "event_id": uuid.uuid4(), "source_event_id": "provider-2"}
        repo.insert(other)
        with self.assertRaisesRegex(ValueError, "identities conflict"):
            repo.insert({**event, "source_event_id": "provider-2"})
        self.assertEqual(2, self.connection.execute("SELECT count(*) FROM raw_events").fetchone()[0])

    def test_late_event_is_ordered_but_not_visible_early(self):
        repo = RawEventRepository(self.connection)
        utc = timezone.utc
        base = {
            "source": "fixture",
            "schema_version": 1,
            "chain_id": "solana-mainnet",
            "mint_address": "mint-fixture",
            "data_quality_status": "PARTIAL",
            "raw_payload": {},
        }
        newer_id = repo.insert({
            **base, "event_id": uuid.uuid4(),
            "event_time": datetime(2026, 9, 15, 8, 1, tzinfo=utc),
            "received_at": datetime(2026, 9, 15, 8, 1, tzinfo=utc),
        })
        late_id = repo.insert({
            **base, "event_id": uuid.uuid4(),
            "event_time": datetime(2026, 9, 15, 15, 0, tzinfo=timezone(timedelta(hours=7))),
            "received_at": datetime(2026, 9, 15, 8, 5, tzinfo=utc),
        })
        no_event_time_id = repo.insert({
            **base, "event_id": uuid.uuid4(), "event_time": None,
            "received_at": datetime(2026, 9, 15, 8, 6, tzinfo=utc),
        })
        self.assertEqual(
            [newer_id],
            [row["raw_event_id"] for row in repo.available_for_mint(
                "solana-mainnet", "mint-fixture", datetime(2026, 9, 15, 8, 3, tzinfo=utc)
            )],
        )
        rows = repo.available_for_mint(
            "solana-mainnet", "mint-fixture", datetime(2026, 9, 15, 8, 7, tzinfo=utc)
        )
        self.assertEqual([late_id, newer_id, no_event_time_id], [row["raw_event_id"] for row in rows])
        self.assertEqual(datetime(2026, 9, 15, 8, tzinfo=utc), rows[0]["event_time"])
        self.assertEqual(datetime(2026, 9, 15, 8, 5, tzinfo=utc), rows[0]["received_at"])
        self.assertIsNone(rows[2]["event_time"])
        with self.assertRaisesRegex(ValueError, "event_time"):
            repo.insert({**base, "event_id": uuid.uuid4(), "event_time": datetime(2026, 9, 15, 8),
                         "received_at": datetime(2026, 9, 15, 8, tzinfo=utc)})
        with self.assertRaisesRegex(ValueError, "received_at"):
            repo.insert({**base, "event_id": uuid.uuid4(), "received_at": datetime(2026, 9, 15, 8)})
        with self.assertRaisesRegex(ValueError, "as_of"):
            repo.available_for_mint("solana-mainnet", "mint-fixture", datetime(2026, 9, 15, 8))

    def test_migration_rejects_existing_duplicates_without_deleting_raw_data(self):
        self.connection.execute("DROP INDEX raw_events_event_id_uidx")
        self.connection.execute("DROP INDEX raw_events_source_event_uidx")
        repo = RawEventRepository(self.connection)
        event = {
            "event_id": uuid.uuid4(), "source": "fixture", "schema_version": 1,
            "chain_id": "solana-mainnet", "mint_address": "mint-fixture",
            "received_at": datetime(2026, 9, 15, 8, tzinfo=timezone.utc),
            "data_quality_status": "PARTIAL", "raw_payload": {},
        }
        repo.insert(event)
        repo.insert(event)
        self.connection.commit()
        with self.assertRaises(psycopg.errors.UniqueViolation):
            migrate(self.connection)
        self.connection.rollback()
        self.assertEqual(2, self.connection.execute("SELECT count(*) FROM raw_events").fetchone()[0])

    def test_birdeye_snapshot_is_accepted_by_raw_repository(self):
        event = raw_event(
            "mint-fixture",
            {"price": 0, "mc": None, "fdv": 1, "liquidity": 0,
             "v1hUSD": 0, "buy1h": 0, "sell1h": 0, "priceChange1hPercent": 0},
            datetime(2026, 9, 15, 8, tzinfo=timezone.utc),
        )
        raw_event_id = RawEventRepository(self.connection).insert(event)
        row = self.connection.execute(
            "SELECT price, market_cap, missing_fields FROM raw_events WHERE raw_event_id = %s",
            (raw_event_id,),
        ).fetchone()
        self.assertEqual((Decimal("0"), None, ["market_cap"]), row)

    def test_reconciliation_uses_latest_available_event(self):
        repo = RawEventRepository(self.connection)
        now = datetime(2026, 9, 15, 8, 5, tzinfo=timezone.utc)
        base = {"source": "fixture", "schema_version": 1, "chain_id": "solana-mainnet",
                "mint_address": "mint-fixture", "data_quality_status": "COMPLETE", "raw_payload": {}}
        repo.insert({**base, "event_id": uuid.uuid4(), "received_at": now - timedelta(minutes=2),
                     "price": 1, "liquidity": 1})
        repo.insert({**base, "event_id": uuid.uuid4(), "received_at": now - timedelta(minutes=1),
                     "price": 0, "liquidity": 0})
        self.assertTrue(reconcile(repo, "solana-mainnet", "mint-fixture", now, timedelta(minutes=2)).ready)
        self.assertFalse(reconcile(repo, "solana-mainnet", "missing", now, timedelta(minutes=2)).ready)

    def test_collection_stores_and_assesses_snapshot(self):
        now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        client = type("Client", (), {"token_overview": lambda *_: {
            "price": 0, "mc": None, "fdv": 1, "liquidity": 0, "v1hUSD": 0,
            "buy1h": 0, "sell1h": 0, "priceChange1hPercent": 0,
        }})()
        raw_event_id, assessment = collect_snapshot(
            client, RawEventRepository(self.connection), "mint-fixture", now, timedelta(minutes=1)
        )
        self.assertTrue(assessment.ready)
        self.assertEqual(1, self.connection.execute(
            "SELECT count(*) FROM raw_events WHERE raw_event_id = %s", (raw_event_id,)
        ).fetchone()[0])

    def test_features_use_only_events_available_at_as_of(self):
        repo = RawEventRepository(self.connection)
        now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        base = {"source": "fixture", "schema_version": 1, "chain_id": "solana-mainnet",
                "mint_address": "mint-fixture", "data_quality_status": "COMPLETE", "raw_payload": {}}
        for minutes, price in ((-2, 10), (-1, 20), (1, 100)):
            repo.insert({**base, "event_id": uuid.uuid4(), "received_at": now + timedelta(minutes=minutes),
                         "event_time": now + timedelta(minutes=minutes), "price": price})
        features = for_mint(repo, "solana-mainnet", "mint-fixture", now, 2)
        self.assertTrue(features.ready)
        self.assertEqual(Decimal("1"), features.price_return)

    def test_atomic_reservation_and_idempotent_release(self):
        self.connection.execute("INSERT INTO accounts VALUES ('paper', 100)")
        repo = ReservationRepository(self.connection)
        reservation = repo.reserve("paper", Decimal("60"))
        with self.assertRaises(InsufficientFunds):
            repo.reserve("paper", Decimal("60"))
        self.assertTrue(repo.release(reservation))
        self.assertFalse(repo.release(reservation))
        self.assertEqual(Decimal("100"), self.connection.execute("SELECT available_balance FROM accounts").fetchone()[0])

    def test_intent_and_attempt_have_separate_ids(self):
        self.connection.execute("INSERT INTO accounts VALUES ('paper', 100)")
        reservation = ReservationRepository(self.connection).reserve("paper", Decimal("10"))
        ledger = Ledger(self.connection)
        intent = ledger.create_intent(reservation)
        attempt = ledger.create_attempt(intent)
        self.assertNotEqual(intent, attempt)
        self.assertEqual(("CREATED", "CREATED"), self.connection.execute(
            "SELECT i.status, a.status FROM execution_intents i JOIN execution_attempts a USING (intent_id) WHERE a.attempt_id = %s", (attempt,)
        ).fetchone())

    def test_ledger_state_machine_allows_only_valid_transitions(self):
        self.connection.execute("INSERT INTO accounts VALUES ('paper', 100)")
        ledger = Ledger(self.connection)
        intent = ledger.create_intent(ReservationRepository(self.connection).reserve("paper", Decimal("10")))
        attempt = ledger.create_attempt(intent)
        ledger.transition_intent(intent, "READY")
        ledger.transition_intent(intent, "SUBMITTED")
        ledger.transition_attempt(attempt, "SUBMITTED")
        ledger.transition_attempt(attempt, "UNKNOWN")
        ledger.transition_attempt(attempt, "CONFIRMED")
        ledger.transition_attempt(attempt, "FINALIZED")
        with self.assertRaises(ValueError):
            ledger.transition_attempt(attempt, "SUBMITTED")

    def test_restart_lists_pending_work_and_blocks_replacement_attempt(self):
        self.connection.execute("INSERT INTO accounts VALUES ('paper', 100)")
        ledger = Ledger(self.connection)
        intent = ledger.create_intent(ReservationRepository(self.connection).reserve("paper", Decimal("10")))
        attempt = ledger.create_attempt(intent)
        self.assertEqual([(attempt, intent, "CREATED")], ledger.pending_attempts())
        self.assertEqual([(intent, self.connection.execute("SELECT reservation_id FROM execution_intents WHERE intent_id = %s", (intent,)).fetchone()[0], "CREATED")], ledger.pending_intents())
        with self.assertRaises(ValueError):
            ledger.create_attempt(intent)
