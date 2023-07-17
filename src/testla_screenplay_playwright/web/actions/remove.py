from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from typing import Literal


class Remove(Action):
    """Action Class.  Remove either Session Storage Items or Local Storage Items from the Browser."""

    def __init__(self, mode: Literal['session_storage', 'local_storage'], payload: str):
        self.mode = mode
        self.payload = payload

    def perform_as(self, actor: Actor) -> None:
        if self.mode == 'session_storage':
            return BrowseTheWeb.As(actor).remove_session_storage_item(self.payload)
        if self.mode == 'local_storage':
            return BrowseTheWeb.As(actor).remove_local_storage_item(self.payload)
        raise RuntimeError('Error: no match for Remove.perform_as()!')

    @staticmethod
    def session_storage_item(key: str) -> "Remove":
        """Remove a session storage item.

        :param key: the key that specifies the item.
        """
        return Remove('session_storage', key)

    @staticmethod
    def local_storage_item(key: str) -> "Remove":
        """Remove a local storage item.

        :param key: the key that specifies the item.
        """
        return Remove('local_storage', key)
