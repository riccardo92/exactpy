from exactpy.controllers.base import BaseController
from exactpy.models import JournalModel


class JournalController(BaseController):
    _resource = "financial/journals"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = JournalModel
