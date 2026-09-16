def allowed(sender_id: int, command: str, senders: frozenset[int], commands: frozenset[str]) -> bool:
    return sender_id in senders and command in commands
