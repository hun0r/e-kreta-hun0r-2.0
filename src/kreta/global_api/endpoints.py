from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Optional

from ..utils.utils import filter_params, Router, week_dates
#from .models import ()

if TYPE_CHECKING:
    from datetime import datetime

    from ..idp.auth_session_protocol import Auth_Session_Protocol
        

class Global(Router):
    BASE_URL: str = ""
