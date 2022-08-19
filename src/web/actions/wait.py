from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb
from typing import Literal


class Wait(Action):
    """Action Class. Wait for either a specified loading state or for a selector to become visible/active."""

    def __init__(self, mode: Literal['selector', 'load_state'],
                 payload: str | Literal['domcontentloaded', 'load', 'networkidle']):
        self.mode = mode
        self.payload = payload

    def perform_as(self, actor: Actor) -> object:
        if self.mode is 'selector':
            return BrowseTheWeb.As(actor).wait_for_selector(self.payload)
        if self.mode is 'load_state':
            return BrowseTheWeb.As(actor).wait_for_load_state(self.payload)
        raise RuntimeError('Error: no match for Wait.perform_as()!')

    @staticmethod
    def for_selector(selector: str) -> "Wait":
        """Wait for a specific selector to exist.

        :param selector: the selector.
        """
        return Wait('selector', selector)

    @staticmethod
    def for_load_state(state: Literal['domcontentloaded', 'load', 'networkidle']) -> "Wait":
        """Wait for a specific status of the page.

        :param state: either 'load', 'domcontentloaded' or 'networkidle'.
        """
        return Wait('load_state', state)
