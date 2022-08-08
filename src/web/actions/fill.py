# from @testla/screenplay import Action, Actor
from abilities.browse_the_web import BrowseTheWeb

class Fill(Action):
    """Action Class. Fill an element specified by a selector string with the specified input."""

    def __init__(self, selector: str, input: str):
        super.__init__()
        self.selector = selector
        self.input = input

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).fill(self.selector, self.input)

    @staticmethod
    def In(selector: str, input: str) -> "Fill":
        """Finds the specified selector and will it with the specified input string.

        :param selector: the selector.
        :param input: the input.
        """
        return Fill(selector, input)
