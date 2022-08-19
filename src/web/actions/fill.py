from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Fill(Action):
    """Action Class. Fill an element specified by a selector string with the specified input."""

    def __init__(self, selector: str, inp: str):
        self.selector = selector
        self.inp = inp

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).fill(self.selector, self.inp)

    @staticmethod
    def In(selector: str, inp: str) -> "Fill":
        """Finds the specified selector and will it with the specified input string.

        :param selector: the selector.
        :param inp: the input.
        """
        return Fill(selector, inp)
