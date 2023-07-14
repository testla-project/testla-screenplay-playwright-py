from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb

class Press(Action):
    """Action Class. Press the specified key(s) on the keyboard."""

    def __init__(self, inp: str):
        self.inp = inp

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).press(self.inp)

    @staticmethod
    def key(inp: str) -> "Press":
        """Press a key on the keyboard. (or multiple keys with +, e.g. Shift+A)

        :param inp: the key(s) to press.
        """
        return Press(inp)
        