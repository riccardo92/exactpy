from exactpy.models.base import ExactOnlineBaseModel


class AgingOverviewByAccount(ExactOnlineBaseModel):
    _pk = "age_group"
    age_group: int | None = None
    age_group_description: str | None = None
    amount_payable: float | None = None
    amount_receivable: float | None = None
