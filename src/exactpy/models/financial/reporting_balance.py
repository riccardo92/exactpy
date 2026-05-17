from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, BalanceTypeEnum, ReportingBalanceStatusEnum
from exactpy.utils.fields import GenericField


class ReportingBalanceModel(ExactOnlineBaseModel):
    id: int
    amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    amount_credit: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    amount_debit: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    balance_type: BalanceTypeEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    cost_center_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    cost_center_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    cost_unit_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    cost_unit_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    count: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
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
    reporting_period: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    reporting_year: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    status: ReportingBalanceStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    type: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
