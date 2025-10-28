from exactpy.controllers.base import BaseController
from exactpy.models.financial import ExchangeRateModel


class ExchangeRateController(BaseController):
    _resource = "financial/ExchangeRates"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = ExchangeRateModel
    _expand = []
