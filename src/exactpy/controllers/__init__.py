from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Type, Union

from loguru import logger
from pydantic import BaseModel, TypeAdapter

from exactpy.exceptions import NoFilterSetException
from exactpy.models import ExactOnlineBaseModel

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

    def show(
        self, primary_key_value: Union[str, int], primary_key: str = "ID"
    ) -> Type[ExactOnlineBaseModel]:
        """Retrieve a single instance of a model by primary key.

        Args:
            primary_key_value (Union[str, int]): value of primary key field.
            primary_key (str, optional): name of primary key field. Defaults to "ID".

        Returns:
            Type[ExactOnlineBaseModel]: In instance of a subclass of ExactOnlineBaseModel.
        """
        return self._model.model_validate(
            json_data=self._client.get(
                resource=self._resource,
                primary_key=primary_key,
                primary_key_value=primary_key_value,
            ).json()["d"]["results"][0],
            extra="ignore",
        )

    def all(
        self,
        filters: Dict[str, Union[str, int, float]] = {},
        select: List[str] = [],
        max_pages: int = -1,
    ) -> List[Type[ExactOnlineBaseModel]]:
        """_summary_

        Args:
            filters (Dict[str, Union[str, int, float]], optional):  Dict of filter key, value pairs. Defaults to {}
            select (List[str], optional): Attributes to select (in Exact Online naming, so Pascal case). Defaults to [].
            max_pages (int, optional): Max number of pages to retrieve. Defaults to -1 (no limit).

        Raises:
            NoFilterSetException:  Raised when a filter is mandatory but no filter was set.

        Returns:
            List[Type[ExactOnlineBaseModel]]: List of instances of a subclass of ExactOnlineBaseModel.
        """
        if max_pages == 0:
            return []

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
            resource=self._resource, filters=filters, select=select
        ).json()

        adapter = TypeAdapter(List[self._model])
        from pprint import pprint

        print("*" * 100)
        pprint(resp["d"]["results"][0])
        results = adapter.validate_python(resp["d"]["results"])
        p = 0
        if self._client.verbose:
            logger.info(f"Fetched page {p + 1}")
        while (next_url := resp["d"].get("__next")) is not None:
            p += 1
            if max_pages != -1 and p + 1 > max_pages:
                break
            if self._client.verbose:
                logger.info(f"Fetching page {p + 1}")
            skip_token = self._client._get_skip_token(next_url)
            resp = self._client.get(
                resource=self._resource,
                filters=filters,
                select=select,
                skip_token=skip_token,
            ).json()
            temp_results = adapter.validate_python(resp["d"]["results"], extra="ignore")
            results.extend(temp_results)

        if self._client.verbose:
            logger.info(f"Fetched a total of {len(results)} records.")

        return results
