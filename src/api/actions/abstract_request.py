from abc import abstractmethod
from typing import Dict
from testla_screenplay import Actor, Action


class ARequest(Action):
    """Abstract parent class for all HTTP request methods. This class extends the testla Action."""
    # HTTP headers to send with the request.
    headers: Dict[str, str] = {}

    @abstractmethod
    def perform_as(self, actor: Actor) -> object:
        pass
