from uuid import UUID, uuid4
from psycopg import Connection

class Ledger:
    def __init__(self, connection: Connection): self.connection = connection
    def create_intent(self, reservation_id: UUID) -> UUID:
        intent_id = uuid4()
        self.connection.execute("INSERT INTO execution_intents (intent_id, reservation_id, status) VALUES (%s, %s, 'CREATED')", (intent_id, reservation_id))
        return intent_id
    def create_attempt(self, intent_id: UUID) -> UUID:
        attempt_id = uuid4()
        self.connection.execute("INSERT INTO execution_attempts (attempt_id, intent_id, status) VALUES (%s, %s, 'CREATED')", (attempt_id, intent_id))
        return attempt_id
