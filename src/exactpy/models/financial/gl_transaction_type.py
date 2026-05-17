from exactpy.models.base import ExactOnlineBaseModel
from exactpy.utils.fields import GenericField


class GLTransactionTypeModel(ExactOnlineBaseModel):
    id: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description_suffix: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
