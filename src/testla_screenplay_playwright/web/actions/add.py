from typing import List
from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from playwright.sync_api import Cookie


class Add(Action):
    """Action Class. Add Cookies to the Browser."""

    def __init__(self, cookies: List[Cookie]):
        self.cookies = cookies

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).add_cookies(cookies=self.cookies)

    @staticmethod
    def cookies(cookies: List[Cookie]) -> "Add":
        """Add the specified cookies.
        
        :param cookies: the cookies to add.
        """
        return Add(cookies=cookies)
