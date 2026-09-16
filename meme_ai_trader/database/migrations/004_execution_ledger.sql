CREATE TABLE IF NOT EXISTS execution_intents (
    intent_id uuid PRIMARY KEY,
    reservation_id uuid NOT NULL REFERENCES reservations(reservation_id),
    status text NOT NULL CHECK (status IN ('CREATED', 'READY', 'SUBMITTED', 'CONFIRMED', 'FINALIZED', 'UNKNOWN', 'FAILED', 'EXPIRED', 'CANCELLED')),
    created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);
CREATE TABLE IF NOT EXISTS execution_attempts (
    attempt_id uuid PRIMARY KEY,
    intent_id uuid NOT NULL REFERENCES execution_intents(intent_id),
    status text NOT NULL CHECK (status IN ('CREATED', 'SUBMITTED', 'CONFIRMED', 'FINALIZED', 'UNKNOWN', 'FAILED', 'EXPIRED')),
    created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);
