CREATE TABLE IF NOT EXISTS accounts (
    account_id text PRIMARY KEY,
    available_balance numeric NOT NULL CHECK (available_balance >= 0)
);

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id uuid PRIMARY KEY,
    account_id text NOT NULL REFERENCES accounts(account_id),
    amount numeric NOT NULL CHECK (amount > 0),
    released_at timestamptz
);
