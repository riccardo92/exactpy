from enum import StrEnum
from pathlib import Path
from typing import Callable, Dict, List, Type
from urllib.parse import parse_qs, urlparse

import httpx
from loguru import logger

from exactpy.auth import Auth
from exactpy.controllers.account import AccountController
from exactpy.controllers.me import MeController
from exactpy.exceptions import NoDivisionSetException

BASE_HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


class FilterOperatorEnum(StrEnum):
    AND = "and"
    OR = "or"


class Client:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_url: str,
        enabling_caching: bool = True,
        write_cache_callable: Callable | None = Auth.write_cache,
        write_cache_callable_kwargs: dict = {"cache_path": Path("./creds.json")},
        read_cache_callable: Callable | None = Auth.read_cache,
        read_cache_callable_kwargs: dict = {"cache_path": Path("./creds.json")},
        base_url: str = "https://start.exactonline.nl/api",
        auth_url: str | None = None,
        token_url: str | None = None,
        endpoints_url: str | None = None,
        current_division: int | None = None,
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
            redirect_url (str): The redirect url, needs to match exactly what
                was entered in the app registration in the Exact Online portal.
            base_url (str, optional): The API base url. Defaults to "https://start.exactonline.nl/api".
            auth_url (str | None, optional): The auth base url. Defaults to None. If unset (None), it will be derived from base_url.
            token_url (str | None, optional): _description_. Defaults to None. If unset (None), it will be derived from base_url.
            endpoints_url (str | None, optional): the v1 endpoints url. Defaults to None. If unset (None), it will be derived from base_url
            current_division (int, optional): The current division to use. Defaults to None.
            verbose (bool, optional): _description_. Defaults to True.
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self.verbose = verbose

        self.current_division = current_division

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
        token_url = token_url.rstrip("/")

        if auth_url is None:
            auth_url = f"{self.base_url}/oauth2/auth"
            if verbose:
                logger.info(f"auth_url was not set. Derived from base_url: {auth_url}")
        auth_url = auth_url.rstrip("/")

        self.auth_client = Auth(
            client_id=client_id,
            client_secret=client_secret,
            auth_url=auth_url,
            token_url=token_url,
            redirect_url=redirect_url,
            write_cache_callable=write_cache_callable,
            write_cache_callable_kwargs=write_cache_callable_kwargs,
            read_cache_callable=read_cache_callable,
            read_cache_callable_kwargs=read_cache_callable_kwargs,
            verbose=self.verbose,
        )

        # Set up endpoints
        self.accounts = AccountController(self)
        self.me = MeController(self)

    @staticmethod
    def _parse_filters(
        filters: Dict[str, str], filter_operator: Type[FilterOperatorEnum]
    ) -> str:
        """Build url filter string from filter dict.

        Args:
            filters (Dict[str, str]): The filter key value pairs.

        Returns:
            str: Filters in Exact Online string form.
        """
        parsed_filters = []
        op = str(filter_operator)
        for key, val in filters.items():
            qu = "' "[val.lower() in ("true", "false")]
            pref = ("", op)[len(filters) > 0]
            parsed_filters.append(f" {pref} {key} eq {qu}{val}{qu}")

        return ",".join(parsed_filters)

    @staticmethod
    def _get_skip_token(next_url: str) -> str:
        """Get skip token from next url.

        Args:
            next_url(str): API response next url containing skip token.

        Returns:
            str: the complete skip token query param key value pair in string form.
        """
        parsed_url = urlparse(next_url)
        return parse_qs(parsed_url.query)["$skiptoken"][0]

    def _check_division(self):
        if self.current_division is None:
            raise NoDivisionSetException(
                "You must set a division. You can pass this on init (current_division arg) or set it using client.division = client.get_current_division()."
            )

    def get(
        self,
        resource: str,
        filters: Dict[str, str] = {},
        filter_operator: Type[FilterOperatorEnum] = FilterOperatorEnum.AND,
        select: List[str] = [],
        include_division: bool = True,
        skip_token: str | None = None,
    ):
        """Calls a get endpoint.

        Args:
            resource (str): The Exact Online API url resource to use.
            filters (Dict[str, str]): A dictionary of
                filter name and filter value key pairs to send to the endpoint. Defaults to {}.
            filter_operator (Type[FilterOperatorEnum]): Operator to use to join the filters (and/or).
            select (List[str]): Attributes to select. Defaults to [].
            include_division (bool): Whether to include the current division in the url. Defaults to True.
            skip_token: (str, Optional): A skiptoken query arg, used for paging in the Exact Online rest api. Defaults to None.
        Returns:
            httpx.Response: the API call httpx response object.
        """
        if include_division:
            self._check_division()

        headers = self.auth_client._check_token_and_get_headers()
        headers.update(BASE_HEADERS)

        parsed_filters = Client._parse_filters(
            filters=filters, filter_operator=filter_operator
        )
        parsed_select = ",".join(select)

        division_part = ("", f"/{self.current_division}")[include_division]
        url = f"{self.endpoints_url}{division_part}/{resource}"
        url += ("", f"?$filter={parsed_filters}")[len(filters) > 0]

        join_str = ("?", "&")[len(filters) > 0]
        url += ("", f"{join_str}$select={parsed_select}")[len(select) > 0]

        join_str = ("?", "&")[len(filters) > 0 or len(select) > 0]
        url += ("", f"{join_str}$skiptoken={skip_token}")[skip_token is not None]

        req = httpx.get(url=url, headers=headers)
        req.raise_for_status()

        return req

    def show(
        self,
        resource: str,
        primary_key_value: str,
        primary_key: str = "ID",
        select: List[str] = [],
        include_division: bool = True,
    ) -> httpx.Response:
        """Calls a get endpoint

        Args:
            filters (Dict[str, str]): A dictionary of
                filter name and filter value key pairs to send to the endpoint.
            primary_key_value (str): Value of the primary key field
            primary_key (str): Name of the primary field. Defaults to "ID".
            select (List[str]): Attributes to select. Defaults to [].
            include_division (bool): Whether to include the current division in the url. Defaults to True.
        Returns:
            httpx.Response: the API call httpx response object.
        """
        if include_division:
            self._check_division()

        headers = self.auth_client._check_token_and_get_headers()
        headers.update(BASE_HEADERS)
        parsed_select = ",".join(select)

        division_part = ("", f"/{self.current_division}")[include_division]
        url = f"{self.endpoints_url}{division_part}/{resource}"
        url += f"?$filter={primary_key} eq guid '{primary_key_value}'"
        url += ("", f"&$select={parsed_select}")[len(select) > 0]

        req = httpx.get(url=url, headers=headers)
        req.raise_for_status()

        return req

    def get_current_division(self):
        return self.me.show().current_division
