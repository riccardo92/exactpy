from typing import Annotated, List

from pydantic import BeforeValidator

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
from exactpy.validators import nested_results_validator


class GLAccountModel(ExactOnlineBaseModel):
    _pk = "id"
    id: GUID
    allow_costs_in_sales: int | None = None
    assimilated_vat__box: int | None = None
    balance_side: BalanceSideEnum
    balance_type: BalanceTypeEnum
    belcotax_type: int | None = None
    code: str | None = None
    compress: bool | None = None
    costcenter: str | None = None
    costcenter_description: str | None = None
    costunit: str | None = None
    costunit_description: str | None = None
    created: ExactUnixTimestamp
    creator: GUID
    creator_full_name: str | None = None
    custom_field: str | None = None
    deductibility_percentages: Annotated[
        List[DeductibilityPercentageModel], BeforeValidator(nested_results_validator)
    ] = []
    description: str | None = None
    division: int | None = None
    exclude_vat__listing: int | None = None
    expense_non_deductible_percentage: float | None = None
    is_blocked: bool | None = None
    matching: bool | None = None
    modified: ExactUnixTimestamp
    modifier: GUID
    modifier_full_name: str | None = None
    private_gl__account: GUID
    private_percentage: float | None = None
    reporting_code: str | None = None
    revalue_currency: bool | None = None
    search_code: str | None = None
    type: GLAccountTypeEnum | None
    type_description: str | None = None
    use_costcenter: CostCenterEnum
    use_costunit: CostUnitEnum
    vat__code: str | None = None
    vat__description: str | None = None
    vatgl__account_type: str | None = None
    vat__non_deductible_gl__account: GUID
    vat__non_deductible_percentage: float | None = None
    vat__system: VATSystemEnum | None
    year_end_cost_gl__account: GUID
    year_end_reflection_gl__account: GUID
