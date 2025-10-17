import json
from pathlib import Path
from time import time
from typing import Callable, Tuple, Union
from urllib.parse import parse_qs, urlparse

from loguru import logger
from requests_oauthlib import OAuth2Session

from exactpy.exceptions import TokenRefreshError


class Auth:
    """Initializes the auth class that handles the Exact Online
    oauth authentication parts.

    Args:
        client_id (str): The Exact Online oauth client ID
        client_secret (str): The Exact Online oauth client secret
        redirect_url (str): The redirect url, needs to match exactly what
            was entered in the app registration in the Exact Online portal.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_url: str,
        auth_url: str,
        cache_callable: Callable | None = None,
        cache_callable_kwargs: dict = {},
        verbose: bool = False,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.auth_url = auth_url
        self.verbose = verbose
        self.token_info = {}
        self.caching_enabled = False
        if cache_callable is not None:
            self.cache_callable = cache_callable
            self.cache_callable_kwargs = cache_callable_kwargs
            self.caching_enabled = True

    @staticmethod
    def cache_creds(contents: dict, cache_path: Union[Path, str]):  # pragma: no cover
        """This is the default caching method for credentials.
        It serializes and saves a the received credential dict
        in string form to the given path.

        Args:
            contents (dict): The credentials dict.
            path (Union[Path, str]): The path to cache to.
        """
        path = Path(cache_path)
        with open(path, "w+") as fp:
            json.dump(contents, fp)

    @staticmethod
    def parse_response_url(response_url: str) -> Tuple[str, str]:
        """This method parses the response url received from
        Exact Online's oauth implementation and extracts both
        the code and the state query params, that can then
        be used to actually request and oauth token and
        refresh token.

        Args:
            response_url (str): The response that Exact Online
            redirected us to.

        Returns:
            Tuple[str, str]: A tuple containing code and state respectively.
        """
        parsed_url = urlparse(response_url)
        code = parse_qs(parsed_url.query)["code"][0]
        state = parse_qs(parsed_url.query)["state"][0]
        return code, state

    def get_authorization_url(self) -> str:  # pragma: no cover
        """Get Exact Online oauth authorization url that can be used to authorize
        the client to obtain a token.

        Returns:
            str: the authorization url.
        """
        oauth_session = OAuth2Session(self.client_id, redirect_uri=self.redirect_url)
        authorization_url, _ = oauth_session.authorization_url(self.auth_url)
        return authorization_url

    def acquire_token(self, redirect_response_url: str) -> None:  # pragma: no cover
        """Acquire token in a fresh state.

        Args:
            redirect_response_url (str): The response url after calling the authorization endpoint.
        """
        _, state = Auth.parse_response_url(redirect_response_url)
        oauth_session = OAuth2Session(
            client_id=self.client_id, state=state, redirect_uri=self.redirect_uri
        )
        oauth_session.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            authorization_response=redirect_response_url,
        )

        self.token_info = {
            "access_token": oauth_session._client.access_token,
            "refresh_token": oauth_session._client.refresh_token,
            "expires_on": int(time() + oauth_session._client.expires_in),
        }

        if self.caching_enabled:
            if self.verbose:
                logger.info("Caching enabled. Caching credentials.")
            self.cache_callable(contents=self.token_info, **self.cache_callable_kwargs)

    def refresh_token(self):  # pragma: no cover
        """Attempt to refresh oauth access token using the refresh token."""

        refresh_token = {
            "access_token": self.token_info["access_token"],
            "refresh_token": self.token_info["refresh_token"],
            "token_type": "Bearer",
            "expires_in": "-30",
        }

        oauth_session = OAuth2Session(client_id=self.client_id, token=refresh_token)

        try:
            oauth_session.refresh_token(
                url=self.token_url,
                client_id=self.client_id,
                client_secret=self.client_secret,
            )

            self.token_info = {
                "access_token": oauth_session._client.access_token,
                "refresh_token": oauth_session._client.refresh_token,
                "expires_on": int(time() + oauth_session._client.expires_in),
            }

            if self.caching_enabled:
                if self.verbose:
                    logger.info("Caching enabled. Caching credentials.")
                self.cache_callable(
                    contents=self.token_info, **self.cache_callable_kwargs
                )

        except Exception:
            raise TokenRefreshError(
                "Token could not be refreshed. Exception message: {e}"
            )

    def is_token_refresh_needed(self, now: float = time()) -> bool:
        """Determines whether a token refresh is needed.

        Args:
            now (float, optional): how soon is now? Defaults to time().
                This is needed to be able to have

        Returns:
            bool: whether a token refresh is needed
        """
        return self.token_info.get("expires_on", 0) - now < 30
