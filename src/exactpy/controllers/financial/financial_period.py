from exactpy.controllers.base import BaseController
from exactpy.models.financial import FinancialPeriodModel


class FinancialPeriodController(BaseController):
    _resource = "financial/FinancialPeriods"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = FinancialPeriodModel
    _expand = []
