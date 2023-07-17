from testla_screenplay import Actor
from typing import Dict
from .abstract_request import ARequest
from ..types import RequestMethod, Response, ResponseBodyFormat
from ..abilities.use_api import UseAPI

class Post(ARequest):
    """Action Class. Send a HTTP POST Request."""
    response_body_format = ResponseBodyFormat.JSON

    data: object

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def perform_as(self, actor: Actor) -> Response:
        """Send a HTTP POST request to the specified url."""
        return UseAPI.As(actor).send_request(method=RequestMethod.POST, url=self.url, headers=self.headers, data=self.data, response_format=self.response_body_format)

    @staticmethod
    def To(url: str) -> 'Post':
        """Send a HTTP POST request to the specified url.
        
        :param url: the URL of the target.
        """
        return Post(url)

    def with_data(self, data: object) -> 'Post':
        """Add data to the HTTP POST request to send.
        
        :param data: the data.
        """
        self.data = data
        return self

    def with_headers(self, headers: Dict[str, str]) -> 'Post':
        """Add headers to the HTTP POST request to send.
        
        :param headers: the headers.
        """
        self.headers = headers
        return self

    def with_response_body_format(self, response_body_format: ResponseBodyFormat) -> 'Post':
        """Set the format the response body should be returned as.
        
        :param response_body_format: the format of the response body.
        """
        self.response_body_format = response_body_format
        return self
