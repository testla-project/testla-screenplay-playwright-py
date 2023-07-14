from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb

class Navigate(Action):
    """Action Class. Navigate to a URL using the specified url string."""

    def __init__(self, url: str):
        self.url = url

    def perform_as(self, actor: Actor) -> object:
        return BrowseTheWeb.As(actor).goto(self.url)

    @staticmethod
    def to(url: str) -> "Navigate":
        """Use the page to navigate to the specified URL.

        :param url: the url which should be accessed.
        """
        return Navigate(url)
