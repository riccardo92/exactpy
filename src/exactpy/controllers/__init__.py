from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Type, Union

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

    def show(self, primary_key_value: Union[str, int], primary_key: str = "ID"):
        """_summary_

        Args:
            primary_key_value (Union[str, int]): _description_
            primary_key (str, optional): _description_. Defaults to "ID".

        Returns:
            _type_: _description_
        """
        return self._model.model_validate_json(
            self._client.get(
                resource=self.resource,
                primary_key=primary_key,
                primary_key_value=primary_key_value,
            ).json()["d"]["results"][0]
        )

    def all(
        self, filters: Dict[str, Union[str, int, float]] = [], select: List[str] = []
    ):
        """_summary_

        Args:
            filters (List[str], optional): _description_. Defaults to [].

        Raises:
            NoFilterSetException: _description_

        Returns:
            _type_: _description_
        """
        if len(self._mandatory_filter_options) > 0 and len(filters) == 0:
            raise NoFilterSetException(
                f"This model requires a mandatory filter. Choices are '{', '.join(self._mandatory_filter_options)}"
            )
        elif (
            len(self._mandatory_filter_options) > 0
            and set(self._mandatory_filter_options).intersection(filters.keys()) == {}
        ):
            raise NoFilterSetException(
                f"No valid mandatory filter set. Choices are '{', '.join(self._mandatory_filter_options)}"
            )

        resp = self._client.get(
            resource=self.resource, filters=filters, select=select
        ).json()

        adapter = TypeAdapter(List[self._model])
        results = adapter.validate_json(resp["d"]["results"])

        while (next_url := resp["d"].get("__next")) is not None:
            skip_token = self._client._get_skip_token(next_url)
            resp = self._client.get(
                resource=self.resource,
                filters=filters,
                select=select,
                skip_token=skip_token,
            ).json()
            temp_results = adapter.validate_json(resp["d"]["results"])
            results.extend(temp_results)

        return results
