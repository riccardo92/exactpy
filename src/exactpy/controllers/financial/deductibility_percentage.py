from exactpy.controllers.base import BaseController
from exactpy.models.financial import DeductibilityPercentageModel


class DeductibilityPercentageController(BaseController):
    _resource = "financial/DeductibilityPercentages"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = DeductibilityPercentageModel
    _expand = []
