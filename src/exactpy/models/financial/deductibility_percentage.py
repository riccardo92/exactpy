from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, ExactUnixTimestamp


class DeductibilityPercentageModel(ExactOnlineBaseModel):
    id: GUID
    created: ExactUnixTimestamp = SparkField(spark_type="string")
    creator: GUID
    creator_full_name: str | None = None
    division: int | None = None
    end_date: ExactUnixTimestamp = SparkField(spark_type="string")
    expense_non_deductible_percentage: float | None = None
    gl__account: GUID
    line_number: int | None = None
    modified: ExactUnixTimestamp = SparkField(spark_type="string")
    modifier: GUID
    modifier_full_name: str | None = None
    private_use_percentage: float | None = None
    start_date: ExactUnixTimestamp = SparkField(spark_type="string")
    vat__non_deductible_percentage: float | None = None
