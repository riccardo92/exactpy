from exactpy.controllers import BaseController
from exactpy.models.gl_account_classification_mappings import (
    GLAccountClassificationMappings,
)


class GLAccountClassificationMappingsController(BaseController):
    _resource = "financial/GLAccountClassificationMappings"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = GLAccountClassificationMappings
