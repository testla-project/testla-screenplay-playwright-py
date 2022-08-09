# from @testla/screenplay import Actor, Question
from typing import Literal
from abilities.browse_the_web import BrowseTheWeb


class Element(Question):
    """Question Class. Get a specified state for a selector like visible or enabled."""

    def __init__(self, check_mode: Literal['to_be', 'not_to_be'], mode: Literal['visible', 'enabled'], selector: str):
        super.__init__()
        self.check_mode = check_mode
        self.mode = mode
        self.selector = selector
        

    def answered_by(self, actor: Actor) -> bool:
        if self.mode == 'visible':
            # if the ability method is not the expected result there will be an exception
            return BrowseTheWeb.As(actor).check_visibility_state(self.selector, 'visible' if self.check_mode == 'to_be' else 'hidden')
        if self.mode == 'enabled':
            # if the ability method is not the expected result there will be an exception
            return BrowseTheWeb.As(actor).check_enabled_state(self.selector, 'enabled' if self.check_mode == 'to_be' else 'disabled')
        raise RuntimeError('Unknown mode: Element.answered_by')

    @staticmethod
    def to_be_visible(selector: str) -> "Element":
        """Verifies if an element is visible.
        
        :param selector: the selector
        """
        return Element('to_be', 'visible', selector)

    @staticmethod
    def not_to_be_visible(selector: str) -> "Element":
        """Verifies if an element is not visible. Opposite of Element.to_be_visible().
        
        :param selector: the selector
        """
        return Element('not_to_be', 'visible', selector)

    
    @staticmethod
    def to_be_enabled(selector: str) -> "Element":
        """Verifies if an element is enabled.
        
        :param selector: the selector
        """
        return Element('to_be', 'enabled', selector)


    @staticmethod
    def not_to_be_enabled(selector: str) -> "Element":
        """Verifies if an element is not enabled. Opposite of Element.to_be_enabled().
        
        :param selector: the selector
        """
        return Element('not_to_be', 'enabled', selector)
