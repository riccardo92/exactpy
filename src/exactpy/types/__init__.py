from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BeforeValidator, PlainSerializer

from exactpy.serializers import exact_unix_transformer
from exactpy.validators import exact_unix_validator, guid_validator

ExactUnixTimestamp = Annotated[
    datetime | None,
    BeforeValidator(exact_unix_validator),
    PlainSerializer(exact_unix_transformer),
]

GUID = Annotated[str | None, BeforeValidator(guid_validator)]


class BalanceTypeEnum(StrEnum):
    BALANCE_SHEET = "b"
    PROFIT_AND_LOSS = "w"


class BankAcountTypeEnum(StrEnum):
    ACCOUNT = "a"
    EMPLOYEE = "e"
    CASH = "k"
    PAYMENT_SERVICE = "p"
    BANK = "r"
    STUDENT = "s"
    UNKNOWN = "u"
