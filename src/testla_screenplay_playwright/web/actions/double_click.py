from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions


class DoubleClick(Action):
    """Action Class. Double Click on an element specified by a selector string."""

    def __init__(self, selector: Selector, options: SelectorOptions | None = None):
        self.selector = selector
        self.options = options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).dblclick(self.selector, options=self.options)

    @staticmethod
    def on(selector: Selector, options: SelectorOptions | None = None) -> "DoubleClick":
        """Specify which element should be clicked.

        :param selector: the string representing the selector.
        """
        return DoubleClick(selector, options=options)
