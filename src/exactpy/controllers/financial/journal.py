from exactpy.controllers.base import BaseController
from exactpy.models.financial import JournalModel


class JournalController(BaseController):
    _resource = "financial/Journals"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = JournalModel
