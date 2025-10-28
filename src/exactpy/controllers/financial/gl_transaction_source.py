from exactpy.controllers.base import BaseController
from exactpy.models.financial import GLTransactionSourceModel


class GLTransactionSourceController(BaseController):
    _resource = "financial/GLSchemes"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = GLTransactionSourceModel
    _expand = []
