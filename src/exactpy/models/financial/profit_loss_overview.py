from exactpy.models.base import ExactOnlineBaseModel


class ProfitLossOverviewModel(ExactOnlineBaseModel):
    _pk = "current_year"
    current_year: int
    costs_current_period: float | None = None
    costs_current_year: float | None = None
    costs_previous_year: float | None = None
    costs_previous_year_period: float | None = None
    currency_code: str | None = None
    current_period: int | None = None
    previous_year: int | None = None
    previous_year_period: int | None = None
    result_current_period: float | None = None
    result_current_year: float | None = None
    result_previous_year: float | None = None
    result_previous_year_period: float | None = None
    revenue_current_period: float | None = None
    revenue_current_year: float | None = None
    revenue_previous_year: float | None = None
    revenue_previous_year_period: float | None = None
