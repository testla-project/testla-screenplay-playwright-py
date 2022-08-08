# from @testla/screenplay import Action, Actor
from abilities.browse_the_web import BrowseTheWeb

class Click(Action):
    """Action Class. Click on an element specified by a selector string."""

    def __init__(self, selector: str):
        super.__init__()
        self.selector = selector

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).click(self.cookies)

    @staticmethod
    def on(selector: str) -> "Click":
        """Specify which element should be clicked.

        :param selector: the string representing the selector.
        """
        return Click(selector)
