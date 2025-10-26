from exactpy.controllers import BaseController
from exactpy.models.account import Account


class ReportingBalanceByClassificationController(BaseController):
    _resource = "read/financial/ReportingBalanceByClassification"
    _mandatory_query_arg_options = ["gl_scheme", "reporting_year"]
    _mandatory_filter_options = []
    _model = Account
