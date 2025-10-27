from exactpy.controllers.base import BaseController
from exactpy.models import MeModel


class MeController(BaseController):
    _resource = "current/Me"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = MeModel

    def all(self):
        raise NotImplementedError("Method not implemented in this controller.")

    def show(self, **kwargs):
        r = self._client.get(
            resource=self._resource,
            include_division=False,
        )

        return self._model.model_validate(r.json()["d"]["results"][0])
