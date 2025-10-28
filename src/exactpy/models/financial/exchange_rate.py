from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, ExactUnixTimestamp


class ExchangeRateModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID
    created: ExactUnixTimestamp
    creator: GUID
    creator_full_name: str | None = None
    division: int | None = None
    modified: ExactUnixTimestamp
    modifier: GUID
    modifier_full_name: str | None = None
    rate: float | None = None
    source_currency: str | None = None
    source_currency_description: str | None = None
    start_date: ExactUnixTimestamp
    target_currency: str | None = None
    target_currency_description: str | None = None
