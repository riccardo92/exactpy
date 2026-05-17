from exactpy.models.base import ExactOnlineBaseModel
from exactpy.utils.fields import GenericField


class AgingOverviewModel(ExactOnlineBaseModel):
    _pk = "age_group"
    age_group: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    age_group_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    amount_payable: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    amount_receivable: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    currency_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
