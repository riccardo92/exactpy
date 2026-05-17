from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, BankAcountTypeEnum, ExactUnixTimestamp
from exactpy.utils.fields import GenericField


class BankAccountModel(ExactOnlineBaseModel):
    id: GUID = GenericField(iceberg_type="string", spark_type="string")
    account: GUID = GenericField(iceberg_type="string", spark_type="string")
    account_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank: GUID = GenericField(iceberg_type="string", spark_type="string")
    bank_account: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_account_holder_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bank_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    bic__code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    blocked: bool | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
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
        iceberg_type="string", spark_type="string", default=None
    )
    format: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    iban__: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    main: bool | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    modified: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    modifier: GUID = GenericField(iceberg_type="string", spark_type="string")
    modifier_full_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    payment_service_account: GUID = GenericField(
        iceberg_type="string", spark_type="string"
    )
    type: BankAcountTypeEnum | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    type_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
