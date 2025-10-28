from exactpy.controllers.base import BaseController
from exactpy.models.financial import OutstandingInvoicesOverviewModel


class OustandingInvoicesOverviewController(BaseController):
    _resource = "read/financial/OutstandingInvoicesOverview"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = OutstandingInvoicesOverviewModel
    _expand = []
