from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    ReturnFrequencyEnum,
    ReturnStatusEnum,
    ReturnTypeEnum,
)
from exactpy.utils.fields import GenericField


class ReturnModel(ExactOnlineBaseModel):
    document_id: GUID = GenericField(iceberg_type="string", spark_type="string")
    amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    currency: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    document_view_url: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    due_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    frequency: ReturnFrequencyEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    payroll_declaration_type: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    period_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    request: GUID = GenericField(iceberg_type="string", spark_type="string")
    status: ReturnStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    subject: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    type: ReturnTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    year: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
