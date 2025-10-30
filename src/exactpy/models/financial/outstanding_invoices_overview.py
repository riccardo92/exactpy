from exactpy.models.base import ExactOnlineBaseModel


class OutstandingInvoicesOverviewModel(ExactOnlineBaseModel):
    _pk = "currency_code"
    currency_code: str | None = None
    outstanding_payable_invoice_amount: float | None = None
    outstanding_payable_invoice_count: float | None = None
    outstanding_receivable_invoice_amount: float | None = None
    outstanding_receivable_invoice_count: float | None = None
    overdue_payable_invoice_amount: float | None = None
    overdue_payable_invoice_count: float | None = None
    overdue_receivable_invoice_amount: float | None = None
    overdue_receivable_invoice_count: float | None = None
