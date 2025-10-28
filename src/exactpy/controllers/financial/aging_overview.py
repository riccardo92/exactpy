from exactpy.controllers.base import BaseController
from exactpy.models.financial import AgingOverviewModel


class AgingOverviewController(BaseController):
    _resource = "read/financial/AgingOverview"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = AgingOverviewModel
    _expand = []


class AgingOverviewByAccountController(BaseController):
    _resource = "/read/financial/AgingOverviewByAccount"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = AgingOverviewModel
    _expand = []
