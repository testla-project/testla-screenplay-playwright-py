from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions


class Select(Action):
    """Action Class. Set the value of a Selector of type select to the given option."""
    
    def __init__(self, selector: Selector, value: str | None = None, *, label: str | None = None, index: int | None = None, selector_options: SelectorOptions | None = None):
        self.selector = selector
        self.value = value
        self.label = label
        self.index = index
        self.selector_options = selector_options
        
    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).select_option(self.selector, self.value, label=self.label, index=self.index, selector_options=self.selector_options)
    
    @staticmethod
    def option(selector: Selector, value: str | None = None, *, label: str | None = None, index: int | None = None, selector_options: SelectorOptions | None = None):
        return Select(selector, value, label=label, index=index, selector_options=selector_options)