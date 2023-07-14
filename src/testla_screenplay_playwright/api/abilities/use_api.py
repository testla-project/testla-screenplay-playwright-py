from time import time
from typing import Any, Dict, Literal
from playwright.sync_api import APIRequestContext, APIResponse
from sqlalchemy import true
from ..types import RequestMethod, Response, ResponseBodyFormat
from testla_screenplay import Ability, Actor


class UseAPI(Ability):
    """This class represents the actor's ability to use an API."""

    def __init__(self, request_context: APIRequestContext):
        self.request_context = request_context

    @staticmethod
    def using(request_context: APIRequestContext) -> 'UseAPI':
        """Initialize this Ability by passing an already existing Playwright APIRequestContext object.
        
        :param request_context: the Playwright APIRequestContext that will be used.
        """
        return UseAPI(request_context)

    @staticmethod
    def As(actor: Actor) -> 'UseAPI':
        """Use this Ability as an Actor."""
        return actor.with_ability_to(UseAPI)

    def get_request_context(self) -> APIRequestContext:
        """Get the request context object."""
        return self.request_context

    def send_request(self, method: RequestMethod, url: str, headers: Dict[str, str] | None = None, data: object | None = None, response_format: ResponseBodyFormat | None = None) -> Response:
        # track time before sending request
        start_time = time()

        res: APIResponse
        match method:
            case RequestMethod.GET:
                res = self.request_context.get(url=url, headers=headers)
            case RequestMethod.POST:
                res = self.request_context.post(url=url, headers=headers, data=data)
            case RequestMethod.PUT:
                res = self.request_context.put(url=url, headers=headers, data=data)
            case RequestMethod.PATCH:
                res = self.request_context.patch(url=url, headers=headers, data=data)
            case RequestMethod.HEAD:
                res = self.request_context.head(url=url, headers=headers)
            case RequestMethod.DELETE:
                res = self.request_context.delete(url=url, headers=headers, data=data)
            # default case
            case _:
                raise RuntimeError("Error: HTTP method not supported.")

        res_body: Any
        match response_format:
            case ResponseBodyFormat.JSON:
                res_body = res.json()
            case ResponseBodyFormat.TEXT:
                res_body = res.text()
            # case ResponseBodyFormat.BUFFER:
            #     res_body = res.body()
            case ResponseBodyFormat.NONE:
                res_body = None
            # default case
            case _:
                raise RuntimeError("Error: ResponseBodyFormat not supported.")

        # track time after receiving response
        end_time = time()

        return Response(res_body, res.status, res.headers, end_time - start_time)

    def check_status(self, response: Response, status: int, mode: Literal['equal', 'unequal']) -> bool:
        """Verify if the given status is equal or unequal to the given response's status.

        :param response: the response to check.
        :param status the status to check.
        :param mode: the result to check for.
        :returns: true if the status is equal/unequal as expected.
        """
        assert (response.status == status) == (mode == 'equal')
        return true

    def check_body(self, response: Response, body: Dict | str | None, mode: Literal['equal', 'unequal']) -> bool:
        """Verify if the given body is equal or unequal to the given response's body.
        
        :param response: the response to check.
        :param body: the body to check.
        :param mode: the result to check for.
        :returns: true if the body equal/unequal as expected.
        """
        if type(response.body) == str and type(body) == str:
            # response body is plain text -> can check for string equality
            assert (response.body == body) == (mode == 'equal')
            return true
        elif type(response.body) == Dict and type(body) == Dict:
            # response body is in json -> can check with Dict equality
            assert (response.body == body) == (mode == 'equal')
            return true
        else:
            # response.body and body do not have same type -> bodies are unequal
            assert (mode == 'unequal')
            return true

    def check_headers(self, response: Response, headers: Dict[str, str], mode: Literal['included', 'excluded']) -> bool:
        """Verify if the given headers are included/excluded in the given response.

        :param response: the response to check.
        :param headers: the headers to check.
        :param mode: the result to check for.
        :returns: true if the headers are is included/excluded as expected.
        """
        # dict1.items() <= dict2.items() checks if dict1 is a subset of dict2.
        assert (headers.items() <= response.headers.items()) == (mode == 'included')
        return true

    def check_duration(self, response: Response, duration: float, mode: Literal['less_or_equal', 'greater']) -> bool:
        """Verify if the response (including receiving body) was received within a given duration or not.

        :param response: the response to check.
        :param duration: expected duration (in milliseconds) not to be exceeded.
        :param mode: the result to check for.
        :returns: true if response was received within given duration, false otherwise.
        """
        assert (response.duration <= duration) == (mode == 'less_or_equal')
        return true
