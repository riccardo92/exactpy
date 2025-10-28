from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    JournalFrequencyEnum,
    ReturnSourceEnum,
)


class OfficialReturnModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID
    amount: float | None = None
    created: ExactUnixTimestamp
    creator: GUID
    creator_full_name: str | None = None
    description: str | None = None
    division: int | None = None
    document: GUID
    document_subject: str | None = None
    frequency: JournalFrequencyEnum | None
    is_correction: int | None = None
    modified: ExactUnixTimestamp
    modifier: GUID
    modifier_full_name: str | None = None
    period: int | None = None
    presentation_data: str | None = None
    presentation_date: ExactUnixTimestamp
    presentation_file: bytes | None = None
    presentation_file_name: str | None = None
    reference: str | None = None
    source: ReturnSourceEnum | None
    status: int | None = None
    type: int | None = None
    type_description: str | None = None
    year: int | None = None
