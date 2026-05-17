from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ApprovalStatusEnum,
    ExactUnixTimestamp,
)
from exactpy.utils.fields import GenericField


class PayablesReceivablesListModel(ExactOnlineBaseModel):
    _pk = "hid__"
    hid__: int
    account_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    account_id: GUID = GenericField(iceberg_type="string", spark_type="string")
    account_name: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    amount_in_transit: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    approval_status: ApprovalStatusEnum | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    currency_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    due_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    entry_number: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    id: GUID | None
    invoice_date: ExactUnixTimestamp = GenericField(
        iceberg_type="timestamp", spark_type="timestamp"
    )
    invoice_number: int | None = GenericField(
        iceberg_type="integer", spark_type="integer", default=None
    )
    journal_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    journal_description: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    # todo
    # notes: List[Node]
    your_ref: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
