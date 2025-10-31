from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, ExactUnixTimestamp


class FinancialPeriodModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID
    created: ExactUnixTimestamp = SparkField(spark_type="string")
    creator: GUID
    creator_full_name: str | None = None
    division: int | None = None
    modified: ExactUnixTimestamp = SparkField(spark_type="string")
    modifier: GUID
    modifier_full_name: str | None = None
    rate: float | None = None
    source_currency: str | None = None
    source_currency_description: str | None = None
    start_date: ExactUnixTimestamp = SparkField(spark_type="string")
    target_currency: str | None = None
    target_currency_description: str | None = None
