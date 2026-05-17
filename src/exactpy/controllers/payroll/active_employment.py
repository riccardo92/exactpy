from exactpy.controllers.base import BaseController
from exactpy.models.payroll import ActiveEmploymentModel


class ActiveEmploymentController(BaseController):
    _resource = "payroll/ActiveEmployments"
    _model = ActiveEmploymentModel
