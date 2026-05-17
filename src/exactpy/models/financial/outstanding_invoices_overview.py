from exactpy.models.base import ExactOnlineBaseModel
from exactpy.utils.fields import GenericField


class OutstandingInvoicesOverviewModel(ExactOnlineBaseModel):
    _pk = "currency_code"
    currency_code: str | None = GenericField(
        iceberg_type="string", spark_type="string", default=None
    )
    outstanding_payable_invoice_amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    outstanding_payable_invoice_count: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    outstanding_receivable_invoice_amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    outstanding_receivable_invoice_count: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    overdue_payable_invoice_amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    overdue_payable_invoice_count: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    overdue_receivable_invoice_amount: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
    overdue_receivable_invoice_count: float | None = GenericField(
        iceberg_type="float", spark_type="float", default=None
    )
