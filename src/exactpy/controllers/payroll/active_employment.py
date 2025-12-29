from exactpy.controllers.base import BaseController
from exactpy.models.payroll import ActiveEmployment


class ActiveEmploymentController(BaseController):
    _resource = "payroll/ActiveEmployments"
    _model = ActiveEmployment
