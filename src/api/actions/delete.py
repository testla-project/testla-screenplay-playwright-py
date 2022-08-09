# from @testla/screenplay import Actor
from typing import Dict
from src.api.actions.abstract_request import ARequest
from src.api.types import RequestMethod, Response, ResponseBodyFormat
from src.api.abilities.use_api import UseAPI


class Delete(ARequest):
    """Action Class. Send a HTTP DELETE Request."""
    
    response_body_format = ResponseBodyFormat.JSON

    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def perform_as(self, actor: Actor) -> Response:
        """Send a HTTP DELETE request to the specified url."""
        return UseAPI.As(actor).send_request(method=RequestMethod.DELETE, url=self.url, headers=self.headers, response_format=self.response_body_format)

    @staticmethod
    def From(url: str) -> 'Delete':
        """Send a HTTP DELETE request to the specified url.
        
        :param url: the URL of the target.
        """
        return Delete(url)

    def with_headers(self, headers: Dict[str, str]) -> 'Delete':
        """Add headers to the HTTP DELETE request to send.
        
        :param headers: the headers.
        """
        self.headers = headers
        return self

    def with_response_body_format(self, response_body_format: ResponseBodyFormat) -> 'Delete':
        """Set the format the response body should be returned as.
        
        :param responseBodyFormat: the format of the response body.
        """
        self.response_body_format = response_body_format
        return self
