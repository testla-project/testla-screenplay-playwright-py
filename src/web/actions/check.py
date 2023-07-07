from src.web.types import Selector, SelectorOptions
from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Check(Action):
    """Action Class. Check a checkbox specified by a selector string."""

    def __init__(self, selector: Selector, options: SelectorOptions | None = None):
        self.selector = selector
        self.options = options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).check_box(self.selector, self.options)

    @staticmethod
    def element(selector: Selector, options: SelectorOptions | None = None) -> "Check":
        """Specify which element should be checked.

        :param selector the string representing the selector.
        """
        return Check(selector, options)
