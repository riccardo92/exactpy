from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    JournalStatusEnum,
    JournalTypeEnum,
)
from exactpy.utils.fields import GenericField


class JournalStatusListModel(ExactOnlineBaseModel):
    journal: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    year: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    journal_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    journal_type: JournalTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    journal_type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    status: JournalStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    status_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
