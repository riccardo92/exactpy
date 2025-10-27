from exactpy.controllers import BaseController
from exactpy.models.journal import Journal


class JournalController(BaseController):
    _resource = "financial/journals"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = Journal
