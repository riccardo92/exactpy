from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    ReturnFrequencyEnum,
    ReturnStatusEnum,
    ReturnTypeEnum,
)


class ReturnModel(ExactOnlineBaseModel):
    document_id: GUID
    amount: float | None = None
    created: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    currency: str | None = None
    description: str | None = None
    document_view_url: str | None = None
    due_date: ExactUnixTimestamp = SparkField(spark_type="timestamp")
    frequency: ReturnFrequencyEnum
    payroll_declaration_type: str | None = None
    period: int | None = None
    period_description: str | None = None
    request: GUID
    status: ReturnStatusEnum
    subject: str | None = None
    type: ReturnTypeEnum
    year: int | None = None
