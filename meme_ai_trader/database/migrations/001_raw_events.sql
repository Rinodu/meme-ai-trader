CREATE TABLE IF NOT EXISTS raw_events (
    raw_event_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    event_id uuid NOT NULL,
    source text NOT NULL,
    source_event_id text,
    schema_version integer NOT NULL CHECK (schema_version > 0),
    chain_id text NOT NULL,
    mint_address text NOT NULL,
    pool_address text,
    token_program text,
    decimals smallint CHECK (decimals BETWEEN 0 AND 255),
    event_time timestamptz,
    received_at timestamptz NOT NULL,
    source_slot bigint CHECK (source_slot >= 0),
    commitment text,
    price numeric CHECK (price >= 0),
    quote_currency text,
    market_cap numeric CHECK (market_cap >= 0),
    fdv numeric CHECK (fdv >= 0),
    liquidity numeric CHECK (liquidity >= 0),
    volume_1m numeric CHECK (volume_1m >= 0),
    volume_5m numeric CHECK (volume_5m >= 0),
    volume_15m numeric CHECK (volume_15m >= 0),
    volume_1h numeric CHECK (volume_1h >= 0),
    buy_count bigint CHECK (buy_count >= 0),
    sell_count bigint CHECK (sell_count >= 0),
    unique_buyer_wallets bigint CHECK (unique_buyer_wallets >= 0),
    unique_seller_wallets bigint CHECK (unique_seller_wallets >= 0),
    price_change_1m numeric,
    price_change_5m numeric,
    price_change_15m numeric,
    price_change_1h numeric,
    data_quality_status text NOT NULL,
    missing_fields text[] NOT NULL DEFAULT '{}',
    raw_payload jsonb NOT NULL,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);

CREATE INDEX IF NOT EXISTS raw_events_received_at_idx
    ON raw_events (received_at);

CREATE INDEX IF NOT EXISTS raw_events_mint_event_time_idx
    ON raw_events (chain_id, mint_address, event_time);
