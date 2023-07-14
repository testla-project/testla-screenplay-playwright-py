from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from typing import Literal


class Set(Action):
    """Action Class. Set either Session Storage Items or Local Storage Items on the Browser."""

    def __init__(self, mode: Literal['session_storage', 'local_storage'], payload: object):
        self.mode = mode
        self.payload = payload

    def perform_as(self, actor: Actor) -> object:
        # payload should consist of only one entry: { key: value } 
        key = [*self.payload][0]
        value = self.payload[key]
        if self.mode == 'session_storage':
            return BrowseTheWeb.As(actor).set_session_storage_item(key, value)
        if self.mode == 'local_storage':
            return BrowseTheWeb.As(actor).set_local_storage_item(key, value)
        raise RuntimeError('Error: no match for Remove.perform_as()!')

    @staticmethod
    def session_storage_item(key: str, value: object) -> "Set":
        """Set a session storage item identified by the given key + value, creating a new key/value pair if none existed for key previously.

        :param key: the key that specifies the item.
        :param value: the value of the item.
        """
        return Set('session_storage', { key: value })

    @staticmethod
    def local_storage_item(key: str, value: object) -> "Set":
        """Remove a local storage item.

        :param key: the key that specifies the item.
        :param value: the value of the item.
        """
        return Set('local_storage', { key: value })
