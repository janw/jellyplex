from __future__ import annotations

from typing import TYPE_CHECKING, Any

from requests import Session
from requests.adapters import HTTPAdapter

if TYPE_CHECKING:
    from requests.models import PreparedRequest, Response

from . import __name__, __version__

USER_AGENT = f"{__name__}/{__version__} (https://github.com/janw/{__name__})"
REQUESTS_TIMEOUT = (5, 30)


class TimeoutHTTPAdapter(HTTPAdapter):
    def send(
        self,
        request: PreparedRequest,
        timeout: tuple[float, float] | float | None = None,
        **kwargs: Any,
    ) -> Response:
        return super().send(request, timeout=timeout or REQUESTS_TIMEOUT, **kwargs)


_adapter = TimeoutHTTPAdapter()

session = Session()
session.mount("http://", _adapter)
session.mount("https://", _adapter)
session.headers.update(
    {
        "user-agent": USER_AGENT,
    }
)
