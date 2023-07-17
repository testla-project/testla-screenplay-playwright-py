from testla_screenplay import Action, Actor
from ..abilities.browse_the_web import BrowseTheWeb
from ..types import Selector, SelectorOptions


class DragAndDrop(Action):
    """Action Class. DragAndDrop an element specified by a selector string and drop it on an element specified by another selector string."""

    def __init__(self, source_selector: Selector, target_selector: Selector, source_options: SelectorOptions | None = None, target_options: SelectorOptions | None = None):
        self.source_selector = source_selector
        self.target_selector = target_selector
        self.source_options = source_options
        self.target_options = target_options

    def perform_as(self, actor: Actor) -> None:
        return BrowseTheWeb.As(actor).drag_and_drop(self.source_selector, self.target_selector, source_options=self.source_options, target_options=self.target_options)

    @staticmethod
    def execute(source_selector: Selector, target_selector: Selector, source_options: SelectorOptions | None = None, target_options: SelectorOptions | None = None ) -> "DragAndDrop":
        """Drag the specified source element to the specified target element and drop it.

        :param source_selector: the selector of the source element.
        :param target_selector: the selector of the target element.
        """
        return DragAndDrop(source_selector, target_selector, source_options=source_options, target_options=target_options)
