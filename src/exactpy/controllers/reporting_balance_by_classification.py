from exactpy.controllers import BaseController
from exactpy.models.account import Account


class AccountController(BaseController):
    _resource = "crm/Accounts"
    _mandatory_query_arg_options = ["gl_scheme", "reporting_year"]
    _mandatory_filter_options = []
    _model = Account
