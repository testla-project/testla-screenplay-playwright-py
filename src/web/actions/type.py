# from @testla/screenplay import Action, Actor
from abilities.browse_the_web import BrowseTheWeb

class Type(Action):
    """Action Class. Type specified input into an element specified by a selector."""

    def __init__(self, selector: str, input: str):
        super.__init__()
        self.selector = selector
        self.input = input

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).type(self.selector, self.input)

    @staticmethod
    def In(selector: str, input: str) -> "Type":
        """Finds the specified selector and type in the given input.

        :param selector: the selector.
        :param input: the input.
        """
        return Type(selector, input)
