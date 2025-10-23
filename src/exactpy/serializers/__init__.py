from datetime import datetime


def exact_unix_transformer(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    return f"/Date({int(dt.timestamp() * 1000)})/"
