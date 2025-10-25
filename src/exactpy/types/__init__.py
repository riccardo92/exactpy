from datetime import datetime
from typing import Annotated

from pydantic import BeforeValidator, PlainSerializer

from exactpy.serializers import exact_unix_transformer
from exactpy.validators import exact_unix_validator, guid_validator

ExactUnixTimestamp = Annotated[
    datetime | None,
    BeforeValidator(exact_unix_validator),
    PlainSerializer(exact_unix_transformer),
]

Guid = Annotated[str | None, BeforeValidator(guid_validator)]
