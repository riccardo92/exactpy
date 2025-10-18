from __future__ import annotations

from typing import TYPE_CHECKING, List, Type

from pydantic import BaseModel, TypeAdapter

from exactpy.exceptions import NoFilterSetException

if TYPE_CHECKING:
    from exactpy.client import Client


class BaseController:
    _resource: str
    _mandatory_filter_options: List[str]
    _model: Type[BaseModel]

    def __init__(
        self,
        client: Client,
    ):
        self._client = client

    def show(self, id: int):
        return self._model.model_validate_json(
            self._client.get(resource=self.resource, id=id)
        )

    def all(self, filters: List[str] = []):
        if len(self._mandatory_filter_options) > 0 and len(filters) == 0:
            raise NoFilterSetException(
                f"This model requires a mandatory filter. Choices are '{', '.join(self._mandatory_filter_options)}"
            )
        adapter = TypeAdapter(List[self._model])
        return adapter.validate_json(
            self._client.get(resource=self.resource, filters=filters)
        )
