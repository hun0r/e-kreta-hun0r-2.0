from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Any, Literal, Optional, Type, TypeVar, get_args, get_origin, overload

if TYPE_CHECKING:
    from pydantic import BaseModel

    from ..idp.auth_session_protocol import Auth_Session_Protocol

T = TypeVar("T")
class Router:
    BASE_URL = ""
    def __init__(self, session: Auth_Session_Protocol):
        self.session = session
    @overload
    def request(
        self,
        url: str,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:...
    @overload
    def request(
        self,
        url: str,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> T:...
    def request(
        self,
        url: str,
        method: Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"
        ],
        model: Optional[Type[T]] = None,
        params: Optional[dict[str, str]] = None,
        data: Optional[dict[str, str]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> T:
        full_url = self.BASE_URL + url
        return self.session.request(method, full_url, model = model, params=params, data=data, headers=headers)


def validate(
    data: dict,
    model: Optional[Type[T]] = None,
) -> T:
    if model is None:
        return None

    if issubclass(model, BaseModel):
        return model.model_validate(data)
    
    if model is dict:
        return data

    origin = get_origin(model)
    if origin is list:
        inner_model: BaseModel = get_args(model)[0]
        return [inner_model.model_validate(item) for item in data]

    raise ValueError(f"Unsupported model: {model}")


def filter_params(**kwargs) -> dict[str, Any]:
    return {
        k: (v.isoformat() if isinstance(v, datetime) else v)
        for k, v in kwargs.items()
        if v is not None
    }


def week_dates(date_in_first_week: datetime, weeks: int) -> tuple[datetime, datetime]:
    monday = date_in_first_week.date() - timedelta(days=date_in_first_week.weekday())
    sunday = monday + timedelta(days=6, weeks=weeks - 1)
    return monday, sunday
