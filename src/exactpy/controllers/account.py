from exactpy.controllers import BaseController
from exactpy.models.account import Account


class AccountController(BaseController):
    _resource = "crm/Accounts"
    _mandatory_filter_options = []
    _model = Account
