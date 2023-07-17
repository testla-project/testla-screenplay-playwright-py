from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions
from typing import List, Literal


class Hover(Action):
    """Action Class. Hover over an element specified by a selector string."""

    def __init__(self, selector: Selector, options: SelectorOptions | None = None, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None):
        self.selector = selector
        self.options = options
        self.modifiers = modifiers

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).hover(self.selector, options=self.options, modifiers=self.modifiers)

    @staticmethod
    def over(selector: Selector, options: SelectorOptions | None = None, modifiers: List[Literal['Alt', 'Control', 'Meta', 'Shift']] | None = None) -> "Hover":
        """Hover over an element specified by a selector string.

        :param selector: the selector.
        :param modifiers: Modifier keys to press. Ensures that (only) these modifiers are pressed during the operation.
        """
        return Hover(selector, options=options, modifiers=modifiers)
