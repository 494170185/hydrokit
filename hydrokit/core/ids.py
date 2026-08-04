"""ID helpers."""
import secrets
import time


def new_id(prefix: str = "hk") -> str:
    ts = int(time.time() * 1000)
    return f"{prefix}_{ts:x}_{secrets.token_hex(5)}"
