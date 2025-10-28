from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
)


class AgingPayablesReceivablesListModel(ExactOnlineBaseModel):
    _pk = "account_id"
    account_id: GUID
    account_code: str | None = None
    account_name: str | None = None
    age_group1: int | None = None
    age_group1_amount: int | None = None
    age_group1_description: str | None = None
    age_group2: int | None = None
    age_group2_amount: int | None = None
    age_group2_description: str | None = None
    age_group3: int | None = None
    age_group3_amount: int | None = None
    age_group3_description: str | None = None
    age_group4: int | None = None
    age_group4_amount: float | None = None
    age_group4_description: str | None = None
    currency_code: str | None = None
    total_amount: int | None = None
