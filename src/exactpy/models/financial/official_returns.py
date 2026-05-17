from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    JournalFrequencyEnum,
    ReturnSourceEnum,
)
from exactpy.utils.fields import GenericField


class OfficialReturnModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    amount: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    document: GUID = GenericField(iceberg_type="string", spark_type="string")
    document_subject: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    frequency: JournalFrequencyEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    is_correction: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    presentation_data: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    presentation_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    presentation_file: bytes | None = GenericField(
        iceberg_type="binary", spark_type="binary", default=None
    )
    presentation_file_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    reference: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    source: ReturnSourceEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    status: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    type: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    year: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
