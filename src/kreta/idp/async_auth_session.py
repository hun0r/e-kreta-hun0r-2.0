from typing import Awaitable, Literal, Optional, Self, Type, TypeVar

import aiohttp

from kreta.idp.auth_session_protocol import Async_Auth_Session_Protocol
from ..utils.utils import validate

from .login import login
from .auth_token import Auth_Token

T = TypeVar("T")
class Async_Auth_Session(aiohttp.ClientSession, Async_Auth_Session_Protocol):
    def __init__(self, token: Auth_Token, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.token = token
        self.headers.update(
            {
                "Authorization": str(self.token),
                "User-Agent": "hu.ekreta.tanulo/1.0.5/Android/0/0",
                "apiKey": "21ff6c25-d1da-4a68-a811-c881a6057463",
            },
        )

    async def __aexit__(
        self,
        *args,
        **kwargs
    ) -> None:
        await self.close()

    async def close(self) -> None:
        self.invalidate()
        super().close()

    async def invalidate(self) -> None:
        if self.token is not None:
            await self.token.revoke_refresh_token(self)
            self.token = None
        if "Authorization" in self.headers:
            self.headers.pop("Authorization")

    @classmethod
    async def login(cls, username: str, password: str, institute_code: str) -> Self:
        r = login(username, password, institute_code)
        token = Auth_Token(**r)
        return cls(token)

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
        # fill the institute code in the url
        if "{institute_code}" in url:
            url = url.format(institute_code=self.token.body.kreta_institute_code)
        # refresh the token if needed
        if self.token.body.is_expired():
            self.token.refresh()
            self.headers.update({"Authorization": str(self.token)})
        # make request
        async with super().request(method, url, params=params, data=data, headers=headers) as response:
            # raise errors with the messages sent by kreta
            response.raise_for_status()
            obj = validate(await response.json())

        return obj

    async def refresh(self) -> None:
        await self.token.refresh(self)
        self.headers.update({"Authorization": str(self.token)})
