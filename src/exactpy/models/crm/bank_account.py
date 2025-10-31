from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import GUID, BankAcountTypeEnum, ExactUnixTimestamp


class BankAccountModel(ExactOnlineBaseModel):
    id: GUID
    account: GUID
    account_name: str | None = None
    bank: GUID
    bank_account: str | None = None
    bank_account_holder_name: str | None = None
    bank_description: str | None = None
    bank_name: str | None = None
    bic__code: str | None = None
    blocked: bool | None = None
    created: ExactUnixTimestamp = SparkField(spark_type="string")
    creator: GUID
    creator_full_name: str | None = None
    description: str | None = None
    division: int | None = None
    format: str | None = None
    iban__: str | None = None
    main: bool | None = None
    modified: ExactUnixTimestamp = SparkField(spark_type="string")
    modifier: GUID
    modifier_full_name: str | None = None
    payment_service_account: GUID
    type: BankAcountTypeEnum | None
    type_description: str | None = None
