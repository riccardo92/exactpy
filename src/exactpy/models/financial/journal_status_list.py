from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    JournalStatusEnum,
    JournalTypeEnum,
)


class JournalStatusListModel(ExactOnlineBaseModel):
    journal: str | None = None
    period: int | None = None
    year: int | None = None
    journal_description: str | None = None
    journal_type: JournalTypeEnum
    journal_type_description: str | None = None
    status: JournalStatusEnum | None
    status_description: str | None = None
