from decimal import Decimal
from uuid import UUID, uuid4

from psycopg import Connection


class InsufficientFunds(ValueError):
    pass


class ReservationRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    def reserve(self, account_id: str, amount: Decimal) -> UUID:
        if amount <= 0:
            raise ValueError("amount must be positive")
        with self.connection.transaction():
            row = self.connection.execute(
                "UPDATE accounts SET available_balance = available_balance - %s WHERE account_id = %s AND available_balance >= %s RETURNING account_id",
                (amount, account_id, amount),
            ).fetchone()
            if row is None:
                raise InsufficientFunds("insufficient available balance")
            reservation_id = uuid4()
            self.connection.execute("INSERT INTO reservations (reservation_id, account_id, amount) VALUES (%s, %s, %s)", (reservation_id, account_id, amount))
            return reservation_id

    def release(self, reservation_id: UUID) -> bool:
        with self.connection.transaction():
            row = self.connection.execute("UPDATE reservations SET released_at = clock_timestamp() WHERE reservation_id = %s AND released_at IS NULL RETURNING account_id, amount", (reservation_id,)).fetchone()
            if row is None:
                return False
            self.connection.execute("UPDATE accounts SET available_balance = available_balance + %s WHERE account_id = %s", (row[1], row[0]))
            return True
