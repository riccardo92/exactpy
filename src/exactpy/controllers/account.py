from exactpy.controllers.base import BaseController
from exactpy.models import AccountModel


class AccountController(BaseController):
    _resource = "crm/Accounts"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = AccountModel
