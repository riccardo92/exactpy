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
    created: ExactUnixTimestamp
    currency: str | None = None
    description: str | None = None
    document_view_url: str | None = None
    due_date: ExactUnixTimestamp
    frequency: ReturnFrequencyEnum
    payroll_declaration_type: str | None = None
    period: int | None = None
    period_description: str | None = None
    request: GUID
    status: ReturnStatusEnum
    subject: str | None = None
    type: ReturnTypeEnum
    year: int | None = None
