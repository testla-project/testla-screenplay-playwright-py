# from @testla/screenplay import Action, Actor
from typing import List, Literal
from abilities.browse_the_web import BrowseTheWeb

class Hover(Action):
    """Action Class. Hover over an element specified by a selector string."""

    def __init__(self, selector: str, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None):
        super.__init__()
        self.selector = selector
        self.modifiers = modifiers

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).hover(self.selector, self.modifiers)

    @staticmethod
    def over(selector: str, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None) -> "Hover":
        """Hover over an element specified by a selector string.

        :param selector: the selector.
        :param modifiers: Modifier keys to press. Ensures that (only) these modifiers are pressed during the operation.
        """
        return Hover(selector, modifiers)
