from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
)


class DeductibilityPercentageModel(ExactOnlineBaseModel):
    id: GUID
    created: ExactUnixTimestamp
    creator: GUID
    creator_full_name: str | None = None
    division: int | None = None
    end_date: ExactUnixTimestamp
    expense_non_deductible_percentage: float | None = None
    gl_account: GUID
    line_number: int | None = None
    modified: ExactUnixTimestamp
    modifier: GUID
    modifier_full_name: str | None = None
    private_use_percentage: float | None = None
    start_date: ExactUnixTimestamp
    vat__non_deductible_percentage: float | None = None
