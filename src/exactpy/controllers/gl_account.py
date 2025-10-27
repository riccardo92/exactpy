from exactpy.controllers import BaseController
from exactpy.models.gl_account import GLAccount


class GLAccountController(BaseController):
    _resource = "financial/GLAccounts"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = GLAccount
    _expand = [
        "DeductibilityPercentages",
    ]
