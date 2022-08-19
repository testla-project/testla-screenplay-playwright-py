from testla_screenplay import Action, Actor
from src.web.abilities.browse_the_web import BrowseTheWeb


class Click(Action):
    """Action Class. Click on an element specified by a selector string."""

    def __init__(self, selector: str):
        self.selector = selector

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).click(self.selector)

    @staticmethod
    def on(selector: str) -> "Click":
        """Specify which element should be clicked.

        :param selector: the string representing the selector.
        """
        return Click(selector)
