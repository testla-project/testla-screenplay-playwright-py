from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions


class Type(Action):
    """Action Class. Type specified input into an element specified by a selector."""

    def __init__(self, selector: Selector, inp: str, options: SelectorOptions | None = None):
        self.selector = selector
        self.inp = inp
        self.options = options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).type(self.selector, self.inp, options=self.options)

    @staticmethod
    def In(selector: Selector, inp: str, options: SelectorOptions | None = None) -> "Type":
        """Finds the specified selector and type in the given input.

        :param selector: the selector.
        :param inp: the input.
        """
        return Type(selector, inp, options=options)
