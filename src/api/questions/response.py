# from @testla/screenplay import Actor, Question
from typing import Dict, Literal
from src.api.abilities.use_api import UseAPI
from src.api.types import Response as ResponseType

class Response(Question):
    """Question Class. Verify certain aspects of an API Response."""

    def __init__(self, check_mode: Literal['has', 'has_not'], mode:  Literal['status', 'body', 'header', 'duration'], response: ResponseType, payload: object):
        super().__init__()
        self.check_mode = check_mode
        self.mode = mode
        self.response = response
        self.payload = payload

    def answered_by(self, actor: Actor) -> bool:
        match self.mode:
            case 'status':
                return UseAPI.As(actor).check_status(response=self.response, status=self.payload, mode='equal' if self.check_mode == 'has' else 'unequal')
            case 'body':
                return UseAPI.As(actor).check_body(response=self.response, body=self.payload, mode='equal' if self.check_mode == 'has' else 'unequal')
            case 'header':
                return UseAPI.As(actor).check_headers(response=self.response, headers=self.payload, mode='included' if self.check_mode == 'has' else 'excluded')
            case 'duration':
                return UseAPI.As(actor).check_duration(response=self.response, duration=self.payload, mode='less_or_equal' if self.check_mode == 'has' else 'greater')
            # default case
            case _:
                raise RuntimeError('Unknown mode for Response.answeredBy')

    @staticmethod
    def has_status_code(response: ResponseType, status_code: int) -> 'Response':
        """Verify if the given status is equal to the given response's status.
        
        :param response: the response to check.
        :param status_code: the expected status code.
        """
        return Response(check_mode='has', mode='status', response=response, payload=status_code)

    @staticmethod
    def has_not_status_code(response: ResponseType, status_code: int) -> 'Response':
        """Verify if the given status is not equal to the given response's status.
        
        :param response: the response to check.
        :param status_code: the not expected status code.
        """
        return Response(check_mode='has_not', mode='status', response=response, payload=status_code)

    @staticmethod
    def has_body(response: ResponseType, body: Dict | str | None) -> 'Response':
        """Verify if the given body is equal to the given response's body.
        
        :param response: the response to check.
        :param body: the expected body.
        """
        return Response(check_mode='has', mode='body', response=response, payload=body)
    
    @staticmethod
    def has_not_body(response: ResponseType, body: Dict | str | None) -> 'Response':
        """Verify if the given body is not equal to the given response's body.
        
        :param response: the response to check.
        :param body: the not expected body.
        """
        return Response(check_mode='has_not', mode='body', response=response, payload=body)

    @staticmethod
    def has_headers(response: ResponseType, headers: Dict[str, str]) -> 'Response':
        """Verify if the given headers are included in the given response.
        
        :param response: the response to check.
        :param headers: the expected headers.
        """
        return Response(check_mode='has', mode='header', response=response, payload=headers)

    @staticmethod
    def has_not_headers(response: ResponseType, headers: Dict[str, str]) -> 'Response':
        """Verify if the given headers are not included in the given response.
        
        :param response: the response to check.
        :param headers: the not expected headers.
        """
        return Response(check_mode='has_not', mode='header', response=response, payload=headers)

    @staticmethod
    def has_been_received_within(response: ResponseType, duration: float) -> 'Response':
        """Verify if the reponse (including receiving body) was received within a given duration.
        
        :param response: the response to check.
        :param duration: expected duration (in seconds) not to be exceeded
        """
        return Response(check_mode='has', mode='header', response=response, payload=duration)

    @staticmethod
    def has_not_been_received_within(response: ResponseType, duration: float) -> 'Response':
        """Verify if the reponse (including receiving body) was not received within a given duration.
        
        :param response: the response to check.
        :param duration: expected duration (in seconds) to be exceeded
        """
        return Response(check_mode='has_not', mode='header', response=response, payload=duration)
