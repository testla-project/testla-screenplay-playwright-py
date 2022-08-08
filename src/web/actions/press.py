# from @testla/screenplay import Action, Actor
from abilities.browse_the_web import BrowseTheWeb

class Press(Action):
    """Action Class. Press the specified key(s) on the keyboard."""

    def __init__(self, input: str):
        super.__init__()
        self.input = input

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).press(self.input)

    @staticmethod
    def key(input: str) -> "Press":
        """Press a key on the keyboard. (or multiple keys with +, e.g. Shift+A)

        :param keys: the key(s) to press.
        """
        return Press(input)
        