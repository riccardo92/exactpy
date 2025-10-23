import re
from datetime import datetime
from typing import Any

from pydantic import ValidationError


def exact_unix_validator(value: Any) -> datetime | None:
    if value is None:
        return None

    if isinstance(value, str) and re.match(r"\/Date\((\d{13})\)\/", value):
        ts = int(re.sub(r"\/Date\((\d{13})\)\/", r"\1", value))
        return datetime.fromtimestamp(ts / 1000)

    raise ValidationError(
        "Input value does not correspond to exact online unix timestamp (string embedded 13-digit millisecond Unix timestamp) format (e.g. '/Date(1758283747417)/')"
    )
