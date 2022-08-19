from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Type(Action):
    """Action Class. Type specified input into an element specified by a selector."""

    def __init__(self, selector: str, inp: str):
        self.selector = selector
        self.inp = inp

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).type(self.selector, self.inp)

    @staticmethod
    def In(selector: str, inp: str) -> "Type":
        """Finds the specified selector and type in the given input.

        :param selector: the selector.
        :param inp: the input.
        """
        return Type(selector, inp)
