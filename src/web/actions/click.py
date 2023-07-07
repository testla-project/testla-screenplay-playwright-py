from src.web.types import Selector, SelectorOptions
from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Click(Action):
    """Action Class. Click on an element specified by a selector string."""

    def __init__(self, selector: Selector, options: SelectorOptions | None = None):
        self.selector = selector
        self.options = options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).click(self.selector, self.options)

    @staticmethod
    def on(selector: Selector, options: SelectorOptions | None = None) -> "Click":
        """Specify which element should be clicked.

        :param selector: the string representing the selector.
        """
        return Click(selector, options)
