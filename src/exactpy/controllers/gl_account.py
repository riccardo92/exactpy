from exactpy.controllers.base import BaseController
from exactpy.models import GLAccountModel


class GLAccountController(BaseController):
    _resource = "financial/glaccounts"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = GLAccountModel
    _expand = [
        "DeductibilityPercentages",
    ]
