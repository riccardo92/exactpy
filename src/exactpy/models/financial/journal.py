from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    GLAccountTypeEnum,
    JournalTypeEnum,
    PaymentServiceProviderTypeEnum,
)


class JournalModel(ExactOnlineBaseModel):
    id: GUID
    allow_variable_currency: bool | None = None
    allow_variable_exchange_rate: bool | None = None
    allow_vat__: bool | None = None
    auto_save: bool | None = None
    bank: GUID
    bank_account_bic_code: str | None = None
    bank_account_country: str | None = None
    bank_account_description: str | None = None
    bank_account_iban: str | None = None
    bank_account_id: GUID
    bank_account_including_mask: str | None = None
    bank_account_use_sepa: bool | None = None
    bank_account_use_sepa_direct_debit: bool | None = None
    bank_name: str | None = None
    code: str | None = None
    created: ExactUnixTimestamp = SparkField(spark_type="str")
    creator: GUID
    creator_full_name: str | None = None
    currency: str | None = None
    currency_description: str | None = None
    custom_field: str | None = None
    description: str | None = None
    division: int | None = None
    gl__account: GUID
    gl__account_code: str | None = None
    gl__account_description: str | None = None
    gl__account_type: GLAccountTypeEnum
    is_blocked: bool | None = None
    modified: ExactUnixTimestamp = SparkField(spark_type="str")
    modifier: GUID
    modifier_full_name: str | None = None
    payment_in_transit_account: GUID
    payment_service_account_identifier: str | None = None
    payment_service_provider: PaymentServiceProviderTypeEnum | None = None
    payment_service_provider_name: str | None = None
    type: JournalTypeEnum
