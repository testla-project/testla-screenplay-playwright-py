from testla_screenplay import Actor
from typing import Dict
from .abstract_request import ARequest
from ..types import RequestMethod, Response, ResponseBodyFormat
from ..abilities.use_api import UseAPI

class Head(ARequest):
    """Action Class. Send a HTTP HEAD Request."""

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def perform_as(self, actor: Actor) -> Response:
        """Send a HTTP HEAD request to the specified url."""
        return UseAPI.As(actor).send_request(method=RequestMethod.HEAD, url=self.url, headers=self.headers, response_format=ResponseBodyFormat.NONE)

    @staticmethod
    def From(url: str) -> 'Head':
        """Send a HTTP HEAD request to the specified url.
        
        :param url: the URL of the target.
        """
        return Head(url)

    def with_headers(self, headers: Dict[str, str]) -> 'Head':
        """Add headers to the HTTP HEAD request to send.
        
        :param headers: the headers.
        """
        self.headers = headers
        return self
