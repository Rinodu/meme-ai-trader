from uuid import UUID, uuid4
from psycopg import Connection

class Ledger:
    _intent_transitions = {
        "CREATED": {"READY", "CANCELLED"},
        "READY": {"SUBMITTED", "CANCELLED", "EXPIRED"},
        "SUBMITTED": {"CONFIRMED", "UNKNOWN", "FAILED", "EXPIRED"},
        "CONFIRMED": {"FINALIZED"},
        "UNKNOWN": {"CONFIRMED", "FINALIZED", "FAILED", "EXPIRED"},
    }
    _attempt_transitions = {
        "CREATED": {"SUBMITTED", "FAILED", "EXPIRED"},
        "SUBMITTED": {"CONFIRMED", "UNKNOWN", "FAILED", "EXPIRED"},
        "CONFIRMED": {"FINALIZED"},
        "UNKNOWN": {"CONFIRMED", "FINALIZED", "FAILED", "EXPIRED"},
    }
    def __init__(self, connection: Connection): self.connection = connection
    def create_intent(self, reservation_id: UUID) -> UUID:
        intent_id = uuid4()
        self.connection.execute("INSERT INTO execution_intents (intent_id, reservation_id, status) VALUES (%s, %s, 'CREATED')", (intent_id, reservation_id))
        return intent_id
    def create_attempt(self, intent_id: UUID) -> UUID:
        if self.connection.execute("SELECT 1 FROM execution_attempts WHERE intent_id = %s AND status IN ('CREATED', 'SUBMITTED', 'CONFIRMED', 'UNKNOWN')", (intent_id,)).fetchone():
            raise ValueError("pending attempt must be reconciled first")
        attempt_id = uuid4()
        self.connection.execute("INSERT INTO execution_attempts (attempt_id, intent_id, status) VALUES (%s, %s, 'CREATED')", (attempt_id, intent_id))
        return attempt_id

    def pending_intents(self) -> list[tuple[UUID, UUID, str]]:
        return list(self.connection.execute("SELECT intent_id, reservation_id, status FROM execution_intents WHERE status IN ('CREATED', 'READY', 'SUBMITTED', 'CONFIRMED', 'UNKNOWN') ORDER BY created_at"))

    def pending_attempts(self) -> list[tuple[UUID, UUID, str]]:
        return list(self.connection.execute("SELECT attempt_id, intent_id, status FROM execution_attempts WHERE status IN ('CREATED', 'SUBMITTED', 'CONFIRMED', 'UNKNOWN') ORDER BY created_at"))

    def transition_intent(self, intent_id: UUID, status: str) -> None:
        self._transition("execution_intents", "intent_id", intent_id, status, self._intent_transitions)

    def transition_attempt(self, attempt_id: UUID, status: str) -> None:
        self._transition("execution_attempts", "attempt_id", attempt_id, status, self._attempt_transitions)

    def _transition(self, table: str, key: str, identifier: UUID, status: str, transitions: dict[str, set[str]]) -> None:
        row = self.connection.execute(f"SELECT status FROM {table} WHERE {key} = %s", (identifier,)).fetchone()
        if not row or status not in transitions.get(row[0], set()):
            raise ValueError(f"invalid transition to {status}")
        if not self.connection.execute(f"UPDATE {table} SET status = %s WHERE {key} = %s AND status = %s", (status, identifier, row[0])).rowcount:
            raise RuntimeError("state changed concurrently")
