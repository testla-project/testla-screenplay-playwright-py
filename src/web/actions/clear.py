# from @testla/screenplay import Action, Actor
from ../abilities/BrowseTheWeb import BrowseTheWeb

class Clear(Action):
    """Action Class. Remove cookies from the Browser."""

    def __init__(self):
        super.__init__()

    def perform_as(actor: Actor) -> object:
        return BrowseTheWeb.As(actor).clear_cookies(self.cookies)

    @staticmethod
    def cookies(selector: str) -> "Clear":
        """Clear all browser cookies."""
        return Clear()
