from exactpy.controllers.base import BaseController
from exactpy.models.financial import OfficialReturnModel


class OfficialReturnController(BaseController):
    _resource = "financial/OfficialReturns"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = OfficialReturnModel
    _expand = []
