from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, BalanceTypeEnum, ReportingBalanceStatusEnum


class ReportingBalanceModel(ExactOnlineBaseModel):
    id: int
    amount: float | None = None
    amount_credit: float | None = None
    amount_debit: float | None = None
    balance_type: BalanceTypeEnum
    cost_center_code: str | None = None
    cost_center_description: str | None = None
    cost_unit_code: str | None = None
    cost_unit_description: str | None = None
    count: int | None = None
    division: int | None = None
    gl__account: GUID
    gl__account_code: str | None = None
    gl__account_description: str | None = None
    reporting_period: int | None = None
    reporting_year: int | None = None
    status: ReportingBalanceStatusEnum
    type: int | None = None
