CREATE UNIQUE INDEX IF NOT EXISTS raw_events_event_id_uidx
    ON raw_events (event_id);

CREATE UNIQUE INDEX IF NOT EXISTS raw_events_source_event_uidx
    ON raw_events (source, source_event_id)
    WHERE source_event_id IS NOT NULL;
