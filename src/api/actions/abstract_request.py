from abc import ABC, abstractmethod
from typing import Dict
# from @testla/screenplay import Actor, Action


class ARequest(ABC, Action):
    """Abstract parent class for all HTTP request methods. This class extends the testla Action."""
    # HTTP headers to send with the request.
    headers: Dict[str, str] = {}

    @abstractmethod
    def perform_as(actor: Actor) -> object:
        pass