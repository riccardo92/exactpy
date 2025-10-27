from datetime import datetime
from enum import Enum, StrEnum
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


class BalanceSideEnum(StrEnum):
    CREDIT = "c"
    DEBIT = "d"


class CostCenterEnum(Enum):
    OPTIONAL: 0
    MANDATORY: 1
    NO: 2


class CostUnitEnum(Enum):
    OPTIONAL: 0
    MANDATORY: 1
    NO: 2


class VATSystemEnum(StrEnum):
    INVOICE = "i"
    CASH = "c"


class BankAcountTypeEnum(StrEnum):
    ACCOUNT = "a"
    EMPLOYEE = "e"
    CASH = "k"
    PAYMENT_SERVICE = "p"
    BANK = "r"
    STUDENT = "s"
    UNKNOWN = "u"


class GLAccountTypeEnum(Enum):
    CASH = 10
    BANK = 12
    CREDIT_CARD = 14
    PAYMENT_SERVICES = 16
    ACCOUNTS_RECEIVABLE = 20
    PREPAYMENT_ACCOUNTS_RECEIVABLE = 21
    ACCOUNTS_PAYABLE = 22
    VAT = 24
    EMPLOYEES_PAYABLE = 25
    PREPAID_EXPENSES = 26
    ACCRUED_EXPENSES = 27
    INCOME_TAXES_PAYABLE = 29
    FIXED_ASSETS = 30
    OTHER_ASSETS = 32
    ACCUMULATED_DEPRECIATION = 35
    INVENTORY = 40
    CAPITAL_STOCK = 50
    RETAINED_EARNINGS = 52
    LONG_TERM_DEBT = 55
    CURRENT_PORTION_OF_DEBT = 60
    GENERAL = 90
    TAX_PAYABLE = 100
    REVENUE = 110
    COST_OF_GOODS = 111
    OTHER_COSTS = 120
    SALES_GENERAL_ADMINISTRATIVE_EXPENSES = 121
    DEPRECIATION_COSTS = 122
    RESEARCH_AND_DEVELOPMENT = 123
    EMPLOYEE_COSTS = 125
    EMPLOYMENT_COST = 126
    EXCEPTIONAL_COSTS = 130
    EXCEPTIONAL_INCOME = 140
    INCOME_TAXES = 150
    INTEREST_INCOME = 160
    YEAR_END_REFLECTION = 300
    INDIRECT_YEAR_END_COSTING = 301
    DIRECT_YEAR_END_COSTING = 302
