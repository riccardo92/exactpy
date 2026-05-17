from typing import Annotated, List

from pydantic import BeforeValidator
from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.models.financial import DeductibilityPercentageModel
from exactpy.types import (
    GUID,
    BalanceSideEnum,
    BalanceTypeEnum,
    CostCenterEnum,
    CostUnitEnum,
    ExactUnixTimestamp,
    GLAccountTypeEnum,
    VATSystemEnum,
)
from exactpy.utils.fields import GenericField
from exactpy.validators import nested_results_validator


class GLAccountModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    allow_costs_in_sales: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    assimilated_vat__box: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    balance_side: BalanceSideEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    balance_type: BalanceTypeEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    belcotax_type: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    compress: bool | None = None
    costcenter: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    costcenter_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    costunit: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    costunit_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    custom_field: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    deductibility_percentages: Annotated[
        List[DeductibilityPercentageModel], BeforeValidator(nested_results_validator)
    ] = SparkField(default=[], exclude=True)
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    division: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    exclude_vat__listing: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    expense_non_deductible_percentage: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    is_blocked: bool | None = None
    matching: bool | None = None
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    private_gl__account: GUID = GenericField(iceberg_type="string", spark_type="string")
    private_percentage: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    reporting_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    revalue_currency: bool | None = None
    search_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    type: GLAccountTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    use_costcenter: CostCenterEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    use_costunit: CostUnitEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    vat__code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    vat__description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    vatgl__account_type: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    vat__non_deductible_gl__account: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
    vat__non_deductible_percentage: float | None = GenericField(
        iceberg_type="double", spark_type="double", default=None
    )
    vat__system: VATSystemEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    year_end_cost_gl__account: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
    year_end_reflection_gl__account: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
