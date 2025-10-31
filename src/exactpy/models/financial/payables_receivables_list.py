from sparkdantic import SparkField

from exactpy.models.base import ExactOnlineBaseModel
from exactpy.types import (
    GUID,
    ApprovalStatusEnum,
    ExactUnixTimestamp,
)


class PayablesReceivablesListModel(ExactOnlineBaseModel):
    _pk = "hid__"
    hid__: int
    account_code: str | None = None
    account_id: GUID
    account_name: str | None = None
    amount: float | None = None
    amount_in_transit: float | None = None
    approval_status: ApprovalStatusEnum | None
    currency_code: str | None = None
    description: str | None = None
    due_date: ExactUnixTimestamp = SparkField(spark_type="string")
    entry_number: int | None = None
    id: GUID | None
    invoice_date: ExactUnixTimestamp = SparkField(spark_type="string")
    invoice_number: int | None = None
    journal_code: str | None = None
    journal_description: str | None = None
    # todo
    # notes: List[Node]
    your_ref: str | None = None
