from exactpy.controllers.base import BaseController
from exactpy.models import (
    ReportingBalanceByClassificationModel,
)


class ReportingBalanceByClassificationController(BaseController):
    _resource = "read/financial/reportingbalancebyclassification"
    _mandatory_query_arg_options = ["gl_scheme", "reporting_year"]
    _mandatory_filter_options = []
    _model = ReportingBalanceByClassificationModel
