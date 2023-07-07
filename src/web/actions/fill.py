from src.web.types import Selector, SelectorOptions
from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Fill(Action):
    """Action Class. Fill an element specified by a selector string with the specified input."""

    def __init__(self, selector: Selector, inp: str, options: SelectorOptions | None = None):
        self.selector = selector
        self.inp = inp
        self.options = options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).fill(self.selector, self.inp, self.options)

    @staticmethod
    def In(selector: Selector, inp: str, options: SelectorOptions | None = None) -> "Fill":
        """Finds the specified selector and will it with the specified input string.

        :param selector: the selector.
        :param inp: the input.
        """
        return Fill(selector, inp, options)
