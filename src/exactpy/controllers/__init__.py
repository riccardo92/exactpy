from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING, Dict, List, Type, Union

import pandas as pd
from loguru import logger
from pydantic import BaseModel, TypeAdapter

from exactpy.exceptions import NoFilterSetException
from exactpy.models import ExactOnlineBaseModel

if TYPE_CHECKING:
    from exactpy.client import Client


class OutputTypeEnum(StrEnum):
    PANDAS = "pandas"
    LIST = "list"


class BaseController:
    _resource: str
    _mandatory_filter_options: List[str]
    _model: Type[BaseModel]

    def __init__(
        self,
        client: Client,
    ):
        self._client = client
        self._list_adapter = TypeAdapter(List[self._model])

    def _check_filters(self, filters: Dict[str, Union[str, int, float]] = {}):
        """Checks whether (the right) filters have been set in case
        they are mandatory.

        Args:
            filters (Dict[str, Union[str, int, float]], optional):  Dict of filter key, value pairs. Defaults to {}

        Raises:
            NoFilterSetException: _description_
        """
        filter_options = ", ".join(self._mandatory_filter_options)
        if len(self._mandatory_filter_options) > 0 and len(filters) == 0:
            raise NoFilterSetException(
                f"This model requires a mandatory filter. Choices are '{filter_options}'"
            )
        elif (
            len(self._mandatory_filter_options) > 0
            and set(self._mandatory_filter_options).intersection(filters.keys()) == {}
        ):
            raise NoFilterSetException(
                f"No valid mandatory filter set. Choices are '{filter_options}'"
            )

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

        # Retrieve single instance and convert to pydantic
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
        type: Type[OutputTypeEnum] = OutputTypeEnum.LIST,
    ) -> Union[List[Type[ExactOnlineBaseModel]], pd.DataFrame]:
        """_summary_

        Args:
            filters (Dict[str, Union[str, int, float]], optional):  Dict of filter key, value pairs. Defaults to {}
            select (List[str], optional): Attributes to select (in Exact Online naming, so Pascal case). Defaults to [].
            max_pages (int, optional): Max number of pages to retrieve. Defaults to -1 (no limit).
            type (Type[OutputTypeEnum]): The output type, list or pandas. Defaults to OutputTypeEnum.LIST.

        Returns:
            Union[List[Type[ExactOnlineBaseModel]], pd.DataFrame]: List of instances of a subclass of ExactOnlineBaseModel or a Pandas dataframe.
        """
        if max_pages == 0:
            return []

        # Check mandatory filters
        self._check_filters(filters=filters)

        # Initial get request to get first page
        resp = self._client.get(
            resource=self._resource, filters=filters, select=select
        ).json()

        # Convert to Pydantic
        results = self._list_adapter.validate_python(resp["d"]["results"])

        page_count = 0

        if self._client.verbose:
            logger.info(f"Fetched page {page_count + 1}")
        while (next_url := resp["d"].get("__next")) is not None:
            page_count += 1
            if max_pages != -1 and page_count + 1 > max_pages:
                break

            if self._client.verbose:
                logger.info(f"Fetching page {page_count + 1}")

            # Extract the skip token, in order to obtain the next page
            skip_token = self._client._get_skip_token(next_url)

            # Get page
            resp = self._client.get(
                resource=self._resource,
                filters=filters,
                select=select,
                skip_token=skip_token,
            ).json()

            # Convert to Pydantic
            temp_results = self._list_adapter.validate_python(
                resp["d"]["results"], extra="ignore"
            )
            results.extend(temp_results)

        if self._client.verbose:
            logger.info(f"Fetched a total of {len(results)} records.")

        # Convert to Pandas if needed and return
        if type == OutputTypeEnum.PANDAS:
            return pd.DataFrame([r.model_dump() for r in results])

        # Or return a list
        return results
