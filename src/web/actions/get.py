# from @testla/screenplay import Action, Actor
from typing import List, Literal
from abilities.browse_the_web import BrowseTheWeb

class Get(Action):
    """Action Class. Get either Cookies, Session Storage Items or Local Storage Items from the Browser."""

    def __init__(self, mode: Literal['cookies', 'session_storage', 'local_storage'], payload: object):
        super.__init__()
        self.mode = mode
        self.payload = payload

    def perform_as(self, actor: Actor) -> object:
        if self.mode is 'cookies':
            return BrowseTheWeb.As(actor).get_cookies(self.payload)
        if self.mode is 'session_storage':
            return BrowseTheWeb.As(actor).get_session_storage_item(self.payload)
        if self.mode is 'local_storage':
            return BrowseTheWeb.As(actor).get_local_storage_item(self.payload)
        raise RuntimeError('Error: no match for Get.perform_as()!')

    @staticmethod
    def cookies(urls: str | List[str] = None) -> "Get":
        """Get the specified cookies.

        :param urls (optional): If URLs are specified, only cookies that affect those URLs are returned. If no URLs are specified, this all cookies are returned.
        """
        return Get('cookies', urls)

    @staticmethod
    def session_storage_item(key: str) -> "Get":
        """Get a session storage item.

        :param key: the key that specifies the item.
        """
        return Get('session_storage', key)

    @staticmethod
    def local_storage_item(key: str) -> "Get":
        """Get a local storage item.

        :param key: the key that specifies the item.
        """
        return Get('local_storage', key)
