from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Check(Action):
    """Action Class. Check a checkbox specified by a selector string."""

    def __init__(self, selector: str):
        self.selector = selector

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).check_box(self.selector)

    @staticmethod
    def element(selector: str) -> "Check":
        """Specify which element should be checked.

        :param selector the string representing the selector.
        """
        return Check(selector)
