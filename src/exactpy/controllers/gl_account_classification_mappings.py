from exactpy.controllers.base import BaseController
from exactpy.models import (
    GLAccountClassificationMappingsModel,
)


class GLAccountClassificationMappingsController(BaseController):
    _resource = "financial/glaccountclassificationmappings"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = GLAccountClassificationMappingsModel
