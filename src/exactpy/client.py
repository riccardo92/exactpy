from enum import StrEnum
from pathlib import Path
from typing import Callable, Dict, List, Type
from urllib.parse import parse_qs, urlparse

import httpx
from loguru import logger

from exactpy.auth import Auth
from exactpy.controllers.account import AccountController

BASE_HEADER = {"Content-Type": "application/json"}


class FilterOperatorEnum(StrEnum):
    AND = "and"
    OR = "or"


class Client:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        cache_callable: Callable | None = Auth.cache_creds,
        cache_callable_kwargs: dict = {"cache_path": Path("./creds.json")},
        base_url: str = "https://start.exactonline.nl/api",
        auth_url: str | None = None,
        token_url: str | None = None,
        endpoints_url: str | None = None,
        verbose: bool = True,
    ):
        """An Exact Online Python client.

        Args:
            client_id (str): The Exact Online app registration client ID.
            client_secret (str): The Exact Online app registration client secret.
            cache_callable (Callable, optional): The Callable to use to store the credentials. It must have argument token_dict of type dict.
                If unset (None), no caching will be done. Defaults to exactpy.Auth.cache_creds.
            cache_callable_kwargs (dict): Extra args to pass to cache_callable.
                Defaults to { "cache_path": Path("./creds.json") } but can be customized when e.g. no path is needed.
            base_url (str, optional): The API base url. Defaults to "https://start.exactonline.nl/api".
            auth_url (str | None, optional): The auth base url. Defaults to None. If unset (None), it will be derived from base_url.
            token_url (str | None, optional): _description_. Defaults to None. If unset (None), it will be derived from base_url.
            endpoints_url (str | None, optional): the v1 endpoints url. Defaults to None. If unset (None), it will be derived from base_url
            verbose (bool, optional): _description_. Defaults to True.
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self.verbose = verbose

        self.base_url = base_url.rstrip("/")
        if not self.base_url.endswith("api"):
            raise ValueError("base_url does not end in api, cannot proceed.")

        if endpoints_url is None:
            self.endpoints_url = f"{self.base_url}/v1"
            if verbose:
                logger.info(
                    f"endpoints_url was not set. Derived from base_url: {self.endpoints_url}"
                )
        self.endpoints_url = self.endpoints_url.rstrip("/")

        if token_url is None:
            token_url = f"{self.base_url}/oauth2/token"
            if verbose:
                logger.info(
                    f"access_token_url was not set. Derived from base_url: {token_url}"
                )
        token_url = self.access_token_url.rstrip("/")

        if auth_url is None:
            auth_url = f"{self.base_url}/oauth2/auth"
            if verbose:
                logger.info(
                    f"auth_url was not set. Derived from base_url: {self.auth_url}"
                )
        auth_url = self.auth_url.rstrip("/")

        self.auth_client = Auth(
            client_id=client_id,
            client_secret=client_secret,
            auth_url=auth_url,
            token_url=token_url,
            cache_callable=cache_callable,
            cache_callable_kwargs=cache_callable_kwargs,
            verbose=self.verbose,
        )

        # Set up endpoints
        self.accounts = AccountController(self)

    @staticmethod
    def parse_filters(
        filters: Dict[str, str], filter_operator: Type[FilterOperatorEnum]
    ) -> str:
        """Build url filter string from filter dict.

        Args:
            filters (Dict[str, str]): The filter key value pairs.

        Returns:
            str: Filters in Exact Online string form.
        """
        filters = []
        op = str(filter_operator)
        for key, val in filters.items():
            qu = "' "[val.lower() in ("true", "false")]
            pref = ("", op)[len(filters) > 0]
            filters.append(f" {pref} {key} eq {qu}{val}{qu}")

        return ",".join(filters)

    @staticmethod
    def _get_skip_token(next_url: str) -> str:
        """Get skip token from next url.

        Args:
            next_url(str): API response next url containing skip token.

        Returns:
            str: the complete skip token query param key value pair in string form.
        """
        parsed_url = urlparse(next_url)
        token = parse_qs(parsed_url.query)["$skiptoken"][0]
        return token

    def get(
        self,
        resource: str,
        filters: Dict[str, str] = {},
        filter_operator: Type[FilterOperatorEnum] = FilterOperatorEnum.AND,
        select: List[str] = [],
    ):
        """Calls a get endpoint.

        Args:
            resource (str): The Exact Online API url resource to use.
            filters (Dict[str, str]): A dictionary of
                filter name and filter value key pairs to send to the endpoint. Defaults to {}.
            filter_operator (Type[FilterOperatorEnum]): Operator to use to join the filters (and/or).
            select (List[str]): Attributes to select. Defaults to [].

        Returns:
            httpx.Response: the API call httpx response object.
        """
        headers = self.auth_client._check_token_and_get_headers()
        headers.update(BASE_HEADER)

        parsed_filters = Client.parse_filters(
            filters=filters, filter_operator=filter_operator
        )
        parsed_select = ",".join(select)

        url = f"{self.endpoints_url}/{resource}"
        url += ("", f"?$filter={parsed_filters}")[len(filters) > 0]

        join_str = ("?", "&")[len(filters) > 0]
        url += ("", f"{join_str}$select={parsed_select}")[len(select) > 0]

        req = httpx.get(url=url, headers=headers)
        req.raise_for_status()

        return req

    def show(
        self,
        resource: str,
        primary_key_value: str,
        primary_key: str = "ID",
        select: List[str] = [],
    ) -> httpx.Response:
        """Calls a get endpoint

        Args:
            filters (Dict[str, str]): A dictionary of
                filter name and filter value key pairs to send to the endpoint.
            primary_key_value (str): Value of the primary key field
            primary_key (str): Name of the primary field. Defaults to "ID".
            select (List[str]): Attributes to select. Defaults to [].

        Returns:
            httpx.Response: the API call httpx response object.
        """
        headers = self.auth_client._check_token_and_get_headers()
        headers.update(BASE_HEADER)
        parsed_select = ",".join(select)

        url = f"{self.endpoints_url}/{resource}"
        url += f"?$filter={primary_key} eq guid '{primary_key_value}'"
        url += ("", f"&$select={parsed_select}")[len(select) > 0]

        req = httpx.get(url=url, headers=headers)
        req.raise_for_status()

        return req
