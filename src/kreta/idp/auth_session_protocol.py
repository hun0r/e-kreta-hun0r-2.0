from typing import Awaitable, Literal, Optional, Self, Type, TypeVar, overload

import requests

from .login import login
from .auth_token import Auth_Token

T = TypeVar("T")
class Sync_Auth_Session_Protocol:
    def __init__(self, token: Auth_Token, *args, **kwargs) -> None:
        """Create an instance from a valid `Auth_token`."""

    def __enter__(self, *args, **kwargs) -> None:
        """
        Enter of the underlying network connections and other things required.

        Allows usage like:

        .. code-block:: python

            with Sync_Auth_Session_Protocol(token) as session:
                # do stuff
                pass
        """

    def __exit__(self, *args, **kwargs) -> None:
        """Cleanup of the underlying network connections and other things that need it."""

    def close(self) -> None:
        """Close the underlying network connections and invalidate the refresh token."""

    def invalidate(self) -> None:
        """Invalidate the refresh token."""

    @classmethod
    def login(cls, username: str, password: str, institute_code: str) -> Self:
        """Class method constructor implementing login protocol."""

    @overload
    def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:...
    @overload
    def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> T:...
    def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> T|None:
        """
        Send an HTTP request to the given ``url`` using the specified ``method``.

        This method wraps the underlying request logic and optionally parses
        the response into a provided model.

        Must replace `{institute_code}` with the `institute_code` of the user.

        :param url: The target URL for the request.
        :type url: :class:`str`

        :param method: The HTTP method to use.
        :type method: :class:`str`

        :param params: HTTP parameters.
        :param data: Form data.
        :param headers: Request headers.

        :param model: Optional response model used to parse the returned data. Either :class:`pydantic.BaseModel`, a :class:`list` of it, :class:`bytes` for raw response or :class:`dict` for a parsed json.
        :type model: Optional[:class:`type`]

        :returns: The parsed response if ``model`` is provided, otherwise None.
        :rtype: :class:`T`

        :raises ValueError: If the request method is invalid.
        :raises RuntimeError: If the request fails.
        """

    def refresh(self) -> None:
        """Refresh the refresh token and request token."""

class Async_Auth_Session_Protocol:
    def __init__(self, token: Auth_Token, *args, **kwargs) -> None:
        """Create an instance from a valid `Auth_token`."""

    async def __aenter__(self, *args, **kwargs) -> Awaitable[None]:
        """
        Enter of the underlying network connections and other things required.

        Allows usage like:

        .. code-block:: python

            with Sync_Auth_Session_Protocol(token) as session:
                # do stuff
                pass
        """

    async def __aexit__(self, *args, **kwargs) -> Awaitable[None]:
        """Cleanup of the underlying network connections and other things that need it."""

    async def close(self) -> Awaitable[None]:
        """Close the underlying network connections and invalidate the refresh token."""

    async def invalidate(self) -> Awaitable[None]:
        """Invalidate the refresh token."""

    @classmethod
    async def login(cls, username: str, password: str, institute_code: str) -> Awaitable[Self]:
        """Class method constructor implementing login protocol."""

    @overload
    async def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Awaitable[None]:...
    @overload
    async def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Awaitable[T]:...
    async def request(
        self,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        url: str,
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Awaitable[T|None]:
        """
        Send an HTTP request to the given ``url`` using the specified ``method``.

        This method wraps the underlying request logic and optionally parses
        the response into a provided model.

        :param url: The target URL for the request.
        :type url: :class:`str`

        :param method: The HTTP method to use.
        :type method: :class:`str`

        :param params: HTTP parameters.
        :param data: Form data.
        :param headers: Request headers.

        :param model: Optional response model used to parse the returned data. Either :class:`pydantic.BaseModel`, a :class:`list` of it, :class:`bytes` for raw response or :class:`dict` for a parsed json.
        :type model: Optional[:class:`type`]

        :returns: The parsed response if ``model`` is provided, otherwise None.
        :rtype: :class:`T`

        :raises ValueError: If the request method is invalid.
        :raises RuntimeError: If the request fails.
        """

    async def refresh(self) -> Awaitable[None]:
        """Refresh the refresh token and request token."""

Auth_Session_Protocol = Sync_Auth_Session_Protocol | Async_Auth_Session_Protocol
