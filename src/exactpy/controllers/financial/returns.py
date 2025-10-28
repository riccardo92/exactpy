from exactpy.controllers.base import BaseController
from exactpy.models.financial import (
    ReturnModel,
)


class ReturnController(BaseController):
    _resource = "read/financial/Returns"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = ReturnModel
