from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID
from exactpy.utils.fields import GenericField


class GLAccountClassificationMappingsModel(ExactOnlineBaseModel):
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    classification: GUID = GenericField(iceberg_type="string", spark_type="string")
    classification_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    classification_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    gl__account: GUID = GenericField(iceberg_type="string", spark_type="string")
    gl__account_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    gl__account_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    gl__scheme_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    gl__scheme_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    gl__scheme_id__: GUID = GenericField(iceberg_type="string", spark_type="string")
