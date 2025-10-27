from typing import List

from exactpy.models import ExactOnlineBaseModel
from exactpy.models.deductibility_percentage import DeductibilityPercentage
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


class GLAccount(ExactOnlineBaseModel):
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
    deductibility_percentages: List[DeductibilityPercentage]
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
    type: GLAccountTypeEnum
    type_description: str | None = None
    use_costcenter: CostCenterEnum
    use_costunit: CostUnitEnum
    vat__code: str | None = None
    vat__description: str | None = None
    vatgl__account_type: str | None = None
    vat__non_deductible_gl_account: GUID
    vat__non_deductible_percentage: float | None = None
    vat__system: VATSystemEnum
    year_end_cost_gl_account: GUID
    year_end_reflection_gl_account: GUID
