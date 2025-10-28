from exactpy.controllers.base import BaseController
from exactpy.models.financial import (
    ReportingBalanceModel,
)


class ReportingBalanceController(BaseController):
    _resource = "financial/ReportingBalance"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = ReportingBalanceModel
