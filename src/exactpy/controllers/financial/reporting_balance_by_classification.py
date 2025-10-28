from exactpy.controllers.base import BaseController
from exactpy.models.financial import (
    ReportingBalanceByClassificationModel,
)


class ReportingBalanceByClassificationController(BaseController):
    _resource = "read/financial/ReportingBalanceByClassification"
    _mandatory_query_arg_options = ["glScheme", "reportingYear"]
    _mandatory_filter_options = []
    _model = ReportingBalanceByClassificationModel
