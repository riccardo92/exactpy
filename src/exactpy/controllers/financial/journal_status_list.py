from exactpy.controllers.base import BaseController
from exactpy.models.financial import JournalStatusListModel


class JournalStatusListController(BaseController):
    _resource = "read/financial/JournalStatusList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = JournalStatusListModel
    _expand = []
