from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ExactUnixTimestamp,
    GLAccountTypeEnum,
    JournalTypeEnum,
    PaymentServiceProviderTypeEnum,
)
from exactpy.utils.fields import GenericField


class JournalModel(ExactOnlineBaseModel):
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    allow_variable_currency: bool | None = None
    allow_variable_exchange_rate: bool | None = None
    allow_vat__: bool | None = None
    auto_save: bool | None = None
    bank: GUID = GenericField(iceberg_type="string", spark_type="string")
    bank_account_bic_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_country: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_iban: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_id: GUID = GenericField(iceberg_type="string", spark_type="string")
    bank_account_including_mask: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_use_sepa: bool | None = None
    bank_account_use_sepa_direct_debit: bool | None = None
    bank_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    created: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    creator: GUID = GenericField(iceberg_type="string", spark_type="string")
    creator_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    currency: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    currency_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    custom_field: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description: str | None = GenericField(
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
    gl__account_type: GLAccountTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    is_blocked: bool | None = None
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    payment_in_transit_account: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
    payment_service_account_identifier: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    payment_service_provider: PaymentServiceProviderTypeEnum = GenericField(
        iceberg_type="integer", spark_type="integer"
    )
    payment_service_provider_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    type: JournalTypeEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
