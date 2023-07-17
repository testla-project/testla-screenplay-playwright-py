from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb

class Clear(Action):
    """Action Class. Remove cookies from the Browser."""

    def perform_as(self, actor: Actor) -> object:
        return BrowseTheWeb.As(actor).clear_cookies()

    @staticmethod
    def cookies() -> "Clear":
        """Clear all browser cookies."""
        return Clear()
