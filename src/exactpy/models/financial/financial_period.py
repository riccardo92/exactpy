from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, ExactUnixTimestamp
from exactpy.utils.fields import GenericField


class FinancialPeriodModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    end_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    fin_period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    fin_year: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    start_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
