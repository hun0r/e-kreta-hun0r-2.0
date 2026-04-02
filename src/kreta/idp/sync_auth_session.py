from typing import Awaitable, Literal, Optional, Self, Type, TypeVar

import requests

from kreta.idp.auth_session_protocol import Sync_Auth_Session_Protocol
from ..utils.utils import validate

from .login import login
from .auth_token import Auth_Token

T = TypeVar("T")
class Sync_Auth_Session(requests.Session, Sync_Auth_Session_Protocol):
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

    def __exit__(
        self,
        *args,
        **kwargs
    ) -> None:
        self.close()

    def close(self) -> None:
        self.invalidate()
        super().close()

    def invalidate(self) -> None:
        if self.token is not None:
            self.token.revoke_refresh_token(self)
            self.token = None
        if "Authorization" in self.headers:
            self.headers.pop("Authorization")

    @classmethod
    def login(cls, username: str, password: str, institute_code: str) -> Self:
        r = login(username, password, institute_code)
        token = Auth_Token(**r)
        return cls(token)

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
    ) -> Awaitable[T|None]:
        # fill the institute code in the url
        if "{institute_code}" in url:
            url = url.format(institute_code=self.token.body.kreta_institute_code)
        # refresh the token if needed
        if self.token.body.is_expired():
            self.token.refresh()
            self.headers.update({"Authorization": str(self.token)})
        # make request
        with super().request(method, url, params=params, data=data, headers=headers) as response:
            # raise errors with the messages sent by kreta
            response.raise_for_status()
            obj = validate(response.json())

        return obj

    def refresh(self) -> None:
        self.token.refresh(self)
        self.headers.update({"Authorization": str(self.token)})
