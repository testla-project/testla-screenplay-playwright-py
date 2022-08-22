from dataclasses import dataclass
from enum import Enum
from typing import Dict


class RequestMethod(Enum):
    """Type for internal handling of the universal request method."""
    GET = 'get',
    POST = 'post',
    PUT = 'put',
    DELETE = 'delete',
    PATCH = 'patch',
    HEAD = 'head'

class ResponseBodyFormat(Enum):
    """Type of the body of the response."""
    JSON = 'json',
    TEXT = 'text',
    # BUFFER = 'buffer',
    NONE = 'none'

@dataclass
class Response:
    """Response type which is returned from any request."""
    body:  Dict | str | None
    status: int
    headers: Dict[str, str]
    duration: float
