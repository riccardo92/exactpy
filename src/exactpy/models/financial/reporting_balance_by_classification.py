from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, BalanceTypeEnum


class ReportingBalanceByClassificationModel(ExactOnlineBaseModel):
    id: GUID
    amount: float | None = None
    amount_credit: float | None = None
    amount_debit: float | None = None
    balance_type: BalanceTypeEnum | None
    classification_code: str | None = None
    classification_description: str | None = None
    cost_center_code: str | None = None
    cost_center_description: str | None = None
    cost_unit_code: str | None = None
    cost_unit_description: str | None = None
    count: str | None = None
    division: str | None = None
    gl__account: GUID
    gl__account_code: str | None = None
    gl__account_description: str | None = None
    gl__scheme: GUID
    reporting_period: int | None = None
    reporting_year: int | None = None
    status: int | None = None
    type: int | None = None
